import numpy as np
import csdl_alpha as csdl

def RA_func(f):
    RA = 12194.**2*f**4 / ((f**2 + 20.6**2)*((f**2 + 107.7**2)*(f**2 + 737.9**2))**0.5*(f**2 + 12194.**2))
    
    return RA

def A_weighting_function(SPL, f):
    shape = SPL.shape
    RA_1000 = RA_func(1000.)
    RA_f = RA_func(f)
    num_nodes = f.shape[0]
    A_shift = 20.*csdl.log(RA_f, base=10.) - 20.*csdl.log(RA_1000, base=10.)

    # A = 10.*csdl.log(csdl.power(10., (SPL + A_shift)/10.), base=10.)
    A = SPL + A_shift

    return A

def A_weighting_function_new(P_mag, fm, freq_axis=None):
    
    K1 = 2.243e16
    K3 = 1.562
    f1 = 20.599
    f2 = 107.653
    f3 = 737.862
    f4 = 12194.22

    wC_m = K1*fm**4 / ((fm**2 + f1**2)**2 * (fm**2 + f4**2)**2)
    wA_m = wC_m*K3*fm**4 / ((fm**2 + f2**2) * (fm**2  + f3**2))

    if freq_axis is not None:
        p2_A = 0.5*csdl.sum(wA_m*P_mag, axes=(freq_axis,))
    else:
        p2_A = 0.5*wA_m*P_mag
    dBA = 10*csdl.log((p2_A)/(20.e-6)**2, base=10.)

    return dBA