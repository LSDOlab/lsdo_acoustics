import numpy as np
import m3l


class AcousticsMesh(m3l.ExplicitOperation):
    def initialize(self, kwargs):
        self.parameters.declare('name', default='acoustics_mesh')
        self.parameters.declare('num_radial', allow_none=True)
        self.parameters.declare('num_azimuthal', allow_none=True)
        self.parameters.declare('num_blades', allow_none=True)
        self.parameters.declare('rotor_disk_mesh', default=None, allow_none=True)
        # self.parameters.declare('')
        # self.parameters.declare('')
        # self.parameters.declare('')
        # self.parameters.declare('')
        # self.parameters.declare('')
    
    def assign_attributes(self):
        self.name = self.parameters['name']