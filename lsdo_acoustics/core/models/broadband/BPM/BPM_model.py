import csdl
import numpy as np

from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel
from lsdo_acoustics.core.models.broadband.BPM.bpm_spl_model import BPMSPLModel

class BPMModel(csdl.Model):
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

        self.add(
            BPMSPLModel(
                num_nodes=num_nodes,
                num_observers=observer_data['num_observers'],
                component_name=component_name,
                num_blades=num_blades,
                num_radial=num_radial
            ),
            'bpm_spl_model'
        )