import numpy as np
import csdl
from python_csdl_backend import Simulator

from lsdo_acoustics import Acoustics

from lsdo_acoustics.core.models.broadband.GL.GL_model import GLModel
from lsdo_acoustics.core.models.broadband.SKM.SKM_model import SKMBroadbandModel
from lsdo_acoustics.core.models.broadband.BPM.BPM_model import BPMModel
from lsdo_acoustics.core.models.total_noise_model import TotalAircraftNoiseModel

from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

''' NOTES:
Data files used for each condition:
    - hover: APCInput.txt
    - edgewise:  
'''
# region dummy mesh
class DummyMesh(object):
    def __init__(self, num_radial, num_tangential):
        self.parameters = {
            'num_radial': num_radial,
            'num_tangential': num_tangential
        }
# endregion

class BroadbandModels(ModuleCSDL):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('disk_prefix')
        self.parameters.declare('blade_prefix')
        self.parameters.declare('mesh')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('num_rotors', types=int)
    
    def define(self):
        component_name = self.parameters['component_name']
        disk_prefix = self.parameters['disk_prefix']
        blade_prefix = self.parameters['blade_prefix']
        mesh = self.parameters['mesh']
        observer_data = self.parameters['observer_data']
        num_observers = observer_data['num_observers']
        num_blades = self.parameters['num_blades'] 
        num_nodes = self.parameters['num_nodes']
        num_rotors = self.parameters['num_rotors']
        
        
        num_radial = mesh.parameters['num_radial']

        test = True # this means we use only the CSDL version, not M3L

        prop_rad_i = self.declare_variable('propeller_radius_input')
        chord_i = self.declare_variable('chord_profile_input', shape=(num_radial,1))
        rpm_i = self.declare_variable('rpm_input')
        origin_i = self.declare_variable('origin_input', shape=(num_rotors, 3))
        t_dir_i = self.declare_variable('thrust_dir_input', shape=(3,))
        M_i = self.declare_variable('mach_number_input')
        CT_i = self.declare_variable('CT_input')

        self.register_output('propeller_radius', prop_rad_i * 1)
        self.register_output('mach_number', M_i*1.)
        self.register_output('chord_profile', chord_i*1.)
        self.register_output('rpm', rpm_i * 1.)
        self.register_output('thrust_dir', t_dir_i * 1)
        self.register_output('Vx', M_i * 343.)
        self.register_output('CT', CT_i * 1.)


        


        for i in range(num_rotors):
            self.register_output(f'origin_{i+1}', csdl.reshape(origin_i[i,:], (3,)))
            self.add(
                GLModel(
                    component_name=f'gl_{i+1}',
                    disk_prefix=disk_prefix,
                    blade_prefix=blade_prefix,
                    mesh=mesh,
                    observer_data=observer_data,
                    num_blades=num_blades,
                    num_nodes=num_nodes,
                    debug=test
                ),
                f'gl_{i+1}_spl_model',
                promotes=[]
            )
            print(i)
            self.connect('propeller_radius', f'gl_{i+1}_spl_model.propeller_radius')
            self.connect('chord_profile', f'gl_{i+1}_spl_model.chord_profile')
            self.connect('rpm', f'gl_{i+1}_spl_model.rpm')
            self.connect(f'origin_{i+1}', f'gl_{i+1}_spl_model.origin')
            self.connect('thrust_dir', f'gl_{i+1}_spl_model.thrust_dir')
            self.connect('CT', f'gl_{i+1}_spl_model.CT')
            self.connect('Vx', f'gl_{i+1}_spl_model.Vx')

            self.add(
                SKMBroadbandModel(
                    component_name=f'skm_{i+1}',
                    disk_prefix=disk_prefix,
                    blade_prefix=blade_prefix,
                    mesh=mesh,
                    observer_data=observer_data,
                    num_blades=num_blades,
                    num_nodes=num_nodes,
                    debug=test
                ),
                f'skm_{i+1}_spl_model',
                promotes=[]
            )

            print(i)
            self.connect('propeller_radius', f'skm_{i+1}_spl_model.propeller_radius')
            self.connect('chord_profile', f'skm_{i+1}_spl_model.chord_profile')
            self.connect('rpm', f'skm_{i+1}_spl_model.rpm')
            self.connect(f'origin_{i+1}', f'skm_{i+1}_spl_model.origin')
            self.connect('thrust_dir', f'skm_{i+1}_spl_model.thrust_dir')
            self.connect('CT', f'skm_{i+1}_spl_model.CT')
            self.connect('Vx', f'skm_{i+1}_spl_model.Vx')

            self.add(
                BPMModel(
                    component_name=f'bpm_{i+1}',
                    disk_prefix=disk_prefix,
                    blade_prefix=blade_prefix,
                    mesh=mesh,
                    observer_data=observer_data,
                    num_blades=num_blades,
                    num_nodes=num_nodes,
                    debug=test
                ),
                f'bpm_{i+1}_spl_model',
                promotes=[]
            )

            self.connect('Vx', f'bpm_{i+1}_spl_model.Vx')
            self.connect('chord_profile', f'bpm_{i+1}_spl_model.chord_profile')
            # self.connect('delta_P', f'bpm_{i+1}_spl_model.delta_P')
            # self.connect('delta_S', f'bpm_{i+1}_spl_model.delta_S')
            # self.connect('twist_profile', f'bpm_{i+1}_spl_model.twist_profile')
            # self.connect('a_CL0', f'bpm_{i+1}_spl_model.a_CL0')
            self.connect('thrust_dir', f'bpm_{i+1}_spl_model.thrust_dir')
            self.connect('rpm', f'bpm_{i+1}_spl_model.rpm')
            self.connect('mach_number', f'bpm_{i+1}_spl_model.mach_number')
            self.connect('propeller_radius', f'bpm_{i+1}_spl_model.propeller_radius')


        model_list = ['gl', 'skm', 'bpm']
        # model_list = ['gl', 'skm']
        for i in range(len(model_list)):
            model_name = model_list[i]
            self.add(
                TotalAircraftNoiseModel(
                    num_observers=observer_data['num_observers'],
                    var_names=[f'{model_list[i]}_{j+1}_broadband_spl' for j in range(num_rotors)]
                ),
                f'{model_list[i]}_total_aircraft_noise_model',
                promotes=[]
            )

            for j in range(num_rotors):
                self.connect(f'{model_name}_{j+1}_spl_model.{model_name}_spl_model.{model_name}_{j+1}_broadband_spl', 
                             f'{model_name}_total_aircraft_noise_model.{model_name}_{j+1}_broadband_spl')

# INPUTS
altitude = 75 # meters
rotor_location = np.array([[0., 0., 0]])
# print(rotor_location.shape)
# exit()
hover_inputs = {
    'prop_radius': 0.14,
    'chord_profile': 0.028 * np.ones((30,)),
    'thrust_dir': np.array([0., 0., 1.]),
    'Mach': 0.,
    'rpm': 3600.,
    'CT': 0.0136,
    'thrust_origin': rotor_location, # NOTE: variable name in CSDL code is origin, not thrust_origin
    'num_blades': 2,
    'exp_observer_position': np.array([1.347, 0., -1.347]),
    'tc': 0.12, # thickness to chord ratio, needed for BPM?
    'exp_result': 54.35 # dB from experimental testing on real rotor
}

edgewise_inputs = {
    'prop_radius': 2,
    'chord_profile': 0.121 * np.ones((30,)),
    'thrust_dir': np.array([0., 0., 1.,]),
    'Mach': 0.0551381568,
    'rpm': 1050,
    'CT': 0.0044,
    'thrust_origin': rotor_location, # NOTE: variable name in CSDL code is origin, not thrust_origin
    'num_blades': 4,
    'exp_observer_position': np.array([0., 0., 7.13232]),
    'tc': 0.12, # thickness to chord ratio, needed for BPM?
    'exp_result': 92.06 # dB from experimental testing on real rotor
}

input_dict = {
    'hover': hover_inputs,
    'edgewise': edgewise_inputs
}

mode = 'hover'
inputs = input_dict[mode]
num_rotors = 1
num_radial = len(inputs['chord_profile'])
mesh = DummyMesh(num_radial=num_radial,num_tangential=35)

observers = Acoustics(
    # aircraft_position=np.array([0.,0.,altitude])
    aircraft_position=np.array([0.,0.,0.])
)

observers.add_observer(
    'obs',
    # np.array([0., 0., 0.]),
    inputs['exp_observer_position'],
    time_vector=np.array([0.])
)

observer_data = observers.assemble_observers()

model = BroadbandModels(
    component_name='comparison',
    disk_prefix='disk',
    blade_prefix='blade',
    mesh=mesh,
    observer_data=observer_data,
    num_blades=inputs['num_blades'],
    num_rotors=num_rotors,
)

sim = Simulator(model, analytics=True)
sim['propeller_radius_input'] = inputs['prop_radius']
sim['chord_profile_input'] = inputs['chord_profile']
sim['rpm_input'] = inputs['rpm']
sim['origin_input'] = inputs['thrust_origin']
sim['thrust_dir_input'] = inputs['thrust_dir']
sim['mach_number_input'] = inputs['Mach']
sim['CT_input'] = inputs['CT']


sim.run()

# generating 
names =  ['gl', 'skm', 'bpm']
output_spl= {}
output_spl['exp'] = inputs['exp_result']
for name in names:
    output_spl[name]  = sim[f'{name}_total_aircraft_noise_model.total_spl'][0][0]

# NOTE: JOB FOR ENLACE STUDENTS: PLOT THE EXPERIMENTAL DATA IN THE output_spl DICTIONARY

for key in output_spl.keys():
    print(key, output_spl[key]) # data for comparison