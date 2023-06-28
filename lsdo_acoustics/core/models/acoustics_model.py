import csdl
import numpy as np

from lsdo_acoustics.core.models.tonal.Lowson.Lowson_model import LowsonModel
from lsdo_acoustics.core.models.tonal.KS.KvurtStalnov_model import KvurtStlanovModel
from lsdo_acoustics.core.models.broadband.BPM_model import BPMModel

class AcousticsModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('model')
        self.parameters.declare('num_rotors')
    
    def define(self):
        model_name = self.parameters['model']
        num_rotors = self.parameters['num_rotors']

        if model_name == 'Lowson':
            model = LowsonModel()
        elif model_name == 'KS':
            model = KvurtStlanovModel()
        elif model_name == 'BPM':
            model = BPMModel()
        
        for i in range(num_rotors):
            1

        # SPL = 10*csdl.log10(csdl.sum(10**(SPL_per_rotor/10), axes=(,)))
        # Shape of SPL is (num_nodes, num_observers)
        # NOTE: need to figure out something new for shape consistency, because different segments can have different numbers of observers