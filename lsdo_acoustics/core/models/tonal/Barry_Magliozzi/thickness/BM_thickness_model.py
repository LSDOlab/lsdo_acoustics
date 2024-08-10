import numpy as np
import csdl_alpha as csdl 

def BM_thickness_model(BM_inputs, num_nodes, num_blades, num_observers, num_radial, modes=[1,2,3]):
    '''
    The equations here are based on this paper:
    Applicability of Low-Fidelity Tonal and Broadband Noise Models on Small-Scale Rotors
    Hyunjune Gill, Seongkyu Lee, Marius Ruh, John T. Hwang
    link: https://www.researchgate.net/publication/367311669
    '''
    P_ref = 2.e-5
    num_modes = len(modes)
    B = num_blades

    rho = BM_inputs['rho']
    M = BM_inputs['mach_number']
    a = BM_inputs['speed_of_sound']
    rpm = BM_inputs['rpm']
    omega = rpm*2.*np.pi/60. + 1.e-8

    rel_obs_position = BM_inputs['rel_obs_position']
    thrust_dir = csdl.expand(BM_inputs['thrust_dir'], (num_nodes, 3, num_observers), 'i->aib')
    S = csdl.reshape(BM_inputs['rel_obs_dist'], (num_nodes, num_observers))

    X = csdl.sum(rel_obs_position*thrust_dir, axes=(1,))
    Y = (S**2 - X**2  + 1.e-12)**0.5 # NOTE: FIX THE NUMERICAL SOFTENING FOR DERIVATIVES HERE
    if num_nodes == 1:
        S0 = (X**2 +  (1-csdl.expand(M, X.shape)**2)*Y**2)**0.5
    else:
        S0 = (X**2 +  (1-csdl.expand(M, X.shape, 'i->ij')**2)*Y**2)**0.5

    t_c = BM_inputs['thickness_to_chord_ratio'] # (num_radial,)
    chord = BM_inputs['chord_profile'] # (num_radial,)
    h = t_c*chord

    Ax = 0.6853*chord*h

    R = BM_inputs['propeller_radius']
    dR = BM_inputs['dr'] # dimensional dr
    nondim_sectional_radius  = BM_inputs['nondim_sectional_radius'] # (num_radial,)
    sectional_radius = nondim_sectional_radius*csdl.expand(R, (num_radial,))

    # expand terms for integration and across modes
    integrand_shape = (num_nodes, num_observers, num_radial) # since we are looping over the integrand
    if num_nodes == 1:
        M_integrand = csdl.expand(M, integrand_shape)
    else:
        M_integrand = csdl.expand(M, integrand_shape, 'i->iab')
    omega_integrand = csdl.expand(omega, integrand_shape)
    Y_integrand = csdl.expand(Y, integrand_shape, 'ij->ija')
    sR_integrand = csdl.expand(sectional_radius, integrand_shape, 'i->abi') # sectional radius (expanded)
    a_integrand = csdl.expand(a, integrand_shape)
    S0_integrand = csdl.expand(S0, integrand_shape, 'ij->ija')
    Ax_integrand = csdl.expand(Ax, integrand_shape, 'i->abi')
    dR_integrand  = csdl.expand(dR, integrand_shape)

    # first deal with the integrand term; output should be (num_nodes, num_observers, num_modes)
    m_array = np.zeros((num_nodes, num_observers, num_modes, num_radial))
    bessel_term = csdl.Variable(shape=m_array.shape, value=0.)
    for i, m in enumerate(modes):
        m_array[:,:,i,:] = m
        bessel_term = bessel_term.set(
            csdl.slice[:,:,i,:],
            value=csdl.bessel(omega_integrand*Y_integrand*sR_integrand*m*B/(a_integrand*S0_integrand), kind=1, order=m*B)
        )
        # bessel_term[:,:,i,:] = csdl.bessel(omega_integrand*Y_integrand*sR_integrand*m*B/(a_integrand*S0_integrand), kind=1, order=m*B)

    integrand = csdl.Variable(shape=m_array.shape, value=0.)
    for i, m in enumerate(modes):
        bessel_m1 = csdl.bessel(omega_integrand*Y_integrand*sR_integrand*(m*B-1)/(a_integrand*S0_integrand), kind=1, order=int(m*B-1))
        bessel_p1 = csdl.bessel(omega_integrand*Y_integrand*sR_integrand*(m*B+1)/(a_integrand*S0_integrand), kind=1, order=int(m*B+1))
        integrand = integrand.set(
            csdl.slice[:,:,i,:],
            value=Ax_integrand*(bessel_term[:,:,i,:] + ((1-M_integrand**2)*Y_integrand*sR_integrand)/(2*S0_integrand**2)*(bessel_m1-bessel_p1))*dR_integrand
        )
        # integrand[:,:,i,:] = Ax_integrand*(bessel_term[:,:,i,:] + ((1-M_integrand**2)*Y_integrand*sR_integrand)/(2*S0_integrand**2)*(bessel_m1-bessel_p1))*dR_integrand
    PmT_integrated_factor = csdl.sum(integrand, axes=(3,)) # summing over radial direction

    # expand terms here across modes
    target_shape = (num_nodes, num_observers, num_modes)
    rho_exp = csdl.expand(rho, target_shape)
    omega_exp = csdl.expand(omega, target_shape)
    if num_nodes == 1:
        M_exp = csdl.expand(M, target_shape)
    else:
        M_exp = csdl.expand(M, target_shape, 'i->iab')
    S0_exp = csdl.expand(S0, target_shape, 'ij->ija')
    X_exp = csdl.expand(X, target_shape, 'ij->ija')
    
    m_array_0 = m_array[:,:,:,0]
    PmT_factor = (rho_exp*(m_array_0*omega_exp)**2*B**3*(S0_exp + M_exp*X_exp)**2)/(2*np.pi*(2**0.5)*(1-M_exp**2)**2*S0_exp**3)

    PmT_per_mode  = PmT_factor*PmT_integrated_factor

    SPL_thickness_per_mode = 10.*csdl.log(PmT_per_mode**2/P_ref**2, base=10.)
    SPL_thickness  = 10.*csdl.log(
        csdl.sum(
            csdl.power(
                10., 
                SPL_thickness_per_mode/10. + 1.e-6
            ),
            axes=(2,)
        ),
        base=10.
    )

    return SPL_thickness, PmT_per_mode**2