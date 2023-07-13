import csdl
import numpy as np

class LoadIntegrationModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_radial', default=10) # RADIAL NODES IN BLADE
        self.parameters.declare('num_azim', default=20) # AZIMUTHAL STEPS IN ROTATION OF BLADES
        self.parameters.declare('num_blades', default=2) # NUMBER OF BLADES
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('load_harmonics', default=np.arange(0,11,1))
    
    def define(self):
        num_radial = self.parameters['num_radial']
        num_azim = self.parameters['num_azim']
        num_blades = self.parameters['num_blades']
        num_nodes = self.parameters['num_nodes']
        load_harmonics = self.parameters['load_harmonics']
        
        sectional_D = csdl.expand(
            self.declare_variable('_dD', shape=(num_nodes, num_radial, num_azim)), # num_azim should provide the number of timesteps
            shape=(num_nodes, num_blades, num_radial, num_azim),
            indices='ijk->iajk'
        )
        
        sectional_T = csdl.expand(
            self.declare_variable('_dT', shape=(num_nodes, num_radial, num_azim)), # num_azim should provide the number of timesteps
            shape=(num_nodes, num_blades, num_radial, num_azim),
            indices='ijk->iajk'
        )

        radial_sum_D = csdl.sum(sectional_D, axes=(2,)) # total blade drag as a function of theta
        radial_sum_T = csdl.sum(sectional_T, axes=(2,)) # total blade thrust as a function of theta



        theta = np.linspace(0., 2*np.pi, num_azim) # we assume num_azim is the number of azimuthal divisions in ONE ROTATION

        n_theta_prod = self.declare_variable('n_theta_prod', np.outer(load_harmonics, theta)) # (num_harmonics, num_azim)
        cos_vec = csdl.expand(csdl.cos(n_theta_prod), (num_nodes, num_blades, len(load_harmonics), num_azim), 'ij->abij') # CHECK
        sin_vec = csdl.expand(csdl.sin(n_theta_prod), (num_nodes, num_blades, len(load_harmonics), num_azim), 'ij->abij') # CHECK

        aT_integrand = self.register_output(
            'aT_integrand',
            csdl.expand(radial_sum_T, (num_nodes, num_blades, len(load_harmonics), num_azim), 'ijk->ijak') * cos_vec
        )
        aD_integrand = self.register_output(
            'aD_integrand',
            csdl.expand(radial_sum_D, (num_nodes, num_blades, len(load_harmonics), num_azim), 'ijk->ijak') * cos_vec
        )
        bT_integrand = self.register_output(
            'bT_integrand',
            csdl.expand(radial_sum_T, (num_nodes, num_blades, len(load_harmonics), num_azim), 'ijk->ijak') * sin_vec * -1.
        )
        bD_integrand = self.register_output(
            'bD_integrand',
            csdl.expand(radial_sum_D, (num_nodes, num_blades, len(load_harmonics), num_azim), 'ijk->ijak') * sin_vec * -1.
        )
        # aT_list = self.create_output('aT_list', shape=(num_nodes, num_blades, len(load_harmonics)))
        # aD_list = self.create_output('aD_list', shape=(num_nodes, num_blades, len(load_harmonics)))
        # bT_list = self.create_output('bT_list', shape=(num_nodes, num_blades, len(load_harmonics)))
        # bD_list = self.create_output('bD_list', shape=(num_nodes, num_blades, len(load_harmonics)))

        input_shape = aT_integrand.shape
        dim = 3
        input_names = ['aT_integrand', 'aD_integrand', 'bT_integrand', 'bD_integrand']
        output_names = ['aT', 'aD', 'bT', 'bD']

        for i in range(4):
            self.add(
                TrapezoidMethod(
                    input_name=input_names[i],
                    input_shape=input_shape,
                    dim=dim,
                    output_name=output_names[i],
                    num_azim=num_azim
                ),
                f'{output_names[i]}_load_integration_model'
            )

        '''
        OUTPUT SHAPE OF aT, ... is (num_nodes, num_blades, num_harmonics)
        '''



class TrapezoidMethod(csdl.Model):
    def initialize(self):
        self.parameters.declare('input_name')
        self.parameters.declare('input_shape', types=tuple)
        self.parameters.declare('dim', types=int) # dimension in which sum is taken for numerical integration
        self.parameters.declare('output_name')
        self.parameters.declare('num_azim')

    def define(self):
        input_name = self.parameters['input_name']
        input_shape = self.parameters['input_shape']
        output_name = self.parameters['output_name']
        dim = self.parameters['dim']
        num_azim = self.parameters['num_azim']

        h = self.declare_variable('dtheta', val=2.*np.pi/num_azim) # FIX TO USE THE AZIMUTHAL SEPARATIONS
        f = self.declare_variable(input_name, shape=input_shape)
        out_pre_integration = 1/(2*np.pi)*(f[:,:,:,0:-1] + f[:,:,:,1:]) *  csdl.expand(h, shape=f[:,:,:,1:].shape)/ 2.
        out = self.register_output(output_name, csdl.sum(out_pre_integration, axes=(dim,)))
        # print(out.shape)

'''
NOTE:
- start with a general trapezoid rule (make a CSDL model for this)
- then, add a higher-order method (like midpoint or Simpson)
'''

if __name__ == '__main__':
    from python_csdl_backend import Simulator

    # m = TrapezoidMethod(
    #     input_name='a',
    #     input_size=5,
    #     output_name='b'
    # )

    # sim = Simulator(m)
    # sim['step_size'] = 0.5
    # sim.run()

    m = LoadIntegrationModel()
    sim = Simulator(m)
    sim.run()
