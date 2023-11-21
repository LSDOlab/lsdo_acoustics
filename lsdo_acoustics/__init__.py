__version__ = '0.0.0'
from lsdo_acoustics.core.acoustics import Acoustics

try:
    from lsdo_acoustics.core.m3l_models.lowson_m3l_model import Lowson
    from lsdo_acoustics.core.m3l_models import Lowson, KS, SKM, GL, TotalAircraftNoise
    from lsdo_acoustics.core import m3l_models
    from lsdo_acoustics.utils.helper_functions import evaluate_multiple_acoustic_models
except:
    pass


from pathlib import Path
ROOT = Path(__file__).parents[0]
GEOMETRY_PATH = ROOT / 'core' / 'sample_geometry' / 'geometry'
IMPORTS_PATH = ROOT / 'core' / 'sample_geometry' / 'imports'
