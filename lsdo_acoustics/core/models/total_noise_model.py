import csdl
import numpy as np

class TotalAircraftNoiseModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('variable_names') # LIST

    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_observers = self.parameters['num_observers']
        var_names = self.parameters['variable_names']
        num_var = len(var_names)

        indiv_rotor_noise = self.create_output(
            'indiv_rotor_noise',
            shape=(num_var, num_nodes, num_observers)
        )
        for i, name in enumerate(var_names):
            temp_var = self.declare_variable(name, shape=(num_nodes, num_observers))
            indiv_rotor_noise[i,:,:] = csdl.expand(temp_var, (1,num_nodes, num_observers), 'ij->aij')

        total_noise = 10.*csdl.log10(
            csdl.sum(
                csdl.exp_a(10.,indiv_rotor_noise/10.),
                axes=(0,)
            )
        )

        # SPL_per_rotor = 10*csdl.log10(csdl.sum(csdl.exp_a(10.,SPL_m/10.), axes=(2,)))

        self.register_output('total_noise', total_noise) # output shape is (num_nodes, num_observers)
