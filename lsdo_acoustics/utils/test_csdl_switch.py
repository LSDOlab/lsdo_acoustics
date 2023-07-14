import csdl
import numpy as np
from lsdo_acoustics.utils.csdl_switch import switch_func

class CSDLSwitchTest(csdl.Model):
    def initialize(self):
        self.parameters.declare('input_shape')
    
    def define(self):
        input_shape = self.parameters['input_shape']
        x = self.declare_variable('x', shape=input_shape)
        f1 = self.register_output('f1', x-1.)
        f2 = self.register_output('f2', x+0.5)
        f3 = self.register_output('f3', x*5.)
        funcs_list = [f1, f2, f3]
        bounds_list = [1.,6.]

        y = switch_func(x, funcs_list, bounds_list)
        self.register_output('y', y)
    
from python_csdl_backend import Simulator

x = np.array([0., 3., 7.])
input_shape = x.shape

model = CSDLSwitchTest(input_shape=input_shape)
sim = Simulator(model)

sim['x'] = np.array([0., 3., 7])

sim.run()
