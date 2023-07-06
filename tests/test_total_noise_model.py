import numpy as np
from lsdo_acoustics import Acoustics
from lsdo_acoustics.core.m3l_models import TotalAircraftNoise
from lsdo_acoustics.core.dummy_component import DummyComponent

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

aaa = DummyComponent(name='aaa')
bbb = DummyComponent(name='bbb')

component_list = [aaa, bbb]

total_aircraft_noise_model = TotalAircraftNoise(observer_data=a, component_list=component_list)
total_aircraft_noise_model.evaluate()