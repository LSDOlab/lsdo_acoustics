import numpy as np

from lsdo_modules.module.module import Module

class AcousticsMesh(Module):
    def initialize(self, kwargs):
        self.parameters.declare('num_radial', allow_none=True)
        self.parameters.declare('num_tangential', allow_none=True)
        self.parameters.declare('num_blades', allow_none=True)
        self.parameters.declare('rotor_disk_mesh', default=None, allow_none=True)
        # self.parameters.declare('')
        # self.parameters.declare('')
        # self.parameters.declare('')
        # self.parameters.declare('')
        # self.parameters.declare('')