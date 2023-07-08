import csdl
import numpy as np

P_ref = 2.e-5

class KSSPLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('num_observers', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        self.parameters.declare('load_harmonics', default=np.arange(0,11,1))
        self.parameters.declare('num_blades', default=2)
        self.parameters.declare('num_radial')

    def sears_function(self, m, omega, r, R, c):
        Ut = omega*r*R
        k = m*omega*c/(2*Ut)
        S_real = ((csdl.bessel(k,1,0)*csdl.bessel(k,1,1)**2 - csdl.bessel(k,1,1)**2*csdl.bessel(k,2,1) + \
        csdl.bessel(k,1,0)*csdl.bessel(k,1,1)*csdl.bessel(k,2,0) - csdl.bessel(k,1,1)*csdl.bessel(k,2,0)*csdl.bessel(k,2,1)) - \
        (csdl.bessel(k,1,0)*csdl.bessel(k,1,1)**2) + csdl.bessel(k,1,0)**2*csdl.bessel(k,2,1) - \
        csdl.bessel(k,1,1)**2*csdl.bessel(k,2,1) - csdl.bessel(k,1,0)*csdl.bessel(k,2,1)**2) \
            / ((csdl.bessel(k,1,1) + csdl.bessel(k,2,0))**2 + (csdl.bessel(k,1,0) - csdl.bessel(k,2,1))**2)
        S_imag = -(csdl.bessel(k,1,1)**3 + csdl.bessel(k,1,0)*csdl.bessel(k,1,1)*csdl.bessel(k,2,1) + \
            csdl.bessel(k,1,1)**2*csdl.bessel(k,2,0)+ csdl.bessel(k,1,0)*csdl.bessel(k,2,0)*csdl.bessel(k,2,1) + \
            csdl.bessel(k,1,0)**2*csdl.bessel(k,1,1)) - csdl.bessel(k,1,0)*csdl.bessel(k,1,1)*csdl.bessel(k,2,1) - \
            csdl.bessel(k,1,0)*csdl.bessel(k,1,1)*csdl.bessel(k,2,1) + csdl.bessel(k,1,1)*csdl.bessel(k,2,1)**2 / \
            ((csdl.bessel(k,1,1) + csdl.bessel(k,2,0))**2 + (csdl.bessel(k,1,0) - csdl.bessel(k,2,1))**2) # CHECK THIS LINE AGAIN
        return S_real, S_imag

    def define(self):
        component_name = self.parameters['component_name']
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        modes = self.parameters['modes']
        num_modes = len(modes) # the mode harmonics of the blades that we want to consider
        harmonics = self.parameters['load_harmonics']
        num_harmonics = len(harmonics) # discrete harmonics considered during truncation of fourier series
        B = self.parameters['num_blades']

        num_radial = self.parameters['num_radial']

        q = 0.05 # gust amplification factor

        rho = self.declare_variable('rho')
        x = csdl.reshape(self.declare_variable('rel_obs_x_pos', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))
        y = self.declare_variable('rel_obs_y_pos', shape=(num_nodes, 1, num_observers))
        z = self.declare_variable('rel_obs_z_pos', shape=(num_nodes, 1, num_observers))
        S = csdl.reshape(self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))

        RPM = self.declare_variable('revolutions_per_minute') # NOTE: UPDATE/FIX LATER
        # BPF = m*RPM*B/60.
        theta = csdl.arccos(x/S)
        r = self.declare_variable('nondim_sectional_radius', shape=(num_nodes, num_radial)) # NOTE: ADJUST LATER 
        lambda_i = self.declare_variable('sectional_inflow_ratio', shape=(num_nodes, num_radial))
        phi = lambda_i/r # DELETE

        omega = RPM*2*np.pi/60
        R = self.declare_variable(f'{component_name}_radius')
        a = self.declare_variable('speed_of_sound')
        c = self.declare_variable('rotor_chord', shape=(num_radial,))

        # setting up the steady loads
        dTdR_real_loads = self.declare_variable('dTdR', shape=(num_nodes, num_radial)) 
        dDdR_real_loads = self.declare_variable('dDdR', shape=(num_nodes, num_radial))
        dTdR_imag_loads = self.declare_variable('dTdR_imag', val=0., shape=(num_nodes, num_radial)) # FIX SHAPE
        dDdR_imag_loads = self.declare_variable('dDdR_imag', val=0., shape=(num_nodes, num_radial)) # FIX SHAPE

        # ======================== VARIABLE EXPANSION ========================
        target_shape = (num_nodes, num_observers, 1, num_radial, 1)

        theta_exp = csdl.expand(theta, target_shape, 'ij->ijabc')
        r_exp = csdl.expand(r, target_shape, 'ij->iabjc')
        lambda_i_exp = csdl.expand(lambda_i, target_shape, 'ij->iabjc')
        phi_exp = lambda_i_exp/r_exp
        omega_exp = csdl.expand(omega, target_shape)
        R_exp = csdl.expand(R, target_shape)
        a_exp = csdl.expand(a, target_shape)
        c_exp = csdl.expand(c, target_shape, 'i->abcid')
        rho_exp = csdl.expand(rho, target_shape)

        # ======================== CREATING OUTPUTS ========================
        An = self.create_output('An', shape=(num_nodes, num_observers, num_modes, num_radial, num_harmonics))
        Bn = self.create_output('Bn', shape=(num_nodes, num_observers, num_modes, num_radial, num_harmonics))
        tonal_SPL_per_mode = self.create_output('tonal_SPL_per_mode', shape=(num_nodes, num_observers, num_modes))

        for i in range(num_modes):
            m = modes[i] # mode
            for j in harmonics: # (in Hyunjune's code, this is lam)
                j = int(j)

                if j == 0: # steady loads 
                    # derivatives of T and D wrt r from steady formulation
                    # expand to shape=(num_nodes, num_observers, 1, 1)
                    dTdR_real = csdl.expand(dTdR_real_loads, (num_nodes, num_observers, 1, num_radial, 1), 'ij->iabjc') # CHECK SHAPE
                    dDdR_real = csdl.expand(dDdR_real_loads, (num_nodes, num_observers, 1, num_radial, 1), 'ij->iabjc') # CHECK SHAPE
                    dTdR_imag = csdl.expand(dTdR_imag_loads, (num_nodes, num_observers, 1, num_radial, 1), 'ij->iabjc') # CHECK SHAPE
                    dDdR_imag = csdl.expand(dDdR_imag_loads, (num_nodes, num_observers, 1, num_radial, 1), 'ij->iabjc') # CHECK SHAPE

                else: # "unsteady" loads
                    S_real, S_imag = self.sears_function(j, omega_exp, r_exp, R_exp, c_exp)
                    w_lam = q*lambda_i_exp*omega_exp*R_exp/(j*B)
                    Vt = 0.
                    dLdR = np.pi*rho_exp*(omega_exp*r_exp*R_exp-Vt) * c_exp * w_lam
                    Lreal = S_real*dLdR
                    Limag = S_imag*dLdR

                    dTdR_real = Lreal*csdl.cos(phi_exp)
                    dDdR_real = Lreal*csdl.sin(phi_exp)
                    dTdR_imag = Limag*csdl.cos(phi_exp)
                    dDdR_imag = Limag*csdl.sin(phi_exp)

                ind = int((m-j)*B)

                if np.mod(ind,2) == 0:
                    # REAL VALUES
                    if np.mod(ind,4) == 2:
                        coeff = -1.
                    elif np.mod(ind,4) == 0:
                        coeff = 1.

                    # SHAPE OF (num_nodes, num_observers, 1, 1)
                    An[:,:,i,:,j] = (dTdR_real*csdl.cos(theta_exp) - dDdR_real*ind*a_exp/(m*B*omega_exp*r_exp*R_exp)) * \
                    csdl.bessel(m*B*omega_exp*r_exp*R_exp/a_exp*csdl.sin(theta_exp), order=ind)*coeff

                    # IMAGINARY VALUES
                    if (-ind+1 < 0) and (np.mod(np.abs(-ind+1), 4) == 1):
                        coeff = -1.
                    elif (-ind+1 < 0) and (np.mod(np.abs(-ind+1), 4) == 3):
                        coeff = 1.
                    elif (-ind+1 > 0) and (np.mod(np.abs(-ind+1), 4) == 1):
                        coeff = 1.
                    elif (-ind+1 > 0) and (np.mod(np.abs(-ind+1), 4) == 3):
                        coeff = -1.

                    # SHAPE OF (num_nodes, num_observers, 1, 1)
                    Bn[:,:,i,:,j] = (dTdR_imag*csdl.cos(theta_exp) - dDdR_imag*ind*a_exp/(m*B*omega_exp*r_exp*R_exp)) * \
                    csdl.bessel(m*B*omega_exp*r_exp*R_exp/a_exp*csdl.sin(theta_exp), order=ind)*coeff

                elif np.mod(ind,2) == 1:
                    # REAL VALUES
                    if np.mod(-ind+1,4) == 2:
                        coeff = -1.
                    elif np.mod(-ind+1,4) == 0:
                        coeff = 1.

                    # SHAPE OF (num_nodes, num_observers, 1, 1)
                    An[:,:,i,:,j] = (dTdR_imag*csdl.cos(theta_exp) - dDdR_imag*ind*a_exp/(m*B*omega_exp*r_exp*R_exp)) * \
                    csdl.bessel(m*B*omega_exp*r_exp*R_exp/a_exp*csdl.sin(theta_exp), order=ind)*coeff

                    # IMAGINARY VALUES
                    if (-ind < 0) and (np.mod(np.abs(ind), 4) == 1):
                        coeff = -1.
                    elif (-ind < 0) and (np.mod(np.abs(ind), 4) == 3):
                        coeff = 1.
                    elif (-ind > 0) and (np.mod(np.abs(ind), 4) == 1):
                        coeff = 1.
                    elif (-ind > 0) and (np.mod(np.abs(ind), 4) == 3):
                        coeff = -1.

                    # SHAPE OF (num_nodes, num_observers, 1, 1)
                    Bn[:,:,i,:,j] = (dTdR_real*csdl.cos(theta_exp) - dDdR_real*ind*a_exp/(m*B*omega_exp*r_exp*R_exp)) * \
                    csdl.bessel(m*B*omega_exp*r_exp*R_exp/a_exp*csdl.sin(theta_exp), order=ind)*coeff

            self.register_output(f'An_{m}', csdl.sum(An[:,:,i,:,:], axes=(4,))) # REMOVES LAST DIMENSION FOR num_harmonics
            self.register_output(f'Bn_{m}', csdl.sum(Bn[:,:,i,:,:], axes=(4,))) # REMOVES LAST DIMENSION FOR num_harmonics
            # ======================== INTEGRATING COEFFICIENTS ========================
            integrand_inputs = [f'An_{m}', f'Bn_{m}'] 
            output_names = [f'C_real_integrand_{m}', f'C_imag_integrand_{m}']
            '''
            INPUTS HAVE SHAPE: (num_nodes, num_observers, 1, num_radial)
            OUTPUTS HAVE SHAPE: (num_nodes, num_observers, 1)
            '''
            for j, variable in enumerate(integrand_inputs):
                self.add(
                    TrapezoidMethod(
                        input_name=variable,
                        input_shape=(num_nodes,num_observers,1,num_radial),
                        dim=3,
                        output_name=output_names[j]
                    ),
                    f'{variable}_integration_model'
                )

            # OUTPUTS OF INTEGRATION
            C_real_integrand = self.declare_variable(output_names[0], shape=(num_nodes, num_observers, 1)) # SHAPE OF (num_nodes, num_observers, 1) 
            C_imag_integrand = self.declare_variable(output_names[1], shape=(num_nodes, num_observers, 1)) # SHAPE OF (num_nodes, num_observers, 1)

            target_int_shape = (num_nodes, num_observers, 1)
            omega_int_exp = csdl.expand(omega, target_int_shape)
            S_int_exp = csdl.expand(S, target_int_shape, 'ij->ija') # dimension for a is of size 1
            a_int_exp = csdl.expand(a, target_int_shape)

            C_real = m*B**2*omega_int_exp/(4*np.pi*S_int_exp*a_int_exp)*C_real_integrand # SHAPE OF (num_nodes, num_observers, 1) corresponding to 1 mode
            C_imag = m*B**2*omega_int_exp/(4*np.pi*S_int_exp*a_int_exp)*C_imag_integrand # SHAPE OF (num_nodes, num_observers, 1) corresponding to 1 mode
            # print(num_modes)
            # print(i)
            # print(C_real.shape)
            # print(C_imag.shape)
            tonal_SPL_per_mode[:,:,i] = 10.*csdl.log10((C_real**2 + C_imag**2)/P_ref) 
            # SHAPE OF (num_nodes, num_observers, 1) corresponding to 1 mode
            # tonal_SPL_per_model overall has shape (num_nodes, num_observers, num_modes)

        tonal_SPL_rotor = 10.*csdl.log10(
            csdl.sum(
                csdl.exp_a(10., tonal_SPL_per_mode/10.),
                axes=(2,)
            )
        ) # FIX TO SUM ACROSS THE MODES
        self.register_output(f'{component_name}_tonal_SPL', tonal_SPL_rotor) # SHAPE OF (num_nodes, num_observers)




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

        h = self.declare_variable('step_size')
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
        num_radial=5
    )
    from python_csdl_backend import Simulator
    sim = Simulator(model)

    sim.run()