import csdl
import numpy as np

class TotalAircraftNoiseModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('component_names') # LIST

    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        component_names = self.parameters['component_names']
        num_components = len(component_names)

        '''
        NOTE:
        - each rotor has a tonal and broadband component
        - in this model, sum them up for EACH component first to get total noise of each rotor
        - then, sum them up to get the combined noise from ALL rotors
        '''

        indiv_rotor_noise = self.create_output(
            'indiv_rotor_noise',
            shape=(num_components, num_nodes, num_observers)
        )
        for i, component_name in enumerate(component_names):

            temp_tonal = self.declare_variable( # TONAL NOISE OF COMPONENT
                f'{component_name}_tonal_spl', 
                shape=(num_nodes, num_observers)
            )
            temp_broadband = self.declare_variable( # BROADBAND NOISE OF COMPONENT
                f'{component_name}_broadband_spl', 
                shape=(num_nodes, num_observers)
            )

            total_rotor_noise = self.register_output( # TOTAL NOISE OF COMPONENT
                f'{component_name}_total_spl',
                10.*csdl.log10(
                    csdl.exp_a(10, temp_tonal/10.) + csdl.exp_a(10., temp_broadband/10.)
                )
            )

            indiv_rotor_noise[i,:,:] = csdl.expand(total_rotor_noise, (1,num_nodes, num_observers), 'ij->aij')

        total_noise = 10.*csdl.log10(
            csdl.sum(
                csdl.exp_a(10.,indiv_rotor_noise/10.),
                axes=(0,)
            )
        )

        self.register_output('total_noise', total_noise) # output shape is (num_nodes, num_observers)
