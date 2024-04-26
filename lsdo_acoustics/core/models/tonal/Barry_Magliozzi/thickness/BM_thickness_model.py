import numpy as np
import csdl

class BMThicknessModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('num_blades', default=2)
        self.parameters.declare('num_observers', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        self.parameters.declare('num_radial')
    
    def define(self):
        p_ref = 2.e-5
        num_nodes = self.parameters['num_nodes']
        B = self.parameters['num_blades']
        num_observers = self.parameters['num_observers']
        modes = self.parameters['modes']
        num_modes = len(modes)
        num_radial = self.parameters['num_radial']

        '''
        The equations here are based on this paper:
        Applicability of Low-Fidelity Tonal and Broadband Noise Models on Small-Scale Rotors
        Hyunjune Gill, Seongkyu Lee, Marius Ruh, John T. Hwang
        link: https://www.researchgate.net/publication/367311669
        '''

        rho = self.declare_variable('density', val=1.225)
        M = self.declare_variable('mach_number', shape=(num_nodes,))
        a = self.declare_variable('speed_of_sound')
        rpm = self.declare_variable('rpm')
        Omega = rpm*2*np.pi/60. + 1.e-8

        rel_obs_position = self.declare_variable('rel_obs_position', shape=(num_nodes,3,num_observers))
        thrust_dir = csdl.expand(self.declare_variable('thrust_dir', shape=(3,)), (num_nodes, 3, num_observers), 'i->aib')
        S = csdl.reshape(self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)), new_shape=(num_nodes, num_observers))

        X = csdl.dot(rel_obs_position, thrust_dir, axis=1) # distance from rotor plane to observer (b/c rotor axis is x) 
        Y = (S**2 - X**2)**0.5 # distance from rotor axis
        self.register_output('asdf', Y)
        S0 = (X**2 +  (1-csdl.expand(M, X.shape, 'i->ij')**2)*Y**2)**0.5

        t_c = self.declare_variable('thickness_to_chord_ratio', shape=(num_radial,))
        chord = self.declare_variable('chord_profile', shape=(num_radial,))
        h = t_c*chord

        Ax = 0.6853*chord*h
        R = self.declare_variable('propeller_radius')
        dR = self.declare_variable('dr') * R

        # expand terms here for integration and across modes
        integrand_shape = (num_nodes, num_observers, 1, num_radial) # since we are looping over the integrand
        Omega_integrand = csdl.expand(Omega, integrand_shape)
        Y_integrand = csdl.expand(Y, integrand_shape, 'ij->ijab')
        R_integrand = csdl.expand(R, integrand_shape)
        a_integrand = csdl.expand(a, integrand_shape)
        S0_integrand = csdl.expand(S0, integrand_shape, 'ij->ijab')
        Ax_integrand = csdl.expand(Ax, integrand_shape, 'i->abci')
        M_integrand = csdl.expand(M, integrand_shape, 'i->iabc')
        dR_integrand  = csdl.expand(dR, integrand_shape)

        # first deal with the integrand term; output should be (num_nodes, num_observers, num_modes)
        m_array = np.zeros((num_nodes, num_observers, num_modes, num_radial))
        bessel_term = self.create_output('bessel_term', shape=m_array.shape)
        for i, m in enumerate(modes):
            m_array[:,:,i,:] = m
            bessel_term[:,:,i,:] = csdl.bessel(m*B*Omega_integrand*Y_integrand*R_integrand/(a_integrand*S0_integrand), kind=1, order=m*B)

        integrand = self.create_output('integrand', shape=(num_nodes, num_observers, num_modes, num_radial))
        for i, m in enumerate(modes):
            bessel_m1 = csdl.bessel((m*B-1)*Omega_integrand*Y_integrand*R_integrand/(a_integrand*S0_integrand), kind=1, order=int(m*B-1))
            bessel_p1 = csdl.bessel((m*B+1)*Omega_integrand*Y_integrand*R_integrand/(a_integrand*S0_integrand), kind=1, order=int(m*B+1))
            integrand[:,:,i,:] = Ax_integrand*(bessel_term[:,:,i,:] + ((1-M_integrand**2)*Y_integrand*R_integrand)/(2*S0_integrand**2)*(bessel_m1-bessel_p1))*dR_integrand
        PmT_integrated_factor = csdl.sum(integrand, axes=(3,)) # summing over radial direction

        # expand terms here across modes
        target_shape =  (num_nodes, num_observers, num_modes)
        rho_exp = csdl.expand(rho, target_shape)
        Omega_exp = csdl.expand(Omega, target_shape)
        M_exp = csdl.expand(M, target_shape, 'i->iab')
        S0_exp = csdl.expand(S0, target_shape, 'ij->ija')
        X_exp = csdl.expand(X, target_shape, 'ij->ija')

        # (num_nodes, num_observers, num_modes)
        m_array = self.declare_variable('m_array', val=m_array[:,:,:,0])
        PmT_factor = -(rho_exp*(m_array*Omega_exp)**2*B**3)/(2*np.pi*(2**0.5)*(1-M_exp**2)**2) * (S0_exp + M_exp*X_exp)**2/(S0_exp)**3

        PmT_per_mode = PmT_factor*PmT_integrated_factor # (num_nodes, num_observers, num_modes)

        # NOTE: CHECK LATER
        SPL_thickness_per_mode = 10*csdl.log10(PmT_per_mode**2/p_ref**2)
        SPL_thickness = 10*csdl.log(
            csdl.sum(
                csdl.exp_a(10., SPL_thickness_per_mode/10 + 1.e-6), axes=(2,)
            )
        )
        # print(SPL_thickness.shape)
        # exit()
        self.register_output('rotor_thickness_spl', SPL_thickness)


