import csdl
import numpy as np

class BPMModel(csdl.Model):
    def define(self):
        asdf = self.declare_variable('asdf')

        aaa = self.register_output('aaa', asdf**2)