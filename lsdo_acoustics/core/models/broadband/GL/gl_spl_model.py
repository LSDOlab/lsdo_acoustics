import csdl 
import numpy as np
from lsdo_acoustics.utils.csdl_switch import switch_func

class GLSPLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('num_observers')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_radial')
        self.parameters.declare('freq_band', default=np.array(
            [12.5, 16, 20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 
             500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000,
             10000, 12500, 16000, 20000,
             25000, 31500, 40000, 50000, 63000 # additional ones used by Hyunjune
             ] 
        ))
    
    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']

        B = self.parameters['num_blades'] 
        num_radial = self.parameters['num_radial']

        freq_band = self.parameters['freq_band']
        frequency_band = self.create_input('frequency_band', freq_band)
        num_freq_band = len(freq_band)

        '''
        Inputs to model:
            - C_T (thrust coefficient)
            - theta_0 (elevation angle)
            - R (rotor radius)
            - S (observer distance)
            - chord profile
        Computed in the model (for the final SPL):
            - M_t (blade mach number)
            - c (solidity-weighted chord length)
            - sigma (rotor solidity)
            - V_t (tip velocity)
        
        NOTE: _pe suffix means "pre expansion"
        '''
        CT_pe = self.declare_variable('CT', shape=(num_nodes,))
        chord_profile_pe = self.declare_variable('chord_profile', shape=(num_radial,))
        S_pe = csdl.reshape(self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)), (num_nodes, num_observers))
        theta_0_pe = self.declare_variable('rel_angle_plane', shape=(num_nodes, num_observers))
        R_pe = self.declare_variable('propeller_radius') # 1.7145
        dr_pe = self.declare_variable('dr')
        rpm_pe = self.declare_variable('rpm', shape=(num_nodes,))
        a_pe = self.declare_variable('speed_of_sound', shape=(num_nodes,), val=343.)

        V_aircraft = self.declare_variable('V_aircraft', shape=(num_nodes, 3))
        V_inf = csdl.pnorm(V_aircraft, axis=1)
        omega_pe = rpm_pe*2.*np.pi/60.
        V_tip_pe = csdl.expand(
            omega_pe*csdl.expand(R_pe, (num_nodes,)), 
            (num_nodes, num_observers),
            'i->ia'
        ) - csdl.expand(V_inf, (num_nodes, num_observers),'i->ia') # correction with the retreating blade

        A_b = csdl.expand(csdl.sum((chord_profile_pe))*dr_pe, CT_pe.shape)
        # A_b = csdl.expand(csdl.sum((chord_profile_pe[:-1] + chord_profile_pe[1:])*dr_pe/2), CT_pe.shape)
        sigma_pe = A_b*B/(np.pi*csdl.expand(R_pe, A_b.shape)**2)
        c_sw_pe = sigma_pe * np.pi * csdl.expand(R_pe, A_b.shape)/B
        # c_sw_pe = A_b/csdl.expand(R_pe, (num_nodes,))

        # region expanding variables
        target_shape = (num_nodes, num_observers, num_freq_band)
        frequency_band = csdl.expand(frequency_band, target_shape, 'i->abi')
        sigma = csdl.expand(sigma_pe, target_shape, 'i->iab')
        V_t = csdl.expand(V_tip_pe, target_shape, 'ij->ija')
        M_t = V_t / csdl.expand(a_pe, target_shape, 'i->iab')
        CT = csdl.expand(CT_pe, target_shape, 'i->iab')
        theta_0 = csdl.expand(theta_0_pe, target_shape, 'ij->ija')
        S = csdl.expand(S_pe, target_shape, 'ij->ija')
        R = csdl.expand(R_pe, target_shape)
        St = frequency_band*csdl.expand(c_sw_pe, target_shape, 'i->iab')/V_t
        # endregion

        f0 = csdl.log10(V_t**7.84) * 10.
        f1 = sigma
        f2 = 0.9*M_t*sigma*(M_t+3.82)
        f3 = 1. # NOT USED
        f4 = 1. # NOT USED
        f5 = -2.*M_t**2 + 2.06
        f6 = -CT * M_t * (CT-csdl.sin((theta_0**2)**0.5)+2.06) + 1.
        f7 = CT
        # f8 = 4.97*CT*csdl.sin((theta_0**2)**0.5)*(4.3*S/R*M_t - (S/R) + 4.3) # OLD FORMULATION
        f8 = 4.97*CT*csdl.sin((theta_0**2)**0.5)*(1.5*S/R*M_t - (S/R) + 15.)

        num = f0*(St-(f1*csdl.log10(CT) + f2*csdl.log10(sigma)))**0.6
        den_1 = csdl.exp_a(
            St - (f1*csdl.log10(CT) + f2*csdl.log10(sigma)) + f5,
            f6
        )
        den_2 = csdl.exp_a(
            f7*(St - (f1*csdl.log10(CT) +  f2*csdl.log10(sigma))),
            f8
        )
        SPL_1_3 = num/(den_1 + den_2)
        
        self.register_output('broadband_spl_spectrum', SPL_1_3)

        OASPL = 10.*csdl.log10(
            csdl.sum(
                csdl.exp_a(10., SPL_1_3/10.),
                axes=(2,) # OVER THE FREQUENCY AXIS
            )
        )
        self.register_output('broadband_spl', OASPL) # shape is (num_nodes, num_observers)


class GLSPLModelOld(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('num_observers')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_radial')
    
    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']

        B = self.parameters['num_blades'] 
        num_radial = self.parameters['num_radial']

        rpm = self.declare_variable('rpm', shape=(num_nodes,))
        R = self.declare_variable('propeller_radius')
        omega = rpm * 2.*np.pi/60.
        V_tip = csdl.expand(
            omega*csdl.expand(R, (num_nodes,)), 
            (num_nodes, num_observers),
            'i->ia'
        )

        CT = csdl.expand(
            self.declare_variable('CT', shape=(num_nodes,)),
            (num_nodes, num_observers),
            'i->ia'
        )

        chord_profile = self.declare_variable('chord_profile', shape=(num_radial, 1))
        dr = self.declare_variable('dr')

        # A_b = B*csdl.expand(csdl.sum((chord_profile[:-1,:] + chord_profile[1:,:])/2) * dr, CT.shape)
        A_b = B*csdl.expand(csdl.sum(chord_profile)*dr, CT.shape)
        self.register_output('Ab', A_b)

        sigma = A_b/(np.pi*csdl.expand(R, A_b.shape)**2)
        self.register_output('sigma', sigma)
        
        OASPL_low = 10.*csdl.log10(V_tip**3.68*A_b**0.9*(CT/sigma)**1.6) + 27.076
        OASPL_high = 10.*csdl.log10(V_tip**7.44*A_b**0.9*(CT/sigma)**1.6) -75.921

        funcs_list = [OASPL_low, OASPL_high]
        bounds_list = [1.]

        OASPL_ref = switch_func(A_b, funcs_list, bounds_list)

        beta_1 = 0.031
        beta_2 = 6.2429
        beta_3 = 0.7267

        D = csdl.expand(2*R, (num_nodes, num_observers))
        s_0 =   csdl.reshape(self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)), (num_nodes, num_observers))
        z =     csdl.reshape(self.declare_variable('rel_obs_z_pos', shape=(num_nodes, 1, num_observers)), (num_nodes, num_observers))

        # theta_0 = csdl.reshape(
        #     csdl.arcsin(z/s_0),
        #     (num_nodes, num_observers)
        # )
        # self.register_output('gl_dummy_theta', theta_0)

        theta_0 = self.declare_variable('rel_angle_plane', shape=(num_nodes, num_observers))

        OASPL = OASPL_ref * csdl.sin((theta_0**2.)**0.5)**beta_1 - \
                csdl.log10(s_0/D) * (beta_2 + beta_3*(1-csdl.sin((theta_0**2)**0.5)))
        
        self.register_output(f'broadband_spl', OASPL) # shape is (num_nodes, num_observers)
        
if __name__ == '__main__':
    model = GLSPLModel(
        num_nodes=2,
        num_observers=3,
        num_blades=3,
        num_radial=10
    )
    from python_csdl_backend import Simulator
    sim = Simulator(model, display_scripts=True)
    sim.run()