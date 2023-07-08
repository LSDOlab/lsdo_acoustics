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
        # num_azim = mesh.parameters['num_tangential']
    
        # FOR TESTING PURPOSES
        sectional_D = self.declare_variable(
            'sectional_D', 
            shape=(num_nodes, num_azim, num_radial)
        )
        sectional_T = self.declare_variable(
            'sectional_T', 
            shape=(num_nodes, num_azim, num_radial)
        )

        self.declare_variable(f'{component_name}_thrust_origin')
        # PARSING MESH
        

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
            )
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

