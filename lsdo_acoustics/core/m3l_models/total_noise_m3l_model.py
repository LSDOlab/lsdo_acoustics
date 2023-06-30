import m3l 
import numpy as np 
from lsdo_acoustics.core.models.total_noise_model import TotalAircraftNoiseModel

class TotalNoise(m3l.ExplicitOperation):
    
    def initialize(self):
        pass

    def compute(self, var_names):
        model = TotalAircraftNoiseModel(
            var_names=var_names
        )

        return model

    def evaluate(self, noise_components) -> m3l.Variable:
        '''
        This method computes the total aircraft noise at the observer locations.
        Inputs:
        - tonal and broadband spl for each rotor at each observer location
        Outputs:
        - total spl from aircraft at each observer location
        '''
        # NOTE: NEED TO FIGURE OUT HOW TO DEAL WITH NAMING CONVENTION
        var_names = ...

        operation_csdl = self.compute(var_names=var_names)

        arguments = {}
        if noise_components is not None:
            for i, name in enumerate(var_names):
                arguments[name] = noise_components[i]


        total_noise_operation = m3l.CSDLOperation(
            name='total_noise_model',
            arguments=arguments,
            operation_csdl=operation_csdl
        )

        total_spl = m3l.Variable(name='total_spl', shape=self.num_observers, operation=total_noise_operation)

        return total_spl