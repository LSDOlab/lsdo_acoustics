import csdl 
import numpy as np 
from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.tonal.KS.ks_spl_model import KSSPLModel


from lsdo_modules.module_csdl.module_csdl import ModuleCSDL

class KvurtStalnovModel(ModuleCSDL):
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
        num_azim = mesh.parameters['num_tangential']
        observer_data = self.parameters['observer_data']
        num_nodes = self.parameters['num_nodes']

        modes = self.parameters['modes']
        load_harmonics = self.parameters['load_harmonics']
        num_blades = self.parameters['num_blades']

        self.register_module_input(f'{component_name}_origin', shape=(3,), promotes=True) * 0.3048
        # NOTE: ROTOR LOCATION CHANGES W OPTIMIZER IF THE AIRCRAFT DESIGN CHANGES
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

        chord = self.register_module_input('rotor_blade_chord_length', shape=(num_radial, 3), promotes=True) # NOTE: GENERALIZE THIS NAMING
        chord_length = csdl.reshape(csdl.pnorm(chord, 2, axis=1), (num_radial, 1))
        if units == 'ft':
            chord_profile = self.register_output('chord_profile', chord_length * 0.3048)
        else:
            chord_profile = self.register_output('chord_profile', chord_length)

        self.register_module_input('altitude', shape=(num_nodes,))
        Vx = self.declare_variable('Vx', shape=(num_nodes,))
        Vy = self.declare_variable('Vy', shape=(num_nodes,))
        Vz = self.declare_variable('Vz', shape=(num_nodes,))

        # region atmospheric model (to get density)
        from lsdo_acoustics.utils.atmosphere_model import AtmosphereModel
        self.add(
            AtmosphereModel(
                shape=(num_nodes,),
            ),
            'atmosphere_model'
        )
        # endregion

        # region observer location model
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
        # endregion

        norm_hub_rad = 0.2
        dr = (1 - norm_hub_rad) * rotor_radius / (num_radial-1)
        self.register_output('dr', dr)

        # region KS SPL model
        self.add(
            KSSPLModel(
                component_name=component_name,
                num_nodes=num_nodes,
                num_observers=observer_data['num_observers'],
                num_blades=num_blades,
                num_radial=num_radial,
                num_azim = num_azim,
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