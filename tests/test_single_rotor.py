import numpy as np
import caddee.api as cd
import lsdo_geo as lg
import m3l
from python_csdl_backend import Simulator
import array_mapper as am
from lsdo_acoustics import GEOMETRY_PATH, IMPORTS_PATH

from lsdo_rotor.core.BEM_caddee.BEM_caddee import BEM, BEMMesh

from lsdo_acoustics import Acoustics
from lsdo_acoustics.core.m3l_models import Lowson, KS, SKM, GL, TotalAircraftNoise

'''
This test script connects the acoustics models to BEM.
The demonstrated case considers 2 flight segments: steady hover and cruise.
The hover tonal noise is computed using the KS model.
The cruise tonal noise is computed using the Lowson model (sort of in edge-wise flight).


NEED TO ADD A-WEIGHTING
67 dBA @ 250 feet below aircraft (Uber Elevate paper)
'''

caddee = cd.CADDEE()
caddee.system_representation = system_rep = cd.SystemRepresentation()
caddee.system_parameterization = system_param = cd.SystemParameterization(system_representation=system_rep)

file_name = GEOMETRY_PATH / 'single_rotor.stp'
spatial_rep = system_rep.spatial_representation
spatial_rep.import_file(file_name=file_name, file_path=str(IMPORTS_PATH))
spatial_rep.refit_geometry(file_name=file_name, file_path=str(IMPORTS_PATH))

'''
======================================== GEOMETRY ========================================
'''

# ==================== ROTOR DISK ====================
prefix = 'rotor'
rotor_disk_primitive_names = list(
    spatial_rep.get_primitives(search_names=['Rotor_disk']).keys()
)
rotor_disk = cd.Rotor(
    name=f'{prefix}_disk',
    spatial_representation=spatial_rep,
    primitive_names=rotor_disk_primitive_names
)
system_rep.add_component(rotor_disk)

# PROJECTIONS
p11 = rotor_disk.project(np.array([0.500, 0.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p12 = rotor_disk.project(np.array([-0.500, 0.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p21 = rotor_disk.project(np.array([0.000, 0.500 , 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p22 = rotor_disk.project(np.array([0.000, -0.500, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
rotor_in_plane_x = am.subtract(p11,p12)
rotor_in_plane_y = am.subtract(p21,p22)
rotor_origin = rotor_disk.project(np.array([0.000, 0.000, 0.000]), direction=np.array([0.,0.,1.]))
system_rep.add_output(f'{prefix}_disk_in_plane_1', quantity=rotor_in_plane_x)
system_rep.add_output(f'{prefix}_disk_in_plane_2', quantity=rotor_in_plane_y)
system_rep.add_output(f'{prefix}_disk_origin', quantity=rotor_origin)

# ==================== ROTOR BLADES ====================
rotor_blade_primitive_names = list(
    spatial_rep.get_primitives(search_names=['Rotor_blades, 0']).keys()
)
rotor_blade = cd.Rotor(
    name=f'{prefix}_blade',
    spatial_representation=spatial_rep,
    primitive_names=rotor_blade_primitive_names
)
system_rep.add_component(rotor_blade)

# PROJECTIONS
le_tip = np.array([-0.032, 0.5, 0.007])
le_root = np.array([-0.014, 0.1, 0.015])
te_tip = np.array([0.032, 0.5, -0.007])
te_root = np.array([0.014, 0.1, -0.015])

offset_x = 0.05
offset_y = 0.05
offset_z = 0.05
num_radial = 40
blade_le = np.linspace(
    le_root + np.array([-offset_x, -offset_y, offset_z]),
    le_tip + np.array([-offset_x, 2*offset_y, offset_z]),
    num_radial
) # array around LE with offsets
blade_te = np.linspace(
    te_root - np.array([-offset_x, offset_y, offset_z]),
    te_tip - np.array([-offset_x, -2*offset_y, offset_z]),
    num_radial
) # array around TE with offsets

p_le = rotor_blade.project(blade_le, direction=np.array([0., 0., -1.]), grid_search_n=50, plot=False) # projection onto LE of BLADE
p_te = rotor_blade.project(blade_te, direction=np.array([0., 0., 1.]), grid_search_n=50, plot=False) # projection onto TE of BLADE

rotor_blade_chord = am.subtract(p_le, p_te) # produces array map of vectors radially, from TE to LE

rotor_disk_le_proj = rotor_disk.project(p_le.evaluate(), direction=np.array([0., 0., -1.]), grid_search_n=50, plot=False) # LE projected onto disk
rotor_disk_te_proj = rotor_disk.project(p_te.evaluate(), direction=np.array([0., 0., 1.]), grid_search_n=50, plot=False) # TE projected onto disk

rotor_v_dist_le = am.subtract(p_le, rotor_disk_le_proj) # vertical distance from LE to disk
rotor_v_dist_te = am.subtract(p_te, rotor_disk_te_proj) # vertical distance from TE to disk
rotor_v_dist_tot = am.subtract(rotor_v_dist_le, rotor_v_dist_te) 

system_rep.add_output(f'{prefix}_blade_chord_length', rotor_blade_chord)
system_rep.add_output(f'{prefix}_blade_twist', rotor_v_dist_tot)

'''
======================================== SYSTEM MODEL ========================================
'''
caddee.system_model = system_model = cd.SystemModel()
design_scenario = cd.DesignScenario(name='single_rotor_test')

# ==================== CRUISE ====================
cruise_model = m3l.Model()
cruise_condition = cd.CruiseCondition(name='cruise')
cruise_condition.atmosphere_model = cd.SimpleAtmosphereModel()

cruise_condition.set_module_input(name='mach_number', val=0.0705)
cruise_condition.set_module_input(name='range', val=40000)
cruise_condition.set_module_input(name='altitude', val=500)
cruise_condition.set_module_input(name='wing_incidence_angle', val=np.deg2rad(0))
cruise_condition.set_module_input(name='pitch_angle', val=np.deg2rad(2), dv_flag=False, lower=np.deg2rad(0), upper=np.deg2rad(5))
cruise_condition.set_module_input(name='observer_location', val=np.array([0, 0, 500]))
ac_states = cruise_condition.evaluate_ac_states()
cruise_model.register_output(ac_states)


# region BEM
rotor_bem_mesh = BEMMesh(
    meshes=dict(
        rotor_in_plane_1=rotor_in_plane_x,
        rotor_in_plane_2=rotor_in_plane_y,
        rotor_origin=rotor_origin
    ),
    airfoil='NACA_4412',
    num_blades=2,
    chord_b_spline_rep=True,
    twist_b_spline_rep=True,
    num_radial=num_radial,
    num_tangential=100,
    use_airfoil_ml=False
)
bem_model = BEM(component=rotor_disk, mesh=rotor_bem_mesh, disk_prefix='rotor_disk', blade_prefix='rotor_blade')
bem_model.set_module_input('rpm', val=5500.)
_, _, dT, dQ, dD, CT = bem_model.evaluate(ac_states=ac_states)
cruise_model.register_output(dT)
cruise_model.register_output(dD)
cruise_model.register_output(CT)
# endregion

# region acoustics
cruise_acoustics = Acoustics(
    aircraft_position = np.array([0.,0.,0])
)

cruise_acoustics.add_observer(
    name='obs1',
    obs_position=np.array([1.85947514, 0., -1.30201851]),
    time_vector=np.array([0., 1.]),
)

lowson_model = Lowson(
    component=rotor_disk,
    mesh=rotor_bem_mesh,
    # mesh=acoustics_mesh,
    acoustics_data=cruise_acoustics,
    disk_prefix='rotor_disk',
    blade_prefix='rotor_blade'
)

cruise_tonal_SPL, cruise_tonal_SPL_A_weighted  = lowson_model.evaluate_tonal_noise(dT, dD, ac_states)
cruise_model.register_output(cruise_tonal_SPL)
cruise_model.register_output(cruise_tonal_SPL_A_weighted)

skm_model = SKM(
    component=rotor_disk,
    mesh=rotor_bem_mesh,
    acoustics_data=cruise_acoustics,
    disk_prefix='rotor_disk',
    blade_prefix='rotor_blade'
)
cruise_broadband_SPL, cruise_broadband_SPL_A_weighted = skm_model.evaluate_broadband_noise(ac_states, CT)
cruise_model.register_output(cruise_broadband_SPL)
cruise_model.register_output(cruise_broadband_SPL_A_weighted)

total_noise_model = TotalAircraftNoise(
    acoustics_data=cruise_acoustics,
    component_list=[rotor_disk],
)
noise_components = [cruise_tonal_SPL, cruise_broadband_SPL]

cruise_total_SPL = total_noise_model.evaluate(noise_components)
cruise_model.register_output(cruise_total_SPL)
# endregion

cruise_condition.add_m3l_model('cruise_model', cruise_model)
design_scenario.add_design_condition(cruise_condition)

# ==================== HOVER ====================
hover_model = m3l.Model()
hover_condition = cd.HoverCondition(name='hover')
hover_condition.atmosphere_model = cd.SimpleAtmosphereModel()

hover_condition.set_module_input(name='altitude', val=500)
hover_condition.set_module_input(name='observer_location', val=np.array([0, 0, 500]))
hover_condition.set_module_input(name='hover_time', val=120.)
ac_states = hover_condition.evaluate_ac_states()
hover_model.register_output(ac_states)

# region BEM
rotor_bem_mesh = BEMMesh(
    meshes=dict(
        rotor_in_plane_1=rotor_in_plane_x,
        rotor_in_plane_2=rotor_in_plane_y,
        rotor_origin=rotor_origin
    ),
    airfoil='NACA_4412',
    num_blades=4,
    chord_b_spline_rep=True,
    twist_b_spline_rep=True,
    num_radial=num_radial,
    num_tangential=30,
    mesh_units='ft',
    use_airfoil_ml=False
)
bem_model = BEM(component=rotor_disk, mesh=rotor_bem_mesh, disk_prefix='rotor_disk', blade_prefix='rotor_blade')
bem_model.set_module_input('rpm', val=5500.)
_, _, dT, dQ, dD, CT = bem_model.evaluate(ac_states=ac_states)
hover_model.register_output(dT)
hover_model.register_output(dD)
hover_model.register_output(CT)
# endregion

# region acoustics
hover_acoustics = Acoustics(
    aircraft_position = np.array([0.,0.,0])
)

hover_acoustics.add_observer(
    name='obs1',
    # obs_position=np.array([1.85947514, 0., -1.30201851]),
    obs_position=np.array([0., 0., -76.2]),
    # obs_position=np.array([1.91, 0., 0.]),
    time_vector=np.array([0., 1.]),
)


ks_model = KS(
    component=rotor_disk,
    mesh=rotor_bem_mesh,
    acoustics_data=hover_acoustics,
    disk_prefix='rotor_disk',
    blade_prefix='rotor_blade'
)
hover_tonal_SPL, hover_tonal_SPL_A_weighted = ks_model.evaluate_tonal_noise(dT, dD, ac_states)
hover_model.register_output(hover_tonal_SPL)
hover_model.register_output(hover_tonal_SPL_A_weighted)

gl_model = GL(
    component=rotor_disk,
    mesh=rotor_bem_mesh,
    acoustics_data=hover_acoustics,
    disk_prefix='rotor_disk',
    blade_prefix='rotor_blade'
)
hover_broadband_SPL, hover_broadband_SPL_A_weighted = gl_model.evaluate_broadband_noise(ac_states, CT)
hover_model.register_output(hover_broadband_SPL)
hover_model.register_output(hover_broadband_SPL_A_weighted)

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
# caddee_csdl_model.connect(
#     'system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model.rpm',
#     'system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.rpm'
# )

# caddee_csdl_model.connect(
#     'system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model.rpm',
#     'system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model.rpm'
# )

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