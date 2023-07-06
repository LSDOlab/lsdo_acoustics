import csdl 
import numpy as np 
from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.tonal.KS.ks_spl_model import KSSPLModel

class KvurtStalnovModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('mesh')
        # self.parameters.declare('num_radial')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_blades', default=2)
        self.parameters.declare('num_nodes', default=1)
        self.parameters.declare('modes', default=[1,2,3])
        self.parameters.declare('load_harmonics', default=np.arange(0,11,1))

    def define(self):
        component_name = self.parameters['component_name']
        mesh = self.parameters['mesh']
        num_radial = mesh.parameters['num_radial']
        observer_data = self.parameters['observer_data']
        num_nodes = self.parameters['num_nodes']

        modes = self.parameters['modes']
        load_harmonics = self.parameters['load_harmonics']
        num_blades = self.parameters['num_blades']

        self.declare_variable(f'{component_name}_thrust_origin') # CENTER OF ROTOR
        # NOTE: ROTOR LOCATION CHANGES W OPTIMIZER IF THE AIRCRAFT DESIGN CHANGES

        # region observer location model
        self.add(
            SteadyObserverLocationModel(
                num_nodes=num_nodes,
                aircraft_location=observer_data['aircraft_position'],
                init_obs_x_loc=observer_data['x'],
                init_obs_y_loc=observer_data['y'],
                init_obs_z_loc=observer_data['z'],
                time_vectors=observer_data['time'],
                total_num_observers=observer_data['num_observers'],
            )
        )
        # endregion

        # region KS SPL model
        self.add(
            KSSPLModel(
                component_name=component_name,
                num_nodes=num_nodes,
                num_observers=observer_data['num_observers'],
                num_blades=num_blades,
                num_radial=num_radial,
                modes=modes,
                load_harmonics=load_harmonics
            ),
            'ks_spl_model'
        )
        # endregion

if __name__ == '__main__':
    model = KvurtStalnovModel(
        component_name='dummy',
        num_radial=5,
        num_observers=2
    )
    from python_csdl_backend import Simulator
    sim = Simulator(model)
    sim.run()