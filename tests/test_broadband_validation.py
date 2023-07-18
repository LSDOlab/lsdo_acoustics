import numpy as np
import csdl
from python_csdl_backend import Simulator
import csv

import pickle
from lsdo_acoustics import Acoustics, ROOT
from lsdo_acoustics.core.models.broadband.SKM.SKM_model import SKMBroadbandModel
from lsdo_acoustics.core.models.broadband.GL.GL_model import GLModel

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
            'num_tangential': num_tangential
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
    'obs_loc': np.array([float(val[1]) for val in rows[6:9]])
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

skm = SKMBroadbandModel(
    component_name='verif',
    mesh=mesh,
    observer_data=observer_data,
    num_blades=input_data['num_blades'],
    num_nodes=1,
    debug=True
)
sim_skm = Simulator(skm)

gl = GLModel(
    component_name='verif',
    mesh=mesh,
    observer_data=observer_data,
    num_blades=input_data['num_blades'],
    num_nodes=1,
    debug=True
)
sim_gl = Simulator(gl)

chord = input_data['chord']

skm_noise = []
gl_noise = []

skm_exp_error = []
skm_HJ_error = []
gl_exp_error = []
gl_HJ_error = []

num_cases = len(RPM)
for i in range(num_cases):
    sim_skm['rpm'] = input_data['RPM'][i]
    sim_skm['chord_profile'] = chord*np.ones((num_radial,))
    sim_skm['propeller_radius'] = input_data['radius']
    sim_skm['CT'] = input_data['CT'][i]
    sim_skm.run()
    skm_noise.append(sim_skm['verif_broadband_spl'][0][0])

    sim_gl['rpm'] = input_data['RPM'][i]
    sim_gl['chord_profile'] = chord*np.ones((num_radial,))
    sim_gl['propeller_radius'] = input_data['radius']
    sim_gl['CT'] = input_data['CT'][i]
    sim_gl.run()
    gl_noise.append(sim_gl['verif_broadband_spl'][0][0])

    # SKM ERRORS
    skm_HJ_error.append((HJ_SKM[i] - skm_noise[i]) / HJ_SKM[i])
    skm_exp_error.append((exp_data[i] - skm_noise[i]) / exp_data[i])

    # GL ERRORS
    gl_HJ_error.append((HJ_GL[i] - gl_noise[i]) / HJ_GL[i])
    gl_exp_error.append((exp_data[i] - gl_noise[i]) / exp_data[i])

