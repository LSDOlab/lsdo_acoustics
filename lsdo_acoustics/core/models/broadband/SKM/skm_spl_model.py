import numpy as np
import csdl
from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

class SKMSPLModel(ModuleCSDL):
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
        Omega_2 = csdl.expand(rpm * 2*np.pi/60. + 1.e-7, (num_nodes, num_observers), 'i->ia')

        # Omega_2 = csdl.expand(
        #     csdl.reshape(
        #         self.declare_variable('rotational_speed', shape=(num_nodes,1)) * 2.*np.pi + 1.e-7,
        #         (num_nodes, )
        #     ),
        #     (num_nodes, num_observers),
        #     'i->ia'
        # )

        R_skm = csdl.expand(
            self.declare_variable(
                'propeller_radius',
                shape=(1,)
            ),
            (num_nodes,num_observers)
        )

        S0_skm = csdl.reshape(
            self.declare_variable('rel_obs_dist', shape=(num_nodes, 1, num_observers)),
            (num_nodes, num_observers)
        )
        z_skm = csdl.reshape(
            self.declare_variable('rel_obs_z_pos', shape=(num_nodes, 1, num_observers)),
            (num_nodes, num_observers)
        )
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
        Ab_skm = csdl.expand(B * csdl.sum(chord_skm * dr_skm, axes=(0,)),(num_nodes,num_observers),'i->ia')
        sigma_skm = Ab_skm / np.pi / R_skm**2
        CT_skm = csdl.expand(
            self.declare_variable('CT', shape=(num_nodes,)),
            (num_nodes, num_observers),
            'i->ia'
        )
        SPL150_SKM = 10*csdl.log10(1e-10 + (Omega_skm*R_skm)**6*Ab_skm*(CT_skm/sigma_skm)**2) - 42.9
        SPL_SKM = SPL150_SKM + 20*csdl.log10(1e-10 + csdl.sin(theta0_skm)/(S0_skm/150))

        self.register_module_output(f'{component_name}_broadband_spl', SPL_SKM) # SHAPE OF (num_nodes, num_observers)

if __name__ == '__main__':
    model = SKMSPLModel(
        num_nodes=2,
        num_observers=3,
        component_name='dummy',
        num_blades=2,
        num_radial=5
    )

    from python_csdl_backend import Simulator
    sim = Simulator(model)

    sim.run()