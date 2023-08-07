import numpy as np
from lsdo_acoustics import Acoustics
from lsdo_acoustics.utils.visualization.visualize_directivity import AcousticsVisualization


# LOADING DATA
import pickle
file_name = 'acoustics_visualization_data.pcikle'
file = open(file_name, 'rb')
data = pickle.load(file)
file.close()

dc_name_list = ['hover_1', 'qst_1']
# dc_name_list = ['hover_1']
rotor_prefix_list = ['fro', 'fri', 'rro', 'rri', 'flo', 'fli', 'rlo', 'rli']
a = Acoustics(aircraft_position=np.array([0., 0., 90.]))
a.setup_directivity_plot(
    'dir_plot',
    center_point=np.array([0., 0., 0.]),
    radius=90.,
    num_azim=40
)
observer_data = a.assemble_observers()

AV = AcousticsVisualization(
    rotor_prefix_list=rotor_prefix_list,
    dc_name_list=dc_name_list,
    data_dict=data,
    observer_data=observer_data
)

spl_dictionary, theta = AV.visualize()

for key in spl_dictionary.keys():
    print('design condition: ', key)
    print('data available: ', list(spl_dictionary[key].keys()))