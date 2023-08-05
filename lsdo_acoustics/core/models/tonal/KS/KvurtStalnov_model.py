import csdl 
import numpy as np 
from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
# from lsdo_acoustics.core.models.tonal.KS.ks_spl_model_old import KSSPLModel
from lsdo_acoustics.core.models.tonal.KS.ks_spl_model import KSSPLModel

from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

from lsdo_acoustics.utils.a_weighting import A_weighting_func
from lsdo_acoustics.utils.atmosphere_model import AtmosphereModel

class KvurtStalnovModel(ModuleCSDL):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('disk_prefix')
        self.parameters.declare('blade_prefix')
        self.parameters.declare('mesh')
        # self.parameters.declare('num_radial')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_blades', default=2)
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        self.parameters.declare('load_harmonics', default=np.arange(0,11,1))
        self.parameters.declare('debug', default=False)
        self.parameters.declare('use_geometry', default=True)

    def define(self):
        component_name = self.parameters['component_name']
        disk_prefix = self.parameters['disk_prefix']
        blade_prefix = self.parameters['blade_prefix']
        mesh = self.parameters['mesh']
        num_radial = mesh.parameters['num_radial']
        num_azim = mesh.parameters['num_tangential']
        observer_data = self.parameters['observer_data']
        num_nodes = self.parameters['num_nodes']

        modes = self.parameters['modes']
        load_harmonics = self.parameters['load_harmonics']
        num_blades = self.parameters['num_blades']
        num_observers = observer_data['num_observers']

        test = self.parameters['debug']
        use_geometry = self.parameters['use_geometry']

        # NOTE: ROTOR LOCATION CHANGES W OPTIMIZER IF THE AIRCRAFT DESIGN CHANGES
        if test or not use_geometry:
            rotor_radius = self.register_module_input('propeller_radius')
            chord_profile = self.register_module_input('chord_profile', shape=(num_radial,))
            self.register_module_input('thrust_dir', shape=(3,))
            self.register_module_input('origin', shape=(3,))
            # self.declare_variable('nondim_sectional_radius', shape=(num_radial,)) # NOTE: ADJUST LATER 
        else:
            # Thrust vector and origin
            units = 'ft'
            if units == 'ft':
                in_plane_y = self.register_module_input(f'{disk_prefix}_in_plane_1', shape=(3, ), promotes=True) * 0.3048
                to = self.register_module_input(f'{disk_prefix}_origin', shape=(3,), promotes=True) * 0.3048
                self.register_output('origin', to)
                in_plane_x = self.register_module_input(f'{disk_prefix}_in_plane_2', shape=(3, ), promotes=True) * 0.3048
                # to = self.register_module_input(f'{component_name}_origin', shape=(3, ), promotes=True) * 0.3048
            else:
                in_plane_y = self.register_module_input(f'{disk_prefix}_in_plane_1', shape=(3, ), promotes=True)
                to = self.register_module_input(f'{disk_prefix}_origin', shape=(3,), promotes=True) 
                self.register_output('origin', to * 1)
                in_plane_x = self.register_module_input(f'{disk_prefix}_in_plane_2', shape=(3, ), promotes=True)
                # to = self.register_module_input(f'{component_name}_origin', shape=(3, ), promotes=True)
                            
            R = csdl.pnorm(in_plane_y, 2) / 2
            rotor_radius = self.register_module_output('propeller_radius', R)

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



        self.register_module_input('altitude', shape=(num_nodes,))
        Vx = self.register_module_input('Vx', shape=(num_nodes,))
        Vy = self.register_module_input('Vy', shape=(num_nodes,))
        Vz = self.register_module_input('Vz', shape=(num_nodes,))
        # rpm = self.register_module_input('rpm', shape=(num_nodes, 1), units='rpm', promotes=True)
        rpm = self.declare_variable('rpm', shape=(num_nodes, 1), units='rpm')

        # region atmospheric model (to get density)
        self.add(
            AtmosphereModel(
                shape=(num_nodes,),
            ),
            'atmosphere_model'
        )
        # endregion

        # region observer location model
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
        # endregion

        norm_hub_rad = 0.2
        dr = (1 - norm_hub_rad) * rotor_radius / (num_radial-1)
        self.register_output('dr', dr)

        # region KS SPL model
        self.add(
            KSSPLModel(
                component_name=component_name,
                num_nodes=num_nodes,
                num_observers=observer_data['num_observers'],
                num_blades=num_blades,
                num_radial=num_radial,
                num_azim=num_azim,
                modes=modes,
                load_harmonics=load_harmonics,
                test=test,
                use_geometry=use_geometry
            ),
            'ks_spl_model'
        )
        # endregion

        # A-WEIGHTING
        rotor_tonal_spl = self.declare_variable(f'{component_name}_tonal_spl', shape=(num_nodes, num_observers))
        BPF = 1. * rpm * num_blades/ 60.
        rotor_tonal_spl_A = A_weighting_func(self=self, tonal_SPL=rotor_tonal_spl, f=BPF)
        self.register_output(f'{component_name}_tonal_spl_A_weighted', rotor_tonal_spl_A)

if __name__ == '__main__':
    model = KvurtStalnovModel(
        component_name='dummy',
        num_radial=5,
        num_observers=2
    )
    from python_csdl_backend import Simulator
    sim = Simulator(model)
    sim.run()