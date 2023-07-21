import m3l 
import numpy as np 
from lsdo_acoustics.core.models.total_noise_model import TotalAircraftNoiseModel
from lsdo_acoustics.core.m3l_models.acoustics_m3l_model import AcousticsModelTemplate

class TotalAircraftNoise(m3l.ExplicitOperation):
    
    def initialize(self, kwargs):
        self.parameters.declare('acoustics_data', default=None)
        self.parameters.declare('component_list', default=[])
        self.parameters.declare('num_nodes', default=1)

        self.num_nodes = 1

    def compute(self):
        model = TotalAircraftNoiseModel(
            num_nodes = self.num_nodes,
            num_observers=self.observer_data['num_observers'],
            component_names=self.component_names,
            var_names = self.var_names,
            var_names_A_weighted = self.var_names_A_weighted
        )

        return model

    def evaluate(self, noise_components=None, A_weighted_noise_components=None) -> m3l.Variable:
        '''
        This method computes the total aircraft noise at the observer locations.
        Inputs:
        - NONE; 
            - NOTE: we automatically parse the noise variables based on the 
                    component name provided in the initialize step
        Outputs:
        - total spl from aircraft at each observer location
        '''
        noise, noise_A = False, False

        if noise_components is not None:
            noise = True
        if A_weighted_noise_components is not None:
            noise_A = True

        self.observer_data = self._assemble_observers() # organizing observer data
        self.num_observers = self.observer_data['num_observers']
        self.component_list = self.parameters['component_list']
        self.num_nodes = self.parameters['num_nodes']
        self.component_names = []
        for component in self.component_list:
            self.component_names.append(component.name)
            # print(component.name)

        self.name = 'total_noise_model'
        self.arguments = {}
        
        self.var_names = None
        if noise:
            self.var_names = []
            for i, comp in enumerate(noise_components):
                print(i, comp.name, type(comp.name))
                # exit()
                self.var_names.append(comp.name)
                self.arguments[comp.name] = noise_components[i]
        
        self.var_names_A_weighted = None
        if noise_A:
            self.var_names_A_weighted = []
            for i, comp in enumerate(A_weighted_noise_components):
                self.var_names_A_weighted.append(comp.name)
                self.arguments[comp.name] = A_weighted_noise_components[i]

        # NOTE: NEED TO FIGURE OUT HOW TO DEAL WITH NAMING CONVENTION
        # var_names = ...

        # operation_csdl = self.compute(var_names=var_names)

        # arguments = {}
        # if noise_components is not None:
        #     for i, name in enumerate(var_names):
        #         arguments[name] = noise_components[i]

        if noise:
            total_spl = m3l.Variable(
                name='total_spl', 
                shape=(self.num_nodes, self.num_observers), 
                operation=self
            )
        
        if noise_A:
            A_weighted_total_spl = m3l.Variable(
                name='A_weighted_total_spl', 
                shape=(self.num_nodes, self.num_observers), 
                operation=self
            )
        
        if noise and noise_A:
            return total_spl, A_weighted_total_spl
        elif noise:
            return total_spl
        elif noise_A:
            return A_weighted_total_spl
        else:
            raise ValueError('No output defined for the total noise acoustics M3L model.')

    
    def _setup_acoustics_data(self):
        acoustics_data = self.parameters['acoustics_data']
        self.observer_group_dictionaries = acoustics_data.observer_group_dictionaries
        self.aircraft_position = acoustics_data.aircraft_position

    def _assemble_observers(self):
        '''
        IN THIS REGION, WE NEED TO SOMEHOW ACCESS THE OBSERVER INFORMATION
        THE CODE BELOW ASSUMES WE HAVE IT ALREADY
        
        VECTORIZATION APPROACH:
        - convert the observers in each mission segment to one single vector
        - len is (sum of observers per segment, )
        '''
        # SETTING UP ACOUSTICS DATA HERE
        self._setup_acoustics_data()

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
            print(observer_group_name)
            print(observer_group_position)
            print(observer_group_position.shape)
            print(list(observer_group_time))
            print(observer_group_time[:])
            
            for i in range(len(observer_group_time)):
                self.observer_x_location.extend(observer_group_position[:, 0])
                self.observer_y_location.extend(observer_group_position[:, 1])
                self.observer_z_location.extend(observer_group_position[:, 2])

            observer_count = observer_group_position.shape[0]
            self.observer_name_list.extend(
                [observer_group_name] * observer_count
            )

            # if len(observer_group_time) == 1:
            #     self.observer_time.extend(
            #         # [observer_group_time] * observer_count
            #         [list(observer_group_time)] * observer_count
            #     )
            # else:
            #     self.observer_time.append(
            #         # [observer_group_time] * observer_count
            #         list(observer_group_time) * observer_count
            #     )

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


            # self.observer_time.extend(observer_group_time)
            print(len(observer_group_time), observer_group_position.shape[0])
            self.num_observers += (len(observer_group_time) * observer_group_position.shape[0])
        
        self.num_observer_groups = len(self.observer_name_list)

        aircraft_positions = np.zeros((3, self.num_observers))
        for i in range(self.num_observers):
            aircraft_positions[:,i] = self.aircraft_position

        self.observer_data = {
            'name': self.observer_name_list,
            # 'aircraft_position': np.resize(self.aircraft_position, (3,self.num_observers)),
            'aircraft_position': aircraft_positions,
            'x': np.array(self.observer_x_location),
            'y': np.array(self.observer_y_location),
            'z': np.array(self.observer_z_location),
            'time': np.array(self.observer_time),
            'num_observers': self.num_observers # this accounts for the additional observers from time segments
        }
            
        return self.observer_data