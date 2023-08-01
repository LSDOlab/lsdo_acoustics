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
aircraft_location = np.array([[0., 0., altitude]])
# rotor_location = np.array([
#     [5.852, -5.715, altitude + 2.746],
#     [5.852, 5.715, altitude + 2.746],
#     [5.718, -2.5756, altitude + 2.835],
#     [5.718, 2.5756, altitude + 2.835],
#     [1.5453, -5.715, altitude + 2.051],
#     [1.5453, 5.715, altitude + 2.051],
#     [1.411, -2.478, altitude + 2.033],
#     [1.411, 2.478, altitude + 2.033]
# ])

rotor_location = np.array([
    [5.852, -5.715, 2.746],
    [5.852, 5.715, 2.746],
    [5.718, -2.5756, 2.835],
    [5.718, 2.5756, 2.835],
    [1.5453, -5.715, 2.051],
    [1.5453, 5.715, 2.051],
    [1.411, -2.478, 2.033],
    [1.411, 2.478, 2.033]
])

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
    'prop_radius': 3.048/2,
    'chord_profile': twist_profile * np.pi/180,
    'chord_profile': chord_profile,
    'aoa': aoa,
    'thrust_dir': np.array([0., 0., 1.]),
    'Mach': 0.,
    'rpm': 1000,
    'CT': 0.08,
    'thrust_origin': rotor_location, # NOTE: variable name in CSDL code is origin, not thrust_origin
    'num_blades': 2,
    'tc': 0.12, # thickness to chord ratio, needed for BPM?
}

edgewise_inputs = {
    'prop_radius': 3.048/2,
    'twist_profile': twist_profile * np.pi/180,
    'chord_profile': chord_profile,
    'aoa': aoa,
    'thrust_dir': np.array([0., 0., 1.,]),
    'Mach': 0.0551381568,
    'rpm': 1000,
    'CT': 0.08,
    'thrust_origin': rotor_location, # NOTE: variable name in CSDL code is origin, not thrust_origin
    'num_blades': 2,
    'tc': 0.12, # thickness to chord ratio, needed for BPM?
}

input_dict = {
    'hover': hover_inputs,
    # 'edgewise': edgewise_inputs # NOTE: DO NOT USE EDGEWISE
}

mode = 'hover'
inputs = input_dict[mode]
num_rotors = len(rotor_location)
num_radial = len(inputs['chord_profile'])
mesh = DummyMesh(num_radial=num_radial,num_tangential=35)

observers = Acoustics(
    aircraft_position=aircraft_location
)

observers.add_observer(
    'obs',
    np.array([0., 0., 0.]),
    time_vector=np.array([0.])
)

# observers.setup_directivity_plot(
#     'directivity_plot',
#     center_point=np.array([0.,0.,0.]),
#     radius=10.,
#     num_azim=45
# )

observer_data = observers.assemble_observers()

model = BroadbandModels(
    component_name='comparison',
    disk_prefix='disk',
    blade_prefix='blade',
    mesh=mesh,
    observer_data=observer_data,
    num_blades=inputs['num_blades'],
    num_rotors=num_rotors,
    f = 500
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

names = ['gl', 'skm', 'bpm']
output_spl = {}
for name in names:
    output_spl[name] = sim[f'{name}_total_aircraft_noise_model.total_spl']


# NOTE: JOB FOR ENLACE STUDENTS: PLOT THE EXPERIMENTAL DATA IN THE output_spl DICTIONARY

# EXAMPLE POLAR PLOT BELOW
# import matplotlib.pyplot as plt

# x = sim['gl_1_spl_model.steady_observer_location_model.init_obs_x_loc'] # x-location
# y = sim['gl_1_spl_model.steady_observer_location_model.init_obs_y_loc'] # y-location

# r = np.sqrt(x**2 + y**2)
# theta = np.arctan2(y,x)

# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(theta, np.reshape(output_spl['gl'], theta.shape))
# ax.plot(theta, np.reshape(output_spl['bpm'], theta.shape))
# ax.grid(True)

# ax.set_title("example", va='bottom')
# plt.show()

# swap between edgewise and hover in line 210