import numpy as np
import caddee.api as cd 
import lsdo_geo as lg
import m3l
from python_csdl_backend import Simulator
from caddee import IMPORTS_FILES_FOLDER
import array_mapper as am

caddee = cd.CADDEE()
caddee.system_representation = system_rep = cd.SystemRepresentation()
caddee.system_parameterization = system_param = cd.SystemParameterization(system_representation=system_rep)

file_name = IMPORTS_FILES_FOLDER / 'LPC_test.stp'
spatial_rep = system_rep.spatial_representation
spatial_rep.import_file(file_name=file_name)
spatial_rep.refit_geometry(file_name=file_name)

'''
FWD EVAL TEST CASE:
- 2 of the hover rotors (to test individual rotor + total aircraft noise models)
'''

rotor_1_primitive_names = list(spatial_rep.get_primitives(search_names=['Rotor_1_disk']).keys())
rotor_1 = cd.Rotor(
    name='rotor_1', 
    spatial_representation=spatial_rep, 
    primitive_names=rotor_1_primitive_names
)

rotor_7_primitive_names = list(spatial_rep.get_primitives(search_names=['Rotor_7_disk']).keys())
rotor_7 = cd.Rotor(
    name='rotor_7', 
    spatial_representation=spatial_rep, 
    primitive_names=rotor_7_primitive_names
)

system_rep.add_component(rotor_1)
system_rep.add_component(rotor_7)

# DEFINE MESHES
p11 = rotor_1.project(np.array([5.070, -23.750, 6.730]), direction=np.array([0., 0., 1.]), plot=False)
p12 = rotor_1.project(np.array([5.070, -13.750, 6.730]), direction=np.array([0., 0., 1.]), plot=False)
p21 = rotor_1.project(np.array([10.070, -18.750, 6.730]), direction=np.array([0., 0., 1.]), plot=False)
p22 = rotor_1.project(np.array([0.070, -18.750, 6.730]), direction=np.array([0., 0., 1.]), plot=False)
rotor_1_in_plane_1 = am.subtract(p11,p12)
rotor_1_in_plane_2 = am.subtract(p21,p22)
rotor_1_origin = rotor_1.project(np.array([5.070, -18.750, 6.730]))
system_rep.add_output('rotor_1_in_plane_1', quantity=rotor_1_in_plane_1)
system_rep.add_output('rotor_1_in_plane_2', quantity=rotor_1_in_plane_2)
system_rep.add_output('rotor_1_origin', quantity=rotor_1_origin)


p11 = rotor_7.project(np.array([5.070, 23.750, 6.730]), direction=np.array([0., 0., 1.]), plot=False)
p12 = rotor_7.project(np.array([5.070, 13.750, 6.730]), direction=np.array([0., 0., 1.]), plot=False)
p21 = rotor_7.project(np.array([0.070, 18.750, 6.730]), direction=np.array([0., 0., 1.]), plot=False)
p22 = rotor_7.project(np.array([10.070, 18.750, 6.730]), direction=np.array([0., 0., 1.]), plot=False)
rotor_7_in_plane_1 = am.subtract(p11,p12)
rotor_7_in_plane_2 = am.subtract(p21,p22)
rotor_7_origin = rotor_7.project(np.array([5.070, 18.750, 6.730]))
system_rep.add_output('rotor_7_in_plane_1', quantity=rotor_7_in_plane_1)
system_rep.add_output('rotor_7_in_plane_2', quantity=rotor_7_in_plane_2)
system_rep.add_output('rotor_7_origin', quantity=rotor_7_origin)


caddee.system_model = system_model = cd.SystemModel()

design_scenario = cd.DesignScenario(name='acoustics_test')

hover_model = m3l.Model()
hover_condition = cd.HoverCondition(name="hover")
hover_condition.atmosphere_model = cd.SimpleAtmosphereModel()

hover_condition.set_module_input(name='altitude', val=1000)
# hover_condition.set_module_input(name='', val=)
# hover_condition.set_module_input(name='', val=)
# hover_condition.set_module_input(name='', val=)
# hover_condition.set_module_input(name='', val=)
# hover_condition.set_module_input(name='', val=)
# hover_condition.set_module_input(name='', val=)
# hover_condition.set_module_input(name='', val=)
# hover_condition.set_module_input(name='', val=)

ac_states = hover_condition.evaluate_ac_states()
hover_model.register_output(ac_states)

'''
================================ BEM MODELS ================================
'''

from lsdo_rotor.core.BEM_caddee.BEM_caddee import BEM, BEMMesh

rotor_1_bem_mesh = BEMMesh(
    meshes=dict(
        rotor_1_in_plane_1=rotor_1_in_plane_1,
        rotor_1_in_plane_2=rotor_1_in_plane_2,
        rotor_1_origin=rotor_1_origin
    ),
    airfoil='NACA_4412',
    num_blades=2,
    chord_b_spline_rep=True,
    twist_b_spline_rep=True
)
bem_model_1 = BEM(component=rotor_1, mesh=rotor_1_bem_mesh)
bem_model_1.set_module_input('rpm', val=1200)
bem_forces_1, bem_moments_1 = bem_model_1.evaluate(ac_states=ac_states)

rotor_7_bem_mesh = BEMMesh(
    meshes=dict(
        rotor_7_in_plane_1=rotor_7_in_plane_1,
        rotor_7_in_plane_2=rotor_7_in_plane_2,
        rotor_7_origin=rotor_7_origin
    ),
    airfoil='NACA_4412',
    num_blades=2,
    chord_b_spline_rep=True,
    twist_b_spline_rep=True
)
bem_model_7 = BEM(component=rotor_7, mesh=rotor_7_bem_mesh)
bem_model_7.set_module_input('rpm', val=1200)
bem_forces_7, bem_moments_7 = bem_model_7.evaluate(ac_states=ac_states)

# NOTE: CODE HAS NO ISSUES UP TO HERE
exit()
'''
================================ ACOUSTICS MODELS ================================
'''
from lsdo_acoustics.core.acoustics import Acoustics
from lsdo_acoustics.core.m3l_models.lowson_m3l_model import Lowson

hover_acoustics = Acoustics(
    design_condition=1, # NOT NEEDED
    aircraft_position = np.array([0.,0.,100.])
)

hover_acoustics.add_observer(
    name='observer_below',
    obs_position=np.array([0.,0.,0.,])
)

hover_acoustics.add_observer(
    name='observer_left',
    obs_position=np.array([0.,20.,0.,])
)

hover_acoustics.add_observer(
    name='observer_right',
    obs_position=np.array([0.,-20.,0.,])
)

lowson_model_1 = Lowson(mesh=rotor_1_bem_mesh, acoustics_data=hover_acoustics)
rotor_1_tonal_spl = lowson_model_1.evaluate_tonal_noise(bem_forces_1)


lowson_model_7 = Lowson(mesh=rotor_7_bem_mesh, acoustics_data=hover_acoustics)
rotor_7_tonal_spl = lowson_model_7.evaluate_tonal_noise(bem_forces_7)


from lsdo_acoustics.core.m3l_models import TotalAircraftNoise

noise_components = [
    rotor_1_tonal_spl,
    rotor_7_tonal_spl
]

total_noise_model = TotalAircraftNoise(acoustics_data=hover_acoustics)
aircraft_noise_spl = total_noise_model.evaluate(
    rotor_1_tonal_spl, rotor_7_tonal_spl
)

hover_model.register_output(aircraft_noise_spl)

hover_condition.add_m3l_model('hover_model', hover_model)
design_scenario.add_design_condition(hover_condition)

system_model.add_design_scenario(design_scenario=design_scenario)
caddee_csdl_model = caddee.assemble_csdl()

sim = Simulator(caddee_csdl_model, analytics=True, display_scripts=True)