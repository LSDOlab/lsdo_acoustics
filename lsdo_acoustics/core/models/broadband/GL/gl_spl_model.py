import csdl 
import numpy as np
from lsdo_acoustics.utils.csdl_switch import switch_func

class GLSPLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('num_nodes')
        self.parameters.declare('num_observers')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_radial')
    
    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        component_name = self.parameters['component_name']

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

        A_b = csdl.expand(csdl.sum((chord_profile[:-1,:] + chord_profile[1:,:])/2) * dr, CT.shape)

        sigma = B*A_b/(np.pi*csdl.expand(R, A_b.shape)**2)
        
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

        theta_0 = csdl.reshape(
            csdl.arcsin(z/s_0),
            (num_nodes, num_observers)
        )

        OASPL = OASPL_ref * csdl.sin((theta_0**2.)**0.5)**beta_1 - \
                csdl.log(s_0/D) * (beta_2 + beta_3*(1-csdl.sin((theta_0**2)**0.5)))
        
        self.register_output(f'{component_name}_broadband_spl', OASPL) # shape is (num_nodes, num_observers)
        
if __name__ == '__main__':
    model = GLSPLModel(
        component_name='dummy',
        num_nodes=2,
        num_observers=2,
        num_blades=3,
        num_radial=10
    )
    from python_csdl_backend import Simulator
    sim = Simulator(model)
    sim.run()