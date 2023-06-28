from lsdo_acoustics.core.m3l_models.acoustics_m3l_model import AcousticsModelTemplate

class BPM(AcousticsModelTemplate):
    def initialize(self, mesh, observer_data=None):
        self.model_name = 'BPM'
        return super().initialize(mesh, self.model_name, observer_data=observer_data)

if __name__ == '__main__':
    aaa = BPM()
    aaa.test()
    aaa._assemble_csdl_model()
    print(aaa.csdl_model)