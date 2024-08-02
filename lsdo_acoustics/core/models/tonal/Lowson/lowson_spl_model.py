import numpy as np
import csdl_alpha as csdl 

def Lowson_spl_model(Lowson_inputs, num_nodes, num_observers, B, num_radial, modes=[1,2,3], harmonics=np.arange(0,11,1)):
    P_ref = 2.e-5
    num_modes = len(modes)
    num_harmonics = len(harmonics)

    a = Lowson_inputs['a']
    R = Lowson_inputs['propeller_radius']
    r = Lowson_inputs['nondim_sectional_radius']
    dr = Lowson_inputs['dr']

    # rpm = csdl.reshape(Lowson_inputs['rpm'], (num_nodes,))
    rpm = Lowson_inputs['rpm']
    omega = rpm*2.*np.pi/60.

    # x = csdl.reshape(Lowson_inputs.rel_obs_x_pos, (num_nodes, num_observers))
    # y = csdl.reshape(Lowson_inputs.rel_obs_y_pos, (num_nodes, num_observers))
    # z = csdl.reshape(Lowson_inputs.rel_obs_z_pos, (num_nodes, num_observers))
    S = csdl.reshape(Lowson_inputs['rel_obs_dist'], (num_nodes, num_observers))
    P = Lowson_inputs['rel_obs_position'] # shape is (nn, 3, num_obs)

    if num_nodes == 1:
        Vx = csdl.expand(Lowson_inputs['Vx'], (num_nodes, num_observers))
        Vy = csdl.expand(Lowson_inputs['Vy'], (num_nodes, num_observers))
        Vz = csdl.expand(Lowson_inputs['Vz'], (num_nodes, num_observers))
    else:
        Vx = csdl.expand(Lowson_inputs['Vx'], (num_nodes, num_observers), 'i->ia')
        Vy = csdl.expand(Lowson_inputs['Vy'], (num_nodes, num_observers), 'i->ia')
        Vz = csdl.expand(Lowson_inputs['Vz'], (num_nodes, num_observers), 'i->ia')

    r1 = convection_adjustment(P, S, Vx, Vy, Vz, a)

    thrust_dir = csdl.expand(Lowson_inputs['thrust_dir'], (num_nodes, 3, num_observers), 'i->aib')

    z_in_frame = csdl.sum(thrust_dir*P, axes=(1,))
    Y_in_frame = (S**2 - z_in_frame**2+1.e-12)**0.5

    aT_uns = Lowson_inputs['aT_uns']
    aD_uns = Lowson_inputs['aD_uns']
    bT_uns = Lowson_inputs['bT_uns']
    bD_uns = Lowson_inputs['bD_uns']

    aT_Sears = Lowson_inputs['aT_Sears']
    aD_Sears = Lowson_inputs['aD_Sears']
    bT_Sears = Lowson_inputs['bT_Sears']
    bD_Sears = Lowson_inputs['bD_Sears']

    # ======== VARIABLE EXPANSION ======== 
    target_shape =  (num_nodes, num_observers, num_modes, B, num_harmonics, num_radial)
    if num_nodes == 1:
        omega_exp = csdl.expand(omega, target_shape)
        # r_exp = csdl.expand(r, target_shape)
    else:
        omega_exp = csdl.expand(omega, target_shape, 'i->iabcde')
    r_exp = csdl.expand(r, target_shape, 'i->abcdei')

    z_exp = csdl.expand(z_in_frame, target_shape, 'ij->ijabcd')
    Y_exp = csdl.expand(Y_in_frame, target_shape, 'ij->ijabcd')
    a_exp = csdl.expand(a, target_shape)
    r1_exp = csdl.expand(r1, target_shape, 'ij->ijabcd')
    R_exp = csdl.expand(R, target_shape)

    coeff_target_shape = (num_nodes, num_observers, num_modes, B, num_harmonics, num_radial) 
    aT_uns_exp = csdl.expand(aT_uns, coeff_target_shape, 'ijkl->iabjkl')
    aD_uns_exp = csdl.expand(aD_uns, coeff_target_shape, 'ijkl->iabjkl')
    bT_uns_exp = csdl.expand(bT_uns, coeff_target_shape, 'ijkl->iabjkl')
    bD_uns_exp = csdl.expand(bD_uns, coeff_target_shape, 'ijkl->iabjkl')

    aT_Sears_exp = csdl.expand(aT_Sears, coeff_target_shape, 'ijkl->iabjkl')
    aD_Sears_exp = csdl.expand(aD_Sears, coeff_target_shape, 'ijkl->iabjkl')
    bT_Sears_exp = csdl.expand(bT_Sears, coeff_target_shape, 'ijkl->iabjkl')
    bD_Sears_exp = csdl.expand(bD_Sears, coeff_target_shape, 'ijkl->iabjkl')

    # region fourier coefficient setup
    n = np.ones(shape=coeff_target_shape)
    for i in range(num_modes):
        n[:,:,i,:,:,:] = modes[i]*B
    n_var = csdl.Variable(value=n)
    lam = np.ones(shape=coeff_target_shape)
    for i in range(num_harmonics):
        lam[:,:,:,:,i,:] = i
    lam_var = csdl.Variable(value=lam)
    ind = n-lam

    term_1_coeff_A = np.ones_like(n)
    term_2_coeff_A = np.ones_like(n)
    term_1_coeff_B = np.ones_like(n)
    term_2_coeff_B = np.ones_like(n)

    coeff_sign_matrix_even = np.zeros_like(n)
    coeff_sign_matrix_odd = np.zeros_like(n)

    A_lin_comb_sign_matrix = np.ones_like(n)
    B_lin_comb_sign_matrix = np.ones_like(n)

    for i in range(num_modes):
        m = modes[i] * B            
        for j in range(num_harmonics):
            ind = m-j
            if np.mod(ind,2) == 0:
                coeff_sign_matrix_even[:,:,i,:,j,:] = 1.
                A_lin_comb_sign_matrix[:,:,i,:,j,:] = -1.
                B_lin_comb_sign_matrix[:,:,i,:,j,:] = 1.
                # A
                if np.mod(ind, 4) == 2:
                    term_1_coeff_A[:,:,i,:,j,:] = 1.
                    term_2_coeff_A[:,:,i,:,j,:] = -1.
                elif np.mod(ind, 4) == 0:
                    term_1_coeff_A[:,:,i,:,j,:] = -1.
                    term_2_coeff_A[:,:,i,:,j,:] = 1.

                # B
                if (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==1):
                    term_1_coeff_B[:,:,i,:,j,:] = -1.
                    term_2_coeff_B[:,:,i,:,j,:] = 1.

                elif (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==3):
                    term_1_coeff_B[:,:,i,:,j,:] = 1.
                    term_2_coeff_B[:,:,i,:,j,:] = -1.

                elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==1):
                    term_1_coeff_B[:,:,i,:,j,:] = 1.
                    term_2_coeff_B[:,:,i,:,j,:] = -1.

                elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==3):
                    term_1_coeff_B[:,:,i,:,j,:] = -1.
                    term_2_coeff_B[:,:,i,:,j,:] = 1.

            elif np.mod(ind,2) == 1:
                coeff_sign_matrix_odd[:,:,i,:,j,:] = 1.
                A_lin_comb_sign_matrix[:,:,i,:,j,:] = 1.
                B_lin_comb_sign_matrix[:,:,i,:,j,:] = -1.
                # A
                if np.mod(ind, 4) == 2:
                    term_1_coeff_A[:,:,i,:,j,:] = -1.
                    term_2_coeff_A[:,:,i,:,j,:] = 1.
                elif np.mod(ind, 4) == 0:
                    term_1_coeff_A[:,:,i,:,j,:] = 1.
                    term_2_coeff_A[:,:,i,:,j,:] = -1.

                # B
                if (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==1):
                    term_1_coeff_B[:,:,i,:,j,:] = 1.
                    term_2_coeff_B[:,:,i,:,j,:] = -1.

                elif (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==3):
                    term_1_coeff_B[:,:,i,:,j,:] = -1.
                    term_2_coeff_B[:,:,i,:,j,:] = 1.

                elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==1):
                    term_1_coeff_B[:,:,i,:,j,:] = -1.
                    term_2_coeff_B[:,:,i,:,j,:] = 1.

                elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==3):
                    term_1_coeff_B[:,:,i,:,j,:] = 1.
                    term_2_coeff_B[:,:,i,:,j,:] = -1.

    term_1_constant = n_var*omega_exp*z_exp/(a_exp*r1_exp**2)
    term_2_constant = 1. / (R_exp*r_exp*r1_exp)
    bessel_input = n_var*omega_exp*R_exp*r_exp*Y_exp/(a_exp*r1_exp)
    # endregion

    # region unsteady SPL (original Lowson)
    
    # TERM A
    term_1_A_fc = (coeff_sign_matrix_even * bT_uns_exp + coeff_sign_matrix_odd * aT_uns_exp) # weighting based on sign of n-lambda
    term_2_A_fc = (coeff_sign_matrix_even * bD_uns_exp + coeff_sign_matrix_odd * aD_uns_exp) # weighting based on sign of n-lambda
    term_1_A = term_1_constant*term_1_A_fc*(csdl.bessel(bessel_input, order=n-lam) + \
    A_lin_comb_sign_matrix*csdl.power(-1., lam_var) * csdl.bessel(bessel_input, order=n+lam))
    term_2_A = term_2_constant * term_2_A_fc * ((n_var-lam_var)*csdl.bessel(bessel_input, order=n-lam) + \
    A_lin_comb_sign_matrix*csdl.power(-1., lam_var) *(n_var+lam_var)*csdl.bessel(bessel_input, order=n+lam))
    
    a_n_radial_harmonics = (term_1_coeff_A*term_1_A + term_2_coeff_A*term_2_A)/(4*np.pi) 

    # TERM B
    term_1_B_fc = (coeff_sign_matrix_even * aT_uns_exp + coeff_sign_matrix_odd * bT_uns_exp) # weighting based on sign of n-lambda
    term_2_B_fc = (coeff_sign_matrix_even * aD_uns_exp + coeff_sign_matrix_odd * bD_uns_exp) # weighting based on sign of n-lambda
    term_1_B = term_1_constant*term_1_B_fc*(csdl.bessel(bessel_input, order=n-lam) + \
    B_lin_comb_sign_matrix * csdl.power(-1., lam_var) *csdl.bessel(bessel_input, order=n+lam))
    term_2_B = term_2_constant * term_2_B_fc * ((n_var-lam_var)*csdl.bessel(bessel_input, order=n-lam) + \
    B_lin_comb_sign_matrix*csdl.power(-1., lam_var) *(n_var+lam_var)*csdl.bessel(bessel_input, order=n+lam))

    b_n_radial_harmonics = (term_1_coeff_B*term_1_B + term_2_coeff_B*term_2_B) / (4*np.pi)

    a_n_radial = csdl.sum(a_n_radial_harmonics, axes=(4,)) # first over harmonics
    b_n_radial = csdl.sum(b_n_radial_harmonics, axes=(4,)) # first over harmonics
    
    An = csdl.sum(a_n_radial, axes=(4,)) # now over radial dimension
    Bn = csdl.sum(b_n_radial, axes=(4,)) # now over radial dimension
    sum_A_B = (An)**2 + (Bn)**2
    
    bladeSPL = 10.*csdl.log(sum_A_B/(2*P_ref**2), base=10.)

    ex = csdl.power(10., bladeSPL/10.)
    ex_sum = csdl.sum(ex, axes=(3,))

    SPL_m = 10.*csdl.log(ex_sum, base=10.)

    spl_unsteady = 10*csdl.log(csdl.sum(csdl.power(10.,SPL_m/10.), axes=(2,)), base=10.) # SHAPE IS (num_nodes, num_observers)
    # endregion

    # region Sears SPL

    # TERM A
    term_1_A_fc = (coeff_sign_matrix_even * bT_Sears_exp + coeff_sign_matrix_odd * aT_Sears_exp) # weighting based on sign of n-lambda
    term_2_A_fc = (coeff_sign_matrix_even * bD_Sears_exp + coeff_sign_matrix_odd * aD_Sears_exp) # weighting based on sign of n-lambda

    term_1_A = term_1_constant*term_1_A_fc*(csdl.bessel(bessel_input, order=n-lam) + \
    A_lin_comb_sign_matrix*csdl.power(-1., lam_var) * csdl.bessel(bessel_input, order=n+lam))
    term_2_A = term_2_constant * term_2_A_fc * ((n_var-lam_var)*csdl.bessel(bessel_input, order=n-lam) + \
    A_lin_comb_sign_matrix*csdl.power(-1., lam_var) *(n_var+lam_var)*csdl.bessel(bessel_input, order=n+lam))
    
    a_n_radial_harmonics = (term_1_coeff_A*term_1_A + term_2_coeff_A*term_2_A)/(4*np.pi) * B

    # TERM B
    term_1_B_fc = (coeff_sign_matrix_even * aT_Sears_exp + coeff_sign_matrix_odd * bT_Sears_exp) # weighting based on sign of n-lambda
    term_2_B_fc = (coeff_sign_matrix_even * aD_Sears_exp + coeff_sign_matrix_odd * bD_Sears_exp) # weighting based on sign of n-lambda

    term_1_B = term_1_constant*term_1_B_fc*(csdl.bessel(bessel_input, order=n-lam) + \
    B_lin_comb_sign_matrix * csdl.power(-1., lam_var) *csdl.bessel(bessel_input, order=n+lam))
    term_2_B = term_2_constant * term_2_B_fc * ((n_var-lam_var)*csdl.bessel(bessel_input, order=n-lam) + \
    B_lin_comb_sign_matrix*csdl.power(-1., lam_var) *(n_var+lam_var)*csdl.bessel(bessel_input, order=n+lam))

    b_n_radial_harmonics = (term_1_coeff_B*term_1_B + term_2_coeff_B*term_2_B) / (4*np.pi) * B

    # RADIAL INTEGRATION
    dr_integration = csdl.expand(dr, coeff_target_shape[:-1])
    A_n_trapz_harmonics = csdl.sum(
        a_n_radial_harmonics[:,:,:,:,:,:-1] + a_n_radial_harmonics[:,:,:,:,:,1:],
        axes=(5,)
    ) / 2. * dr_integration[:,:,:,:,:]
    B_n_trapz_harmonics = csdl.sum(
        b_n_radial_harmonics[:,:,:,:,:,:-1] + b_n_radial_harmonics[:,:,:,:,:,1:],
        axes=(5,)
    ) / 2. * dr_integration[:,:,:,:,:]

    A_n_trapz_s = csdl.reshape(A_n_trapz_harmonics[:,:,:,:,0], coeff_target_shape[:-2]) # STEADY
    B_n_trapz_s = csdl.reshape(B_n_trapz_harmonics[:,:,:,:,0], coeff_target_shape[:-2]) # STEADY
    A_n_trapz_uns = csdl.sum(A_n_trapz_harmonics[:,:,:,:,1:], axes=(4,)) # UNSTEADY
    B_n_trapz_uns = csdl.sum(B_n_trapz_harmonics[:,:,:,:,1:], axes=(4,)) # UNSTEADY

    C_n_trapz_s = A_n_trapz_s**2 + B_n_trapz_s**2
    SPL_steady_Sears = 10.*csdl.log(C_n_trapz_s/(2*P_ref**2), base=10.)
    C_n_trapz_uns = A_n_trapz_uns**2 + B_n_trapz_uns**2
    SPL_unsteady_Sears = 10.*csdl.log(C_n_trapz_uns/(2*P_ref**2), base=10.)
    # shape = (num_nodes, num_observers, num_modes, num_blades)

    SPL_per_mode_per_blade = 10*csdl.log(
        csdl.power(10., SPL_steady_Sears/10.) + csdl.power(10., SPL_unsteady_Sears/10.),
        base=10.
    )

    SPL_m = csdl.reshape(SPL_per_mode_per_blade[:,:,:,0], (num_nodes, num_observers, num_modes))

    spl_Sears = 10*csdl.log(csdl.sum(csdl.power(10.,SPL_m/10.), axes=(2,)), base=10.) # SHAPE IS (num_nodes, num_observers)
    # endregion

    return spl_unsteady, spl_Sears, sum_A_B, C_n_trapz_s, C_n_trapz_uns


def convection_adjustment(P, S, Vx, Vy, Vz, a):
    num_nodes, num_observers = P.shape[0], P.shape[2]

    velocity = csdl.Variable(shape=P.shape, value=0.)
    velocity = velocity.set(csdl.slice[:,0,:], value=Vx)
    velocity = velocity.set(csdl.slice[:,1,:], value=Vy)
    velocity = velocity.set(csdl.slice[:,2,:], value=Vz)
    v_comp_obs = csdl.sum(velocity*P, axes=(1,)) / S

    r1 = S*(1-v_comp_obs/csdl.expand(a, v_comp_obs.shape))
    return r1