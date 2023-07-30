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

    def define(self):
        component_name = self.parameters['component_name']
        disk_prefix = self.parameters['disk_prefix']
        blade_prefix = self.parameters['blade_prefix']
        mesh = self.parameters['mesh']
        observer_data = self.parameters['observer_data']
        num_blades = self.parameters['num_blades'] 
        num_nodes = self.parameters['num_nodes']
        test = self.parameters['debug']

        num_radial = mesh.parameters['num_radial']
        num_observers = observer_data['num_observers']

        if test:
            propeller_radius = self.declare_variable('propeller_radius')
            chord_profile = self.declare_variable('chord_profile', shape=(num_radial,1))
            twist_profile = self.declare_variable('twist_profile', val = 0., shape=(num_radial,1))
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

        # region BPM SPL inputs 
        target_shape = (num_nodes, num_observers, num_radial)
        delta_P = self.register_module_input('delta_P', 1.025e-4, shape=(num_nodes,)) # NOTE: FIX NAME LATER

        rho = self.declare_variable('density')
        mu = self.declare_variable('dynamic_viscosity')
        nu = self.register_output('nu', mu/rho)

        non_dim_rad = csdl.expand(
            self.declare_variable('non_dim_rad', np.linspace(0.2, 1, num_radial)),
            (num_nodes, num_radial), 'i->ai'
        )
        rpm = self.declare_variable('rpm', shape=(num_nodes,1))

        # Vx = self.declare_variable('Vx', shape=(num_nodes,), val=0.)
        # Vy = self.declare_variable('Vy', shape=(num_nodes,), val=0.)
        # Vz = self.declare_variable('Vz', shape=(num_nodes,), val=0.)

        # U = self.register_output('U', (Vx**2 + Vy**2 + Vz**2)**0.5 + 1e-7)

        rpm = csdl.expand(
            csdl.reshape(self.declare_variable('rpm', shape=(num_nodes,1)), new_shape=(num_nodes,)), 
            (num_nodes, num_radial), 'i->ia'
        )

        U = non_dim_rad * 2*np.pi/60. * rpm  * csdl.expand(propeller_radius, (num_nodes, num_radial))
        self.register_output('U', U)
        # COMPUTE REYNOLDS NUMBERS HERE
        chord_exp = csdl.expand(
            csdl.reshape(chord_profile, (num_radial,)), 
            (num_nodes, num_observers, num_radial), 
            'i->abi'
        )
        # U_exp = csdl.expand(U, target_shape, 'i->iab')
        U_exp = csdl.expand(U, target_shape, 'ij->iaj')
        nu_exp  = csdl.expand(nu, target_shape)
        delta_P_exp = csdl.expand(delta_P, target_shape, 'i->iab')
        Rc = self.register_output('Rc', (U_exp*chord_exp/nu_exp)+1e-7)
        Rdp = self.register_output('Rdp', U_exp*delta_P_exp/nu_exp+1e-7)

        a_CL0 = self.register_module_input('a_CL0', val=0., shape=(num_radial,1))
        a_star = twist_profile - a_CL0
        self.register_output('a_star', a_star)

        # endregion
        

        self.add(
            BPMSPLModel(
                num_nodes=num_nodes,
                num_observers=num_observers,
                component_name=component_name,
                num_blades=num_blades,
                num_radial=num_radial
            ),
            'bpm_spl_model'
        )