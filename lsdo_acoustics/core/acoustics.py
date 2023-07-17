import numpy as np
from typing import Union

class Acoustics(object):
    def __init__(self, 
                #  design_condition: CADDEE.DesignCondition, 
                #  design_condition: None,
                 aircraft_position: np.array,
                 ):
        # self.design_condition = design_condition
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
                                For directivity plots, please use setup_directivity_plot.')
            
        num_locations = obs_position.shape[0]
        if num_locations > 1 and stationary: 
            pass # this is for directivity plots

        self.observer_group_names.append(name)

        # if directivity:
        #     self.directivity_names.append(name)
        # else:
        #     self.directivity_names.append(False)
        if len(obs_position.shape) == 1:
            obs_position = obs_position.reshape(1,3)
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
                               center_point: np.array, # LATER ADD 'aircraft as another option
                               radius: float,
                               num_azim: int=25,
                               orientation = np.array([0., 1., 0.])
                               ):
        '''
        Inputs:
        - name: String to identify directivity plot points/observers
        - center point: The center point defining the directivity plot
            - 'aircraft' is used for unsteady segments
        - radius: Radius around center where we want to 
        - num_azim: Azimuthal discretization of directivity plot
        - orientation: Normal vector of the directivity plot. By default, it points vertically
        '''

        if np.linalg.norm(orientation - np.array([0., 1., 0.])) > 1e-6:
            raise Warning('Orientation has not been implemented yet \
                          By default, the surface normal vector points vertically.')
        
        angles = np.linspace(0.,2*np.pi*(num_azim-1)/num_azim, num_azim)
        dir_plot_boundary = np.empty((num_azim,3))
        dir_plot_boundary[:,0] = radius*np.cos(angles) + center_point[0]
        dir_plot_boundary[:,1] = radius*np.sin(angles) + center_point[1]
        dir_plot_boundary[:,2] = center_point[2]

        # NOTE: STORE NAME AND MAYBE SOMETHING ELSE TO CALL OR REFER TO THAT DATA

        # Adding each node at the boundary of the directivity plot as an observer
        self.add_observer(
            name=name,
            obs_position=dir_plot_boundary,
            time_vector=np.array([0]),
            directivity=True,
            stationary=True,
        )
        self.directivity_names.append(name)

    '''
    Assembling observer data
    '''
    def assemble_observers(self):
        '''
        IN THIS REGION, WE NEED TO SOMEHOW ACCESS THE OBSERVER INFORMATION
        THE CODE BELOW ASSUMES WE HAVE IT ALREADY
        
        VECTORIZATION APPROACH:
        - convert the observers in each mission segment to one single vector
        - len is (sum of observers per segment, )
        '''

        # self.observer_list = []
        self.observer_name_list = []
        self.observer_x_location = []
        self.observer_y_location = []
        self.observer_z_location = []
        self.observer_count = []
        self.observer_time = []

        self.num_observers = 0

        observer_groups = self.observer_group_dictionaries
        for observer_group in observer_groups: # loop over list
            observer_group_name = observer_group['name']
            observer_group_position = observer_group['init_position']
            observer_group_time = observer_group['time_vec']
            
            for i in range(len(observer_group_time)):
                self.observer_x_location.extend(observer_group_position[:, 0])
                self.observer_y_location.extend(observer_group_position[:, 1])
                self.observer_z_location.extend(observer_group_position[:, 2])

            observer_count = observer_group_position.shape[0]
            self.observer_name_list.extend(
                [observer_group_name] * observer_count
            )

            if len(observer_group_time) == 1:
                self.observer_time.extend(
                    # [observer_group_time] * observer_count
                    list(observer_group_time) * observer_count
                )
            else:
                self.observer_time.extend(
                    # [observer_group_time] * observer_count
                    list(observer_group_time) * observer_count
                )

            self.num_observers += (len(observer_group_time) * observer_group_position.shape[0])
        
        self.num_observer_groups = len(self.observer_name_list)

        self.observer_data = {
            'name': self.observer_name_list,
            'aircraft_position': np.resize(self.aircraft_position, (3,self.num_observers)),
            # 'aircraft_position': self.aircraft_position,
            'x': np.array(self.observer_x_location),
            'y': np.array(self.observer_y_location),
            'z': np.array(self.observer_z_location),
            'time': np.array(self.observer_time),
            'num_observers': self.num_observers # this accounts for the additional observers from time segments
        }
            
        return self.observer_data

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