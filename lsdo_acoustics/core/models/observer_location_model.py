import csdl
import numpy as np

class SteadyObserverLocationModel(csdl.Model):
    '''
    This model is used to compute the observer locations relative to the moving aircraft.
    We treat the problem such that the aircraft is still and the observer moves.
    '''
    def initialize(self):
        self.parameters.declare('component_name')
        self.parameters.declare('aircraft_location')
        self.parameters.declare('init_obs_x_loc')
        self.parameters.declare('init_obs_y_loc')
        self.parameters.declare('init_obs_z_loc')
        self.parameters.declare('time_vectors')
        self.parameters.declare('total_num_observers') # NOT OBSERVER GROUPS
        self.parameters.declare('num_nodes', default=1)
    
    def define(self):
        component_name = self.parameters['component_name']
        num_nodes = self.parameters['num_nodes']
        aircraft_location = self.parameters['aircraft_location']
        init_obs_x_loc = self.parameters['init_obs_x_loc']
        init_obs_y_loc = self.parameters['init_obs_y_loc']
        init_obs_z_loc = self.parameters['init_obs_z_loc']
        time_vectors = self.parameters['time_vectors']

        # total number of observers is equal to sum[(size of observer group) * (number of time steps)]
        num_observers =  self.parameters['total_num_observers'] 
        num_observer_groups = len(time_vectors)

        init_obs_x_loc = self.declare_variable('init_obs_x_loc', init_obs_x_loc)
        init_obs_y_loc = self.declare_variable('init_obs_y_loc', init_obs_y_loc)
        init_obs_z_loc = self.declare_variable('init_obs_z_loc', init_obs_z_loc)

        Vx = self.declare_variable('Vx', shape=(num_nodes,), val=1.)
        Vy = self.declare_variable('Vy', shape=(num_nodes,), val=-1.)
        Vz = self.declare_variable('Vz', shape=(num_nodes,), val=0.)

        # aircraft_location = self.declare_variable('aircraft_location', aircraft_location)
        V_aircraft = self.create_output('V_aircraft', shape=(num_nodes, 3))
        V_aircraft[:,0] = csdl.expand(Vx, (num_nodes,1), 'i->ia')
        V_aircraft[:,1] = csdl.expand(Vy, (num_nodes,1), 'i->ia')
        V_aircraft[:,2] = csdl.expand(Vz, (num_nodes,1), 'i->ia')

        V_expanded = csdl.expand(V_aircraft, (num_nodes, 3, num_observers), 'ij->ija')

        # need to compute how the observer location changes relative to aircraft CG
        # we can expand this later to be relative to the rotors
        # print(aircraft_location)
        # aircraft_location = self.declare_variable('aircraft_location', aircraft_location)

        init_aircraft_location = csdl.expand(
            self.declare_variable('aircraft_location', aircraft_location),
            (num_nodes, 3, num_observers), 'ij->aij'
        )

        time = csdl.expand(
            self.declare_variable('time_vectors', time_vectors),
            (num_nodes, 3, num_observers), 'i->abi'
        )

        aircraft_x_pos = self.register_output(
            'aircraft_x_pos',
            init_aircraft_location[:,0,:] + V_expanded[:,0,:]*time[:,0,:]
        )

        aircraft_y_pos = self.register_output(
            'aircraft_y_pos',
            init_aircraft_location[:,1,:] + V_expanded[:,1,:]*time[:,1,:]
        )

        aircraft_z_pos = self.register_output(
            'aircraft_z_pos',
            init_aircraft_location[:,2,:] + V_expanded[:,2,:]*time[:,2,:]
        )

        init_obs_x_loc = csdl.expand(init_obs_x_loc, (num_nodes, 1, num_observers), 'i->abi')
        init_obs_y_loc = csdl.expand(init_obs_y_loc, (num_nodes, 1, num_observers), 'i->abi')
        init_obs_z_loc = csdl.expand(init_obs_z_loc, (num_nodes, 1, num_observers), 'i->abi')

        # ROTOR POSITION RELATIVE TO NOSE OF AIRCRAFT
        rotor_position = csdl.expand(
            self.declare_variable(
                'origin', # NOTE: CHECK AGAIN LATER
                val=0.,
                shape=((3,))
            ),
            shape=(num_nodes, 3, num_observers),
            indices='i->aib'
        ) # HOLDS x, y, z POSITION OF ROTOR RELATIVE TO AIRCRAFT NOSE

        # OBSERVER LOCATIONS RELATIVE TO AIRCRAFT LOCATION
        rel_obs_x_pos = self.register_output('rel_obs_x_pos', init_obs_x_loc - (aircraft_x_pos + rotor_position[:,0,:]))
        rel_obs_y_pos = self.register_output('rel_obs_y_pos', init_obs_y_loc - (aircraft_y_pos + rotor_position[:,1,:]))
        rel_obs_z_pos = self.register_output('rel_obs_z_pos', init_obs_z_loc - (aircraft_z_pos + rotor_position[:,2,:]))

        rel_obs_dist = self.register_output(
            'rel_obs_dist',
            (rel_obs_x_pos**2 + rel_obs_y_pos**2 + rel_obs_z_pos**2)**(0.5),
        )

        rel_obs_angle = self.register_output(
            'rel_obs_angle',
            csdl.arccos(rel_obs_z_pos / rel_obs_dist) *  \
                (rel_obs_z_pos + 1e-12) / ((rel_obs_z_pos + 1e-12)**2)**(0.5)
        ) # CHECK THIS LATER

