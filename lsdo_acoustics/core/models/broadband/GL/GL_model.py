import csdl
import numpy as np


from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.broadband.GL.gl_spl_model import GLSPLModel
from lsdo_acoustics.utils.a_weighting import A_weighting_func


class GLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('mesh')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('debug', default=False)
        self.parameters.declare('use_geometry', default=True)

    def define(self):
        
        mesh = self.parameters['mesh']
        units = mesh.parameters['mesh_units']
        observer_data = self.parameters['observer_data']
        num_observers = observer_data['num_observers']
        num_blades = self.parameters['num_blades'] 
        num_nodes = self.parameters['num_nodes']
        test = self.parameters['debug']
        use_geometry = self.parameters['use_geometry']

        num_radial = mesh.parameters['num_radial']


        if test or not use_geometry:
            rotor_radius = self.declare_variable('propeller_radius')
            chord_profile = self.declare_variable('chord_profile', shape=(num_radial,1))
            self.declare_variable('thrust_dir', shape=(3,))
        else:
            # Thrust vector and origin
            if units == 'ft':
                r = self.declare_variable('R', shape=(num_nodes, 1))
                rotor_radius = self.register_output('propeller_radius', r * 0.3048)
                to = self.declare_variable(f'disk_origin', shape=(3, )) * 0.3048
                self.register_output('origin', to)
            else:
                r = self.declare_variable('R', shape=(num_nodes, 1))
                rotor_radius = self.register_output('propeller_radius', r * 1)
                to = self.declare_variable(f'disk_origin', shape=(3, ))
                self.register_output('origin', to*1)
                            

            # Chord 
            chord_length = self.declare_variable(f'chord_length', shape=(num_radial, )) # NOTE: GENERALIZE THIS NAMING
            if units == 'ft':
                chord_profile = self.register_output('chord_profile', chord_length * 0.3048)
            else:
                chord_profile = self.register_output('chord_profile', chord_length * 1)

            # FINDING THRUST VECTOR DIRECTION
            theta = self.declare_variable(name='theta', shape=(num_nodes, 1), val=0.*np.pi/180.)
            rotation_matrix = self.create_output('rot_mat', shape=(3,3), val=0.)
            # ONLY CONSIDERING PITCH CHANGES (X-Z), NO YAW OR ROLL FOR NOW
            rotation_matrix[1, 1] = (theta + 10)/(theta + 10)
            rotation_matrix[0, 0] = csdl.cos(theta)
            rotation_matrix[0, 2] = -1 * csdl.sin(theta)
            rotation_matrix[2, 0] = -1 * csdl.sin(theta)
            rotation_matrix[2, 2] = -1 * csdl.cos(theta)
            thrust_vec = self.declare_variable('thrust_vector', shape=(3, ))
            thrust_dir = csdl.matvec(rotation_matrix, thrust_vec/csdl.expand(csdl.pnorm(thrust_vec), shape=(3,)))
            self.register_output('thrust_dir', thrust_dir)

        self.add(
            SteadyObserverLocationModel(
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

        rpm = self.declare_variable('rpm', shape=(num_nodes, 1), units='rpm')
        # rpm = self.declare_variable('rpm', shape=(num_nodes, 1), units='rpm')

        norm_hub_rad = 0.2
        dr = (1 - norm_hub_rad) * rotor_radius / (num_radial-1)
        self.register_output('dr', dr)

        self.add(
            GLSPLModel(
                num_nodes=num_nodes,
                num_observers=num_observers,
                num_blades=num_blades,
                num_radial=num_radial
            ),
            'gl_spl_model'
        )

        # A-WEIGHTING
        rotor_broadband_spl = self.declare_variable(f'broadband_spl', shape=(num_nodes, num_observers))
        BPF = 1. * rpm * num_blades/ 60.
        rotor_broadband_spl_A = A_weighting_func(self=self, tonal_SPL=rotor_broadband_spl, f=BPF)
        self.register_output(f'broadband_spl_A_weighted', rotor_broadband_spl_A)