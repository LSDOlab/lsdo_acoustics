from lsdo_acoustics.core.m3l_models.acoustics_m3l_model import AcousticsModelTemplate

class SKM(AcousticsModelTemplate):
    def initialize(self, kwargs):
        kwargs['model_name'] = 'SKM'
        return super().initialize(kwargs)

if __name__ == '__main__':
    aaa = SKM()
    aaa.test()
    aaa._assemble_csdl_model()
    print(aaa.csdl_model)