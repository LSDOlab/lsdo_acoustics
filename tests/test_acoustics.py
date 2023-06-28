import numpy as np
from lsdo_acoustics.core.acoustics import Acoustics
from lsdo_acoustics.core.m3l_models.lowson_m3l_model import Lowson


a = Acoustics(design_condition=1, 
              aircraft_position=np.array([0,0,0])
              )

a.add_observer(name='obs',
               obs_position=np.array([0.,0.,1.]),
               time_vector=np.linspace(0,1,5),
               )

a.setup_directivity_plot(name='plot',
                         center_point=np.array([0.,0.,0]),
                         radius=1,
                         num_azim=4
                         )
print(a.observer_group_dictionaries)
a_m3l = Lowson(mesh='mesh', acoustics_data=a)
# a_m3l.set_acoustics(a)
# a_m3l.observer_group_dictionaries = a.observer_group_dictionaries
a_m3l._assemble_observers()