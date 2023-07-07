import m3l
import numpy as np

class AcousticsModelTemplate(m3l.ExplicitOperation):

    def initialize(self, kwargs):
        self.parameters.declare('component', default=None)
        self.parameters.declare('mesh', default=None)
        self.parameters.declare('model_name', types=str, default='SHO-TIME')
        self.parameters.declare('custom_model', default=None)
        self.parameters.declare('acoustics_data', default=None)

        self.num_nodes = 1

    def setup_acoustics_data(self):
        acoustics_data = self.parameters['acoustics_data']
        self.observer_group_dictionaries = acoustics_data.observer_group_dictionaries
        self.aircraft_position = acoustics_data.aircraft_position

        self.component_name = self.parameters['component'].name

        self.model_name = self.parameters['model_name']
        self.custom_model = self.parameters['custom_model']

    def compute_tonal_noise(self, rotor_name: str, observer_data: None):
        '''
        Outputs:
        - csdl_model: csdl.Model()
            The csdl model that computes the outputs
        '''

        if self.model_name == 'KS':
            from lsdo_acoustics.core.models.tonal.KS.KvurtStalnov_model import KvurtStalnovModel
            model = KvurtStalnovModel(
                num_nodes=self.num_nodes,
                component_name=rotor_name,
                observer_data=observer_data,
            )
        elif self.model_name == 'Lowson':
            from lsdo_acoustics.core.models.tonal.Lowson.Lowson_model import LowsonModel
            model = LowsonModel(
                num_nodes=self.num_nodes,
                component_name=rotor_name,
                observer_data=observer_data,
            )
        else:
            model = self.custom_model(
                num_nodes=self.num_nodes,
                component_name=rotor_name,
                observer_data=observer_data,
            )
            # NOTE: or model = self.add_custom_csdl_model(...)
            # we need to add kwargs to the model most likely

        return model
    
    def compute_broadband_noise(self, rotor_name: str, observer_data: None):
        '''
        Outputs:
        - csdl_model: csdl.Model()
            The csdl model that computes the outputs
        '''
        if self.model_name == 'BPM':
            from lsdo_acoustics.core.models.broadband.BPM.BPM_model import BPMModel
            model = BPMModel(
                num_nodes=self.num_nodes,
                component_name=rotor_name,
                observer_data=observer_data,
            )
        elif self.model_name == 'SKM':
            from lsdo_acoustics.core.models.broadband.SKM.SKM_model import SKMBroadbandModel
            model = SKMBroadbandModel(
                num_nodes=self.num_nodes,
                component_name=rotor_name,
                observer_data=observer_data
            )
        else:
            model = self.custom_model(
                num_nodes=self.num_nodes,
                component_name=rotor_name,
                observer_data=observer_data,
            )
            # NOTE: or model = self.add_custom_csdl_model(...)
            # we need to add kwargs to the model most likely

        return model

    def evaluate_tonal_noise(self, mesh, rotor_loading: m3l.Variable=None) -> m3l.Variable:
        '''
        This method computes the tonal noise for one rotor.

        Outputs:
        - spl: sound pressure level (dB) at a set of observer locations
        '''
        observer_data = self._assemble_observers()
        rotor_name = self.component_name
        operation_csdl = self.compute_tonal_noise(
            rotor_name=rotor_name,
            observer_data=observer_data
        )

        arguments = {}
        if rotor_loading is not None:
            arguments[f'{rotor_name}_rotor_loading'] = rotor_loading

        tonal_noise_operation = m3l.CSDLOperation(
            name='tonal_model',
            arguments=arguments,
            operation_csdl=operation_csdl
        )

        tonal_spl = m3l.Variable(name=f'{rotor_name}_tonal_spl', shape=self.num_observers, operation=tonal_noise_operation)

        return tonal_spl
    
    def evaluate_broadband_noise(self, rotor_loading: m3l.Variable=None) -> m3l.Variable:
        '''
        This method computes the broadband noise for one rotor.

        Outputs:
        - spl: sound pressure level (dB) at a set of observer locations
        '''
        observer_data = self._assemble_observers()
        rotor_name = self.component_name
        operation_csdl = self.compute_broadband_noise(
            rotor_name=rotor_name,
            observer_data=observer_data
        )

        arguments = {}
        if rotor_loading is not None:
            arguments[f'{rotor_name}_rotor_loading'] = rotor_loading

        broadband_noise_operation = m3l.CSDLOperation(
            name='broadband_model',
            arguments=arguments,
            operation_csdl=operation_csdl
        )

        broadband_spl = m3l.Variable(name=f'{rotor_name}_broadband_spl', shape=self.num_observers, operation=broadband_noise_operation)

        return broadband_spl


    def _assemble_observers(self):
        '''
        IN THIS REGION, WE NEED TO SOMEHOW ACCESS THE OBSERVER INFORMATION
        THE CODE BELOW ASSUMES WE HAVE IT ALREADY
        
        VECTORIZATION APPROACH:
        - convert the observers in each mission segment to one single vector
        - len is (sum of observers per segment, )
        '''
        # SETTING UP ACOUSTICS DATA HERE
        self.setup_acoustics_data()

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

    def test(self):
        print('test successful')


