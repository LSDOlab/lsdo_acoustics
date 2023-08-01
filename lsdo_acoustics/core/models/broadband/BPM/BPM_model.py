import csdl
import numpy as np
from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.broadband.BPM.bpm_spl_model import BPMSPLModel

from lsdo_acoustics.utils.atmosphere_model import AtmosphereModel

class BPMModel(ModuleCSDL):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('disk_prefix')
        self.parameters.declare('blade_prefix')
        self.parameters.declare('mesh')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('debug', default=False)
        self.parameters.declare('freq')

    def define(self):
        component_name = self.parameters['component_name']
        disk_prefix = self.parameters['disk_prefix']
        blade_prefix = self.parameters['blade_prefix']
        mesh = self.parameters['mesh']
        observer_data = self.parameters['observer_data']
        num_blades = self.parameters['num_blades'] 
        num_nodes = self.parameters['num_nodes']
        test = self.parameters['debug']
        freq = self.parameters['freq']

        num_radial = mesh.parameters['num_radial']
        num_azim = mesh.parameters['num_tangential']
        num_observers = observer_data['num_observers']

        if test:
            propeller_radius = self.declare_variable('propeller_radius')
            chord_profile = self.declare_variable('chord_profile', shape=(num_radial,1))
            twist_profile = self.declare_variable('twist_profile', val = 0. * np.pi/180, shape=(num_radial,1))
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

        # region atmospheric model (to get density and dynamic viscosity)
        self.add(
            AtmosphereModel(
                shape=(num_nodes,),
            ),
            'atmosphere_model'
        )
        # endregion

        self.add(
            SteadyObserverLocationModel(
                component_name=component_name,
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

        # region observer adjustment based on mesh
        x = self.declare_variable('rel_obs_x_pos', shape=(num_nodes, 1, num_observers))
        y = self.declare_variable('rel_obs_y_pos', shape=(num_nodes, 1, num_observers))
        z = self.declare_variable('rel_obs_z_pos', shape=(num_nodes, 1, num_observers))

        non_dim_r = self.declare_variable(
            'non_dim_rad',
            val=np.linspace(0.2, 1., num_radial)
        )
        radial_dist = csdl.expand(propeller_radius, (num_radial,)) * non_dim_r
        x_r, y_r, z_r = self.compute_rotor_frame_position(
            x, y, z, radial_dist, twist_profile, mesh, num_nodes, num_observers
        )
        self.register_output('x_r', x_r) # shape of (num_nodes, num_observers, num_radial, num_azim)
        self.register_output('y_r', y_r)
        self.register_output('z_r', z_r)
        self.register_output('S_r', (x_r**2 + y_r**2 + z_r**2)**0.5)
        # endregion
        
        # region BPM SPL inputs 
        target_shape = (num_nodes, num_observers, num_radial, num_azim)
        delta_P = self.register_module_input('delta_P', 3.1690e-04, shape=(num_nodes,num_radial)) # NOTE: FIX NAME LATER

        rho = self.declare_variable('density')
        mu = self.declare_variable('dynamic_viscosity')
        nu = self.register_output('nu', mu/rho)

        non_dim_rad_exp = csdl.expand(non_dim_r, (num_nodes, num_radial), 'i->ai' )

        rpm = csdl.expand(
            csdl.reshape(self.declare_variable('rpm', shape=(num_nodes,1)), new_shape=(num_nodes,)), 
            (num_nodes, num_radial), 'i->ia'
        )

        U = non_dim_rad_exp * 2*np.pi/60. * rpm  * csdl.expand(propeller_radius, (num_nodes, num_radial))
        self.register_output('U', U)
        # COMPUTE REYNOLDS NUMBERS HERE
        chord_exp = csdl.expand(
            csdl.reshape(chord_profile, (num_radial,)), 
            target_shape, 
            'i->abic'
        )
        # U_exp = csdl.expand(U, target_shape, 'i->iab')
        U_exp = csdl.expand(U, target_shape, 'ij->iajb')
        nu_exp  = csdl.expand(nu, target_shape)
        delta_P_exp = csdl.expand(delta_P, target_shape, 'ij->iajb')
        Rc = self.register_output('Rc', (U_exp*chord_exp/nu_exp)+1e-7)
        Rdp = self.register_output('Rdp', U_exp*delta_P_exp/nu_exp+1e-7)

        a_CL0 = self.register_module_input('a_CL0', val=0., shape=(num_radial,1))
        AOA =  self.register_module_input('aoa', val=0., shape=(num_radial,1))
        a_star = AOA - a_CL0
        self.register_output('a_star', a_star)

        # endregion
        
        self.add(
            BPMSPLModel(
                num_nodes=num_nodes,
                num_observers=num_observers,
                component_name=component_name,
                num_blades=num_blades,
                num_radial=num_radial,
                num_azim=num_azim,
                freq=freq
            ),
            'bpm_spl_model'
        )

    def compute_rotor_frame_position(self, x, y, z, radial_dist, twist_profile, mesh, num_nodes, num_observers):
        '''
        inputs:
            x, y, z: inertial frame position
            mesh: holds the num radial and num tangential info
        outputs:
            - x_r, y_r, z_r: positions in the frame of the disk element
        '''
        num_radial = mesh.parameters['num_radial']
        num_azim = mesh.parameters['num_tangential']

        target_shape = (num_nodes, num_observers, num_radial, num_azim)

        # azim_angle = np.linspace(-np.pi, np.pi, num_azim+1)[:-1]
        azim_angle = np.linspace(0, 2*np.pi, num_azim+1)[:-1]
        azim_dist = self.declare_variable('azim_dist', azim_angle)

        x_exp = csdl.expand(csdl.reshape(x, (num_nodes, num_observers)), target_shape, 'ij->ijab')
        y_exp = csdl.expand(csdl.reshape(y, (num_nodes, num_observers)), target_shape, 'ij->ijab')
        z_exp = csdl.expand(csdl.reshape(z, (num_nodes, num_observers)), target_shape, 'ij->ijab')

        twist_exp = csdl.expand(csdl.reshape(twist_profile, (num_radial,)), target_shape, 'i->abic') # twist_profile has shape (num_radial, 1)
        radius_exp = csdl.expand(radial_dist, target_shape, 'i->abic')
        azim_expanded = csdl.expand(azim_dist, target_shape, 'i->abci')

        sin_th = csdl.sin(twist_exp)
        cos_th = csdl.cos(twist_exp)
        sin_ph = csdl.sin(azim_expanded)
        cos_ph = csdl.cos(azim_expanded)
        
        beta_p = 0. # flapping angle
        coll = 0. # collective pitch

        x_r = x_exp*cos_th*sin_ph - y_exp*cos_ph*cos_th + (z_exp+radius_exp)*sin_th
        y_r = x_exp*cos_ph + y_exp*sin_th
        z_r = -x_exp*sin_ph*sin_th + y_exp*cos_ph*sin_th + (z_exp+radius_exp)*cos_th

        return x_r, y_r, z_r
