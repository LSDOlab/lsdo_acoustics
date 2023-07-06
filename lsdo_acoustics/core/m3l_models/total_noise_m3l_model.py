import m3l 
import numpy as np 
from lsdo_acoustics.core.models.total_noise_model import TotalAircraftNoiseModel

class TotalAircraftNoise(m3l.ExplicitOperation):
    
    def initialize(self, kwargs):
        self.parameters.declare('observer_data', default=None)
        self.parameters.declare('component_list', default=[])

        self.num_nodes = 1

    def compute(self, var_names):
        model = TotalAircraftNoiseModel(
            num_nodes = self.num_nodes,
            num_observers=self.observer_data['num_observers'],
            component_list=self.component_list
        )

        return model

    def evaluate(self) -> m3l.Variable:
        '''
        This method computes the total aircraft noise at the observer locations.
        Inputs:
        - NONE; 
            - NOTE: we automatically parse the noise variables based on the 
                    component name provided in the initialize step
        Outputs:
        - total spl from aircraft at each observer location
        '''
        self.observer_data = self.parameters['observer_data']
        self.component_list = self.parameters['component_list']
        for component in self.component_list:
            print(component.name)
        # NOTE: NEED TO FIGURE OUT HOW TO DEAL WITH NAMING CONVENTION
        # var_names = ...

        # operation_csdl = self.compute(var_names=var_names)

        # arguments = {}
        # if noise_components is not None:
        #     for i, name in enumerate(var_names):
        #         arguments[name] = noise_components[i]


        # total_noise_operation = m3l.CSDLOperation(
        #     name='total_noise_model',
        #     arguments=arguments,
        #     operation_csdl=operation_csdl
        # )

        # total_spl = m3l.Variable(name='total_spl', shape=self.num_observers, operation=total_noise_operation)

        # return total_spl