import csdl
import numpy as np

class LoadIntegrationModel(csdl.Model):
    def initialize(self):
        return super().initialize()
    
    def define(self):
        
        sectional_D = self.declare_variable('sectional_D', shape=())
        sectional_T = self.declare_variable('sectional_T', shape=())

        # self.add(
        #     TrapezoidMethod(
        #         input_name=,
        #         input_size=,
        #         output_name=,
        #     )
        # )


class TrapezoidMethod(csdl.Model):
    def initialize(self):
        self.parameters.declare('input_name')
        self.parameters.declare('input_size')
        self.parameters.declare('output_name')

    def define(self):
        input_name = self.parameters['input_name']
        input_size = self.parameters['input_size']
        output_name = self.parameters['output_name']

        h = self.declare_variable('step_size')
        f = self.declare_variable(input_name, shape=(input_size,))

        out_pre_integration = (f[0:-1] + f[1:]) *  csdl.expand(h, shape=(input_size-1,))/ 2.
        out_pre_integration = self.register_output('out', out_pre_integration)
        out = self.register_output(output_name, csdl.sum(out_pre_integration))

'''
NOTE:
- start with a general trapezoid rule (make a CSDL model for this)
- then, add a higher-order method (like midpoint or Simpson)
'''

if __name__ == '__main__':
    from python_csdl_backend import Simulator

    m = TrapezoidMethod(
        input_name='a',
        input_size=5,
        output_name='b'
    )

    sim = Simulator(m)
    sim['step_size'] = 0.5
    sim.run()
