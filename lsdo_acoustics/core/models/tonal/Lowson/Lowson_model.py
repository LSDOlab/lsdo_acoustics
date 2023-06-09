import csdl
import numpy as np
from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.tonal.Lowson.load_integration_model import LoadIntegrationModel
# from load_integration_model import LoadIntegrationModel
from lsdo_acoustics.core.models.tonal.Lowson.lowson_spl_model import LowsonSPLModel


from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

class LowsonModel(ModuleCSDL):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('mesh')
        self.parameters.declare('num_blades')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        self.parameters.declare('load_harmonics', default=np.arange(0,11,1))

    def define(self):
        component_name = self.parameters['component_name']
        num_nodes = self.parameters['num_nodes']
        num_blades = self.parameters['num_blades']
        observer_data = self.parameters['observer_data']
        modes = self.parameters['modes']
        load_harmonics = self.parameters['load_harmonics']

        mesh = self.parameters['mesh']
        num_radial = mesh.parameters['num_radial']
        num_azim = mesh.parameters['num_tangential']
    
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
        self.register_module_input(f'{component_name}_origin', shape=(3,), promotes=True) * 0.3048
        self.register_module_input('rpm', shape=(num_nodes, 1), units='rpm', promotes=True)
        self.register_module_input('altitude', shape=(num_nodes,), promotes=True)

        # Thrust vector and origin
        units = 'ft'
        if units == 'ft':
            in_plane_y = self.register_module_input(f'{component_name}_in_plane_1', shape=(3, ), promotes=True) * 0.3048
            # in_plane_x = self.register_module_input(f'{component_name}_in_plane_2', shape=(3, ), promotes=True) * 0.3048
            # to = self.register_module_input(f'{component_name}_origin', shape=(3, ), promotes=True) * 0.3048
        else:
            in_plane_y = self.register_module_input(f'{component_name}_in_plane_1', shape=(3, ), promotes=True)
            # in_plane_x = self.register_module_input(f'{component_name}_in_plane_2', shape=(3, ), promotes=True)
            # to = self.register_module_input(f'{component_name}_origin', shape=(3, ), promotes=True)
                        
        R = csdl.pnorm(in_plane_y, 2) / 2
        self.register_module_output('propeller_radius', R)

        # region atmospheric model (to get speed of sound)
        from lsdo_acoustics.utils.atmosphere_model import AtmosphereModel
        self.add(
            AtmosphereModel(
                shape=(num_nodes,),
            ),
            'atmosphere_model'
        )
        # endregion

        a = self.declare_variable('speed_of_sound', shape=(num_nodes,))
        Vx = self.declare_variable('Vx', shape=(num_nodes,))
        Vy = self.declare_variable('Vy', shape=(num_nodes,))
        Vz = self.declare_variable('Vz', shape=(num_nodes,))

        M = self.register_output(
            'mach_number',
            (Vx**2 + Vy**2 + Vz**2)**0.5/a
        )

        '''
        NOTE:
        - add model that computes the observer position relative to EACH rotor and the angle \theta 
        '''
        # region observer position model
        self.add(
            SteadyObserverLocationModel(
                component_name=component_name,
                aircraft_location=observer_data['aircraft_position'],
                init_obs_x_loc=observer_data['x'],
                init_obs_y_loc=observer_data['y'],
                init_obs_z_loc=observer_data['z'],
                time_vectors=observer_data['time'],
                total_num_observers=observer_data['num_observers'],
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
                component_name=component_name, # FROM ROTOR
                num_nodes=num_nodes,
                num_blades=num_blades,
                num_observers=observer_data['num_observers'],
                modes=modes,
                load_harmonics=load_harmonics,
            ), 
            'lowson_spl_model'
        )
        # endregion

