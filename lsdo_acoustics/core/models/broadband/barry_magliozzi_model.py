import numpy as np
import csdl

class BarryMagliozziBroadbandModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('num_observers')

    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']

        B = self.parameters['num_blades'] 
        num_radial = self.parameters['num_radial']

        Omega_2 = self.declare_variable('rotational_speed', shape=(num_nodes,1)) * 2.*np.pi + 1.e-7

        R_skm = csdl.expand(
            self.declare_variable(
                'propeller_radius',
                shape=(1,)
            ),
            (num_nodes,1,num_observers)
        )

        S0_skm = self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers))
        z_skm = self.declare_variable('rel_obs_z_pos', shape=(num_nodes, 1, num_observers))
        theta0_skm = csdl.arcsin((z_skm**2)**0.5 / S0_skm)

        Omega_skm = Omega_2 + 1.e-6

        chord_skm = self.declare_variable('chord_profile', shape=(num_radial, 1))
        dr_skm = csdl.expand(
            self.declare_variable(
                'dr',
                shape=(1,)
            ), 
            (num_radial,1), 'i->ji'
        )
        Ab_skm = csdl.expand(B * csdl.sum(chord_skm * dr_skm, axes=(0,)),(num_nodes,1),'i->ji')
        sigma_skm = Ab_skm / np.pi / R_skm**2
        CT_skm = self.declare_variable('CT', shape=(num_nodes,1))

        SPL150_SKM = 10*csdl.log10(1e-10 + (Omega_skm*R_skm)**6*Ab_skm*(CT_skm/sigma_skm)**2) - 42.9
        SPL_SKM = SPL150_SKM + 20*csdl.log10(1e-10 + csdl.sin(theta0_skm)/(S0_skm/150))