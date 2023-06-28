import csdl
import numpy as np

class SteadyObserverLocationModel(csdl.Model):
    '''
    This model is used to compute the observer locations relative to the moving aircraft.
    We treat the problem such that the aircraft is still and the observer moves.
    '''
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('aircraft_location')
        self.parameters.declare('initial_observer_locations')
        self.parameters.declare('observers_per_group')
        self.parameters.declare('time_vectors')
    
    def define(self):
        num_nodes = self.parameters['num_nodes']
        aircraft_location = self.parameters['aircraft_location']
        P0 = self.parameters['initial_observer_locations']
        observers_per_group = self.parameters['observers_per_group']
        time_vectors = self.parameters['time_vectors']

        observer_groups = len(P0)

        Vx = self.declare_variable('Vx', shape=(num_nodes,))
        Vy = self.declare_variable('Vy', shape=(num_nodes,))
        Vz = self.declare_variable('Vz', shape=(num_nodes,))

        # need to compute how the observer location changes relative to aircraft CG
        # we can expand this later to be relative to the rotors

