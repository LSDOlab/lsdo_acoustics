from lsdo_acoustics.core.m3l_models.acoustics_m3l_model import AcousticsModelTemplate

class KS(AcousticsModelTemplate):
    def initialize(self, mesh, observer_data=None):
        self.model_name = 'KS'
        return super().initialize(mesh, self.model_name, observer_data=observer_data)
    