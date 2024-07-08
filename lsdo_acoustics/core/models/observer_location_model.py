import csdl_alpha as csdl

def steady_observer_location_model(num_nodes, observer_data, rotor_origin, thrust_vector, velocity):
    '''
    The input observer_data is a dictionary containing keys:
    - original x, y, z position of observers
    - time vectors 
    - total number of observers 
    '''

    # initializing data
    aircraft_location = observer_data['aircraft_position']
    init_obs_x = observer_data['x']
    init_obs_y = observer_data['y']
    init_obs_z = observer_data['z']
    time_vectors = observer_data['time']
    num_observers = observer_data['num_observers']

    # setting target shape for expansions
    target_shape = (num_nodes, 3, num_observers)

    # computing expanded aircraft position
    v_exp = csdl.expand(velocity, target_shape, 'ij->ija')
    init_aircraft_loc_exp = csdl.expand(aircraft_location, target_shape, 'ij->aij')
    if num_observers == 1:
        time = csdl.expand(time_vectors, target_shape)
        init_obs_x_exp = csdl.expand(init_obs_x, target_shape)
        init_obs_y_exp = csdl.expand(init_obs_y, target_shape)
        init_obs_z_exp = csdl.expand(init_obs_z, target_shape)
    else:
        time = csdl.expand(time_vectors, target_shape, 'i->abi')
        init_obs_x_exp = csdl.expand(init_obs_x, target_shape, 'i->abi')
        init_obs_y_exp = csdl.expand(init_obs_y, target_shape, 'i->abi')
        init_obs_z_exp = csdl.expand(init_obs_z, target_shape, 'i->abi')

    aircraft_x_pos = init_aircraft_loc_exp[:,0,:] + v_exp[:,0,:]*time[:,0,:]
    aircraft_y_pos = init_aircraft_loc_exp[:,1,:] + v_exp[:,1,:]*time[:,1,:]
    aircraft_z_pos = init_aircraft_loc_exp[:,2,:] + v_exp[:,2,:]*time[:,2,:]

    # computing observer position relative to rotor thrust origin
    rotor_position = csdl.expand(rotor_origin, target_shape, 'i->aib')

    print(init_obs_x.shape)
    print(aircraft_x_pos.shape)
    print(rotor_position[:,0,:].shape)

    rel_obs_pos_x = init_obs_x.reshape((num_nodes, num_observers)) - (aircraft_x_pos + rotor_position[:,0,:])
    rel_obs_pos_y = init_obs_y.reshape((num_nodes, num_observers)) - (aircraft_y_pos + rotor_position[:,1,:])
    rel_obs_pos_z = init_obs_z.reshape((num_nodes, num_observers)) - (aircraft_z_pos + rotor_position[:,2,:])

    rel_obs_position = csdl.Variable(shape=(num_nodes, 3, num_observers), value=0.)
    rel_obs_position = rel_obs_position.set(csdl.slice[:,0,:], value=rel_obs_pos_x)
    rel_obs_position = rel_obs_position.set(csdl.slice[:,1,:], value=rel_obs_pos_y)
    rel_obs_position = rel_obs_position.set(csdl.slice[:,2,:], value=rel_obs_pos_z)

    rel_obs_dist = csdl.norm(rel_obs_position, axes=(1,))
    # print(rel_obs_dist.value)
    

    thrust_dir_exp = csdl.expand(thrust_vector, target_shape, 'i->aib')
    normal_proj = csdl.sum(rel_obs_position*thrust_dir_exp, axes=(1,))
    rel_angle_plane = csdl.arcsin(normal_proj/rel_obs_dist)
    rel_angle_normal = csdl.arccos(normal_proj/rel_obs_dist)
    # print(normal_proj.value)
    # print(rel_angle_plane.value)
    # print(rel_angle_normal.value)
    # exit()

    return  rel_obs_position, rel_obs_dist, rel_angle_plane, rel_angle_normal