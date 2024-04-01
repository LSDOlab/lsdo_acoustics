import numpy as np
import csdl


class SKMSPLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('num_observers')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_radial')
        self.parameters.declare('name', default=None, types=str, allow_none=True)

    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        model_name = self.parameters['name']

        B = self.parameters['num_blades'] 
        num_radial = self.parameters['num_radial']

        rpm = csdl.reshape(self.declare_variable('rpm', shape=(num_nodes,1)), (num_nodes,))
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
        # theta0_skm = csdl.arcsin((z_skm**2)**0.5 / S0_skm)
        # self.register_output('theta_dummy', theta0_skm)
        theta0_skm = self.declare_variable('rel_angle_plane', shape=(num_nodes, num_observers))

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
        self.register_output('Ab', Ab_skm)
        sigma_skm = Ab_skm / np.pi / R_skm**2
        CT_skm = csdl.expand(
            self.declare_variable('CT', shape=(num_nodes,)),
            (num_nodes, num_observers),
            'i->ia'
        )
        SPL150_SKM = 10*csdl.log10(1e-10 + (Omega_skm*R_skm)**6*Ab_skm*(CT_skm/sigma_skm)**2) - 42.9
        SPL_SKM = SPL150_SKM + 20*csdl.log10(1e-10 + csdl.sin((theta0_skm**2)**0.5)/(S0_skm/150))

        if model_name is not None:
            self.register_output(f'{model_name}_broadband_spl', SPL_SKM) # shape is (num_nodes, num_observers)
        else:
            self.register_output('broadband_spl', SPL_SKM) # shape is (num_nodes, num_observers)

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