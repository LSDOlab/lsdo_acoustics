import numpy as np 
import csdl
from python_csdl_backend import Simulator

from lsdo_acoustics.core.acoustics import Acoustics
from lsdo_acoustics.core.models.tonal.Lowson.Lowson_model import LowsonModel
from lsdo_acoustics.core.models.tonal.KS.KvurtStalnov_model import KvurtStalnovModel

'''
This script runs a verification case for the newly-formulated Lowson model.

We check the "unsteady" steady loading in the hover case and compare it with data from Hyunjune.
'''

class DummyMesh(object):
    def __init__(self, num_radial, num_tangential):
        self.parameters = {
            'num_radial': num_radial,
            'num_tangential': num_tangential,
            'mesh_units': 'm'
        }

# observer data
a = Acoustics(aircraft_position=np.array([0., 0., 0.,]))

obs_radius = 1.5
num_observers = 37
theta = np.linspace(0, np.pi, num_observers)
z = obs_radius * np.cos(theta)
x = obs_radius * np.sin(theta)

obs_position_array = np.zeros((num_observers, 3))
obs_position_array[:,0] = x
obs_position_array[:,2] = z

for i in range(num_observers):
    a.add_observer(
        name=f'obs_{i}',
        obs_position=obs_position_array[i,:],
        time_vector=np.array([0.])
    )
observer_data = a.assemble_observers()

num_blades = 3
RPM = 1500
radius = 0.3556
M = 0
rho = 1.225
A = np.pi*radius**2
omega = RPM*2.*np.pi/60.

# KvurtStandard_Chord.csv GEOMETRY data
chord_profile_data = np.array([0.047937743, 0.051342412, 0.054552529, 
                          0.057470817, 0.057957198, 0.058249027, 
                          0.057276265, 0.056206226, 0.053968872, 
                          0.05192607, 0.049688716, 0.047159533, 
                          0.044727626, 0.042392996, 0.039863813, 
                          0.037723735, 0.035972763, 0.033735409, 
                          0.031984436, 0.029844358, 0.028385214, 
                          0.024785992, 0.021867704, 0.017879377])

nondim_sectional_radius_data = np.array([0.2, 0.233204633, 0.266409266, 
                                    0.294208494, 0.345945946, 0.393822394, 
                                    0.443243243, 0.49034749, 0.542857143, 
                                    0.593050193, 0.633976834, 0.682625483, 
                                    0.72046332, 0.758301158, 0.795366795, 
                                    0.824710425, 0.847876448, 0.877992278, 
                                    0.8996139, 0.925096525, 0.942857143, 
                                    0.962162162, 0.977606178, 0.984555985])

# geometry adjusted to the experimental data
nondim_sectional_radius = np.linspace(0.21, 0.99, 40)
# chord_profile = np.interp(nondim_sectional_radius, nondim_sectional_radius_data, chord_profile_data)
chord_profile = np.array([0.0491, 0.0511, 0.0529, 
                          0.0550, 0.0571, 0.0581, 
                          0.0581, 0.0579, 0.0581, 
                          0.0583, 0.0581, 0.0576, 
                          0.0571, 0.0567, 0.0562, 
                          0.0554, 0.0545, 0.0537, 
                          0.0529, 0.0521, 0.0510, 
                          0.0499, 0.0489, 0.0479, 
                          0.0467, 0.0454, 0.0441, 
                          0.0429, 0.0416, 0.0402, 
                          0.0388, 0.0373, 0.0358, 
                          0.0343, 0.0328, 0.0310, 
                          0.0296, 0.0271, 0.0238, 
                          0.0124])
num_radial = len(chord_profile)

# experimental data
dCTdr = np.array([0.001418, 0.002502, 0.003372, 
                  0.004193, 0.005004, 0.005819, 
                  0.006643, 0.007475, 0.008313, 
                  0.009155, 0.009995, 0.010830, 
                  0.011654, 0.012463, 0.013251, 
                  0.014012, 0.014741, 0.015433, 
                  0.016083, 0.016684, 0.017231, 
                  0.017720, 0.018144, 0.018498, 
                  0.018776, 0.018974, 0.019087, 
                  0.019108, 0.019033, 0.018856, 
                  0.018572, 0.018173, 0.017652, 
                  0.017000, 0.016202, 0.015237, 
                  0.014065, 0.012604, 0.010648, 
                  0.007315])

# multiply by rho*A*V**2 (LEAVE OUT THE 1/2)
# A is the area of the disk (including the hub, so use pi*R**2)
dTdR = dCTdr*rho*A*(omega)**2 * radius

dCDdr = np.array([0.382386, 0.472668, 0.513254, 
                  0.535224, 0.547541, 0.554094, 
                  0.556868, 0.556999, 0.555171, 
                  0.551836, 0.547306, 0.541799, 
                  0.535481, 0.528476, 0.520885, 
                  0.512789, 0.504252, 0.495329, 
                  0.486071, 0.476518, 0.466704, 
                  0.456663, 0.446425, 0.436012, 
                  0.425447, 0.414750, 0.403942, 
                  0.393037, 0.382048, 0.370986, 
                  0.359856, 0.348660, 0.337389, 
                  0.326024, 0.314518, 0.302778, 
                  0.290617, 0.277627, 0.262714, 
                  0.241180])

lambda_i = np.array([0.067510, 0.066167, 0.066825, 
                     0.068136, 0.069702, 0.071347, 
                     0.072980, 0.074549, 0.076028, 
                     0.077399, 0.078652, 0.079780, 
                     0.080780, 0.081651, 0.082391, 
                     0.082999, 0.083478, 0.083825, 
                     0.084042, 0.084127, 0.084082, 
                     0.083906, 0.083598, 0.083157, 
                     0.082584, 0.081878, 0.081037, 
                     0.080060, 0.078948, 0.077700, 
                     0.076319, 0.074807, 0.073175, 
                     0.071434, 0.069614, 0.067770, 
                     0.066009, 0.064569, 0.064084, 
                     0.067274])

CL = np.array([0.650342, 0.956401, 1.090936, 
               1.163009, 1.203194, 1.224505, 
               1.233513, 1.233939, 1.228004, 
               1.217168, 1.202426, 1.184479, 
               1.163851, 1.140926, 1.116029, 
               1.089405, 1.061251, 1.031740, 
               1.001031, 0.969240, 0.936476, 
               0.902841, 0.868424, 0.833295, 
               0.797525, 0.761172, 0.724300, 
               0.686955, 0.649177, 0.610993, 
               0.572421, 0.533463, 0.494077, 
               0.454196, 0.413648, 0.372091, 
               0.328847, 0.282429, 0.228851, 
               0.150922])

# DON'T USE THE DATA FOR dCDdr, USE THE APPROACH IN HIS CODE (LOOK AT VALIDATION TEST CASE FOR MORE INFO)

dr = 0.02 * radius
sigma = dr*np.sum((chord_profile[:-1] + chord_profile[1:])/2) * num_blades / A
dCQdr = 0.5*sigma*CL*lambda_i*nondim_sectional_radius**2
dQdR = rho*A*(omega**2*radius**2)*dCQdr
dDdR = dQdR / (nondim_sectional_radius*radius)

dLdR_s = 0.5*rho*chord_profile*(radius*omega)**2 * CL

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
    use_geometry=False
)

sim = Simulator(m, analytics=True)

sim['propeller_radius'] = radius
sim['rpm'] = RPM
sim['thrust_dir'] = np.array([0., 0., 1.])
sim['origin'] = np.array([0., 0., 0.])
sim['chord_profile'] = chord_profile
sim['in_plane_ex'] = np.array([1., 0., 0.])
sim['mach_number'] = M
# sim['_dTdR'] = dTdR * nondim_sectional_radius
# sim['_dDdR'] = dDdR * nondim_sectional_radius
sim['_dTdR'] = dLdR_s * np.cos(lambda_i/nondim_sectional_radius)
sim['_dDdR'] = dLdR_s * np.sin(lambda_i/nondim_sectional_radius)
sim['lambda_i'] = lambda_i
sim['nondim_sectional_radius'] = nondim_sectional_radius

sim.run()
spl_Lowson = sim['tonal_spl_compute']
spl_Lowson_A_weighted = sim['tonal_spl_A_weighted']
Lowson_unsteady_aT = sim['aT_Sears']
Lowson_unsteady_aD = sim['aD_Sears']
Lowson_unsteady_bT = sim['bT_Sears']
Lowson_unsteady_bD = sim['bD_Sears']

# m = KvurtStalnovModel(
#     mesh=dummy_mesh,
#     num_blades=num_blades,
#     observer_data=observer_data,
#     # modes=,
#     # load_harmonics=,
#     debug=True,
#     use_geometry=False
# )

# sim = Simulator(m)

# sim['propeller_radius'] = radius
# sim['rpm'] = RPM
# sim['thrust_dir'] = np.array([0., 0., 1.])
# sim['origin'] = np.array([0., 0., 0.])
# sim['chord_profile'] = chord_profile
# # sim['in_plane_ex'] = np.array([1., 0., 0.])
# # sim['mach_number'] = M
# sim['dTdR_real'] = dTdr
# sim['dDdR_real'] = dDdr
# sim['lambda_i'] = lambda_i
# sim['nondim_sectional_radius'] = nondim_sectional_radius

# sim.run()
# spl_KS = sim['tonal_spl']
# spl_KS_A_weighted = sim['tonal_spl_A_weighted']
# KS_dTdR_real = sim['dTdR_real_exp']
# KS_dTdR_imag = sim['dTdR_imag_exp']
# KS_dDdR_real = sim['dDdR_real_exp']
# KS_dDdR_imag = sim['dDdR_imag_exp']

print('Lowson SPL (dB): ', spl_Lowson)
print('Lowson A-weighted SPL (dBA): ', spl_Lowson_A_weighted)
# print('KS SPL (dB): ', spl_KS)
# print('KS A-weighted SPL (dBA): ', spl_KS_A_weighted)

Lowson_HG_MATLAB = np.array([56.09030376, 56.05900428, 55.959839, 
                        55.79123069, 55.55058298, 55.23416832, 
                        54.83700993, 54.35281411, 53.77406123, 
                        53.09246373, 52.30020539, 51.39280254, 
                        50.37525646, 49.27442523, 48.16076518, 
                        47.17445812, 46.52037166, 46.3711999, 
                        46.72683781, 47.41997678, 48.25942433, 
                        49.12136842, 49.95023478, 50.73060024, 
                        51.46395235, 52.15517066, 52.80625136, 
                        53.41469247, 53.97452335, 54.47835522, 
                        54.91931082, 55.29226174, 55.59427014, 
                        55.82439018, 55.98306853, 56.07137996, 
                        56.09030376])
Lowson_HG_theta = np.linspace(np.pi/2, -np.pi/2, len(Lowson_HG_MATLAB))


Lowson_exp_data = np.zeros((16,2))
Lowson_exp_data[:,0] = np.array([0 ,7.479641242 ,15.03601545 ,
                                 22.29715788 ,30.03328044 ,37.793943 ,
                                 45.19291435 ,52.73843809 ,59.87876773 ,
                                 67.59578772 ,74.83689096 ,74.83689096 ,
                                 82.20792192 ,89.85118013 ,97.4691854 ,
                                 104.9314172])

Lowson_exp_data[:,1] = np.array([57.40552099, 56.83751618, 56.58951333, 
                                 55.69409618, 54.8948303, 53.83251151, 
                                 52.26290671, 51.09803395, 49.63700234,
                                 48.71564441, 48.04448109, 48.04448109, 
                                 48.18220778, 48.34550388, 49.16512923, 
                                 50.42903289])

import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
theta_plot = np.linspace(-np.pi/2, np.pi/2, num_observers)
ax.plot(np.linspace(np.pi/2, -np.pi/2, len(Lowson_HG_MATLAB)), Lowson_HG_MATLAB, label='HG Matlab')
ax.plot(theta_plot, spl_Lowson.reshape(num_observers,), label='Lowson')
ax.plot((90. - Lowson_exp_data[:,0])*np.pi/180., Lowson_exp_data[:,1], label='Exp. data')
# ax.plot(theta_plot, spl_KS.reshape(num_observers,), label='KS')
ax.set_rticks([55., 45., 35., 25.])
ax.set_rlabel_position(-120)

ax.grid(True)
plt.legend()

if num_observers == len(Lowson_HG_MATLAB):
    Lowson_error = (spl_Lowson.reshape(num_observers,) - Lowson_HG_MATLAB[::-1])/Lowson_HG_MATLAB[::-1] * 100
    print('Lowson error percentage: ', Lowson_error)

    plt.figure()
    plt.plot(theta_plot * 180./np.pi, Lowson_error)
    plt.title('Lowson Model Error Percentage')
    plt.xlabel('Angle (deg)')
    plt.ylabel('Error (%)')
    plt.grid()


plt.show()

# NOTE: THE DATA ONLY USES THE FIRST MODE (m=1 in Hyunjune's code) SO REDO FOR THAT
# ADD EXPERIMENTAL DATA TO PLOT
# SEPARATE THE UNSTEADY AND STEADY COMPONENTS AND PLOT






