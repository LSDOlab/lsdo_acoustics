import csdl
import numpy as np
from lsdo_acoustics.utils.csdl_switch import switch_func

class CSDLSwitchTest(csdl.Model):
    def initialize(self):
        self.parameters.declare('x_val')
    
    def define(self):
        x_val = self.parameters['x_val']
        x = self.declare_variable('x', val=x_val)
        f1 = self.register_output('f1', x-1.)
        f2 = self.register_output('f2', x+0.5)
        f3 = self.register_output('f3', x*5.)
        funcs_list = [f1, f2, f3]
        bounds_list = [1.,6.]
        y = self.create_output('y', shape=len(funcs_list))
        y = switch_func(x=x, y=y, funcs_list=funcs_list, bounds_list=bounds_list)
        self.register_output('sum', csdl.sum(y))

    
from python_csdl_backend import Simulator

model = CSDLSwitchTest(x_val = 1.5)
sim = Simulator(model)

sim.run()