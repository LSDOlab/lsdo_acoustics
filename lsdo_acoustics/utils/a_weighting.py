import numpy as np
import csdl

def RA_func(f):
    RA = 12194.**2*f**4 / ((f**2 + 20.6**2)*((f**2 + 107.7**2)*(f**2 + 737.9**2))**0.5*(f**2 + 12194.**2))
    
    return RA

def A_weighting_func(self, tonal_SPL, f):
    shape = tonal_SPL.shape
    RA_1000_val = RA_func(1000.)
    RA_1000 = self.create_input('RA_1000', val=RA_1000_val, shape=f.shape)
    RA_f = RA_func(f)
    A_shift = csdl.reshape(
        20.*csdl.log10(RA_f) - 20.*csdl.log10(RA_1000),
        (f.shape[0],)
    )

    A = 10.*csdl.log10(csdl.exp_a(10., (tonal_SPL + csdl.expand(A_shift, shape, 'i->ij'))/10.))

    return A