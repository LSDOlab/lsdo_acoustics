from lsdo_acoustics.core.m3l_models.acoustics_m3l_model import AcousticsModelTemplate

class Lowson(AcousticsModelTemplate):
    def initialize(self, kwargs):
        kwargs['model_name'] = 'Lowson'
        return super().initialize(kwargs)

if __name__ == '__main__':
    model = Lowson(mesh=1)