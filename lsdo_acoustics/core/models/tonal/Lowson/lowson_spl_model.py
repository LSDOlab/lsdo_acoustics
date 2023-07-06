import csdl
import numpy as np

class LowsonSPLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('num_blades', default=2)
        self.parameters.declare('num_observers', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        self.parameters.declare('harmonics', default=np.arange(0,11,1))
        self.parameters.declare('component_name')

    
    def define(self):
        P_ref = 2.e-5

        num_nodes = self.parameters['num_nodes']
        B = self.parameters['num_blades']
        num_observers = self.parameters['num_observers']
        modes = self.parameters['modes']
        num_modes = len(modes)
        harmonics = self.parameters['harmonics']
        num_harmonics = len(harmonics)

        component_name = self.parameters['component_name']

        a = self.declare_variable('speed_of_sound')
        M = self.declare_variable('forward_mach_number') # mach number traveling forward
        R = self.declare_variable('rotor_radius')
        
        rpm = self.declare_variable('rpm', shape=(num_nodes,))


        omega = rpm*2*np.pi/60 # conversion to radians per second

        # DATA ON OBSERVER LOCATIONS
        x = csdl.reshape(self.declare_variable('rel_obs_x_pos', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))
        y = csdl.reshape(self.declare_variable('rel_obs_y_pos', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))
        z = csdl.reshape(self.declare_variable('rel_obs_z_pos', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))
        S = csdl.reshape(self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))

        theta = csdl.arctan(z/(x**2+y**2)**0.5)
        # beta = (1 - M**2)**0.5
        r1 = S*(1.-csdl.expand(M,(num_nodes, num_observers))*csdl.cos(theta))

        # FOURIER COEFFICIENTS FOR THRUST AND DRAG
        a_T = self.declare_variable('a_T', shape=(num_nodes, B, num_harmonics))
        b_T = self.declare_variable('b_T', shape=(num_nodes, B, num_harmonics))
        a_D = self.declare_variable('a_D', shape=(num_nodes, B, num_harmonics))
        b_D = self.declare_variable('b_D', shape=(num_nodes, B, num_harmonics))

        # theta = self.declare_variable('observer_theta', shape=(num_nodes, num_observers))

        # ====================================== VARIABLE EXPANSION ======================================
        target_shape = (num_nodes, num_observers, 1, 1, 1)
        omega_exp = csdl.expand(omega, target_shape, 'i->iabcd')
        z_exp = csdl.expand(z, target_shape, 'ij->ijabc')
        x_exp = csdl.expand(x, target_shape, 'ij->ijabc')
        a_exp = csdl.expand(a, target_shape)
        r1_exp = csdl.expand(r1, target_shape, 'ij->ijabc')
        R_exp = csdl.expand(R, target_shape)
        
        # Target shape for fourier coefficients from integration step
        # NOTE: dim for num_modes == 1 because they do not differ across the blade modes
        coeff_target_shape = (num_nodes, num_observers, 1, B, num_harmonics) 
        a_T_exp = csdl.expand(a_T, coeff_target_shape, 'ijk->iabjk')
        b_T_exp = csdl.expand(b_T, coeff_target_shape, 'ijk->iabjk')
        a_D_exp = csdl.expand(a_D, coeff_target_shape, 'ijk->iabjk')
        b_D_exp = csdl.expand(b_D, coeff_target_shape, 'ijk->iabjk')

        # ====================================== SETTING UP OUTPUTS ======================================

        An = self.create_output('An', shape=(num_nodes, num_observers, num_modes, B, num_harmonics))
        Bn = self.create_output('Bn', shape=(num_nodes, num_observers, num_modes, B, num_harmonics))
        bladeSPL = self.create_output('bladeSPL', shape=(num_nodes, num_observers, num_modes, B))
        SPL_m = self.create_output('SPL_m', shape=(num_nodes, num_observers, num_modes))

        for i in range(num_modes): # looping over harmonic modes
            m = modes[i]
            n = m*B
            for q in range(B):  # looping over number of blades
                for j in range(num_harmonics):  # looping through summation of Fourier coefficients
                    ind = m*B-j
                    # IF CLAUSES
                    if np.mod(ind,2) == 0: # n-lam is even
                        # REAL
                        if np.mod(ind, 4) == 2:
                            term_1_coeff = 1.
                            term_2_coeff = -1.
                        elif np.mod(ind, 4) == 0:
                            term_1_coeff = -1.
                            term_2_coeff = 1.

                        # NOTE: both terms default to a positive sign, and the if condition determines the actual sign
                        term_1_A = n*omega_exp*z_exp/(a_exp*r1_exp**2)*b_T_exp[:,:,0,q,j]*(csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n-j) - \
                        (-1)**j *csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n+j))
                        term_2_A = b_D_exp[:,:,0,q,j]/(R_exp*r1_exp) * ((n-j)*csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n-j) - \
                        (-1)**j*(n+j)*csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp), order=n+j))
                        
                        An[:,:,i,q,j] = 1./(4*np.pi) * (term_1_coeff*term_1_A + term_2_coeff*term_2_A)

                        # IMAG
                        if (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==1):
                            term_1_coeff = -1.
                            term_2_coeff = 1.

                        elif (-ind+1<0) and (np.mod(np.abs(-ind+1),4)==3):
                            term_1_coeff = 1.
                            term_2_coeff = -1.

                        elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==1):
                            term_1_coeff = 1.
                            term_2_coeff = -1.

                        elif (-ind+1>0) and (np.mod(np.abs(-ind+1),4)==3):
                            term_1_coeff = -1.
                            term_2_coeff = 1.

                        term_1_B = n*omega_exp*z_exp/(a_exp*r1_exp**2)*a_T_exp[:,:,0,q,j]*(csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n-j) + \
                        (-1)**j *csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n+j))
                        term_2_B = a_D_exp[:,:,0,q,j]/(R_exp*r1_exp)*((n-j)*csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n-j) + \
                        (-1)**j*(n+j)*csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp), order=n+j))
                    
                        Bn[:,:,i,q,j] = 1./(4*np.pi)*(term_1_coeff*term_1_B + term_2_coeff*term_2_B)
                        

                    if np.mod(ind,2) == 1: # n-lam is odd
                        # REAL
                        if np.mod(-ind+1, 4) == 2:
                            term_1_coeff = -1.
                            term_2_coeff = 1.
                        elif np.mod(-ind+1, 4) == 0:
                            term_1_coeff = 1.
                            term_2_coeff = -1.

                        term_1_A = n*omega_exp*z_exp/(a_exp*r1_exp**2)*a_T_exp[:,:,0,q,j]*(csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n-j) + \
                        (-1)**j *csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n+j))
                        term_2_A = a_D_exp[:,:,0,q,j]/(R_exp*r1_exp)*((n-j)*csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n-j) + \
                        (-1)**j*(n+j)*csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp), order=n+j))

                        An[:,:,i,q,j] = 1./(4*np.pi) * (term_1_coeff*term_1_A + term_2_coeff*term_2_A)
                        
                        # IMAG
                        if (-ind<0) and (np.mod(np.abs(ind),4)==1):
                            term_1_coeff = 1.
                            term_2_coeff = -1.

                        elif (-ind<0) and (np.mod(np.abs(ind),4)==3):
                            term_1_coeff = -1.
                            term_2_coeff = 1.

                        elif (-ind>0) and (np.mod(np.abs(ind),4)==1):
                            term_1_coeff = -1.
                            term_2_coeff = 1.

                        elif (-ind>0) and (np.mod(np.abs(ind),4)==3):
                            term_1_coeff = 1.
                            term_2_coeff = -1.

                        term_1_B = n*omega_exp*z_exp/(a_exp*r1_exp**2)*b_T_exp[:,:,0,q,j]*(csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n-j) - \
                        (-1)**j *csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n+j))
                        term_2_B = b_D_exp[:,:,0,q,j]/(R_exp*r1_exp)*((n-j)*csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp),order=n-j) - \
                        (-1)**j*(n+j)*csdl.bessel(n*omega_exp*R_exp*x_exp/(a_exp*r1_exp), order=n+j))

                        Bn[:,:,i,q,j] = 1./(4*np.pi)*(term_1_coeff*term_1_B + term_2_coeff*term_2_B)
                        # SHAPE IS (num_nodes, num_observers, 1, 1, 1)

                sum1 = csdl.sum(An[:,:,i,q,:], axes=(4,)) # SHAPE IS (num_nodes, num_observers, 1, 1)
                sum2 = csdl.sum(Bn[:,:,i,q,:], axes=(4,)) # SHAPE IS (num_nodes, num_observers, 1, 1)
                sum_A_B = (sum1)**2 + (sum2)**2 

                bladeSPL[:,:,i,q] = 10.*csdl.log10((sum_A_B) / (2*P_ref**2)) 
                # SHAPE IS (num_nodes, num_observers, 1, 1)
        
            # SPL_m[:,:,m] = 10*csdl.log10(csdl.sum(10.**(bladeSPL[:,:,m,:])/10., axes=(3,)))
            print(bladeSPL.shape)
            ex = csdl.exp_a(10.,bladeSPL[:,:,i,:]/10.)
            print(ex.shape)
            ex_sum = csdl.sum(ex, axes=(3,))
            SPL_m[:,:,i] = 10*csdl.log10(ex_sum) # SHAPE IS (num_nodes, num_observers, 1)
            # TOTAL SHAPE OF SPL_m IS (num_nodes, num_observers, num_modes)

        rotor_tonal_spl = 10*csdl.log10(csdl.sum(csdl.exp_a(10.,SPL_m/10.), axes=(2,)))
        self.register_output(f'{component_name}_tonal_SPL', rotor_tonal_spl) # SHAPE IS (num_nodes, num_observers)
        print(rotor_tonal_spl.shape)
        

if __name__ == '__main__':
    from python_csdl_backend import Simulator
    import time
    
    m = LowsonSPLModel(
        num_nodes=2, 
        num_blades=2, 
        num_observers=2,
        component_name='dummy'
    )
    sim = Simulator(m)
    sim.run()

    

'''
NOTE:
- Include 3 harmonic mode numbers (m = 1,2,3)
'''