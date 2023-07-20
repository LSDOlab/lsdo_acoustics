import csdl
import numpy as np

P_ref = 2.e-5

class KSSPLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('num_observers', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        # self.parameters.declare('load_harmonics', default=np.arange(0,3,1))
        self.parameters.declare('load_harmonics', default=None)
        self.parameters.declare('num_blades', default=2)
        self.parameters.declare('num_radial')
        self.parameters.declare('num_azim')
        self.parameters.declare('test', default=False)

    def sears_function(self, m, omega, r, R, c):
        Ut = omega*r*R
        k = m*omega*c/(2*Ut)

        S_real = ((csdl.bessel(k,1,0)*csdl.bessel(k,1,1)**2 - csdl.bessel(k,1,1)**2*csdl.bessel(k,2,1) + \
        csdl.bessel(k,1,0)*csdl.bessel(k,1,1)*csdl.bessel(k,2,0) - csdl.bessel(k,1,1)*csdl.bessel(k,2,0)*csdl.bessel(k,2,1)) - \
        ((csdl.bessel(k,1,0)*csdl.bessel(k,1,1)**2) + csdl.bessel(k,1,0)**2*csdl.bessel(k,2,1) - \
        csdl.bessel(k,1,1)**2*csdl.bessel(k,2,1) - csdl.bessel(k,1,0)*csdl.bessel(k,2,1)**2)) \
            / ((csdl.bessel(k,1,1) + csdl.bessel(k,2,0))**2 + (csdl.bessel(k,1,0) - csdl.bessel(k,2,1))**2)  # RECHECK
        
        S_imag = -(csdl.bessel(k,1,1)**3 + csdl.bessel(k,1,0)*csdl.bessel(k,1,1)*csdl.bessel(k,2,1) + \
            csdl.bessel(k,1,1)**2*csdl.bessel(k,2,0)+ csdl.bessel(k,1,0)*csdl.bessel(k,2,0)*csdl.bessel(k,2,1) + \
            csdl.bessel(k,1,0)**2*csdl.bessel(k,1,1) - csdl.bessel(k,1,0)*csdl.bessel(k,1,1)*csdl.bessel(k,2,1) - \
            csdl.bessel(k,1,0)*csdl.bessel(k,1,1)*csdl.bessel(k,2,1) + csdl.bessel(k,1,1)*csdl.bessel(k,2,1)**2) / \
            ((csdl.bessel(k,1,1) + csdl.bessel(k,2,0))**2 + (csdl.bessel(k,1,0) - csdl.bessel(k,2,1))**2) # RECHECK
        return S_real, S_imag

    def define(self):
        component_name = self.parameters['component_name']
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        modes = self.parameters['modes']
        num_modes = len(modes) # the mode harmonics of the blades that we want to consider
        if self.parameters['load_harmonics'] == None:
            harmonics = np.arange(0, modes[-1], 1)
        else:
            harmonics = self.parameters['load_harmonics']
        num_harmonics = len(harmonics) # discrete harmonics considered during truncation of fourier series
        B = self.parameters['num_blades']

        num_radial = self.parameters['num_radial']
        num_azim = self.parameters['num_azim']

        test = self.parameters['test']

        q = 0.05 # gust amplification factor

        rho = self.declare_variable('density')
        x = csdl.reshape(self.declare_variable('rel_obs_x_pos', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))
        S = csdl.reshape(self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))

        RPM = self.declare_variable('rpm') # NOTE: UPDATE/FIX LATER
        # BPF = m*RPM*B/60.
        theta = csdl.arccos(x/S)
        self.register_output('theta_dummy', theta)
        

        omega = RPM*2*np.pi/60
        # R = self.declare_variable(f'{component_name}_radius')
        R = self.declare_variable('propeller_radius')
        a = self.declare_variable('speed_of_sound')
        c = self.declare_variable('chord_profile', shape=(num_radial,))

        if test:
            dTdR_real_loads = self.declare_variable('dTdR_real', shape=(num_nodes, num_radial))
            dDdR_real_loads = self.declare_variable('dDdR_real', shape=(num_nodes, num_radial))
            r = self.declare_variable('nondim_sectional_radius', shape=(num_radial,)) # NOTE: ADJUST LATER 
        else:
            r = self.declare_variable('nondim_sectional_radius', val=np.linspace(0.2, 1., num_radial)) # NOTE: ADJUST LATER 
            # setting up the steady loads
            dT = self.declare_variable('_dT', shape=(num_nodes, num_radial, num_azim)) 
            dD = self.declare_variable('_dD', shape=(num_nodes, num_radial, num_azim))
            dr = self.declare_variable('dr')

            dTdR_inputs = dT / csdl.expand(dr, shape=dT.shape)
            dDdR_inputs = dD / csdl.expand(dr, shape=dD.shape)

            self.register_output('aaa', dTdR_inputs)
            self.register_output('bbb', dDdR_inputs)

            dTdR_real_loads = csdl.reshape(dTdR_inputs[:,:,0], (num_nodes, num_radial)) 
            dDdR_real_loads = csdl.reshape(dDdR_inputs[:,:,0], (num_nodes, num_radial))


        # ======================== VARIABLE EXPANSION ========================
        target_shape = (num_nodes, num_observers, num_modes, num_radial, num_harmonics)

        theta_exp = csdl.expand(theta, target_shape, 'ij->ijabc')
        r_exp = csdl.expand(r, target_shape, 'i->abcid')
        omega_exp = csdl.expand(omega, target_shape)
        R_exp = csdl.expand(R, target_shape)
        a_exp = csdl.expand(a, target_shape)
        c_exp = csdl.expand(c, target_shape, 'i->abcid')
        rho_exp = csdl.expand(rho, target_shape)

        theta_uns = theta_exp[:,:,:,:,1:]
        r_uns = r_exp[:,:,:,:,1:]
        omega_uns = omega_exp[:,:,:,:,1:]
        R_uns = R_exp[:,:,:,:,1:]
        a_uns = a_exp[:,:,:,:,1:]
        c_uns = c_exp[:,:,:,:,1:]
        rho_uns = rho_exp[:,:,:,:,1:]

        # lambda_i_exp = csdl.expand(lambda_i, target_shape, 'ij->iabjc')
        # phi_exp = lambda_i_exp/r_exp

        if test: # inputs are lambda and r, get phi
            lambda_i = self.declare_variable('lambda_i', shape=(num_nodes, num_radial))
            lambda_i_exp = csdl.expand(lambda_i, target_shape, 'ij->iabjc')
            phi_exp = lambda_i_exp / r_exp
            self.register_output('phi_exp', phi_exp)
        else: # inputs are phi and r, get lambda
            phi = csdl.reshape(self.declare_variable('phi', shape=(num_nodes, num_radial, num_azim))[:,:,0], (num_nodes, num_radial))
            phi_exp = csdl.expand(phi, target_shape, 'ij->iabjc')
            lambda_i_exp = phi_exp * r_exp
            self.register_output('lambda_test', lambda_i_exp)
        phi_uns = phi_exp[:,:,:,:,1:]
        lambda_i_uns = lambda_i_exp[:,:,:,:,1:]

        n = np.ones(shape=target_shape)
        for i in range(num_modes):
            n[:,:,i,:,:] = modes[i]
        n_var = self.declare_variable('n_var', val=n)

        lam = np.ones(shape=target_shape)
        for i in range(num_harmonics):
            lam[:,:,:,:,i] = i
        lam_var = self.declare_variable('lam_var', val=lam)


        coeff_matrix_A = np.ones_like(n)
        coeff_matrix_B = np.ones_like(n)
        real_weighting_matrix = np.zeros_like(n)
        imag_weighting_matrix = np.zeros_like(n)

        for i in range(num_modes):
            m = modes[i]
            for j in range(num_harmonics):

                ind = int((m-j)*B)
                if np.mod(ind,2) == 0:
                    real_weighting_matrix[:,:,i,:,j] = 1.

                    # REAL VALUES
                    if np.mod(ind,4) == 2:
                        coeff_A = -1.
                        
                    elif np.mod(ind,4) == 0:
                        coeff_A = 1.

                    # IMAG VALUES
                    if (-ind+1 < 0) and (np.mod(np.abs(-ind+1), 4) == 1):
                        coeff_B = -1.
                    elif (-ind+1 < 0) and (np.mod(np.abs(-ind+1), 4) == 3):
                        coeff_B = 1.
                    elif (-ind+1 > 0) and (np.mod(np.abs(-ind+1), 4) == 1):
                        coeff_B = 1.
                    elif (-ind+1 > 0) and (np.mod(np.abs(-ind+1), 4) == 3):
                        coeff_B = -1.

                elif np.mod(ind,2) == 1:
                    imag_weighting_matrix[:,:,i,:,j] = 1.
                    # REAL VALUES
                    if np.mod(ind,4) == 2:
                        coeff_A = -1.
                    elif np.mod(ind,4) == 0:
                        coeff_A = 1.

                    # IMAG VALUES
                    if (-ind < 0) and (np.mod(np.abs(ind), 4) == 1):
                        coeff_B = -1.
                    elif (-ind < 0) and (np.mod(np.abs(ind), 4) == 3):
                        coeff_B = 1.
                    elif (-ind > 0) and (np.mod(np.abs(ind), 4) == 1):
                        coeff_B = 1.
                    elif (-ind > 0) and (np.mod(np.abs(ind), 4) == 3):
                        coeff_B = -1.
                
                coeff_matrix_A[:,:,i,:,j] = coeff_A
                coeff_matrix_B[:,:,i,:,j] = coeff_B

        coeff_matrix_A = self.declare_variable('coeff_matrix_A', coeff_matrix_A)
        coeff_matrix_B = self.declare_variable('coeff_matrix_B', coeff_matrix_B)
        real_weighting = self.declare_variable('real_weighting', real_weighting_matrix)
        imag_weighting = self.declare_variable('imag_weighting', imag_weighting_matrix)
        # SUM ACROSS HARMONICS (lambda) AND INTEGRATE RADIALLY
        dTdR_real = self.create_output('dTdR_real_exp', val=0., shape=(num_nodes, num_observers, num_modes, num_radial, num_harmonics))
        dDdR_real = self.create_output('dDdR_real_exp', val=0., shape=(num_nodes, num_observers, num_modes, num_radial, num_harmonics)) 
        dTdR_imag = self.create_output('dTdR_imag_exp', val=0., shape=(num_nodes, num_observers, num_modes, num_radial, num_harmonics))
        dDdR_imag = self.create_output('dDdR_imag_exp', val=0., shape=(num_nodes, num_observers, num_modes, num_radial, num_harmonics))

        # ASSIGNING LOADS BASED ON HARMONICS
        # STEADY LOADS (FIRST HARMONIC (lambda = 0))
        dTdR_real[:,:,:,:,0] = csdl.expand(dTdR_real_loads, (num_nodes, num_observers, num_modes, num_radial, 1), 'ij->iabjc')
        dDdR_real[:,:,:,:,0] = csdl.expand(dDdR_real_loads, (num_nodes, num_observers, num_modes, num_radial, 1), 'ij->iabjc')

        # UNSTEADY LOADS (REMAINING HARMONICS)
        S_real, S_imag = self.sears_function(lam_var[:,:,:,:,1:], omega_uns, r_uns, R_uns, c_uns)
        w_lam = lambda_i_uns*omega_uns*R_uns/lam_var[:,:,:,:,1:] * q/B
        Vt = 0.
        dLdR = rho_uns*(omega_uns*r_uns*R_uns-Vt)*c_uns*w_lam*np.pi
        Lreal = S_real*dLdR
        Limag = S_imag*dLdR
        
        dTdR_real[:,:,:,:,1:] = Lreal*csdl.cos(phi_uns)
        dDdR_real[:,:,:,:,1:] = Lreal*csdl.sin(phi_uns)
        dTdR_imag[:,:,:,:,1:] = Limag*csdl.cos(phi_uns)
        dDdR_imag[:,:,:,:,1:] = Limag*csdl.sin(phi_uns)

        # REAL-IMAG (RI) weighting based on lambda and mode
        RI_weighting_A_T = (real_weighting*dTdR_real + imag_weighting*dTdR_imag)
        RI_weighting_A_D = (real_weighting*dDdR_real + imag_weighting*dDdR_imag)
        RI_weighting_B_T = (real_weighting*dTdR_imag + imag_weighting*dTdR_real) # NOTE THESE TWO ARE SWAPPED; IF A USES REAL, B USES IMAG (AND VICE-VERSA)
        RI_weighting_B_D = (real_weighting*dDdR_imag + imag_weighting*dDdR_real) # NOTE THESE TWO ARE SWAPPED; IF A USES REAL, B USES IMAG (AND VICE-VERSA)

        bessel_input = n_var*B*omega_exp*r_exp*R_exp/a_exp*csdl.sin(theta_exp)

        An = coeff_matrix_A * (RI_weighting_A_T*csdl.cos(theta_exp) - RI_weighting_A_D*(n_var-lam_var)*B*a_exp/(n_var*B*omega_exp*r_exp*R_exp))*\
                               csdl.bessel(bessel_input, kind=1, order=(n-lam)*B)
        Bn = coeff_matrix_B * (RI_weighting_B_T*csdl.cos(theta_exp) - RI_weighting_B_D*(n_var-lam_var)*B*a_exp/(n_var*B*omega_exp*r_exp*R_exp))*\
                               csdl.bessel(bessel_input, kind=1, order=(n-lam)*B)

        An = self.register_output('An', csdl.sum(An, axes=(4,)))
        Bn = self.register_output('Bn', csdl.sum(Bn, axes=(4,)))

        # INTEGRATION ACROSS RADIAL DIMENSION
        self.add(
            TrapezoidMethod(
                input_name='An',
                input_shape=(num_nodes, num_observers, num_modes, num_radial),
                dim=3,
                output_name='C_real_integrand'
            ),
            'An_integration_model'
        )

        self.add(
            TrapezoidMethod(
                input_name='Bn',
                input_shape=(num_nodes, num_observers, num_modes, num_radial),
                dim=3,
                output_name='C_imag_integrand'
            ),
            'Bn_integration_model'
        )

        C_real_integrand = self.declare_variable('C_real_integrand', shape=(num_nodes, num_observers, num_modes))
        C_imag_integrand = self.declare_variable('C_imag_integrand', shape=(num_nodes, num_observers, num_modes))


        target_int_shape = (num_nodes, num_observers, num_modes)
        n_var_int_exp = csdl.reshape(n_var[:,:,:,0,0], target_int_shape)
        omega_int_exp = csdl.expand(omega, target_int_shape)
        S_int_exp = csdl.expand(S, target_int_shape, 'ij->ija') # dimension for a is of size 1
        a_int_exp = csdl.expand(a, target_int_shape)


        C_real = n_var_int_exp*B**2*omega_int_exp/(4*np.pi*S_int_exp*a_int_exp)*C_real_integrand # SHAPE OF (num_nodes, num_observers, num_modes)
        C_imag = n_var_int_exp*B**2*omega_int_exp/(4*np.pi*S_int_exp*a_int_exp)*C_imag_integrand # SHAPE OF (num_nodes, num_observers, num_modes)
            

        tonal_SPL_per_mode = 10.*csdl.log10((C_real**2 + C_imag**2)/P_ref**2 / 2.) # (num_nodes, num_observers, num_modes)

        tonal_SPL_rotor = 10.*csdl.log10(
            csdl.sum(
                csdl.exp_a(10., tonal_SPL_per_mode/10.),
                axes=(2,)
            )
        )
        self.register_output(f'{component_name}_tonal_spl', tonal_SPL_rotor) # (num_nodes, num_observers)

class TrapezoidMethod(csdl.Model):
    def initialize(self):
        self.parameters.declare('input_name')
        self.parameters.declare('input_shape', types=tuple)
        self.parameters.declare('dim', types=int) # dimension in which sum is taken for numerical integration
        self.parameters.declare('output_name')
        self.parameters.declare('step_size', default=1)

    def define(self):
        input_name = self.parameters['input_name']
        input_shape = self.parameters['input_shape']
        output_name = self.parameters['output_name']
        dim = self.parameters['dim']

        h = self.declare_variable('dr')
        # h = self.parameters['step_size']

        f = self.declare_variable(input_name, shape=input_shape)
        out_pre_integration = (f[:,:,:,0:-1] + f[:,:,:,1:]) *  csdl.expand(h, shape=f[:,:,:,1:].shape)/ 2.
        out = self.register_output(output_name, csdl.sum(out_pre_integration, axes=(dim,)))

if __name__ == '__main__':
    model = KSSPLModel(
        component_name='dummy',
        num_nodes=2,
        num_observers=3,
        num_blades=2,
        num_radial=5,
        num_azim=30,
    )
    from python_csdl_backend import Simulator
    sim = Simulator(model)

    sim.run()