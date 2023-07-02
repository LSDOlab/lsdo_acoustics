from lsdo_acoustics.core.m3l_models.acoustics_m3l_model import AcousticsModelTemplate

class BPM(AcousticsModelTemplate):
    def initialize(self, kwargs):
        kwargs['model_name'] = 'BPM'
        return super().initialize(kwargs)

if __name__ == '__main__':
    aaa = BPM()
    aaa.test()
    aaa._assemble_csdl_model()
    print(aaa.csdl_model)