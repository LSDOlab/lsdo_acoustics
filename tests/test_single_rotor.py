import numpy as np
import caddee.api as cd
import lsdo_geo as lg
import m3l
from python_csdl_backend import Simulator
from lsdo_acoustics import GEOMETRY_PATH, IMPORTS_PATH

from lsdo_rotor import BEM, BEMParameters



from lsdo_acoustics import Acoustics, Lowson, KS, SKM, GL, TotalAircraftNoise

'''
This test script connects the acoustics models to BEM.
The demonstrated case considers 2 flight segments: steady hover and cruise.
The hover tonal noise is computed using the KS model.
The cruise tonal noise is computed using the Lowson model (sort of in edge-wise flight).


NEED TO ADD A-WEIGHTING
67 dBA @ 250 feet below aircraft (Uber Elevate paper)
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

# ==================== CRUISE ====================
cruise_condition = cd.CruiseCondition(
    name='cruise',
    num_nodes=1,
)

mach_number = system_model.create_input('mach_number', val=0.0705)
altitude = system_model.create_input('cruise_altitude', val=500)
pitch_angle = system_model.create_input('pitch_angle', val=0)
range = system_model.create_input('cruise_range', val=40000)

ac_states, atmosphere = cruise_condition.evaluate(
    mach_number=mach_number, 
    pitch_angle=pitch_angle, 
    altitude=altitude, 
    cruise_range=range
)
system_model.register_output(ac_states)
system_model.register_output(atmosphere)


bem_rotor_parameters = BEMParameters(
    num_blades=3,
    num_radial=num_radial,
    num_tangential=50,
    airfoil='NACA_4412',
    use_custom_airfoil_ml=True,
    mesh_units='m',
)

rpm = system_model.create_input('rpm', val=5500.)

bem_model = BEM(name='test_bem', BEM_parameters=bem_rotor_parameters, num_nodes=1)
bem_outputs = bem_model.evaluate(ac_states=ac_states, atmosphere=atmosphere, rpm=rpm, rotor_radius=rotor_disk_mesh.radius,
                                 thrust_origin=rotor_disk_mesh.thrust_origin, thrust_vector=rotor_disk_mesh.thrust_vector,
                                 blade_chord=rotor_disk_mesh.chord_profile, blade_twist=rotor_disk_mesh.twist_profile)

system_model.register_output(bem_outputs)

# region acoustics
cruise_acoustics = Acoustics(
    aircraft_position = np.array([0.,0.,100.])
)

cruise_acoustics.add_observer(
    name='obs1',
    obs_position=np.array([0., 0., 0.]),
    time_vector=np.array([0., 1.]),
)


lowson_model = Lowson(
    name='test_lowson',
    num_nodes=1,
    rotor_parameters=bem_rotor_parameters,
    acoustics_data=cruise_acoustics,
)

cruise_tonal_SPL, cruise_tonal_SPL_A_weighted  = lowson_model.evaluate_tonal_noise(bem_outputs.dT, bem_outputs.dD, ac_states,
                                                                                   rpm=rpm, rotor_origin=rotor_disk_mesh.thrust_origin,
                                                                                   thrust_vector=rotor_disk_mesh.thrust_vector, 
                                                                                   rotor_radius=rotor_disk_mesh.radius, altitude=altitude,
                                                                                   in_plane_ex=rotor_disk_mesh.in_plane_2,
                                                                                   chord_length=rotor_disk_mesh.chord_profile, phi_profile=bem_outputs.phi)
system_model.register_output(cruise_tonal_SPL)
system_model.register_output(cruise_tonal_SPL_A_weighted)



skm_model = SKM(
    name='test_skm',
    num_nodes=1,
    rotor_parameters=bem_rotor_parameters,
    acoustics_data=cruise_acoustics,
)
cruise_broadband_SPL, cruise_broadband_SPL_A_weighted = skm_model.evaluate_broadband_noise(ac_states, bem_outputs.C_T, rpm=rpm,
                                                                                           disk_origin=rotor_disk_mesh.thrust_origin,
                                                                                           thrust_vector=rotor_disk_mesh.thrust_vector,
                                                                                           radius=rotor_disk_mesh.radius, chord_length=rotor_disk_mesh.chord_profile)
system_model.register_output(cruise_broadband_SPL)
system_model.register_output(cruise_broadband_SPL_A_weighted)



total_noise_model = TotalAircraftNoise(
    name='test_total_noise',
    acoustics_data=cruise_acoustics,
)
noise_components = [cruise_tonal_SPL, cruise_broadband_SPL]
noise_components_A = [cruise_tonal_SPL_A_weighted, cruise_broadband_SPL_A_weighted]

cruise_total_SPL, cruise_total_SPL_A_weighted = total_noise_model.evaluate(noise_components, A_weighted_noise_components=noise_components_A)
system_model.register_output(cruise_total_SPL)
system_model.register_output(cruise_total_SPL_A_weighted)
# endregion

# ==================== HOVER ====================
hover_condition = cd.HoverCondition(name='hover')

hover_altitude = system_model.create_input(name='hover_altitude', val=100)
hover_time = system_model.create_input(name='hvoer_time', val=120.)
hover_ac_states, hover_atmosphere = hover_condition.evaluate(hover_time=hover_time, altitude=hover_altitude)

system_model.register_output(hover_ac_states)
system_model.register_output(hover_atmosphere)

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
    aircraft_position = np.array([0.,0.,100.])
)

hover_acoustics.add_observer(
    name='obs1',
    obs_position=np.array([100., 0., 0.]),
    time_vector=np.array([0.]),
)


ks_model = Lowson(
    name='hover_Lowson_model',
    num_nodes=1,
    rotor_parameters=bem_rotor_parameters,
    acoustics_data=hover_acoustics,
)
hover_tonal_SPL, hover_tonal_SPL_A_weighted = ks_model.evaluate_tonal_noise(hover_bem_outputs.dT, hover_bem_outputs.dD, hover_ac_states,
                                                                                   rpm=rpm, rotor_origin=rotor_disk_mesh.thrust_origin,
                                                                                   thrust_vector=rotor_disk_mesh.thrust_vector, 
                                                                                   rotor_radius=rotor_disk_mesh.radius, altitude=altitude,
                                                                                   in_plane_ex=rotor_disk_mesh.in_plane_2,
                                                                                   chord_length=rotor_disk_mesh.chord_profile, phi_profile=hover_bem_outputs.phi)
system_model.register_output(hover_tonal_SPL)
system_model.register_output(hover_tonal_SPL_A_weighted)




gl_model = GL(
    name='hover_GL_model',
    num_nodes=1, 
    rotor_parameters=bem_rotor_parameters,
    acoustics_data=hover_acoustics,
)
hover_broadband_SPL, hover_broadband_SPL_A_weighted = gl_model.evaluate_broadband_noise(hover_ac_states, bem_outputs.C_T, rpm=rpm,
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


csdl_model = system_model.assemble_csdl()

sim = Simulator(csdl_model, analytics=True)
sim.run()
print('Lowson tonal_spl_A_weighted', sim['test_lowson_Lowson_tonal_model.tonal_spl_A_weighted'])
print('Lowson tonal_spl', sim['test_lowson_Lowson_tonal_model.tonal_spl'])
print('SKM broadband_spl_A_weighted', sim['test_skm_SKM_broadband_model.broadband_spl_A_weighted'])
print('Edgewise total_spl', sim['test_total_noise.total_spl'])
print('Edgewise A_weighted_total_spl', sim['test_total_noise.A_weighted_total_spl'])
print('\n')
print('Hover Lowson tonal_spl_A_weighted', sim['hover_Lowson_model_Lowson_tonal_model.tonal_spl_A_weighted'])
print('Hover Lowson tonal_spl', sim['hover_Lowson_model_Lowson_tonal_model.tonal_spl'])
print('Hover GL broadband_spl_A_weighted', sim['hover_GL_model_GL_broadband_model.broadband_spl_A_weighted'])
print('Hover GL broadband_spl', sim['hover_GL_model_GL_broadband_model.broadband_spl'])
print('Hover total_spl', sim['hover_total_noise.total_spl'])
print('Hover A_weighted_total_spl', sim['hover_total_noise.A_weighted_total_spl'])

print('\n')
print(sim['test_bem.T'])
exit()

# skm_model = SKM(
#     component=rotor_disk,
#     mesh=rotor_bem_mesh,
#     acoustics_data=cruise_acoustics
# )
# hover_broadband_SPL = skm_model.evaluate_broadband_noise(ac_states, CT)
# hover_model.register_output(cruise_broadband_SPL)

total_noise_model = TotalAircraftNoise(
    acoustics_data=hover_acoustics,
    component_list=[rotor_disk],
)
noise_components = [hover_tonal_SPL, hover_broadband_SPL]
A_weighted_noise_components = [hover_tonal_SPL_A_weighted, hover_broadband_SPL_A_weighted]

hover_total_SPL, hover_total_SPL_A_weighted = total_noise_model.evaluate(noise_components, A_weighted_noise_components)
hover_model.register_output(hover_total_SPL)
hover_model.register_output(hover_total_SPL_A_weighted)
# endregion

hover_condition.add_m3l_model('hover_model', hover_model)
design_scenario.add_design_condition(hover_condition)

system_model.add_design_scenario(design_scenario=design_scenario)
caddee_csdl_model = caddee.assemble_csdl()




# =================== CONNECTIONS ===================
caddee_csdl_model.connect(
    'system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model.rpm',
    'system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model.rpm'
)

caddee_csdl_model.connect(
    'system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model.in_plane_ex',
    'system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model.in_plane_ex'
)

caddee_csdl_model.connect(
    'system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model.rpm',
    'system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.rpm'
)

caddee_csdl_model.connect(
    'system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model.rpm',
    'system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.rpm'
)

caddee_csdl_model.connect(
    'system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model.rpm',
    'system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model.rpm'
)

caddee_csdl_model.connect(
    'system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.cruise_altitude',
    'system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model.altitude'
)

caddee_csdl_model.connect(
    'system_model.single_rotor_test.hover.hover.hover_ac_states_operation.hover_altitude',
    'system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model.altitude'
)

caddee_csdl_model.connect(
    'system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.phi_bracketed_search_group.phi_distribution',
    'system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.phi'
)

memory_debug = False
if memory_debug:
    import csdl
    m = csdl.Model()
    for i in range(10):
        caddee_csdl_model = caddee.assemble_csdl()
        m.add(caddee_csdl_model, promotes=[])
    sim = Simulator(m, analytics=True)

else:
    sim = Simulator(caddee_csdl_model, analytics=True, display_scripts=True, name='single_rotor')
    sim.run()
    # sim.check_totals()
    # print(sim['system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model.thrust_vector'])