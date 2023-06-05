##test lowson_spl

def test_lowson_spl_model():
    from lsdo_acoustics.core.tonal.Lowson.lowson_spl_model import LowsonSPLModel
    from python_csdl_backend import Simulator

    m = LowsonSPLModel(
        num_nodes=1,
        num_blades=2,
        num_observers=3
    )

    sim = Simulator(m)
    