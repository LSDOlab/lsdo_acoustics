import numpy as np
import caddee.api as cd
import lsdo_geo as lg
import m3l
from python_csdl_backend import Simulator
import array_mapper as am
from lsdo_acoustics import GEOMETRY_PATH, IMPORTS_PATH

caddee = cd.CADDEE()
caddee.system_representation = system_rep = cd.SystemRepresentation()
caddee.system_parameterization = system_param = cd.SystemParameterization(system_representation=system_rep)

file_name = GEOMETRY_PATH / 'single_rotor.stp'
spatial_rep = system_rep.spatial_representation
spatial_rep.import_file(file_name=file_name, file_path=str(IMPORTS_PATH))
spatial_rep.refit_geometry(file_name=file_name, file_path=str(IMPORTS_PATH))

rotor_primitive_names = list(
    spatial_rep.get_primitives(search_names=['Rotor_disk']).keys()
)
rotor = cd.Rotor(
    name='rotor',
    spatial_representation=spatial_rep,
    primitive_names=rotor_primitive_names
)

system_rep.add_component(rotor)

p11 = rotor.project(np.array([15.000, 0.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p12 = rotor.project(np.array([-15.000, 0.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p21 = rotor.project(np.array([0.000, 15.000 , 0.000]), direction=np.array([0.,0.,1.]), plot=False)
p22 = rotor.project(np.array([0.000, -15.000, 0.000]), direction=np.array([0.,0.,1.]), plot=False)
rotor_in_plane_x = am.subtract(p11,p12)
rotor_in_plane_y = am.subtract(p21,p22)
rotor_origin = rotor.project(np.array([0.000, 0.000, 0.000]), direction=np.array([0.,0.,1.]))
system_rep.add_output('rotor_in_plane_x', quantity=rotor_in_plane_x)
system_rep.add_output('rotor_in_plane_y', quantity=rotor_in_plane_y)
system_rep.add_output('rotor_origin', quantity=rotor_origin)

caddee.system_model = system_model = cd.SystemModel()

design_scenario = cd.DesignScenario(name='single_rotor_test')
test_model = m3l.Model()
cruise_condition = cd.CruiseCondition(name='cruise')
cruise_condition.atmosphere_model = cd.SimpleAtmosphereModel()

cruise_condition.set_module_input(name='mach_number', val=0.17)
cruise_condition.set_module_input(name='range', val=40000)
cruise_condition.set_module_input(name='altitude', val=500)
cruise_condition.set_module_input(name='wing_incidence_angle', val=np.deg2rad(0))
cruise_condition.set_module_input(name='pitch_angle', val=np.deg2rad(2), dv_flag=False, lower=np.deg2rad(0), upper=np.deg2rad(5))
cruise_condition.set_module_input(name='observer_location', val=np.array([0, 0, 500]))
ac_states = cruise_condition.evaluate_ac_states()
test_model.register_output(ac_states)


# region acoustics
from lsdo_acoustics import Acoustics
from lsdo_acoustics.core.m3l_models import Lowson
from lsdo_acoustics.core.m3l_models import SKM

cruise_acoustics = Acoustics(
    aircraft_position = np.array([0.,0.,0])
)

cruise_acoustics.add_observer(
    name='obs1',
    obs_position=np.array([0., 0., 1.75]),
    time_vector=np.array([0.]),
)

from lsdo_acoustics.core.acoustics_mesh import AcousticsMesh

acoustics_mesh = AcousticsMesh(
    # rotor_disk_mesh=rotor_bem_mesh,
    num_radial=30,
    num_azimuthal=10,
    num_blades=2
)

lowson_model = Lowson(
    component=rotor,
    # mesh=rotor_bem_mesh,
    mesh=acoustics_mesh,
    acoustics_data=cruise_acoustics
)
cruise_tonal_SPL = lowson_model.evaluate_tonal_noise()
test_model.register_output(cruise_tonal_SPL)

# endregion

cruise_condition.add_m3l_model('validation', test_model)
design_scenario.add_design_condition(cruise_condition)

system_model.add_design_scenario(design_scenario=design_scenario)
caddee_csdl_model = caddee.assemble_csdl()

sim = Simulator(caddee_csdl_model, analytics=True)

# region validation inputs
sim['system_model.single_rotor_test.cruise.cruise.rotor_Lowson_tonal_model.lowson_spl_model.rpm'] = 5500
sim['system_model.single_rotor_test.cruise.cruise.rotor_Lowson_tonal_model.lowson_spl_model.speed_of_sound'] = 340.3
sim['system_model.single_rotor_test.cruise.cruise.rotor_Lowson_tonal_model.lowson_spl_model.forward_mach_number'] = 0.0705 


import pickle
# FILE NAME
from pathlib import Path
root_path = Path(__file__).parents[1] # goes back one directory
file_title = 'loading_Jamaluddin'
file_path = root_path / 'lsdo_acoustics' / 'core' / 'validation' / file_title

# open a file, where you stored the pickled data
file = open(file_path, 'rb')
exp_data = pickle.load(file) # NEED TO LOAD THIS INTO THE MESH
file.close()

# endregion

# sim.run()
# print('rotor spl:', sim['system_model.single_rotor_test.cruise.cruise.rotor_Lowson_tonal_model.lowson_spl_model.rotor_tonal_SPL'])
# print('observer_angle:', sim['system_model.single_rotor_test.cruise.cruise.rotor_Lowson_tonal_model._003i.rel_obs_angle'])