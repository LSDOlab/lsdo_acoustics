import csdl
import numpy as np
from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

class LowsonSPLModel(ModuleCSDL):
    def initialize(self):
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('num_blades', default=2)
        self.parameters.declare('num_observers', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        self.parameters.declare('load_harmonics', default=np.arange(0,11,1))
        self.parameters.declare('component_name')

    
    def define(self):
        P_ref = 2.e-5

        num_nodes = self.parameters['num_nodes']
        B = self.parameters['num_blades']
        num_observers = self.parameters['num_observers']
        modes = self.parameters['modes']
        num_modes = len(modes)
        harmonics = self.parameters['load_harmonics']
        num_harmonics = len(harmonics)

        component_name = self.parameters['component_name']

        a = self.declare_variable('speed_of_sound')
        M = self.declare_variable('mach_number') # mach number traveling forward
        R = self.declare_variable('propeller_radius')
        
        rpm = csdl.reshape(
            self.declare_variable('rpm', shape=(num_nodes,1)),
            (num_nodes, ),
        )

        omega = rpm*2*np.pi/60 # conversion to radians per second

        # DATA ON OBSERVER LOCATIONS
        x = csdl.reshape(self.declare_variable('rel_obs_x_pos', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))
        y = csdl.reshape(self.declare_variable('rel_obs_y_pos', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))
        z = csdl.reshape(self.declare_variable('rel_obs_z_pos', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))
        S = csdl.reshape(self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))

        theta = csdl.arctan(z/(x**2+y**2 + 1e-6)**0.5)
        self.register_output('dummy', theta)
        # beta = (1 - M**2)**0.5
        r1 = S*(1.-csdl.expand(M,(num_nodes, num_observers))*csdl.cos(theta))

        # FOURIER COEFFICIENTS FOR THRUST AND DRAG
        a_T = self.declare_variable('aT', shape=(num_nodes, B, num_harmonics))
        b_T = self.declare_variable('bT', shape=(num_nodes, B, num_harmonics))
        a_D = self.declare_variable('aD', shape=(num_nodes, B, num_harmonics))
        b_D = self.declare_variable('bD', shape=(num_nodes, B, num_harmonics))

        # theta = self.declare_variable('observer_theta', shape=(num_nodes, num_observers))

        # ====================================== VARIABLE EXPANSION ======================================
        target_shape = (num_nodes, num_observers, num_modes, B, num_harmonics)
        omega_exp = csdl.expand(omega, target_shape, 'i->iabcd')
        z_exp = csdl.expand(z, target_shape, 'ij->ijabc')
        x_exp = csdl.expand(x, target_shape, 'ij->ijabc')
        a_exp = csdl.expand(a, target_shape)
        r1_exp = csdl.expand(r1, target_shape, 'ij->ijabc')
        R_exp = csdl.expand(R, target_shape)
        
        # Target shape for fourier coefficients from integration step
        # NOTE: dim for num_modes == 1 because they do not differ across the blade modes
        coeff_target_shape = (num_nodes, num_observers, num_modes, B, num_harmonics) 
        a_T_exp = csdl.expand(a_T, coeff_target_shape, 'ijk->iabjk')
        b_T_exp = csdl.expand(b_T, coeff_target_shape, 'ijk->iabjk')
        a_D_exp = csdl.expand(a_D, coeff_target_shape, 'ijk->iabjk')
        b_D_exp = csdl.expand(b_D, coeff_target_shape, 'ijk->iabjk')

        # ====================================== SETTING UP OUTPUTS ======================================

        # An = self.create_output('An', shape=(num_nodes, num_observers, num_modes, B, num_harmonics))
        # Bn = self.create_output('Bn', shape=(num_nodes, num_observers, num_modes, B, num_harmonics))
        # bladeSPL = self.create_output('bladeSPL', shape=(num_nodes, num_observers, num_modes, B))
        # SPL_m = self.create_output('SPL_m', shape=(num_nodes, num_observers, num_modes))

        # region setting up multi-dim coefficient sizes
        n = np.ones(shape=coeff_target_shape)
        for i in range(num_modes):
            n[:,:,i,:,:] = modes[i] * B
        n_var = self.declare_variable('n_var', val=n)

        lam = np.ones(shape=coeff_target_shape)
        for i in range(num_harmonics):
            lam[:,:,:,:,i] = i
        lam_var = self.declare_variable('lam_var', val=lam)

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
                    coeff_sign_matrix_even[:,:,i,:,j] = 1.
                    A_lin_comb_sign_matrix[:,:,i,:,j] = -1.
                    B_lin_comb_sign_matrix[:,:,i,:,j] = 1.
                    # A
                    if np.mod(ind, 4) == 2:
                        term_1_coeff_A[:,:,i,:,j] = 1.
                        term_2_coeff_A[:,:,i,:,j] = -1.
                    elif np.mod(ind, 4) == 0:
                        term_1_coeff_A[:,:,i,:,j] = -1.
                        term_2_coeff_A[:,:,i,:,j] = 1.

                    # B
                    if (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==1):
                        term_1_coeff_B[:,:,i,:,j] = -1.
                        term_2_coeff_B[:,:,i,:,j] = 1.

                    elif (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==3):
                        term_1_coeff_B[:,:,i,:,j] = 1.
                        term_2_coeff_B[:,:,i,:,j] = -1.

                    elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==1):
                        term_1_coeff_B[:,:,i,:,j] = 1.
                        term_2_coeff_B[:,:,i,:,j] = -1.

                    elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==3):
                        term_1_coeff_B[:,:,i,:,j] = -1.
                        term_2_coeff_B[:,:,i,:,j] = 1.

                elif np.mod(ind,2) == 1:
                    coeff_sign_matrix_odd[:,:,i,:,j] = 1.
                    A_lin_comb_sign_matrix[:,:,i,:,j] = 1.
                    B_lin_comb_sign_matrix[:,:,i,:,j] = -1.
                    # A
                    if np.mod(ind, 4) == 2:
                        term_1_coeff_A[:,:,i,:,j] = -1.
                        term_2_coeff_A[:,:,i,:,j] = 1.
                    elif np.mod(ind, 4) == 0:
                        term_1_coeff_A[:,:,i,:,j] = 1.
                        term_2_coeff_A[:,:,i,:,j] = -1.

                    # B
                    if (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==1):
                        term_1_coeff_B[:,:,i,:,j] = 1.
                        term_2_coeff_B[:,:,i,:,j] = -1.

                    elif (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==3):
                        term_1_coeff_B[:,:,i,:,j] = -1.
                        term_2_coeff_B[:,:,i,:,j] = 1.

                    elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==1):
                        term_1_coeff_B[:,:,i,:,j] = -1.
                        term_2_coeff_B[:,:,i,:,j] = 1.

                    elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==3):
                        term_1_coeff_B[:,:,i,:,j] = 1.
                        term_2_coeff_B[:,:,i,:,j] = -1.

        term_1_coeff_A = self.declare_variable('term_1_coeff_A', term_1_coeff_A)
        term_2_coeff_A = self.declare_variable('term_2_coeff_A', term_2_coeff_A)
        term_1_coeff_B = self.declare_variable('term_1_coeff_B', term_1_coeff_B)
        term_2_coeff_B = self.declare_variable('term_2_coeff_B', term_2_coeff_B)
        coeff_sign_matrix_odd = self.declare_variable('coeff_sign_matrix_odd', coeff_sign_matrix_odd)
        coeff_sign_matrix_even = self.declare_variable('coeff_sign_matrix_even', coeff_sign_matrix_even)
        A_lin_comb_sign_matrix = self.declare_variable('A_lin_comb_sign_matrix', A_lin_comb_sign_matrix)
        B_lin_comb_sign_matrix = self.declare_variable('B_lin_comb_sign_matrix', B_lin_comb_sign_matrix)
        #endregion 

        # NOTE: need to a_lambda and b_lambda coeff from load integration to a new array 
        # called A_fourier_coeff and B_fourier_coeff; these change based on if n-lambda is even or odd
        term_1_constant = n_var*omega_exp*z_exp/(a_exp*r1_exp**2)
        term_2_constant = 1. / (R_exp*r1_exp)
        bessel_input = n_var*omega_exp*R_exp*x_exp/(a_exp*r1_exp)

        self.register_output('bessel_dummy', csdl.bessel(bessel_input, order=n-lam))
        # TERM A

        term_1_A_fc = (coeff_sign_matrix_even * b_T_exp + coeff_sign_matrix_odd * a_T_exp) # weighting based on sign of n-lambda
        term_2_A_fc = (coeff_sign_matrix_even * b_D_exp + coeff_sign_matrix_odd * a_D_exp) # weighting based on sign of n-lambda

        self.register_output('asdf', term_1_A_fc)
        term_1_A = term_1_constant*term_1_A_fc*(csdl.bessel(bessel_input, order=n-lam) + \
        A_lin_comb_sign_matrix*csdl.exp_a(-1., lam_var) * csdl.bessel(bessel_input, order=n+lam))
        self.print_var(term_1_A)
        term_2_A = term_2_constant * term_2_A_fc * ((n_var-lam_var)*csdl.bessel(bessel_input, order=n-lam) + \
        A_lin_comb_sign_matrix*csdl.exp_a(-1., lam_var) *(n_var+lam_var)*csdl.bessel(bessel_input, order=n+lam))
        self.print_var(term_2_A)

        An = (term_1_coeff_A*term_1_A + term_2_coeff_A*term_2_A)/(4*np.pi) 

        # TERM B

        term_1_B_fc = (coeff_sign_matrix_even * a_T_exp + coeff_sign_matrix_odd * b_T_exp) # weighting based on sign of n-lambda
        term_2_B_fc = (coeff_sign_matrix_even * a_D_exp + coeff_sign_matrix_odd * b_D_exp) # weighting based on sign of n-lambda

        term_1_B = term_1_constant*term_1_B_fc*(csdl.bessel(bessel_input, order=n-lam) + \
        B_lin_comb_sign_matrix * csdl.exp_a(-1., lam_var) *csdl.bessel(bessel_input, order=n+lam))
        term_2_B = term_2_constant * term_2_B_fc * ((n_var-lam_var)*csdl.bessel(bessel_input, order=n-lam) + \
        B_lin_comb_sign_matrix*csdl.exp_a(-1., lam_var) *(n_var+lam_var)*csdl.bessel(bessel_input, order=n+lam))

        Bn = (term_1_coeff_B*term_1_B + term_2_coeff_B*term_2_B) / (4*np.pi)
        
        self.register_output('An', An)
        self.register_output('Bn', Bn)

        sum1 = csdl.sum(An, axes=(4,))
        sum2 = csdl.sum(Bn, axes=(4,))
        sum_A_B = (sum1)**2 + (sum2)**2
        
        bladeSPL = 10.*csdl.log10(sum_A_B/(2*P_ref**2))
        self.register_output('bladeSPL', bladeSPL)

        ex = csdl.exp_a(10., bladeSPL/10.)
        ex_sum = csdl.sum(ex, axes=(3,))
        SPL_m = 10.*csdl.log10(ex_sum)

        rotor_tonal_spl = 10*csdl.log10(csdl.sum(csdl.exp_a(10.,SPL_m/10.), axes=(2,)))
        self.register_output(f'{component_name}_tonal_spl', rotor_tonal_spl) # SHAPE IS (num_nodes, num_observers)

if __name__ == '__main__':
    from python_csdl_backend import Simulator
    import time
    
    m = LowsonSPLModel(
        num_nodes=2, 
        num_blades=2, 
        num_observers=2,
        component_name='dummy'
    )
    sim = Simulator(m, display_scripts=True)
    sim.run()

    