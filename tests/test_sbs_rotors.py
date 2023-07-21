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
This test script sets up two side-by-side rotors of 0.5 feet diameter, separated by 4 feet.
We consider 2 flight segments: steady hover and cruise.

We use this test case to assess cumulative noise from multiple rotors.
'''

caddee = cd.CADDEE()
caddee.system_representation = system_rep = cd.SystemRepresentation()
caddee.system_parameterization = system_param = cd.SystemParameterization(system_representation=system_rep)

file_name = GEOMETRY_PATH / 'side_by_side_rotors.stp'
spatial_rep = system_rep.spatial_representation
spatial_rep.import_file(file_name=file_name, file_path=str(IMPORTS_PATH))
spatial_rep.refit_geometry(file_name=file_name, file_path=str(IMPORTS_PATH))

'''
======================================== GEOMETRY ========================================
Rotor 1: + Y direction
Rotor 2: - Y direction
'''
# ================================ ROTOR 1 DISK ================================
rotor_1_disk_primitive_names = list(
    spatial_rep.get_primitives(search_names=['Rotor1_disk']).keys()
)
rotor_1_disk = cd.Rotor(
    name='rotor_1_disk',
    spatial_representation=spatial_rep,
    primitive_names=rotor_1_disk_primitive_names
)
system_rep.add_component(rotor_1_disk)

p11 = rotor_1_disk.project(np.array([2., 2., 1.]), direction=np.array([0., 0., 1.]), plot=False)
p12 = rotor_1_disk.project(np.array([0., 2., 1.]), direction=np.array([0., 0., 1.]), plot=False)
p21 = rotor_1_disk.project(np.array([1., 3., 1.]), direction=np.array([0., 0., 1.]), plot=False)
p22 = rotor_1_disk.project(np.array([1., 1., 1.]), direction=np.array([0., 0., 1.]), plot=False)
rotor_1_origin = rotor_1_disk.project(np.array([1., 2., 1.]), direction=np.array([0., 0., 1.]))
rotor_1_in_plane_x = am.subtract(p11, p12)
rotor_1_in_plane_y = am.subtract(p21, p22)
system_rep.add_output('rotor_1_disk_in_plane_1', quantity=rotor_1_in_plane_x)
system_rep.add_output('rotor_1_disk_in_plane_2', quantity=rotor_1_in_plane_y)
system_rep.add_output('rotor_1_disk_origin', quantity=rotor_1_origin)

# ================================ ROTOR 1 BLADE ================================
rotor_1_blade_primitive_names = list(
    spatial_rep.get_primitives(search_names=['Rotor1_blades, 0']).keys()
)
rotor_1_blade = cd.Rotor(
    name='rotor_1_blade',
    spatial_representation=spatial_rep,
    primitive_names=rotor_1_blade_primitive_names
)
system_rep.add_component(rotor_1_blade)

le_tip = np.array([0.937, 3.000, 1.015])
le_root = np.array([0.973, 2.200, 1.029])
te_tip = np.array([1.063, 3.000, 0.985])
te_root = np.array([1.027, 2.200, 0.971])

offset_x = 0.05
offset_y = 0.05
offset_z = 0.05
num_radial=40
blade_1_le = np.linspace(
    le_root + np.array([-offset_x, -offset_y, offset_z]),
    le_tip + np.array([-offset_x, 2*offset_y, offset_z]),
    num_radial
)
blade_1_te = np.linspace(
    te_root + np.array([offset_x, -offset_y, -offset_z]),
    te_tip + np.array([offset_x, 2*offset_y, -offset_z]),
    num_radial
)
p_b1_le = rotor_1_blade.project(blade_1_le, direction=np.array([0., 0., -1.]), grid_search_n=50, plot=False)
p_b1_te = rotor_1_blade.project(blade_1_te, direction=np.array([0., 0., 1.]), grid_search_n=50, plot=False)

rotor_1_blade_chord = am.subtract(p_b1_le, p_b1_te)

rotor_1_disk_le_proj = rotor_1_disk.project(p_b1_le.evaluate(), direction=np.array([0.,0.,-1.]), grid_search_n=50, plot=False)
rotor_1_disk_te_proj = rotor_1_disk.project(p_b1_te.evaluate(), direction=np.array([0.,0.,1.]), grid_search_n=50, plot=False)

rotor_1_v_dist_le = am.subtract(p_b1_le, rotor_1_disk_le_proj)
rotor_1_v_dist_te = am.subtract(p_b1_te, rotor_1_disk_te_proj)
rotor_1_v_dist_tot = am.subtract(rotor_1_v_dist_le, rotor_1_v_dist_te)

system_rep.add_output('rotor_1_blade_chord_length', rotor_1_blade_chord)
system_rep.add_output('rotor_1_blade_twist', rotor_1_v_dist_tot)

# ================================ ROTOR 2 DISK ================================
rotor_2_disk_primitive_names = list(
    spatial_rep.get_primitives(search_names=['Rotor2_disk']).keys()
)
rotor_2_disk = cd.Rotor(
    name='rotor_2_disk',
    spatial_representation=spatial_rep,
    primitive_names=rotor_2_disk_primitive_names
)
system_rep.add_component(rotor_2_disk)
p11 = rotor_2_disk.project(np.array([2., -2., 1.]), direction=np.array([0., 0., 1.]), plot=False)
p12 = rotor_2_disk.project(np.array([0., -2., 1.]), direction=np.array([0., 0., 1.]), plot=False)
p21 = rotor_2_disk.project(np.array([1., -1., 1.]), direction=np.array([0., 0., 1.]), plot=False)
p22 = rotor_2_disk.project(np.array([1., -3., 1.]), direction=np.array([0., 0., 1.]), plot=False)
rotor_2_origin = rotor_2_disk.project(np.array([1., -2., 1.]), direction=np.array([0., 0., 1.]))
rotor_2_in_plane_x = am.subtract(p11, p12)
rotor_2_in_plane_y = am.subtract(p21, p22)
system_rep.add_output('rotor_2_disk_in_plane_1', quantity=rotor_2_in_plane_x)
system_rep.add_output('rotor_2_disk_in_plane_2', quantity=rotor_2_in_plane_y)
system_rep.add_output('rotor_2_disk_origin', quantity=rotor_2_origin)

# ================================ ROTOR 2 BLADES ================================
rotor_2_blade_primitive_names = list(
    spatial_rep.get_primitives(search_names=['Rotor2_blades, 0']).keys()
)
rotor_2_blade = cd.Rotor(
    name='rotor_2_blades',
    spatial_representation=spatial_rep,
    primitive_names=rotor_2_blade_primitive_names
)
system_rep.add_component(rotor_2_blade)

le_tip = np.array([0.937, -3.000, 1.015])
le_root = np.array([0.973, -2.200, 1.029])
te_tip = np.array([1.063, -3.000, 0.985])
te_root = np.array([1.027, -2.200, 0.971])

offset_x = 0.05
offset_y = 0.05
offset_z = 0.05
num_radial=40
blade_2_le = np.linspace(
    le_root + np.array([-offset_x, offset_y, offset_z]),
    le_tip + np.array([-offset_x, -2*offset_y, offset_z]),
    num_radial
)
blade_2_te = np.linspace(
    te_root + np.array([offset_x, offset_y, -offset_z]),
    te_tip + np.array([offset_x, -2*offset_y, -offset_z]),
    num_radial
)
p_b2_le = rotor_2_blade.project(blade_2_le, direction=np.array([0., 0., -1.]), grid_search_n=50, plot=False)
p_b2_te = rotor_2_blade.project(blade_2_te, direction=np.array([0., 0., 1.]), grid_search_n=50, plot=False)

rotor_2_blade_chord = am.subtract(p_b2_le, p_b2_te)

rotor_2_disk_le_proj = rotor_2_disk.project(p_b2_le.evaluate(), direction=np.array([0.,0.,-1.]), grid_search_n=50, plot=False)
rotor_2_disk_te_proj = rotor_2_disk.project(p_b2_te.evaluate(), direction=np.array([0.,0.,1.]), grid_search_n=50, plot=False)

rotor_2_v_dist_le = am.subtract(p_b2_le, rotor_2_disk_le_proj)
rotor_2_v_dist_te = am.subtract(p_b2_te, rotor_2_disk_te_proj)
rotor_2_v_dist_tot = am.subtract(rotor_2_v_dist_le, rotor_2_v_dist_te)

system_rep.add_output('rotor_2_blade_chord_length', rotor_2_blade_chord)
system_rep.add_output('rotor_2_blade_twist', rotor_2_v_dist_tot)

# exit()

'''
======================================== SYSTEM MODEL ========================================
TWO FLIGHT CASES: HOVER AND CRUISE
'''
# ================================ HOVER ================================
caddee.system_model = system_model = cd.SystemModel()

design_scenario = cd.DesignScenario(name='hover_test')
hover_model = m3l.Model()
hover_condition = cd.HoverCondition(name="hover")
hover_condition.atmosphere_model = cd.SimpleAtmosphereModel()

hover_condition.set_module_input(name='altitude', val=500)
hover_condition.set_module_input(name='observer_location', val=np.array([0, 0, 500]))
hover_condition.set_module_input(name='hover_time', val=120.)

ac_states = hover_condition.evaluate_ac_states()
hover_model.register_output(ac_states)

'''
================================ BEM MODELS ================================
'''
rotor_1_bem_mesh = BEMMesh(
    meshes=dict(
        rotor_1_in_plane_x=rotor_1_in_plane_x,
        rotor_1_in_plane_y=rotor_1_in_plane_y,
        rotor_1_origin=rotor_1_origin
    ),
    airfoil='NACA_4412',
    num_blades=3,
    chord_b_spline_rep=True,
    twist_b_spline_rep=True,
    num_radial=num_radial,
    num_tangential=30
)
bem_model_1 = BEM(component=rotor_1_disk, mesh=rotor_1_bem_mesh, disk_prefix='rotor_1_disk', blade_prefix='rotor_1_blade')
bem_model_1.set_module_input('rpm', val=1350.)
_, _, dT_1, _, dD_1, CT_1 = bem_model_1.evaluate(ac_states=ac_states)

hover_model.register_output(dT_1)
hover_model.register_output(dD_1)

rotor_2_bem_mesh = BEMMesh(
    meshes=dict(
        rotor_2_in_plane_x=rotor_2_in_plane_x,
        rotor_2_in_plane_y=rotor_2_in_plane_y,
        rotor_2_origin=rotor_2_origin
    ),
    airfoil='NACA_4412',
    num_blades=3,
    chord_b_spline_rep=True,
    twist_b_spline_rep=True,
    num_radial=num_radial,
    num_tangential=30
)
bem_model_2 = BEM(component=rotor_2_disk, mesh=rotor_2_bem_mesh, disk_prefix='rotor_2_disk', blade_prefix='rotor_2_blade')
bem_model_2.set_module_input('rpm', val=1350.)
_, _, dT_2, _, dD_2, CT_2 = bem_model_2.evaluate(ac_states=ac_states)

hover_model.register_output(dT_2)
hover_model.register_output(dD_2)


hover_acoustics = Acoustics(
    aircraft_position=np.array([0.,0.,250*.3048])
)

hover_acoustics.add_observer(
    name='obs1',
    obs_position=np.array([0., 0., 0.]),
    time_vector=np.array([0., 1.])
)

hover_acoustics.setup_directivity_plot(
    name='ground_dir',
    center_point=np.array([0.,0.,0.]),
    radius=10.,
)

ks_model_rotor_1 = KS(
    component=rotor_1_disk,
    mesh=rotor_1_bem_mesh,
    acoustics_data=hover_acoustics,
    disk_prefix='rotor_1_disk',
    blade_prefix='rotor_1_blade'
)
hover_tonal_SPL_1, hover_tonal_SPL_A_weighted_1 = ks_model_rotor_1.evaluate_tonal_noise(dT_1, dD_1, ac_states)
hover_model.register_output(hover_tonal_SPL_1)
hover_model.register_output(hover_tonal_SPL_A_weighted_1)

gl_model_rotor_1 = GL(
    component=rotor_1_disk,
    mesh=rotor_1_bem_mesh,
    acoustics_data=hover_acoustics,
    disk_prefix='rotor_1_disk',
    blade_prefix='rotor_1_blade'
)
hover_broadband_SPL_1, hover_broadband_SPL_A_weighted_1 = gl_model_rotor_1.evaluate_broadband_noise(ac_states, CT_1)
hover_model.register_output(hover_broadband_SPL_1)
hover_model.register_output(hover_broadband_SPL_A_weighted_1)

ks_model_rotor_2 = KS(
    component=rotor_2_disk,
    mesh=rotor_2_bem_mesh,
    acoustics_data=hover_acoustics,
    disk_prefix='rotor_2_disk',
    blade_prefix='rotor_2_blade'
)
hover_tonal_SPL_2, hover_tonal_SPL_A_weighted_2 = ks_model_rotor_2.evaluate_tonal_noise(dT_2, dD_2, ac_states)
hover_model.register_output(hover_tonal_SPL_2)
hover_model.register_output(hover_tonal_SPL_A_weighted_2)

gl_model_rotor_2 = GL(
    component=rotor_2_disk,
    mesh=rotor_2_bem_mesh,
    acoustics_data=hover_acoustics,
    disk_prefix='rotor_2_disk',
    blade_prefix='rotor_2_blade'
)
hover_broadband_SPL_2, hover_broadband_SPL_A_weighted_2 = gl_model_rotor_2.evaluate_broadband_noise(ac_states, CT_2)
hover_model.register_output(hover_broadband_SPL_2)
hover_model.register_output(hover_broadband_SPL_A_weighted_2)

hover_total_noise_model = TotalAircraftNoise(
    acoustics_data=hover_acoustics,
    component_list=[rotor_1_disk, rotor_2_disk]
)
noise_components = [hover_tonal_SPL_1, hover_broadband_SPL_1, hover_tonal_SPL_2, hover_broadband_SPL_2]
A_weighted_noise_components = [
    hover_tonal_SPL_A_weighted_1, hover_broadband_SPL_A_weighted_1, hover_tonal_SPL_A_weighted_2, hover_broadband_SPL_A_weighted_2
]
hover_total_SPL, hover_total_SPL_A_weighted = hover_total_noise_model.evaluate(
    noise_components=noise_components,
    A_weighted_noise_components=A_weighted_noise_components
)

hover_acoustics.visualize(hover_total_SPL)

hover_model.register_output(hover_total_SPL)
hover_model.register_output(hover_total_SPL_A_weighted)

hover_condition.add_m3l_model('hover_model', hover_model)
design_scenario.add_design_condition(hover_condition)

system_model.add_design_scenario(design_scenario=design_scenario)


# ================================ CRUISE ================================


















caddee_csdl_model = caddee.assemble_csdl()

caddee_csdl_model.connect(
    'system_model.hover_test.hover.hover.rotor_1_disk_bem_model.rpm',
    'system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.rpm'
)
caddee_csdl_model.connect(
    'system_model.hover_test.hover.hover.rotor_1_disk_bem_model.rpm',
    'system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.rpm'
)

caddee_csdl_model.connect(
    'system_model.hover_test.hover.hover.rotor_2_disk_bem_model.rpm',
    'system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.rpm'
)
caddee_csdl_model.connect(
    'system_model.hover_test.hover.hover.rotor_2_disk_bem_model.rpm',
    'system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.rpm'
)

caddee_csdl_model.connect(
    'system_model.hover_test.hover.hover.rotor_1_disk_bem_model.phi_bracketed_search_group.phi_distribution',
    'system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.phi'
)

caddee_csdl_model.connect(
    'system_model.hover_test.hover.hover.rotor_2_disk_bem_model.phi_bracketed_search_group.phi_distribution',
    'system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.phi'
)

'''
LIST OF CONNECTIONS THAT ARE MISSING:
- system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.rpm
- system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model.altitude
- system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.phi
- system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.rpm
- system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.rpm
- system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model.altitude
- system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.phi
- system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.rpm
'''

sim = Simulator(caddee_csdl_model, analytics=True, display_scripts=True, name='sbs_rotors')
sim.run()