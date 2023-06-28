from lsdo_acoustics.core.m3l_models.acoustics_m3l_model import AcousticsModelTemplate

class Lowson(AcousticsModelTemplate):
    def initialize(self, mesh, acoustics_data):
        self.model_name = 'Lowson'
        return super().initialize(mesh, acoustics_data, self.model_name)

if __name__ == '__main__':
    model = Lowson(mesh=1)