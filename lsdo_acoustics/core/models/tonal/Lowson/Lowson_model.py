import csdl
import numpy as np
from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.tonal.Lowson.load_integration_model import LoadIntegrationModel
# from load_integration_model import LoadIntegrationModel
from lsdo_acoustics.core.models.tonal.Lowson.lowson_spl_model import LowsonSPLModel

class LowsonModel(csdl.Model):
    def initialize(self):

        self.parameters.declare('num_nodes')
        self.parameters.declare('num_blades')
        self.parameters.declare('harmonic_mode_num', default=1)
        self.parameters.declare('observer_data', types=np.array)


    def define(self):

        num_nodes = self.parameters['num_nodes']
        B = self.parameters['num_blades']
        m = self.parameters['harmonic_mode_num']
        observer_data = self.parameters['observer_data']

        # FOR TESTING PURPOSES
        sectional_D = self.declare_variable(
            'sectional_D', 
            shape=(num_nodes, num_azim, num_radial)
        )
        sectional_T = self.declare_variable(
            'sectional_T', 
            shape=(num_nodes, num_azim, num_radial)
        )
        # PARSING MESH
        

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
                total_num_observers=observer_data['num_observers'],
                rotor_location=rotor_location
            )
        )
        # endregion
        # NOTE: NEED ROTOR LOCATION RELATIVE TO AIRCRAFT CG

        # region load integration
        self.add(LoadIntegrationModel(
            num_radial=num_radial,
            num_azim=num_azim,
            num_blades=num_blades,
        ), 'load_integration_model')
        # endregion

        # region lowson SPL model
        self.add(LowsonSPLModel(
            num_blades=num_blades,
            num_observers=observer_data['num_observers'],
            component_name=component_name # FROM ROTOR
        ), 'lowson_spl_model')
        # endregion

