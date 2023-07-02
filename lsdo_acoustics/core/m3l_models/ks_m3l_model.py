from lsdo_acoustics.core.m3l_models.acoustics_m3l_model import AcousticsModelTemplate

class KS(AcousticsModelTemplate):
    def initialize(self, kwargs):
        kwargs['model_name'] = 'KS'
        return super().initialize(kwargs)
    