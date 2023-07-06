import csdl 
from python_csdl_backend import Simulator

class DummyModel(csdl.Model):
    def define(self):
        i1 = self.declare_variable('i1', shape=(3,))
        i2 = self.declare_variable('i2', shape=(3,1))

        self.print_var(i1)
        self.print_var(i2)

        o1 = csdl.expand(i1, (3,3), 'i->ia')
        o2 = csdl.expand(csdl.reshape(i2, (3,)), (3,3), 'i->ia')

        self.register_output('o1', o1)
        self.register_output('o2', o2)

if __name__ == '__main__':
    model = DummyModel()

    sim = Simulator(model)