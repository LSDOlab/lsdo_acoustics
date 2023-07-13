import csdl
import numpy as np
from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

class TotalAircraftNoiseModel(ModuleCSDL):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('num_observers')
        self.parameters.declare('component_names') # LIST
        self.parameters.declare('var_names')

    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        component_names = self.parameters['component_names']
        num_components = len(component_names)
        var_names = self.parameters['var_names']
        num_vars = len(var_names)

        '''
        NOTE:
        - each rotor has a tonal and broadband component
        - in this model, sum them up for EACH component first to get total noise of each rotor
        - then, sum them up to get the combined noise from ALL rotors
        '''

        noise_components = self.create_output(
            'noise_components',
            shape=(num_vars, num_nodes, num_observers)
        )
        
        for i in range(num_vars):
            temp_var = self.declare_variable(
                var_names[i],
                shape=(num_nodes, num_observers)
            )

            noise_components[i,:,:] = csdl.expand(
                temp_var, 
                (1, num_nodes, num_observers), 
                'ij->aij'
            )
        
        total_noise = 10.*csdl.log10(
            csdl.sum(
                csdl.exp_a(10., noise_components/10.),
                axes=(0,)
            )
        )
        self.register_module_output('total_noise', total_noise)

        # indiv_rotor_noise = self.create_output(
        #     'indiv_rotor_noise',
        #     shape=(num_components, num_nodes, num_observers)
        # ) 
        # for i, component_name in enumerate(component_names):

        #     temp_tonal = self.register_module_input( # TONAL NOISE OF COMPONENT
        #         f'{component_name}_tonal_spl', 
        #         shape=(num_nodes, num_observers),
        #         # promotes=True
        #     )
        #     temp_broadband = self.register_module_input( # BROADBAND NOISE OF COMPONENT
        #         f'{component_name}_broadband_spl', 
        #         shape=(num_nodes, num_observers),
        #         # promotes=True,
        #     )

        #     total_rotor_noise = self.register_output( # TOTAL NOISE OF COMPONENT
        #         f'{component_name}_total_spl',
        #         10.*csdl.log10(
        #             csdl.exp_a(10, temp_tonal/10.) + csdl.exp_a(10., temp_broadband/10.)
        #         )
        #     )

        #     indiv_rotor_noise[i,:,:] = csdl.expand(total_rotor_noise, (1,num_nodes, num_observers), 'ij->aij')

        # total_noise = 10.*csdl.log10(
        #     csdl.sum(
        #         csdl.exp_a(10.,indiv_rotor_noise/10.),
        #         axes=(0,)
        #     )
        # )

        # self.register_output('total_noise', total_noise) # output shape is (num_nodes, num_observers)
