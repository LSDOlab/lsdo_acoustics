import numpy as np
import csdl

from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.broadband.SKM.skm_spl_model import SKMSPLModel

from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

class SKMBroadbandModel(ModuleCSDL):
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('mesh')
        self.parameters.declare('observer_data')
        self.parameters.declare('num_blades')
        self.parameters.declare('num_nodes', default=1)

    def define(self):
        component_name = self.parameters['component_name']
        mesh = self.parameters['mesh']
        observer_data = self.parameters['observer_data']
        num_blades = self.parameters['num_blades'] 
        num_nodes = self.parameters['num_nodes']

        num_radial = mesh.parameters['num_radial']

        self.register_module_input(f'{component_name}_origin', shape=(3,), promotes=True) * 0.3048
        self.register_module_input('rpm', shape=(num_nodes, 1), units='rpm', promotes=True)

        # Thrust vector and origin
        units = 'ft'
        if units == 'ft':
            in_plane_y = self.register_module_input(f'{component_name}_in_plane_1', shape=(3, ), promotes=True) * 0.3048
            # in_plane_x = self.register_module_input(f'{component_name}_in_plane_2', shape=(3, ), promotes=True) * 0.3048
            # to = self.register_module_input(f'{component_name}_origin', shape=(3, ), promotes=True) * 0.3048
        else:
            in_plane_y = self.register_module_input(f'{component_name}_in_plane_1', shape=(3, ), promotes=True)
            # in_plane_x = self.register_module_input(f'{component_name}_in_plane_2', shape=(3, ), promotes=True)
            # to = self.register_module_input(f'{component_name}_origin', shape=(3, ), promotes=True)
                        
        R = csdl.pnorm(in_plane_y, 2) / 2
        rotor_radius = self.register_module_output('propeller_radius', R)

        # Chord 
        # chord = self.register_module_input(f'{component_name}_chord_length', shape=(num_radial, 3), promotes=True)
        chord = self.register_module_input('rotor_blade_chord_length', shape=(num_radial, 3), promotes=True) # NOTE: GENERALIZE THIS NAMING
        chord_length = csdl.reshape(csdl.pnorm(chord, 2, axis=1), (num_radial, 1))
        if units == 'ft':
            chord_profile = self.register_output('chord_profile', chord_length * 0.3048)
        else:
            chord_profile = self.register_output('chord_profile', chord_length)


        self.add(
            SteadyObserverLocationModel(
                component_name=component_name,
                num_nodes=num_nodes,
                aircraft_location=observer_data['aircraft_position'],
                init_obs_x_loc=observer_data['x'],
                init_obs_y_loc=observer_data['y'],
                init_obs_z_loc=observer_data['z'],
                time_vectors=observer_data['time'],
                total_num_observers=observer_data['num_observers'],
            ),
            'steady_observer_location_model'
        )

        norm_hub_rad = 0.2
        dr = (1 - norm_hub_rad) * rotor_radius / (num_radial-1)
        self.register_output('dr', dr)

        self.add(
            SKMSPLModel(
                num_nodes=num_nodes,
                num_observers=observer_data['num_observers'],
                component_name=component_name,
                num_blades=num_blades,
                num_radial=num_radial
            ),
            'skm_spl_model'
        )

if __name__ == '__main__':
    model = SKMBroadbandModel(
        num_nodes=2,
        num_observers=3,
        component_name='dummy',
        num_blades=2,
        num_radial=5
    )

    from python_csdl_backend import Simulator
    sim = Simulator(model)

    sim.run()