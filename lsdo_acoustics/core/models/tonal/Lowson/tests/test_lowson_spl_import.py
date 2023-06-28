##test lowson_spl_import

def test_lowson_spl_import():
    from lsdo_acoustics.core.tonal.Lowson.lowson_spl_model import LowsonSPLModel
    from python_csdl_backend import Simulator

    sim = Simulator(LowsonSPLModel())
    


    