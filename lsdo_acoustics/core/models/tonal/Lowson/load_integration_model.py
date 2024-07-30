import csdl_alpha as csdl
import numpy as np

def load_integration_model(load_integration_inputs, num_nodes, num_blades, num_radial, num_azim, load_harmonics=np.arange(0,11,1)):
    num_harmonics = len(load_harmonics)
    dD = load_integration_inputs['dD'] # sectional loads (num_nodes, num_radial, num_azim)
    dT = load_integration_inputs['dT'] # sectional loads

    if dD.shape != (num_nodes, num_radial, num_azim):
        dD = dD.reshape((num_nodes, num_radial, num_azim))
        dT = dT.reshape((num_nodes, num_radial, num_azim))

    dD_exp = csdl.expand(dD, (num_nodes, num_blades, num_radial, num_azim), 'ijk->iajk')
    dT_exp = csdl.expand(dT, (num_nodes, num_blades, num_radial, num_azim), 'ijk->iajk')

    radial_sum_dD = csdl.sum(dD_exp, axes=(2,))
    radial_sum_dT = csdl.sum(dT_exp, axes=(2,))

    theta = np.linspace(0., 2*np.pi, num_azim) # we assume num_azim is the number of azimuthal divisions in ONE ROTATION
    n_theta_prod = np.outer(load_harmonics, theta) # (num_harmonics, num_azim)
    cos_vec = csdl.expand(csdl.cos(n_theta_prod), (num_nodes, num_blades, num_harmonics, num_radial, num_azim), 'ij->abicj')
    sin_vec = csdl.expand(csdl.sin(n_theta_prod), (num_nodes, num_blades, num_harmonics, num_radial, num_azim), 'ij->abicj')

    target_shape = (num_nodes, num_blades, num_harmonics, num_radial, num_azim)
    aT_integrand = csdl.expand(dT_exp, target_shape, 'ijkl->ijakl') * cos_vec
    aD_integrand = csdl.expand(dD_exp, target_shape, 'ijkl->ijakl') * cos_vec
    bT_integrand = csdl.expand(dT_exp, target_shape, 'ijkl->ijakl') * sin_vec * -1.
    bD_integrand = csdl.expand(dD_exp, target_shape, 'ijkl->ijakl') * sin_vec * -1.

    # add trapeziod method here
    h = 2.*np.pi/num_azim
    aT = 1/(2.*np.pi)*csdl.sum(aT_integrand, axes=(4,)) * csdl.expand(h, target_shape[:4])
    aD = 1/(2.*np.pi)*csdl.sum(aD_integrand, axes=(4,)) * csdl.expand(h, target_shape[:4])
    bT = 1/(2.*np.pi)*csdl.sum(bT_integrand, axes=(4,)) * csdl.expand(h, target_shape[:4])
    bD = 1/(2.*np.pi)*csdl.sum(bD_integrand, axes=(4,)) * csdl.expand(h, target_shape[:4])

    return aT, aD, bT, bD