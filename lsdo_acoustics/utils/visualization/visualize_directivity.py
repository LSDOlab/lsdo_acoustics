import numpy as np
import re
import csdl
from python_csdl_backend import Simulator
from lsdo_acoustics import Acoustics

from lsdo_acoustics.core.models.broadband.GL.GL_model import GLModel
from lsdo_acoustics.core.models.tonal.KS.KvurtStalnov_model import KvurtStalnovModel
from lsdo_acoustics.core.models.tonal.Lowson.Lowson_model import LowsonModel

from lsdo_acoustics.core.models.total_noise_model import TotalAircraftNoiseModel

'''
Input: data dictionary in the dashboard

use the design conditions, model names (Lowson, KS, GL) 
'''

class DummyMesh(object):
    def __init__(self) -> None:
        self.parameters = {
            'num_radial': 25,
            'num_tangential': 25,
        }

dummy_mesh = DummyMesh()

class AcousticsVisualization(object):
    def __init__(self, rotor_prefix_list, dc_name_list, data_dict, observer_data, sim: Simulator=None) -> None:
        # if sim is None:
        #     raise ValueError('Requires a simulator object.')
        
        # self.sim = sim
        self.rotor_prefix_list = rotor_prefix_list
        self.dc_name_list = dc_name_list
        self.data_dict = data_dict
        self.observer_data = observer_data

        self.acoustics_models = ['Lowson', 'KS', 'GL']

        self.common_inputs = ['rpm', 'propeller_radius', 'thrust_dir', 'origin', 'Vx', 'Vy', 'Vz']
        self.Lowson_inputs = ['_dD', '_dT']
        self.KS_inputs = ['chord_profile', 'phi', '_dD', '_dT']
        self.GL_inputs = ['chord_profile', 'CT']

        full_input_list = []
        full_input_list.extend(self.common_inputs)
        full_input_list.extend(self.Lowson_inputs)
        full_input_list.extend(self.KS_inputs)
        full_input_list.extend(self.GL_inputs)
        self.full_input_list = list(set(full_input_list))

    def visualize(self):
        self.dc_data_dict = self.parse_variables()

        theta = self.calculate_angle()

        spl_dictionary, sim_list = self.evaluate(self.dc_data_dict)

        return spl_dictionary, theta
    
    def calculate_angle(self):
        x = self.observer_data['x']
        y = self.observer_data['y']

        r = (x**2 + y**2)**0.5
        theta = np.arctan2(y,x)
        theta_full = list(theta)
        theta_full.append(theta_full[0])
        
        return np.array(theta_full)
    
    def evaluate(self, dc_data_dict):
        sim_list = []
        spl_dictionary = {}
        for dc in dc_data_dict:
            sim = self.assemble_simulator(dc, dc_data_dict[dc])
            sim.run()
            sim_list.append(sim)
            
            temp_dict = {}
            total_spl = sim['total_noise_model.total_spl']
            A_weighted_total_spl = sim['total_noise_model.A_weighted_total_spl']

            # RESHAPING TO DUPLICATE THE FIRST POINT
            total_spl_full = list(total_spl[0])
            total_spl_full.append(total_spl_full[0])
            A_weighted_total_spl_full = list(A_weighted_total_spl[0])
            A_weighted_total_spl_full.append(A_weighted_total_spl_full[0])
            # print(total_spl_full)
            # exit()


            temp_dict['total_spl'] = np.array(total_spl_full)
            temp_dict['A_weighted_total_spl'] = np.array(A_weighted_total_spl_full)
            spl_dictionary[dc] = temp_dict

        return spl_dictionary, sim_list



    def assemble_simulator(self, dc, data_dict):

        model = csdl.Model()
        var_names = []
        var_names_A_weighted = []
        full_model_names = []
        model_types = []
        component_connection_list = []
        
        for component in data_dict.keys():
            unique_model_list = list(set(data_dict[component]['model']))
            for model_name in unique_model_list:

                if model_name == 'KS':
                    temp_model = KvurtStalnovModel(
                        component_name=component,
                        disk_prefix='disk',
                        blade_prefix='blade',
                        mesh=dummy_mesh,
                        observer_data=self.observer_data,
                        use_geometry=False
                    )
                    model_name += '_tonal'

                    var_names.append(f'{component}_tonal_spl')
                    var_names_A_weighted.append(f'{component}_tonal_spl_A_weighted')

                    model_type = 'tonal'

                elif model_name == 'GL':
                    temp_model = GLModel(
                        component_name=component,
                        disk_prefix='disk',
                        blade_prefix='blade',
                        mesh=dummy_mesh,
                        observer_data=self.observer_data,
                        use_geometry=False,
                        num_blades=2
                    )
                    model_name += '_broadband'

                    var_names.append(f'{component}_broadband_spl')
                    var_names_A_weighted.append(f'{component}_broadband_spl_A_weighted')

                    model_type = 'broadband'

                elif model_name == 'Lowson':
                    temp_model = LowsonModel(
                        component_name=component,
                        disk_prefix='disk',
                        mesh=dummy_mesh,
                        observer_data=self.observer_data,
                        use_geometry=False,
                        num_blades=2
                    )
                    model_name += '_tonal'

                    var_names.append(f'{component}_tonal_spl')
                    var_names_A_weighted.append(f'{component}_tonal_spl_A_weighted')

                    model_type = 'tonal'

                model_types.append(model_type)
                component_connection_list.append(component)

                full_model_name = dc+'_'+component+'_disk_'+model_name+'_model'
                full_model_names.append(full_model_name)
                print(full_model_name)
                # exit()

                model.add(
                    temp_model,
                    name=full_model_name,
                    promotes=[]
                )
        print(var_names)
        # exit()
        model.add(
            TotalAircraftNoiseModel(
                num_observers=self.observer_data['num_observers'],
                component_names=list(data_dict.keys()),
                var_names=var_names,
                var_names_A_weighted=var_names_A_weighted
            ),
            'total_noise_model'
        )

        for i in range(len(var_names)):
            # connecting var for normal spl to total noise
            model.connect(full_model_names[i] + f'.{component_connection_list[i]}_{model_types[i]}_spl', var_names[i])
            # connecting var for A-weighted spl to total noise
            model.connect(full_model_names[i] + f'.{component_connection_list[i]}_{model_types[i]}_spl_A_weighted', var_names_A_weighted[i])

        sim = Simulator(model, analytics=True, name=f'dir_plot_{dc}')
        # ADDING CONNECTIONS HERE TO TOTAL NOISE MODEL
        
        for component in data_dict.keys():
            print(component)
            variable_list = data_dict[component]['variable']
            values_list = data_dict[component]['val']
            for i, var in enumerate(variable_list):
                sim[var] = values_list[i]

        return sim
        


    def parse_variables(self):
        # Finding the acoustics variables in the simulator by checking for the acoustics model names
        self.acoustics_variables_list = []
        for key in self.data_dict.keys():
            split_key_full = re.split(r'[._]', key) # splitting with .
            for model in self.acoustics_models:
                if model in split_key_full:
                    self.acoustics_variables_list.append(key)
                    print(model)
                    break

        print('acoustics variables have been found')
        # organizing the list of acoustics variables
        self.acoustics_variables = {}
        for name in self.acoustics_variables_list:
            split_key_period = re.split(r'[.]', name) # splitting with . and _
            split_key_full = re.split(r'[._]', name) # splitting with .

            for model in self.acoustics_models:
                if model in split_key_full: # means that model is in the string
                    for dc_name in self.dc_name_list:
                        if dc_name in split_key_period[0]: # means that dc is in the variable name
                            # print(dc_name)
                            # exit()
                            for rotor_pref in self.rotor_prefix_list:
                                if rotor_pref in split_key_full: # means rotor prefix is in variable name
                                    for var in self.full_input_list:
                                        if var in split_key_period: # means variable is in the name
                                            new_dict_key = split_key_period[:]
                                            self.acoustics_variables[name] = {
                                                'dc': dc_name,
                                                'component': rotor_pref,
                                                'model': model,
                                                'val': self.data_dict[name],
                                            }
                                    break # rotor prefix has been satisfied, can exit loop
                                else:
                                    continue # means rotor prefix is not satisfied, continue checking
                            break # dc has been satisfied, can exit
                        else:
                            continue # dc_name has not been satisfied
                    break # model name satisfied, can exit
                else:
                    continue # model name has not been satisfied

        
        '''
        At this point, we have a dictionary where the keys are variable names, and the sub-dictionaries
        have info on the design condition, rotor name, model and the value
        '''
        
        # Reorganizing variables on a PER-DESIGN CONDITION BASIS
        # for now consider only hover
        dc_data_dict = {}
        for dc in self.dc_name_list:
            dc_data_dict[dc] = {}
            for comp_name in self.rotor_prefix_list:
                dc_data_dict[dc][comp_name] = {
                    'model': [],
                    'val': [],
                    'variable': [],
                }


        for key in self.acoustics_variables.keys():
            dc_name = self.acoustics_variables[key]['dc']
            comp_name = self.acoustics_variables[key]['component']
            
            # dc_data_dict[dc_name][comp_name]['model'] = self.acoustics_variables[key]['model']
            # dc_data_dict[dc_name][comp_name]['val'] = self.acoustics_variables[key]['val']
            # dc_data_dict[dc_name][comp_name]['variable'] = key

            dc_data_dict[dc_name][comp_name]['model'].append(self.acoustics_variables[key]['model'])
            dc_data_dict[dc_name][comp_name]['val'].append(self.acoustics_variables[key]['val'])
            dc_data_dict[dc_name][comp_name]['variable'].append(key)


        '''
        OUTPUT IS A NESTED DICTIONARY:
        - design condition
            - component name (of rotors)
                - lists for the:
                    - noise model used
                    - value of variable
                    - full variable namespace
        '''

        return dc_data_dict

        










if __name__ == '__main__':
    # LOADING DATA
    import pickle
    file_name = 'acoustics_visualization_data.pcikle'
    file = open(file_name, 'rb')
    data = pickle.load(file)
    file.close()

    dc_name_list = ['hover_1', 'qst_1']
    rotor_prefix_list = ['fro', 'fri', 'rro', 'rri', 'flo', 'fli', 'rlo', 'rli']
    a = Acoustics(aircraft_position=np.array([0., 0., 90.]))
    a.setup_directivity_plot(
        'dir_plot',
        center_point=np.array([0., 0., 0.]),
        radius=45.,
        num_azim=40
    )
    observer_data = a.assemble_observers()

    AV = AcousticsVisualization(
        rotor_prefix_list=rotor_prefix_list,
        dc_name_list=dc_name_list,
        data_dict=data,
        observer_data=observer_data
    )









# def plot_acoustics(num_GLs=8, num_KS=8, disk_prefixes=['','','']):
#     # sim = Simulator(m, analytics=True)

#     a = Acoustics(inputs['obs_loc'])
#     a.setup_directivity_plot(
#         name='dir_plot',
#         center_point=[0., 0., 0.,],
#         radius=4.,
#         num_azim=50
#     )
    
#     obs_data = a.assemble_observers()

#     noise_post_process_model = csdl.Model()

#     for prefix in disk_prefixes:
#         mt = KvurtStalnovModel(
#             component_name=prefix
#         )
#         noise_post_process_model.add(f'{prefix}_KS', mt)

#         mb = GLModel(
#             component_name=prefix
#         )
#         noise_post_process_model.add(f'{prefix}_GL', mb)
    
#     total_noise = TotalAircraftNoiseModel(
#         arg=arg,
#     )

#     noise_post_process_model.add('total_noise', total_noise, promotes=[])

#     sim = Simulator(noise_post_process_model)

#     for prefix in disk_prefixes:
#         sim[f'{prefix}_KS_phi'] = data_dict['system_level']