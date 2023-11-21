import csdl
import numpy as np
from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.tonal.Lowson.load_integration_model import LoadIntegrationModel
# from load_integration_model import LoadIntegrationModel
# from lsdo_acoustics.core.models.tonal.Lowson.lowson_spl_model_old import LowsonSPLModel
from lsdo_acoustics.core.models.tonal.Lowson.lowson_spl_model import LowsonSPLModel

from lsdo_acoustics.utils.a_weighting import A_weighting_func




class LowsonModel(csdl.Model):
    def initialize(self):
        # self.parameters.declare('component_name')
        # self.parameters.declare('disk_prefix')
        self.parameters.declare('mesh')
        self.parameters.declare('num_blades')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        self.parameters.declare('load_harmonics', default=np.arange(0,11,1))
        self.parameters.declare('debug', default=False)
        self.parameters.declare('use_geometry', default=True)

    def define(self):
        # component_name = self.parameters['component_name']
        # disk_prefix = self.parameters['disk_prefix']
        num_nodes = self.parameters['num_nodes']
        num_blades = self.parameters['num_blades']
        observer_data = self.parameters['observer_data']
        num_observers = observer_data['num_observers']

        modes = self.parameters['modes']
        load_harmonics = self.parameters['load_harmonics']

        mesh = self.parameters['mesh']
        num_radial = mesh.parameters['num_radial']
        num_azim = mesh.parameters['num_tangential']
        units = mesh.parameters['mesh_units']

        test = self.parameters['debug'] # USE FOR VALIDATION PURPOSES
        use_geometry = self.parameters['use_geometry']
        # FOR TESTING PURPOSES
        sectional_D = self.declare_variable(
            '_dD', 
            shape=(num_nodes, num_radial, num_azim)
        )
        sectional_T = self.declare_variable(
            '_dT', 
            shape=(num_nodes, num_radial, num_azim)
        )

        # self.declare_variable(f'{component_name}_thrust_origin', shape=(3,))
        # rpm = self.declare_variable('rpm', shape=(num_nodes, 1), units='rpm')
        rpm = self.declare_variable('rpm', shape=(num_nodes, 1), units='rpm')
        self.declare_variable('altitude', shape=(num_nodes,), val=0.)

        # Thrust vector and origin
        if test or not use_geometry:
            self.declare_variable('propeller_radius')
            self.declare_variable('thrust_dir', shape=(3,))
            self.declare_variable('in_plane_ex', shape=(3,))
            self.declare_variable('origin', shape=(3,))
        else:
            if units == 'ft':
                r = self.declare_variable('R', shape=(num_nodes, 1))
                self.register_output('propeller_radius', r * 0.3048)
                self.declare_variable(f'disk_origin', shape=(3,)) * 0.3048

            else:
                r = self.declare_variable('R', shape=(num_nodes, 1))
                self.register_output('propeller_radius', r * 1)
                self.declare_variable(f'disk_origin', shape=(3,)) * 1
                            
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

        # region atmospheric model (to get speed of sound)
        from lsdo_acoustics.utils.atmosphere_model import AtmosphereModel
        self.add(
            AtmosphereModel(
                shape=(num_nodes,),
            ),
            'atmosphere_model'
        )

        a = self.declare_variable('speed_of_sound', shape=(num_nodes,))
        # endregion

        if test:
            # Vx = self.declare_variable('Vx', shape=(num_nodes,))
            # Vy = self.declare_variable('Vy', shape=(num_nodes,))
            # Vz = self.declare_variable('Vz', shape=(num_nodes,))
            # M = self.register_output( 'mach_number', (Vx**2 + Vy**2 + Vz**2)**0.5/a)

            M  = self.declare_variable('mach_number')
            Vx = self.register_output('Vx', csdl.expand(M, (num_nodes, ))*a)
        else:
            Vx = self.declare_variable('Vx', shape=(num_nodes,))
            Vy = self.declare_variable('Vy', shape=(num_nodes,))
            Vz = self.declare_variable('Vz', shape=(num_nodes,))

            M = self.register_output( 'mach_number', (Vx**2 + Vy**2 + Vz**2)**0.5/a)

        '''
        NOTE:
        - add model that computes the observer position relative to EACH rotor and the angle \theta 
        '''
        # region observer position model
        self.add(
            SteadyObserverLocationModel(
                aircraft_location=observer_data['aircraft_position'],
                init_obs_x_loc=observer_data['x'],
                init_obs_y_loc=observer_data['y'],
                init_obs_z_loc=observer_data['z'],
                time_vectors=observer_data['time'],
                total_num_observers=num_observers,
            ),
            'observer_location_model'
        )
        # endregion
        # NOTE: NEED ROTOR LOCATION RELATIVE TO AIRCRAFT CG

        # region load integration
        self.add(
            LoadIntegrationModel(
                num_radial=num_radial,
                num_azim=num_azim,
                num_blades=num_blades,
            ), 
            'load_integration_model'
        )
        # endregion

        # region lowson SPL model
        self.add(
            LowsonSPLModel(
                num_nodes=num_nodes,
                num_blades=num_blades,
                num_observers=num_observers,
                modes=modes,
                load_harmonics=load_harmonics,
            ), 
            'lowson_spl_model'
        )
        # endregion

        # A-WEIGHTING
        rotor_tonal_spl = self.declare_variable(f'tonal_spl_compute', shape=(num_nodes, num_observers))
        self.register_output('tonal_spl', rotor_tonal_spl * 1)
        BPF = 1. * rpm * num_blades/ 60.
        rotor_tonal_spl_A = A_weighting_func(self=self, tonal_SPL=rotor_tonal_spl, f=BPF)
        self.register_output(f'tonal_spl_A_weighted', rotor_tonal_spl_A)
