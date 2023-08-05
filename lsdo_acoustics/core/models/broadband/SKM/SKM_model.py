import numpy as np
import csdl

from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.broadband.SKM.skm_spl_model import SKMSPLModel

from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

from lsdo_acoustics.utils.a_weighting import A_weighting_func

class SKMBroadbandModel(ModuleCSDL):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('disk_prefix')
        self.parameters.declare('blade_prefix')
        self.parameters.declare('mesh')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('debug', default=False)

    def define(self):
        component_name = self.parameters['component_name']
        disk_prefix = self.parameters['disk_prefix']
        blade_prefix = self.parameters['blade_prefix']
        mesh = self.parameters['mesh']
        observer_data = self.parameters['observer_data']
        num_observers = observer_data['num_observers']
        num_blades = self.parameters['num_blades'] 
        num_nodes = self.parameters['num_nodes']
        test = self.parameters['debug']

        num_radial = mesh.parameters['num_radial']


        # self.register_module_input(f'{disk_prefix}_origin', shape=(3,), promotes=True) * 0.3048
        self.declare_variable('rpm', shape=(num_nodes, 1), units='rpm')

        if test:
            rotor_radius = self.declare_variable('propeller_radius')
            chord_profile = self.declare_variable('chord_profile', shape=(num_radial,1))
            self.declare_variable('thrust_dir', shape=(3,))
        else:
            # Thrust vector and origin
            units = 'ft'
            if units == 'ft':
                in_plane_y = self.register_module_input(f'{disk_prefix}_in_plane_1', shape=(3, ), promotes=True) * 0.3048
                to = self.register_module_input(f'{disk_prefix}_origin', shape=(3, ), promotes=True) * 0.3048
                self.register_output('origin', to)
                in_plane_x = self.register_module_input(f'{disk_prefix}_in_plane_2', shape=(3, ), promotes=True) * 0.3048
                # in_plane_x = self.register_module_input(f'{component_name}_in_plane_2', shape=(3, ), promotes=True) * 0.3048
            else:
                in_plane_y = self.register_module_input(f'{disk_prefix}_in_plane_1', shape=(3, ), promotes=True)
                to = self.register_module_input(f'{disk_prefix}_origin', shape=(3, ), promotes=True)
                self.register_output('origin', to*1)
                in_plane_x = self.register_module_input(f'{disk_prefix}_in_plane_2', shape=(3, ), promotes=True)
                # in_plane_x = self.register_module_input(f'{component_name}_in_plane_2', shape=(3, ), promotes=True)
                            
            R = csdl.pnorm(in_plane_y, 2) / 2
            rotor_radius = self.register_module_output('propeller_radius', R)

            # Chord 
            # chord = self.register_module_input(f'{component_name}_chord_length', shape=(num_radial, 3), promotes=True)
            chord = self.register_module_input(f'{blade_prefix}_chord_length', shape=(num_radial, 3), promotes=True) # NOTE: GENERALIZE THIS NAMING
            chord_length = csdl.reshape(csdl.pnorm(chord, 2, axis=1), (num_radial, 1))
            if units == 'ft':
                chord_profile = self.register_output('chord_profile', chord_length * 0.3048)
            else:
                chord_profile = self.register_output('chord_profile', chord_length)

            # FINDING THRUST VECTOR DIRECTION
            theta = self.register_module_input(name='theta', shape=(num_nodes, 1), val=0.*np.pi/180.)
            rotation_matrix = self.create_output('rot_mat', shape=(3,3), val=0.)
            # ONLY CONSIDERING PITCH CHANGES (X-Z), NO YAW OR ROLL FOR NOW
            rotation_matrix[1, 1] = (theta + 10)/(theta + 10)
            rotation_matrix[0, 0] = csdl.cos(theta)
            rotation_matrix[0, 2] = -1 * csdl.sin(theta)
            rotation_matrix[2, 0] = -1 * csdl.sin(theta)
            rotation_matrix[2, 2] = -1 * csdl.cos(theta)
            thrust_vec = csdl.cross(in_plane_x, in_plane_y, axis=0)
            thrust_dir = csdl.matvec(rotation_matrix, thrust_vec/csdl.expand(csdl.pnorm(thrust_vec), shape=(3,)))
            self.register_output('thrust_dir', thrust_dir)

        self.add(
            SteadyObserverLocationModel(
                component_name=disk_prefix,
                num_nodes=num_nodes,
                aircraft_location=observer_data['aircraft_position'],
                init_obs_x_loc=observer_data['x'],
                init_obs_y_loc=observer_data['y'],
                init_obs_z_loc=observer_data['z'],
                time_vectors=observer_data['time'],
                total_num_observers=observer_data['num_observers'],
            ),
            'steady_observer_location_model'
        )

        norm_hub_rad = 0.2
        dr = (1 - norm_hub_rad) * rotor_radius / (num_radial-1)
        self.register_output('dr', dr)

        self.add(
            SKMSPLModel(
                num_nodes=num_nodes,
                num_observers=observer_data['num_observers'],
                component_name=component_name,
                num_blades=num_blades,
                num_radial=num_radial
            ),
            'skm_spl_model'
        )

        # A-WEIGHTING
        rpm = self.register_module_input('rpm', shape=(num_nodes, 1), units='rpm', promotes=True)
        rotor_broadband_spl = self.declare_variable(f'{component_name}_broadband_spl', shape=(num_nodes, num_observers))
        BPF = 1. * rpm * num_blades/ 60.
        rotor_broadband_spl_A = A_weighting_func(self=self, tonal_SPL=rotor_broadband_spl, f=BPF)
        self.register_output(f'{component_name}_broadband_spl_A_weighted', rotor_broadband_spl_A)

if __name__ == '__main__':
    model = SKMBroadbandModel(
        num_nodes=2,
        num_observers=3,
        component_name='dummy',
        num_blades=2,
        num_radial=5
    )

    from python_csdl_backend import Simulator
    sim = Simulator(model)

    sim.run()