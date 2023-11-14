import numpy as np
import csdl
from python_csdl_backend import Simulator

from lsdo_acoustics import Acoustics

from lsdo_acoustics.core.models.broadband.GL.GL_model import GLModel
from lsdo_acoustics.core.models.broadband.SKM.SKM_model import SKMBroadbandModel
from lsdo_acoustics.core.models.broadband.BPM.BPM_model import BPMModel
from lsdo_acoustics.core.models.total_noise_model import TotalAircraftNoiseModel



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

class BroadbandModels(csdl.Model):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('disk_prefix')
        self.parameters.declare('blade_prefix')
        self.parameters.declare('mesh')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('num_rotors', types=int)
        self.parameters.declare('f')
    
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
        
        freq = self.parameters['f']
        
        num_radial = mesh.parameters['num_radial']

        test = True # this means we use only the CSDL version, not M3L

        prop_rad_i = self.declare_variable('propeller_radius_input')
        chord_i = self.declare_variable('chord_profile_input', shape=(num_radial,1))
        twist_i = self.declare_variable('twist_profile_input', shape=(num_radial,1))
        aoa_i = self.declare_variable('aoa_input', shape=(num_radial,1))
        rpm_i = self.declare_variable('rpm_input')
        origin_i = self.declare_variable('origin_input', shape=(num_rotors, 3))
        t_dir_i = self.declare_variable('thrust_dir_input', shape=(3,))
        M_i = self.declare_variable('mach_number_input')
        CT_i = self.declare_variable('CT_input')

        self.register_output('propeller_radius', prop_rad_i * 1)
        self.register_output('mach_number', M_i*1.)
        self.register_output('chord_profile', chord_i*1.)
        self.register_output('twist_profile', twist_i*1.*np.pi/180)
        self.register_output('aoa_profile', aoa_i*1.)
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
                    debug=test,
                    freq=freq
                ),
                f'bpm_{i+1}_spl_model',
                promotes=[]
            )

            self.connect('Vx', f'bpm_{i+1}_spl_model.Vx')
            self.connect('chord_profile', f'bpm_{i+1}_spl_model.chord_profile')
            self.connect('twist_profile', f'bpm_{i+1}_spl_model.twist_profile')
            self.connect('aoa_profile', f'bpm_{i+1}_spl_model.aoa')

            # self.connect('delta_P', f'bpm_{i+1}_spl_model.delta_P')
            # self.connect('delta_S', f'bpm_{i+1}_spl_model.delta_S')
            # self.connect('twist_profile', f'bpm_{i+1}_spl_model.twist_profile')
            # self.connect('a_CL0', f'bpm_{i+1}_spl_model.a_CL0')
            self.connect('thrust_dir', f'bpm_{i+1}_spl_model.thrust_dir')
            self.connect('rpm', f'bpm_{i+1}_spl_model.rpm')
            # self.connect('mach_number', f'bpm_{i+1}_spl_model.mach_number')
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

twist_profile = np.array([20.1916, 21.1277, 21.8059, 22.2317, 22.4106, 22.3507, 22.0879, 21.6735, 21.1662, 20.6342, 20.1075, 19.5118, 18.7633, 17.8987,
17.0489, 16.2841, 15.5870, 14.9334, 14.2981, 13.6595, 13.0435, 12.5037, 12.0380, 11.5740, 11.0647, 10.5702, 10.1621, 9.8043,
9.4096, 8.9594, 8.5263, 8.1540, 7.7885, 7.3698, 6.9057, 6.4276, 5.9366, 5.4100, 4.8245, 4.1566])
num_radial = len(twist_profile)

chord_profile = np.array([
    0.0163, 0.0177, 0.0192, 0.0205, 0.0219, 0.0232, 0.0244, 0.0257, 0.0268, 0.0279, 0.0286, 0.0293, 0.0299,
    0.0306, 0.0311, 0.0314, 0.0317, 0.0319, 0.0321, 0.0322, 0.0321, 0.0318, 0.0315, 0.0311, 0.0306, 0.0300,
    0.0293, 0.0286, 0.0278, 0.0267, 0.0255, 0.0242, 0.0227, 0.0214, 0.0198, 0.0179, 0.0154, 0.0124, 0.0093, 0.0061
])

aoa = np.array([
   -0.4870, 3.2590, 5.1330, 6.2770, 7.0290, 7.5360, 7.8790, 8.1030, 8.2390, 8.3050, 8.3160, 8.2820,  8.2100,
    8.1060, 7.9750, 7.8200, 7.6440, 7.4490, 7.2380, 7.0110, 6.7710, 6.5180, 6.2530, 5.9760, 5.6880,  5.3900,
    5.0810, 4.7620, 4.4300, 4.0870, 3.7290, 3.3550, 2.9620, 2.5440, 2.0940, 1.5980, 1.0320, 0.3480, -0.5820,
   -2.3300
])

hover_inputs = {
    'prop_radius': 0.14,
    'twist_profile': twist_profile * np.pi/180,
    # 'chord_profile': 0.028 * np.ones((30,)),
    'chord_profile': chord_profile,
    'aoa': aoa,
    'thrust_dir': np.array([0., 0., 1.]),
    'Mach': 0.,
    'rpm': 3600.,
    'CT': 0.0136,
    'thrust_origin': rotor_location, # NOTE: variable name in CSDL code is origin, not thrust_origin
    'num_blades': 2,
    'exp_observer_position': np.array([1.347, 0., -1.347]),
    'exp_result': 54.35, # dB from experimental testing on real rotor
    'f': 725
}

e_twist_profile = np.array([20.07449857,20.19675263,19.03533906,17.36962751,15.93314231,14.9703916,14.34383954,13.73256925,
13.09073543,12.47946514,12.03629417,11.68481375,11.39446036,10.98185291,10.43170965,9.789875836,8.934097421,7.956064947])

e_chord_profile = np.array([
    0.029332061,0.029866412,0.028454198,0.026526718,0.024732824,0.023167939,0.021851145,0.020629771,0.019446565,0.018377863,
    0.017347328,0.01639313,0.015438931,0.014503817,0.013549618,0.012614504,0.011698473,0.010820611,
])

edgewise_inputs = {
    'prop_radius': 0.12,
    'twist_profile': e_twist_profile * np.pi/180.,
    'chord_profile': e_chord_profile,
    'thrust_dir': np.array([0., 0., 1.,]),
    'aoa': 4.8 * np.ones_like(e_twist_profile),
    'Mach': 0.0235,
    'rpm': 6081,
    'CT': 0.015,
    'thrust_origin': rotor_location, # NOTE: variable name in CSDL code is origin, not thrust_origin
    'num_blades': 2,
    'exp_observer_position': np.array([2.1369, 0., 1.9458]),
    'exp_result': 45.3316256, # dB from experimental testing on real rotor
    'f': 1000
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
    f = inputs['f']
)

sim = Simulator(model, analytics=True)
sim['propeller_radius_input'] = inputs['prop_radius']
sim['chord_profile_input'] = inputs['chord_profile']
sim['twist_profile_input'] = inputs['twist_profile']
sim['aoa_input'] = inputs['aoa']
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