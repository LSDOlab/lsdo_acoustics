import csdl
import numpy as np

class AcousticsModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_rotors')
    
    def define(self):
        num_rotors = self.parameters['num_rotors']
        
        for i in range(num_rotors):
            1

        # SPL = 10*csdl.log10(csdl.sum(10**(SPL_per_rotor/10), axes=(,)))
        # Shape of SPL is (num_nodes, num_observers)
        # NOTE: need to figure out something new for shape consistency, because different segments can have different numbers of observers