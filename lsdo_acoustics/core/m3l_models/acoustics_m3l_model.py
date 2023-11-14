import m3l
import numpy as np

class AcousticsModelTemplate(m3l.ExplicitOperation):

    def initialize(self, kwargs):
        self.parameters.declare('name', types=str)
        self.parameters.declare('num_nodes', types=int)
        self.parameters.declare('rotor_parameters', default=None)
        self.parameters.declare('custom_model', default=None)
        self.parameters.declare('acoustics_data', default=None)
        self.parameters.declare('model_name', types=str, default='SHO-TIME') # SOLVER


    def assign_attributes(self):
        self.user_name = self.parameters['name']
        self.num_nodes = self.parameters['num_nodes']

    def compute(self):
        if self.model_type == 'tonal':
            csdl_model = self.compute_tonal_noise()
        elif self.model_type == 'broadband':
            csdl_model = self.compute_broadband_noise()
        return csdl_model

    def compute_tonal_noise(self):
        '''
        Outputs:
        - csdl_model: csdl.Model()
            The csdl model that computes the outputs
        '''

        if self.model_name == 'KS':
            from lsdo_acoustics.core.models.tonal.KS.KvurtStalnov_model import KvurtStalnovModel
            model = KvurtStalnovModel(
                mesh=self.mesh,
                num_blades=self.mesh.parameters['num_blades'],
                observer_data=self.observer_data,
                num_nodes=self.num_nodes,
            )
        elif self.model_name == 'Lowson':
            from lsdo_acoustics.core.models.tonal.Lowson.Lowson_model import LowsonModel
            model = LowsonModel(
                # component_name=self.rotor_name,
                # disk_prefix=self.disk_prefix,
                # blade_prefix=self.blade_prefix,
                mesh=self.mesh,
                num_blades=self.mesh.parameters['num_blades'],
                observer_data=self.observer_data,
                num_nodes=self.num_nodes,
            )
        else:
            model = self.custom_model(
                num_nodes=self.num_nodes,
                # component_name=self.rotor_name,
                observer_data=self.observer_data,
            )
            # NOTE: or model = self.add_custom_csdl_model(...)
            # we need to add kwargs to the model most likely

        return model
    
    def compute_broadband_noise(self):
        '''
        Outputs:
        - csdl_model: csdl.Model()
            The csdl model that computes the outputs
        '''
        if self.model_name == 'BPM':
            from lsdo_acoustics.core.models.broadband.BPM.BPM_model import BPMModel
            model = BPMModel(
                num_nodes=self.num_nodes,
                # component_name=self.rotor_name,
                observer_data=self.observer_data,
            )
        elif self.model_name == 'SKM':
            from lsdo_acoustics.core.models.broadband.SKM.SKM_model import SKMBroadbandModel
            model = SKMBroadbandModel(
                num_nodes=self.num_nodes,
                observer_data=self.observer_data,
                mesh=self.mesh,
                num_blades=self.mesh.parameters['num_blades']
            )
        elif self.model_name == 'GL':
            from lsdo_acoustics.core.models.broadband.GL.GL_model import GLModel
            model = GLModel(
                num_nodes=self.num_nodes,
                # component_name=self.rotor_name,
                observer_data=self.observer_data,
                mesh=self.mesh,
                num_blades=self.mesh.parameters['num_blades']
            )
        else:
            model = self.custom_model(
                num_nodes=self.num_nodes,
                # component_name=self.rotor_name,
                observer_data=self.observer_data,
            )
            # NOTE: or model = self.add_custom_csdl_model(...)
            # we need to add kwargs to the model most likely

        return model

    def evaluate_tonal_noise(self, 
                             thrust_input: m3l.Variable, 
                             drag_input: m3l.Variable, 
                             ac_states: m3l.Variable,
                             rpm : m3l.Variable,
                             rotor_origin : m3l.Variable,
                             thrust_vector : m3l.Variable,
                             rotor_radius : m3l.Variable,
                             altitude : m3l.Variable,
                             in_plane_ex: m3l.Variable=None,
                             chord_length : m3l.Variable=None,
                             phi_profile : m3l.Variable=None) -> m3l.Variable:
        '''
        This method computes the tonal noise for one rotor.

        Outputs:
        - spl: sound pressure level (dB) at a set of observer locations
        '''
        self.model_type = 'tonal' # used in the compute() method
        self.observer_data = self._assemble_observers() # organizing observer data
        # self.rotor_name = self.component_name
        self.mesh = self.parameters['rotor_parameters']

        # NEEDED BY M3L
        self.name = f'{self.user_name}_{self.model_name}_tonal_model'
        self.arguments = {}
        self.arguments['_dT'] = thrust_input
        self.arguments['_dD'] = drag_input
        self.arguments['Vx'] = ac_states.u
        self.arguments['Vy'] = ac_states.v
        self.arguments['Vz'] = ac_states.w
        self.arguments['theta'] = ac_states.theta
        self.arguments['rpm'] = rpm
        self.arguments['origin'] = rotor_origin
        self.arguments['R'] = rotor_radius
        self.arguments['thrust_vector'] = thrust_vector
        self.arguments['altitude'] = altitude
        if self.model_name == 'Lowson':
            self.arguments['in_plane_ex'] = in_plane_ex
        elif self.model_name == 'KS':
            self.arguments['chord_length'] = chord_length
            self.arguments['phi'] = phi_profile
            # self.arguments['z'] = ac_states['z']
        # if self.model_name == 'KS':
        #     pass

        tonal_spl = m3l.Variable(
            name=f'tonal_spl', 
            shape=(self.num_nodes, self.num_observers), 
            operation=self
        )

        A_weighted_tonal_spl = m3l.Variable(
            name=f'tonal_spl_A_weighted', 
            shape=(self.num_nodes, self.num_observers), 
            operation=self
        )

        return tonal_spl, A_weighted_tonal_spl
    
    def evaluate_broadband_noise(self, ac_states: m3l.Variable, CT: m3l.Variable, rpm : m3l.Variable,
                                 thrust_vector : m3l.Variable, chord_length : m3l.Variable, 
                                 disk_origin : m3l.Variable, radius : m3l.Variable) -> m3l.Variable:
        '''
        This method computes the broadband noise for one rotor.

        Outputs:
        - spl: sound pressure level (dB) at a set of observer locations
        '''
        self.model_type = 'broadband'
        self.observer_data = self._assemble_observers()
        # self.rotor_name = self.component_name
        self.mesh = self.parameters['rotor_parameters']

        # NEEDED BY M3L

        self.name = f'{self.user_name}_{self.model_name}_broadband_model'
        self.arguments = {}
        self.arguments['Vx'] = ac_states.u
        self.arguments['Vy'] = ac_states.v
        self.arguments['Vz'] = ac_states.w
        self.arguments['theta'] = ac_states.theta
        self.arguments['CT'] = CT
        self.arguments['rpm'] = rpm
        self.arguments['thrust_vector'] = thrust_vector
        self.arguments['chord_length'] = chord_length
        self.arguments['disk_origin'] = disk_origin
        self.arguments['R'] = radius

        broadband_spl = m3l.Variable(
            name=f'broadband_spl', 
            shape=(self.num_nodes, self.num_observers), 
            operation=self
        )

        A_weighted_broadband_spl = m3l.Variable(
            name=f'broadband_spl_A_weighted', 
            shape=(self.num_nodes, self.num_observers), 
            operation=self
        )

        return broadband_spl, A_weighted_broadband_spl

    def _setup_acoustics_data(self):
        acoustics_data = self.parameters['acoustics_data']
        self.observer_group_dictionaries = acoustics_data.observer_group_dictionaries
        self.aircraft_position = acoustics_data.aircraft_position

        # self.component_name = self.parameters['component'].parameters['name']

        # self.disk_prefix = self.parameters['disk_prefix']
        # self.blade_prefix = self.parameters['blade_prefix']

        self.model_name = self.parameters['model_name']
        self.custom_model = self.parameters['custom_model']

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

        aircraft_positions = np.zeros((3, self.num_observers))
        for i in range(self.num_observers):
            aircraft_positions[:,i] = self.aircraft_position

        self.observer_data = {
            'name': self.observer_name_list,
            # 'aircraft_position': np.resize(self.aircraft_position, (3,self.num_observers)),
            'aircraft_position': aircraft_positions,
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


