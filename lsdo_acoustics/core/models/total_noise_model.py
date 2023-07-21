import csdl
import numpy as np
from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

class TotalAircraftNoiseModel(ModuleCSDL):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('num_observers')
        self.parameters.declare('component_names') # LIST
        self.parameters.declare('var_names')
        self.parameters.declare('var_names_A_weighted')

    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        component_names = self.parameters['component_names']
        num_components = len(component_names)
        var_names = self.parameters['var_names']
        var_names_A = self.parameters['var_names_A_weighted']

        '''
        NOTE:
        - each rotor has a tonal and broadband component
        - in this model, sum them up for EACH component first to get total noise of each rotor
        - then, sum them up to get the combined noise from ALL rotors
        '''
        # TOTAL NOISE COMPUTATION
        if var_names is not None:
            num_vars = len(var_names)
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
            self.register_module_output('total_spl', total_noise)

        # A-WEIGHTED TOTAL NOISE COMPUTATION   
        if var_names_A is not None: 
            num_vars_A = len(var_names_A)
            noise_components_A = self.create_output(
                'A_weighted_noise_components',
                shape=(num_vars_A, num_nodes, num_observers)
            )

            for i in range(num_vars_A):
                temp_var = self.declare_variable(
                    var_names_A[i],
                    shape=(num_nodes, num_observers)
                )

                noise_components_A[i,:,:] = csdl.expand(
                    temp_var, 
                    (1, num_nodes, num_observers), 
                    'ij->aij'
                )
            
            total_noise_A = 10.*csdl.log10(
                csdl.sum(
                    csdl.exp_a(10., noise_components_A/10.),
                    axes=(0,)
                )
            )
            self.register_module_output('A_weighted_total_spl', total_noise_A)
        