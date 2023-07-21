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
    spatial_rep.get_primitives(search_names=['Rotor_1_disk']).keys()
)
rotor_1_disk = cd.Rotor(
    name='rotor_1_disk',
    spatial_representation=spatial_rep,
    primitive_names=rotor_1_disk_primitive_names
)
system_rep.add_component(rotor_1_disk)

p11 = rotor_1_disk.project(np.array([0.25, 1. , 0.]), direction=np.array([]), plot=True)
p12 = rotor_1_disk.project(np.array([-0.25, 1., 0.]), direction=np.array([]), plot=True)
p21 = rotor_1_disk.project(np.array([0., 1.25, 0.]), direction=np.array([]), plot=True)
p22 = rotor_1_disk.project(np.array([0., -0.75, 0.]), direction=np.array([]), plot=True)
rotor_1_origin = rotor_1_disk.project(np.array([0., 1., 0.]), direction=np.array([0., 0., 1.]))
rotor_1_in_plane_x = am.subtract(p11, p12)
rotor_1_in_plane_y = am.subtract(p21, p22)
system_rep.add_output('rotor_1_disk_in_plane_1', quantity=rotor_1_in_plane_x)
system_rep.add_output('rotor_1_disk_in_plane_2', quantity=rotor_1_in_plane_y)
system_rep.add_output('rotor_1_disk_origin', quantity=rotor_1_origin)



exit()
rotor_2_primitive_names = list(
    spatial_rep.get_primitives(search_names=['Rotor_2_disk']).keys()
)
rotor_2 = cd.Rotor(
    name='rotor_2',
    spatial_representation=spatial_rep,
    primitive_names=rotor_2_primitive_names
)

system_rep.add_component(rotor_1)
system_rep.add_component(rotor_2)

p11 = rotor_1.project(np.array([0.000, 25.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p12 = rotor_1.project(np.array([15.000, 40.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p21 = rotor_1.project(np.array([-15.000, 40.000 , 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p22 = rotor_1.project(np.array([0.000, 55.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
rotor_1_in_plane_x = am.subtract(p12,p21)
rotor_1_in_plane_y = am.subtract(p22,p11)
rotor_1_origin = rotor_1.project(np.array([0.000, -40.000, 0.000]), direction=np.array([0.,0.,1.]))
system_rep.add_output('rotor_1_in_plane_x', quantity=rotor_1_in_plane_x)
system_rep.add_output('rotor_1_in_plane_y', quantity=rotor_1_in_plane_y)
system_rep.add_output('rotor_1_origin', quantity=rotor_1_origin)


p11 = rotor_2.project(np.array([0.000, -25.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p12 = rotor_2.project(np.array([15.000, -40.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p21 = rotor_2.project(np.array([-15.000, -40.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p22 = rotor_2.project(np.array([0.000, -55.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
rotor_2_in_plane_x = am.subtract(p12, p21)
rotor_2_in_plane_y = am.subtract(p11, p22)
rotor_2_origin = rotor_2.project(np.array([0.000, -40.000, 0.000]), direction=np.array([0.,0.,1.]))
system_rep.add_output('rotor_2_in_plane_x', quantity=rotor_2_in_plane_x)
system_rep.add_output('rotor_2_in_plane_y', quantity=rotor_2_in_plane_y)
system_rep.add_output('rotor_2_origin', quantity=rotor_2_origin)

caddee.system_model = system_model = cd.SystemModel()

design_scenario = cd.DesignScenario(name='hover_test')
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
        rotor_1_in_plane_x=rotor_1_in_plane_x,
        rotor_1_in_plane_y=rotor_1_in_plane_y,
        rotor_1_origin=rotor_1_origin
    ),
    airfoil='NACA_4412',
    num_blades=3,
    chord_b_spline_rep=True,
    twist_b_spline_rep=True
)
bem_model_1 = BEM(component=rotor_1, mesh=rotor_1_bem_mesh)
bem_model_1.set_module_input('rpm', val=1200)
bem_forces_1, bem_moments_1 = bem_model_1.evaluate(ac_states=ac_states)

rotor_2_bem_mesh = BEMMesh(
    meshes=dict(
        rotor_2_in_plane_x=rotor_2_in_plane_x,
        rotor_2_in_plane_y=rotor_2_in_plane_y,
        rotor_2_origin=rotor_2_origin
    ),
    airfoil='NACA_4412',
    num_blades=3,
    chord_b_spline_rep=True,
    twist_b_spline_rep=True
)
bem_model_2 = BEM(component=rotor_2, mesh=rotor_2_bem_mesh)
bem_model_2.set_module_input('rpm', val=1200)
bem_forces_2, bem_moments_2 = bem_model_2.evaluate(ac_states=ac_states)

# NOTE: CODE HAS NO ISSUES UP TO HERE
# exit()