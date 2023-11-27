import csdl
import numpy as np

class SearsFunctionModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('num_observers', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        # self.parameters.declare('load_harmonics', default=np.arange(0,3,1))
        self.parameters.declare('load_harmonics', default=None)
        self.parameters.declare('num_blades', default=2)
        self.parameters.declare('num_radial')
        self.parameters.declare('num_azim')
        self.parameters.declare('test', default=False)
        self.parameters.declare('use_geometry', default=True)

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
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        modes = self.parameters['modes']
        num_modes = len(modes) # the mode harmonics of the blades that we want to consider
        if self.parameters['load_harmonics'] is None:
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
        RPM = self.declare_variable('rpm')
    
        omega = RPM*2*np.pi/60
        # R = self.declare_variable(f'{component_name}_radius')
        R = self.declare_variable('propeller_radius')
        a = self.declare_variable('speed_of_sound')
        c = self.declare_variable('chord_length', shape=(num_radial,))
        # self.print_var(c)

        if test:
            dTdR_real_loads = self.declare_variable('dTdR_real', shape=(num_nodes, num_radial))
            dDdR_real_loads = self.declare_variable('dDdR_real', shape=(num_nodes, num_radial))
            r = self.declare_variable('nondim_sectional_radius', shape=(num_radial,)) # NOTE: ADJUST LATER 
        else:
            r = self.create_input('nondim_sectional_radius', val=np.linspace(0.2, 1., num_radial)) # NOTE: ADJUST LATER 
            # setting up the steady loads
            dT = self.declare_variable('_dT', shape=(num_nodes, num_radial, num_azim)) 
            dD = self.declare_variable('_dD', shape=(num_nodes, num_radial, num_azim))
            # dT_test = self.register_output('dT_test', dT[0,-1,:])
            # dD_test = self.register_output('dD_test', dD[0,-1,:])
            # self.print_var(dT_test)
            # self.print_var(dD_test)
            dr = self.declare_variable('dr')

            dTdR_inputs = dT / csdl.expand(dr, shape=dT.shape)
            dDdR_inputs = dD / csdl.expand(dr, shape=dD.shape)

            dTdR_real_loads = csdl.reshape(dTdR_inputs[:,:,0], (num_nodes, num_radial)) 
            dDdR_real_loads = csdl.reshape(dDdR_inputs[:,:,0], (num_nodes, num_radial))

        # ======================== VARIABLE EXPANSION ========================
        target_shape = (num_nodes, B, num_harmonics, num_radial)

        r_exp = csdl.expand(r, target_shape, 'i->abci')
        omega_exp = csdl.expand(omega, target_shape)
        R_exp = csdl.expand(R, target_shape)
        a_exp = csdl.expand(a, target_shape)
        c_exp = csdl.expand(c, target_shape, 'i->abci')
        rho_exp = csdl.expand(rho, target_shape)

        r_uns = r_exp[:,:,1:,:]
        omega_uns = omega_exp[:,:,1:,:]
        R_uns = R_exp[:,:,1:,:]
        a_uns = a_exp[:,:,1:,:]
        c_uns = c_exp[:,:,1:,:]
        rho_uns = rho_exp[:,:,1:,:]

        # lambda_i_exp = csdl.expand(lambda_i, target_shape, 'ij->iabjc')
        # phi_exp = lambda_i_exp/r_exp

        if test: # inputs are lambda and r, get phi
            lambda_i = self.declare_variable('lambda_i', shape=(num_nodes, num_radial))
            lambda_i_exp = csdl.expand(lambda_i, target_shape, 'ij->iabj')
            phi_exp = lambda_i_exp / r_exp
            self.register_output('phi_exp', phi_exp)
        else: # inputs are phi and r, get lambda
            phi = csdl.reshape(self.declare_variable('phi', shape=(num_nodes, num_radial, num_azim))[:,:,0], (num_nodes, num_radial))
            # self.print_var(phi)
            phi_exp = csdl.expand(phi, target_shape, 'ij->iabj')
            lambda_i_exp = phi_exp * r_exp
            self.register_output('lambda_test', lambda_i_exp)
        phi_uns = phi_exp[:,:,1:,:]
        lambda_i_uns = lambda_i_exp[:,:,1:,:]

        lam = np.ones(shape=target_shape)
        for i in range(num_harmonics):
            lam[:,:,i,:] = i
        lam_var = self.create_input('lam_var_Sears', val=lam)

        dTdR_real = self.create_output('aT_Sears', val=0., shape=target_shape) # dTdR_real_exp
        dDdR_real = self.create_output('aD_Sears', val=0., shape=target_shape) # dDdR_real_exp 
        dTdR_imag = self.create_output('bT_Sears', val=0., shape=target_shape) # dTdR_imag_exp
        dDdR_imag = self.create_output('bD_Sears', val=0., shape=target_shape) # dDdR_imag_exp

        # ASSIGNING LOADS BASED ON HARMONICS
        # STEADY LOADS (FIRST HARMONIC (lambda = 0))
        dTdR_real[:,:,0,:] = csdl.expand(dTdR_real_loads, (num_nodes, B, 1, num_radial), 'ij->iabj')
        dDdR_real[:,:,0,:] = csdl.expand(dDdR_real_loads, (num_nodes, B, 1, num_radial), 'ij->iabj')

        # UNSTEADY LOADS (REMAINING HARMONICS)
        S_real, S_imag = self.sears_function(lam_var[:,:,1:,:], omega_uns, r_uns, R_uns, c_uns)
        w_lam = lambda_i_uns*omega_uns*R_uns/lam_var[:,:,1:,:] * q/B
        dLdR = rho_uns*(omega_uns*r_uns*R_uns)*c_uns*w_lam*np.pi
        Lreal = S_real*dLdR
        Limag = S_imag*dLdR
        
        dTdR_real[:,:,1:,:] = Lreal*csdl.cos(phi_uns)
        dDdR_real[:,:,1:,:] = Lreal*csdl.sin(phi_uns)
        dTdR_imag[:,:,1:,:] = Limag*csdl.cos(phi_uns)
        dDdR_imag[:,:,1:,:] = Limag*csdl.sin(phi_uns)
        print(dTdR_real.shape)
        # exit()