import numpy as np
import caddee.api as cd
import lsdo_geo as lg
import m3l
from python_csdl_backend import Simulator
from lsdo_acoustics import GEOMETRY_PATH, IMPORTS_PATH

from lsdo_rotor import BEM, BEMParameters

from lsdo_acoustics import Acoustics, Lowson, SKM, GL, TotalAircraftNoise

'''
This test script connects the acoustics models to BEM.
The demonstrated case considers the hover flight segment
The hover tonal noise is computed using the Lowson model (tonal) and GL model (broadband)
'''

caddee = cd.CADDEE()
file_name = GEOMETRY_PATH / 'single_rotor.stp'
geometry = lg.import_geometry(file_name, parallelize=True)
geometry.refit(parallelize=True)
# geometry.plot()
'''
======================================== GEOMETRY ========================================
'''

rotor_disk = geometry.declare_component(component_name='wing', b_spline_search_names=['Rotor_disk'])
rotor_blade = geometry.declare_component(component_name='blade_0', b_spline_search_names=['Rotor_blades, 0'])

rotor_blade_parameters = cd.BladeParameters(
    blade_component=rotor_blade,
    point_on_leading_edge=np.array([-0.062, 0.30, 0.007])
) 

num_radial = 30
rotor_disk_mesh = cd.make_rotor_mesh(
    geometry=geometry,
    num_radial=num_radial,
    disk_component=rotor_disk,
    origin=np.array([0., 0., 0.000]),
    y1=np.array([0.500, 0.000, 0.000]),
    y2=np.array([-0.500, 0.000, 0.000]),
    z1=np.array([0.000, 0.500 , 0.000]),
    z2=np.array([0.000, -0.500, 0.000]),
    blade_geometry_parameters=[rotor_blade_parameters],
    plot=False,
)

'''
======================================== SYSTEM MODEL ========================================
'''
caddee = cd.CADDEE()
system_model = m3l.Model()

rotor_disk_mesh.radius = system_model.create_input('radius', val=1)

# ==================== HOVER ====================
hover_condition = cd.HoverCondition(name='hover')

hover_altitude = system_model.create_input(name='hover_altitude', val=100)
hover_time = system_model.create_input(name='hover_time', val=120.)
hover_ac_states, hover_atmosphere = hover_condition.evaluate(hover_time=hover_time, altitude=hover_altitude)

system_model.register_output(hover_ac_states)
system_model.register_output(hover_atmosphere)

bem_rotor_parameters = BEMParameters(
    num_blades=3,
    num_radial=num_radial,
    num_tangential=50,
    airfoil='NACA_4412',
    use_custom_airfoil_ml=True,
    mesh_units='m',
)

# region BEM
rpm = system_model.create_input('hover_rpm', val=5500.)

hover_bem_model = BEM(name='hover_bem', BEM_parameters=bem_rotor_parameters, num_nodes=1)
hover_bem_outputs = hover_bem_model.evaluate(ac_states=hover_ac_states, atmosphere=hover_atmosphere, rpm=rpm, rotor_radius=rotor_disk_mesh.radius,
                                 thrust_origin=rotor_disk_mesh.thrust_origin, thrust_vector=rotor_disk_mesh.thrust_vector,
                                 blade_chord=rotor_disk_mesh.chord_profile, blade_twist=rotor_disk_mesh.twist_profile)
system_model.register_output(hover_bem_outputs)

# endregion

# region acoustics
hover_acoustics = Acoustics(
    aircraft_position = np.array([0.,0.,0.])
)
observer_mode = 'single'

# # ==== SINGLE OBSERVER ====
if observer_mode == 'single':
    altitude = 100.
    hover_acoustics.add_observer(
        name='obs1',
        obs_position=np.array([0., 0., altitude]),
        time_vector=np.array([0.]),
    )
elif observer_mode == 'directivity':
    obs_radius = 100.
    num_observers = 37 * 2
    theta = np.linspace(0, 2*np.pi, num_observers)
    z = obs_radius * np.cos(theta)
    x = obs_radius * np.sin(theta)

    obs_position_array = np.zeros((num_observers, 3))
    obs_position_array[:,0] = x
    obs_position_array[:,2] = z

    for i in range(num_observers):
        hover_acoustics.add_observer(
            name=f'obs_{i}',
            obs_position=obs_position_array[i,:],
            time_vector=np.array([0.])
        )

Lowson_model = Lowson(
    name='hover_Lowson_model',
    num_nodes=1,
    rotor_parameters=bem_rotor_parameters,
    acoustics_data=hover_acoustics,
)
hover_tonal_SPL, hover_tonal_SPL_A_weighted = Lowson_model.evaluate_tonal_noise(hover_bem_outputs.dT, hover_bem_outputs.dD, hover_ac_states,
                                                                                   rpm=rpm, rotor_origin=rotor_disk_mesh.thrust_origin,
                                                                                   thrust_vector=rotor_disk_mesh.thrust_vector, 
                                                                                   rotor_radius=rotor_disk_mesh.radius, altitude=hover_altitude,
                                                                                #    in_plane_ex=rotor_disk_mesh.in_plane_2,
                                                                                   chord_length=rotor_disk_mesh.chord_profile, phi_profile=hover_bem_outputs.phi)
system_model.register_output(hover_tonal_SPL)
system_model.register_output(hover_tonal_SPL_A_weighted)


SKM_model = SKM(
    name='hover_SKM_model',
    num_nodes=1, 
    rotor_parameters=bem_rotor_parameters,
    acoustics_data=hover_acoustics,
)
hover_broadband_SPL, hover_broadband_SPL_A_weighted = SKM_model.evaluate_broadband_noise(hover_ac_states, hover_bem_outputs.C_T, rpm=rpm,
                                                                                           disk_origin=rotor_disk_mesh.thrust_origin,
                                                                                           thrust_vector=rotor_disk_mesh.thrust_vector,
                                                                                           radius=rotor_disk_mesh.radius, chord_length=rotor_disk_mesh.chord_profile)
system_model.register_output(hover_broadband_SPL)
system_model.register_output(hover_broadband_SPL_A_weighted)

total_noise_model = TotalAircraftNoise(
    name='hover_total_noise',
    acoustics_data=hover_acoustics,
)
noise_components = [hover_tonal_SPL, hover_broadband_SPL]
noise_components_A = [hover_tonal_SPL_A_weighted, hover_broadband_SPL_A_weighted]

hover_total_SPL, hover_total_SPL_A_weighted = total_noise_model.evaluate(noise_components, A_weighted_noise_components=noise_components_A)
system_model.register_output(hover_total_SPL)
system_model.register_output(hover_total_SPL_A_weighted)
# endregion

csdl_model = system_model.assemble_csdl()

sim = Simulator(csdl_model, analytics=True, display_scripts=True)
sim.run()
print('\n')
print('Hover Lowson tonal SPL')
print(sim['hover_Lowson_model_Lowson_tonal_model.hover_Lowson_model_Lowson_tonal_model_tonal_spl'])
print('\n')
print('Hover Lowson A-weighted tonal SPL')
print(sim['hover_Lowson_model_Lowson_tonal_model.hover_Lowson_model_Lowson_tonal_model_tonal_spl_A_weighted'])
print('\n')
print('Hover SKM broadband_spl')
print(sim['hover_SKM_model_SKM_broadband_model.hover_SKM_model_SKM_broadband_model_broadband_spl'])
print('\n')
print('Hover SKM broadband_spl_A_weighted')
print(sim['hover_SKM_model_SKM_broadband_model.hover_SKM_model_SKM_broadband_model_broadband_spl_A_weighted'])
print('\n')
print('Hover total_spl', sim['hover_total_noise.total_spl'])
print('Hover A_weighted_total_spl', sim['hover_total_noise.A_weighted_total_spl'])

print('\n')

if observer_mode == 'directivity':

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    theta_plot = np.linspace(np.pi/2, -3*np.pi/2, num_observers)
    ax.plot(theta_plot, sim['hover_Lowson_model_Lowson_tonal_model.lowson_spl_model.tonal_spl_uns'].reshape((num_observers,)), label='Hover (Default Lowson)')
    ax.plot(theta_plot, sim['hover_Lowson_model_Lowson_tonal_model.lowson_spl_model.tonal_spl_Sears'].reshape((num_observers,)), label='Hover (Sears)')
    ax.set_rlabel_position(-120)

    ax.grid(True)
    plt.legend(loc='best')
    plt.title('SPL distribution in hover and edgewise flight')
    plt.show()


