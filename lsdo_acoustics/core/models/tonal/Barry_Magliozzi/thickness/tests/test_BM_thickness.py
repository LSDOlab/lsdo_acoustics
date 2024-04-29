import numpy as np
# from lsdo_acoustics.core.models.tonal.Barry_Magliozzi.thickness.BM_thickness_model import BMThicknessModel
from lsdo_acoustics.core.models.tonal.Lowson.Lowson_model import LowsonModel
from python_csdl_backend import Simulator
from lsdo_acoustics import Acoustics

class DummyMesh(object):
    def __init__(self, num_radial, num_tangential):
        self.parameters = {
            'num_radial': num_radial,
            'num_tangential': num_tangential,
            'mesh_units': 'm'
        }


num_observers = 33
theta = np.linspace(10., 170, num_observers) * np.pi/180.
obs_dist = (1.8594751405**2+(-1.3020185105)**2)**0.5
z = obs_dist * np.cos(theta)
x = obs_dist * np.sin(theta)

obs_position_array = np.zeros((num_observers, 3))
obs_position_array[:,0] = x
obs_position_array[:,2] = z

a = Acoustics(aircraft_position=np.array([0.,0.,0.]))
for i in range(num_observers):
    a.add_observer(
        name=f'obs_{i}',
        obs_position=obs_position_array[i,:],
        time_vector=[0]
    )
observer_data = a.assemble_observers()

num_nodes = 1
num_blades = 4
modes = [1]
num_radial=40
t_c = 0.12
chord = 0.03176
R = .1588
RPM = 5500
nondim_sectional_radius = np.linspace(0.21, 0.99, 40)

dummy_mesh = DummyMesh(
    num_radial=num_radial,
    num_tangential=1
)

m = LowsonModel(
    mesh=dummy_mesh,
    num_blades=num_blades,
    observer_data=observer_data,
    modes=[1],
    # load_harmonics=,
    debug=True,
    use_geometry=False,
    toggle_thickness_noise=True
)

sim = Simulator(m, analytics=True)

sim['thrust_dir'] =  np.array([0., 0., 1.])
sim['origin'] = np.array([0., 0., 0.])
sim['in_plane_ex'] = np.array([1., 0., 0.])
sim['mach_number'] = np.zeros((num_nodes,))
sim['thickness_to_chord_ratio'] = t_c
sim['chord_profile'] = np.ones((num_radial,)) * chord
sim['propeller_radius'] = R
sim['nondim_sectional_radius'] = nondim_sectional_radius
sim['rpm'] = RPM
sim['speed_of_sound'] = 343.

sim.run()

thickness_noise = sim['rotor_thickness_spl'].reshape(num_observers,)

HJ_SPL_TM = np.array([-5.2059,
    8.6455,
   18.3101,
   25.6372,
   31.4505,
   36.1888,
   40.1133,
   43.3922,
   46.1391,
   48.4345,
   50.3363,
   51.8875,
   53.1198,
   54.0565,
   54.7145,
   55.1050,
   55.2344,
   55.1050,
   54.7145,
   54.0565,
   53.1198,
   51.8875,
   50.3363,
   48.4345,
   46.1391,
   43.3922,
   40.1133,
   36.1888,
   31.4505,
   25.6372,
   18.3101,
    8.6455,
   -5.2059
])

HJ_theta = np.linspace(10,170,33) *  np.pi/180. - np.pi/2.


import matplotlib.pyplot as plt
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
theta_plot = np.linspace(-np.pi/2, np.pi/2, num_observers)
ax.plot(theta-np.pi/2., thickness_noise, label='CSDL BM Thickness noise')
ax.plot(HJ_theta, HJ_SPL_TM.reshape(33,), label='HJ BM Thickness noise')
# ax.plot(theta_plot, spl_Lowson.reshape(num_observers,), label='Lowson')
# ax.plot((90. - Lowson_exp_data[:,0])*np.pi/180., Lowson_exp_data[:,1], label='Exp. data')
# ax.plot(theta_plot, spl_KS.reshape(num_observers,), label='KS')
# ax.set_rticks([55., 45., 35., 25.])
ax.set_rlabel_position(-120)
ax.grid(True)
plt.legend()

plt.figure()
plt.plot(HJ_theta * 180/np.pi, HJ_SPL_TM - thickness_noise)
plt.xlabel('Angle')
plt.ylabel('delta dB (exp. - CSDL)')
plt.grid(True)

plt.show()