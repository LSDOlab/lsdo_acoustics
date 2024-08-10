import numpy as np 
import csdl_alpha as csdl

freq_band = np.array(
    [12.5, 16, 20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 
    500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000,
    10000, 12500, 16000, 20000,
    25000, 31500, 40000, 50000, 63000 # additional ones used by Hyunjune
    ])

def GL_spl_model(num_nodes, num_observers, num_blades, inputs_dict, frequency_band=freq_band):
    B =  num_blades
    num_freq_band = len(frequency_band)

    CT = inputs_dict['CT']
    chord_profile = inputs_dict['chord_profile']
    S = csdl.reshape(inputs_dict['rel_obs_dist'], shape=(num_nodes, num_observers))
    theta_0 = inputs_dict['rel_angle_plane']
    R = inputs_dict['propeller_radius']
    dr = inputs_dict['dr']
    rpm = inputs_dict['rpm']
    a = inputs_dict['speed_of_sound']

    V = inputs_dict['velocity']
    V_inf = csdl.norm(V, axes=(1,))
    omega = rpm*2.*np.pi/60.
    if num_nodes == 1:
        V_tip = csdl.expand(
            omega*csdl.expand(R, (num_nodes,)),
            (num_nodes, num_observers)
        ) - csdl.expand(V_inf, (num_nodes, num_observers))
    else:
        V_tip = csdl.expand(
            omega*csdl.expand(R, (num_nodes,)),
            (num_nodes, num_observers),
            'i->ia'
        ) - csdl.expand(V_inf, (num_nodes, num_observers), 'i->ia')

    A_b = csdl.expand(csdl.sum((chord_profile))*dr, CT.shape)
    # A_b = csdl.sum((chord_profile))*dr
    sigma = A_b*B/np.pi/csdl.expand(R,A_b.shape)**2
    c_sw = sigma*np.pi*csdl.expand(R, A_b.shape)/B

    # region expanding variables
    target_shape = (num_nodes, num_observers, num_freq_band)
    frequency_band_exp = csdl.expand(frequency_band, target_shape, 'i->abi')
    V_t_exp = csdl.expand(V_tip, target_shape, 'ij->ija')
    theta_0_exp = csdl.expand(theta_0, target_shape, 'ij->ija')
    S_exp = csdl.expand(S, target_shape, 'ij->ija')
    R_exp = csdl.expand(R, target_shape)
    if num_nodes == 1:
        sigma_exp = csdl.expand(sigma, target_shape)
        M_t_exp = V_t_exp / csdl.expand(a, target_shape)
        CT_exp = csdl.expand(CT, target_shape)
        St_exp = frequency_band_exp*csdl.expand(c_sw, target_shape)/V_t_exp
    else:
        sigma_exp = csdl.expand(sigma, target_shape, 'i->iab')
        M_t_exp = V_t_exp / csdl.expand(a, target_shape, 'i->iab')
        CT_exp = csdl.expand(CT, target_shape, 'i->iab')
        St_exp = frequency_band_exp*csdl.expand(c_sw, target_shape, 'i->iab')/V_t_exp
    # endregion

    f0 = csdl.log(V_t_exp**7.84, base=10.) * 10.
    f1 = sigma_exp * 1.
    f2 = 0.9*M_t_exp*sigma_exp*(M_t_exp+3.82)
    f3 = 1. # NOT USED
    f4 = 1. # NOT USED
    f5 = -2.*M_t_exp**2 + 2.06
    f6 = -CT_exp * M_t_exp * (CT_exp-csdl.sin((theta_0_exp**2)**0.5)+2.06) + 1.
    f7 = CT_exp
    # f8 = 4.97*CT*csdl.sin((theta_0**2)**0.5)*(4.3*S/R*M_t - (S/R) + 4.3) # OLD FORMULATION
    f8 = 4.97*CT_exp*csdl.sin((theta_0_exp**2)**0.5)*(1.5*S_exp/R_exp*M_t_exp - (S_exp/R_exp) + 15.)

    num = f0*(St_exp-(f1*csdl.log(CT_exp, base=10.) + f2*csdl.log(sigma_exp, base=10.)))**0.6
    den_1 = csdl.power(
        St_exp - (f1*csdl.log(CT_exp, base=10.) + f2*csdl.log(sigma_exp, base=10.)) + f5,
        f6
    )
    den_2 = csdl.power(
        f7*(St_exp - (f1*csdl.log(CT_exp, base=10.) +  f2*csdl.log(sigma_exp, base=10.))),
        f8
    )
    
    SPL_1_3 = num/(den_1 + den_2)
    GL_spl = 10 * csdl.log(
        csdl.sum(
            csdl.power(10., SPL_1_3/10.),
            axes=(2,)
        ),
        base=10
    )
    return GL_spl, SPL_1_3