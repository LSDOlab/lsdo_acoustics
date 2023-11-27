import numpy as np
import csdl

from lsdo_acoustics import Acoustics
from lsdo_acoustics.core.models.broadband.GL.GL_model import GLModel

from python_csdl_backend import Simulator

class DummyMesh(object):
    def __init__(self, num_radial, num_tangential):
        self.parameters = {
            'num_radial': num_radial,
            'num_tangential': num_tangential,
            'mesh_units': 'm'
        }

B = 2
R = 0.14
CT = np.array([0.0136, 0.014, 0.0148])
Mach = np.zeros_like(CT)
RPM = np.array([3600,4200,4800])

nondim_rad = np.array([
    0.14729694,
    0.202010172,
    0.250643054,
    0.300488287,
    0.352743347,
    0.402552631,
    0.451138408,
    0.502134011,
    0.551897429,
    0.60164969,
    0.646530234,
    0.699892277,
    0.749589995,
    0.806551902,
    0.850149437,
    0.905872961,
    0.954226928,
    1.001352428
])
dr = R*(nondim_rad[1:] - nondim_rad[:-1])
chord = np.array([
    0.11180406,
    0.136914976,
    0.158963403,
    0.180705023,
    0.198155813,
    0.211010826,
    0.221414732,
    0.227527808,
    0.229044734,
    0.227803748,
    0.222274162,
    0.213371191,
    0.198647076,
    0.179630642,
    0.156941082,
    0.131796325,
    0.084896932,
    0.034320693
]) * R

num_radial = len(nondim_rad)
dummy_mesh = DummyMesh(num_radial, 1)

a = Acoustics(aircraft_position=np.zeros(3,))
a.add_observer('dummy', np.array([1.3470, 0., -1.3470]), time_vector=np.array([0.]))
observer_data = a.assemble_observers()

freq_band = np.array([
    101.715445, 
    125.114991, 
    159.474581, 
    201.3104175, 
    251.6712975, 
    318.7527275, 
    401.0699282, 
    496.5439295, 
    643.2786269, 
    801.6156015, 
    1021.787454, 
    1273.254796, 
    1607.198901, 
    2015.696682, 
    2511.580936, 
    3119.280596, 
    4027.353363, 
    5018.482847, 
    6294.552364, 
    8127.112769, 
    10225.05432, 
    12494.64156, 
    15921.76722, 
    20026.3527, 
    25191.93854, 
    31386.48184
])

m = GLModel(
    mesh=dummy_mesh,
    observer_data=observer_data,
    num_blades=B,
    num_nodes=len(CT),
    debug=True,
    use_geometry=False,
    freq_band=freq_band
)

sim = Simulator(m, analytics=True)

sim['propeller_radius'] = R
sim['chord_profile'] = chord
sim['thrust_dir'] = np.array([0., 0., -1.])
sim['rpm'] = RPM
sim['CT'] = CT
# sim['dr'] = dr

sim.run()

print(sim['rel_angle_plane'] * 180./np.pi)
print(sim['broadband_spl'])
for i in range(len(CT)):
    print(sim['asdf'][i,0,:])