import numpy as np
from lsdo_acoustics import Acoustics
from lsdo_acoustics.core.m3l_models import Lowson
from python_csdl_backend import Simulator
from lsdo_acoustics.core.models.observer_location_model import SteadyObserverLocationModel

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
print(a.observer_group_dictionaries)

dummy_rotor = DummyComponent(name='rotor')

a_m3l = Lowson(component=dummy_rotor, mesh='mesh', acoustics_data=a)
# a_m3l.set_acoustics(a)
# a_m3l.observer_group_dictionaries = a.observer_group_dictionaries
a_m3l._assemble_observers()

observer_data = a_m3l.observer_data


m = SteadyObserverLocationModel(
    # num_nodes=2,
    aircraft_location=observer_data['aircraft_position'],
    init_obs_x_loc=observer_data['x'],
    init_obs_y_loc=observer_data['y'],
    init_obs_z_loc=observer_data['z'],
    time_vectors=observer_data['time'],
    total_num_observers=observer_data['num_observers']
)

sim = Simulator(m)
sim.run()

print('x:', sim['rel_obs_x_pos'])
print('y:', sim['rel_obs_y_pos'])
print('z:', sim['rel_obs_z_pos'])
print('dist:', sim['rel_obs_dist'])
print('angle:', sim['rel_obs_angle'])