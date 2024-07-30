import numpy as np
import csdl_alpha as csdl

def sears_function(m, omega, r, R, c):
    Ut = omega*r*R
    k = m*omega*c/(2*Ut)

    # BESSEL ARGUMENT FOR F & G IS k
    J0 = csdl.bessel(k,1,0)
    J1 = csdl.bessel(k,1,1)
    Y0 = csdl.bessel(k,2,0)
    Y1 = csdl.bessel(k,2,1)

    # C-function from Hyunjune
    den_term_1 = J1+Y0
    den_term_2 = Y1-J0
    den = den_term_1**2 + (-1.*den_term_2)**2
    F = (J1*den_term_1 + Y1*den_term_2) / den
    G = -(Y1*Y0 + J1*J0) / den

    # Sears function (by modifying C-function)
    S_real = F*J0 + G*J1
    S_imag = (G*J0 - F*J1 + J1)
    
    return S_real, S_imag

def Sears_function_model(input_dict, num_nodes, num_blades, num_radial, num_azim, modes=[1,2,3], load_harmonics=np.arange(0,11,1), test=False):
    num_modes = len(modes)
    num_harmonics = len(load_harmonics)
    B = num_blades

    q = 0.06 # gust amplification factor
    rho = input_dict['density']
    RPM = input_dict['RPM']
    omega = RPM*2.*np.pi/60.

    R = input_dict['propeller_radius']
    a = input_dict['speed_of_sound']
    c = input_dict['chord_profile'] # (num_radial, )

    r = input_dict['nondim_sectional_radius']
    
    if test:
        dTdR = input_dict['_dTdR']
        dDdR = input_dict['_dDdR']

        dTdR_real = csdl.reshape(dTdR[:,:], (num_nodes, num_radial))
        dDdR_real = csdl.reshape(dDdR[:,:], (num_nodes, num_radial))
        
    else:
        dT = input_dict['dT']
        dD = input_dict['dD']
        dr = input_dict['dr']

        if dT.shape != (num_nodes, num_radial, num_azim):
            dT = dT.reshape((num_nodes, num_radial, num_azim))

        if dD.shape != (num_nodes, num_radial, num_azim):
            dD = dD.reshape((num_nodes, num_radial, num_azim))

        dTdR = dT / csdl.expand(dr, dT.shape)
        dDdR = dD / csdl.expand(dr, dD.shape)

        dTdR_real = csdl.reshape(dTdR[:,:,0], (num_nodes, num_radial))
        dDdR_real = csdl.reshape(dDdR[:,:,0], (num_nodes, num_radial))

    # region variable expansion
    target_shape = (num_nodes, B, num_harmonics, num_radial)
    r_exp = csdl.expand(r, target_shape, 'i->abci')
    omega_exp = csdl.expand(omega, target_shape)
    R_exp = csdl.expand(R, target_shape)
    a_exp = csdl.expand(a, target_shape)
    c_exp = csdl.expand(c, target_shape, 'i->abci')
    rho_exp = csdl.expand(rho, target_shape)
     # endregion

    r_uns = r_exp[:,:,1:,:]
    omega_uns = omega_exp[:,:,1:,:]
    R_uns = R_exp[:,:,1:,:]
    a_uns = a_exp[:,:,1:,:]
    c_uns = c_exp[:,:,1:,:]
    rho_uns = rho_exp[:,:,1:,:]
    if test:
        lambda_i = input_dict['lambda_i'].reshape((num_nodes, num_radial)) # (num_nodes, num_radial)
        lambda_i_exp = csdl.expand(lambda_i, target_shape, 'ij->iabj')
        phi_exp = lambda_i_exp / r_exp
    else:
        phi_input = input_dict['phi']
        if phi_input.shape != (num_nodes, num_radial, num_azim):
            phi_input = phi_input.reshape((num_nodes, num_radial, num_azim))
        
        phi = phi_input[:,:,0].reshape((num_nodes, num_radial)) # originally (nn, nr, na) and taking one azimuth
        phi_exp = csdl.expand(phi, target_shape, 'ij->iabj')
        lambda_i_exp = phi_exp*r_exp

    phi_uns = phi_exp[:,:,1:,:]
    lambda_i_uns = lambda_i_exp[:,:,1:,:]

    lam = np.ones(shape=target_shape)
    for i in range(num_harmonics):
        lam[:,:,i,:] = i
    lam_var = csdl.Variable(value=lam)

    aT_Sears = csdl.Variable(shape=target_shape, value=0.) # dTdR_real_exp
    aD_Sears = csdl.Variable(shape=target_shape, value=0.) # dDdR_real_exp 
    bT_Sears = csdl.Variable(shape=target_shape, value=0.) # dTdR_imag_exp
    bD_Sears = csdl.Variable(shape=target_shape, value=0.) # dDdR_imag_exp

    # print(dTdR_real.shape)
    aT_Sears = aT_Sears.set(csdl.slice[:,:,0,:], value=csdl.expand(dTdR_real, (num_nodes, B, num_radial), 'ij->iaj'))
    aD_Sears = aD_Sears.set(csdl.slice[:,:,0,:], value=csdl.expand(dDdR_real, (num_nodes, B, num_radial), 'ij->iaj'))

    # region Sears function
    S_real, S_imag = sears_function(lam_var[:,:,1:,:], omega_uns, r_uns, R_uns, c_uns)
    w_lam  = lambda_i_uns*omega_uns*R_uns/lam_var[:,:,1:,:]*q
    dLdR = rho_uns*(omega_uns*r_uns*R_uns)*c_uns*w_lam*np.pi
    Lreal = S_real*dLdR
    Limag = S_imag*dLdR
    # endregion

    aT_Sears = aT_Sears.set(csdl.slice[:,:,1:,:], value=Lreal*csdl.cos(phi_uns))
    aD_Sears = aD_Sears.set(csdl.slice[:,:,1:,:], value=Lreal*csdl.sin(phi_uns))
    bT_Sears = bT_Sears.set(csdl.slice[:,:,1:,:], value=Limag*csdl.cos(phi_uns))
    bD_Sears = bD_Sears.set(csdl.slice[:,:,1:,:], value=Limag*csdl.sin(phi_uns))
   
    return aT_Sears, aD_Sears, bT_Sears, bD_Sears