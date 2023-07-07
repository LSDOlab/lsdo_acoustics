import numpy as np
import csdl

class BPMSPLModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('num_nodes')
        self.parameters.declare('num_observers')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_radial')
        
    
    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        component_name = self.parameters['component_name']

        B = self.parameters['num_blades'] 
        num_radial = self.parameters['num_radial']


        asdf = self.declare_variable('asdf')

        aaa = self.register_output('aaa', asdf**2)