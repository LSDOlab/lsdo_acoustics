import numpy as np
from typing import Union

class Acoustics(object):
    def __init__(self, 
                 design_condition: CADDEE.DesignCondition, 
                 aircraft_position: np.array,
                 ):
        self.design_condition = design_condition
        self.aircraft_position = aircraft_position

        self.observer_group_dictionaries = [] # WE PASS THIS INTO M3L MODEL

        self.observer_group_names = []
        self.directivity_names = []

        self.observer_position = []
        self.observer_time_vector = []
        self.observer_velocity = []

    def add_observer(self,
                    #  name: Union[str, list],
                     name: str,
                     obs_position: np.array,
                     time_vector: np.array,
                     directivity: bool=False,
                     stationary: bool=True,
                     obs_velocity: np.array=np.array([0.,0.,0.])
                     ):
        '''
        NOTE: DO SOMETHING WITH DIRECTIVITY INPUT TO CHECK THE SIZES OF THE INPUTS
            - WE WANT TO MAKE SURE THAT SINGULAR OBSERVERS ARE DEFINED
            - EACH OBSERVER HAS A UNIQUE NAME
            - USING ONE NAME FOR MULTIPLE OBSERVERS IS CONFUSING, BUT THE DIRECTIVITY FLAG CAN HELP DIFFERENTIATE
            - IF directivity=True, WE ALLOW ONE NAME FOR MULTIPLE OBSERVERS
        '''
        if isinstance(name, list):
            if len(name) > 1:
                raise TypeError('Cannot define multiple stand-alone observers at once. \
                                For directivity plots, please use setup_directivity_plot.'
                                )
            
        num_locations = obs_position.shape[0]
        if num_locations > 1 and stationary: 
            pass # this is for directivity plots

        self.observer_group_names.append(name)

        # if directivity:
        #     self.directivity_names.append(name)
        # else:
        #     self.directivity_names.append(False)
                        
        self.observer_position.append(obs_position)
        self.observer_time_vector.append(time_vector)
        self.observer_velocity.append(obs_velocity)

        observer_group = {
            'name': name,
            'directivity': directivity, # indicates multiple positions for different observers, not one moving observer
            'init_position': obs_position,
            'time_vec': time_vector,
            'velocity': obs_velocity 
        }
        
        self.observer_group_dictionaries.append(observer_group)

    def add_evaluation_point(self,
                             ):
        pass

    # Directivity plot
    def setup_directivity_plot(self,
                               name: str,
                               center_point: np.array,
                               radius: float,
                               num_azim: int=25):
        
        angles = np.linspace(0.,2*np.pi, num_azim)
        dir_plot_boundary = np.empty((num_azim,3))
        dir_plot_boundary[:,0] = radius*np.cos(angles) + center_point[0]
        dir_plot_boundary[:,1] = radius*np.cos(angles) + center_point[1]
        dir_plot_boundary[:,2] = center_point[2]

        # NOTE: STORE NAME AND MAYBE SOMETHING ELSE TO CALL OR REFER TO THAT DATA

        # Adding each node at the boundary of the directivity plot as an observer
        self.add_observer(
            name=name,
            obs_position=dir_plot_boundary,
            time_vector=np.array[0],
            directivity=True,
            stationary=True
        )
        self.directivity_names.append(name)

    '''
    VISUALIZATION FUNCTIONS:
    NOTE: framework can be designed to automatically generate plots after running
        - automatically produces all directivity plots
    '''

    def plot_observer_distribution(self):
        for name in self.observer_group_names:
            if name in self.directivity_names:
                continue

            # extract data here or something
            

    def plot_directivity(self):
        for name in self.directivity_names:
            # extract data here or something
            pass


'''
NOTES
- Information that eneeds to get passed to CSDL models:
    - the (initial) observer locations
        - we say initial because the observers are allowed to move
        - in steady cases, the aircraft is considered "stationary" while the observer moves
        - the subsequent relative movement gets calculated based on the velocity of the flight segment
    - a time vector for steady segments
        - t = 0 represents aircraft at initial location
        - unsteady segments will have an inherent time vector (like in transition)
        - NOTE: ALL SEGMENTS WILL HAVE SOME KIND OF TRANSIENT REPRESENTATION (pseudo for steady segments)



'''