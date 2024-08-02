import numpy as np
import csdl_alpha as csdl
from python_csdl_backend import Simulator
import csv

import pickle
from lsdo_acoustics import Acoustics, ROOT
from lsdo_acoustics.core.models.broadband.GL.GL_model import GL_model, GLVariableGroup
from lsdo_acoustics.core.models.total_noise_model import total_noise_model

'''
This file is a validation test for the SKM and GL broadband noise models.

The input files currently supported are:
    - IdealTwist4PitchInput.csv (hover)
    - BO105ForwardInput.csv (forward flight)
'''

# dummy mesh object
class DummyMesh(object):
    def __init__(self, num_radial, num_tangential):
        self.parameters = {
            'num_radial': num_radial,
            'num_tangential': num_tangential,
            'mesh_units': 'm'
        }

# region input file + data
        
file_name = 'IdealTwist4PitchInput.csv'
file_path = ROOT / 'core' / 'validation' / 'data_files' / file_name
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

RPM = []
CT = []
# M = []
exp_data = []
HJ_SKM = []
HJ_GL = []

for i in range(1,len(rows[5])):
    RPM.append(float(rows[5][i]))
    CT.append(float(rows[9][i]))
    # M.append(float(rows[12][i]))
    exp_data.append(float(rows[13][i]))
    HJ_SKM.append(float(rows[14][i]))
    HJ_GL.append(float(rows[15][i]))

input_data = {
    'num_blades': int(rows[1][1]),
    'chord': float(rows[2][1]),
    'radius': float(rows[3][1]),
    'RPM': np.array(RPM),
    'CT': np.array(CT),
    # 'M': np.array(M),
    # 'obs_loc': np.array([float(val[1]) for val in rows[6:9]])*2.
    'obs_loc': np.array([3., 0., 0.])*5
}
# endregion
num_radial=5
mesh = DummyMesh(
    num_radial=num_radial,
    num_tangential=1 # this input is useless but kept for now in case it's needed in the future
)

broadband_acoustics = Acoustics(aircraft_position=np.array([0.,0.,0.]))
broadband_acoustics.add_observer('obs', input_data['obs_loc'], time_vector=np.array([0.]))
observer_data = broadband_acoustics.assemble_observers()

chord = input_data['chord']

gl_noise = []
gl_exp_error = []
gl_HJ_error = []

num_cases = len(RPM)
num_nodes = 1
velocity = np.zeros((num_nodes, 3))
recorder = csdl.Recorder(inline=True)
recorder.start()

for i in range(num_cases):

    RPM = csdl.Variable(value=input_data['RPM'][i])

    gl_vg = GLVariableGroup(
        thrust_vector=np.array([0., 0., -1.]),
        thrust_origin=np.array([0., 0., 0.]),
        CT=np.array([input_data['CT'][i]]),
        rotor_radius=input_data['radius'],
        chord_profile=chord*np.ones((num_radial,)),
        mach_number=0.,
        speed_of_sound=340.3,
        rpm=RPM,
        mesh=mesh,
        num_radial=num_radial,
        # chord_length=0,
        # theta=0,
    )

    gl_spl, gl_spl_A_weighted = GL_model(
        GLVariableGroup=gl_vg,
        observer_data=observer_data,
        num_blades=input_data['num_blades'],
        num_nodes=num_nodes,
        debug=True,
        A_weighting=True
    )

    print(f'GL noise: {gl_spl.value}')
    print(f'A-weighted GL noise: {gl_spl_A_weighted.value}')
    
    gl_noise.append(gl_spl)

    # GL ERRORS
    gl_HJ_error.append((HJ_GL[i] - gl_noise[i].value) / HJ_GL[i])
    gl_exp_error.append((exp_data[i] - gl_noise[i].value) / exp_data[i])

    asdf = csdl.derivative(ofs=gl_spl, wrts=RPM)
    print(f'derivative value: {asdf.value}')

print('================ spl values: ================')
print([spl.value[0] for spl in gl_noise])

print('================ gl error (%): ================')
print([error[0] for error in gl_exp_error])


total_spl = total_noise_model(SPL_list = gl_noise)
print(total_spl.value)
recorder.stop()