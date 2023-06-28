##test BPM_import

def test_BPM_import():
    from lsdo_acoustics.core.broadband.BPM_model import BPMModel
    from python_csdl_backend import Simulator

    sim = Simulator(BPMModel())
    


    