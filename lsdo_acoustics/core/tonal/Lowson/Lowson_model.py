import csdl
import numpy as np
from load_integration_model import LoadIntegrationModel
from lowson_spl_model import LowsonSPLModel

class LowsonModel(csdl.Model):
    def initialize(self):

        self.parameters.declare('num_nodes')
        self.parameters.declare('num_blades')
        self.parameters.declare('harmonic_mode_num', default=1)
        self.parameters.declare('observer_location', types=np.array)


    def define(self):

        num_nodes = self.parameters['num_nodes']
        B = self.parameters['num_blades']
        m = self.parameters['harmonic_mode_num']
        n = m*B

        a = self.declare_variable('speed_of_sound')
        M = self.declare_variable('forward_mach_number') # mach number traveling forward
        R = self.declare_variable('radial_stations') # radial stations along blade
        rpm = self.declare_variable('rpm', shape=(num_nodes,))
        # observer_location = self.declare_variable('observer_location')

        # FOR TESTING PURPOSES
        num_rad = 10
        sectional_D = self.declare_variable('sectional_D', shape=(num_rad,))
        sectional_T = self.declare_variable('sectional_T', shape=(num_rad,))

        '''
        NOTE:
        - add model that computes the observer position relative to EACH rotor and the angle \theta 
        '''

        # region loading integration
        self.add(LoadIntegrationModel(

        ), 'load_integration_model')
        # endregion

        # region lowson SPL model
        self.add(LowsonSPLModel(

        ), 'lowson_spl_model')
        # endregion

