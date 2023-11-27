import numpy as np 
import csdl
from python_csdl_backend import Simulator

from lsdo_acoustics.core.acoustics import Acoustics
from lsdo_acoustics.core.models.tonal.Lowson.Lowson_model import LowsonModel
from lsdo_acoustics.core.models.tonal.KS.KvurtStalnov_model import KvurtStalnovModel
from lsdo_acoustics.core.models.broadband.SKM.SKM_model import SKMBroadbandModel
from lsdo_acoustics.core.models.broadband.GL.GL_model import GLModel

'''
This script runs the different acoustics models in CSDL with input
data for rotor operation and geometry.

The currently supported models are:
- Lowson (tonal) -> accurate in hover, edgewise and axial (allegedly)
- KS (tonal) -> accurate in hover (maybe axial)
- SKM (broadband) -> hover (maybe axial)
- GL (broadband) -> hover (maybe axial)
- NOTE: All of the models should theoretically work in steady cases

Locations are all specified with the Earth-fixed reference with freedom of
rotation in the x-y plane to adjust for aircraft direction. To be more specific:
    x points in the direction of aircraft movement
    y points to the left of the aircraft
    z points up, normal to the Earth surface

Inputs (all units should be in SI):
- number of blades (scalar)
- radial and tangential discretization of rotor blade (num_radial, num_tangential)
    - note that for steady cases, num_tangential should be 1
- rotor radius (scalar)
    - units: m
- rpm (scalar)
- chord profile (num_radial,)
    - units: m
- mach number (scalar)
- CT, rotor thrust coefficient (scalar)
- sectional drag and thrust (_dD, _dT) for Lowson model (num_radial,)
    - units: N
- radial derivative of drag and thrust (dD/dR and dT/dR) (num_radial,)
    - units: N/m
- non-dimensional sectional radius (num_radial,)
- thrust origin (location of rotor) (3)
    - units: m
- lambda_i (local induced inflow ratio) (num_radial,)

'''
class DummyMesh(object):
    def __init__(self, num_radial, num_tangential):
        self.parameters = {
            'num_radial': num_radial,
            'num_tangential': num_tangential,
            'mesh_units': 'm'
        }

class AcousticsComparisonModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('dummy_mesh') # HOLDS RADIAL AND TANGENTIAL DATA
        self.parameters.declare('num_blades')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('observer_data')


    def define(self):
        num_blades = self.parameters['num_blades']
        num_nodes = self.parameters['num_nodes']

        observer_data = self.parameters['observer_data']
        num_observers = observer_data['num_observers']

        dummy_mesh = self.parameters['dummy_mesh']
        num_radial, num_tangential = dummy_mesh.parameters['num_radial'], dummy_mesh.parameters['num_tangential']

        # declaring variables here
        self.create_input('propeller_radius')
        self.create_input('chord_profile', shape=(num_radial,))
        self.create_input('rpm', shape=(num_nodes, 1))
        self.create_input('thrust_origin', shape=(3,))
        self.create_input('thrust_dir', shape=(num_nodes, 3))
        self.create_input('CT', shape=(num_nodes,))
        self.create_input('Vx', shape=(num_nodes,))
        self.create_input('_dD', shape=(num_nodes, num_radial, num_tangential))
        self.create_input('_dT', shape=(num_nodes, num_radial, num_tangential))
        self.create_input('mach_number')
        self.create_input('in_plane_ex', shape=(num_nodes, 3))
        self.create_input('dTdR_real', shape=(num_nodes, num_radial))
        self.create_input('dDdR_real', shape=(num_nodes, num_radial))
        self.create_input('lambda_i', shape=(num_nodes, num_radial))
        self.create_input('nondim_sectional_radius', shape=(num_radial,))

        self.add(
            LowsonModel(
                mesh=dummy_mesh,
                num_blades=num_blades,
                observer_data=observer_data,
                num_nodes=num_nodes,
                debug=True,
                use_geometry=False
            ),
            'Lowson_model',
            promotes=[]
        )

        self.add(
            KvurtStalnovModel(
                mesh=dummy_mesh,
                num_blades=num_blades,
                observer_data=observer_data,
                num_nodes=num_nodes,
                debug=True,
                use_geometry=False
            ),
            'KS_model',
            promotes=[]
        )

        self.add(
            SKMBroadbandModel(
                mesh=dummy_mesh,
                observer_data=observer_data,
                num_blades=num_blades,
                num_nodes=num_nodes,
                debug=True,
            ),
            'SKM_model',
            promotes=[]
        )

        self.add(
            GLModel(
                mesh=dummy_mesh,
                num_blades=num_blades,
                observer_data=observer_data,
                num_nodes=num_nodes,
                debug=True,
                use_geometry=False
            ),
            'GL_model',
            promotes=[]
        )
        
        # region CONNECTING VARIABLES
        models = ['Lowson', 'KS', 'SKM', 'GL']
        model_type = ['tonal', 'tonal', 'broadband', 'broadband']
        for model in models:
            self.connect('propeller_radius', f'{model}_model.propeller_radius') # radius
            self.connect('rpm', f'{model}_model.rpm') # RPM
            self.connect('thrust_dir', f'{model}_model.thrust_dir') # thrust direction vector
            self.connect('thrust_origin', f'{model}_model.origin') # thrust origin 
            self.connect('chord_profile', f'{model}_model.chord_profile') # chord_profile
            if model == 'Lowson':
                self.connect('in_plane_ex', f'{model}_model.in_plane_ex') # vector in plane of rotor disk
                self.connect('mach_number', f'{model}_model.mach_number') # chord_profile
                self.connect('_dT', f'{model}_model._dT') # chord_profile
                self.connect('_dD', f'{model}_model._dD') # chord_profile
                self.connect('lambda_i', f'{model}_model.lambda_i') # radius
                self.connect('nondim_sectional_radius', f'{model}_model.nondim_sectional_radius') # radius
            if model in ['SKM', 'GL']:
                self.connect('CT', f'{model}_model.CT') # CT
                self.connect('Vx', f'{model}_model.Vx') # Vx
            if model == 'KS':
                self.connect('dTdR_real', f'{model}_model.dTdR_real') # radius
                self.connect('dDdR_real', f'{model}_model.dDdR_real') # radius
                self.connect('nondim_sectional_radius', f'{model}_model.nondim_sectional_radius') # radius
                self.connect('lambda_i', f'{model}_model.lambda_i') # radius
        # endregion

# ==== SETTING UP INPUTS ====
# region ==== FLIGHT CASE/SEGMENT (does not need to be changed) ====
case = 'cruise'                  # options are hover or cruise
if case == 'hover':
    thrust_dir = np.array([0., 0., 1.])
    in_plane_ex = np.array([[1., 0., 0.,]])

elif case == 'cruise':
    thrust_dir = np.array([-1., 0., 0.])
    in_plane_ex = np.array([[0., 0., 1.,]])
# endregion
    
# region ==== SETTING UP ROTOR LOCATION (do change based on configuration) ====
altitude = 0.
rotor_location = np.array([0., 0., altitude]) # rotor location in space
# endregion

# region ==== OBSERVER DATA (do change to set up custom observers) ====
observer_mode = 'single'
observer_pos = np.array([1.75, 0., 0.])

# UNCOMMENT BELOW IF DIRECTIVITY/MULTIPLE OBSEVERS ARE USED
# observer_mode = 'directivity'
# observer_pos = [
#     np.array([1., 0., 0.,]),
#     np.array([0.5, 0., 0.5,]),
#     np.array([0., 0., 1.,])
# ]

a = Acoustics(aircraft_position=rotor_location)
if observer_mode == 'single': # Options are single and directivity
    a.add_observer('observer_0', obs_position=observer_pos, time_vector=np.array([0.]))
elif observer_mode == 'directivity':
    for i in range():
        a.add_observer(f'observer_{i}', obs_position=observer_pos[i], time_vector=np.array([0.]))
observer_data = a.assemble_observers()
# endregion

# region ==== ORGANIZING DATA TO PUT INTO CSDL (do change based on experimental data) ====
import pickle
from lsdo_acoustics import ROOT
file_name = ROOT / 'core' / 'validation' / 'data_files' / 'loading_Jamaluddin.pkl'
file = open(str(file_name), 'rb')
data = pickle.load(file)
file.close()

inputs = {
    'num_blades': 2,
    'radius': 0.1524, # m
    'obs_loc': np.array([1.75, 0., 0.]),
    'mach': 0.0705,
    'RPM': 5500.,
    'num_radial': 40,
    'num_tangential': len(data['time'])
}

num_radial = inputs['num_radial']                 # radial discretization of data
num_tangential = inputs['num_tangential']              # tangential/temporal discretization of data 

num_blades = inputs['num_blades']
prop_radius = inputs['radius']
rpm = inputs['RPM']
chord_profile = 0.03176 * np.ones((num_radial,)) # shape must be (num_radial,)
mach_number = inputs['mach']
Vx = mach_number/343.
CT = 1. # thrust coefficient

thrust_origin = rotor_location

# Specific to Lowson
_dD = np.reshape(
    data['fx'],
    newshape=(1, data['fx'].shape[0], data['fx'].shape[1])
)
_dT = np.reshape(
    data['fz'],
    newshape=(1, data['fz'].shape[0], data['fz'].shape[1])
)

# Specific to KS
dTdR = (_dT/(prop_radius*0.8/num_radial))[:,:,0]
dDdR = (_dD/(prop_radius*0.8/num_radial))[:,:,0]
nondim_sectional_radius = np.linspace(0.2,1,num_radial) # 
lambda_i = np.linspace(0.07,0.1,num_radial) # LOCAL INDUCED INFLOW RATIO
# NOTE: we can also use phi, the local induced angle of attack, if this data is available
# endregion

# region ==== SETTING UP DUMMY MESH AND MODEL (no need to change)====
dummy_mesh = DummyMesh(
    num_radial=num_radial,
    num_tangential=num_tangential
)

model = AcousticsComparisonModel(
    dummy_mesh=dummy_mesh,
    num_blades=num_blades,
    num_nodes=1,
    observer_data=observer_data,
)
# endregion

sim = Simulator(model, analytics=False)

# PLEASE REFER TO THIS FOR A LIST OF CSDL VARIABLES NEEDED AS INPUTS
sim['propeller_radius'] = prop_radius
sim['chord_profile'] = chord_profile
sim['rpm'] = rpm
sim['thrust_origin'] = thrust_origin
sim['thrust_dir'] = thrust_dir
sim['CT'] = CT
sim['Vx'] = Vx  
sim['_dD'] = _dD
sim['_dT'] = _dT 
sim['mach_number'] = mach_number
sim['in_plane_ex'] = in_plane_ex
sim['dTdR_real'] = dTdR
sim['dDdR_real'] = dDdR
sim['lambda_i'] = lambda_i
sim['nondim_sectional_radius'] = nondim_sectional_radius

sim.run()

models = ['Lowson', 'KS', 'SKM', 'GL']
model_type = ['tonal', 'tonal', 'broadband', 'broadband']
print('==== PRINTING SPL OUTPUTS ====')
for i, model in enumerate(models):
    print('===='*5)
    print(f'{model} SPL values  (dB): ', sim[f'{model}_model.{model_type[i]}_spl'])
    print(f'A_weighted {model} SPL values (dB): ', sim[f'{model}_model.{model_type[i]}_spl_A_weighted'])