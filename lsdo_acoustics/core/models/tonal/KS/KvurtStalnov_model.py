import csdl 
import numpy as np 

class KvurtStalnovModel(csdl.Model):
    def define(self):
        asdf = self.declare_variable('asdf')

        aaa = self.register_output('aaa', asdf**2)