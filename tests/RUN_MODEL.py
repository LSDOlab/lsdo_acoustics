

# RUN_MODEL

# system evaluation block

# op _0009_sparsematmat_eval
# LANG: system_representation_geometry --> _000a
# SHAPES: (16250, 3) --> (1, 3)
# full namespace: system_representation.nonlinear_outputs_model
v05__000a = _0009_sparsematmat_eval_mat@v04_system_representation_geometry

# op _000d_sparsematmat_eval
# LANG: system_representation_geometry --> _000e
# SHAPES: (16250, 3) --> (1, 3)
# full namespace: system_representation.nonlinear_outputs_model
v07__000e = _000d_sparsematmat_eval_mat@v04_system_representation_geometry

# op _000b reshape_eval
# LANG: _000a --> rotor_disk_in_plane_1
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.nonlinear_outputs_model
v06_rotor_disk_in_plane_1 = v05__000a.reshape((1, 3))

# op _000f reshape_eval
# LANG: _000e --> rotor_disk_in_plane_2
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.nonlinear_outputs_model
v08_rotor_disk_in_plane_2 = v07__000e.reshape((1, 3))

# op _003d_power_combination_eval
# LANG: cruise_pitch_angle --> theta
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v046_theta = (v015_cruise_pitch_angle**1)
v046_theta = (v046_theta*_003d_coeff).reshape((1,))

# op _004c cross_product_eval
# LANG: rotor_disk_in_plane_1, rotor_disk_in_plane_2 --> _004d
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((3,))
v08_rotor_disk_in_plane_2 = v08_rotor_disk_in_plane_2.reshape((3,))
v0128__004d = np.cross(v08_rotor_disk_in_plane_2, v06_rotor_disk_in_plane_1, axisa = 0, axisb = 0, axisc = 0)
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((1, 3))
v08_rotor_disk_in_plane_2 = v08_rotor_disk_in_plane_2.reshape((1, 3))

# op _003C_linear_combination_eval
# LANG: theta --> _003D
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v046_theta = v046_theta.reshape((1, 1))
v0111__003D = _003C_constant+1*v046_theta
v046_theta = v046_theta.reshape((1,))

# op _003E_linear_combination_eval
# LANG: theta --> _003F
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v046_theta = v046_theta.reshape((1, 1))
v0113__003F = _003E_constant+1*v046_theta
v046_theta = v046_theta.reshape((1,))

# op _003I_sin_eval
# LANG: theta --> _003J
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v046_theta = v046_theta.reshape((1, 1))
v0114__003J = np.sin(v046_theta)
v046_theta = v046_theta.reshape((1,))

# op _003M_cos_eval
# LANG: theta --> _003N
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v046_theta = v046_theta.reshape((1, 1))
v0116__003N = np.cos(v046_theta)
v046_theta = v046_theta.reshape((1,))

# op _003y_sin_eval
# LANG: theta --> _003z
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v046_theta = v046_theta.reshape((1, 1))
v0109__003z = np.sin(v046_theta)
v046_theta = v046_theta.reshape((1,))

# op _004e pnorm_eval
# LANG: _004d --> _004f
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0130__004f = np.linalg.norm(v0128__004d.flatten(), ord=2)

# op _000L_power_combination_eval
# LANG: cruise_altitude --> _000M
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v081__000M = (v050_cruise_altitude**6)
v081__000M = (v081__000M*_000L_coeff).reshape((1,))

# op _000Y_power_combination_eval
# LANG: cruise_altitude --> _000Z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v084__000Z = (v050_cruise_altitude**5)
v084__000Z = (v084__000Z*_000Y_coeff).reshape((1,))

# op _0019_power_combination_eval
# LANG: cruise_altitude --> _001a
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v086__001a = (v050_cruise_altitude**4)
v086__001a = (v086__001a*_0019_coeff).reshape((1,))

# op _001J_power_combination_eval
# LANG: cruise_altitude --> _001K
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v092__001K = (v050_cruise_altitude**1)
v092__001K = (v092__001K*_001J_coeff).reshape((1,))

# op _001V_power_combination_eval
# LANG: cruise_altitude --> _001W
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v094__001W = (v050_cruise_altitude**0)
v094__001W = (v094__001W*_001V_coeff).reshape((1,))

# op _001l_power_combination_eval
# LANG: cruise_altitude --> _001m
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v088__001m = (v050_cruise_altitude**3)
v088__001m = (v088__001m*_001l_coeff).reshape((1,))

# op _001x_power_combination_eval
# LANG: cruise_altitude --> _001y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v090__001y = (v050_cruise_altitude**2)
v090__001y = (v090__001y*_001x_coeff).reshape((1,))

# op _003A_power_combination_eval
# LANG: _003z --> _003B
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0110__003B = (v0109__003z**1)
v0110__003B = (v0110__003B*_003A_coeff).reshape((1, 1))

# op _003G_power_combination_eval
# LANG: _003D, _003F --> _003H
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0112__003H = (v0111__003D**1)*(v0113__003F**-1)
v0112__003H = (v0112__003H*_003G_coeff).reshape((1, 1))

# op _003K_power_combination_eval
# LANG: _003J --> _003L
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0115__003L = (v0114__003J**1)
v0115__003L = (v0115__003L*_003K_coeff).reshape((1, 1))

# op _003O_power_combination_eval
# LANG: _003N --> _003P
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0117__003P = (v0116__003N**1)
v0117__003P = (v0117__003P*_003O_coeff).reshape((1, 1))

# op _003v_cos_eval
# LANG: theta --> _003w
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v046_theta = v046_theta.reshape((1, 1))
v0107__003w = np.cos(v046_theta)
v046_theta = v046_theta.reshape((1,))

# op _004g expand_scalar_eval
# LANG: _004f --> _004h
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0131__004h = np.empty((3,))
v0131__004h.fill(v0130__004f.item())

# op _00y3_decompose_eval
# LANG: hover_observer_location --> _00y4, _00y5, _00y6
# SHAPES: (3,) --> (1,), (1,), (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0914__00y4 = ((v0912_hover_observer_location.flatten())[src_indices__00y4__00y3]).reshape((1,))
v0915__00y5 = ((v0912_hover_observer_location.flatten())[src_indices__00y5__00y3]).reshape((1,))
v0916__00y6 = ((v0912_hover_observer_location.flatten())[src_indices__00y6__00y3]).reshape((1,))

# op _00zk_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00zl
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((3,))
v01006__00zl = (v06_rotor_disk_in_plane_1**1)
v01006__00zl = (v01006__00zl*_00zk_coeff).reshape((3,))
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((1, 3))

# op _00zn_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _00zo
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v08_rotor_disk_in_plane_2 = v08_rotor_disk_in_plane_2.reshape((3,))
v01010__00zo = (v08_rotor_disk_in_plane_2**1)
v01010__00zo = (v01010__00zo*_00zn_coeff).reshape((3,))
v08_rotor_disk_in_plane_2 = v08_rotor_disk_in_plane_2.reshape((1, 3))

# op _000N_power_combination_eval
# LANG: _000M --> _000O
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v082__000O = (v081__000M**1)
v082__000O = (v082__000O*_000N_coeff).reshape((1,))

# op _000__power_combination_eval
# LANG: _000Z --> _0010
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v085__0010 = (v084__000Z**1)
v085__0010 = (v085__0010*_000__coeff).reshape((1,))

# op _001L_power_combination_eval
# LANG: _001K --> _001M
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v093__001M = (v092__001K**1)
v093__001M = (v093__001M*_001L_coeff).reshape((1,))

# op _001X_power_combination_eval
# LANG: _001W --> _001Y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v095__001Y = (v094__001W**1)
v095__001Y = (v095__001Y*_001X_coeff).reshape((1,))

# op _001b_power_combination_eval
# LANG: _001a --> _001c
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v087__001c = (v086__001a**1)
v087__001c = (v087__001c*_001b_coeff).reshape((1,))

# op _001n_power_combination_eval
# LANG: _001m --> _001o
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v089__001o = (v088__001m**1)
v089__001o = (v089__001o*_001n_coeff).reshape((1,))

# op _001z_power_combination_eval
# LANG: _001y --> _001A
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v091__001A = (v090__001y**1)
v091__001A = (v091__001A*_001z_coeff).reshape((1,))

# op _003x_indexed_passthrough_eval
# LANG: _003w, _003B, _003H, _003L, _003P --> rotation_matrix
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0108_rotation_matrix__temp[i_v0107__003w__003x_indexed_passthrough_eval] = v0107__003w.flatten()
v0108_rotation_matrix = v0108_rotation_matrix__temp.copy()
v0108_rotation_matrix__temp[i_v0110__003B__003x_indexed_passthrough_eval] = v0110__003B.flatten()
v0108_rotation_matrix = v0108_rotation_matrix__temp.copy()
v0108_rotation_matrix__temp[i_v0112__003H__003x_indexed_passthrough_eval] = v0112__003H.flatten()
v0108_rotation_matrix = v0108_rotation_matrix__temp.copy()
v0108_rotation_matrix__temp[i_v0115__003L__003x_indexed_passthrough_eval] = v0115__003L.flatten()
v0108_rotation_matrix = v0108_rotation_matrix__temp.copy()
v0108_rotation_matrix__temp[i_v0117__003P__003x_indexed_passthrough_eval] = v0117__003P.flatten()
v0108_rotation_matrix = v0108_rotation_matrix__temp.copy()

# op _004i_power_combination_eval
# LANG: _004d, _004h --> _004j
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0129__004j = (v0128__004d**1)*(v0131__004h**-1)
v0129__004j = (v0129__004j*_004i_coeff).reshape((3,))

# op _00yp_power_combination_eval
# LANG: _00y4 --> theta
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0926_theta = (v0914__00y4**1)
v0926_theta = (v0926_theta*_00yp_coeff).reshape((1,))

# op _00zw cross_product_eval
# LANG: _00zl, _00zo --> _00zx
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01011__00zx = np.cross(v01010__00zo, v01006__00zl, axisa = 0, axisb = 0, axisc = 0)

# op _000P_indexed_passthrough_eval
# LANG: _000O, _0010, _001c, _001o, _001A, _001M, _001Y --> temp_temperature
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v083_temp_temperature__temp[i_v082__000O__000P_indexed_passthrough_eval] = v082__000O.flatten()
v083_temp_temperature = v083_temp_temperature__temp.copy()
v083_temp_temperature__temp[i_v085__0010__000P_indexed_passthrough_eval] = v085__0010.flatten()
v083_temp_temperature = v083_temp_temperature__temp.copy()
v083_temp_temperature__temp[i_v087__001c__000P_indexed_passthrough_eval] = v087__001c.flatten()
v083_temp_temperature = v083_temp_temperature__temp.copy()
v083_temp_temperature__temp[i_v089__001o__000P_indexed_passthrough_eval] = v089__001o.flatten()
v083_temp_temperature = v083_temp_temperature__temp.copy()
v083_temp_temperature__temp[i_v091__001A__000P_indexed_passthrough_eval] = v091__001A.flatten()
v083_temp_temperature = v083_temp_temperature__temp.copy()
v083_temp_temperature__temp[i_v093__001M__000P_indexed_passthrough_eval] = v093__001M.flatten()
v083_temp_temperature = v083_temp_temperature__temp.copy()
v083_temp_temperature__temp[i_v095__001Y__000P_indexed_passthrough_eval] = v095__001Y.flatten()
v083_temp_temperature = v083_temp_temperature__temp.copy()

# op _004k_matvec_eval
# LANG: rotation_matrix, _004j --> _004l
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0127__004l = v0108_rotation_matrix@v0129__004j

# op _00yK_sin_eval
# LANG: theta --> _00yL
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0926_theta = v0926_theta.reshape((1, 1))
v0989__00yL = np.sin(v0926_theta)
v0926_theta = v0926_theta.reshape((1,))

# op _00yO_linear_combination_eval
# LANG: theta --> _00yP
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0926_theta = v0926_theta.reshape((1, 1))
v0991__00yP = _00yO_constant+1*v0926_theta
v0926_theta = v0926_theta.reshape((1,))

# op _00yQ_linear_combination_eval
# LANG: theta --> _00yR
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0926_theta = v0926_theta.reshape((1, 1))
v0993__00yR = _00yQ_constant+1*v0926_theta
v0926_theta = v0926_theta.reshape((1,))

# op _00yU_sin_eval
# LANG: theta --> _00yV
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0926_theta = v0926_theta.reshape((1, 1))
v0994__00yV = np.sin(v0926_theta)
v0926_theta = v0926_theta.reshape((1,))

# op _00yY_cos_eval
# LANG: theta --> _00yZ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0926_theta = v0926_theta.reshape((1, 1))
v0996__00yZ = np.cos(v0926_theta)
v0926_theta = v0926_theta.reshape((1,))

# op _00zy pnorm_eval
# LANG: _00zx --> _00zz
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01013__00zz = np.linalg.norm(v01011__00zx.flatten(), ord=2)

# op _0022 single_tensor_sum_no_axis_eval
# LANG: temp_temperature --> cruise_temperature
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v096_cruise_temperature = np.sum(v083_temp_temperature).reshape((1,))

# op _002s_decompose_eval
# LANG: cruise_observer_location --> _002t, _0035, _0036
# SHAPES: (3,) --> (1,), (1,), (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v023__002t = ((v016_cruise_observer_location.flatten())[src_indices__002t__002s]).reshape((1,))
v024__0035 = ((v016_cruise_observer_location.flatten())[src_indices__0035__002s]).reshape((1,))
v025__0036 = ((v016_cruise_observer_location.flatten())[src_indices__0036__002s]).reshape((1,))

# op _004m expand_array_eval
# LANG: _004l --> thrust_vector
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0132_thrust_vector = np.einsum('b,a->ab', v0127__004l.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

# op _00yH_cos_eval
# LANG: theta --> _00yI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0926_theta = v0926_theta.reshape((1, 1))
v0987__00yI = np.cos(v0926_theta)
v0926_theta = v0926_theta.reshape((1,))

# op _00yM_power_combination_eval
# LANG: _00yL --> _00yN
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0990__00yN = (v0989__00yL**1)
v0990__00yN = (v0990__00yN*_00yM_coeff).reshape((1, 1))

# op _00yS_power_combination_eval
# LANG: _00yP, _00yR --> _00yT
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0992__00yT = (v0991__00yP**1)*(v0993__00yR**-1)
v0992__00yT = (v0992__00yT*_00yS_coeff).reshape((1, 1))

# op _00yW_power_combination_eval
# LANG: _00yV --> _00yX
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0995__00yX = (v0994__00yV**1)
v0995__00yX = (v0995__00yX*_00yW_coeff).reshape((1, 1))

# op _00y__power_combination_eval
# LANG: _00yZ --> _00z0
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0997__00z0 = (v0996__00yZ**1)
v0997__00z0 = (v0997__00z0*_00y__coeff).reshape((1, 1))

# op _00zA expand_scalar_eval
# LANG: _00zz --> _00zB
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01014__00zB = np.empty((3,))
v01014__00zB.fill(v01013__00zz.item())

# op _002g_power_combination_eval
# LANG: cruise_temperature --> _002h
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0105__002h = (v096_cruise_temperature**1)
v0105__002h = (v0105__002h*_002g_coeff).reshape((1,))

# op _002w_power_combination_eval
# LANG: _002t --> _002x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v026__002x = (v023__002t**1)
v026__002x = (v026__002x*_002w_coeff).reshape((1,))

# op _005Z_decompose_eval
# LANG: thrust_vector --> _005_
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0174__005_ = ((v0132_thrust_vector.flatten())[src_indices__005___005Z]).reshape((1, 3))

# op _00yJ_indexed_passthrough_eval
# LANG: _00yI, _00yN, _00yT, _00yX, _00z0 --> rotation_matrix
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0988_rotation_matrix__temp[i_v0987__00yI__00yJ_indexed_passthrough_eval] = v0987__00yI.flatten()
v0988_rotation_matrix = v0988_rotation_matrix__temp.copy()
v0988_rotation_matrix__temp[i_v0990__00yN__00yJ_indexed_passthrough_eval] = v0990__00yN.flatten()
v0988_rotation_matrix = v0988_rotation_matrix__temp.copy()
v0988_rotation_matrix__temp[i_v0992__00yT__00yJ_indexed_passthrough_eval] = v0992__00yT.flatten()
v0988_rotation_matrix = v0988_rotation_matrix__temp.copy()
v0988_rotation_matrix__temp[i_v0995__00yX__00yJ_indexed_passthrough_eval] = v0995__00yX.flatten()
v0988_rotation_matrix = v0988_rotation_matrix__temp.copy()
v0988_rotation_matrix__temp[i_v0997__00z0__00yJ_indexed_passthrough_eval] = v0997__00z0.flatten()
v0988_rotation_matrix = v0988_rotation_matrix__temp.copy()

# op _00zC_power_combination_eval
# LANG: _00zx, _00zB --> _00zD
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01012__00zD = (v01011__00zx**1)*(v01014__00zB**-1)
v01012__00zD = (v01012__00zD*_00zC_coeff).reshape((3,))

# op _002A_power_combination_eval
# LANG: _002t --> _002B
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v031__002B = (v023__002t**1)
v031__002B = (v031__002B*_002A_coeff).reshape((1,))

# op _002C_linear_combination_eval
# LANG: cruise_pitch_angle, _002x --> _002D
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v022__002D = _002C_constant+1*v015_cruise_pitch_angle+-1*v026__002x

# op _002i_power_combination_eval
# LANG: _002h --> cruise_speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0106_cruise_speed_of_sound = (v0105__002h**0.5)
v0106_cruise_speed_of_sound = (v0106_cruise_speed_of_sound*_002i_coeff).reshape((1,))

# op _002y_power_combination_eval
# LANG: _002t --> _002z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v029__002z = (v023__002t**1)
v029__002z = (v029__002z*_002y_coeff).reshape((1,))

# op _0062_tensor_dot_product_eval
# LANG: projection_vector, _005_ --> _0063
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0181__0063 = np.sum(v0163_projection_vector * v0174__005_, axis=1)

# op _00zE_matvec_eval
# LANG: rotation_matrix, _00zD --> _00zF
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01009__00zF = v0988_rotation_matrix@v01012__00zD

# op _002E_linear_combination_eval
# LANG: _002z, _002B --> _002F
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v030__002F = _002E_constant+1*v029__002z+1*v031__002B

# op _002G_cos_eval
# LANG: _002D --> _002H
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v027__002H = np.cos(v022__002D)

# op _002o_power_combination_eval
# LANG: cruise_mach_number, cruise_speed_of_sound --> cruise_speed
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v020_cruise_speed = (v0106_cruise_speed_of_sound**1)*(v018_cruise_mach_number**1)
v020_cruise_speed = (v020_cruise_speed*_002o_coeff).reshape((1,))

# op _0064 expand_scalar_eval
# LANG: _0063 --> _0065
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0182__0065 = np.empty((1, 3))
v0182__0065.fill(v0181__0063.item())

# op _00zG expand_array_eval
# LANG: _00zF --> thrust_vector
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01015_thrust_vector = np.einsum('b,a->ab', v01009__00zF.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

# op _002I_power_combination_eval
# LANG: cruise_speed, _002H --> _002J
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v021__002J = (v020_cruise_speed**1)*(v027__002H**1)
v021__002J = (v021__002J*_002I_coeff).reshape((1,))

# op _002K_cos_eval
# LANG: _002F --> _002L
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v032__002L = np.cos(v030__002F)

# op _002S_sin_eval
# LANG: _002D --> _002T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v036__002T = np.sin(v022__002D)

# op _0066_power_combination_eval
# LANG: _005_, _0065 --> _0067
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0183__0067 = (v0182__0065**1)*(v0174__005_**1)
v0183__0067 = (v0183__0067*_0066_coeff).reshape((1, 3))

# op _00Bi_decompose_eval
# LANG: thrust_vector --> _00Bj
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01058__00Bj = ((v01015_thrust_vector.flatten())[src_indices__00Bj__00Bi]).reshape((1, 3))

# op _002M_power_combination_eval
# LANG: _002J, _002L --> u
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v028_u = (v021__002J**1)*(v032__002L**1)
v028_u = (v028_u*_002M_coeff).reshape((1,))

# op _002O_sin_eval
# LANG: _002F --> _002P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v034__002P = np.sin(v030__002F)

# op _002U_power_combination_eval
# LANG: cruise_speed, _002T --> _002V
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v035__002V = (v020_cruise_speed**1)*(v036__002T**1)
v035__002V = (v035__002V*_002U_coeff).reshape((1,))

# op _002W_cos_eval
# LANG: _002F --> _002X
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v038__002X = np.cos(v030__002F)

# op _0068_linear_combination_eval
# LANG: projection_vector, _0067 --> _0069
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0180__0069 = _0068_constant+1*v0163_projection_vector+-1*v0183__0067

# op _00Bm_tensor_dot_product_eval
# LANG: projection_vector, _00Bj --> _00Bn
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01065__00Bn = np.sum(v01047_projection_vector * v01058__00Bj, axis=1)

# op _002Q_power_combination_eval
# LANG: cruise_speed, _002P --> v
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v033_v = (v020_cruise_speed**1)*(v034__002P**1)
v033_v = (v033_v*_002Q_coeff).reshape((1,))

# op _002Y_power_combination_eval
# LANG: _002V, _002X --> w
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v037_w = (v035__002V**1)*(v038__002X**1)
v037_w = (v037_w*_002Y_coeff).reshape((1,))

# op _005A_power_combination_eval
# LANG: u --> _005B
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v028_u = v028_u.reshape((1, 1))
v0164__005B = (v028_u**1)
v0164__005B = (v0164__005B*_005A_coeff).reshape((1, 1))
v028_u = v028_u.reshape((1,))

# op _006a pnorm_eval
# LANG: _0069 --> _006b
# SHAPES: (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0185__006b = np.linalg.norm(v0180__0069.flatten(), ord=2)

# op _00Bo expand_scalar_eval
# LANG: _00Bn --> _00Bp
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01066__00Bp = np.empty((1, 3))
v01066__00Bp.fill(v01065__00Bn.item())

# op _006c expand_scalar_eval
# LANG: _006b --> _006d
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0186__006d = np.empty((1, 3))
v0186__006d.fill(v0185__006b.item())

# op _006n_decompose_eval
# LANG: _005B --> _006o
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0165__006o = ((v0164__005B.flatten())[src_indices__006o__006n]).reshape((1, 1))

# op _006q_decompose_eval
# LANG: v --> _006r
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v033_v = v033_v.reshape((1, 1))
v0167__006r = ((v033_v.flatten())[src_indices__006r__006q]).reshape((1, 1))
v033_v = v033_v.reshape((1,))

# op _006s_decompose_eval
# LANG: w --> _006t
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v037_w = v037_w.reshape((1, 1))
v0168__006t = ((v037_w.flatten())[src_indices__006t__006s]).reshape((1, 1))
v037_w = v037_w.reshape((1,))

# op _00Bq_power_combination_eval
# LANG: _00Bj, _00Bp --> _00Br
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01067__00Br = (v01066__00Bp**1)*(v01058__00Bj**1)
v01067__00Br = (v01067__00Br*_00Bq_coeff).reshape((1, 3))

# op _006e_power_combination_eval
# LANG: _0069, _006d --> in_plane_ey
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0184_in_plane_ey = (v0180__0069**1)*(v0186__006d**-1)
v0184_in_plane_ey = (v0184_in_plane_ey*_006e_coeff).reshape((1, 3))

# op _006p_indexed_passthrough_eval
# LANG: _006o, _006r, _006t --> velocity_vector
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0166_velocity_vector__temp[i_v0165__006o__006p_indexed_passthrough_eval] = v0165__006o.flatten()
v0166_velocity_vector = v0166_velocity_vector__temp.copy()
v0166_velocity_vector__temp[i_v0167__006r__006p_indexed_passthrough_eval] = v0167__006r.flatten()
v0166_velocity_vector = v0166_velocity_vector__temp.copy()
v0166_velocity_vector__temp[i_v0168__006t__006p_indexed_passthrough_eval] = v0168__006t.flatten()
v0166_velocity_vector = v0166_velocity_vector__temp.copy()

# op _00Bs_linear_combination_eval
# LANG: projection_vector, _00Br --> _00Bt
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01064__00Bt = _00Bs_constant+1*v01047_projection_vector+-1*v01067__00Br

# op _00y7_power_combination_eval
# LANG: _00y4 --> u
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0917_u = (v0914__00y4**1)
v0917_u = (v0917_u*_00y7_coeff).reshape((1,))

# op _006g cross_product_eval
# LANG: _005_, in_plane_ey --> in_plane_ex
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0179_in_plane_ex = np.cross(v0174__005_, v0184_in_plane_ey, axisa = 1, axisb = 1, axisc = 1)

# op _006u_decompose_eval
# LANG: velocity_vector --> _006v
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0172__006v = ((v0166_velocity_vector.flatten())[src_indices__006v__006u]).reshape((1, 3))

# op _00AU_power_combination_eval
# LANG: u --> _00AV
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0917_u = v0917_u.reshape((1, 1))
v01048__00AV = (v0917_u**1)
v01048__00AV = (v01048__00AV*_00AU_coeff).reshape((1, 1))
v0917_u = v0917_u.reshape((1,))

# op _00Bu pnorm_eval
# LANG: _00Bt --> _00Bv
# SHAPES: (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01069__00Bv = np.linalg.norm(v01064__00Bt.flatten(), ord=2)

# op _00y9_power_combination_eval
# LANG: _00y4 --> v
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0918_v = (v0914__00y4**1)
v0918_v = (v0918_v*_00y9_coeff).reshape((1,))

# op _00yb_power_combination_eval
# LANG: _00y4 --> w
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0919_w = (v0914__00y4**1)
v0919_w = (v0919_w*_00yb_coeff).reshape((1,))

# op _0060_power_combination_eval
# LANG: _005_ --> _0061
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0175__0061 = (v0174__005_**1)
v0175__0061 = (v0175__0061*_0060_coeff).reshape((1, 3))

# op _006w_tensor_dot_product_eval
# LANG: _006v, in_plane_ex --> _006x
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0178__006x = np.sum(v0172__006v * v0179_in_plane_ex, axis=1)

# op _00BH_decompose_eval
# LANG: _00AV --> _00BI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01049__00BI = ((v01048__00AV.flatten())[src_indices__00BI__00BH]).reshape((1, 1))

# op _00BK_decompose_eval
# LANG: v --> _00BL
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0918_v = v0918_v.reshape((1, 1))
v01051__00BL = ((v0918_v.flatten())[src_indices__00BL__00BK]).reshape((1, 1))
v0918_v = v0918_v.reshape((1,))

# op _00BM_decompose_eval
# LANG: w --> _00BN
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0919_w = v0919_w.reshape((1, 1))
v01052__00BN = ((v0919_w.flatten())[src_indices__00BN__00BM]).reshape((1, 1))
v0919_w = v0919_w.reshape((1,))

# op _00Bw expand_scalar_eval
# LANG: _00Bv --> _00Bx
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01070__00Bx = np.empty((1, 3))
v01070__00Bx.fill(v01069__00Bv.item())

# op _0048 pnorm_eval
# LANG: rotor_disk_in_plane_1 --> _0049
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((3,))
v0125__0049 = np.linalg.norm(v06_rotor_disk_in_plane_1.flatten(), ord=2)
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((1, 3))

# op _006A_tensor_dot_product_eval
# LANG: _006v, _0061 --> _006B
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0173__006B = np.sum(v0172__006v * v0175__0061, axis=1)

# op _006F_linear_combination_eval
# LANG: _006x --> _006G
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0187__006G = _006F_constant+-1*v0178__006x

# op _006y_tensor_dot_product_eval
# LANG: _006v, in_plane_ey --> _006z
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0189__006z = np.sum(v0172__006v * v0184_in_plane_ey, axis=1)

# op _00BJ_indexed_passthrough_eval
# LANG: _00BI, _00BL, _00BN --> velocity_vector
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01050_velocity_vector__temp[i_v01049__00BI__00BJ_indexed_passthrough_eval] = v01049__00BI.flatten()
v01050_velocity_vector = v01050_velocity_vector__temp.copy()
v01050_velocity_vector__temp[i_v01051__00BL__00BJ_indexed_passthrough_eval] = v01051__00BL.flatten()
v01050_velocity_vector = v01050_velocity_vector__temp.copy()
v01050_velocity_vector__temp[i_v01052__00BN__00BJ_indexed_passthrough_eval] = v01052__00BN.flatten()
v01050_velocity_vector = v01050_velocity_vector__temp.copy()

# op _00By_power_combination_eval
# LANG: _00Bt, _00Bx --> in_plane_ey
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01068_in_plane_ey = (v01064__00Bt**1)*(v01070__00Bx**-1)
v01068_in_plane_ey = (v01068_in_plane_ey*_00By_coeff).reshape((1, 3))

# op _004a_power_combination_eval
# LANG: _0049 --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0126_propeller_radius = (v0125__0049**1)
v0126_propeller_radius = (v0126_propeller_radius*_004a_coeff).reshape((1,))

# op _006C expand_scalar_eval
# LANG: _006B --> _006D
# SHAPES: (1,) --> (1, 40, 100, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0176__006D = np.empty((1, 40, 100, 1))
v0176__006D.fill(v0173__006B.item())

# op _006H expand_scalar_eval
# LANG: _006G --> _006I
# SHAPES: (1,) --> (1, 40, 100, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0188__006I = np.empty((1, 40, 100, 1))
v0188__006I.fill(v0187__006G.item())

# op _006J expand_scalar_eval
# LANG: _006z --> _006K
# SHAPES: (1,) --> (1, 40, 100, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0190__006K = np.empty((1, 40, 100, 1))
v0190__006K.fill(v0189__006z.item())

# op _00BA cross_product_eval
# LANG: _00Bj, in_plane_ey --> in_plane_ex
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01063_in_plane_ex = np.cross(v01058__00Bj, v01068_in_plane_ey, axisa = 1, axisb = 1, axisc = 1)

# op _00BO_decompose_eval
# LANG: velocity_vector --> _00BP
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01056__00BP = ((v01050_velocity_vector.flatten())[src_indices__00BP__00BO]).reshape((1, 3))

# op _005P_power_combination_eval
# LANG: propeller_radius --> hub_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0191_hub_radius = (v0126_propeller_radius**1)
v0191_hub_radius = (v0191_hub_radius*_005P_coeff).reshape((1,))

# op _006E_indexed_passthrough_eval
# LANG: _006D, _006I, _006K --> inflow_velocity
# SHAPES: (1, 40, 100, 1), (1, 40, 100, 1), (1, 40, 100, 1) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0177_inflow_velocity__temp[i_v0176__006D__006E_indexed_passthrough_eval] = v0176__006D.flatten()
v0177_inflow_velocity = v0177_inflow_velocity__temp.copy()
v0177_inflow_velocity__temp[i_v0188__006I__006E_indexed_passthrough_eval] = v0188__006I.flatten()
v0177_inflow_velocity = v0177_inflow_velocity__temp.copy()
v0177_inflow_velocity__temp[i_v0190__006K__006E_indexed_passthrough_eval] = v0190__006K.flatten()
v0177_inflow_velocity = v0177_inflow_velocity__temp.copy()

# op _006i_decompose_eval
# LANG: rpm --> _006j
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0195__006j = ((v0162_rpm.flatten())[src_indices__006j__006i]).reshape((1, 1))

# op _0088_power_combination_eval
# LANG: z --> _0089
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0235__0089 = (v0234_z**1)
v0235__0089 = (v0235__0089*_0088_coeff).reshape((1, 1))

# op _00BQ_tensor_dot_product_eval
# LANG: _00BP, in_plane_ex --> _00BR
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01062__00BR = np.sum(v01056__00BP * v01063_in_plane_ex, axis=1)

# op _00Bk_power_combination_eval
# LANG: _00Bj --> _00Bl
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01059__00Bl = (v01058__00Bj**1)
v01059__00Bl = (v01059__00Bl*_00Bk_coeff).reshape((1, 3))

# op _006Z expand_scalar_eval
# LANG: hub_radius --> _hub_radius
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0201__hub_radius = np.empty((1, 40, 100))
v0201__hub_radius.fill(v0191_hub_radius.item())

# op _006k_power_combination_eval
# LANG: _006j --> _006l
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0196__006l = (v0195__006j**1)
v0196__006l = (v0196__006l*_006k_coeff).reshape((1, 1))

# op _0070 expand_scalar_eval
# LANG: propeller_radius --> _rotor_radius
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0202__rotor_radius = np.empty((1, 40, 100))
v0202__rotor_radius.fill(v0126_propeller_radius.item())

# op _0078 expand_array_eval
# LANG: y_dir --> _y_dir
# SHAPES: (1, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0206__y_dir = np.einsum('ad,bc->abcd', v0199_y_dir.reshape((1, 3)) ,np.ones((40, 100))).reshape((1, 40, 100, 3))

# op _007a expand_array_eval
# LANG: z_dir --> _z_dir
# SHAPES: (1, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0207__z_dir = np.einsum('ad,bc->abcd', v0200_z_dir.reshape((1, 3)) ,np.ones((40, 100))).reshape((1, 40, 100, 3))

# op _007c_power_combination_eval
# LANG: inflow_velocity --> _inflow_velocity
# SHAPES: (1, 40, 100, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0208__inflow_velocity = (v0177_inflow_velocity**1)
v0208__inflow_velocity = (v0208__inflow_velocity*_007c_coeff).reshape((1, 40, 100, 3))

# op _008a_linear_combination_eval
# LANG: _0089 --> _008b
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0236__008b = _008a_constant+-1*v0235__0089

# op _00BS_tensor_dot_product_eval
# LANG: _00BP, in_plane_ey --> _00BT
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01073__00BT = np.sum(v01056__00BP * v01068_in_plane_ey, axis=1)

# op _00BU_tensor_dot_product_eval
# LANG: _00BP, _00Bl --> _00BV
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01057__00BV = np.sum(v01056__00BP * v01059__00Bl, axis=1)

# op _00BZ_linear_combination_eval
# LANG: _00BR --> _00B_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01071__00B_ = _00BZ_constant+-1*v01062__00BR

# op _00zs pnorm_eval
# LANG: _00zl --> _00zt
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01007__00zt = np.linalg.norm(v01006__00zl.flatten(), ord=2)

# op _006m_indexed_passthrough_eval
# LANG: _006l --> rotational_speed
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0197_rotational_speed__temp[i_v0196__006l__006m_indexed_passthrough_eval] = v0196__006l.flatten()
v0197_rotational_speed = v0197_rotational_speed__temp.copy()

# op _007M_tensor_dot_product_eval
# LANG: _y_dir, _inflow_velocity --> _in_plane_inflow_velocity
# SHAPES: (1, 40, 100, 3), (1, 40, 100, 3) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0223__in_plane_inflow_velocity = np.sum(v0208__inflow_velocity * v0206__y_dir, axis=3)

# op _007O_tensor_dot_product_eval
# LANG: _z_dir, _inflow_velocity --> inflow_z
# SHAPES: (1, 40, 100, 3), (1, 40, 100, 3) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0224_inflow_z = np.sum(v0208__inflow_velocity * v0207__z_dir, axis=3)

# op _007w_linear_combination_eval
# LANG: _hub_radius, _rotor_radius --> _007x
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0216__007x = _007w_constant+1*v0202__rotor_radius+-1*v0201__hub_radius

# op _008c_power_combination_eval
# LANG: _008b --> _008d
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0237__008d = (v0236__008b**1)
v0237__008d = (v0237__008d*_008c_coeff).reshape((1, 1))

# op _00BW expand_scalar_eval
# LANG: _00BV --> _00BX
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01060__00BX = np.empty((1, 40, 30, 1))
v01060__00BX.fill(v01057__00BV.item())

# op _00C0 expand_scalar_eval
# LANG: _00B_ --> _00C1
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01072__00C1 = np.empty((1, 40, 30, 1))
v01072__00C1.fill(v01071__00B_.item())

# op _00C2 expand_scalar_eval
# LANG: _00BT --> _00C3
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01074__00C3 = np.empty((1, 40, 30, 1))
v01074__00C3.fill(v01073__00BT.item())

# op _00zu_power_combination_eval
# LANG: _00zt --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01008_propeller_radius = (v01007__00zt**1)
v01008_propeller_radius = (v01008_propeller_radius*_00zu_coeff).reshape((1,))

# op _0074 expand_scalar_eval
# LANG: rotational_speed --> _rotational_speed
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0197_rotational_speed = v0197_rotational_speed.reshape((1,))
v0204__rotational_speed = np.empty((1, 40, 100))
v0204__rotational_speed.fill(v0197_rotational_speed.item())
v0197_rotational_speed = v0197_rotational_speed.reshape((1, 1))

# op _007Q_power_combination_eval
# LANG: inflow_z --> _007R
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0225__007R = (v0224_inflow_z**1)
v0225__007R = (v0225__007R*_007Q_coeff).reshape((1, 40, 100))

# op _007S_cos_eval
# LANG: _theta --> _007T
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0227__007T = np.cos(v0212__theta)

# op _007W_power_combination_eval
# LANG: _in_plane_inflow_velocity --> _007X
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0229__007X = (v0223__in_plane_inflow_velocity**1)
v0229__007X = (v0229__007X*_007W_coeff).reshape((1, 40, 100))

# op _007Y_sin_eval
# LANG: _theta --> _007Z
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0231__007Z = np.sin(v0212__theta)

# op _007y_power_combination_eval
# LANG: _007x, _normalized_radius --> _007z
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0217__007z = (v0216__007x**1)*(v0213__normalized_radius**1)
v0217__007z = (v0217__007z*_007y_coeff).reshape((1, 40, 100))

# op _008e_linear_combination_eval
# LANG: _008d --> temperature
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0238_temperature = _008e_constant+1*v0237__008d

# op _00B8_power_combination_eval
# LANG: propeller_radius --> hub_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01075_hub_radius = (v01008_propeller_radius**1)
v01075_hub_radius = (v01075_hub_radius*_00B8_coeff).reshape((1,))

# op _00BC_decompose_eval
# LANG: rpm --> _00BD
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01079__00BD = ((v01046_rpm.flatten())[src_indices__00BD__00BC]).reshape((1, 1))

# op _00BY_indexed_passthrough_eval
# LANG: _00BX, _00C1, _00C3 --> inflow_velocity
# SHAPES: (1, 40, 30, 1), (1, 40, 30, 1), (1, 40, 30, 1) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01061_inflow_velocity__temp[i_v01060__00BX__00BY_indexed_passthrough_eval] = v01060__00BX.flatten()
v01061_inflow_velocity = v01061_inflow_velocity__temp.copy()
v01061_inflow_velocity__temp[i_v01072__00C1__00BY_indexed_passthrough_eval] = v01072__00C1.flatten()
v01061_inflow_velocity = v01061_inflow_velocity__temp.copy()
v01061_inflow_velocity__temp[i_v01074__00C3__00BY_indexed_passthrough_eval] = v01074__00C3.flatten()
v01061_inflow_velocity = v01061_inflow_velocity__temp.copy()

# op _00Ds_power_combination_eval
# LANG: z --> _00Dt
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01119__00Dt = (v01118_z**1)
v01119__00Dt = (v01119__00Dt*_00Ds_coeff).reshape((1, 1))

# op _000l_sparsematmat_eval
# LANG: system_representation_geometry --> _000m
# SHAPES: (16250, 3) --> (40, 3)
# full namespace: system_representation.nonlinear_outputs_model
v011__000m = _000l_sparsematmat_eval_mat@v04_system_representation_geometry

# op _007A_linear_combination_eval
# LANG: _007z, _hub_radius --> _radius
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0215__radius = _007A_constant+1*v0201__hub_radius+1*v0217__007z

# op _007U_power_combination_eval
# LANG: _007R, _007T --> _007V
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0226__007V = (v0225__007R**1)*(v0227__007T**1)
v0226__007V = (v0226__007V*_007U_coeff).reshape((1, 40, 100))

# op _007__power_combination_eval
# LANG: _007X, _007Z --> _0080
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0230__0080 = (v0229__007X**1)*(v0231__007Z**1)
v0230__0080 = (v0230__0080*_007__coeff).reshape((1, 40, 100))

# op _007u_power_combination_eval
# LANG: _rotational_speed --> _angular_speed
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0214__angular_speed = (v0204__rotational_speed**1)
v0214__angular_speed = (v0214__angular_speed*_007u_coeff).reshape((1, 40, 100))

# op _008g_power_combination_eval
# LANG: temperature --> _008h
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0239__008h = (v0238_temperature**1)
v0239__008h = (v0239__008h*_008g_coeff).reshape((1, 1))

# op _00BE_power_combination_eval
# LANG: _00BD --> _00BF
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01080__00BF = (v01079__00BD**1)
v01080__00BF = (v01080__00BF*_00BE_coeff).reshape((1, 1))

# op _00Ci expand_scalar_eval
# LANG: hub_radius --> _hub_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01085__hub_radius = np.empty((1, 40, 30))
v01085__hub_radius.fill(v01075_hub_radius.item())

# op _00Ck expand_scalar_eval
# LANG: propeller_radius --> _rotor_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01086__rotor_radius = np.empty((1, 40, 30))
v01086__rotor_radius.fill(v01008_propeller_radius.item())

# op _00Cs expand_array_eval
# LANG: y_dir --> _y_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01090__y_dir = np.einsum('ad,bc->abcd', v01083_y_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _00Cu expand_array_eval
# LANG: z_dir --> _z_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01091__z_dir = np.einsum('ad,bc->abcd', v01084_z_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _00Cw_power_combination_eval
# LANG: inflow_velocity --> _inflow_velocity
# SHAPES: (1, 40, 30, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01092__inflow_velocity = (v01061_inflow_velocity**1)
v01092__inflow_velocity = (v01092__inflow_velocity*_00Cw_coeff).reshape((1, 40, 30, 3))

# op _00Du_linear_combination_eval
# LANG: _00Dt --> _00Dv
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01120__00Dv = _00Du_constant+-1*v01119__00Dt

# op _000n reshape_eval
# LANG: _000m --> rotor_blade_chord_length
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.nonlinear_outputs_model
v012_rotor_blade_chord_length = v011__000m.reshape((40, 3))

# op _000p_sparsematmat_eval
# LANG: system_representation_geometry --> _000q
# SHAPES: (16250, 3) --> (40, 3)
# full namespace: system_representation.nonlinear_outputs_model
v013__000q = _000p_sparsematmat_eval_mat@v04_system_representation_geometry

# op _0076 expand_array_eval
# LANG: x_dir --> _x_dir
# SHAPES: (1, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0205__x_dir = np.einsum('ad,bc->abcd', v0198_x_dir.reshape((1, 3)) ,np.ones((40, 100))).reshape((1, 40, 100, 3))

# op _0081_linear_combination_eval
# LANG: _007V, _0080 --> _0082
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0228__0082 = _0081_constant+1*v0226__007V+1*v0230__0080

# op _0083_power_combination_eval
# LANG: _angular_speed, _radius --> _0084
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0233__0084 = (v0215__radius**1)*(v0214__angular_speed**1)
v0233__0084 = (v0233__0084*_0083_coeff).reshape((1, 40, 100))

# op _008i_power_combination_eval
# LANG: _008h --> _008j
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0240__008j = (v0239__008h**5.258643795229161)
v0240__008j = (v0240__008j*_008i_coeff).reshape((1, 1))

# op _00BG_indexed_passthrough_eval
# LANG: _00BF --> rotational_speed
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01081_rotational_speed__temp[i_v01080__00BF__00BG_indexed_passthrough_eval] = v01080__00BF.flatten()
v01081_rotational_speed = v01081_rotational_speed__temp.copy()

# op _00CQ_linear_combination_eval
# LANG: _hub_radius, _rotor_radius --> _00CR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01100__00CR = _00CQ_constant+1*v01086__rotor_radius+-1*v01085__hub_radius

# op _00D5_tensor_dot_product_eval
# LANG: _y_dir, _inflow_velocity --> _in_plane_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01107__in_plane_inflow_velocity = np.sum(v01092__inflow_velocity * v01090__y_dir, axis=3)

# op _00D7_tensor_dot_product_eval
# LANG: _z_dir, _inflow_velocity --> inflow_z
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01108_inflow_z = np.sum(v01092__inflow_velocity * v01091__z_dir, axis=3)

# op _00Dw_power_combination_eval
# LANG: _00Dv --> _00Dx
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01121__00Dx = (v01120__00Dv**1)
v01121__00Dx = (v01121__00Dx*_00Dw_coeff).reshape((1, 1))

# op _000r reshape_eval
# LANG: _000q --> rotor_blade_twist
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.nonlinear_outputs_model
v014_rotor_blade_twist = v013__000q.reshape((40, 3))

# op _003R pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _003S
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0118__003S = np.sum(v012_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _007K_tensor_dot_product_eval
# LANG: _x_dir, _inflow_velocity --> _axial_inflow_velocity
# SHAPES: (1, 40, 100, 3), (1, 40, 100, 3) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0222__axial_inflow_velocity = np.sum(v0208__inflow_velocity * v0205__x_dir, axis=3)

# op _0085_linear_combination_eval
# LANG: _0082, _0084 --> _tangential_inflow_velocity
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0232__tangential_inflow_velocity = _0085_constant+1*v0228__0082+1*v0233__0084

# op _008k_power_combination_eval
# LANG: _008j --> pressure
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0241_pressure = (v0240__008j**1)
v0241_pressure = (v0241_pressure*_008k_coeff).reshape((1, 1))

# op _008q_power_combination_eval
# LANG: temperature --> _008r
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0244__008r = (v0238_temperature**1)
v0244__008r = (v0244__008r*_008q_coeff).reshape((1, 1))

# op _00CS_power_combination_eval
# LANG: _00CR, _normalized_radius --> _00CT
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01101__00CT = (v01100__00CR**1)*(v01097__normalized_radius**1)
v01101__00CT = (v01101__00CT*_00CS_coeff).reshape((1, 40, 30))

# op _00Co expand_scalar_eval
# LANG: rotational_speed --> _rotational_speed
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01081_rotational_speed = v01081_rotational_speed.reshape((1,))
v01088__rotational_speed = np.empty((1, 40, 30))
v01088__rotational_speed.fill(v01081_rotational_speed.item())
v01081_rotational_speed = v01081_rotational_speed.reshape((1, 1))

# op _00D9_power_combination_eval
# LANG: inflow_z --> _00Da
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01109__00Da = (v01108_inflow_z**1)
v01109__00Da = (v01109__00Da*_00D9_coeff).reshape((1, 40, 30))

# op _00Db_cos_eval
# LANG: _theta --> _00Dc
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01111__00Dc = np.cos(v01096__theta)

# op _00Df_power_combination_eval
# LANG: _in_plane_inflow_velocity --> _00Dg
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01113__00Dg = (v01107__in_plane_inflow_velocity**1)
v01113__00Dg = (v01113__00Dg*_00Df_coeff).reshape((1, 40, 30))

# op _00Dh_sin_eval
# LANG: _theta --> _00Di
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01115__00Di = np.sin(v01096__theta)

# op _00Dy_linear_combination_eval
# LANG: _00Dx --> temperature
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01122_temperature = _00Dy_constant+1*v01121__00Dx

# op _003T reshape_eval
# LANG: _003S --> chord_profile
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0119_chord_profile = v0118__003S.reshape((40, 1))

# op _003W_single_tensor_sum_with_axis_eval
# LANG: rotor_blade_twist --> _003X
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0120__003X = np.sum(v014_rotor_blade_twist, axis = (1,)).reshape((40,))

# op _004x_power_combination_eval
# LANG: _axial_inflow_velocity --> _004y
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0136__004y = (v0222__axial_inflow_velocity**2)
v0136__004y = (v0136__004y*_004x_coeff).reshape((1, 40, 100))

# op _004z_power_combination_eval
# LANG: _tangential_inflow_velocity --> _004A
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0138__004A = (v0232__tangential_inflow_velocity**2)
v0138__004A = (v0138__004A*_004z_coeff).reshape((1, 40, 100))

# op _008m_power_combination_eval
# LANG: pressure --> _008n
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0242__008n = (v0241_pressure**1)
v0242__008n = (v0242__008n*_008m_coeff).reshape((1, 1))

# op _008s_power_combination_eval
# LANG: _008r --> _008t
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0245__008t = (v0244__008r**1.5)
v0245__008t = (v0245__008t*_008s_coeff).reshape((1, 1))

# op _00CO_power_combination_eval
# LANG: _rotational_speed --> _angular_speed
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01098__angular_speed = (v01088__rotational_speed**1)
v01098__angular_speed = (v01098__angular_speed*_00CO_coeff).reshape((1, 40, 30))

# op _00CU_linear_combination_eval
# LANG: _00CT, _hub_radius --> _radius
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01099__radius = _00CU_constant+1*v01085__hub_radius+1*v01101__00CT

# op _00DA_power_combination_eval
# LANG: temperature --> _00DB
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01123__00DB = (v01122_temperature**1)
v01123__00DB = (v01123__00DB*_00DA_coeff).reshape((1, 1))

# op _00Dd_power_combination_eval
# LANG: _00Da, _00Dc --> _00De
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01110__00De = (v01109__00Da**1)*(v01111__00Dc**1)
v01110__00De = (v01110__00De*_00Dd_coeff).reshape((1, 40, 30))

# op _00Dj_power_combination_eval
# LANG: _00Dg, _00Di --> _00Dk
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01114__00Dk = (v01113__00Dg**1)*(v01115__00Di**1)
v01114__00Dk = (v01114__00Dk*_00Dj_coeff).reshape((1, 40, 30))

# op _003Y reshape_eval
# LANG: _003X --> _003Z
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0121__003Z = v0120__003X.reshape((40, 1))

# op _004B_linear_combination_eval
# LANG: _004y, _004A --> _004C
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0137__004C = _004B_constant+1*v0136__004y+1*v0138__004A

# op _007g expand_array_eval
# LANG: chord_profile --> _chord
# SHAPES: (40,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0119_chord_profile = v0119_chord_profile.reshape((40,))
v0210__chord = np.einsum('b,ac->abc', v0119_chord_profile.reshape((40,)) ,np.ones((1, 100))).reshape((1, 40, 100))
v0119_chord_profile = v0119_chord_profile.reshape((40, 1))

# op _008o_power_combination_eval
# LANG: temperature, _008n --> density
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0243_density = (v0242__008n**1)*(v0238_temperature**-1)
v0243_density = (v0243_density*_008o_coeff).reshape((1, 1))

# op _008u_power_combination_eval
# LANG: _008t --> _008v
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0246__008v = (v0245__008t**1)
v0246__008v = (v0246__008v*_008u_coeff).reshape((1, 1))

# op _00Cq expand_array_eval
# LANG: x_dir --> _x_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01089__x_dir = np.einsum('ad,bc->abcd', v01082_x_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _00DC_power_combination_eval
# LANG: _00DB --> _00DD
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01124__00DD = (v01123__00DB**5.258643795229161)
v01124__00DD = (v01124__00DD*_00DC_coeff).reshape((1, 1))

# op _00Dl_linear_combination_eval
# LANG: _00De, _00Dk --> _00Dm
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01112__00Dm = _00Dl_constant+1*v01110__00De+1*v01114__00Dk

# op _00Dn_power_combination_eval
# LANG: _angular_speed, _radius --> _00Do
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01117__00Do = (v01099__radius**1)*(v01098__angular_speed**1)
v01117__00Do = (v01117__00Do*_00Dn_coeff).reshape((1, 40, 30))

# op _00z2 pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00z3
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0998__00z3 = np.sum(v012_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _003__power_combination_eval
# LANG: chord_profile, _003Z --> _0040
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0122__0040 = (v0121__003Z**1)*(v0119_chord_profile**-1)
v0122__0040 = (v0122__0040*_003__coeff).reshape((40, 1))

# op _004D_power_combination_eval
# LANG: _004C --> _004E
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0139__004E = (v0137__004C**0.5)
v0139__004E = (v0139__004E*_004D_coeff).reshape((1, 40, 100))

# op _004G expand_scalar_eval
# LANG: density --> _004H
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0243_density = v0243_density.reshape((1,))
v0134__004H = np.empty((1, 40, 100))
v0134__004H.fill(v0243_density.item())
v0243_density = v0243_density.reshape((1, 1))

# op _007C_power_combination_eval
# LANG: _chord --> _007D
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0218__007D = (v0210__chord**1)
v0218__007D = (v0218__007D*_007C_coeff).reshape((1, 40, 100))

# op _008w_power_combination_eval
# LANG: _008v --> _008x
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0247__008x = (v0246__008v**1)
v0247__008x = (v0247__008x*_008w_coeff).reshape((1, 1))

# op _008y_linear_combination_eval
# LANG: temperature --> _008z
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0249__008z = _008y_constant+1*v0238_temperature

# op _00D3_tensor_dot_product_eval
# LANG: _x_dir, _inflow_velocity --> _axial_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01106__axial_inflow_velocity = np.sum(v01092__inflow_velocity * v01089__x_dir, axis=3)

# op _00DE_power_combination_eval
# LANG: _00DD --> pressure
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01125_pressure = (v01124__00DD**1)
v01125_pressure = (v01125_pressure*_00DE_coeff).reshape((1, 1))

# op _00DK_power_combination_eval
# LANG: temperature --> _00DL
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01128__00DL = (v01122_temperature**1)
v01128__00DL = (v01128__00DL*_00DK_coeff).reshape((1, 1))

# op _00Dp_linear_combination_eval
# LANG: _00Dm, _00Do --> _tangential_inflow_velocity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01116__tangential_inflow_velocity = _00Dp_constant+1*v01112__00Dm+1*v01117__00Do

# op _00z4 reshape_eval
# LANG: _00z3 --> _00z5
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0999__00z5 = v0998__00z3.reshape((40, 1))

# op _0041_arcsin_eval
# LANG: _0040 --> _0042
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0123__0042 = np.arcsin(v0122__0040)

# op _004O_power_combination_eval
# LANG: _004H, _004E --> _004P
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0135__004P = (v0134__004H**1)*(v0139__004E**1)
v0135__004P = (v0135__004P*_004O_coeff).reshape((1, 40, 100))

# op _007E_power_combination_eval
# LANG: _007D --> _007F
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0219__007F = (v0218__007D**1)
v0219__007F = (v0219__007F*_007E_coeff).reshape((1, 40, 100))

# op _008A_power_combination_eval
# LANG: _008x, _008z --> dynamic_viscosity
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0248_dynamic_viscosity = (v0247__008x**1)*(v0249__008z**-1)
v0248_dynamic_viscosity = (v0248_dynamic_viscosity*_008A_coeff).reshape((1, 1))

# op _00DG_power_combination_eval
# LANG: pressure --> _00DH
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01126__00DH = (v01125_pressure**1)
v01126__00DH = (v01126__00DH*_00DG_coeff).reshape((1, 1))

# op _00DM_power_combination_eval
# LANG: _00DL --> _00DN
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01129__00DN = (v01128__00DL**1.5)
v01129__00DN = (v01129__00DN*_00DM_coeff).reshape((1, 1))

# op _00z6_power_combination_eval
# LANG: _00z5 --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01000_chord_profile = (v0999__00z5**1)
v01000_chord_profile = (v01000_chord_profile*_00z6_coeff).reshape((40, 1))

# op _00z9_single_tensor_sum_with_axis_eval
# LANG: rotor_blade_twist --> _00za
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01001__00za = np.sum(v014_rotor_blade_twist, axis = (1,)).reshape((40,))

# op _00zR_power_combination_eval
# LANG: _axial_inflow_velocity --> _00zS
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01020__00zS = (v01106__axial_inflow_velocity**2)
v01020__00zS = (v01020__00zS*_00zR_coeff).reshape((1, 40, 30))

# op _00zT_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00zU
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01022__00zU = (v01116__tangential_inflow_velocity**2)
v01022__00zU = (v01022__00zU*_00zT_coeff).reshape((1, 40, 30))

# op _0043_linear_combination_eval
# LANG: _0042 --> twist_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0124_twist_profile = _0043_constant+1*v0123__0042

# op _004J expand_scalar_eval
# LANG: dynamic_viscosity --> _004K
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0248_dynamic_viscosity = v0248_dynamic_viscosity.reshape((1,))
v0142__004K = np.empty((1, 40, 100))
v0142__004K.fill(v0248_dynamic_viscosity.item())
v0248_dynamic_viscosity = v0248_dynamic_viscosity.reshape((1, 1))

# op _004Q_power_combination_eval
# LANG: _004P, _chord --> _004R
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0140__004R = (v0135__004P**1)*(v0210__chord**1)
v0140__004R = (v0140__004R*_004Q_coeff).reshape((1, 40, 100))

# op _007G_power_combination_eval
# LANG: _007F --> _007H
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0220__007H = (v0219__007F**1)
v0220__007H = (v0220__007H*_007G_coeff).reshape((1, 40, 100))

# op _00CA expand_array_eval
# LANG: chord_profile --> _chord
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01000_chord_profile = v01000_chord_profile.reshape((40,))
v01094__chord = np.einsum('b,ac->abc', v01000_chord_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v01000_chord_profile = v01000_chord_profile.reshape((40, 1))

# op _00DI_power_combination_eval
# LANG: temperature, _00DH --> density
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01127_density = (v01126__00DH**1)*(v01122_temperature**-1)
v01127_density = (v01127_density*_00DI_coeff).reshape((1, 1))

# op _00DO_power_combination_eval
# LANG: _00DN --> _00DP
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01130__00DP = (v01129__00DN**1)
v01130__00DP = (v01130__00DP*_00DO_coeff).reshape((1, 1))

# op _00zV_linear_combination_eval
# LANG: _00zS, _00zU --> _00zW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01021__00zW = _00zV_constant+1*v01020__00zS+1*v01022__00zU

# op _00zb reshape_eval
# LANG: _00za --> _00zc
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01002__00zc = v01001__00za.reshape((40, 1))

# op _004S_power_combination_eval
# LANG: _004R, _004K --> Re
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0141_Re = (v0140__004R**1)*(v0142__004K**-1)
v0141_Re = (v0141_Re*_004S_coeff).reshape((1, 40, 100))

# op _007I_power_combination_eval
# LANG: _radius, _007H --> _blade_solidity
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0221__blade_solidity = (v0220__007H**1)*(v0215__radius**-1)
v0221__blade_solidity = (v0221__blade_solidity*_007I_coeff).reshape((1, 40, 100))

# op _007e expand_array_eval
# LANG: twist_profile --> _pitch
# SHAPES: (40,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0124_twist_profile = v0124_twist_profile.reshape((40,))
v0209__pitch = np.einsum('b,ac->abc', v0124_twist_profile.reshape((40,)) ,np.ones((1, 100))).reshape((1, 40, 100))
v0124_twist_profile = v0124_twist_profile.reshape((40, 1))

# op _00CW_power_combination_eval
# LANG: _chord --> _00CX
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01102__00CX = (v01094__chord**1)
v01102__00CX = (v01102__00CX*_00CW_coeff).reshape((1, 40, 30))

# op _00DQ_power_combination_eval
# LANG: _00DP --> _00DR
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01131__00DR = (v01130__00DP**1)
v01131__00DR = (v01131__00DR*_00DQ_coeff).reshape((1, 1))

# op _00DS_linear_combination_eval
# LANG: temperature --> _00DT
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01133__00DT = _00DS_constant+1*v01122_temperature

# op _00zX_power_combination_eval
# LANG: _00zW --> _00zY
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01023__00zY = (v01021__00zW**0.5)
v01023__00zY = (v01023__00zY*_00zX_coeff).reshape((1, 40, 30))

# op _00z_ expand_scalar_eval
# LANG: density --> _00A0
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01127_density = v01127_density.reshape((1,))
v01018__00A0 = np.empty((1, 40, 30))
v01018__00A0.fill(v01127_density.item())
v01127_density = v01127_density.reshape((1, 1))

# op _00zd_power_combination_eval
# LANG: _00z5, _00zc --> _00ze
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01003__00ze = (v01002__00zc**1)*(v0999__00z5**-1)
v01003__00ze = (v01003__00ze*_00zd_coeff).reshape((40, 1))

# op _00as_bracketed_implict_eval
# LANG: Re, _hub_radius, _rotor_radius, _pitch, _chord, _radius, _blade_solidity, _axial_inflow_velocity, _tangential_inflow_velocity --> phi_distribution, alpha_distribution, Cl, Cd
# SHAPES: (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100) --> (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.phi_bracketed_search_group
_00as_bracketed.set_guess(initial_guess_v0252_phi_distribution)
_00as_bracketed_out = _00as_bracketed.solve(v0221__blade_solidity, v0222__axial_inflow_velocity, v0232__tangential_inflow_velocity, v0215__radius, v0202__rotor_radius, v0201__hub_radius, v0210__chord, v0209__pitch, v0141_Re)
v0252_phi_distribution = _00as_bracketed_out[0]
v0253_alpha_distribution = _00as_bracketed_out[1]
v0254_Cl = _00as_bracketed_out[2]
v0255_Cd = _00as_bracketed_out[3]

# op _00A7_power_combination_eval
# LANG: _00A0, _00zY --> _00A8
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01019__00A8 = (v01018__00A0**1)*(v01023__00zY**1)
v01019__00A8 = (v01019__00A8*_00A7_coeff).reshape((1, 40, 30))

# op _00CY_power_combination_eval
# LANG: _00CX --> _00CZ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01103__00CZ = (v01102__00CX**1)
v01103__00CZ = (v01103__00CZ*_00CY_coeff).reshape((1, 40, 30))

# op _00DU_power_combination_eval
# LANG: _00DR, _00DT --> dynamic_viscosity
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01132_dynamic_viscosity = (v01131__00DR**1)*(v01133__00DT**-1)
v01132_dynamic_viscosity = (v01132_dynamic_viscosity*_00DU_coeff).reshape((1, 1))

# op _00zf_arcsin_eval
# LANG: _00ze --> _00zg
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01004__00zg = np.arcsin(v01003__00ze)

# op _00A2 expand_scalar_eval
# LANG: dynamic_viscosity --> _00A3
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01132_dynamic_viscosity = v01132_dynamic_viscosity.reshape((1,))
v01026__00A3 = np.empty((1, 40, 30))
v01026__00A3.fill(v01132_dynamic_viscosity.item())
v01132_dynamic_viscosity = v01132_dynamic_viscosity.reshape((1, 1))

# op _00A9_power_combination_eval
# LANG: _00A8, _chord --> _00Aa
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01024__00Aa = (v01019__00A8**1)*(v01094__chord**1)
v01024__00Aa = (v01024__00Aa*_00A9_coeff).reshape((1, 40, 30))

# op _00C__power_combination_eval
# LANG: _00CZ --> _00D0
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01104__00D0 = (v01103__00CZ**1)
v01104__00D0 = (v01104__00D0*_00C__coeff).reshape((1, 40, 30))

# op _00zh_linear_combination_eval
# LANG: _00zg --> twist_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01005_twist_profile = _00zh_constant+1*v01004__00zg

# op _00Ab_power_combination_eval
# LANG: _00Aa, _00A3 --> Re
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01025_Re = (v01024__00Aa**1)*(v01026__00A3**-1)
v01025_Re = (v01025_Re*_00Ab_coeff).reshape((1, 40, 30))

# op _00Cy expand_array_eval
# LANG: twist_profile --> _pitch
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01005_twist_profile = v01005_twist_profile.reshape((40,))
v01093__pitch = np.einsum('b,ac->abc', v01005_twist_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v01005_twist_profile = v01005_twist_profile.reshape((40, 1))

# op _00D1_power_combination_eval
# LANG: _radius, _00D0 --> _blade_solidity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01105__blade_solidity = (v01104__00D0**1)*(v01099__radius**-1)
v01105__blade_solidity = (v01105__blade_solidity*_00D1_coeff).reshape((1, 40, 30))

# op _00FM_bracketed_implict_eval
# LANG: Re, _hub_radius, _rotor_radius, _pitch, _chord, _radius, _blade_solidity, _axial_inflow_velocity, _tangential_inflow_velocity --> phi_distribution, alpha_distribution, Cl, Cd
# SHAPES: (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30) --> (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.phi_bracketed_search_group
_00FM_bracketed.set_guess(initial_guess_v01136_phi_distribution)
_00FM_bracketed_out = _00FM_bracketed.solve(v01105__blade_solidity, v01106__axial_inflow_velocity, v01116__tangential_inflow_velocity, v01099__radius, v01086__rotor_radius, v01085__hub_radius, v01094__chord, v01093__pitch, v01025_Re)
v01136_phi_distribution = _00FM_bracketed_out[0]
v01137_alpha_distribution = _00FM_bracketed_out[1]
v01138_Cl = _00FM_bracketed_out[2]
v01139_Cd = _00FM_bracketed_out[3]

# op _00aB_linear_combination_eval
# LANG: _rotor_radius, _radius --> _00aC
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0256__00aC = _00aB_constant+1*v0202__rotor_radius+-1*v0215__radius

# op _00aL_linear_combination_eval
# LANG: _hub_radius, _radius --> _00aM
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0266__00aM = _00aL_constant+1*v0215__radius+-1*v0201__hub_radius

# op _00aD_power_combination_eval
# LANG: _00aC --> _00aE
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0257__00aE = (v0256__00aC**1)
v0257__00aE = (v0257__00aE*_00aD_coeff).reshape((1, 40, 100))

# op _00aN_power_combination_eval
# LANG: _00aM --> _00aO
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0267__00aO = (v0266__00aM**1)
v0267__00aO = (v0267__00aO*_00aN_coeff).reshape((1, 40, 100))

# op _00aF_power_combination_eval
# LANG: _00aE, _radius --> _00aG
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0258__00aG = (v0257__00aE**1)*(v0215__radius**-1)
v0258__00aG = (v0258__00aG*_00aF_coeff).reshape((1, 40, 100))

# op _00aH_sin_eval
# LANG: phi_distribution --> _00aI
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0260__00aI = np.sin(v0252_phi_distribution)

# op _00aP_power_combination_eval
# LANG: _00aO, _hub_radius --> _00aQ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0268__00aQ = (v0267__00aO**1)*(v0201__hub_radius**-1)
v0268__00aQ = (v0268__00aQ*_00aP_coeff).reshape((1, 40, 100))

# op _00aR_sin_eval
# LANG: phi_distribution --> _00aS
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0270__00aS = np.sin(v0252_phi_distribution)

# op _00FV_linear_combination_eval
# LANG: _rotor_radius, _radius --> _00FW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01140__00FW = _00FV_constant+1*v01086__rotor_radius+-1*v01099__radius

# op _00G4_linear_combination_eval
# LANG: _hub_radius, _radius --> _00G5
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01150__00G5 = _00G4_constant+1*v01099__radius+-1*v01085__hub_radius

# op _00aJ_power_combination_eval
# LANG: _00aG, _00aI --> _00aK
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0259__00aK = (v0258__00aG**1)*(v0260__00aI**-1)
v0259__00aK = (v0259__00aK*_00aJ_coeff).reshape((1, 40, 100))

# op _00aT_power_combination_eval
# LANG: _00aQ, _00aS --> _00aU
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0269__00aU = (v0268__00aQ**1)*(v0270__00aS**-1)
v0269__00aU = (v0269__00aU*_00aT_coeff).reshape((1, 40, 100))

# op _00FX_power_combination_eval
# LANG: _00FW --> _00FY
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01141__00FY = (v01140__00FW**1)
v01141__00FY = (v01141__00FY*_00FX_coeff).reshape((1, 40, 30))

# op _00G6_power_combination_eval
# LANG: _00G5 --> _00G7
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01151__00G7 = (v01150__00G5**1)
v01151__00G7 = (v01151__00G7*_00G6_coeff).reshape((1, 40, 30))

# op _00QV_power_combination_eval
# LANG: rpm --> _00QW
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v0162_rpm = v0162_rpm.reshape((1,))
v01490__00QW = (v0162_rpm**1)
v01490__00QW = (v01490__00QW*_00QV_coeff).reshape((1,))
v0162_rpm = v0162_rpm.reshape((1, 1))

# op _00aV_linear_combination_eval
# LANG: _00aK --> _00aW
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0261__00aW = _00aV_constant+-1*v0259__00aK

# op _00b2_linear_combination_eval
# LANG: _00aU --> _00b3
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0271__00b3 = _00b2_constant+-1*v0269__00aU

# op _00FZ_power_combination_eval
# LANG: _00FY, _radius --> _00F_
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01142__00F_ = (v01141__00FY**1)*(v01099__radius**-1)
v01142__00F_ = (v01142__00F_*_00FZ_coeff).reshape((1, 40, 30))

# op _00G0_sin_eval
# LANG: phi_distribution --> _00G1
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01144__00G1 = np.sin(v01136_phi_distribution)

# op _00G8_power_combination_eval
# LANG: _00G7, _hub_radius --> _00G9
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01152__00G9 = (v01151__00G7**1)*(v01085__hub_radius**-1)
v01152__00G9 = (v01152__00G9*_00G8_coeff).reshape((1, 40, 30))

# op _00Ga_sin_eval
# LANG: phi_distribution --> _00Gb
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01154__00Gb = np.sin(v01136_phi_distribution)

# op _00Nh_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00Ni
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((3,))
v01361__00Ni = (v06_rotor_disk_in_plane_1**1)
v01361__00Ni = (v01361__00Ni*_00Nh_coeff).reshape((3,))
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((1, 3))

# op _00QX_power_combination_eval
# LANG: _00QW --> _00QY
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01491__00QY = (v01490__00QW**1)
v01491__00QY = (v01491__00QY*_00QX_coeff).reshape((1,))

# op _00aX exp_eval
# LANG: _00aW --> _00aY
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0262__00aY = np.exp(v0261__00aW)

# op _00b4 exp_eval
# LANG: _00b3 --> _00b5
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0272__00b5 = np.exp(v0271__00b3)

# op _00G2_power_combination_eval
# LANG: _00F_, _00G1 --> _00G3
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01143__00G3 = (v01142__00F_**1)*(v01144__00G1**-1)
v01143__00G3 = (v01143__00G3*_00G2_coeff).reshape((1, 40, 30))

# op _00Gc_power_combination_eval
# LANG: _00G9, _00Gb --> _00Gd
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01153__00Gd = (v01152__00G9**1)*(v01154__00Gb**-1)
v01153__00Gd = (v01153__00Gd*_00Gc_coeff).reshape((1, 40, 30))

# op _00Nj pnorm_eval
# LANG: _00Ni --> _00Nk
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01362__00Nk = np.linalg.norm(v01361__00Ni.flatten(), ord=2)

# op _00No pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00Np
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01364__00Np = np.sum(v012_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00QZ_power_combination_eval
# LANG: _00QY --> _00Q_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01492__00Q_ = (v01491__00QY**1)
v01492__00Q_ = (v01492__00Q_*_00QZ_coeff).reshape((1,))

# op _00aZ arccos_eval
# LANG: _00aY --> _00a_
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0263__00a_ = np.arccos(v0262__00aY)

# op _00b6 arccos_eval
# LANG: _00b5 --> _00b7
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0273__00b7 = np.arccos(v0272__00b5)

# op _00Ge_linear_combination_eval
# LANG: _00G3 --> _00Gf
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01145__00Gf = _00Ge_constant+-1*v01143__00G3

# op _00Gm_linear_combination_eval
# LANG: _00Gd --> _00Gn
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01155__00Gn = _00Gm_constant+-1*v01153__00Gd

# op _00Nl_power_combination_eval
# LANG: _00Nk --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01363_propeller_radius = (v01362__00Nk**1)
v01363_propeller_radius = (v01363_propeller_radius*_00Nl_coeff).reshape((1,))

# op _00Nq reshape_eval
# LANG: _00Np --> _00Nr
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01365__00Nr = v01364__00Np.reshape((40, 1))

# op _00Rp expand_array_eval
# LANG: nondim_sectional_radius --> _00Rq
# SHAPES: (40,) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01482__00Rq = np.einsum('d,abce->abcde', v01481_nondim_sectional_radius.reshape((40,)) ,np.ones((1, 1, 3, 11))).reshape((1, 1, 3, 40, 11))

# op _00Rr expand_scalar_eval
# LANG: _00Q_ --> _00Rs
# SHAPES: (1,) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01493__00Rs = np.empty((1, 1, 3, 40, 11))
v01493__00Rs.fill(v01492__00Q_.item())

# op _00b0_power_combination_eval
# LANG: _00a_ --> _00b1
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0264__00b1 = (v0263__00a_**1)
v0264__00b1 = (v0264__00b1*_00b0_coeff).reshape((1, 40, 100))

# op _00b8_power_combination_eval
# LANG: _00b7 --> _00b9
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0274__00b9 = (v0273__00b7**1)
v0274__00b9 = (v0274__00b9*_00b8_coeff).reshape((1, 40, 100))

# op _00bH_sin_eval
# LANG: phi_distribution --> _00bI
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0289__00bI = np.sin(v0252_phi_distribution)

# op _00bL_cos_eval
# LANG: phi_distribution --> _00bM
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0292__00bM = np.cos(v0252_phi_distribution)

# op _00Gg exp_eval
# LANG: _00Gf --> _00Gh
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01146__00Gh = np.exp(v01145__00Gf)

# op _00Go exp_eval
# LANG: _00Gn --> _00Gp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01156__00Gp = np.exp(v01155__00Gn)

# op _00Ns_power_combination_eval
# LANG: _00Nr --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01366_chord_profile = (v01365__00Nr**1)
v01366_chord_profile = (v01366_chord_profile*_00Ns_coeff).reshape((40, 1))

# op _00RD_decompose_eval
# LANG: _00Rq --> _00RE
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01500__00RE = ((v01482__00Rq.flatten())[src_indices__00RE__00RD]).reshape((1, 1, 3, 40, 10))

# op _00RF_decompose_eval
# LANG: _00Rs --> _00RG
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01494__00RG = ((v01493__00Rs.flatten())[src_indices__00RG__00RF]).reshape((1, 1, 3, 40, 10))

# op _00Rt expand_scalar_eval
# LANG: propeller_radius --> _00Ru
# SHAPES: (1,) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01502__00Ru = np.empty((1, 1, 3, 40, 11))
v01502__00Ru.fill(v01363_propeller_radius.item())

# op _00bB_sin_eval
# LANG: phi_distribution --> _00bC
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0299__00bC = np.sin(v0252_phi_distribution)

# op _00bJ_power_combination_eval
# LANG: _00bI, Cl --> _00bK
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0288__00bK = (v0254_Cl**1)*(v0289__00bI**1)
v0288__00bK = (v0288__00bK*_00bJ_coeff).reshape((1, 40, 100))

# op _00bN_power_combination_eval
# LANG: _00bM, Cd --> _00bO
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0291__00bO = (v0255_Cd**1)*(v0292__00bM**1)
v0291__00bO = (v0291__00bO*_00bN_coeff).reshape((1, 40, 100))

# op _00ba_power_combination_eval
# LANG: _00b1, _00b9 --> prandtl_loss_factor
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0265_prandtl_loss_factor = (v0264__00b1**1)*(v0274__00b9**1)
v0265_prandtl_loss_factor = (v0265_prandtl_loss_factor*_00ba_coeff).reshape((1, 40, 100))

# op _00bx_cos_eval
# LANG: phi_distribution --> _00by
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0296__00by = np.cos(v0252_phi_distribution)

# op _00cS_power_combination_eval
# LANG: phi_distribution --> _00cT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0315__00cT = (v0252_phi_distribution**1)
v0315__00cT = (v0315__00cT*_00cS_coeff).reshape((1, 40, 100))

# op _00Gi arccos_eval
# LANG: _00Gh --> _00Gj
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01147__00Gj = np.arccos(v01146__00Gh)

# op _00Gq arccos_eval
# LANG: _00Gp --> _00Gr
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01157__00Gr = np.arccos(v01156__00Gp)

# op _00RH_decompose_eval
# LANG: _00Ru --> _00RI
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01503__00RI = ((v01502__00Ru.flatten())[src_indices__00RI__00RH]).reshape((1, 1, 3, 40, 10))

# op _00Rx expand_array_eval
# LANG: chord_profile --> _00Ry
# SHAPES: (40,) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01366_chord_profile = v01366_chord_profile.reshape((40,))
v01496__00Ry = np.einsum('d,abce->abcde', v01366_chord_profile.reshape((40,)) ,np.ones((1, 1, 3, 11))).reshape((1, 1, 3, 40, 11))
v01366_chord_profile = v01366_chord_profile.reshape((40, 1))

# op _00Sh_decompose_eval
# LANG: lam_var --> _00Si
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01488__00Si = ((v01487_lam_var.flatten())[src_indices__00Si__00Sh]).reshape((1, 1, 3, 40, 10))

# op _00Sj_power_combination_eval
# LANG: _00RG, _00RE --> _00Sk
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01499__00Sk = (v01494__00RG**1)*(v01500__00RE**1)
v01499__00Sk = (v01499__00Sk*_00Sj_coeff).reshape((1, 1, 3, 40, 10))

# op _00bD_power_combination_eval
# LANG: _00bC, Cd --> _00bE
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0298__00bE = (v0255_Cd**1)*(v0299__00bC**1)
v0298__00bE = (v0298__00bE*_00bD_coeff).reshape((1, 40, 100))

# op _00bP_linear_combination_eval
# LANG: _00bK, _00bO --> _00bQ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0290__00bQ = _00bP_constant+1*v0288__00bK+1*v0291__00bO

# op _00bz_power_combination_eval
# LANG: _00by, Cl --> _00bA
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0295__00bA = (v0254_Cl**1)*(v0296__00by**1)
v0295__00bA = (v0295__00bA*_00bz_coeff).reshape((1, 40, 100))

# op _00cK_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00cL
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0309__00cL = (v0232__tangential_inflow_velocity**1)
v0309__00cL = (v0309__00cL*_00cK_coeff).reshape((1, 40, 100))

# op _00cQ_power_combination_eval
# LANG: prandtl_loss_factor --> _00cR
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0313__00cR = (v0265_prandtl_loss_factor**1)
v0313__00cR = (v0313__00cR*_00cQ_coeff).reshape((1, 40, 100))

# op _00cU_sin_eval
# LANG: _00cT --> _00cV
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0316__00cV = np.sin(v0315__00cT)

# op _00cs_power_combination_eval
# LANG: prandtl_loss_factor --> _00ct
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0302__00ct = (v0265_prandtl_loss_factor**1)
v0302__00ct = (v0302__00ct*_00cs_coeff).reshape((1, 40, 100))

# op _00cu_sin_eval
# LANG: phi_distribution --> _00cv
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0304__00cv = np.sin(v0252_phi_distribution)

# op _00Gk_power_combination_eval
# LANG: _00Gj --> _00Gl
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01148__00Gl = (v01147__00Gj**1)
v01148__00Gl = (v01148__00Gl*_00Gk_coeff).reshape((1, 40, 30))

# op _00Gs_power_combination_eval
# LANG: _00Gr --> _00Gt
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01158__00Gt = (v01157__00Gr**1)
v01158__00Gt = (v01158__00Gt*_00Gs_coeff).reshape((1, 40, 30))

# op _00H0_sin_eval
# LANG: phi_distribution --> _00H1
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01173__00H1 = np.sin(v01136_phi_distribution)

# op _00H4_cos_eval
# LANG: phi_distribution --> _00H5
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01176__00H5 = np.cos(v01136_phi_distribution)

# op _00OC_power_combination_eval
# LANG: altitude --> _00OD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01398__00OD = (v0930_hover_altitude**1)
v01398__00OD = (v01398__00OD*_00OC_coeff).reshape((1,))

# op _00RL_decompose_eval
# LANG: _00Ry --> _00RM
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01497__00RM = ((v01496__00Ry.flatten())[src_indices__00RM__00RL]).reshape((1, 1, 3, 40, 10))

# op _00Sl_power_combination_eval
# LANG: _00Sk, _00RI --> _00Sm
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01501__00Sm = (v01499__00Sk**1)*(v01503__00RI**1)
v01501__00Sm = (v01501__00Sm*_00Sl_coeff).reshape((1, 1, 3, 40, 10))

# op _00Sn_power_combination_eval
# LANG: _00Si, _00RG --> _00So
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01489__00So = (v01488__00Si**1)*(v01494__00RG**1)
v01489__00So = (v01489__00So*_00Sn_coeff).reshape((1, 1, 3, 40, 10))

# op _00bF_linear_combination_eval
# LANG: _00bA, _00bE --> _00bG
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0297__00bG = _00bF_constant+1*v0295__00bA+-1*v0298__00bE

# op _00c8_power_combination_eval
# LANG: prandtl_loss_factor --> _00c9
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0281__00c9 = (v0265_prandtl_loss_factor**1)
v0281__00c9 = (v0281__00c9*_00c8_coeff).reshape((1, 40, 100))

# op _00cM_power_combination_eval
# LANG: _00cL, _blade_solidity --> _00cN
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0310__00cN = (v0309__00cL**1)*(v0221__blade_solidity**1)
v0310__00cN = (v0310__00cN*_00cM_coeff).reshape((1, 40, 100))

# op _00cW_power_combination_eval
# LANG: _00cR, _00cV --> _00cX
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0314__00cX = (v0313__00cR**1)*(v0316__00cV**1)
v0314__00cX = (v0314__00cX*_00cW_coeff).reshape((1, 40, 100))

# op _00cY_power_combination_eval
# LANG: _00bQ, _blade_solidity --> _00cZ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0318__00cZ = (v0221__blade_solidity**1)*(v0290__00bQ**1)
v0318__00cZ = (v0318__00cZ*_00cY_coeff).reshape((1, 40, 100))

# op _00ca_sin_eval
# LANG: phi_distribution --> _00cb
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0283__00cb = np.sin(v0252_phi_distribution)

# op _00cw_power_combination_eval
# LANG: _00ct, _00cv --> _00cx
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0303__00cx = (v0302__00ct**1)*(v0304__00cv**1)
v0303__00cx = (v0303__00cx*_00cw_coeff).reshape((1, 40, 100))

# op _00cy_cos_eval
# LANG: phi_distribution --> _00cz
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0306__00cz = np.cos(v0252_phi_distribution)

# op _00k3 expand_scalar_eval
# LANG: Vx --> _00k4
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0533__00k4 = np.empty((1, 1))
v0533__00k4.fill(v028_u.item())

# op _00k6 expand_scalar_eval
# LANG: Vy --> _00k7
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0535__00k7 = np.empty((1, 1))
v0535__00k7.fill(v033_v.item())

# op _00k8 expand_scalar_eval
# LANG: Vz --> _00k9
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0536__00k9 = np.empty((1, 1))
v0536__00k9.fill(v037_w.item())

# op _00GR_cos_eval
# LANG: phi_distribution --> _00GS
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01180__00GS = np.cos(v01136_phi_distribution)

# op _00GV_sin_eval
# LANG: phi_distribution --> _00GW
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01183__00GW = np.sin(v01136_phi_distribution)

# op _00Gu_power_combination_eval
# LANG: _00Gl, _00Gt --> prandtl_loss_factor
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01149_prandtl_loss_factor = (v01148__00Gl**1)*(v01158__00Gt**1)
v01149_prandtl_loss_factor = (v01149_prandtl_loss_factor*_00Gu_coeff).reshape((1, 40, 30))

# op _00H2_power_combination_eval
# LANG: _00H1, Cl --> _00H3
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01172__00H3 = (v01138_Cl**1)*(v01173__00H1**1)
v01172__00H3 = (v01172__00H3*_00H2_coeff).reshape((1, 40, 30))

# op _00H6_power_combination_eval
# LANG: _00H5, Cd --> _00H7
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01175__00H7 = (v01139_Cd**1)*(v01176__00H5**1)
v01175__00H7 = (v01175__00H7*_00H6_coeff).reshape((1, 40, 30))

# op _00Ib_power_combination_eval
# LANG: phi_distribution --> _00Ic
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01199__00Ic = (v01136_phi_distribution**1)
v01199__00Ic = (v01199__00Ic*_00Ib_coeff).reshape((1, 40, 30))

# op _00OE_linear_combination_eval
# LANG: _00OD --> _00OF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01399__00OF = _00OE_constant+-1*v01398__00OD

# op _00Sp_power_combination_eval
# LANG: _00So, _00RM --> _00Sq
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01495__00Sq = (v01489__00So**1)*(v01497__00RM**1)
v01495__00Sq = (v01495__00Sq*_00Sp_coeff).reshape((1, 1, 3, 40, 10))

# op _00Sr_power_combination_eval
# LANG: _00Sm --> _00Ss
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01504__00Ss = (v01501__00Sm**1)
v01504__00Ss = (v01504__00Ss*_00Sr_coeff).reshape((1, 1, 3, 40, 10))

# op _00bZ_power_combination_eval
# LANG: prandtl_loss_factor --> _00b_
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0275__00b_ = (v0265_prandtl_loss_factor**1)
v0275__00b_ = (v0275__00b_*_00bZ_coeff).reshape((1, 40, 100))

# op _00c2_sin_eval
# LANG: phi_distribution --> _00c3
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0278__00c3 = np.sin(v0252_phi_distribution)

# op _00cA_power_combination_eval
# LANG: _00cx, _00cz --> _00cB
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0305__00cB = (v0303__00cx**1)*(v0306__00cz**1)
v0305__00cB = (v0305__00cB*_00cA_coeff).reshape((1, 40, 100))

# op _00cC_power_combination_eval
# LANG: _00bQ, _blade_solidity --> _00cD
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0308__00cD = (v0221__blade_solidity**1)*(v0290__00bQ**1)
v0308__00cD = (v0308__00cD*_00cC_coeff).reshape((1, 40, 100))

# op _00cO_power_combination_eval
# LANG: _00bQ, _00cN --> _00cP
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0311__00cP = (v0310__00cN**1)*(v0290__00bQ**1)
v0311__00cP = (v0311__00cP*_00cO_coeff).reshape((1, 40, 100))

# op _00c__linear_combination_eval
# LANG: _00cX, _00cZ --> _00d0
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0317__00d0 = _00c__constant+1*v0314__00cX+1*v0318__00cZ

# op _00cc_power_combination_eval
# LANG: _00c9, _00cb --> _00cd
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0282__00cd = (v0281__00c9**1)*(v0283__00cb**1)
v0282__00cd = (v0282__00cd*_00cc_coeff).reshape((1, 40, 100))

# op _00ce_cos_eval
# LANG: phi_distribution --> _00cf
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0285__00cf = np.cos(v0252_phi_distribution)

# op _00co_power_combination_eval
# LANG: _00bG, _blade_solidity --> _00cp
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0294__00cp = (v0221__blade_solidity**1)*(v0297__00bG**1)
v0294__00cp = (v0294__00cp*_00co_coeff).reshape((1, 40, 100))

# op _00k5_indexed_passthrough_eval
# LANG: _00k4, _00k7, _00k9 --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0534_V_aircraft__temp[i_v0533__00k4__00k5_indexed_passthrough_eval] = v0533__00k4.flatten()
v0534_V_aircraft = v0534_V_aircraft__temp.copy()
v0534_V_aircraft__temp[i_v0535__00k7__00k5_indexed_passthrough_eval] = v0535__00k7.flatten()
v0534_V_aircraft = v0534_V_aircraft__temp.copy()
v0534_V_aircraft__temp[i_v0536__00k9__00k5_indexed_passthrough_eval] = v0536__00k9.flatten()
v0534_V_aircraft = v0534_V_aircraft__temp.copy()

# op _000h_sparsematmat_eval
# LANG: system_representation_geometry --> _000i
# SHAPES: (16250, 3) --> (1, 3)
# full namespace: system_representation.nonlinear_outputs_model
v09__000i = _000h_sparsematmat_eval_mat@v04_system_representation_geometry

# op _00GT_power_combination_eval
# LANG: _00GS, Cl --> _00GU
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01179__00GU = (v01138_Cl**1)*(v01180__00GS**1)
v01179__00GU = (v01179__00GU*_00GT_coeff).reshape((1, 40, 30))

# op _00GX_power_combination_eval
# LANG: _00GW, Cd --> _00GY
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01182__00GY = (v01139_Cd**1)*(v01183__00GW**1)
v01182__00GY = (v01182__00GY*_00GX_coeff).reshape((1, 40, 30))

# op _00H8_linear_combination_eval
# LANG: _00H3, _00H7 --> _00H9
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01174__00H9 = _00H8_constant+1*v01172__00H3+1*v01175__00H7

# op _00HM_power_combination_eval
# LANG: prandtl_loss_factor --> _00HN
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01186__00HN = (v01149_prandtl_loss_factor**1)
v01186__00HN = (v01186__00HN*_00HM_coeff).reshape((1, 40, 30))

# op _00HO_sin_eval
# LANG: phi_distribution --> _00HP
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01188__00HP = np.sin(v01136_phi_distribution)

# op _00I3_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00I4
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01193__00I4 = (v01116__tangential_inflow_velocity**1)
v01193__00I4 = (v01193__00I4*_00I3_coeff).reshape((1, 40, 30))

# op _00I9_power_combination_eval
# LANG: prandtl_loss_factor --> _00Ia
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01197__00Ia = (v01149_prandtl_loss_factor**1)
v01197__00Ia = (v01197__00Ia*_00I9_coeff).reshape((1, 40, 30))

# op _00Id_sin_eval
# LANG: _00Ic --> _00Ie
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01200__00Ie = np.sin(v01199__00Ic)

# op _00OG_power_combination_eval
# LANG: _00OF --> _00OH
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01400__00OH = (v01399__00OF**1)
v01400__00OH = (v01400__00OH*_00OG_coeff).reshape((1,))

# op _00St_power_combination_eval
# LANG: _00Sq, _00Ss --> _00Su
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01498__00Su = (v01495__00Sq**1)*(v01504__00Ss**-1)
v01498__00Su = (v01498__00Su*_00St_coeff).reshape((1, 1, 3, 40, 10))

# op _00c0_power_combination_eval
# LANG: _00b_, _tangential_inflow_velocity --> _00c1
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0276__00c1 = (v0275__00b_**1)*(v0232__tangential_inflow_velocity**1)
v0276__00c1 = (v0276__00c1*_00c0_coeff).reshape((1, 40, 100))

# op _00c4_power_combination_eval
# LANG: _00c3 --> _00c5
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0279__00c5 = (v0278__00c3**2)
v0279__00c5 = (v0279__00c5*_00c4_coeff).reshape((1, 40, 100))

# op _00cE_linear_combination_eval
# LANG: _00cB, _00cD --> _00cF
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0307__00cF = _00cE_constant+1*v0305__00cB+1*v0308__00cD

# op _00cg_power_combination_eval
# LANG: _00cd, _00cf --> _00ch
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0284__00ch = (v0282__00cd**1)*(v0285__00cf**1)
v0284__00ch = (v0284__00ch*_00cg_coeff).reshape((1, 40, 100))

# op _00ci_power_combination_eval
# LANG: _00bQ, _blade_solidity --> _00cj
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0287__00cj = (v0221__blade_solidity**1)*(v0290__00bQ**1)
v0287__00cj = (v0287__00cj*_00ci_coeff).reshape((1, 40, 100))

# op _00cq_power_combination_eval
# LANG: _00cp, _tangential_inflow_velocity --> _00cr
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0300__00cr = (v0294__00cp**1)*(v0232__tangential_inflow_velocity**1)
v0300__00cr = (v0300__00cr*_00cq_coeff).reshape((1, 40, 100))

# op _00d1_power_combination_eval
# LANG: _00cP, _00d0 --> _ut
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0312__ut = (v0311__00cP**1)*(v0317__00d0**-1)
v0312__ut = (v0312__ut*_00d1_coeff).reshape((1, 40, 100))

# op _00ka expand_array_eval
# LANG: V_aircraft --> _00kb
# SHAPES: (1, 3) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0543__00kb = np.einsum('ab,c->abc', v0534_V_aircraft.reshape((1, 3)) ,np.ones((1,))).reshape((1, 3, 1))

# op _00kg expand_scalar_eval
# LANG: time_vectors --> _00kh
# SHAPES: (1,) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0549__00kh = np.empty((1, 3, 1))
v0549__00kh.fill(v0548_time_vectors.item())

# op _000j reshape_eval
# LANG: _000i --> rotor_disk_origin
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.nonlinear_outputs_model
v010_rotor_disk_origin = v09__000i.reshape((1, 3))

# op _00GZ_linear_combination_eval
# LANG: _00GU, _00GY --> _00G_
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01181__00G_ = _00GZ_constant+1*v01179__00GU+-1*v01182__00GY

# op _00HQ_power_combination_eval
# LANG: _00HN, _00HP --> _00HR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01187__00HR = (v01186__00HN**1)*(v01188__00HP**1)
v01187__00HR = (v01187__00HR*_00HQ_coeff).reshape((1, 40, 30))

# op _00HS_cos_eval
# LANG: phi_distribution --> _00HT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01190__00HT = np.cos(v01136_phi_distribution)

# op _00I5_power_combination_eval
# LANG: _00I4, _blade_solidity --> _00I6
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01194__00I6 = (v01193__00I4**1)*(v01105__blade_solidity**1)
v01194__00I6 = (v01194__00I6*_00I5_coeff).reshape((1, 40, 30))

# op _00If_power_combination_eval
# LANG: _00Ia, _00Ie --> _00Ig
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01198__00Ig = (v01197__00Ia**1)*(v01200__00Ie**1)
v01198__00Ig = (v01198__00Ig*_00If_coeff).reshape((1, 40, 30))

# op _00Ih_power_combination_eval
# LANG: _00H9, _blade_solidity --> _00Ii
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01202__00Ii = (v01105__blade_solidity**1)*(v01174__00H9**1)
v01202__00Ii = (v01202__00Ii*_00Ih_coeff).reshape((1, 40, 30))

# op _00OI_linear_combination_eval
# LANG: _00OH --> temperature
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01401_temperature = _00OI_constant+1*v01400__00OH

# op _00RQ_decompose_eval
# LANG: phi --> _00RR
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01477__00RR = ((v01136_phi_distribution.flatten())[src_indices__00RR__00RQ]).reshape((1, 40, 1))

# op _00Ub_bessel_eval
# LANG: _00Su --> _00Uc
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01584__00Uc=_00Ub_bessel_eval(0,v01498__00Su)

# op _00Ud_bessel_eval
# LANG: _00Su --> _00Ue
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01586__00Ue=_00Ud_bessel_eval(1,v01498__00Su)

# op _00br expand_scalar_eval
# LANG: density --> _00bs
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0243_density = v0243_density.reshape((1,))
v0321__00bs = np.empty((1, 40, 100))
v0321__00bs.fill(v0243_density.item())
v0243_density = v0243_density.reshape((1, 1))

# op _00c6_power_combination_eval
# LANG: _00c1, _00c5 --> _00c7
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0277__00c7 = (v0276__00c1**1)*(v0279__00c5**1)
v0277__00c7 = (v0277__00c7*_00c6_coeff).reshape((1, 40, 100))

# op _00cG_power_combination_eval
# LANG: _00cr, _00cF --> _00cH
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0301__00cH = (v0300__00cr**1)*(v0307__00cF**-1)
v0301__00cH = (v0301__00cH*_00cG_coeff).reshape((1, 40, 100))

# op _00ck_linear_combination_eval
# LANG: _00ch, _00cj --> _00cl
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0286__00cl = _00ck_constant+1*v0284__00ch+1*v0287__00cj

# op _00d3_power_combination_eval
# LANG: _radius --> _00d4
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0319__00d4 = (v0215__radius**1)
v0319__00d4 = (v0319__00d4*_00d3_coeff).reshape((1, 40, 100))

# op _00eC_power_combination_eval
# LANG: _ut --> _00eD
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0381__00eD = (v0312__ut**1)
v0381__00eD = (v0381__00eD*_00eC_coeff).reshape((1, 40, 100))

# op _00kd expand_array_eval
# LANG: aircraft_location --> _00ke
# SHAPES: (3, 1) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0538__00ke = np.einsum('bc,a->abc', v0537_aircraft_location.reshape((3, 1)) ,np.ones((1,))).reshape((1, 3, 1))

# op _00kk_decompose_eval
# LANG: _00kb --> _00kl, _00kt, _00kA
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0544__00kl = ((v0543__00kb.flatten())[src_indices__00kl__00kk]).reshape((1, 1, 1))
v0545__00kt = ((v0543__00kb.flatten())[src_indices__00kt__00kk]).reshape((1, 1, 1))
v0546__00kA = ((v0543__00kb.flatten())[src_indices__00kA__00kk]).reshape((1, 1, 1))

# op _00km_decompose_eval
# LANG: _00kh --> _00kn, _00ku, _00kB
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0550__00kn = ((v0549__00kh.flatten())[src_indices__00kn__00km]).reshape((1, 1, 1))
v0551__00ku = ((v0549__00kh.flatten())[src_indices__00ku__00km]).reshape((1, 1, 1))
v0552__00kB = ((v0549__00kh.flatten())[src_indices__00kB__00km]).reshape((1, 1, 1))

# op _005R_power_combination_eval
# LANG: propeller_radius --> _005S
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0193__005S = (v0126_propeller_radius**1)
v0193__005S = (v0193__005S*_005R_coeff).reshape((1,))

# op _00HI_power_combination_eval
# LANG: _00G_, _blade_solidity --> _00HJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01178__00HJ = (v01105__blade_solidity**1)*(v01181__00G_**1)
v01178__00HJ = (v01178__00HJ*_00HI_coeff).reshape((1, 40, 30))

# op _00HU_power_combination_eval
# LANG: _00HR, _00HT --> _00HV
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01189__00HV = (v01187__00HR**1)*(v01190__00HT**1)
v01189__00HV = (v01189__00HV*_00HU_coeff).reshape((1, 40, 30))

# op _00HW_power_combination_eval
# LANG: _00H9, _blade_solidity --> _00HX
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01192__00HX = (v01105__blade_solidity**1)*(v01174__00H9**1)
v01192__00HX = (v01192__00HX*_00HW_coeff).reshape((1, 40, 30))

# op _00I7_power_combination_eval
# LANG: _00H9, _00I6 --> _00I8
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01195__00I8 = (v01194__00I6**1)*(v01174__00H9**1)
v01195__00I8 = (v01195__00I8*_00I7_coeff).reshape((1, 40, 30))

# op _00Ij_linear_combination_eval
# LANG: _00Ig, _00Ii --> _00Ik
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01201__00Ik = _00Ij_constant+1*v01198__00Ig+1*v01202__00Ii

# op _00OK_power_combination_eval
# LANG: temperature --> _00OL
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01402__00OL = (v01401_temperature**1)
v01402__00OL = (v01402__00OL*_00OK_coeff).reshape((1,))

# op _00RS reshape_eval
# LANG: _00RR --> _00RT
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01478__00RT = v01477__00RR.reshape((1, 40))

# op _00U7_bessel_eval
# LANG: _00Su --> _00U8
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01581__00U8=_00U7_bessel_eval(1,v01498__00Su)

# op _00Uf_power_combination_eval
# LANG: _00Uc, _00Ue --> _00Ug
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01585__00Ug = (v01584__00Uc**1)*(v01586__00Ue**1)
v01585__00Ug = (v01585__00Ug*_00Uf_coeff).reshape((1, 1, 3, 40, 10))

# op _00Uh_bessel_eval
# LANG: _00Su --> _00Ui
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01588__00Ui=_00Uh_bessel_eval(1,v01498__00Su)

# op _00Un_bessel_eval
# LANG: _00Su --> _00Uo
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01590__00Uo=_00Un_bessel_eval(1,v01498__00Su)

# op _00cI_linear_combination_eval
# LANG: _00cH, _axial_inflow_velocity --> _ux_2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0293__ux_2 = _00cI_constant+1*v0222__axial_inflow_velocity+1*v0301__00cH

# op _00cm_power_combination_eval
# LANG: _00c7, _00cl --> _ux
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0280__ux = (v0277__00c7**1)*(v0286__00cl**-1)
v0280__ux = (v0280__ux*_00cm_coeff).reshape((1, 40, 100))

# op _00d5_power_combination_eval
# LANG: _00d4, _00bs --> _00d6
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0320__00d6 = (v0319__00d4**1)*(v0321__00bs**1)
v0320__00d6 = (v0320__00d6*_00d5_coeff).reshape((1, 40, 100))

# op _00eE_linear_combination_eval
# LANG: _00eD, _tangential_inflow_velocity --> _00eF
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0380__00eF = _00eE_constant+1*v0232__tangential_inflow_velocity+-1*v0381__00eD

# op _00eu_power_combination_eval
# LANG: Cd --> _00ev
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0374__00ev = (v0255_Cd**1)
v0374__00ev = (v0374__00ev*_00eu_coeff).reshape((1, 40, 100))

# op _00kN expand_array_eval
# LANG: rotor_disk_origin --> _00kO
# SHAPES: (3,) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((3,))
v0561__00kO = np.einsum('b,ac->abc', v010_rotor_disk_origin.reshape((3,)) ,np.ones((1, 1))).reshape((1, 3, 1))
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((1, 3))

# op _00ki_decompose_eval
# LANG: _00ke --> _00kj, _00ks, _00kz
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0539__00kj = ((v0538__00ke.flatten())[src_indices__00kj__00ki]).reshape((1, 1, 1))
v0540__00ks = ((v0538__00ke.flatten())[src_indices__00ks__00ki]).reshape((1, 1, 1))
v0541__00kz = ((v0538__00ke.flatten())[src_indices__00kz__00ki]).reshape((1, 1, 1))

# op _00ko_power_combination_eval
# LANG: _00kl, _00kn --> _00kp
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0547__00kp = (v0544__00kl**1)*(v0550__00kn**1)
v0547__00kp = (v0547__00kp*_00ko_coeff).reshape((1, 1, 1))

# op _00kv_power_combination_eval
# LANG: _00kt, _00ku --> _00kw
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0554__00kw = (v0545__00kt**1)*(v0551__00ku**1)
v0554__00kw = (v0554__00kw*_00kv_coeff).reshape((1, 1, 1))

# op _005T_linear_combination_eval
# LANG: _005S, propeller_radius --> _005U
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0192__005U = _005T_constant+1*v0126_propeller_radius+-1*v0193__005S

# op _00HK_power_combination_eval
# LANG: _00HJ, _tangential_inflow_velocity --> _00HL
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01184__00HL = (v01178__00HJ**1)*(v01116__tangential_inflow_velocity**1)
v01184__00HL = (v01184__00HL*_00HK_coeff).reshape((1, 40, 30))

# op _00HY_linear_combination_eval
# LANG: _00HV, _00HX --> _00HZ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01191__00HZ = _00HY_constant+1*v01189__00HV+1*v01192__00HX

# op _00Il_power_combination_eval
# LANG: _00I8, _00Ik --> _ut
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01196__ut = (v01195__00I8**1)*(v01201__00Ik**-1)
v01196__ut = (v01196__ut*_00Il_coeff).reshape((1, 40, 30))

# op _00OM_power_combination_eval
# LANG: _00OL --> _00ON
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01403__00ON = (v01402__00OL**5.258643795229161)
v01403__00ON = (v01403__00ON*_00OM_coeff).reshape((1,))

# op _00RU expand_array_eval
# LANG: _00RT --> _00RV
# SHAPES: (1, 40) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01479__00RV = np.einsum('ad,bce->abcde', v01478__00RT.reshape((1, 40)) ,np.ones((1, 3, 11))).reshape((1, 1, 3, 40, 11))

# op _00U9_power_combination_eval
# LANG: _00U8 --> _00Ua
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01582__00Ua = (v01581__00U8**3)
v01582__00Ua = (v01582__00Ua*_00U9_coeff).reshape((1, 1, 3, 40, 10))

# op _00Uj_power_combination_eval
# LANG: _00Ug, _00Ui --> _00Uk
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01587__00Uk = (v01585__00Ug**1)*(v01588__00Ui**1)
v01587__00Uk = (v01587__00Uk*_00Uj_coeff).reshape((1, 1, 3, 40, 10))

# op _00Up_power_combination_eval
# LANG: _00Uo --> _00Uq
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01591__00Uq = (v01590__00Uo**2)
v01591__00Uq = (v01591__00Uq*_00Up_coeff).reshape((1, 1, 3, 40, 10))

# op _00Ur_bessel_eval
# LANG: _00Su --> _00Us
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01593__00Us=_00Ur_bessel_eval(0,v01498__00Su)

# op _00Ux_bessel_eval
# LANG: _00Su --> _00Uy
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01595__00Uy=_00Ux_bessel_eval(0,v01498__00Su)

# op _00Uz_bessel_eval
# LANG: _00Su --> _00UA
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01597__00UA=_00Uz_bessel_eval(0,v01498__00Su)

# op _00d7_power_combination_eval
# LANG: _ux, _00d6 --> _00d8
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0322__00d8 = (v0320__00d6**1)*(v0280__ux**1)
v0322__00d8 = (v0322__00d8*_00d7_coeff).reshape((1, 40, 100))

# op _00d9_linear_combination_eval
# LANG: _ux, _axial_inflow_velocity --> _00da
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0324__00da = _00d9_constant+1*v0280__ux+-1*v0222__axial_inflow_velocity

# op _00eA_power_combination_eval
# LANG: _ux_2 --> _00eB
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0378__00eB = (v0293__ux_2**2)
v0378__00eB = (v0378__00eB*_00eA_coeff).reshape((1, 40, 100))

# op _00eG_power_combination_eval
# LANG: _00eF --> _00eH
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0382__00eH = (v0380__00eF**2)
v0382__00eH = (v0382__00eH*_00eG_coeff).reshape((1, 40, 100))

# op _00ew_power_combination_eval
# LANG: _00ev --> _00ex
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0375__00ex = (v0374__00ev**1)
v0375__00ex = (v0375__00ex*_00ew_coeff).reshape((1, 40, 100))

# op _00kP_decompose_eval
# LANG: _00kO --> _00kQ, _00kV, _00k_
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0562__00kQ = ((v0561__00kO.flatten())[src_indices__00kQ__00kP]).reshape((1, 1, 1))
v0563__00kV = ((v0561__00kO.flatten())[src_indices__00kV__00kP]).reshape((1, 1, 1))
v0564__00k_ = ((v0561__00kO.flatten())[src_indices__00k___00kP]).reshape((1, 1, 1))

# op _00kq_linear_combination_eval
# LANG: _00kj, _00kp --> aircraft_x_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0542_aircraft_x_pos = _00kq_constant+1*v0539__00kj+1*v0547__00kp

# op _00kx_linear_combination_eval
# LANG: _00ks, _00kw --> aircraft_y_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0553_aircraft_y_pos = _00kx_constant+1*v0540__00ks+1*v0554__00kw

# op _005V_power_combination_eval
# LANG: _005U --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0194_dr = (v0192__005U**1)
v0194_dr = (v0194_dr*_005V_coeff).reshape((1,))

# op _00H__power_combination_eval
# LANG: _00HL, _00HZ --> _00I0
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01185__00I0 = (v01184__00HL**1)*(v01191__00HZ**-1)
v01185__00I0 = (v01185__00I0*_00H__coeff).reshape((1, 40, 30))

# op _00Hs_power_combination_eval
# LANG: prandtl_loss_factor --> _00Ht
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01165__00Ht = (v01149_prandtl_loss_factor**1)
v01165__00Ht = (v01165__00Ht*_00Hs_coeff).reshape((1, 40, 30))

# op _00Hu_sin_eval
# LANG: phi_distribution --> _00Hv
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01167__00Hv = np.sin(v01136_phi_distribution)

# op _00JW_power_combination_eval
# LANG: _ut --> _00JX
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01265__00JX = (v01196__ut**1)
v01265__00JX = (v01265__00JX*_00JW_coeff).reshape((1, 40, 30))

# op _00OO_power_combination_eval
# LANG: _00ON --> pressure
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01404_pressure = (v01403__00ON**1)
v01404_pressure = (v01404_pressure*_00OO_coeff).reshape((1,))

# op _00Pg expand_scalar_eval
# LANG: Vx --> _00Ph
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01415__00Ph = np.empty((1, 1))
v01415__00Ph.fill(v0917_u.item())

# op _00Pj expand_scalar_eval
# LANG: Vy --> _00Pk
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01417__00Pk = np.empty((1, 1))
v01417__00Pk.fill(v0918_v.item())

# op _00Pl expand_scalar_eval
# LANG: Vz --> _00Pm
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01418__00Pm = np.empty((1, 1))
v01418__00Pm.fill(v0919_w.item())

# op _00RW_power_combination_eval
# LANG: _00RV, _00Rq --> lambda_test
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01480_lambda_test = (v01479__00RV**1)*(v01482__00Rq**1)
v01480_lambda_test = (v01480_lambda_test*_00RW_coeff).reshape((1, 1, 3, 40, 11))

# op _00UB_power_combination_eval
# LANG: _00Uy, _00UA --> _00UC
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01596__00UC = (v01595__00Uy**1)*(v01597__00UA**1)
v01596__00UC = (v01596__00UC*_00UB_coeff).reshape((1, 1, 3, 40, 10))

# op _00UD_bessel_eval
# LANG: _00Su --> _00UE
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01599__00UE=_00UD_bessel_eval(1,v01498__00Su)

# op _00UJ_bessel_eval
# LANG: _00Su --> _00UK
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01601__00UK=_00UJ_bessel_eval(0,v01498__00Su)

# op _00Ul_linear_combination_eval
# LANG: _00Ua, _00Uk --> _00Um
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01583__00Um = _00Ul_constant+1*v01582__00Ua+1*v01587__00Uk

# op _00Ut_power_combination_eval
# LANG: _00Uq, _00Us --> _00Uu
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01592__00Uu = (v01591__00Uq**1)*(v01593__00Us**1)
v01592__00Uu = (v01592__00Uu*_00Ut_coeff).reshape((1, 1, 3, 40, 10))

# op _00db_power_combination_eval
# LANG: _00d8, _00da --> _00dc
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0323__00dc = (v0322__00d8**1)*(v0324__00da**1)
v0323__00dc = (v0323__00dc*_00db_coeff).reshape((1, 40, 100))

# op _00eI_linear_combination_eval
# LANG: _00eB, _00eH --> _00eJ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0379__00eJ = _00eI_constant+1*v0378__00eB+1*v0382__00eH

# op _00ey_power_combination_eval
# LANG: _00bs, _00ex --> _00ez
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0376__00ez = (v0375__00ex**1)*(v0321__00bs**1)
v0376__00ez = (v0376__00ez*_00ey_coeff).reshape((1, 40, 100))

# op _00kG expand_scalar_eval
# LANG: init_obs_x_loc --> _00kH
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0558__00kH = np.empty((1, 1, 1))
v0558__00kH.fill(v0557_init_obs_x_loc.item())

# op _00kI expand_scalar_eval
# LANG: init_obs_y_loc --> _00kJ
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0566__00kJ = np.empty((1, 1, 1))
v0566__00kJ.fill(v0565_init_obs_y_loc.item())

# op _00kR_linear_combination_eval
# LANG: aircraft_x_pos, _00kQ --> _00kS
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0560__00kS = _00kR_constant+1*v0542_aircraft_x_pos+1*v0562__00kQ

# op _00kW_linear_combination_eval
# LANG: aircraft_y_pos, _00kV --> _00kX
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0568__00kX = _00kW_constant+1*v0553_aircraft_y_pos+1*v0563__00kV

# op _0072 expand_scalar_eval
# LANG: dr --> _dr
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0203__dr = np.empty((1, 40, 100))
v0203__dr.fill(v0194_dr.item())

# op _00Hi_power_combination_eval
# LANG: prandtl_loss_factor --> _00Hj
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01159__00Hj = (v01149_prandtl_loss_factor**1)
v01159__00Hj = (v01159__00Hj*_00Hi_coeff).reshape((1, 40, 30))

# op _00Hm_sin_eval
# LANG: phi_distribution --> _00Hn
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01162__00Hn = np.sin(v01136_phi_distribution)

# op _00Hw_power_combination_eval
# LANG: _00Ht, _00Hv --> _00Hx
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01166__00Hx = (v01165__00Ht**1)*(v01167__00Hv**1)
v01166__00Hx = (v01166__00Hx*_00Hw_coeff).reshape((1, 40, 30))

# op _00Hy_cos_eval
# LANG: phi_distribution --> _00Hz
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01169__00Hz = np.cos(v01136_phi_distribution)

# op _00I1_linear_combination_eval
# LANG: _00I0, _axial_inflow_velocity --> _ux_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01177__ux_2 = _00I1_constant+1*v01106__axial_inflow_velocity+1*v01185__00I0

# op _00JO_power_combination_eval
# LANG: Cd --> _00JP
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01258__00JP = (v01139_Cd**1)
v01258__00JP = (v01258__00JP*_00JO_coeff).reshape((1, 40, 30))

# op _00JY_linear_combination_eval
# LANG: _00JX, _tangential_inflow_velocity --> _00JZ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01264__00JZ = _00JY_constant+1*v01116__tangential_inflow_velocity+-1*v01265__00JX

# op _00OQ_power_combination_eval
# LANG: pressure --> _00OR
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01405__00OR = (v01404_pressure**1)
v01405__00OR = (v01405__00OR*_00OQ_coeff).reshape((1,))

# op _00Pi_indexed_passthrough_eval
# LANG: _00Ph, _00Pk, _00Pm --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01416_V_aircraft__temp[i_v01415__00Ph__00Pi_indexed_passthrough_eval] = v01415__00Ph.flatten()
v01416_V_aircraft = v01416_V_aircraft__temp.copy()
v01416_V_aircraft__temp[i_v01417__00Pk__00Pi_indexed_passthrough_eval] = v01417__00Pk.flatten()
v01416_V_aircraft = v01416_V_aircraft__temp.copy()
v01416_V_aircraft__temp[i_v01418__00Pm__00Pi_indexed_passthrough_eval] = v01418__00Pm.flatten()
v01416_V_aircraft = v01416_V_aircraft__temp.copy()

# op _00R__decompose_eval
# LANG: lambda_test --> _00S0
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01565__00S0 = ((v01480_lambda_test.flatten())[src_indices__00S0__00R_]).reshape((1, 1, 3, 40, 10))

# op _00SD_bessel_eval
# LANG: _00Su --> _00SE
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01510__00SE=_00SD_bessel_eval(1,v01498__00Su)

# op _00Sx_bessel_eval
# LANG: _00Su --> _00Sy
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01507__00Sy=_00Sx_bessel_eval(1,v01498__00Su)

# op _00Tc_bessel_eval
# LANG: _00Su --> _00Td
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01529__00Td=_00Tc_bessel_eval(1,v01498__00Su)

# op _00Ti_bessel_eval
# LANG: _00Su --> _00Tj
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01532__00Tj=_00Ti_bessel_eval(0,v01498__00Su)

# op _00UF_power_combination_eval
# LANG: _00UC, _00UE --> _00UG
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01598__00UG = (v01596__00UC**1)*(v01599__00UE**1)
v01598__00UG = (v01598__00UG*_00UF_coeff).reshape((1, 1, 3, 40, 10))

# op _00UL_power_combination_eval
# LANG: _00UK --> _00UM
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01602__00UM = (v01601__00UK**2)
v01602__00UM = (v01602__00UM*_00UL_coeff).reshape((1, 1, 3, 40, 10))

# op _00UN_bessel_eval
# LANG: _00Su --> _00UO
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01604__00UO=_00UN_bessel_eval(1,v01498__00Su)

# op _00UT_bessel_eval
# LANG: _00Su --> _00UU
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01606__00UU=_00UT_bessel_eval(0,v01498__00Su)

# op _00UV_bessel_eval
# LANG: _00Su --> _00UW
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01608__00UW=_00UV_bessel_eval(1,v01498__00Su)

# op _00Uv_linear_combination_eval
# LANG: _00Um, _00Uu --> _00Uw
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01589__00Uw = _00Uv_constant+1*v01583__00Um+1*v01592__00Uu

# op _00dd_power_combination_eval
# LANG: _00dc, prandtl_loss_factor --> _00de
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0325__00de = (v0323__00dc**1)*(v0265_prandtl_loss_factor**1)
v0325__00de = (v0325__00de*_00dd_coeff).reshape((1, 40, 100))

# op _00eK_power_combination_eval
# LANG: _00ez, _00eJ --> _00eL
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0377__00eL = (v0376__00ez**1)*(v0379__00eJ**1)
v0377__00eL = (v0377__00eL*_00eK_coeff).reshape((1, 40, 100))

# op _00kT_linear_combination_eval
# LANG: _00kH, _00kS --> rel_obs_x_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0559_rel_obs_x_pos = _00kT_constant+1*v0558__00kH+-1*v0560__00kS

# op _00kY_linear_combination_eval
# LANG: _00kJ, _00kX --> rel_obs_y_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0567_rel_obs_y_pos = _00kY_constant+1*v0566__00kJ+-1*v0568__00kX

# op _00Ba_power_combination_eval
# LANG: propeller_radius --> _00Bb
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01077__00Bb = (v01008_propeller_radius**1)
v01077__00Bb = (v01077__00Bb*_00Ba_coeff).reshape((1,))

# op _00GL expand_scalar_eval
# LANG: density --> _00GM
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01127_density = v01127_density.reshape((1,))
v01205__00GM = np.empty((1, 40, 30))
v01205__00GM.fill(v01127_density.item())
v01127_density = v01127_density.reshape((1, 1))

# op _00HA_power_combination_eval
# LANG: _00Hx, _00Hz --> _00HB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01168__00HB = (v01166__00Hx**1)*(v01169__00Hz**1)
v01168__00HB = (v01168__00HB*_00HA_coeff).reshape((1, 40, 30))

# op _00HC_power_combination_eval
# LANG: _00H9, _blade_solidity --> _00HD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01171__00HD = (v01105__blade_solidity**1)*(v01174__00H9**1)
v01171__00HD = (v01171__00HD*_00HC_coeff).reshape((1, 40, 30))

# op _00Hk_power_combination_eval
# LANG: _00Hj, _tangential_inflow_velocity --> _00Hl
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01160__00Hl = (v01159__00Hj**1)*(v01116__tangential_inflow_velocity**1)
v01160__00Hl = (v01160__00Hl*_00Hk_coeff).reshape((1, 40, 30))

# op _00Ho_power_combination_eval
# LANG: _00Hn --> _00Hp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01163__00Hp = (v01162__00Hn**2)
v01163__00Hp = (v01163__00Hp*_00Ho_coeff).reshape((1, 40, 30))

# op _00JQ_power_combination_eval
# LANG: _00JP --> _00JR
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01259__00JR = (v01258__00JP**1)
v01259__00JR = (v01259__00JR*_00JQ_coeff).reshape((1, 40, 30))

# op _00JU_power_combination_eval
# LANG: _ux_2 --> _00JV
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01262__00JV = (v01177__ux_2**2)
v01262__00JV = (v01262__00JV*_00JU_coeff).reshape((1, 40, 30))

# op _00J__power_combination_eval
# LANG: _00JZ --> _00K0
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01266__00K0 = (v01264__00JZ**2)
v01266__00K0 = (v01266__00K0*_00J__coeff).reshape((1, 40, 30))

# op _00OS_power_combination_eval
# LANG: temperature, _00OR --> density
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01406_density = (v01405__00OR**1)*(v01401_temperature**-1)
v01406_density = (v01406_density*_00OS_coeff).reshape((1,))

# op _00Pn expand_array_eval
# LANG: V_aircraft --> _00Po
# SHAPES: (1, 3) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01425__00Po = np.einsum('ab,c->abc', v01416_V_aircraft.reshape((1, 3)) ,np.ones((1,))).reshape((1, 3, 1))

# op _00Pt expand_scalar_eval
# LANG: time_vectors --> _00Pu
# SHAPES: (1,) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01431__00Pu = np.empty((1, 3, 1))
v01431__00Pu.fill(v01430_time_vectors.item())

# op _00SF_power_combination_eval
# LANG: _00SE --> _00SG
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01511__00SG = (v01510__00SE**2)
v01511__00SG = (v01511__00SG*_00SF_coeff).reshape((1, 1, 3, 40, 10))

# op _00SH_bessel_eval
# LANG: _00Su --> _00SI
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01513__00SI=_00SH_bessel_eval(1,v01498__00Su)

# op _00SN_bessel_eval
# LANG: _00Su --> _00SO
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01515__00SO=_00SN_bessel_eval(0,v01498__00Su)

# op _00SP_bessel_eval
# LANG: _00Su --> _00SQ
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01517__00SQ=_00SP_bessel_eval(1,v01498__00Su)

# op _00Sv_bessel_eval
# LANG: _00Su --> _00Sw
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01505__00Sw=_00Sv_bessel_eval(0,v01498__00Su)

# op _00Sz_power_combination_eval
# LANG: _00Sy --> _00SA
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01508__00SA = (v01507__00Sy**2)
v01508__00SA = (v01508__00SA*_00Sz_coeff).reshape((1, 1, 3, 40, 10))

# op _00Ta_bessel_eval
# LANG: _00Su --> _00Tb
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01527__00Tb=_00Ta_bessel_eval(0,v01498__00Su)

# op _00Te_power_combination_eval
# LANG: _00Td --> _00Tf
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01530__00Tf = (v01529__00Td**2)
v01530__00Tf = (v01530__00Tf*_00Te_coeff).reshape((1, 1, 3, 40, 10))

# op _00Tk_power_combination_eval
# LANG: _00Tj --> _00Tl
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01533__00Tl = (v01532__00Tj**2)
v01533__00Tl = (v01533__00Tl*_00Tk_coeff).reshape((1, 1, 3, 40, 10))

# op _00Tm_bessel_eval
# LANG: _00Su --> _00Tn
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01535__00Tn=_00Tm_bessel_eval(1,v01498__00Su)

# op _00Ts_bessel_eval
# LANG: _00Su --> _00Tt
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01537__00Tt=_00Ts_bessel_eval(1,v01498__00Su)

# op _00UH_linear_combination_eval
# LANG: _00Uw, _00UG --> _00UI
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01594__00UI = _00UH_constant+1*v01589__00Uw+1*v01598__00UG

# op _00UP_power_combination_eval
# LANG: _00UM, _00UO --> _00UQ
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01603__00UQ = (v01602__00UM**1)*(v01604__00UO**1)
v01603__00UQ = (v01603__00UQ*_00UP_coeff).reshape((1, 1, 3, 40, 10))

# op _00UX_power_combination_eval
# LANG: _00UU, _00UW --> _00UY
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01607__00UY = (v01606__00UU**1)*(v01608__00UW**1)
v01607__00UY = (v01607__00UY*_00UX_coeff).reshape((1, 1, 3, 40, 10))

# op _00UZ_bessel_eval
# LANG: _00Su --> _00U_
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01610__00U_=_00UZ_bessel_eval(1,v01498__00Su)

# op _00V4_bessel_eval
# LANG: _00Su --> _00V5
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01612__00V5=_00V4_bessel_eval(0,v01498__00Su)

# op _00V6_bessel_eval
# LANG: _00Su --> _00V7
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01614__00V7=_00V6_bessel_eval(1,v01498__00Su)

# op _00VM_power_combination_eval
# LANG: _00RG, _00S0 --> _00VN
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01566__00VN = (v01565__00S0**1)*(v01494__00RG**1)
v01566__00VN = (v01566__00VN*_00VM_coeff).reshape((1, 1, 3, 40, 10))

# op _00VW_power_combination_eval
# LANG: _00RG, _00RE --> _00VX
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01560__00VX = (v01494__00RG**1)*(v01500__00RE**1)
v01560__00VX = (v01560__00VX*_00VW_coeff).reshape((1, 1, 3, 40, 10))

# op _00df_power_combination_eval
# LANG: _00de, _dr --> _local_thrust
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0326__local_thrust = (v0325__00de**1)*(v0203__dr**1)
v0326__local_thrust = (v0326__local_thrust*_00df_coeff).reshape((1, 40, 100))

# op _00eM_power_combination_eval
# LANG: _00eL, _chord --> _00eN
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0383__00eN = (v0377__00eL**1)*(v0210__chord**1)
v0383__00eN = (v0383__00eN*_00eM_coeff).reshape((1, 40, 100))

# op _00jp_power_combination_eval
# LANG: altitude --> _00jq
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0516__00jq = (v050_cruise_altitude**1)
v0516__00jq = (v0516__00jq*_00jp_coeff).reshape((1,))

# op _00kC_power_combination_eval
# LANG: _00kA, _00kB --> _00kD
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0556__00kD = (v0546__00kA**1)*(v0552__00kB**1)
v0556__00kD = (v0556__00kD*_00kC_coeff).reshape((1, 1, 1))

# op _00nu reshape_eval
# LANG: rel_obs_x_pos --> _00nv
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0641__00nv = v0559_rel_obs_x_pos.reshape((1, 1))

# op _00nx reshape_eval
# LANG: rel_obs_y_pos --> _00ny
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0644__00ny = v0567_rel_obs_y_pos.reshape((1, 1))

# op _00Bc_linear_combination_eval
# LANG: _00Bb, propeller_radius --> _00Bd
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01076__00Bd = _00Bc_constant+1*v01008_propeller_radius+-1*v01077__00Bb

# op _00HE_linear_combination_eval
# LANG: _00HB, _00HD --> _00HF
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01170__00HF = _00HE_constant+1*v01168__00HB+1*v01171__00HD

# op _00Hq_power_combination_eval
# LANG: _00Hl, _00Hp --> _00Hr
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01161__00Hr = (v01160__00Hl**1)*(v01163__00Hp**1)
v01161__00Hr = (v01161__00Hr*_00Hq_coeff).reshape((1, 40, 30))

# op _00In_power_combination_eval
# LANG: _radius --> _00Io
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01203__00Io = (v01099__radius**1)
v01203__00Io = (v01203__00Io*_00In_coeff).reshape((1, 40, 30))

# op _00JS_power_combination_eval
# LANG: _00GM, _00JR --> _00JT
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01260__00JT = (v01259__00JR**1)*(v01205__00GM**1)
v01260__00JT = (v01260__00JT*_00JS_coeff).reshape((1, 40, 30))

# op _00K1_linear_combination_eval
# LANG: _00JV, _00K0 --> _00K2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01263__00K2 = _00K1_constant+1*v01262__00JV+1*v01266__00K0

# op _00Pq expand_array_eval
# LANG: aircraft_location --> _00Pr
# SHAPES: (3, 1) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01420__00Pr = np.einsum('bc,a->abc', v01419_aircraft_location.reshape((3, 1)) ,np.ones((1,))).reshape((1, 3, 1))

# op _00Px_decompose_eval
# LANG: _00Po --> _00Py, _00PG, _00PN
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01426__00Py = ((v01425__00Po.flatten())[src_indices__00Py__00Px]).reshape((1, 1, 1))
v01427__00PG = ((v01425__00Po.flatten())[src_indices__00PG__00Px]).reshape((1, 1, 1))
v01428__00PN = ((v01425__00Po.flatten())[src_indices__00PN__00Px]).reshape((1, 1, 1))

# op _00Pz_decompose_eval
# LANG: _00Pu --> _00PA, _00PH, _00PO
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01432__00PA = ((v01431__00Pu.flatten())[src_indices__00PA__00Pz]).reshape((1, 1, 1))
v01433__00PH = ((v01431__00Pu.flatten())[src_indices__00PH__00Pz]).reshape((1, 1, 1))
v01434__00PO = ((v01431__00Pu.flatten())[src_indices__00PO__00Pz]).reshape((1, 1, 1))

# op _00Rz expand_scalar_eval
# LANG: density --> _00RA
# SHAPES: (1,) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01557__00RA = np.empty((1, 1, 3, 40, 11))
v01557__00RA.fill(v01406_density.item())

# op _00SB_power_combination_eval
# LANG: _00Sw, _00SA --> _00SC
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01506__00SC = (v01505__00Sw**1)*(v01508__00SA**1)
v01506__00SC = (v01506__00SC*_00SB_coeff).reshape((1, 1, 3, 40, 10))

# op _00SJ_power_combination_eval
# LANG: _00SG, _00SI --> _00SK
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01512__00SK = (v01511__00SG**1)*(v01513__00SI**1)
v01512__00SK = (v01512__00SK*_00SJ_coeff).reshape((1, 1, 3, 40, 10))

# op _00SR_power_combination_eval
# LANG: _00SO, _00SQ --> _00SS
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01516__00SS = (v01515__00SO**1)*(v01517__00SQ**1)
v01516__00SS = (v01516__00SS*_00SR_coeff).reshape((1, 1, 3, 40, 10))

# op _00ST_bessel_eval
# LANG: _00Su --> _00SU
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01519__00SU=_00ST_bessel_eval(0,v01498__00Su)

# op _00SZ_bessel_eval
# LANG: _00Su --> _00S_
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01521__00S_=_00SZ_bessel_eval(1,v01498__00Su)

# op _00T0_bessel_eval
# LANG: _00Su --> _00T1
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01523__00T1=_00T0_bessel_eval(0,v01498__00Su)

# op _00TE_bessel_eval
# LANG: _00Su --> _00TF
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01544__00TF=_00TE_bessel_eval(1,v01498__00Su)

# op _00Tg_power_combination_eval
# LANG: _00Tb, _00Tf --> _00Th
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01528__00Th = (v01527__00Tb**1)*(v01530__00Tf**1)
v01528__00Th = (v01528__00Th*_00Tg_coeff).reshape((1, 1, 3, 40, 10))

# op _00To_power_combination_eval
# LANG: _00Tl, _00Tn --> _00Tp
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01534__00Tp = (v01533__00Tl**1)*(v01535__00Tn**1)
v01534__00Tp = (v01534__00Tp*_00To_coeff).reshape((1, 1, 3, 40, 10))

# op _00Tu_power_combination_eval
# LANG: _00Tt --> _00Tv
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01538__00Tv = (v01537__00Tt**2)
v01538__00Tv = (v01538__00Tv*_00Tu_coeff).reshape((1, 1, 3, 40, 10))

# op _00Tw_bessel_eval
# LANG: _00Su --> _00Tx
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01540__00Tx=_00Tw_bessel_eval(1,v01498__00Su)

# op _00UR_linear_combination_eval
# LANG: _00UI, _00UQ --> _00US
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01600__00US = _00UR_constant+1*v01594__00UI+1*v01603__00UQ

# op _00V0_power_combination_eval
# LANG: _00UY, _00U_ --> _00V1
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01609__00V1 = (v01607__00UY**1)*(v01610__00U_**1)
v01609__00V1 = (v01609__00V1*_00V0_coeff).reshape((1, 1, 3, 40, 10))

# op _00V8_power_combination_eval
# LANG: _00V5, _00V7 --> _00V9
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01613__00V9 = (v01612__00V5**1)*(v01614__00V7**1)
v01613__00V9 = (v01613__00V9*_00V8_coeff).reshape((1, 1, 3, 40, 10))

# op _00VO_power_combination_eval
# LANG: _00RI, _00VN --> _00VP
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01567__00VP = (v01566__00VN**1)*(v01503__00RI**1)
v01567__00VP = (v01567__00VP*_00VO_coeff).reshape((1, 1, 3, 40, 10))

# op _00VY_power_combination_eval
# LANG: _00RI, _00VX --> _00VZ
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01561__00VZ = (v01560__00VX**1)*(v01503__00RI**1)
v01561__00VZ = (v01561__00VZ*_00VY_coeff).reshape((1, 1, 3, 40, 10))

# op _00Va_bessel_eval
# LANG: _00Su --> _00Vb
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01616__00Vb=_00Va_bessel_eval(1,v01498__00Su)

# op _00Vi_bessel_eval
# LANG: _00Su --> _00Vj
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01620__00Vj=_00Vi_bessel_eval(1,v01498__00Su)

# op _00eO_power_combination_eval
# LANG: _00eN, _dr --> _dD
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0384__dD = (v0383__00eN**1)*(v0203__dr**1)
v0384__dD = (v0384__dD*_00eO_coeff).reshape((1, 40, 100))

# op _00hN_power_combination_eval
# LANG: _local_thrust --> _dT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0327__dT = (v0326__local_thrust**1)
v0327__dT = (v0327__dT*_00hN_coeff).reshape((1, 40, 100))

# op _00jr_linear_combination_eval
# LANG: _00jq --> _00js
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0517__00js = _00jr_constant+-1*v0516__00jq

# op _00kE_linear_combination_eval
# LANG: _00kz, _00kD --> aircraft_z_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0555_aircraft_z_pos = _00kE_constant+1*v0541__00kz+1*v0556__00kD

# op _00nF_power_combination_eval
# LANG: _00nv --> _00nG
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0642__00nG = (v0641__00nv**2)
v0642__00nG = (v0642__00nG*_00nF_coeff).reshape((1, 1))

# op _00nH_power_combination_eval
# LANG: _00ny --> _00nI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0645__00nI = (v0644__00ny**2)
v0645__00nI = (v0645__00nI*_00nH_coeff).reshape((1, 1))

# op _00Be_power_combination_eval
# LANG: _00Bd --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01078_dr = (v01076__00Bd**1)
v01078_dr = (v01078_dr*_00Be_coeff).reshape((1,))

# op _00HG_power_combination_eval
# LANG: _00Hr, _00HF --> _ux
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01164__ux = (v01161__00Hr**1)*(v01170__00HF**-1)
v01164__ux = (v01164__ux*_00HG_coeff).reshape((1, 40, 30))

# op _00Ip_power_combination_eval
# LANG: _00Io, _00GM --> _00Iq
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01204__00Iq = (v01203__00Io**1)*(v01205__00GM**1)
v01204__00Iq = (v01204__00Iq*_00Ip_coeff).reshape((1, 40, 30))

# op _00K3_power_combination_eval
# LANG: _00JT, _00K2 --> _00K4
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01261__00K4 = (v01260__00JT**1)*(v01263__00K2**1)
v01261__00K4 = (v01261__00K4*_00K3_coeff).reshape((1, 40, 30))

# op _00NB_power_combination_eval
# LANG: propeller_radius --> _00NC
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01367__00NC = (v01363_propeller_radius**1)
v01367__00NC = (v01367__00NC*_00NB_coeff).reshape((1,))

# op _00PB_power_combination_eval
# LANG: _00Py, _00PA --> _00PC
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01429__00PC = (v01426__00Py**1)*(v01432__00PA**1)
v01429__00PC = (v01429__00PC*_00PB_coeff).reshape((1, 1, 1))

# op _00PI_power_combination_eval
# LANG: _00PG, _00PH --> _00PJ
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01436__00PJ = (v01427__00PG**1)*(v01433__00PH**1)
v01436__00PJ = (v01436__00PJ*_00PI_coeff).reshape((1, 1, 1))

# op _00P_ expand_array_eval
# LANG: rotor_disk_origin --> _00Q0
# SHAPES: (3,) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((3,))
v01443__00Q0 = np.einsum('b,ac->abc', v010_rotor_disk_origin.reshape((3,)) ,np.ones((1, 1))).reshape((1, 3, 1))
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((1, 3))

# op _00Pv_decompose_eval
# LANG: _00Pr --> _00Pw, _00PF, _00PM
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01421__00Pw = ((v01420__00Pr.flatten())[src_indices__00Pw__00Pv]).reshape((1, 1, 1))
v01422__00PF = ((v01420__00Pr.flatten())[src_indices__00PF__00Pv]).reshape((1, 1, 1))
v01423__00PM = ((v01420__00Pr.flatten())[src_indices__00PM__00Pv]).reshape((1, 1, 1))

# op _00RN_decompose_eval
# LANG: _00RA --> _00RO
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01558__00RO = ((v01557__00RA.flatten())[src_indices__00RO__00RN]).reshape((1, 1, 3, 40, 10))

# op _00SL_linear_combination_eval
# LANG: _00SC, _00SK --> _00SM
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01509__00SM = _00SL_constant+1*v01506__00SC+-1*v01512__00SK

# op _00SV_power_combination_eval
# LANG: _00SS, _00SU --> _00SW
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01518__00SW = (v01516__00SS**1)*(v01519__00SU**1)
v01518__00SW = (v01518__00SW*_00SV_coeff).reshape((1, 1, 3, 40, 10))

# op _00T2_power_combination_eval
# LANG: _00S_, _00T1 --> _00T3
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01522__00T3 = (v01521__00S_**1)*(v01523__00T1**1)
v01522__00T3 = (v01522__00T3*_00T2_coeff).reshape((1, 1, 3, 40, 10))

# op _00T4_bessel_eval
# LANG: _00Su --> _00T5
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01525__00T5=_00T4_bessel_eval(1,v01498__00Su)

# op _00TC_bessel_eval
# LANG: _00Su --> _00TD
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01542__00TD=_00TC_bessel_eval(0,v01498__00Su)

# op _00TG_power_combination_eval
# LANG: _00TF --> _00TH
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01545__00TH = (v01544__00TF**2)
v01545__00TH = (v01545__00TH*_00TG_coeff).reshape((1, 1, 3, 40, 10))

# op _00TO_bessel_eval
# LANG: _00Su --> _00TP
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01547__00TP=_00TO_bessel_eval(1,v01498__00Su)

# op _00TQ_bessel_eval
# LANG: _00Su --> _00TR
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01549__00TR=_00TQ_bessel_eval(0,v01498__00Su)

# op _00TW_bessel_eval
# LANG: _00Su --> _00TX
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01552__00TX=_00TW_bessel_eval(0,v01498__00Su)

# op _00TY_bessel_eval
# LANG: _00Su --> _00TZ
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01554__00TZ=_00TY_bessel_eval(1,v01498__00Su)

# op _00Tq_linear_combination_eval
# LANG: _00Th, _00Tp --> _00Tr
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01531__00Tr = _00Tq_constant+1*v01528__00Th+1*v01534__00Tp

# op _00Ty_power_combination_eval
# LANG: _00Tv, _00Tx --> _00Tz
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01539__00Tz = (v01538__00Tv**1)*(v01540__00Tx**1)
v01539__00Tz = (v01539__00Tz*_00Ty_coeff).reshape((1, 1, 3, 40, 10))

# op _00V2_linear_combination_eval
# LANG: _00US, _00V1 --> _00V3
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01605__00V3 = _00V2_constant+1*v01600__00US+-1*v01609__00V1

# op _00VA_bessel_eval
# LANG: _00Su --> _00VB
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01629__00VB=_00VA_bessel_eval(0,v01498__00Su)

# op _00VC_bessel_eval
# LANG: _00Su --> _00VD
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01631__00VD=_00VC_bessel_eval(1,v01498__00Su)

# op _00VQ_power_combination_eval
# LANG: _00Si, _00VP --> _00VR
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01568__00VR = (v01567__00VP**1)*(v01488__00Si**-1)
v01568__00VR = (v01568__00VR*_00VQ_coeff).reshape((1, 1, 3, 40, 10))

# op _00V__linear_combination_eval
# LANG: _00VZ --> _00W0
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01562__00W0 = _00V__constant+1*v01561__00VZ

# op _00Vc_power_combination_eval
# LANG: _00V9, _00Vb --> _00Vd
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01615__00Vd = (v01613__00V9**1)*(v01616__00Vb**1)
v01615__00Vd = (v01615__00Vd*_00Vc_coeff).reshape((1, 1, 3, 40, 10))

# op _00Vg_bessel_eval
# LANG: _00Su --> _00Vh
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01618__00Vh=_00Vg_bessel_eval(1,v01498__00Su)

# op _00Vk_power_combination_eval
# LANG: _00Vj --> _00Vl
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01621__00Vl = (v01620__00Vj**2)
v01621__00Vl = (v01621__00Vl*_00Vk_coeff).reshape((1, 1, 3, 40, 10))

# op _00Vs_bessel_eval
# LANG: _00Su --> _00Vt
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01624__00Vt=_00Vs_bessel_eval(1,v01498__00Su)

# op _00Vu_bessel_eval
# LANG: _00Su --> _00Vv
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01626__00Vv=_00Vu_bessel_eval(0,v01498__00Su)

# op _00ic_power_combination_eval
# LANG: Vx --> _00id
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0480__00id = (v028_u**2)
v0480__00id = (v0480__00id*_00ic_coeff).reshape((1,))

# op _00ie_power_combination_eval
# LANG: Vy --> _00if
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0482__00if = (v033_v**2)
v0482__00if = (v0482__00if*_00ie_coeff).reshape((1,))

# op _00jt_power_combination_eval
# LANG: _00js --> _00ju
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0518__00ju = (v0517__00js**1)
v0518__00ju = (v0518__00ju*_00jt_coeff).reshape((1,))

# op _00kK expand_scalar_eval
# LANG: init_obs_z_loc --> _00kL
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0570__00kL = np.empty((1, 1, 1))
v0570__00kL.fill(v0569_init_obs_z_loc.item())

# op _00l0_linear_combination_eval
# LANG: aircraft_z_pos, _00k_ --> _00l1
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0572__00l1 = _00l0_constant+1*v0555_aircraft_z_pos+1*v0564__00k_

# op _00lA expand_array_eval
# LANG: _dT --> _00lB
# SHAPES: (1, 40, 100) --> (1, 2, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0589__00lB = np.einsum('acd,b->abcd', v0327__dT.reshape((1, 40, 100)) ,np.ones((2,))).reshape((1, 2, 40, 100))

# op _00lx expand_array_eval
# LANG: _dD --> _00ly
# SHAPES: (1, 40, 100) --> (1, 2, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0587__00ly = np.einsum('acd,b->abcd', v0384__dD.reshape((1, 40, 100)) ,np.ones((2,))).reshape((1, 2, 40, 100))

# op _00nJ_linear_combination_eval
# LANG: _00nG, _00nI --> _00nK
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0643__00nK = _00nJ_constant+1*v0642__00nG+1*v0645__00nI

# op _00Cm expand_scalar_eval
# LANG: dr --> _dr
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01087__dr = np.empty((1, 40, 30))
v01087__dr.fill(v01078_dr.item())

# op _00Ir_power_combination_eval
# LANG: _ux, _00Iq --> _00Is
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01206__00Is = (v01204__00Iq**1)*(v01164__ux**1)
v01206__00Is = (v01206__00Is*_00Ir_coeff).reshape((1, 40, 30))

# op _00It_linear_combination_eval
# LANG: _ux, _axial_inflow_velocity --> _00Iu
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01208__00Iu = _00It_constant+1*v01164__ux+-1*v01106__axial_inflow_velocity

# op _00K5_power_combination_eval
# LANG: _00K4, _chord --> _00K6
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01267__00K6 = (v01261__00K4**1)*(v01094__chord**1)
v01267__00K6 = (v01267__00K6*_00K5_coeff).reshape((1, 40, 30))

# op _00ND_power_combination_eval
# LANG: _00NC --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01368_dr = (v01367__00NC**1)
v01368_dr = (v01368_dr*_00ND_coeff).reshape((1,))

# op _00PD_linear_combination_eval
# LANG: _00Pw, _00PC --> aircraft_x_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01424_aircraft_x_pos = _00PD_constant+1*v01421__00Pw+1*v01429__00PC

# op _00PK_linear_combination_eval
# LANG: _00PF, _00PJ --> aircraft_y_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01435_aircraft_y_pos = _00PK_constant+1*v01422__00PF+1*v01436__00PJ

# op _00PP_power_combination_eval
# LANG: _00PN, _00PO --> _00PQ
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01438__00PQ = (v01428__00PN**1)*(v01434__00PO**1)
v01438__00PQ = (v01438__00PQ*_00PP_coeff).reshape((1, 1, 1))

# op _00Q1_decompose_eval
# LANG: _00Q0 --> _00Q2, _00Q7, _00Qc
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01444__00Q2 = ((v01443__00Q0.flatten())[src_indices__00Q2__00Q1]).reshape((1, 1, 1))
v01445__00Q7 = ((v01443__00Q0.flatten())[src_indices__00Q7__00Q1]).reshape((1, 1, 1))
v01446__00Qc = ((v01443__00Q0.flatten())[src_indices__00Qc__00Q1]).reshape((1, 1, 1))

# op _00SX_linear_combination_eval
# LANG: _00SM, _00SW --> _00SY
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01514__00SY = _00SX_constant+1*v01509__00SM+1*v01518__00SW

# op _00T6_power_combination_eval
# LANG: _00T3, _00T5 --> _00T7
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01524__00T7 = (v01522__00T3**1)*(v01525__00T5**1)
v01524__00T7 = (v01524__00T7*_00T6_coeff).reshape((1, 1, 3, 40, 10))

# op _00TA_linear_combination_eval
# LANG: _00Tr, _00Tz --> _00TB
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01536__00TB = _00TA_constant+1*v01531__00Tr+-1*v01539__00Tz

# op _00TI_power_combination_eval
# LANG: _00TD, _00TH --> _00TJ
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01543__00TJ = (v01542__00TD**1)*(v01545__00TH**1)
v01543__00TJ = (v01543__00TJ*_00TI_coeff).reshape((1, 1, 3, 40, 10))

# op _00TS_linear_combination_eval
# LANG: _00TP, _00TR --> _00TT
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01548__00TT = _00TS_constant+1*v01547__00TP+1*v01549__00TR

# op _00T__linear_combination_eval
# LANG: _00TX, _00TZ --> _00U0
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01553__00U0 = _00T__constant+1*v01552__00TX+-1*v01554__00TZ

# op _00VE_linear_combination_eval
# LANG: _00VB, _00VD --> _00VF
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01630__00VF = _00VE_constant+1*v01629__00VB+-1*v01631__00VD

# op _00VS_power_combination_eval
# LANG: _00VR --> _00VT
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01569__00VT = (v01568__00VR**1)
v01569__00VT = (v01569__00VT*_00VS_coeff).reshape((1, 1, 3, 40, 10))

# op _00Ve_linear_combination_eval
# LANG: _00V3, _00Vd --> _00Vf
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01611__00Vf = _00Ve_constant+1*v01605__00V3+-1*v01615__00Vd

# op _00Vm_power_combination_eval
# LANG: _00Vh, _00Vl --> _00Vn
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01619__00Vn = (v01618__00Vh**1)*(v01621__00Vl**1)
v01619__00Vn = (v01619__00Vn*_00Vm_coeff).reshape((1, 1, 3, 40, 10))

# op _00Vw_linear_combination_eval
# LANG: _00Vt, _00Vv --> _00Vx
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01625__00Vx = _00Vw_constant+1*v01624__00Vt+1*v01626__00Vv

# op _00W1_power_combination_eval
# LANG: _00RO, _00W0 --> _00W2
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01559__00W2 = (v01558__00RO**1)*(v01562__00W0**1)
v01559__00W2 = (v01559__00W2*_00W1_coeff).reshape((1, 1, 3, 40, 10))

# op _00ig_linear_combination_eval
# LANG: _00id, _00if --> _00ih
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0481__00ih = _00ig_constant+1*v0480__00id+1*v0482__00if

# op _00ii_power_combination_eval
# LANG: Vz --> _00ij
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0484__00ij = (v037_w**2)
v0484__00ij = (v0484__00ij*_00ii_coeff).reshape((1,))

# op _00jv_linear_combination_eval
# LANG: _00ju --> temperature
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0519_temperature = _00jv_constant+1*v0518__00ju

# op _00l2_linear_combination_eval
# LANG: _00kL, _00l1 --> rel_obs_z_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0571_rel_obs_z_pos = _00l2_constant+1*v0570__00kL+-1*v0572__00l1

# op _00lC_single_tensor_sum_with_axis_eval
# LANG: _00ly --> aaa
# SHAPES: (1, 2, 40, 100) --> (1, 2, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0588_aaa = np.sum(v0587__00ly, axis = (2,)).reshape((1, 2, 100))

# op _00lE_single_tensor_sum_with_axis_eval
# LANG: _00lB --> bbb
# SHAPES: (1, 2, 40, 100) --> (1, 2, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0590_bbb = np.sum(v0589__00lB, axis = (2,)).reshape((1, 2, 100))

# op _00lL_sin_eval
# LANG: n_theta_prod --> _00lM
# SHAPES: (11, 100) --> (11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0600__00lM = np.sin(v0593_n_theta_prod)

# op _00nL_linear_combination_eval
# LANG: _00nK --> _00nM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0646__00nM = _00nL_constant+1*v0643__00nK

# op _00Iv_power_combination_eval
# LANG: _00Is, _00Iu --> _00Iw
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01207__00Iw = (v01206__00Is**1)*(v01208__00Iu**1)
v01207__00Iw = (v01207__00Iw*_00Iv_coeff).reshape((1, 40, 30))

# op _00K7_power_combination_eval
# LANG: _00K6, _dr --> _dD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01268__dD = (v01267__00K6**1)*(v01087__dr**1)
v01268__dD = (v01268__dD*_00K7_coeff).reshape((1, 40, 30))

# op _00PR_linear_combination_eval
# LANG: _00PM, _00PQ --> aircraft_z_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01437_aircraft_z_pos = _00PR_constant+1*v01423__00PM+1*v01438__00PQ

# op _00PT expand_scalar_eval
# LANG: init_obs_x_loc --> _00PU
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01440__00PU = np.empty((1, 1, 1))
v01440__00PU.fill(v01439_init_obs_x_loc.item())

# op _00PV expand_scalar_eval
# LANG: init_obs_y_loc --> _00PW
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01448__00PW = np.empty((1, 1, 1))
v01448__00PW.fill(v01447_init_obs_y_loc.item())

# op _00Q3_linear_combination_eval
# LANG: aircraft_x_pos, _00Q2 --> _00Q4
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01442__00Q4 = _00Q3_constant+1*v01424_aircraft_x_pos+1*v01444__00Q2

# op _00Q8_linear_combination_eval
# LANG: aircraft_y_pos, _00Q7 --> _00Q9
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01450__00Q9 = _00Q8_constant+1*v01435_aircraft_y_pos+1*v01445__00Q7

# op _00Rb expand_scalar_eval
# LANG: dr --> _00Rc
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01476__00Rc = np.empty((1, 40, 30))
v01476__00Rc.fill(v01368_dr.item())

# op _00T8_linear_combination_eval
# LANG: _00SY, _00T7 --> _00T9
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01520__00T9 = _00T8_constant+1*v01514__00SY+-1*v01524__00T7

# op _00TK_linear_combination_eval
# LANG: _00TB, _00TJ --> _00TL
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01541__00TL = _00TK_constant+1*v01536__00TB+-1*v01543__00TJ

# op _00TU_power_combination_eval
# LANG: _00TT --> _00TV
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01550__00TV = (v01548__00TT**2)
v01550__00TV = (v01550__00TV*_00TU_coeff).reshape((1, 1, 3, 40, 10))

# op _00U1_power_combination_eval
# LANG: _00U0 --> _00U2
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01555__00U2 = (v01553__00U0**2)
v01555__00U2 = (v01555__00U2*_00U1_coeff).reshape((1, 1, 3, 40, 10))

# op _00VG_power_combination_eval
# LANG: _00VF --> _00VH
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01632__00VH = (v01630__00VF**2)
v01632__00VH = (v01632__00VH*_00VG_coeff).reshape((1, 1, 3, 40, 10))

# op _00VU_power_combination_eval
# LANG: _00VT --> _00VV
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01570__00VV = (v01569__00VT**1)
v01570__00VV = (v01570__00VV*_00VU_coeff).reshape((1, 1, 3, 40, 10))

# op _00Vo_linear_combination_eval
# LANG: _00Vf, _00Vn --> _00Vp
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01617__00Vp = _00Vo_constant+1*v01611__00Vf+1*v01619__00Vn

# op _00Vy_power_combination_eval
# LANG: _00Vx --> _00Vz
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01627__00Vz = (v01625__00Vx**2)
v01627__00Vz = (v01627__00Vz*_00Vy_coeff).reshape((1, 1, 3, 40, 10))

# op _00W3_power_combination_eval
# LANG: _00RM, _00W2 --> _00W4
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01563__00W4 = (v01559__00W2**1)*(v01497__00RM**1)
v01563__00W4 = (v01563__00W4*_00W3_coeff).reshape((1, 1, 3, 40, 10))

# op _00ik_linear_combination_eval
# LANG: _00ih, _00ij --> _00il
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0483__00il = _00ik_constant+1*v0481__00ih+1*v0484__00ij

# op _00jT_power_combination_eval
# LANG: temperature --> _00jU
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0531__00jU = (v0519_temperature**1)
v0531__00jU = (v0531__00jU*_00jT_coeff).reshape((1,))

# op _00lH_cos_eval
# LANG: n_theta_prod --> _00lI
# SHAPES: (11, 100) --> (11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0594__00lI = np.cos(v0593_n_theta_prod)

# op _00lN expand_array_eval
# LANG: _00lM --> _00lO
# SHAPES: (11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0601__00lO = np.einsum('cd,ab->abcd', v0600__00lM.reshape((11, 100)) ,np.ones((1, 2))).reshape((1, 2, 11, 100))

# op _00lX expand_array_eval
# LANG: bbb --> _00lY
# SHAPES: (1, 2, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0598__00lY = np.einsum('abd,c->abcd', v0590_bbb.reshape((1, 2, 100)) ,np.ones((11,))).reshape((1, 2, 11, 100))

# op _00m2 expand_array_eval
# LANG: aaa --> _00m3
# SHAPES: (1, 2, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0603__00m3 = np.einsum('abd,c->abcd', v0588_aaa.reshape((1, 2, 100)) ,np.ones((11,))).reshape((1, 2, 11, 100))

# op _00nA reshape_eval
# LANG: rel_obs_z_pos --> _00nB
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0639__00nB = v0571_rel_obs_z_pos.reshape((1, 1))

# op _00nN_power_combination_eval
# LANG: _00nM --> _00nO
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0647__00nO = (v0646__00nM**0.5)
v0647__00nO = (v0647__00nO*_00nN_coeff).reshape((1, 1))

# op _00Ix_power_combination_eval
# LANG: _00Iw, prandtl_loss_factor --> _00Iy
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01209__00Iy = (v01207__00Iw**1)*(v01149_prandtl_loss_factor**1)
v01209__00Iy = (v01209__00Iy*_00Ix_coeff).reshape((1, 40, 30))

# op _00PX expand_scalar_eval
# LANG: init_obs_z_loc --> _00PY
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01452__00PY = np.empty((1, 1, 1))
v01452__00PY.fill(v01451_init_obs_z_loc.item())

# op _00Q5_linear_combination_eval
# LANG: _00PU, _00Q4 --> rel_obs_x_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01441_rel_obs_x_pos = _00Q5_constant+1*v01440__00PU+-1*v01442__00Q4

# op _00Qa_linear_combination_eval
# LANG: _00PW, _00Q9 --> rel_obs_y_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01449_rel_obs_y_pos = _00Qa_constant+1*v01448__00PW+-1*v01450__00Q9

# op _00Qd_linear_combination_eval
# LANG: aircraft_z_pos, _00Qc --> _00Qe
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01454__00Qe = _00Qd_constant+1*v01437_aircraft_z_pos+1*v01446__00Qc

# op _00Rd_power_combination_eval
# LANG: _00Rc, _dD --> bbb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01475_bbb = (v01268__dD**1)*(v01476__00Rc**-1)
v01475_bbb = (v01475_bbb*_00Rd_coeff).reshape((1, 40, 30))

# op _00TM_linear_combination_eval
# LANG: _00T9, _00TL --> _00TN
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01526__00TN = _00TM_constant+1*v01520__00T9+-1*v01541__00TL

# op _00U3_linear_combination_eval
# LANG: _00TV, _00U2 --> _00U4
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01551__00U4 = _00U3_constant+1*v01550__00TV+1*v01555__00U2

# op _00VI_linear_combination_eval
# LANG: _00Vz, _00VH --> _00VJ
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01628__00VJ = _00VI_constant+1*v01627__00Vz+1*v01632__00VH

# op _00Vq_linear_combination_eval
# LANG: _00Vp --> _00Vr
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01622__00Vr = _00Vq_constant+-1*v01617__00Vp

# op _00W5_power_combination_eval
# LANG: _00W4, _00VV --> _00W6
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01564__00W6 = (v01563__00W4**1)*(v01570__00VV**1)
v01564__00W6 = (v01564__00W6*_00W5_coeff).reshape((1, 1, 3, 40, 10))

# op _00im_power_combination_eval
# LANG: _00il --> _00in
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0485__00in = (v0483__00il**0.5)
v0485__00in = (v0485__00in*_00im_coeff).reshape((1,))

# op _00jV_power_combination_eval
# LANG: _00jU --> speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0532_speed_of_sound = (v0531__00jU**0.5)
v0532_speed_of_sound = (v0532_speed_of_sound*_00jV_coeff).reshape((1,))

# op _00l4_power_combination_eval
# LANG: rel_obs_x_pos --> _00l5
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0573__00l5 = (v0559_rel_obs_x_pos**2)
v0573__00l5 = (v0573__00l5*_00l4_coeff).reshape((1, 1, 1))

# op _00l6_power_combination_eval
# LANG: rel_obs_y_pos --> _00l7
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0575__00l7 = (v0567_rel_obs_y_pos**2)
v0575__00l7 = (v0575__00l7*_00l6_coeff).reshape((1, 1, 1))

# op _00lJ expand_array_eval
# LANG: _00lI --> _00lK
# SHAPES: (11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0595__00lK = np.einsum('cd,ab->abcd', v0594__00lI.reshape((11, 100)) ,np.ones((1, 2))).reshape((1, 2, 11, 100))

# op _00lP expand_array_eval
# LANG: bbb --> _00lQ
# SHAPES: (1, 2, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0591__00lQ = np.einsum('abd,c->abcd', v0590_bbb.reshape((1, 2, 100)) ,np.ones((11,))).reshape((1, 2, 11, 100))

# op _00lT expand_array_eval
# LANG: aaa --> _00lU
# SHAPES: (1, 2, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0596__00lU = np.einsum('abd,c->abcd', v0588_aaa.reshape((1, 2, 100)) ,np.ones((11,))).reshape((1, 2, 11, 100))

# op _00lZ_power_combination_eval
# LANG: _00lY, _00lO --> _00l_
# SHAPES: (1, 2, 11, 100), (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0599__00l_ = (v0598__00lY**1)*(v0601__00lO**1)
v0599__00l_ = (v0599__00l_*_00lZ_coeff).reshape((1, 2, 11, 100))

# op _00m4_power_combination_eval
# LANG: _00lO, _00m3 --> _00m5
# SHAPES: (1, 2, 11, 100), (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0604__00m5 = (v0603__00m3**1)*(v0601__00lO**1)
v0604__00m5 = (v0604__00m5*_00m4_coeff).reshape((1, 2, 11, 100))

# op _00nP_power_combination_eval
# LANG: _00nB, _00nO --> _00nQ
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0640__00nQ = (v0639__00nB**1)*(v0647__00nO**-1)
v0640__00nQ = (v0640__00nQ*_00nP_coeff).reshape((1, 1))

# op _00nl reshape_eval
# LANG: rpm --> _00nm
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0651__00nm = v0162_rpm.reshape((1,))

# op _00Iz_power_combination_eval
# LANG: _00Iy, _dr --> _local_thrust
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01210__local_thrust = (v01209__00Iy**1)*(v01087__dr**1)
v01210__local_thrust = (v01210__local_thrust*_00Iz_coeff).reshape((1, 40, 30))

# op _00Qf_linear_combination_eval
# LANG: _00PY, _00Qe --> rel_obs_z_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01453_rel_obs_z_pos = _00Qf_constant+1*v01452__00PY+-1*v01454__00Qe

# op _00Qh_power_combination_eval
# LANG: rel_obs_x_pos --> _00Qi
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01455__00Qi = (v01441_rel_obs_x_pos**2)
v01455__00Qi = (v01455__00Qi*_00Qh_coeff).reshape((1, 1, 1))

# op _00Qj_power_combination_eval
# LANG: rel_obs_y_pos --> _00Qk
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01457__00Qk = (v01449_rel_obs_y_pos**2)
v01457__00Qk = (v01457__00Qk*_00Qj_coeff).reshape((1, 1, 1))

# op _00RY_decompose_eval
# LANG: _00RV --> _00RZ
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01573__00RZ = ((v01479__00RV.flatten())[src_indices__00RZ__00RY]).reshape((1, 1, 3, 40, 10))

# op _00Rj_decompose_eval
# LANG: bbb --> _00Rk
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01575__00Rk = ((v01475_bbb.flatten())[src_indices__00Rk__00Rj]).reshape((1, 40, 1))

# op _00U5_power_combination_eval
# LANG: _00TN, _00U4 --> _00U6
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01546__00U6 = (v01526__00TN**1)*(v01551__00U4**-1)
v01546__00U6 = (v01546__00U6*_00U5_coeff).reshape((1, 1, 3, 40, 10))

# op _00VK_power_combination_eval
# LANG: _00Vr, _00VJ --> _00VL
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01623__00VL = (v01622__00Vr**1)*(v01628__00VJ**-1)
v01623__00VL = (v01623__00VL*_00VK_coeff).reshape((1, 1, 3, 40, 10))

# op _00W7_power_combination_eval
# LANG: _00W6 --> _00W8
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01571__00W8 = (v01564__00W6**1)
v01571__00W8 = (v01571__00W8*_00W7_coeff).reshape((1, 1, 3, 40, 10))

# op _00io_power_combination_eval
# LANG: _00in, speed_of_sound --> mach_number
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0486_mach_number = (v0485__00in**1)*(v0532_speed_of_sound**-1)
v0486_mach_number = (v0486_mach_number*_00io_coeff).reshape((1,))

# op _00l8_linear_combination_eval
# LANG: _00l5, _00l7 --> _00l9
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0574__00l9 = _00l8_constant+1*v0573__00l5+1*v0575__00l7

# op _00lR_power_combination_eval
# LANG: _00lQ, _00lK --> aT_integrand
# SHAPES: (1, 2, 11, 100), (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0592_aT_integrand = (v0591__00lQ**1)*(v0595__00lK**1)
v0592_aT_integrand = (v0592_aT_integrand*_00lR_coeff).reshape((1, 2, 11, 100))

# op _00lV_power_combination_eval
# LANG: _00lK, _00lU --> aD_integrand
# SHAPES: (1, 2, 11, 100), (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0597_aD_integrand = (v0596__00lU**1)*(v0595__00lK**1)
v0597_aD_integrand = (v0597_aD_integrand*_00lV_coeff).reshape((1, 2, 11, 100))

# op _00la_power_combination_eval
# LANG: rel_obs_z_pos --> _00lb
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0577__00lb = (v0571_rel_obs_z_pos**2)
v0577__00lb = (v0577__00lb*_00la_coeff).reshape((1, 1, 1))

# op _00m0_power_combination_eval
# LANG: _00l_ --> bT_integrand
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0602_bT_integrand = (v0599__00l_**1)
v0602_bT_integrand = (v0602_bT_integrand*_00m0_coeff).reshape((1, 2, 11, 100))

# op _00m6_power_combination_eval
# LANG: _00m5 --> bD_integrand
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0605_bD_integrand = (v0604__00m5**1)
v0605_bD_integrand = (v0605_bD_integrand*_00m6_coeff).reshape((1, 2, 11, 100))

# op _00nR_arctan_eval
# LANG: _00nQ --> dummy
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0648_dummy = np.arctan(v0640__00nQ)

# op _00nn_power_combination_eval
# LANG: _00nm --> _00no
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0652__00no = (v0651__00nm**1)
v0652__00no = (v0652__00no*_00nn_coeff).reshape((1,))

# op _00N6_power_combination_eval
# LANG: _local_thrust --> _dT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01211__dT = (v01210__local_thrust**1)
v01211__dT = (v01211__dT*_00N6_coeff).reshape((1, 40, 30))

# op _00Ql_linear_combination_eval
# LANG: _00Qi, _00Qk --> _00Qm
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01456__00Qm = _00Ql_constant+1*v01455__00Qi+1*v01457__00Qk

# op _00Qn_power_combination_eval
# LANG: rel_obs_z_pos --> _00Qo
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01459__00Qo = (v01453_rel_obs_z_pos**2)
v01459__00Qo = (v01459__00Qo*_00Qn_coeff).reshape((1, 1, 1))

# op _00R7 expand_scalar_eval
# LANG: dr --> _00R8
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01474__00R8 = np.empty((1, 40, 30))
v01474__00R8.fill(v01368_dr.item())

# op _00Rl reshape_eval
# LANG: _00Rk --> _00Rm
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01576__00Rm = v01575__00Rk.reshape((1, 40))

# op _00W9_power_combination_eval
# LANG: _00U6, _00W8 --> _00Wa
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01556__00Wa = (v01546__00U6**1)*(v01571__00W8**1)
v01556__00Wa = (v01556__00Wa*_00W9_coeff).reshape((1, 1, 3, 40, 10))

# op _00Wb_power_combination_eval
# LANG: _00W8, _00VL --> _00Wc
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01633__00Wc = (v01623__00VL**1)*(v01571__00W8**1)
v01633__00Wc = (v01633__00Wc*_00Wb_coeff).reshape((1, 1, 3, 40, 10))

# op _00Wh_sin_eval
# LANG: _00RZ --> _00Wi
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01580__00Wi = np.sin(v01573__00RZ)

# op _00Wq_sin_eval
# LANG: _00RZ --> _00Wr
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01638__00Wr = np.sin(v01573__00RZ)

# op _00i1_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00i2
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((3,))
v0477__00i2 = (v06_rotor_disk_in_plane_1**1)
v0477__00i2 = (v0477__00i2*_00i1_coeff).reshape((3,))
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((1, 3))

# op _00lc_linear_combination_eval
# LANG: _00l9, _00lb --> _00ld
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0576__00ld = _00lc_constant+1*v0574__00l9+1*v0577__00lb

# op _00mM_decompose_eval
# LANG: bT_integrand --> _00mN, _00mO
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 99), (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0623__00mN = ((v0602_bT_integrand.flatten())[src_indices__00mN__00mM]).reshape((1, 2, 11, 99))
v0624__00mO = ((v0602_bT_integrand.flatten())[src_indices__00mO__00mM]).reshape((1, 2, 11, 99))

# op _00me_decompose_eval
# LANG: aT_integrand --> _00mf, _00mg
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 99), (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0606__00mf = ((v0592_aT_integrand.flatten())[src_indices__00mf__00me]).reshape((1, 2, 11, 99))
v0607__00mg = ((v0592_aT_integrand.flatten())[src_indices__00mg__00me]).reshape((1, 2, 11, 99))

# op _00mv_decompose_eval
# LANG: aD_integrand --> _00mw, _00mx
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 99), (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0615__00mw = ((v0597_aD_integrand.flatten())[src_indices__00mw__00mv]).reshape((1, 2, 11, 99))
v0616__00mx = ((v0597_aD_integrand.flatten())[src_indices__00mx__00mv]).reshape((1, 2, 11, 99))

# op _00n2_decompose_eval
# LANG: bD_integrand --> _00n3, _00n4
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 99), (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0631__00n3 = ((v0605_bD_integrand.flatten())[src_indices__00n3__00n2]).reshape((1, 2, 11, 99))
v0632__00n4 = ((v0605_bD_integrand.flatten())[src_indices__00n4__00n2]).reshape((1, 2, 11, 99))

# op _00nT expand_scalar_eval
# LANG: mach_number --> _00nU
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0665__00nU = np.empty((1, 1))
v0665__00nU.fill(v0486_mach_number.item())

# op _00nV_cos_eval
# LANG: dummy --> _00nW
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0667__00nW = np.cos(v0648_dummy)

# op _00np_power_combination_eval
# LANG: _00no --> _00nq
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0653__00nq = (v0652__00no**1)
v0653__00nq = (v0653__00nq*_00np_coeff).reshape((1,))

# op _00Qp_linear_combination_eval
# LANG: _00Qm, _00Qo --> _00Qq
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01458__00Qq = _00Qp_constant+1*v01456__00Qm+1*v01459__00Qo

# op _00R9_power_combination_eval
# LANG: _00R8, _dT --> aaa
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01473_aaa = (v01211__dT**1)*(v01474__00R8**-1)
v01473_aaa = (v01473_aaa*_00R9_coeff).reshape((1, 40, 30))

# op _00Se expand_array_eval
# LANG: _00Rm --> _00Sf
# SHAPES: (1, 40) --> (1, 1, 3, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01577__00Sf = np.einsum('ad,bce->abcde', v01576__00Rm.reshape((1, 40)) ,np.ones((1, 3, 1))).reshape((1, 1, 3, 40, 1))

# op _00Wj_power_combination_eval
# LANG: _00Wa, _00Wi --> _00Wk
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01579__00Wk = (v01556__00Wa**1)*(v01580__00Wi**1)
v01579__00Wk = (v01579__00Wk*_00Wj_coeff).reshape((1, 1, 3, 40, 10))

# op _00Ws_power_combination_eval
# LANG: _00Wc, _00Wr --> _00Wt
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01637__00Wt = (v01633__00Wc**1)*(v01638__00Wr**1)
v01637__00Wt = (v01637__00Wt*_00Ws_coeff).reshape((1, 1, 3, 40, 10))

# op _00i3 pnorm_eval
# LANG: _00i2 --> _00i4
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0478__00i4 = np.linalg.norm(v0477__00i2.flatten(), ord=2)

# op _00le_power_combination_eval
# LANG: _00ld --> rel_obs_dist
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0578_rel_obs_dist = (v0576__00ld**0.5)
v0578_rel_obs_dist = (v0578_rel_obs_dist*_00le_coeff).reshape((1, 1, 1))

# op _00mP_linear_combination_eval
# LANG: _00mN, _00mO --> _00mQ
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0625__00mQ = _00mP_constant+1*v0623__00mN+1*v0624__00mO

# op _00mh_linear_combination_eval
# LANG: _00mf, _00mg --> _00mi
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0608__00mi = _00mh_constant+1*v0606__00mf+1*v0607__00mg

# op _00my_linear_combination_eval
# LANG: _00mw, _00mx --> _00mz
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0617__00mz = _00my_constant+1*v0615__00mw+1*v0616__00mx

# op _00n5_linear_combination_eval
# LANG: _00n3, _00n4 --> _00n6
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0633__00n6 = _00n5_constant+1*v0631__00n3+1*v0632__00n4

# op _00nX_power_combination_eval
# LANG: _00nU, _00nW --> _00nY
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0666__00nY = (v0665__00nU**1)*(v0667__00nW**1)
v0666__00nY = (v0666__00nY*_00nX_coeff).reshape((1, 1))

# op _00nr_power_combination_eval
# LANG: _00nq --> _00ns
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0654__00ns = (v0653__00nq**1)
v0654__00ns = (v0654__00ns*_00nr_coeff).reshape((1,))

# op _00Qr_power_combination_eval
# LANG: _00Qq --> rel_obs_dist
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01460_rel_obs_dist = (v01458__00Qq**0.5)
v01460_rel_obs_dist = (v01460_rel_obs_dist*_00Qr_coeff).reshape((1, 1, 1))

# op _00Rf_decompose_eval
# LANG: aaa --> _00Rg
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01483__00Rg = ((v01473_aaa.flatten())[src_indices__00Rg__00Rf]).reshape((1, 40, 1))

# op _00Sg_indexed_passthrough_eval
# LANG: _00Sf, _00Wk --> dDdR_real_exp
# SHAPES: (1, 1, 3, 40, 1), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01578_dDdR_real_exp__temp[i_v01577__00Sf__00Sg_indexed_passthrough_eval] = v01577__00Sf.flatten()
v01578_dDdR_real_exp = v01578_dDdR_real_exp__temp.copy()
v01578_dDdR_real_exp__temp[i_v01579__00Wk__00Sg_indexed_passthrough_eval] = v01579__00Wk.flatten()
v01578_dDdR_real_exp = v01578_dDdR_real_exp__temp.copy()

# op _00Wu_indexed_passthrough_eval
# LANG: _00Wt --> dDdR_imag_exp
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01639_dDdR_imag_exp__temp[i_v01637__00Wt__00Wu_indexed_passthrough_eval] = v01637__00Wt.flatten()
v01639_dDdR_imag_exp = v01639_dDdR_imag_exp__temp.copy()

# op _00i5_power_combination_eval
# LANG: _00i4 --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0479_propeller_radius = (v0478__00i4**1)
v0479_propeller_radius = (v0479_propeller_radius*_00i5_coeff).reshape((1,))

# op _00mA_power_combination_eval
# LANG: _00mz --> _00mB
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0618__00mB = (v0617__00mz**1)
v0618__00mB = (v0618__00mB*_00mA_coeff).reshape((1, 2, 11, 99))

# op _00mC expand_scalar_eval
# LANG: dtheta --> _00mD
# SHAPES: (1,) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0620__00mD = np.empty((1, 2, 11, 99))
v0620__00mD.fill(v0611_dtheta.item())

# op _00mR_power_combination_eval
# LANG: _00mQ --> _00mS
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0626__00mS = (v0625__00mQ**1)
v0626__00mS = (v0626__00mS*_00mR_coeff).reshape((1, 2, 11, 99))

# op _00mT expand_scalar_eval
# LANG: dtheta --> _00mU
# SHAPES: (1,) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0628__00mU = np.empty((1, 2, 11, 99))
v0628__00mU.fill(v0611_dtheta.item())

# op _00mj_power_combination_eval
# LANG: _00mi --> _00mk
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0609__00mk = (v0608__00mi**1)
v0609__00mk = (v0609__00mk*_00mj_coeff).reshape((1, 2, 11, 99))

# op _00ml expand_scalar_eval
# LANG: dtheta --> _00mm
# SHAPES: (1,) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0612__00mm = np.empty((1, 2, 11, 99))
v0612__00mm.fill(v0611_dtheta.item())

# op _00n7_power_combination_eval
# LANG: _00n6 --> _00n8
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0634__00n8 = (v0633__00n6**1)
v0634__00n8 = (v0634__00n8*_00n7_coeff).reshape((1, 2, 11, 99))

# op _00n9 expand_scalar_eval
# LANG: dtheta --> _00na
# SHAPES: (1,) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0636__00na = np.empty((1, 2, 11, 99))
v0636__00na.fill(v0611_dtheta.item())

# op _00nD reshape_eval
# LANG: rel_obs_dist --> _00nE
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0663__00nE = v0578_rel_obs_dist.reshape((1, 1))

# op _00nZ_linear_combination_eval
# LANG: _00nY --> _00n_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0668__00n_ = _00nZ_constant+-1*v0666__00nY

# op _00o6 expand_scalar_eval
# LANG: _00ns --> _00o7
# SHAPES: (1,) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0655__00o7 = np.empty((1, 1, 3, 2, 11))
v0655__00o7.fill(v0654__00ns.item())

# op _00QL reshape_eval
# LANG: rel_obs_x_pos --> _00QM
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01469__00QM = v01441_rel_obs_x_pos.reshape((1, 1))

# op _00QO reshape_eval
# LANG: rel_obs_dist --> _00QP
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01471__00QP = v01460_rel_obs_dist.reshape((1, 1))

# op _00Rh reshape_eval
# LANG: _00Rg --> _00Ri
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01484__00Ri = v01483__00Rg.reshape((1, 40))

# op _00WB_power_combination_eval
# LANG: dDdR_real_exp, real_weighting --> _00WC
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01651__00WC = (v01642_real_weighting**1)*(v01578_dDdR_real_exp**1)
v01651__00WC = (v01651__00WC*_00WB_coeff).reshape((1, 1, 3, 40, 11))

# op _00WD_power_combination_eval
# LANG: dDdR_imag_exp, imag_weighting --> _00WE
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01653__00WE = (v01645_imag_weighting**1)*(v01639_dDdR_imag_exp**1)
v01653__00WE = (v01653__00WE*_00WD_coeff).reshape((1, 1, 3, 40, 11))

# op _00WN_power_combination_eval
# LANG: dDdR_imag_exp, real_weighting --> _00WO
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01683__00WO = (v01642_real_weighting**1)*(v01639_dDdR_imag_exp**1)
v01683__00WO = (v01683__00WO*_00WN_coeff).reshape((1, 1, 3, 40, 11))

# op _00WP_power_combination_eval
# LANG: dDdR_real_exp, imag_weighting --> _00WQ
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01685__00WQ = (v01645_imag_weighting**1)*(v01578_dDdR_real_exp**1)
v01685__00WQ = (v01685__00WQ*_00WP_coeff).reshape((1, 1, 3, 40, 11))

# op _00Wd_cos_eval
# LANG: _00RZ --> _00We
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01574__00We = np.cos(v01573__00RZ)

# op _00Wl_cos_eval
# LANG: _00RZ --> _00Wm
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01635__00Wm = np.cos(v01573__00RZ)

# op _00mE_power_combination_eval
# LANG: _00mB, _00mD --> _00mF
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0619__00mF = (v0618__00mB**1)*(v0620__00mD**1)
v0619__00mF = (v0619__00mF*_00mE_coeff).reshape((1, 2, 11, 99))

# op _00mV_power_combination_eval
# LANG: _00mS, _00mU --> _00mW
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0627__00mW = (v0626__00mS**1)*(v0628__00mU**1)
v0627__00mW = (v0627__00mW*_00mV_coeff).reshape((1, 2, 11, 99))

# op _00mn_power_combination_eval
# LANG: _00mk, _00mm --> _00mo
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0610__00mo = (v0609__00mk**1)*(v0612__00mm**1)
v0610__00mo = (v0610__00mo*_00mn_coeff).reshape((1, 2, 11, 99))

# op _00nb_power_combination_eval
# LANG: _00n8, _00na --> _00nc
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0635__00nc = (v0634__00n8**1)*(v0636__00na**1)
v0635__00nc = (v0635__00nc*_00nb_coeff).reshape((1, 2, 11, 99))

# op _00o0_power_combination_eval
# LANG: _00nE, _00n_ --> _00o1
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0664__00o1 = (v0663__00nE**1)*(v0668__00n_**1)
v0664__00o1 = (v0664__00o1*_00o0_coeff).reshape((1, 1))

# op _00oO_power_combination_eval
# LANG: n_var, _00o7 --> _00oP
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0650__00oP = (v0649_n_var**1)*(v0655__00o7**1)
v0650__00oP = (v0650__00oP*_00oO_coeff).reshape((1, 1, 3, 2, 11))

# op _00og expand_scalar_eval
# LANG: propeller_radius --> _00oh
# SHAPES: (1,) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0657__00oh = np.empty((1, 1, 3, 2, 11))
v0657__00oh.fill(v0479_propeller_radius.item())

# op _00P5_power_combination_eval
# LANG: temperature --> _00P6
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01413__00P6 = (v01401_temperature**1)
v01413__00P6 = (v01413__00P6*_00P5_coeff).reshape((1,))

# op _00QR_power_combination_eval
# LANG: _00QM, _00QP --> _00QS
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01470__00QS = (v01469__00QM**1)*(v01471__00QP**-1)
v01470__00QS = (v01470__00QS*_00QR_coeff).reshape((1, 1))

# op _00Sb expand_array_eval
# LANG: _00Ri --> _00Sc
# SHAPES: (1, 40) --> (1, 1, 3, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01485__00Sc = np.einsum('ad,bce->abcde', v01484__00Ri.reshape((1, 40)) ,np.ones((1, 3, 1))).reshape((1, 1, 3, 40, 1))

# op _00WF_linear_combination_eval
# LANG: _00WC, _00WE --> _00WG
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01652__00WG = _00WF_constant+1*v01651__00WC+1*v01653__00WE

# op _00WR_linear_combination_eval
# LANG: _00WO, _00WQ --> _00WS
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01684__00WS = _00WR_constant+1*v01683__00WO+1*v01685__00WQ

# op _00WT_power_combination_eval
# LANG: n_var --> _00WU
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01666__00WU = (v01655_n_var**1)
v01666__00WU = (v01666__00WU*_00WT_coeff).reshape((1, 1, 3, 40, 11))

# op _00Wf_power_combination_eval
# LANG: _00Wa, _00We --> _00Wg
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01572__00Wg = (v01556__00Wa**1)*(v01574__00We**1)
v01572__00Wg = (v01572__00Wg*_00Wf_coeff).reshape((1, 1, 3, 40, 10))

# op _00Wn_power_combination_eval
# LANG: _00Wc, _00Wm --> _00Wo
# SHAPES: (1, 1, 3, 40, 10), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01634__00Wo = (v01633__00Wc**1)*(v01635__00Wm**1)
v01634__00Wo = (v01634__00Wo*_00Wn_coeff).reshape((1, 1, 3, 40, 10))

# op _00XE_linear_combination_eval
# LANG: lam_var, n_var --> _00XF
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01687__00XF = _00XE_constant+1*v01655_n_var+-1*v01487_lam_var

# op _00XM_power_combination_eval
# LANG: n_var --> _00XN
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01691__00XN = (v01655_n_var**1)
v01691__00XN = (v01691__00XN*_00XM_coeff).reshape((1, 1, 3, 40, 11))

# op _00Xa_linear_combination_eval
# LANG: lam_var, n_var --> _00Xb
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01656__00Xb = _00Xa_constant+1*v01655_n_var+-1*v01487_lam_var

# op _00Xi_power_combination_eval
# LANG: n_var --> _00Xj
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01661__00Xj = (v01655_n_var**1)
v01661__00Xj = (v01661__00Xj*_00Xi_coeff).reshape((1, 1, 3, 40, 11))

# op _00mG_power_combination_eval
# LANG: _00mF --> _00mH
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0621__00mH = (v0619__00mF**1)
v0621__00mH = (v0621__00mH*_00mG_coeff).reshape((1, 2, 11, 99))

# op _00mX_power_combination_eval
# LANG: _00mW --> _00mY
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0629__00mY = (v0627__00mW**1)
v0629__00mY = (v0629__00mY*_00mX_coeff).reshape((1, 2, 11, 99))

# op _00mp_power_combination_eval
# LANG: _00mo --> _00mq
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0613__00mq = (v0610__00mo**1)
v0613__00mq = (v0613__00mq*_00mp_coeff).reshape((1, 2, 11, 99))

# op _00nd_power_combination_eval
# LANG: _00nc --> _00ne
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0637__00ne = (v0635__00nc**1)
v0637__00ne = (v0637__00ne*_00nd_coeff).reshape((1, 2, 11, 99))

# op _00oQ_power_combination_eval
# LANG: _00oP, _00oh --> _00oR
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0656__00oR = (v0650__00oP**1)*(v0657__00oh**1)
v0656__00oR = (v0656__00oR*_00oQ_coeff).reshape((1, 1, 3, 2, 11))

# op _00oa expand_array_eval
# LANG: _00nv --> _00ob
# SHAPES: (1, 1) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0659__00ob = np.einsum('ab,cde->abcde', v0641__00nv.reshape((1, 1)) ,np.ones((3, 2, 11))).reshape((1, 1, 3, 2, 11))

# op _00oc expand_scalar_eval
# LANG: speed_of_sound --> _00od
# SHAPES: (1,) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0661__00od = np.empty((1, 1, 3, 2, 11))
v0661__00od.fill(v0532_speed_of_sound.item())

# op _00oe expand_array_eval
# LANG: _00o1 --> _00of
# SHAPES: (1, 1) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0669__00of = np.einsum('ab,cde->abcde', v0664__00o1.reshape((1, 1)) ,np.ones((3, 2, 11))).reshape((1, 1, 3, 2, 11))

# op _00P7_power_combination_eval
# LANG: _00P6 --> speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01414_speed_of_sound = (v01413__00P6**0.5)
v01414_speed_of_sound = (v01414_speed_of_sound*_00P7_coeff).reshape((1,))

# op _00QT arccos_eval
# LANG: _00QS --> theta_dummy
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01472_theta_dummy = np.arccos(v01470__00QS)

# op _00Sd_indexed_passthrough_eval
# LANG: _00Sc, _00Wg --> dTdR_real_exp
# SHAPES: (1, 1, 3, 40, 1), (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01486_dTdR_real_exp__temp[i_v01485__00Sc__00Sd_indexed_passthrough_eval] = v01485__00Sc.flatten()
v01486_dTdR_real_exp = v01486_dTdR_real_exp__temp.copy()
v01486_dTdR_real_exp__temp[i_v01572__00Wg__00Sd_indexed_passthrough_eval] = v01572__00Wg.flatten()
v01486_dTdR_real_exp = v01486_dTdR_real_exp__temp.copy()

# op _00WV_power_combination_eval
# LANG: _00Rs, _00WU --> _00WW
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01667__00WW = (v01666__00WU**1)*(v01493__00Rs**1)
v01667__00WW = (v01667__00WW*_00WV_coeff).reshape((1, 1, 3, 40, 11))

# op _00Wp_indexed_passthrough_eval
# LANG: _00Wo --> dTdR_imag_exp
# SHAPES: (1, 1, 3, 40, 10) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01636_dTdR_imag_exp__temp[i_v01634__00Wo__00Wp_indexed_passthrough_eval] = v01634__00Wo.flatten()
v01636_dTdR_imag_exp = v01636_dTdR_imag_exp__temp.copy()

# op _00XG_power_combination_eval
# LANG: _00WS, _00XF --> _00XH
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01686__00XH = (v01684__00WS**1)*(v01687__00XF**1)
v01686__00XH = (v01686__00XH*_00XG_coeff).reshape((1, 1, 3, 40, 11))

# op _00XO_power_combination_eval
# LANG: _00Rs, _00XN --> _00XP
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01692__00XP = (v01691__00XN**1)*(v01493__00Rs**1)
v01692__00XP = (v01692__00XP*_00XO_coeff).reshape((1, 1, 3, 40, 11))

# op _00Xc_power_combination_eval
# LANG: _00WG, _00Xb --> _00Xd
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01654__00Xd = (v01652__00WG**1)*(v01656__00Xb**1)
v01654__00Xd = (v01654__00Xd*_00Xc_coeff).reshape((1, 1, 3, 40, 11))

# op _00Xk_power_combination_eval
# LANG: _00Rs, _00Xj --> _00Xl
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01662__00Xl = (v01661__00Xj**1)*(v01493__00Rs**1)
v01662__00Xl = (v01662__00Xl*_00Xk_coeff).reshape((1, 1, 3, 40, 11))

# op _00mI_single_tensor_sum_with_axis_eval
# LANG: _00mH --> aD
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0622_aD = np.sum(v0621__00mH, axis = (3,)).reshape((1, 2, 11))

# op _00mZ_single_tensor_sum_with_axis_eval
# LANG: _00mY --> bT
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0630_bT = np.sum(v0629__00mY, axis = (3,)).reshape((1, 2, 11))

# op _00mr_single_tensor_sum_with_axis_eval
# LANG: _00mq --> aT
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0614_aT = np.sum(v0613__00mq, axis = (3,)).reshape((1, 2, 11))

# op _00nf_single_tensor_sum_with_axis_eval
# LANG: _00ne --> bD
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0638_bD = np.sum(v0637__00ne, axis = (3,)).reshape((1, 2, 11))

# op _00oS_power_combination_eval
# LANG: _00oR, _00ob --> _00oT
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0658__00oT = (v0656__00oR**1)*(v0659__00ob**1)
v0658__00oT = (v0658__00oT*_00oS_coeff).reshape((1, 1, 3, 2, 11))

# op _00oU_power_combination_eval
# LANG: _00od, _00of --> _00oV
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0662__00oV = (v0661__00od**1)*(v0669__00of**1)
v0662__00oV = (v0662__00oV*_00oU_coeff).reshape((1, 1, 3, 2, 11))

# op _00pB_exp_a_eval
# LANG: lam_var --> _00pC
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0709__00pC = _00pB_exp_a_eval_a**v0690_lam_var

# op _00qA_exp_a_eval
# LANG: lam_var --> _00qB
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0748__00qB = _00qA_exp_a_eval_a**v0690_lam_var

# op _00Rn expand_array_eval
# LANG: theta_dummy --> _00Ro
# SHAPES: (1, 1) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01648__00Ro = np.einsum('ab,cde->abcde', v01472_theta_dummy.reshape((1, 1)) ,np.ones((3, 40, 11))).reshape((1, 1, 3, 40, 11))

# op _00Rv expand_scalar_eval
# LANG: speed_of_sound --> _00Rw
# SHAPES: (1,) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01659__00Rw = np.empty((1, 1, 3, 40, 11))
v01659__00Rw.fill(v01414_speed_of_sound.item())

# op _00WH_power_combination_eval
# LANG: dTdR_imag_exp, real_weighting --> _00WI
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01677__00WI = (v01642_real_weighting**1)*(v01636_dTdR_imag_exp**1)
v01677__00WI = (v01677__00WI*_00WH_coeff).reshape((1, 1, 3, 40, 11))

# op _00WJ_power_combination_eval
# LANG: dTdR_real_exp, imag_weighting --> _00WK
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01679__00WK = (v01645_imag_weighting**1)*(v01486_dTdR_real_exp**1)
v01679__00WK = (v01679__00WK*_00WJ_coeff).reshape((1, 1, 3, 40, 11))

# op _00WX_power_combination_eval
# LANG: _00Rq, _00WW --> _00WY
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01668__00WY = (v01667__00WW**1)*(v01482__00Rq**1)
v01668__00WY = (v01668__00WY*_00WX_coeff).reshape((1, 1, 3, 40, 11))

# op _00Wv_power_combination_eval
# LANG: dTdR_real_exp, real_weighting --> _00Ww
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01643__00Ww = (v01642_real_weighting**1)*(v01486_dTdR_real_exp**1)
v01643__00Ww = (v01643__00Ww*_00Wv_coeff).reshape((1, 1, 3, 40, 11))

# op _00Wx_power_combination_eval
# LANG: dTdR_imag_exp, imag_weighting --> _00Wy
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01646__00Wy = (v01645_imag_weighting**1)*(v01636_dTdR_imag_exp**1)
v01646__00Wy = (v01646__00Wy*_00Wx_coeff).reshape((1, 1, 3, 40, 11))

# op _00XI_power_combination_eval
# LANG: _00XH --> _00XJ
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01688__00XJ = (v01686__00XH**1)
v01688__00XJ = (v01688__00XJ*_00XI_coeff).reshape((1, 1, 3, 40, 11))

# op _00XQ_power_combination_eval
# LANG: _00Rq, _00XP --> _00XR
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01693__00XR = (v01692__00XP**1)*(v01482__00Rq**1)
v01693__00XR = (v01693__00XR*_00XQ_coeff).reshape((1, 1, 3, 40, 11))

# op _00Xe_power_combination_eval
# LANG: _00Xd --> _00Xf
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01657__00Xf = (v01654__00Xd**1)
v01657__00Xf = (v01657__00Xf*_00Xe_coeff).reshape((1, 1, 3, 40, 11))

# op _00Xm_power_combination_eval
# LANG: _00Rq, _00Xl --> _00Xn
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01663__00Xn = (v01662__00Xl**1)*(v01482__00Rq**1)
v01663__00Xn = (v01663__00Xn*_00Xm_coeff).reshape((1, 1, 3, 40, 11))

# op _00_Y expand_scalar_eval
# LANG: Vx --> _00_Z
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01778__00_Z = np.empty((1, 1))
v01778__00_Z.fill(v0917_u.item())

# op _00o8 expand_array_eval
# LANG: _00nB --> _00o9
# SHAPES: (1, 1) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0680__00o9 = np.einsum('ab,cde->abcde', v0639__00nB.reshape((1, 1)) ,np.ones((3, 2, 11))).reshape((1, 1, 3, 2, 11))

# op _00oA_power_combination_eval
# LANG: n_var, _00o7 --> _00oB
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0678__00oB = (v0649_n_var**1)*(v0655__00o7**1)
v0678__00oB = (v0678__00oB*_00oA_coeff).reshape((1, 1, 3, 2, 11))

# op _00oE_power_combination_eval
# LANG: _00of --> _00oF
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0683__00oF = (v0669__00of**2)
v0683__00oF = (v0683__00oF*_00oE_coeff).reshape((1, 1, 3, 2, 11))

# op _00oW_power_combination_eval
# LANG: _00oT, _00oV --> _00oX
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0660__00oX = (v0658__00oT**1)*(v0662__00oV**-1)
v0660__00oX = (v0660__00oX*_00oW_coeff).reshape((1, 1, 3, 2, 11))

# op _00oi expand_array_eval
# LANG: aT --> _00oj
# SHAPES: (1, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0677__00oj = np.einsum('ade,bc->abcde', v0614_aT.reshape((1, 2, 11)) ,np.ones((1, 3))).reshape((1, 1, 3, 2, 11))

# op _00ok expand_array_eval
# LANG: bT --> _00ol
# SHAPES: (1, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0673__00ol = np.einsum('ade,bc->abcde', v0630_bT.reshape((1, 2, 11)) ,np.ones((1, 3))).reshape((1, 1, 3, 2, 11))

# op _00om expand_array_eval
# LANG: aD --> _00on
# SHAPES: (1, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0702__00on = np.einsum('ade,bc->abcde', v0622_aD.reshape((1, 2, 11)) ,np.ones((1, 3))).reshape((1, 1, 3, 2, 11))

# op _00oo expand_array_eval
# LANG: bD --> _00op
# SHAPES: (1, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0699__00op = np.einsum('ade,bc->abcde', v0638_bD.reshape((1, 2, 11)) ,np.ones((1, 3))).reshape((1, 1, 3, 2, 11))

# op _00pD_power_combination_eval
# LANG: A_lin_comb_sign_matrix, _00pC --> _00pE
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0708__00pE = (v0688_A_lin_comb_sign_matrix**1)*(v0709__00pC**1)
v0708__00pE = (v0708__00pE*_00pD_coeff).reshape((1, 1, 3, 2, 11))

# op _00pF_linear_combination_eval
# LANG: n_var, lam_var --> _00pG
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0711__00pG = _00pF_constant+1*v0649_n_var+1*v0690_lam_var

# op _00pf_exp_a_eval
# LANG: lam_var --> _00pg
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0691__00pg = _00pf_exp_a_eval_a**v0690_lam_var

# op _00qC_power_combination_eval
# LANG: B_lin_comb_sign_matrix, _00qB --> _00qD
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0747__00qD = (v0730_B_lin_comb_sign_matrix**1)*(v0748__00qB**1)
v0747__00qD = (v0747__00qD*_00qC_coeff).reshape((1, 1, 3, 2, 11))

# op _00qE_linear_combination_eval
# LANG: n_var, lam_var --> _00qF
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0750__00qF = _00qE_constant+1*v0649_n_var+1*v0690_lam_var

# op _00qg_exp_a_eval
# LANG: lam_var --> _00qh
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0732__00qh = _00qg_exp_a_eval_a**v0690_lam_var

# op _0100 expand_scalar_eval
# LANG: Vy --> _0101
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01780__0101 = np.empty((1, 1))
v01780__0101.fill(v0918_v.item())

# op _0102 expand_scalar_eval
# LANG: Vz --> _0103
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01781__0103 = np.empty((1, 1))
v01781__0103.fill(v0919_w.item())

# op _00WL_linear_combination_eval
# LANG: _00WI, _00WK --> _00WM
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01678__00WM = _00WL_constant+1*v01677__00WI+1*v01679__00WK

# op _00WZ_power_combination_eval
# LANG: _00Ru, _00WY --> _00W_
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01669__00W_ = (v01668__00WY**1)*(v01502__00Ru**1)
v01669__00W_ = (v01669__00W_*_00WZ_coeff).reshape((1, 1, 3, 40, 11))

# op _00Wz_linear_combination_eval
# LANG: _00Ww, _00Wy --> _00WA
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01644__00WA = _00Wz_constant+1*v01643__00Ww+1*v01646__00Wy

# op _00X6_cos_eval
# LANG: _00Ro --> _00X7
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01649__00X7 = np.cos(v01648__00Ro)

# op _00XA_cos_eval
# LANG: _00Ro --> _00XB
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01681__00XB = np.cos(v01648__00Ro)

# op _00XK_power_combination_eval
# LANG: _00Rw, _00XJ --> _00XL
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01689__00XL = (v01688__00XJ**1)*(v01659__00Rw**1)
v01689__00XL = (v01689__00XL*_00XK_coeff).reshape((1, 1, 3, 40, 11))

# op _00XS_power_combination_eval
# LANG: _00Ru, _00XR --> _00XT
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01694__00XT = (v01693__00XR**1)*(v01502__00Ru**1)
v01694__00XT = (v01694__00XT*_00XS_coeff).reshape((1, 1, 3, 40, 11))

# op _00Xg_power_combination_eval
# LANG: _00Xf, _00Rw --> _00Xh
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01658__00Xh = (v01657__00Xf**1)*(v01659__00Rw**1)
v01658__00Xh = (v01658__00Xh*_00Xg_coeff).reshape((1, 1, 3, 40, 11))

# op _00Xo_power_combination_eval
# LANG: _00Ru, _00Xn --> _00Xp
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01664__00Xp = (v01663__00Xn**1)*(v01502__00Ru**1)
v01664__00Xp = (v01664__00Xp*_00Xo_coeff).reshape((1, 1, 3, 40, 11))

# op _00___indexed_passthrough_eval
# LANG: _00_Z, _0101, _0103 --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01779_V_aircraft__temp[i_v01778__00_Z__00___indexed_passthrough_eval] = v01778__00_Z.flatten()
v01779_V_aircraft = v01779_V_aircraft__temp.copy()
v01779_V_aircraft__temp[i_v01780__0101__00___indexed_passthrough_eval] = v01780__0101.flatten()
v01779_V_aircraft = v01779_V_aircraft__temp.copy()
v01779_V_aircraft__temp[i_v01781__0103__00___indexed_passthrough_eval] = v01781__0103.flatten()
v01779_V_aircraft = v01779_V_aircraft__temp.copy()

# op _00oC_power_combination_eval
# LANG: _00oB, _00o9 --> _00oD
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0679__00oD = (v0678__00oB**1)*(v0680__00o9**1)
v0679__00oD = (v0679__00oD*_00oC_coeff).reshape((1, 1, 3, 2, 11))

# op _00oG_power_combination_eval
# LANG: _00od, _00oF --> _00oH
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0682__00oH = (v0661__00od**1)*(v0683__00oF**1)
v0682__00oH = (v0682__00oH*_00oG_coeff).reshape((1, 1, 3, 2, 11))

# op _00oK_power_combination_eval
# LANG: _00oh, _00of --> _00oL
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0695__00oL = (v0657__00oh**1)*(v0669__00of**1)
v0695__00oL = (v0695__00oL*_00oK_coeff).reshape((1, 1, 3, 2, 11))

# op _00o__power_combination_eval
# LANG: coeff_sign_matrix_even, _00ol --> _00p0
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0672__00p0 = (v0671_coeff_sign_matrix_even**1)*(v0673__00ol**1)
v0672__00p0 = (v0672__00p0*_00o__coeff).reshape((1, 1, 3, 2, 11))

# op _00p1_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00oj --> _00p2
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0676__00p2 = (v0675_coeff_sign_matrix_odd**1)*(v0677__00oj**1)
v0676__00p2 = (v0676__00p2*_00p1_coeff).reshape((1, 1, 3, 2, 11))

# op _00p5_power_combination_eval
# LANG: coeff_sign_matrix_even, _00op --> _00p6
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0698__00p6 = (v0671_coeff_sign_matrix_even**1)*(v0699__00op**1)
v0698__00p6 = (v0698__00p6*_00p5_coeff).reshape((1, 1, 3, 2, 11))

# op _00p7_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00on --> _00p8
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0701__00p8 = (v0675_coeff_sign_matrix_odd**1)*(v0702__00on**1)
v0701__00p8 = (v0701__00p8*_00p7_coeff).reshape((1, 1, 3, 2, 11))

# op _00pH_power_combination_eval
# LANG: _00pE, _00pG --> _00pI
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0710__00pI = (v0708__00pE**1)*(v0711__00pG**1)
v0710__00pI = (v0710__00pI*_00pH_coeff).reshape((1, 1, 3, 2, 11))

# op _00pJ_bessel_eval
# LANG: _00oX --> _00pK
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0713__00pK=_00pJ_bessel_eval(_00pJ_bessel_eval_order,v0660__00oX)

# op _00ph_power_combination_eval
# LANG: A_lin_comb_sign_matrix, _00pg --> _00pi
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0689__00pi = (v0688_A_lin_comb_sign_matrix**1)*(v0691__00pg**1)
v0689__00pi = (v0689__00pi*_00ph_coeff).reshape((1, 1, 3, 2, 11))

# op _00pj_bessel_eval
# LANG: _00oX --> _00pk
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0693__00pk=_00pj_bessel_eval(_00pj_bessel_eval_order,v0660__00oX)

# op _00pv_linear_combination_eval
# LANG: n_var, lam_var --> _00pw
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0704__00pw = _00pv_constant+1*v0649_n_var+-1*v0690_lam_var

# op _00px_bessel_eval
# LANG: _00oX --> _00py
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0706__00py=_00px_bessel_eval(_00px_bessel_eval_order,v0660__00oX)

# op _00q0_power_combination_eval
# LANG: coeff_sign_matrix_even, _00oj --> _00q1
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0724__00q1 = (v0671_coeff_sign_matrix_even**1)*(v0677__00oj**1)
v0724__00q1 = (v0724__00q1*_00q0_coeff).reshape((1, 1, 3, 2, 11))

# op _00q2_power_combination_eval
# LANG: _00ol, coeff_sign_matrix_odd --> _00q3
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0726__00q3 = (v0675_coeff_sign_matrix_odd**1)*(v0673__00ol**1)
v0726__00q3 = (v0726__00q3*_00q2_coeff).reshape((1, 1, 3, 2, 11))

# op _00q6_power_combination_eval
# LANG: coeff_sign_matrix_even, _00on --> _00q7
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0739__00q7 = (v0671_coeff_sign_matrix_even**1)*(v0702__00on**1)
v0739__00q7 = (v0739__00q7*_00q6_coeff).reshape((1, 1, 3, 2, 11))

# op _00q8_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00op --> _00q9
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0741__00q9 = (v0675_coeff_sign_matrix_odd**1)*(v0699__00op**1)
v0741__00q9 = (v0741__00q9*_00q8_coeff).reshape((1, 1, 3, 2, 11))

# op _00qG_power_combination_eval
# LANG: _00qD, _00qF --> _00qH
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0749__00qH = (v0747__00qD**1)*(v0750__00qF**1)
v0749__00qH = (v0749__00qH*_00qG_coeff).reshape((1, 1, 3, 2, 11))

# op _00qI_bessel_eval
# LANG: _00oX --> _00qJ
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0752__00qJ=_00qI_bessel_eval(_00qI_bessel_eval_order,v0660__00oX)

# op _00qi_power_combination_eval
# LANG: B_lin_comb_sign_matrix, _00qh --> _00qj
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0731__00qj = (v0730_B_lin_comb_sign_matrix**1)*(v0732__00qh**1)
v0731__00qj = (v0731__00qj*_00qi_coeff).reshape((1, 1, 3, 2, 11))

# op _00qk_bessel_eval
# LANG: _00oX --> _00ql
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0734__00ql=_00qk_bessel_eval(_00qk_bessel_eval_order,v0660__00oX)

# op _00qu_linear_combination_eval
# LANG: n_var, lam_var --> _00qv
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0743__00qv = _00qu_constant+1*v0649_n_var+-1*v0690_lam_var

# op _00qw_bessel_eval
# LANG: _00oX --> _00qx
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0745__00qx=_00qw_bessel_eval(_00qw_bessel_eval_order,v0660__00oX)

# op _00X0_power_combination_eval
# LANG: _00Rw, _00W_ --> _00X1
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01670__00X1 = (v01669__00W_**1)*(v01659__00Rw**-1)
v01670__00X1 = (v01670__00X1*_00X0_coeff).reshape((1, 1, 3, 40, 11))

# op _00X2_sin_eval
# LANG: _00Ro --> _00X3
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01672__00X3 = np.sin(v01648__00Ro)

# op _00X8_power_combination_eval
# LANG: _00WA, _00X7 --> _00X9
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01647__00X9 = (v01644__00WA**1)*(v01649__00X7**1)
v01647__00X9 = (v01647__00X9*_00X8_coeff).reshape((1, 1, 3, 40, 11))

# op _00XC_power_combination_eval
# LANG: _00WM, _00XB --> _00XD
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01680__00XD = (v01678__00WM**1)*(v01681__00XB**1)
v01680__00XD = (v01680__00XD*_00XC_coeff).reshape((1, 1, 3, 40, 11))

# op _00XU_power_combination_eval
# LANG: _00XL, _00XT --> _00XV
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01690__00XV = (v01689__00XL**1)*(v01694__00XT**-1)
v01690__00XV = (v01690__00XV*_00XU_coeff).reshape((1, 1, 3, 40, 11))

# op _00Xq_power_combination_eval
# LANG: _00Xh, _00Xp --> _00Xr
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01660__00Xr = (v01658__00Xh**1)*(v01664__00Xp**-1)
v01660__00Xr = (v01660__00Xr*_00Xq_coeff).reshape((1, 1, 3, 40, 11))

# op _00oI_power_combination_eval
# LANG: _00oD, _00oH --> _00oJ
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0681__00oJ = (v0679__00oD**1)*(v0682__00oH**-1)
v0681__00oJ = (v0681__00oJ*_00oI_coeff).reshape((1, 1, 3, 2, 11))

# op _00oM_power_combination_eval
# LANG: _00oL --> _00oN
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0696__00oN = (v0695__00oL**-1)
v0696__00oN = (v0696__00oN*_00oM_coeff).reshape((1, 1, 3, 2, 11))

# op _00p3_linear_combination_eval
# LANG: _00p0, _00p2 --> asdf
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0674_asdf = _00p3_constant+1*v0672__00p0+1*v0676__00p2

# op _00p9_linear_combination_eval
# LANG: _00p6, _00p8 --> _00pa
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0700__00pa = _00p9_constant+1*v0698__00p6+1*v0701__00p8

# op _00pL_power_combination_eval
# LANG: _00pI, _00pK --> _00pM
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0712__00pM = (v0710__00pI**1)*(v0713__00pK**1)
v0712__00pM = (v0712__00pM*_00pL_coeff).reshape((1, 1, 3, 2, 11))

# op _00pd_bessel_eval
# LANG: _00oX --> _00pe
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0686__00pe=_00pd_bessel_eval(_00pd_bessel_eval_order,v0660__00oX)

# op _00pl_power_combination_eval
# LANG: _00pi, _00pk --> _00pm
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0692__00pm = (v0689__00pi**1)*(v0693__00pk**1)
v0692__00pm = (v0692__00pm*_00pl_coeff).reshape((1, 1, 3, 2, 11))

# op _00pz_power_combination_eval
# LANG: _00pw, _00py --> _00pA
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0705__00pA = (v0704__00pw**1)*(v0706__00py**1)
v0705__00pA = (v0705__00pA*_00pz_coeff).reshape((1, 1, 3, 2, 11))

# op _00q4_linear_combination_eval
# LANG: _00q1, _00q3 --> _00q5
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0725__00q5 = _00q4_constant+1*v0724__00q1+1*v0726__00q3

# op _00qK_power_combination_eval
# LANG: _00qH, _00qJ --> _00qL
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0751__00qL = (v0749__00qH**1)*(v0752__00qJ**1)
v0751__00qL = (v0751__00qL*_00qK_coeff).reshape((1, 1, 3, 2, 11))

# op _00qa_linear_combination_eval
# LANG: _00q7, _00q9 --> _00qb
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0740__00qb = _00qa_constant+1*v0739__00q7+1*v0741__00q9

# op _00qe_bessel_eval
# LANG: _00oX --> _00qf
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0728__00qf=_00qe_bessel_eval(_00qe_bessel_eval_order,v0660__00oX)

# op _00qm_power_combination_eval
# LANG: _00qj, _00ql --> _00qn
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0733__00qn = (v0731__00qj**1)*(v0734__00ql**1)
v0733__00qn = (v0733__00qn*_00qm_coeff).reshape((1, 1, 3, 2, 11))

# op _00qy_power_combination_eval
# LANG: _00qv, _00qx --> _00qz
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0744__00qz = (v0743__00qv**1)*(v0745__00qx**1)
v0744__00qz = (v0744__00qz*_00qy_coeff).reshape((1, 1, 3, 2, 11))

# op _0104 expand_array_eval
# LANG: V_aircraft --> _0105
# SHAPES: (1, 3) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01788__0105 = np.einsum('ab,c->abc', v01779_V_aircraft.reshape((1, 3)) ,np.ones((1,))).reshape((1, 3, 1))

# op _010a expand_scalar_eval
# LANG: time_vectors --> _010b
# SHAPES: (1,) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01794__010b = np.empty((1, 3, 1))
v01794__010b.fill(v01793_time_vectors.item())

# op _00X4_power_combination_eval
# LANG: _00X1, _00X3 --> _00X5
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01671__00X5 = (v01670__00X1**1)*(v01672__00X3**1)
v01671__00X5 = (v01671__00X5*_00X4_coeff).reshape((1, 1, 3, 40, 11))

# op _00XW_linear_combination_eval
# LANG: _00XD, _00XV --> _00XX
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01682__00XX = _00XW_constant+1*v01680__00XD+-1*v01690__00XV

# op _00Xs_linear_combination_eval
# LANG: _00X9, _00Xr --> _00Xt
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01650__00Xt = _00Xs_constant+1*v01647__00X9+-1*v01660__00Xr

# op _00pN_linear_combination_eval
# LANG: _00pA, _00pM --> _00pO
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0707__00pO = _00pN_constant+1*v0705__00pA+1*v0712__00pM

# op _00pb_power_combination_eval
# LANG: asdf, _00oJ --> _00pc
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0684__00pc = (v0681__00oJ**1)*(v0674_asdf**1)
v0684__00pc = (v0684__00pc*_00pb_coeff).reshape((1, 1, 3, 2, 11))

# op _00pn_linear_combination_eval
# LANG: _00pe, _00pm --> _00po
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0687__00po = _00pn_constant+1*v0686__00pe+1*v0692__00pm

# op _00pt_power_combination_eval
# LANG: _00oN, _00pa --> _00pu
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0697__00pu = (v0696__00oN**1)*(v0700__00pa**1)
v0697__00pu = (v0697__00pu*_00pt_coeff).reshape((1, 1, 3, 2, 11))

# op _00qM_linear_combination_eval
# LANG: _00qz, _00qL --> _00qN
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0746__00qN = _00qM_constant+1*v0744__00qz+1*v0751__00qL

# op _00qc_power_combination_eval
# LANG: _00oJ, _00q5 --> _00qd
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0723__00qd = (v0681__00oJ**1)*(v0725__00q5**1)
v0723__00qd = (v0723__00qd*_00qc_coeff).reshape((1, 1, 3, 2, 11))

# op _00qo_linear_combination_eval
# LANG: _00qf, _00qn --> _00qp
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0729__00qp = _00qo_constant+1*v0728__00qf+1*v0733__00qn

# op _00qs_power_combination_eval
# LANG: _00oN, _00qb --> _00qt
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0738__00qt = (v0696__00oN**1)*(v0740__00qb**1)
v0738__00qt = (v0738__00qt*_00qs_coeff).reshape((1, 1, 3, 2, 11))

# op _00sZ expand_scalar_eval
# LANG: Vx --> _00s_
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0809__00s_ = np.empty((1, 1))
v0809__00s_.fill(v028_u.item())

# op _00t1 expand_scalar_eval
# LANG: Vy --> _00t2
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0811__00t2 = np.empty((1, 1))
v0811__00t2.fill(v033_v.item())

# op _00t3 expand_scalar_eval
# LANG: Vz --> _00t4
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0812__00t4 = np.empty((1, 1))
v0812__00t4.fill(v037_w.item())

# op _0107 expand_array_eval
# LANG: aircraft_location --> _0108
# SHAPES: (3, 1) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01783__0108 = np.einsum('bc,a->abc', v01782_aircraft_location.reshape((3, 1)) ,np.ones((1,))).reshape((1, 3, 1))

# op _010e_decompose_eval
# LANG: _0105 --> _010f, _010n, _010u
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01789__010f = ((v01788__0105.flatten())[src_indices__010f__010e]).reshape((1, 1, 1))
v01790__010n = ((v01788__0105.flatten())[src_indices__010n__010e]).reshape((1, 1, 1))
v01791__010u = ((v01788__0105.flatten())[src_indices__010u__010e]).reshape((1, 1, 1))

# op _010g_decompose_eval
# LANG: _010b --> _010h, _010o, _010v
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01795__010h = ((v01794__010b.flatten())[src_indices__010h__010g]).reshape((1, 1, 1))
v01796__010o = ((v01794__010b.flatten())[src_indices__010o__010g]).reshape((1, 1, 1))
v01797__010v = ((v01794__010b.flatten())[src_indices__010v__010g]).reshape((1, 1, 1))

# op _00XY_power_combination_eval
# LANG: coeff_matrix_B, _00XX --> _00XZ
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01676__00XZ = (v01675_coeff_matrix_B**1)*(v01682__00XX**1)
v01676__00XZ = (v01676__00XZ*_00XY_coeff).reshape((1, 1, 3, 40, 11))

# op _00X__bessel_eval
# LANG: _00X5 --> _00Y0
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01696__00Y0=_00X__bessel_eval(_00X__bessel_eval_order,v01671__00X5)

# op _00Xu_power_combination_eval
# LANG: coeff_matrix_A, _00Xt --> _00Xv
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01641__00Xv = (v01640_coeff_matrix_A**1)*(v01650__00Xt**1)
v01641__00Xv = (v01641__00Xv*_00Xu_coeff).reshape((1, 1, 3, 40, 11))

# op _00Xw_bessel_eval
# LANG: _00X5 --> _00Xx
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01673__00Xx=_00Xw_bessel_eval(_00Xw_bessel_eval_order,v01671__00X5)

# op _00pP_power_combination_eval
# LANG: _00pu, _00pO --> _00pQ
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0703__00pQ = (v0697__00pu**1)*(v0707__00pO**1)
v0703__00pQ = (v0703__00pQ*_00pP_coeff).reshape((1, 1, 3, 2, 11))

# op _00pp_power_combination_eval
# LANG: _00pc, _00po --> _00pq
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0685__00pq = (v0684__00pc**1)*(v0687__00po**1)
v0685__00pq = (v0685__00pq*_00pp_coeff).reshape((1, 1, 3, 2, 11))

# op _00qO_power_combination_eval
# LANG: _00qt, _00qN --> _00qP
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0742__00qP = (v0738__00qt**1)*(v0746__00qN**1)
v0742__00qP = (v0742__00qP*_00qO_coeff).reshape((1, 1, 3, 2, 11))

# op _00qq_power_combination_eval
# LANG: _00qd, _00qp --> _00qr
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0727__00qr = (v0723__00qd**1)*(v0729__00qp**1)
v0727__00qr = (v0727__00qr*_00qq_coeff).reshape((1, 1, 3, 2, 11))

# op _00rD_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00rE
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((3,))
v0772__00rE = (v06_rotor_disk_in_plane_1**1)
v0772__00rE = (v0772__00rE*_00rD_coeff).reshape((3,))
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((1, 3))

# op _00t0_indexed_passthrough_eval
# LANG: _00s_, _00t2, _00t4 --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0810_V_aircraft__temp[i_v0809__00s___00t0_indexed_passthrough_eval] = v0809__00s_.flatten()
v0810_V_aircraft = v0810_V_aircraft__temp.copy()
v0810_V_aircraft__temp[i_v0811__00t2__00t0_indexed_passthrough_eval] = v0811__00t2.flatten()
v0810_V_aircraft = v0810_V_aircraft__temp.copy()
v0810_V_aircraft__temp[i_v0812__00t4__00t0_indexed_passthrough_eval] = v0812__00t4.flatten()
v0810_V_aircraft = v0810_V_aircraft__temp.copy()

# op _010H expand_array_eval
# LANG: rotor_disk_origin --> _010I
# SHAPES: (3,) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01807__010I = np.einsum('b,ac->abc', v01806_rotor_disk_origin.reshape((3,)) ,np.ones((1, 1))).reshape((1, 3, 1))

# op _010c_decompose_eval
# LANG: _0108 --> _010d, _010m, _010t
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01784__010d = ((v01783__0108.flatten())[src_indices__010d__010c]).reshape((1, 1, 1))
v01785__010m = ((v01783__0108.flatten())[src_indices__010m__010c]).reshape((1, 1, 1))
v01786__010t = ((v01783__0108.flatten())[src_indices__010t__010c]).reshape((1, 1, 1))

# op _010i_power_combination_eval
# LANG: _010f, _010h --> _010j
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01792__010j = (v01789__010f**1)*(v01795__010h**1)
v01792__010j = (v01792__010j*_010i_coeff).reshape((1, 1, 1))

# op _010p_power_combination_eval
# LANG: _010n, _010o --> _010q
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01799__010q = (v01790__010n**1)*(v01796__010o**1)
v01799__010q = (v01799__010q*_010p_coeff).reshape((1, 1, 1))

# op _00GB_power_combination_eval
# LANG: _angular_speed --> _00GC
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01324__00GC = (v01098__angular_speed**1)
v01324__00GC = (v01324__00GC*_00GB_coeff).reshape((1, 40, 30))

# op _00Xy_power_combination_eval
# LANG: _00Xv, _00Xx --> _00Xz
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01665__00Xz = (v01641__00Xv**1)*(v01673__00Xx**1)
v01665__00Xz = (v01665__00Xz*_00Xy_coeff).reshape((1, 1, 3, 40, 11))

# op _00Y1_power_combination_eval
# LANG: _00XZ, _00Y0 --> _00Y2
# SHAPES: (1, 1, 3, 40, 11), (1, 1, 3, 40, 11) --> (1, 1, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01695__00Y2 = (v01676__00XZ**1)*(v01696__00Y0**1)
v01695__00Y2 = (v01695__00Y2*_00Y1_coeff).reshape((1, 1, 3, 40, 11))

# op _00ZD_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00ZE
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((3,))
v01741__00ZE = (v06_rotor_disk_in_plane_1**1)
v01741__00ZE = (v01741__00ZE*_00ZD_coeff).reshape((3,))
v06_rotor_disk_in_plane_1 = v06_rotor_disk_in_plane_1.reshape((1, 3))

# op _00pT_power_combination_eval
# LANG: _00pq, term_1_coeff_A --> _00pU
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0716__00pU = (v0715_term_1_coeff_A**1)*(v0685__00pq**1)
v0716__00pU = (v0716__00pU*_00pT_coeff).reshape((1, 1, 3, 2, 11))

# op _00pV_power_combination_eval
# LANG: _00pQ, term_2_coeff_A --> _00pW
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0719__00pW = (v0718_term_2_coeff_A**1)*(v0703__00pQ**1)
v0719__00pW = (v0719__00pW*_00pV_coeff).reshape((1, 1, 3, 2, 11))

# op _00qQ_power_combination_eval
# LANG: term_1_coeff_B, _00qr --> _00qR
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0722__00qR = (v0721_term_1_coeff_B**1)*(v0727__00qr**1)
v0722__00qR = (v0722__00qR*_00qQ_coeff).reshape((1, 1, 3, 2, 11))

# op _00qS_power_combination_eval
# LANG: term_2_coeff_B, _00qP --> _00qT
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0737__00qT = (v0736_term_2_coeff_B**1)*(v0742__00qP**1)
v0737__00qT = (v0737__00qT*_00qS_coeff).reshape((1, 1, 3, 2, 11))

# op _00rF pnorm_eval
# LANG: _00rE --> _00rG
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0773__00rG = np.linalg.norm(v0772__00rE.flatten(), ord=2)

# op _00t5 expand_array_eval
# LANG: V_aircraft --> _00t6
# SHAPES: (1, 3) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0819__00t6 = np.einsum('ab,c->abc', v0810_V_aircraft.reshape((1, 3)) ,np.ones((1,))).reshape((1, 3, 1))

# op _00tb expand_scalar_eval
# LANG: time_vectors --> _00tc
# SHAPES: (1,) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0825__00tc = np.empty((1, 3, 1))
v0825__00tc.fill(v0824_time_vectors.item())

# op _010J_decompose_eval
# LANG: _010I --> _010K, _010P, _010U
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01808__010K = ((v01807__010I.flatten())[src_indices__010K__010J]).reshape((1, 1, 1))
v01809__010P = ((v01807__010I.flatten())[src_indices__010P__010J]).reshape((1, 1, 1))
v01810__010U = ((v01807__010I.flatten())[src_indices__010U__010J]).reshape((1, 1, 1))

# op _010k_linear_combination_eval
# LANG: _010d, _010j --> aircraft_x_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01787_aircraft_x_pos = _010k_constant+1*v01784__010d+1*v01792__010j

# op _010r_linear_combination_eval
# LANG: _010m, _010q --> aircraft_y_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01798_aircraft_y_pos = _010r_constant+1*v01785__010m+1*v01799__010q

# op _010w_power_combination_eval
# LANG: _010u, _010v --> _010x
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01801__010x = (v01791__010u**1)*(v01797__010v**1)
v01801__010x = (v01801__010x*_010w_coeff).reshape((1, 1, 1))

# op _00GD_power_combination_eval
# LANG: _00GC --> _00GE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01325__00GE = (v01324__00GC**1)
v01325__00GE = (v01325__00GE*_00GD_coeff).reshape((1, 40, 30))

# op _00Y3_single_tensor_sum_with_axis_eval
# LANG: _00Xz --> An
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01674_An = np.sum(v01665__00Xz, axis = (4,)).reshape((1, 1, 3, 40))

# op _00Y5_single_tensor_sum_with_axis_eval
# LANG: _00Y2 --> Bn
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01697_Bn = np.sum(v01695__00Y2, axis = (4,)).reshape((1, 1, 3, 40))

# op _00ZF pnorm_eval
# LANG: _00ZE --> _00ZG
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01742__00ZG = np.linalg.norm(v01741__00ZE.flatten(), ord=2)

# op _00ZK pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00ZL
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01744__00ZL = np.sum(v012_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00pX_linear_combination_eval
# LANG: _00pU, _00pW --> _00pY
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0717__00pY = _00pX_constant+1*v0716__00pU+1*v0719__00pW

# op _00qU_linear_combination_eval
# LANG: _00qR, _00qT --> _00qV
# SHAPES: (1, 1, 3, 2, 11), (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0735__00qV = _00qU_constant+1*v0722__00qR+1*v0737__00qT

# op _00rH_power_combination_eval
# LANG: _00rG --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0774_propeller_radius = (v0773__00rG**1)
v0774_propeller_radius = (v0774_propeller_radius*_00rH_coeff).reshape((1,))

# op _00t8 expand_array_eval
# LANG: aircraft_location --> _00t9
# SHAPES: (3, 1) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0814__00t9 = np.einsum('bc,a->abc', v0813_aircraft_location.reshape((3, 1)) ,np.ones((1,))).reshape((1, 3, 1))

# op _00tf_decompose_eval
# LANG: _00t6 --> _00tg, _00to, _00tv
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0820__00tg = ((v0819__00t6.flatten())[src_indices__00tg__00tf]).reshape((1, 1, 1))
v0821__00to = ((v0819__00t6.flatten())[src_indices__00to__00tf]).reshape((1, 1, 1))
v0822__00tv = ((v0819__00t6.flatten())[src_indices__00tv__00tf]).reshape((1, 1, 1))

# op _00th_decompose_eval
# LANG: _00tc --> _00ti, _00tp, _00tw
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0826__00ti = ((v0825__00tc.flatten())[src_indices__00ti__00th]).reshape((1, 1, 1))
v0827__00tp = ((v0825__00tc.flatten())[src_indices__00tp__00th]).reshape((1, 1, 1))
v0828__00tw = ((v0825__00tc.flatten())[src_indices__00tw__00th]).reshape((1, 1, 1))

# op _010A expand_scalar_eval
# LANG: init_obs_x_loc --> _010B
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01803__010B = np.empty((1, 1, 1))
v01803__010B.fill(v01802_init_obs_x_loc.item())

# op _010C expand_scalar_eval
# LANG: init_obs_y_loc --> _010D
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01812__010D = np.empty((1, 1, 1))
v01812__010D.fill(v01811_init_obs_y_loc.item())

# op _010L_linear_combination_eval
# LANG: aircraft_x_pos, _010K --> _010M
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01805__010M = _010L_constant+1*v01787_aircraft_x_pos+1*v01808__010K

# op _010Q_linear_combination_eval
# LANG: aircraft_y_pos, _010P --> _010R
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01814__010R = _010Q_constant+1*v01798_aircraft_y_pos+1*v01809__010P

# op _010y_linear_combination_eval
# LANG: _010t, _010x --> aircraft_z_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01800_aircraft_z_pos = _010y_constant+1*v01786__010t+1*v01801__010x

# op _00LW_single_tensor_sum_with_axis_eval
# LANG: _00GE --> _00LX
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01326__00LX = np.sum(v01325__00GE, axis = (1, 2)).reshape((1,))

# op _00M5_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00M6
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01331__00M6 = np.sum(v01086__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00Yb_decompose_eval
# LANG: n_var --> _00Yc
# SHAPES: (1, 1, 3, 40, 11) --> (1, 1, 3, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01698__00Yc = ((v01655_n_var.flatten())[src_indices__00Yc__00Yb]).reshape((1, 1, 3, 1, 1))

# op _00Z8_decompose_eval
# LANG: An --> _00Z9, _00Za
# SHAPES: (1, 1, 3, 40) --> (1, 1, 3, 39), (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01727__00Z9 = ((v01674_An.flatten())[src_indices__00Z9__00Z8]).reshape((1, 1, 3, 39))
v01728__00Za = ((v01674_An.flatten())[src_indices__00Za__00Z8]).reshape((1, 1, 3, 39))

# op _00ZH_power_combination_eval
# LANG: _00ZG --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01743_propeller_radius = (v01742__00ZG**1)
v01743_propeller_radius = (v01743_propeller_radius*_00ZH_coeff).reshape((1,))

# op _00ZM reshape_eval
# LANG: _00ZL --> _00ZN
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01745__00ZN = v01744__00ZL.reshape((40, 1))

# op _00Zn_decompose_eval
# LANG: Bn --> _00Zo, _00Zp
# SHAPES: (1, 1, 3, 40) --> (1, 1, 3, 39), (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01734__00Zo = ((v01697_Bn.flatten())[src_indices__00Zo__00Zn]).reshape((1, 1, 3, 39))
v01735__00Zp = ((v01697_Bn.flatten())[src_indices__00Zp__00Zn]).reshape((1, 1, 3, 39))

# op _00bh_power_combination_eval
# LANG: _angular_speed --> _00bi
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0440__00bi = (v0214__angular_speed**1)
v0440__00bi = (v0440__00bi*_00bh_coeff).reshape((1, 40, 100))

# op _00pZ_power_combination_eval
# LANG: _00pY --> An
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0720_An = (v0717__00pY**1)
v0720_An = (v0720_An*_00pZ_coeff).reshape((1, 1, 3, 2, 11))

# op _00qW_power_combination_eval
# LANG: _00qV --> Bn
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0753_Bn = (v0735__00qV**1)
v0753_Bn = (v0753_Bn*_00qW_coeff).reshape((1, 1, 3, 2, 11))

# op _00rK pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00rL
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0775__00rL = np.sum(v012_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00rR_power_combination_eval
# LANG: propeller_radius --> _00rS
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0778__00rS = (v0774_propeller_radius**1)
v0778__00rS = (v0778__00rS*_00rR_coeff).reshape((1,))

# op _00tI expand_array_eval
# LANG: rotor_disk_origin --> _00tJ
# SHAPES: (3,) --> (1, 3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((3,))
v0837__00tJ = np.einsum('b,ac->abc', v010_rotor_disk_origin.reshape((3,)) ,np.ones((1, 1))).reshape((1, 3, 1))
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((1, 3))

# op _00td_decompose_eval
# LANG: _00t9 --> _00te, _00tn, _00tu
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0815__00te = ((v0814__00t9.flatten())[src_indices__00te__00td]).reshape((1, 1, 1))
v0816__00tn = ((v0814__00t9.flatten())[src_indices__00tn__00td]).reshape((1, 1, 1))
v0817__00tu = ((v0814__00t9.flatten())[src_indices__00tu__00td]).reshape((1, 1, 1))

# op _00tj_power_combination_eval
# LANG: _00tg, _00ti --> _00tk
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0823__00tk = (v0820__00tg**1)*(v0826__00ti**1)
v0823__00tk = (v0823__00tk*_00tj_coeff).reshape((1, 1, 1))

# op _00tq_power_combination_eval
# LANG: _00to, _00tp --> _00tr
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0830__00tr = (v0821__00to**1)*(v0827__00tp**1)
v0830__00tr = (v0830__00tr*_00tq_coeff).reshape((1, 1, 1))

# op _010E expand_scalar_eval
# LANG: init_obs_z_loc --> _010F
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01816__010F = np.empty((1, 1, 1))
v01816__010F.fill(v01815_init_obs_z_loc.item())

# op _010N_linear_combination_eval
# LANG: _010B, _010M --> rel_obs_x_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01804_rel_obs_x_pos = _010N_constant+1*v01803__010B+-1*v01805__010M

# op _010S_linear_combination_eval
# LANG: _010D, _010R --> rel_obs_y_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01813_rel_obs_y_pos = _010S_constant+1*v01812__010D+-1*v01814__010R

# op _010V_linear_combination_eval
# LANG: aircraft_z_pos, _010U --> _010W
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01818__010W = _010V_constant+1*v01800_aircraft_z_pos+1*v01810__010U

# op _00KZ_single_tensor_sum_with_axis_eval
# LANG: _local_thrust --> _00K_
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01225__00K_ = np.sum(v01210__local_thrust, axis = (1, 2)).reshape((1,))

# op _00LY_power_combination_eval
# LANG: _00LX --> _00LZ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01327__00LZ = (v01326__00LX**1)
v01327__00LZ = (v01327__00LZ*_00LY_coeff).reshape((1,))

# op _00M7_power_combination_eval
# LANG: _00M6 --> _00M8
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01332__00M8 = (v01331__00M6**1)
v01332__00M8 = (v01332__00M8*_00M7_coeff).reshape((1,))

# op _00Yd reshape_eval
# LANG: _00Yc --> _00Ye
# SHAPES: (1, 1, 3, 1, 1) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01699__00Ye = v01698__00Yc.reshape((1, 1, 3))

# op _00Yh expand_array_eval
# LANG: _00QP --> _00Yi
# SHAPES: (1, 1) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01704__00Yi = np.einsum('ab,c->abc', v01471__00QP.reshape((1, 1)) ,np.ones((3,))).reshape((1, 1, 3))

# op _00ZO_power_combination_eval
# LANG: _00ZN --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01746_chord_profile = (v01745__00ZN**1)
v01746_chord_profile = (v01746_chord_profile*_00ZO_coeff).reshape((40, 1))

# op _00ZR_power_combination_eval
# LANG: propeller_radius --> _00ZS
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01747__00ZS = (v01743_propeller_radius**1)
v01747__00ZS = (v01747__00ZS*_00ZR_coeff).reshape((1,))

# op _00Zb_linear_combination_eval
# LANG: _00Z9, _00Za --> _00Zc
# SHAPES: (1, 1, 3, 39), (1, 1, 3, 39) --> (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01729__00Zc = _00Zb_constant+1*v01727__00Z9+1*v01728__00Za

# op _00Zd expand_scalar_eval
# LANG: dr --> _00Ze
# SHAPES: (1,) --> (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01731__00Ze = np.empty((1, 1, 3, 39))
v01731__00Ze.fill(v01368_dr.item())

# op _00Zq_linear_combination_eval
# LANG: _00Zo, _00Zp --> _00Zr
# SHAPES: (1, 1, 3, 39), (1, 1, 3, 39) --> (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01736__00Zr = _00Zq_constant+1*v01734__00Zo+1*v01735__00Zp

# op _00Zs expand_scalar_eval
# LANG: dr --> _00Zt
# SHAPES: (1,) --> (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01738__00Zt = np.empty((1, 1, 3, 39))
v01738__00Zt.fill(v01368_dr.item())

# op _00bj_power_combination_eval
# LANG: _00bi --> _00bk
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0441__00bk = (v0440__00bi**1)
v0441__00bk = (v0441__00bk*_00bj_coeff).reshape((1, 40, 100))

# op _00qY_single_tensor_sum_with_axis_eval
# LANG: An --> _00qZ
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0754__00qZ = np.sum(v0720_An, axis = (4,)).reshape((1, 1, 3, 2))

# op _00q__single_tensor_sum_with_axis_eval
# LANG: Bn --> _00r0
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0757__00r0 = np.sum(v0753_Bn, axis = (4,)).reshape((1, 1, 3, 2))

# op _00rM reshape_eval
# LANG: _00rL --> _00rN
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0776__00rN = v0775__00rL.reshape((40, 1))

# op _00rT_power_combination_eval
# LANG: _00rS --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0779_dr = (v0778__00rS**1)
v0779_dr = (v0779_dr*_00rT_coeff).reshape((1,))

# op _00tK_decompose_eval
# LANG: _00tJ --> _00tL, _00tQ, _00tV
# SHAPES: (1, 3, 1) --> (1, 1, 1), (1, 1, 1), (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0838__00tL = ((v0837__00tJ.flatten())[src_indices__00tL__00tK]).reshape((1, 1, 1))
v0839__00tQ = ((v0837__00tJ.flatten())[src_indices__00tQ__00tK]).reshape((1, 1, 1))
v0840__00tV = ((v0837__00tJ.flatten())[src_indices__00tV__00tK]).reshape((1, 1, 1))

# op _00tl_linear_combination_eval
# LANG: _00te, _00tk --> aircraft_x_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0818_aircraft_x_pos = _00tl_constant+1*v0815__00te+1*v0823__00tk

# op _00ts_linear_combination_eval
# LANG: _00tn, _00tr --> aircraft_y_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0829_aircraft_y_pos = _00ts_constant+1*v0816__00tn+1*v0830__00tr

# op _00tx_power_combination_eval
# LANG: _00tv, _00tw --> _00ty
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0832__00ty = (v0822__00tv**1)*(v0828__00tw**1)
v0832__00ty = (v0832__00ty*_00tx_coeff).reshape((1, 1, 1))

# op _00us reshape_eval
# LANG: rpm --> _00ut
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0868__00ut = v0162_rpm.reshape((1,))

# op _010X_linear_combination_eval
# LANG: _010F, _010W --> rel_obs_z_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01817_rel_obs_z_pos = _010X_constant+1*v01816__010F+-1*v01818__010W

# op _010Z_power_combination_eval
# LANG: rel_obs_x_pos --> _010_
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01819__010_ = (v01804_rel_obs_x_pos**2)
v01819__010_ = (v01819__010_*_010Z_coeff).reshape((1, 1, 1))

# op _0110_power_combination_eval
# LANG: rel_obs_y_pos --> _0111
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01821__0111 = (v01813_rel_obs_y_pos**2)
v01821__0111 = (v01821__0111*_0110_coeff).reshape((1, 1, 1))

# op _00L0_power_combination_eval
# LANG: _00K_ --> T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01226_T = (v01225__00K_**1)
v01226_T = (v01226_T*_00L0_coeff).reshape((1,))

# op _00L__power_combination_eval
# LANG: _00LZ --> _00M0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01328__00M0 = (v01327__00LZ**1)
v01328__00M0 = (v01328__00M0*_00L__coeff).reshape((1,))

# op _00M9_power_combination_eval
# LANG: _00M8 --> _00Ma
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01333__00Ma = (v01332__00M8**1)
v01333__00Ma = (v01333__00Ma*_00M9_coeff).reshape((1,))

# op _00YB_power_combination_eval
# LANG: _00Yi --> _00YC
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01714__00YC = (v01704__00Yi**1)
v01714__00YC = (v01714__00YC*_00YB_coeff).reshape((1, 1, 3))

# op _00Yf expand_scalar_eval
# LANG: _00Q_ --> _00Yg
# SHAPES: (1,) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01702__00Yg = np.empty((1, 1, 3))
v01702__00Yg.fill(v01492__00Q_.item())

# op _00Yj expand_scalar_eval
# LANG: speed_of_sound --> _00Yk
# SHAPES: (1,) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01707__00Yk = np.empty((1, 1, 3))
v01707__00Yk.fill(v01414_speed_of_sound.item())

# op _00Yl_power_combination_eval
# LANG: _00Ye --> _00Ym
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01700__00Ym = (v01699__00Ye**1)
v01700__00Ym = (v01700__00Ym*_00Yl_coeff).reshape((1, 1, 3))

# op _00Yp_power_combination_eval
# LANG: _00Yi --> _00Yq
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01705__00Yq = (v01704__00Yi**1)
v01705__00Yq = (v01705__00Yq*_00Yp_coeff).reshape((1, 1, 3))

# op _00Yx_power_combination_eval
# LANG: _00Ye --> _00Yy
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01711__00Yy = (v01699__00Ye**1)
v01711__00Yy = (v01711__00Yy*_00Yx_coeff).reshape((1, 1, 3))

# op _00ZT_power_combination_eval
# LANG: _00ZS --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01748_dr = (v01747__00ZS**1)
v01748_dr = (v01748_dr*_00ZT_coeff).reshape((1,))

# op _00Zf_power_combination_eval
# LANG: _00Zc, _00Ze --> _00Zg
# SHAPES: (1, 1, 3, 39), (1, 1, 3, 39) --> (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01730__00Zg = (v01729__00Zc**1)*(v01731__00Ze**1)
v01730__00Zg = (v01730__00Zg*_00Zf_coeff).reshape((1, 1, 3, 39))

# op _00Zu_power_combination_eval
# LANG: _00Zr, _00Zt --> _00Zv
# SHAPES: (1, 1, 3, 39), (1, 1, 3, 39) --> (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01737__00Zv = (v01736__00Zr**1)*(v01738__00Zt**1)
v01737__00Zv = (v01737__00Zv*_00Zu_coeff).reshape((1, 1, 3, 39))

# op _00gC_single_tensor_sum_with_axis_eval
# LANG: _00bk --> _00gD
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0442__00gD = np.sum(v0441__00bk, axis = (1, 2)).reshape((1,))

# op _00gM_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00gN
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0447__00gN = np.sum(v0202__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00r1_power_combination_eval
# LANG: _00qZ --> _00r2
# SHAPES: (1, 1, 3, 2) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0755__00r2 = (v0754__00qZ**2)
v0755__00r2 = (v0755__00r2*_00r1_coeff).reshape((1, 1, 3, 2))

# op _00r3_power_combination_eval
# LANG: _00r0 --> _00r4
# SHAPES: (1, 1, 3, 2) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0758__00r4 = (v0757__00r0**2)
v0758__00r4 = (v0758__00r4*_00r3_coeff).reshape((1, 1, 3, 2))

# op _00rO_power_combination_eval
# LANG: _00rN --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0777_chord_profile = (v0776__00rN**1)
v0777_chord_profile = (v0777_chord_profile*_00rO_coeff).reshape((40, 1))

# op _00tB expand_scalar_eval
# LANG: init_obs_x_loc --> _00tC
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0834__00tC = np.empty((1, 1, 1))
v0834__00tC.fill(v0833_init_obs_x_loc.item())

# op _00tD expand_scalar_eval
# LANG: init_obs_y_loc --> _00tE
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0842__00tE = np.empty((1, 1, 1))
v0842__00tE.fill(v0841_init_obs_y_loc.item())

# op _00tM_linear_combination_eval
# LANG: aircraft_x_pos, _00tL --> _00tN
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0836__00tN = _00tM_constant+1*v0818_aircraft_x_pos+1*v0838__00tL

# op _00tR_linear_combination_eval
# LANG: aircraft_y_pos, _00tQ --> _00tS
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0844__00tS = _00tR_constant+1*v0829_aircraft_y_pos+1*v0839__00tQ

# op _00tz_linear_combination_eval
# LANG: _00tu, _00ty --> aircraft_z_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0831_aircraft_z_pos = _00tz_constant+1*v0817__00tu+1*v0832__00ty

# op _00uZ expand_scalar_eval
# LANG: dr --> _00u_
# SHAPES: (1,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0864__00u_ = np.empty((40, 1))
v0864__00u_.fill(v0779_dr.item())

# op _00uu_power_combination_eval
# LANG: _00ut --> _00uv
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0869__00uv = (v0868__00ut**1)
v0869__00uv = (v0869__00uv*_00uu_coeff).reshape((1,))

# op _0112_linear_combination_eval
# LANG: _010_, _0111 --> _0113
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01820__0113 = _0112_constant+1*v01819__010_+1*v01821__0111

# op _0114_power_combination_eval
# LANG: rel_obs_z_pos --> _0115
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01823__0115 = (v01817_rel_obs_z_pos**2)
v01823__0115 = (v01823__0115*_0114_coeff).reshape((1, 1, 1))

# op _011J single_tensor_sum_no_axis_eval
# LANG: chord_profile --> _011K
# SHAPES: (40, 1) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01833__011K = np.sum(v01746_chord_profile).reshape((1,))

# op _011s_power_combination_eval
# LANG: rpm --> _011t
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v0162_rpm = v0162_rpm.reshape((1,))
v01841__011t = (v0162_rpm**1)
v01841__011t = (v01841__011t*_011s_coeff).reshape((1,))
v0162_rpm = v0162_rpm.reshape((1, 1))

# op _00LU_power_combination_eval
# LANG: T, density --> _00LV
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01127_density = v01127_density.reshape((1,))
v01322__00LV = (v01226_T**1)*(v01127_density**-1)
v01322__00LV = (v01322__00LV*_00LU_coeff).reshape((1,))
v01127_density = v01127_density.reshape((1, 1))

# op _00M1_power_combination_eval
# LANG: _00M0 --> _00M2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01329__00M2 = (v01328__00M0**2)
v01329__00M2 = (v01329__00M2*_00M1_coeff).reshape((1,))

# op _00Mb_power_combination_eval
# LANG: _00Ma --> _00Mc
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01334__00Mc = (v01333__00Ma**1)
v01334__00Mc = (v01334__00Mc*_00Mb_coeff).reshape((1,))

# op _00YD_power_combination_eval
# LANG: _00Yk, _00YC --> _00YE
# SHAPES: (1, 1, 3), (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01715__00YE = (v01714__00YC**1)*(v01707__00Yk**1)
v01715__00YE = (v01715__00YE*_00YD_coeff).reshape((1, 1, 3))

# op _00Yn_power_combination_eval
# LANG: _00Ym, _00Yg --> _00Yo
# SHAPES: (1, 1, 3), (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01701__00Yo = (v01700__00Ym**1)*(v01702__00Yg**1)
v01701__00Yo = (v01701__00Yo*_00Yn_coeff).reshape((1, 1, 3))

# op _00Yr_power_combination_eval
# LANG: _00Yq, _00Yk --> _00Ys
# SHAPES: (1, 1, 3), (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01706__00Ys = (v01705__00Yq**1)*(v01707__00Yk**1)
v01706__00Ys = (v01706__00Ys*_00Yr_coeff).reshape((1, 1, 3))

# op _00Yz_power_combination_eval
# LANG: _00Yg, _00Yy --> _00YA
# SHAPES: (1, 1, 3), (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01712__00YA = (v01711__00Yy**1)*(v01702__00Yg**1)
v01712__00YA = (v01712__00YA*_00Yz_coeff).reshape((1, 1, 3))

# op _00Zh_power_combination_eval
# LANG: _00Zg --> _00Zi
# SHAPES: (1, 1, 3, 39) --> (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01732__00Zi = (v01730__00Zg**1)
v01732__00Zi = (v01732__00Zi*_00Zh_coeff).reshape((1, 1, 3, 39))

# op _00Zw_power_combination_eval
# LANG: _00Zv --> _00Zx
# SHAPES: (1, 1, 3, 39) --> (1, 1, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01739__00Zx = (v01737__00Zv**1)
v01739__00Zx = (v01739__00Zx*_00Zw_coeff).reshape((1, 1, 3, 39))

# op _00fF_single_tensor_sum_with_axis_eval
# LANG: _local_thrust --> _00fG
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0341__00fG = np.sum(v0326__local_thrust, axis = (1, 2)).reshape((1,))

# op _00gE_power_combination_eval
# LANG: _00gD --> _00gF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0443__00gF = (v0442__00gD**1)
v0443__00gF = (v0443__00gF*_00gE_coeff).reshape((1,))

# op _00gO_power_combination_eval
# LANG: _00gN --> _00gP
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0448__00gP = (v0447__00gN**1)
v0448__00gP = (v0448__00gP*_00gO_coeff).reshape((1,))

# op _00r5_linear_combination_eval
# LANG: _00r2, _00r4 --> _00r6
# SHAPES: (1, 1, 3, 2), (1, 1, 3, 2) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0756__00r6 = _00r5_constant+1*v0755__00r2+1*v0758__00r4

# op _00tF expand_scalar_eval
# LANG: init_obs_z_loc --> _00tG
# SHAPES: (1,) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0846__00tG = np.empty((1, 1, 1))
v0846__00tG.fill(v0845_init_obs_z_loc.item())

# op _00tO_linear_combination_eval
# LANG: _00tC, _00tN --> rel_obs_x_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0835_rel_obs_x_pos = _00tO_constant+1*v0834__00tC+-1*v0836__00tN

# op _00tT_linear_combination_eval
# LANG: _00tE, _00tS --> rel_obs_y_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0843_rel_obs_y_pos = _00tT_constant+1*v0842__00tE+-1*v0844__00tS

# op _00tW_linear_combination_eval
# LANG: aircraft_z_pos, _00tV --> _00tX
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0848__00tX = _00tW_constant+1*v0831_aircraft_z_pos+1*v0840__00tV

# op _00uw_power_combination_eval
# LANG: _00uv --> _00ux
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0870__00ux = (v0869__00uv**1)
v0870__00ux = (v0870__00ux*_00uw_coeff).reshape((1,))

# op _00v0_power_combination_eval
# LANG: _00u_, chord_profile --> _00v1
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0863__00v1 = (v0777_chord_profile**1)*(v0864__00u_**1)
v0863__00v1 = (v0863__00v1*_00v0_coeff).reshape((40, 1))

# op _0116_linear_combination_eval
# LANG: _0113, _0115 --> _0117
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01822__0117 = _0116_constant+1*v01820__0113+1*v01823__0115

# op _011L_power_combination_eval
# LANG: _011K, dr --> _011M
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01834__011M = (v01833__011K**1)*(v01748_dr**1)
v01834__011M = (v01834__011M*_011L_coeff).reshape((1,))

# op _011R expand_scalar_eval
# LANG: propeller_radius --> _011S
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01838__011S = np.empty((1, 1))
v01838__011S.fill(v01743_propeller_radius.item())

# op _011u_power_combination_eval
# LANG: _011t --> _011v
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01842__011v = (v01841__011t**1)
v01842__011v = (v01842__011v*_011u_coeff).reshape((1,))

# op _00M3_power_combination_eval
# LANG: _00LV, _00M2 --> _00M4
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01323__00M4 = (v01322__00LV**1)*(v01329__00M2**-1)
v01323__00M4 = (v01323__00M4*_00M3_coeff).reshape((1,))

# op _00Md_power_combination_eval
# LANG: _00Mc --> _00Me
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01335__00Me = (v01334__00Mc**4)
v01335__00Me = (v01335__00Me*_00Md_coeff).reshape((1,))

# op _00YF_power_combination_eval
# LANG: _00YA, _00YE --> _00YG
# SHAPES: (1, 1, 3), (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01713__00YG = (v01712__00YA**1)*(v01715__00YE**-1)
v01713__00YG = (v01713__00YG*_00YF_coeff).reshape((1, 1, 3))

# op _00Yt_power_combination_eval
# LANG: _00Yo, _00Ys --> _00Yu
# SHAPES: (1, 1, 3), (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01703__00Yu = (v01701__00Yo**1)*(v01706__00Ys**-1)
v01703__00Yu = (v01703__00Yu*_00Yt_coeff).reshape((1, 1, 3))

# op _00Zj_single_tensor_sum_with_axis_eval
# LANG: _00Zi --> C_real_integrand
# SHAPES: (1, 1, 3, 39) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01733_C_real_integrand = np.sum(v01732__00Zi, axis = (3,)).reshape((1, 1, 3))

# op _00Zy_single_tensor_sum_with_axis_eval
# LANG: _00Zx --> C_imag_integrand
# SHAPES: (1, 1, 3, 39) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01740_C_imag_integrand = np.sum(v01739__00Zx, axis = (3,)).reshape((1, 1, 3))

# op _00fH_power_combination_eval
# LANG: _00fG --> T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0342_T = (v0341__00fG**1)
v0342_T = (v0342_T*_00fH_coeff).reshape((1,))

# op _00gG_power_combination_eval
# LANG: _00gF --> _00gH
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0444__00gH = (v0443__00gF**1)
v0444__00gH = (v0444__00gH*_00gG_coeff).reshape((1,))

# op _00gQ_power_combination_eval
# LANG: _00gP --> _00gR
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0449__00gR = (v0448__00gP**1)
v0449__00gR = (v0449__00gR*_00gQ_coeff).reshape((1,))

# op _00r7_power_combination_eval
# LANG: _00r6 --> _00r8
# SHAPES: (1, 1, 3, 2) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0759__00r8 = (v0756__00r6**1)
v0759__00r8 = (v0759__00r8*_00r7_coeff).reshape((1, 1, 3, 2))

# op _00tY_linear_combination_eval
# LANG: _00tG, _00tX --> rel_obs_z_pos
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0847_rel_obs_z_pos = _00tY_constant+1*v0846__00tG+-1*v0848__00tX

# op _00t__power_combination_eval
# LANG: rel_obs_x_pos --> _00u0
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0849__00u0 = (v0835_rel_obs_x_pos**2)
v0849__00u0 = (v0849__00u0*_00t__coeff).reshape((1, 1, 1))

# op _00u1_power_combination_eval
# LANG: rel_obs_y_pos --> _00u2
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0851__00u2 = (v0843_rel_obs_y_pos**2)
v0851__00u2 = (v0851__00u2*_00u1_coeff).reshape((1, 1, 1))

# op _00uy_power_combination_eval
# LANG: _00ux --> _00uz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0871__00uz = (v0870__00ux**1)
v0871__00uz = (v0871__00uz*_00uy_coeff).reshape((1,))

# op _00v2_single_tensor_sum_with_axis_eval
# LANG: _00v1 --> _00v3
# SHAPES: (40, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0865__00v3 = np.sum(v0863__00v1, axis = (0,)).reshape((1,))

# op _0118_power_combination_eval
# LANG: _0117 --> rel_obs_dist
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01824_rel_obs_dist = (v01822__0117**0.5)
v01824_rel_obs_dist = (v01824_rel_obs_dist*_0118_coeff).reshape((1, 1, 1))

# op _011N expand_scalar_eval
# LANG: _011M --> _011O
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01835__011O = np.empty((1, 1))
v01835__011O.fill(v01834__011M.item())

# op _011T_power_combination_eval
# LANG: _011S --> _011U
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01839__011U = (v01838__011S**2)
v01839__011U = (v01839__011U*_011T_coeff).reshape((1, 1))

# op _011w_power_combination_eval
# LANG: _011v --> _011x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01843__011x = (v01842__011v**1)
v01843__011x = (v01843__011x*_011w_coeff).reshape((1,))

# op _011y expand_scalar_eval
# LANG: propeller_radius --> _011z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01845__011z = np.empty((1,))
v01845__011z.fill(v01743_propeller_radius.item())

# op _00Mf_power_combination_eval
# LANG: _00M4, _00Me --> C_T
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01330_C_T = (v01323__00M4**1)*(v01335__00Me**-1)
v01330_C_T = (v01330_C_T*_00Mf_coeff).reshape((1,))

# op _00YH_power_combination_eval
# LANG: _00YG, C_imag_integrand --> _00YI
# SHAPES: (1, 1, 3), (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01716__00YI = (v01713__00YG**1)*(v01740_C_imag_integrand**1)
v01716__00YI = (v01716__00YI*_00YH_coeff).reshape((1, 1, 3))

# op _00Yv_power_combination_eval
# LANG: _00Yu, C_real_integrand --> _00Yw
# SHAPES: (1, 1, 3), (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01708__00Yw = (v01703__00Yu**1)*(v01733_C_real_integrand**1)
v01708__00Yw = (v01708__00Yw*_00Yv_coeff).reshape((1, 1, 3))

# op _00gA_power_combination_eval
# LANG: T, density --> _00gB
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0243_density = v0243_density.reshape((1,))
v0438__00gB = (v0342_T**1)*(v0243_density**-1)
v0438__00gB = (v0438__00gB*_00gA_coeff).reshape((1,))
v0243_density = v0243_density.reshape((1, 1))

# op _00gI_power_combination_eval
# LANG: _00gH --> _00gJ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0445__00gJ = (v0444__00gH**2)
v0445__00gJ = (v0445__00gJ*_00gI_coeff).reshape((1,))

# op _00gS_power_combination_eval
# LANG: _00gR --> _00gT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0450__00gT = (v0449__00gR**1)
v0450__00gT = (v0450__00gT*_00gS_coeff).reshape((1,))

# op _00r9_log10_eval
# LANG: _00r8 --> _00ra
# SHAPES: (1, 1, 3, 2) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0760__00ra = np.log10(v0759__00r8)

# op _00u3_linear_combination_eval
# LANG: _00u0, _00u2 --> _00u4
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0850__00u4 = _00u3_constant+1*v0849__00u0+1*v0851__00u2

# op _00u5_power_combination_eval
# LANG: rel_obs_z_pos --> _00u6
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0853__00u6 = (v0847_rel_obs_z_pos**2)
v0853__00u6 = (v0853__00u6*_00u5_coeff).reshape((1, 1, 1))

# op _00uA_linear_combination_eval
# LANG: _00uz --> _00uB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0872__00uB = _00uA_constant+1*v0871__00uz

# op _00v4_power_combination_eval
# LANG: _00v3 --> _00v5
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0866__00v5 = (v0865__00v3**1)
v0866__00v5 = (v0866__00v5*_00v4_coeff).reshape((1,))

# op _011A_power_combination_eval
# LANG: _011x, _011z --> _011B
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01844__011B = (v01843__011x**1)*(v01845__011z**1)
v01844__011B = (v01844__011B*_011A_coeff).reshape((1,))

# op _011P_power_combination_eval
# LANG: _011O --> Ab
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01836_Ab = (v01835__011O**1)
v01836_Ab = (v01836_Ab*_011P_coeff).reshape((1, 1))

# op _011V_power_combination_eval
# LANG: _011U --> _011W
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01840__011W = (v01839__011U**1)
v01840__011W = (v01840__011W*_011V_coeff).reshape((1, 1))

# op _0132 reshape_eval
# LANG: rel_obs_dist --> _0133
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01882__0133 = v01824_rel_obs_dist.reshape((1, 1))

# op _0135 reshape_eval
# LANG: rel_obs_z_pos --> _0136
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01880__0136 = v01817_rel_obs_z_pos.reshape((1, 1))

# op _00NH_power_combination_eval
# LANG: rpm --> _00NI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01370__00NI = (v0162_rpm**1)
v01370__00NI = (v01370__00NI*_00NH_coeff).reshape((1, 1))

# op _00YJ_power_combination_eval
# LANG: _00Yw --> _00YK
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01709__00YK = (v01708__00Yw**2)
v01709__00YK = (v01709__00YK*_00YJ_coeff).reshape((1, 1, 3))

# op _00YL_power_combination_eval
# LANG: _00YI --> _00YM
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01717__00YM = (v01716__00YI**2)
v01717__00YM = (v01717__00YM*_00YL_coeff).reshape((1, 1, 3))

# op _00ZX_power_combination_eval
# LANG: rpm --> _00ZY
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01750__00ZY = (v0162_rpm**1)
v01750__00ZY = (v01750__00ZY*_00ZX_coeff).reshape((1, 1))

# op _00gK_power_combination_eval
# LANG: _00gB, _00gJ --> _00gL
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0439__00gL = (v0438__00gB**1)*(v0445__00gJ**-1)
v0439__00gL = (v0439__00gL*_00gK_coeff).reshape((1,))

# op _00gU_power_combination_eval
# LANG: _00gT --> _00gV
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0451__00gV = (v0450__00gT**4)
v0451__00gV = (v0451__00gV*_00gU_coeff).reshape((1,))

# op _00iu_power_combination_eval
# LANG: rpm --> _00iv
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0488__00iv = (v0162_rpm**1)
v0488__00iv = (v0488__00iv*_00iu_coeff).reshape((1, 1))

# op _00rY_power_combination_eval
# LANG: rpm --> _00rZ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0781__00rZ = (v0162_rpm**1)
v0781__00rZ = (v0781__00rZ*_00rY_coeff).reshape((1, 1))

# op _00rb_power_combination_eval
# LANG: _00ra --> bladeSPL
# SHAPES: (1, 1, 3, 2) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0761_bladeSPL = (v0760__00ra**1)
v0761_bladeSPL = (v0761_bladeSPL*_00rb_coeff).reshape((1, 1, 3, 2))

# op _00u7_linear_combination_eval
# LANG: _00u4, _00u6 --> _00u8
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0852__00u8 = _00u7_constant+1*v0850__00u4+1*v0853__00u6

# op _00uC expand_scalar_eval
# LANG: _00uB --> _00uD
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0873__00uD = np.empty((1, 1))
v0873__00uD.fill(v0872__00uB.item())

# op _00uF expand_scalar_eval
# LANG: propeller_radius --> _00uG
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0876__00uG = np.empty((1, 1))
v0876__00uG.fill(v0774_propeller_radius.item())

# op _00uL reshape_eval
# LANG: rel_obs_z_pos --> _00uM
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0891__00uM = v0847_rel_obs_z_pos.reshape((1, 1))

# op _00v6 expand_scalar_eval
# LANG: _00v5 --> Ab
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0867_Ab = np.empty((1, 1))
v0867_Ab.fill(v0866__00v5.item())

# op _011C expand_scalar_eval
# LANG: _011B --> _011D
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01846__011D = np.empty((1, 1))
v01846__011D.fill(v01844__011B.item())

# op _011F expand_scalar_eval
# LANG: CT --> _011G
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01851__011G = np.empty((1, 1))
v01851__011G.fill(v01330_C_T.item())

# op _011X_power_combination_eval
# LANG: Ab, _011W --> sigma
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01837_sigma = (v01836_Ab**1)*(v01840__011W**-1)
v01837_sigma = (v01837_sigma*_011X_coeff).reshape((1, 1))

# op _0137_power_combination_eval
# LANG: _0136, _0133 --> _0138
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01881__0138 = (v01880__0136**1)*(v01882__0133**-1)
v01881__0138 = (v01881__0138*_0137_coeff).reshape((1, 1))

# op _00NJ_power_combination_eval
# LANG: _00NI --> _00NK
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01371__00NK = (v01370__00NI**1)
v01371__00NK = (v01371__00NK*_00NJ_coeff).reshape((1, 1))

# op _00YN_linear_combination_eval
# LANG: _00YK, _00YM --> _00YO
# SHAPES: (1, 1, 3), (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01710__00YO = _00YN_constant+1*v01709__00YK+1*v01717__00YM

# op _00ZZ_power_combination_eval
# LANG: _00ZY --> _00Z_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01751__00Z_ = (v01750__00ZY**1)
v01751__00Z_ = (v01751__00Z_*_00ZZ_coeff).reshape((1, 1))

# op _00gW_power_combination_eval
# LANG: _00gL, _00gV --> C_T
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0446_C_T = (v0439__00gL**1)*(v0451__00gV**-1)
v0446_C_T = (v0446_C_T*_00gW_coeff).reshape((1,))

# op _00iw_power_combination_eval
# LANG: _00iv --> _00ix
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0489__00ix = (v0488__00iv**1)
v0489__00ix = (v0489__00ix*_00iw_coeff).reshape((1, 1))

# op _00r__power_combination_eval
# LANG: _00rZ --> _00s0
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0782__00s0 = (v0781__00rZ**1)
v0782__00s0 = (v0782__00s0*_00r__coeff).reshape((1, 1))

# op _00rd_power_combination_eval
# LANG: bladeSPL --> _00re
# SHAPES: (1, 1, 3, 2) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0762__00re = (v0761_bladeSPL**1)
v0762__00re = (v0762__00re*_00rd_coeff).reshape((1, 1, 3, 2))

# op _00u9_power_combination_eval
# LANG: _00u8 --> rel_obs_dist
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0854_rel_obs_dist = (v0852__00u8**0.5)
v0854_rel_obs_dist = (v0854_rel_obs_dist*_00u9_coeff).reshape((1, 1, 1))

# op _00uN_power_combination_eval
# LANG: _00uM --> _00uO
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0892__00uO = (v0891__00uM**2)
v0892__00uO = (v0892__00uO*_00uN_coeff).reshape((1, 1))

# op _00uV_linear_combination_eval
# LANG: _00uD --> _00uW
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0874__00uW = _00uV_constant+1*v0873__00uD

# op _00v8_power_combination_eval
# LANG: Ab --> _00v9
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0882__00v9 = (v0867_Ab**1)
v0882__00v9 = (v0882__00v9*_00v8_coeff).reshape((1, 1))

# op _00va_power_combination_eval
# LANG: _00uG --> _00vb
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0884__00vb = (v0876__00uG**2)
v0884__00vb = (v0884__00vb*_00va_coeff).reshape((1, 1))

# op _011Z_power_combination_eval
# LANG: _011D --> _011_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01847__011_ = (v01846__011D**3.68)
v01847__011_ = (v01847__011_*_011Z_coeff).reshape((1, 1))

# op _0120_power_combination_eval
# LANG: Ab --> _0121
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01849__0121 = (v01836_Ab**0.9)
v01849__0121 = (v01849__0121*_0120_coeff).reshape((1, 1))

# op _0124_power_combination_eval
# LANG: sigma, _011G --> _0125
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01852__0125 = (v01851__011G**1)*(v01837_sigma**-1)
v01852__0125 = (v01852__0125*_0124_coeff).reshape((1, 1))

# op _012g_power_combination_eval
# LANG: _011D --> _012h
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01864__012h = (v01846__011D**7.44)
v01864__012h = (v01864__012h*_012g_coeff).reshape((1, 1))

# op _012i_power_combination_eval
# LANG: Ab --> _012j
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01866__012j = (v01836_Ab**0.9)
v01866__012j = (v01866__012j*_012i_coeff).reshape((1, 1))

# op _012m_power_combination_eval
# LANG: sigma, _011G --> _012n
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01868__012n = (v01851__011G**1)*(v01837_sigma**-1)
v01868__012n = (v01868__012n*_012m_coeff).reshape((1, 1))

# op _0139_arcsin_eval
# LANG: _0138 --> _013a
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01883__013a = np.arcsin(v01881__0138)

# op _00NL_power_combination_eval
# LANG: _00NK --> _00NM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01372__00NM = (v01371__00NK**1)
v01372__00NM = (v01372__00NM*_00NL_coeff).reshape((1, 1))

# op _00YP_power_combination_eval
# LANG: _00YO --> _00YQ
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01718__00YQ = (v01710__00YO**1)
v01718__00YQ = (v01718__00YQ*_00YP_coeff).reshape((1, 1, 3))

# op _00_0_power_combination_eval
# LANG: _00Z_ --> _00_1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01752__00_1 = (v01751__00Z_**1)
v01752__00_1 = (v01752__00_1*_00_0_coeff).reshape((1, 1))

# op _00iy_power_combination_eval
# LANG: _00ix --> _00iz
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0490__00iz = (v0489__00ix**1)
v0490__00iz = (v0490__00iz*_00iy_coeff).reshape((1, 1))

# op _00rf_exp_a_eval
# LANG: _00re --> _00rg
# SHAPES: (1, 1, 3, 2) --> (1, 1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0763__00rg = _00rf_exp_a_eval_a**v0762__00re

# op _00s1_power_combination_eval
# LANG: _00s0 --> _00s2
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0783__00s2 = (v0782__00s0**1)
v0783__00s2 = (v0783__00s2*_00s1_coeff).reshape((1, 1))

# op _00uI reshape_eval
# LANG: rel_obs_dist --> _00uJ
# SHAPES: (1, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0895__00uJ = v0854_rel_obs_dist.reshape((1, 1))

# op _00uP_power_combination_eval
# LANG: _00uO --> _00uQ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0893__00uQ = (v0892__00uO**0.5)
v0893__00uQ = (v0893__00uQ*_00uP_coeff).reshape((1, 1))

# op _00vc_power_combination_eval
# LANG: _00v9, _00vb --> _00vd
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0883__00vd = (v0882__00v9**1)*(v0884__00vb**-1)
v0883__00vd = (v0883__00vd*_00vc_coeff).reshape((1, 1))

# op _00vf expand_scalar_eval
# LANG: CT --> _00vg
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0880__00vg = np.empty((1, 1))
v0880__00vg.fill(v0446_C_T.item())

# op _00vh_power_combination_eval
# LANG: _00uW, _00uG --> _00vi
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0875__00vi = (v0874__00uW**1)*(v0876__00uG**1)
v0875__00vi = (v0875__00vi*_00vh_coeff).reshape((1, 1))

# op _0122_power_combination_eval
# LANG: _011_, _0121 --> _0123
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01848__0123 = (v01847__011_**1)*(v01849__0121**1)
v01848__0123 = (v01848__0123*_0122_coeff).reshape((1, 1))

# op _0126_power_combination_eval
# LANG: _0125 --> _0127
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01853__0127 = (v01852__0125**1.6)
v01853__0127 = (v01853__0127*_0126_coeff).reshape((1, 1))

# op _012K_linear_combination_eval
# LANG: Ab --> _012L
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01874__012L = _012K_constant+1*v01836_Ab

# op _012k_power_combination_eval
# LANG: _012h, _012j --> _012l
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01865__012l = (v01864__012h**1)*(v01866__012j**1)
v01865__012l = (v01865__012l*_012k_coeff).reshape((1, 1))

# op _012o_power_combination_eval
# LANG: _012n --> _012p
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01869__012p = (v01868__012n**1.6)
v01869__012p = (v01869__012p*_012o_coeff).reshape((1, 1))

# op _012y_linear_combination_eval
# LANG: Ab --> _012z
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01858__012z = _012y_constant+-1*v01836_Ab

# op _013b reshape_eval
# LANG: _013a --> _013c
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01884__013c = v01883__013a.reshape((1, 1))

# op _00NW_power_combination_eval
# LANG: _00NM --> _00NX
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01379__00NX = (v01372__00NM**2)
v01379__00NX = (v01379__00NX*_00NW_coeff).reshape((1, 1))

# op _00N__power_combination_eval
# LANG: _00NM --> _00O0
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01382__00O0 = (v01372__00NM**2)
v01382__00O0 = (v01382__00O0*_00N__coeff).reshape((1, 1))

# op _00YR_power_combination_eval
# LANG: _00YQ --> _00YS
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01719__00YS = (v01718__00YQ**1)
v01719__00YS = (v01719__00YS*_00YR_coeff).reshape((1, 1, 3))

# op _00_b_power_combination_eval
# LANG: _00_1 --> _00_c
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01759__00_c = (v01752__00_1**2)
v01759__00_c = (v01759__00_c*_00_b_coeff).reshape((1, 1))

# op _00_f_power_combination_eval
# LANG: _00_1 --> _00_g
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01762__00_g = (v01752__00_1**2)
v01762__00_g = (v01762__00_g*_00_f_coeff).reshape((1, 1))

# op _00iJ_power_combination_eval
# LANG: _00iz --> _00iK
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0497__00iK = (v0490__00iz**2)
v0497__00iK = (v0497__00iK*_00iJ_coeff).reshape((1, 1))

# op _00iN_power_combination_eval
# LANG: _00iz --> _00iO
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0500__00iO = (v0490__00iz**2)
v0500__00iO = (v0500__00iO*_00iN_coeff).reshape((1, 1))

# op _00rh_single_tensor_sum_with_axis_eval
# LANG: _00rg --> _00ri
# SHAPES: (1, 1, 3, 2) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0764__00ri = np.sum(v0763__00rg, axis = (3,)).reshape((1, 1, 3))

# op _00sc_power_combination_eval
# LANG: _00s2 --> _00sd
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0790__00sd = (v0783__00s2**2)
v0790__00sd = (v0790__00sd*_00sc_coeff).reshape((1, 1))

# op _00sg_power_combination_eval
# LANG: _00s2 --> _00sh
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0793__00sh = (v0783__00s2**2)
v0793__00sh = (v0793__00sh*_00sg_coeff).reshape((1, 1))

# op _00uR_power_combination_eval
# LANG: _00uQ, _00uJ --> _00uS
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0894__00uS = (v0893__00uQ**1)*(v0895__00uJ**-1)
v0894__00uS = (v0894__00uS*_00uR_coeff).reshape((1, 1))

# op _00vj_power_combination_eval
# LANG: _00vi --> _00vk
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0877__00vk = (v0875__00vi**6)
v0877__00vk = (v0877__00vk*_00vj_coeff).reshape((1, 1))

# op _00vn_power_combination_eval
# LANG: _00vg, _00vd --> _00vo
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0881__00vo = (v0880__00vg**1)*(v0883__00vd**-1)
v0881__00vo = (v0881__00vo*_00vn_coeff).reshape((1, 1))

# op _0128_power_combination_eval
# LANG: _0123, _0127 --> _0129
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01850__0129 = (v01848__0123**1)*(v01853__0127**1)
v01850__0129 = (v01850__0129*_0128_coeff).reshape((1, 1))

# op _012A_power_combination_eval
# LANG: _012z --> _012B
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01859__012B = (v01858__012z**1)
v01859__012B = (v01859__012B*_012A_coeff).reshape((1, 1))

# op _012M_power_combination_eval
# LANG: _012L --> _012N
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01875__012N = (v01874__012L**1)
v01875__012N = (v01875__012N*_012M_coeff).reshape((1, 1))

# op _012q_power_combination_eval
# LANG: _012l, _012p --> _012r
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01867__012r = (v01865__012l**1)*(v01869__012p**1)
v01867__012r = (v01867__012r*_012q_coeff).reshape((1, 1))

# op _013r_power_combination_eval
# LANG: _013c --> _013s
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01895__013s = (v01884__013c**2)
v01895__013s = (v01895__013s*_013r_coeff).reshape((1, 1))

# op _00IR_power_combination_eval
# LANG: _radius --> _00IS
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01227__00IS = (v01099__radius**2)
v01227__00IS = (v01227__00IS*_00IR_coeff).reshape((1, 40, 30))

# op _00NY_linear_combination_eval
# LANG: _00NX --> _00NZ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01380__00NZ = _00NY_constant+1*v01379__00NX

# op _00O1_linear_combination_eval
# LANG: _00O0 --> _00O2
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01383__00O2 = _00O1_constant+1*v01382__00O0

# op _00YT_log10_eval
# LANG: _00YS --> _00YU
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01720__00YU = np.log10(v01719__00YS)

# op _00_d_linear_combination_eval
# LANG: _00_c --> _00_e
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01760__00_e = _00_d_constant+1*v01759__00_c

# op _00_h_linear_combination_eval
# LANG: _00_g --> _00_i
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01763__00_i = _00_h_constant+1*v01762__00_g

# op _00dx_power_combination_eval
# LANG: _radius --> _00dy
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0343__00dy = (v0215__radius**2)
v0343__00dy = (v0343__00dy*_00dx_coeff).reshape((1, 40, 100))

# op _00iL_linear_combination_eval
# LANG: _00iK --> _00iM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0498__00iM = _00iL_constant+1*v0497__00iK

# op _00iP_linear_combination_eval
# LANG: _00iO --> _00iQ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0501__00iQ = _00iP_constant+1*v0500__00iO

# op _00rj_log10_eval
# LANG: _00ri --> _00rk
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0765__00rk = np.log10(v0764__00ri)

# op _00se_linear_combination_eval
# LANG: _00sd --> _00sf
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0791__00sf = _00se_constant+1*v0790__00sd

# op _00si_linear_combination_eval
# LANG: _00sh --> _00sj
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0794__00sj = _00si_constant+1*v0793__00sh

# op _00uT_arcsin_eval
# LANG: _00uS --> _00uU
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0896__00uU = np.arcsin(v0894__00uS)

# op _00vl_power_combination_eval
# LANG: Ab, _00vk --> _00vm
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0878__00vm = (v0877__00vk**1)*(v0867_Ab**1)
v0878__00vm = (v0878__00vm*_00vl_coeff).reshape((1, 1))

# op _00vp_power_combination_eval
# LANG: _00vo --> _00vq
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0885__00vq = (v0881__00vo**2)
v0885__00vq = (v0885__00vq*_00vp_coeff).reshape((1, 1))

# op _012C_tanh_eval
# LANG: _012B --> _012D
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01860__012D = np.tanh(v01859__012B)

# op _012O_tanh_eval
# LANG: _012N --> _012P
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01876__012P = np.tanh(v01875__012N)

# op _012a_log10_eval
# LANG: _0129 --> _012b
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01854__012b = np.log10(v01850__0129)

# op _012s_log10_eval
# LANG: _012r --> _012t
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01870__012t = np.log10(v01867__012r)

# op _013t_power_combination_eval
# LANG: _013s --> _013u
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01896__013u = (v01895__013s**0.5)
v01896__013u = (v01896__013u*_013t_coeff).reshape((1, 1))

# op _00IT_power_combination_eval
# LANG: _00IS --> _00IU
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01228__00IU = (v01227__00IS**1)
v01228__00IU = (v01228__00IU*_00IT_coeff).reshape((1, 40, 30))

# op _00NS_power_combination_eval
# LANG: _00NM --> _00NT
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01376__00NT = (v01372__00NM**2)
v01376__00NT = (v01376__00NT*_00NS_coeff).reshape((1, 1))

# op _00O3_power_combination_eval
# LANG: _00NZ, _00O2 --> _00O4
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01381__00O4 = (v01380__00NZ**1)*(v01383__00O2**1)
v01381__00O4 = (v01381__00O4*_00O3_coeff).reshape((1, 1))

# op _00YV_power_combination_eval
# LANG: _00YU --> _00YW
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01721__00YW = (v01720__00YU**1)
v01721__00YW = (v01721__00YW*_00YV_coeff).reshape((1, 1, 3))

# op _00_7_power_combination_eval
# LANG: _00_1 --> _00_8
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01756__00_8 = (v01752__00_1**2)
v01756__00_8 = (v01756__00_8*_00_7_coeff).reshape((1, 1))

# op _00_j_power_combination_eval
# LANG: _00_e, _00_i --> _00_k
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01761__00_k = (v01760__00_e**1)*(v01763__00_i**1)
v01761__00_k = (v01761__00_k*_00_j_coeff).reshape((1, 1))

# op _00dz_power_combination_eval
# LANG: _00dy --> _00dA
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0344__00dA = (v0343__00dy**1)
v0344__00dA = (v0344__00dA*_00dz_coeff).reshape((1, 40, 100))

# op _00iF_power_combination_eval
# LANG: _00iz --> _00iG
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0494__00iG = (v0490__00iz**2)
v0494__00iG = (v0494__00iG*_00iF_coeff).reshape((1, 1))

# op _00iR_power_combination_eval
# LANG: _00iM, _00iQ --> _00iS
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0499__00iS = (v0498__00iM**1)*(v0501__00iQ**1)
v0499__00iS = (v0499__00iS*_00iR_coeff).reshape((1, 1))

# op _00rl_power_combination_eval
# LANG: _00rk --> _00rm
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0766__00rm = (v0765__00rk**1)
v0766__00rm = (v0766__00rm*_00rl_coeff).reshape((1, 1, 3))

# op _00s8_power_combination_eval
# LANG: _00s2 --> _00s9
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0787__00s9 = (v0783__00s2**2)
v0787__00s9 = (v0787__00s9*_00s8_coeff).reshape((1, 1))

# op _00sk_power_combination_eval
# LANG: _00sf, _00sj --> _00sl
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0792__00sl = (v0791__00sf**1)*(v0794__00sj**1)
v0792__00sl = (v0792__00sl*_00sk_coeff).reshape((1, 1))

# op _00vB_sin_eval
# LANG: _00uU --> _00vC
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0897__00vC = np.sin(v0896__00uU)

# op _00vD_power_combination_eval
# LANG: _00uJ --> _00vE
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0899__00vE = (v0895__00uJ**1)
v0899__00vE = (v0899__00vE*_00vD_coeff).reshape((1, 1))

# op _00vr_power_combination_eval
# LANG: _00vm, _00vq --> _00vs
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0879__00vs = (v0878__00vm**1)*(v0885__00vq**1)
v0879__00vs = (v0879__00vs*_00vr_coeff).reshape((1, 1))

# op _012E_power_combination_eval
# LANG: _012D --> _012F
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01861__012F = (v01860__012D**1)
v01861__012F = (v01861__012F*_012E_coeff).reshape((1, 1))

# op _012Q_power_combination_eval
# LANG: _012P --> _012R
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01877__012R = (v01876__012P**1)
v01877__012R = (v01877__012R*_012Q_coeff).reshape((1, 1))

# op _012Y_power_combination_eval
# LANG: propeller_radius --> _012Z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01891__012Z = (v01743_propeller_radius**1)
v01891__012Z = (v01891__012Z*_012Y_coeff).reshape((1,))

# op _012c_power_combination_eval
# LANG: _012b --> _012d
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01855__012d = (v01854__012b**1)
v01855__012d = (v01855__012d*_012c_coeff).reshape((1, 1))

# op _012u_power_combination_eval
# LANG: _012t --> _012v
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01871__012v = (v01870__012t**1)
v01871__012v = (v01871__012v*_012u_coeff).reshape((1, 1))

# op _013d_power_combination_eval
# LANG: _013c --> _013e
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01885__013e = (v01884__013c**2.0)
v01885__013e = (v01885__013e*_013d_coeff).reshape((1, 1))

# op _013v_sin_eval
# LANG: _013u --> _013w
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01897__013w = np.sin(v01896__013u)

# op _00IV_power_combination_eval
# LANG: _00GM, _00IU --> _00IW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01229__00IW = (v01228__00IU**1)*(v01205__00GM**1)
v01229__00IW = (v01229__00IW*_00IV_coeff).reshape((1, 40, 30))

# op _00NU_linear_combination_eval
# LANG: _00NT --> _00NV
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01377__00NV = _00NU_constant+1*v01376__00NT

# op _00O5_power_combination_eval
# LANG: _00O4 --> _00O6
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01384__00O6 = (v01381__00O4**0.5)
v01384__00O6 = (v01384__00O6*_00O5_coeff).reshape((1, 1))

# op _00O9_power_combination_eval
# LANG: _00NM --> _00Oa
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01386__00Oa = (v01372__00NM**2)
v01386__00Oa = (v01386__00Oa*_00O9_coeff).reshape((1, 1))

# op _00YX_power_combination_eval
# LANG: _00YW --> _00YY
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01722__00YY = (v01721__00YW**1)
v01722__00YY = (v01722__00YY*_00YX_coeff).reshape((1, 1, 3))

# op _00_9_linear_combination_eval
# LANG: _00_8 --> _00_a
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01757__00_a = _00_9_constant+1*v01756__00_8

# op _00_l_power_combination_eval
# LANG: _00_k --> _00_m
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01764__00_m = (v01761__00_k**0.5)
v01764__00_m = (v01764__00_m*_00_l_coeff).reshape((1, 1))

# op _00_p_power_combination_eval
# LANG: _00_1 --> _00_q
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01766__00_q = (v01752__00_1**2)
v01766__00_q = (v01766__00_q*_00_p_coeff).reshape((1, 1))

# op _00dB_power_combination_eval
# LANG: _00bs, _00dA --> _00dC
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0345__00dC = (v0344__00dA**1)*(v0321__00bs**1)
v0345__00dC = (v0345__00dC*_00dB_coeff).reshape((1, 40, 100))

# op _00iH_linear_combination_eval
# LANG: _00iG --> _00iI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0495__00iI = _00iH_constant+1*v0494__00iG

# op _00iT_power_combination_eval
# LANG: _00iS --> _00iU
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0502__00iU = (v0499__00iS**0.5)
v0502__00iU = (v0502__00iU*_00iT_coeff).reshape((1, 1))

# op _00iX_power_combination_eval
# LANG: _00iz --> _00iY
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0504__00iY = (v0490__00iz**2)
v0504__00iY = (v0504__00iY*_00iX_coeff).reshape((1, 1))

# op _00rn_power_combination_eval
# LANG: _00rm --> _00ro
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0767__00ro = (v0766__00rm**1)
v0767__00ro = (v0767__00ro*_00rn_coeff).reshape((1, 1, 3))

# op _00sa_linear_combination_eval
# LANG: _00s9 --> _00sb
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0788__00sb = _00sa_constant+1*v0787__00s9

# op _00sm_power_combination_eval
# LANG: _00sl --> _00sn
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0795__00sn = (v0792__00sl**0.5)
v0795__00sn = (v0795__00sn*_00sm_coeff).reshape((1, 1))

# op _00sq_power_combination_eval
# LANG: _00s2 --> _00sr
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0797__00sr = (v0783__00s2**2)
v0797__00sr = (v0797__00sr*_00sq_coeff).reshape((1, 1))

# op _00vF_power_combination_eval
# LANG: _00vC, _00vE --> _00vG
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0898__00vG = (v0897__00vC**1)*(v0899__00vE**-1)
v0898__00vG = (v0898__00vG*_00vF_coeff).reshape((1, 1))

# op _00vt_linear_combination_eval
# LANG: _00vs --> _00vu
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0886__00vu = _00vt_constant+1*v0879__00vs

# op _012G_linear_combination_eval
# LANG: _012F --> _012H
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01862__012H = _012G_constant+1*v01861__012F

# op _012S_linear_combination_eval
# LANG: _012R --> _012T
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01878__012T = _012S_constant+1*v01877__012R

# op _012_ expand_scalar_eval
# LANG: _012Z --> _0130
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01892__0130 = np.empty((1, 1))
v01892__0130.fill(v01891__012Z.item())

# op _012e_linear_combination_eval
# LANG: _012d --> _012f
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01856__012f = _012e_constant+1*v01855__012d

# op _012w_linear_combination_eval
# LANG: _012v --> _012x
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01872__012x = _012w_constant+1*v01871__012v

# op _013f_power_combination_eval
# LANG: _013e --> _013g
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01886__013g = (v01885__013e**0.5)
v01886__013g = (v01886__013g*_013f_coeff).reshape((1, 1))

# op _013x_linear_combination_eval
# LANG: _013w --> _013y
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01898__013y = _013x_constant+-1*v01897__013w

# op _00IX_power_combination_eval
# LANG: _ux, _00IW --> _00IY
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01230__00IY = (v01229__00IW**1)*(v01164__ux**1)
v01230__00IY = (v01230__00IY*_00IX_coeff).reshape((1, 40, 30))

# op _00NO_power_combination_eval
# LANG: _00NM --> _00NP
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01373__00NP = (v01372__00NM**4)
v01373__00NP = (v01373__00NP*_00NO_coeff).reshape((1, 1))

# op _00O7_power_combination_eval
# LANG: _00NV, _00O6 --> _00O8
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01378__00O8 = (v01377__00NV**1)*(v01384__00O6**1)
v01378__00O8 = (v01378__00O8*_00O7_coeff).reshape((1, 1))

# op _00Ob_linear_combination_eval
# LANG: _00Oa --> _00Oc
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01387__00Oc = _00Ob_constant+1*v01386__00Oa

# op _00YZ_exp_a_eval
# LANG: _00YY --> _00Y_
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01723__00Y_ = _00YZ_exp_a_eval_a**v01722__00YY

# op _00_3_power_combination_eval
# LANG: _00_1 --> _00_4
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01753__00_4 = (v01752__00_1**4)
v01753__00_4 = (v01753__00_4*_00_3_coeff).reshape((1, 1))

# op _00_n_power_combination_eval
# LANG: _00_a, _00_m --> _00_o
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01758__00_o = (v01757__00_a**1)*(v01764__00_m**1)
v01758__00_o = (v01758__00_o*_00_n_coeff).reshape((1, 1))

# op _00_r_linear_combination_eval
# LANG: _00_q --> _00_s
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01767__00_s = _00_r_constant+1*v01766__00_q

# op _00dD_power_combination_eval
# LANG: _ux, _00dC --> _00dE
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0346__00dE = (v0345__00dC**1)*(v0280__ux**1)
v0346__00dE = (v0346__00dE*_00dD_coeff).reshape((1, 40, 100))

# op _00iB_power_combination_eval
# LANG: _00iz --> _00iC
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0491__00iC = (v0490__00iz**4)
v0491__00iC = (v0491__00iC*_00iB_coeff).reshape((1, 1))

# op _00iV_power_combination_eval
# LANG: _00iI, _00iU --> _00iW
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0496__00iW = (v0495__00iI**1)*(v0502__00iU**1)
v0496__00iW = (v0496__00iW*_00iV_coeff).reshape((1, 1))

# op _00iZ_linear_combination_eval
# LANG: _00iY --> _00i_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0505__00i_ = _00iZ_constant+1*v0504__00iY

# op _00rp_exp_a_eval
# LANG: _00ro --> _00rq
# SHAPES: (1, 1, 3) --> (1, 1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0768__00rq = _00rp_exp_a_eval_a**v0767__00ro

# op _00s4_power_combination_eval
# LANG: _00s2 --> _00s5
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0784__00s5 = (v0783__00s2**4)
v0784__00s5 = (v0784__00s5*_00s4_coeff).reshape((1, 1))

# op _00so_power_combination_eval
# LANG: _00sb, _00sn --> _00sp
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0789__00sp = (v0788__00sb**1)*(v0795__00sn**1)
v0789__00sp = (v0789__00sp*_00so_coeff).reshape((1, 1))

# op _00ss_linear_combination_eval
# LANG: _00sr --> _00st
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0798__00st = _00ss_constant+1*v0797__00sr

# op _00vH_linear_combination_eval
# LANG: _00vG --> _00vI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0900__00vI = _00vH_constant+1*v0898__00vG

# op _00vv_log10_eval
# LANG: _00vu --> _00vw
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0887__00vw = np.log10(v0886__00vu)

# op _012I_power_combination_eval
# LANG: _012f, _012H --> _012J
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01857__012J = (v01856__012f**1)*(v01862__012H**1)
v01857__012J = (v01857__012J*_012I_coeff).reshape((1, 1))

# op _012U_power_combination_eval
# LANG: _012x, _012T --> _012V
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01873__012V = (v01872__012x**1)*(v01878__012T**1)
v01873__012V = (v01873__012V*_012U_coeff).reshape((1, 1))

# op _013h_sin_eval
# LANG: _013g --> _013i
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01887__013i = np.sin(v01886__013g)

# op _013n_power_combination_eval
# LANG: _0133, _0130 --> _013o
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01890__013o = (v01882__0133**1)*(v01892__0130**-1)
v01890__013o = (v01890__013o*_013n_coeff).reshape((1, 1))

# op _013z_power_combination_eval
# LANG: _013y --> _013A
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01899__013A = (v01898__013y**1)
v01899__013A = (v01899__013A*_013z_coeff).reshape((1, 1))

# op _00IZ_power_combination_eval
# LANG: _ut, _00IY --> _00I_
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01231__00I_ = (v01230__00IY**1)*(v01196__ut**1)
v01231__00I_ = (v01231__00I_*_00IZ_coeff).reshape((1, 40, 30))

# op _00Jy_power_combination_eval
# LANG: _ut --> _00Jz
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01299__00Jz = (v01196__ut**1)
v01299__00Jz = (v01299__00Jz*_00Jy_coeff).reshape((1, 40, 30))

# op _00NQ_power_combination_eval
# LANG: _00NP --> _00NR
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01374__00NR = (v01373__00NP**1)
v01374__00NR = (v01374__00NR*_00NQ_coeff).reshape((1, 1))

# op _00Od_power_combination_eval
# LANG: _00O8, _00Oc --> _00Oe
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01385__00Oe = (v01378__00O8**1)*(v01387__00Oc**1)
v01385__00Oe = (v01385__00Oe*_00Od_coeff).reshape((1, 1))

# op _00Z0_single_tensor_sum_with_axis_eval
# LANG: _00Y_ --> _00Z1
# SHAPES: (1, 1, 3) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01724__00Z1 = np.sum(v01723__00Y_, axis = (2,)).reshape((1, 1))

# op _00_5_power_combination_eval
# LANG: _00_4 --> _00_6
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01754__00_6 = (v01753__00_4**1)
v01754__00_6 = (v01754__00_6*_00_5_coeff).reshape((1, 1))

# op _00_t_power_combination_eval
# LANG: _00_o, _00_s --> _00_u
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01765__00_u = (v01758__00_o**1)*(v01767__00_s**1)
v01765__00_u = (v01765__00_u*_00_t_coeff).reshape((1, 1))

# op _00dF_power_combination_eval
# LANG: _ut, _00dE --> _00dG
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0347__00dG = (v0346__00dE**1)*(v0312__ut**1)
v0347__00dG = (v0347__00dG*_00dF_coeff).reshape((1, 40, 100))

# op _00ee_power_combination_eval
# LANG: _ut --> _00ef
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0415__00ef = (v0312__ut**1)
v0415__00ef = (v0415__00ef*_00ee_coeff).reshape((1, 40, 100))

# op _00iD_power_combination_eval
# LANG: _00iC --> _00iE
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0492__00iE = (v0491__00iC**1)
v0492__00iE = (v0492__00iE*_00iD_coeff).reshape((1, 1))

# op _00j0_power_combination_eval
# LANG: _00iW, _00i_ --> _00j1
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0503__00j1 = (v0496__00iW**1)*(v0505__00i_**1)
v0503__00j1 = (v0503__00j1*_00j0_coeff).reshape((1, 1))

# op _00rr_single_tensor_sum_with_axis_eval
# LANG: _00rq --> _00rs
# SHAPES: (1, 1, 3) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0769__00rs = np.sum(v0768__00rq, axis = (2,)).reshape((1, 1))

# op _00s6_power_combination_eval
# LANG: _00s5 --> _00s7
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0785__00s7 = (v0784__00s5**1)
v0785__00s7 = (v0785__00s7*_00s6_coeff).reshape((1, 1))

# op _00su_power_combination_eval
# LANG: _00sp, _00st --> _00sv
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0796__00sv = (v0789__00sp**1)*(v0798__00st**1)
v0796__00sv = (v0796__00sv*_00su_coeff).reshape((1, 1))

# op _00vJ_log10_eval
# LANG: _00vI --> _00vK
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0901__00vK = np.log10(v0900__00vI)

# op _00vx_power_combination_eval
# LANG: _00vw --> _00vy
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0888__00vy = (v0887__00vw**1)
v0888__00vy = (v0888__00vy*_00vx_coeff).reshape((1, 1))

# op _012W_linear_combination_eval
# LANG: _012J, _012V --> _012X
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01863__012X = _012W_constant+1*v01857__012J+1*v01873__012V

# op _013B_linear_combination_eval
# LANG: _013A --> _013C
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01900__013C = _013B_constant+1*v01899__013A

# op _013j_power_combination_eval
# LANG: _013i --> _013k
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01888__013k = (v01887__013i**0.031)
v01888__013k = (v01888__013k*_013j_coeff).reshape((1, 1))

# op _013p_log10_eval
# LANG: _013o --> _013q
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01893__013q = np.log10(v01890__013o)

# op _00J0_power_combination_eval
# LANG: _00I_, prandtl_loss_factor --> _00J1
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01232__00J1 = (v01231__00I_**1)*(v01149_prandtl_loss_factor**1)
v01232__00J1 = (v01232__00J1*_00J0_coeff).reshape((1, 40, 30))

# op _00JA_linear_combination_eval
# LANG: _00Jz, _tangential_inflow_velocity --> _00JB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01298__00JB = _00JA_constant+1*v01116__tangential_inflow_velocity+-1*v01299__00Jz

# op _00Jc_power_combination_eval
# LANG: _ut --> _00Jd
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01252__00Jd = (v01196__ut**1)
v01252__00Jd = (v01252__00Jd*_00Jc_coeff).reshape((1, 40, 30))

# op _00Jq_power_combination_eval
# LANG: _00H9 --> _00Jr
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01292__00Jr = (v01174__00H9**1)
v01292__00Jr = (v01292__00Jr*_00Jq_coeff).reshape((1, 40, 30))

# op _00Of_power_combination_eval
# LANG: _00NR, _00Oe --> _00Og
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01375__00Og = (v01374__00NR**1)*(v01385__00Oe**-1)
v01375__00Og = (v01375__00Og*_00Of_coeff).reshape((1, 1))

# op _00Z2_log10_eval
# LANG: _00Z1 --> _00Z3
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01725__00Z3 = np.log10(v01724__00Z1)

# op _00_v_power_combination_eval
# LANG: _00_6, _00_u --> _00_w
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01755__00_w = (v01754__00_6**1)*(v01765__00_u**-1)
v01755__00_w = (v01755__00_w*_00_v_coeff).reshape((1, 1))

# op _00dH_power_combination_eval
# LANG: _00dG, prandtl_loss_factor --> _00dI
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0348__00dI = (v0347__00dG**1)*(v0265_prandtl_loss_factor**1)
v0348__00dI = (v0348__00dI*_00dH_coeff).reshape((1, 40, 100))

# op _00dT_power_combination_eval
# LANG: _ut --> _00dU
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0368__00dU = (v0312__ut**1)
v0368__00dU = (v0368__00dU*_00dT_coeff).reshape((1, 40, 100))

# op _00e6_power_combination_eval
# LANG: _00bQ --> _00e7
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0408__00e7 = (v0290__00bQ**1)
v0408__00e7 = (v0408__00e7*_00e6_coeff).reshape((1, 40, 100))

# op _00eg_linear_combination_eval
# LANG: _00ef, _tangential_inflow_velocity --> _00eh
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0414__00eh = _00eg_constant+1*v0232__tangential_inflow_velocity+-1*v0415__00ef

# op _00j2_power_combination_eval
# LANG: _00iE, _00j1 --> _00j3
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0493__00j3 = (v0492__00iE**1)*(v0503__00j1**-1)
v0493__00j3 = (v0493__00j3*_00j2_coeff).reshape((1, 1))

# op _00rt_log10_eval
# LANG: _00rs --> _00ru
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0770__00ru = np.log10(v0769__00rs)

# op _00sw_power_combination_eval
# LANG: _00s7, _00sv --> _00sx
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0786__00sx = (v0785__00s7**1)*(v0796__00sv**-1)
v0786__00sx = (v0786__00sx*_00sw_coeff).reshape((1, 1))

# op _00vL_power_combination_eval
# LANG: _00vK --> _00vM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0902__00vM = (v0901__00vK**1)
v0902__00vM = (v0902__00vM*_00vL_coeff).reshape((1, 1))

# op _00vz_linear_combination_eval
# LANG: _00vy --> _00vA
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0889__00vA = _00vz_constant+1*v0888__00vy

# op _00wG_power_combination_eval
# LANG: hover_altitude --> _00wH
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0964__00wH = (v0930_hover_altitude**5)
v0964__00wH = (v0964__00wH*_00wG_coeff).reshape((1,))

# op _00wS_power_combination_eval
# LANG: hover_altitude --> _00wT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0966__00wT = (v0930_hover_altitude**4)
v0966__00wT = (v0966__00wT*_00wS_coeff).reshape((1,))

# op _00wt_power_combination_eval
# LANG: hover_altitude --> _00wu
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0961__00wu = (v0930_hover_altitude**6)
v0961__00wu = (v0961__00wu*_00wt_coeff).reshape((1,))

# op _00x3_power_combination_eval
# LANG: hover_altitude --> _00x4
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0968__00x4 = (v0930_hover_altitude**3)
v0968__00x4 = (v0968__00x4*_00x3_coeff).reshape((1,))

# op _00xD_power_combination_eval
# LANG: hover_altitude --> _00xE
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0974__00xE = (v0930_hover_altitude**0)
v0974__00xE = (v0974__00xE*_00xD_coeff).reshape((1,))

# op _00xf_power_combination_eval
# LANG: hover_altitude --> _00xg
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0970__00xg = (v0930_hover_altitude**2)
v0970__00xg = (v0970__00xg*_00xf_coeff).reshape((1,))

# op _00xr_power_combination_eval
# LANG: hover_altitude --> _00xs
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0972__00xs = (v0930_hover_altitude**1)
v0972__00xs = (v0972__00xs*_00xr_coeff).reshape((1,))

# op _013D_power_combination_eval
# LANG: _013q, _013C --> _013E
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01894__013E = (v01893__013q**1)*(v01900__013C**1)
v01894__013E = (v01894__013E*_013D_coeff).reshape((1, 1))

# op _013l_power_combination_eval
# LANG: _012X, _013k --> _013m
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01879__013m = (v01863__012X**1)*(v01888__013k**1)
v01879__013m = (v01879__013m*_013l_coeff).reshape((1, 1))

# op _00Ha_cos_eval
# LANG: phi_distribution --> _00Hb
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01213__00Hb = np.cos(v01136_phi_distribution)

# op _00He_sin_eval
# LANG: phi_distribution --> _00Hf
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01280__00Hf = np.sin(v01136_phi_distribution)

# op _00J2_power_combination_eval
# LANG: _00J1, _dr --> _local_torque
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01233__local_torque = (v01232__00J1**1)*(v01087__dr**1)
v01233__local_torque = (v01233__local_torque*_00J2_coeff).reshape((1, 40, 30))

# op _00J4_power_combination_eval
# LANG: _00G_ --> _00J5
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01245__00J5 = (v01181__00G_**1)
v01245__00J5 = (v01245__00J5*_00J4_coeff).reshape((1, 40, 30))

# op _00JC_power_combination_eval
# LANG: _00JB --> _00JD
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01300__00JD = (v01298__00JB**2)
v01300__00JD = (v01300__00JD*_00JC_coeff).reshape((1, 40, 30))

# op _00Je_linear_combination_eval
# LANG: _00Jd, _tangential_inflow_velocity --> _00Jf
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01251__00Jf = _00Je_constant+1*v01116__tangential_inflow_velocity+-1*v01252__00Jd

# op _00Js_power_combination_eval
# LANG: _00Jr --> _00Jt
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01293__00Jt = (v01292__00Jr**1)
v01293__00Jt = (v01293__00Jt*_00Js_coeff).reshape((1, 40, 30))

# op _00Jw_power_combination_eval
# LANG: _ux_2 --> _00Jx
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01296__00Jx = (v01177__ux_2**2)
v01296__00Jx = (v01296__00Jx*_00Jw_coeff).reshape((1, 40, 30))

# op _00L8_power_combination_eval
# LANG: _ut --> _00L9
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01272__00L9 = (v01196__ut**1)
v01272__00L9 = (v01272__00L9*_00L8_coeff).reshape((1, 40, 30))

# op _00LE_power_combination_eval
# LANG: _axial_inflow_velocity --> _00LF
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01316__00LF = (v01106__axial_inflow_velocity**2)
v01316__00LF = (v01316__00LF*_00LE_coeff).reshape((1, 40, 30))

# op _00Ls_power_combination_eval
# LANG: _ux, _tangential_inflow_velocity --> _00Lt
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01309__00Lt = (v01116__tangential_inflow_velocity**1)*(v01164__ux**1)
v01309__00Lt = (v01309__00Lt*_00Ls_coeff).reshape((1, 40, 30))

# op _00Lw_power_combination_eval
# LANG: _axial_inflow_velocity --> _00Lx
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01312__00Lx = (v01106__axial_inflow_velocity**1)
v01312__00Lx = (v01312__00Lx*_00Lw_coeff).reshape((1, 40, 30))

# op _00Ly_power_combination_eval
# LANG: _ux --> _00Lz
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01314__00Lz = (v01164__ux**2)
v01314__00Lz = (v01314__00Lz*_00Ly_coeff).reshape((1, 40, 30))

# op _00Ml_single_tensor_sum_with_axis_eval
# LANG: _00GE --> _00Mm
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01338__00Mm = np.sum(v01325__00GE, axis = (1, 2)).reshape((1,))

# op _00Mv_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00Mw
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01343__00Mw = np.sum(v01086__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00Oh_log10_eval
# LANG: _00Og --> _00Oi
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01388__00Oi = np.log10(v01375__00Og)

# op _00Ol_log10_eval
# LANG: RA_1000 --> _00Om
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01392__00Om = np.log10(v01391_RA_1000)

# op _00Z4_power_combination_eval
# LANG: _00Z3 --> rotor_disk_tonal_spl
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01726_rotor_disk_tonal_spl = (v01725__00Z3**1)
v01726_rotor_disk_tonal_spl = (v01726_rotor_disk_tonal_spl*_00Z4_coeff).reshape((1, 1))

# op _00_B_log10_eval
# LANG: RA_1000 --> _00_C
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01772__00_C = np.log10(v01771_RA_1000)

# op _00_x_log10_eval
# LANG: _00_w --> _00_y
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01768__00_y = np.log10(v01755__00_w)

# op _00bR_cos_eval
# LANG: phi_distribution --> _00bS
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0329__00bS = np.cos(v0252_phi_distribution)

# op _00bV_sin_eval
# LANG: phi_distribution --> _00bW
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0396__00bW = np.sin(v0252_phi_distribution)

# op _00dJ_power_combination_eval
# LANG: _00dI, _dr --> _local_torque
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0349__local_torque = (v0348__00dI**1)*(v0203__dr**1)
v0349__local_torque = (v0349__local_torque*_00dJ_coeff).reshape((1, 40, 100))

# op _00dL_power_combination_eval
# LANG: _00bG --> _00dM
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0361__00dM = (v0297__00bG**1)
v0361__00dM = (v0361__00dM*_00dL_coeff).reshape((1, 40, 100))

# op _00dV_linear_combination_eval
# LANG: _00dU, _tangential_inflow_velocity --> _00dW
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0367__00dW = _00dV_constant+1*v0232__tangential_inflow_velocity+-1*v0368__00dU

# op _00e8_power_combination_eval
# LANG: _00e7 --> _00e9
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0409__00e9 = (v0408__00e7**1)
v0409__00e9 = (v0409__00e9*_00e8_coeff).reshape((1, 40, 100))

# op _00ec_power_combination_eval
# LANG: _ux_2 --> _00ed
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0412__00ed = (v0293__ux_2**2)
v0412__00ed = (v0412__00ed*_00ec_coeff).reshape((1, 40, 100))

# op _00ei_power_combination_eval
# LANG: _00eh --> _00ej
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0416__00ej = (v0414__00eh**2)
v0416__00ej = (v0416__00ej*_00ei_coeff).reshape((1, 40, 100))

# op _00fP_power_combination_eval
# LANG: _ut --> _00fQ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0388__00fQ = (v0312__ut**1)
v0388__00fQ = (v0388__00fQ*_00fP_coeff).reshape((1, 40, 100))

# op _00g8_power_combination_eval
# LANG: _ux, _tangential_inflow_velocity --> _00g9
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0425__00g9 = (v0232__tangential_inflow_velocity**1)*(v0280__ux**1)
v0425__00g9 = (v0425__00g9*_00g8_coeff).reshape((1, 40, 100))

# op _00gc_power_combination_eval
# LANG: _axial_inflow_velocity --> _00gd
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0428__00gd = (v0222__axial_inflow_velocity**1)
v0428__00gd = (v0428__00gd*_00gc_coeff).reshape((1, 40, 100))

# op _00ge_power_combination_eval
# LANG: _ux --> _00gf
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0430__00gf = (v0280__ux**2)
v0430__00gf = (v0430__00gf*_00ge_coeff).reshape((1, 40, 100))

# op _00gk_power_combination_eval
# LANG: _axial_inflow_velocity --> _00gl
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0432__00gl = (v0222__axial_inflow_velocity**2)
v0432__00gl = (v0432__00gl*_00gk_coeff).reshape((1, 40, 100))

# op _00h1_single_tensor_sum_with_axis_eval
# LANG: _00bk --> _00h2
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0454__00h2 = np.sum(v0441__00bk, axis = (1, 2)).reshape((1,))

# op _00hb_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00hc
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0459__00hc = np.sum(v0202__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00j4_log10_eval
# LANG: _00j3 --> _00j5
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0506__00j5 = np.log10(v0493__00j3)

# op _00j8_log10_eval
# LANG: RA_1000 --> _00j9
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0510__00j9 = np.log10(v0509_RA_1000)

# op _00rv_power_combination_eval
# LANG: _00ru --> rotor_disk_tonal_spl
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0771_rotor_disk_tonal_spl = (v0770__00ru**1)
v0771_rotor_disk_tonal_spl = (v0771_rotor_disk_tonal_spl*_00rv_coeff).reshape((1, 1))

# op _00sC_log10_eval
# LANG: RA_1000 --> _00sD
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0803__00sD = np.log10(v0802_RA_1000)

# op _00sy_log10_eval
# LANG: _00sx --> _00sz
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0799__00sz = np.log10(v0786__00sx)

# op _00vN_linear_combination_eval
# LANG: _00vA, _00vM --> rotor_disk_broadband_spl
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0890_rotor_disk_broadband_spl = _00vN_constant+1*v0889__00vA+1*v0902__00vM

# op _00wI_power_combination_eval
# LANG: _00wH --> _00wJ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0965__00wJ = (v0964__00wH**1)
v0965__00wJ = (v0965__00wJ*_00wI_coeff).reshape((1,))

# op _00wU_power_combination_eval
# LANG: _00wT --> _00wV
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0967__00wV = (v0966__00wT**1)
v0967__00wV = (v0967__00wV*_00wU_coeff).reshape((1,))

# op _00wv_power_combination_eval
# LANG: _00wu --> _00ww
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0962__00ww = (v0961__00wu**1)
v0962__00ww = (v0962__00ww*_00wv_coeff).reshape((1,))

# op _00x5_power_combination_eval
# LANG: _00x4 --> _00x6
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0969__00x6 = (v0968__00x4**1)
v0969__00x6 = (v0969__00x6*_00x5_coeff).reshape((1,))

# op _00xF_power_combination_eval
# LANG: _00xE --> _00xG
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0975__00xG = (v0974__00xE**1)
v0975__00xG = (v0975__00xG*_00xF_coeff).reshape((1,))

# op _00xh_power_combination_eval
# LANG: _00xg --> _00xi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0971__00xi = (v0970__00xg**1)
v0971__00xi = (v0971__00xi*_00xh_coeff).reshape((1,))

# op _00xt_power_combination_eval
# LANG: _00xs --> _00xu
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0973__00xu = (v0972__00xs**1)
v0973__00xu = (v0973__00xu*_00xt_coeff).reshape((1,))

# op _013F_linear_combination_eval
# LANG: _013m, _013E --> rotor_disk_broadband_spl
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01889_rotor_disk_broadband_spl = _013F_constant+1*v01879__013m+-1*v01894__013E

# op _00Hc_power_combination_eval
# LANG: _00Hb, Cl --> _00Hd
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01212__00Hd = (v01138_Cl**1)*(v01213__00Hb**1)
v01212__00Hd = (v01212__00Hd*_00Hc_coeff).reshape((1, 40, 30))

# op _00Hg_power_combination_eval
# LANG: _00Hf, Cl --> _00Hh
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01279__00Hh = (v01138_Cl**1)*(v01280__00Hf**1)
v01279__00Hh = (v01279__00Hh*_00Hg_coeff).reshape((1, 40, 30))

# op _00J6_power_combination_eval
# LANG: _00J5 --> _00J7
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01246__00J7 = (v01245__00J5**1)
v01246__00J7 = (v01246__00J7*_00J6_coeff).reshape((1, 40, 30))

# op _00JE_linear_combination_eval
# LANG: _00Jx, _00JD --> _00JF
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01297__00JF = _00JE_constant+1*v01296__00Jx+1*v01300__00JD

# op _00Ja_power_combination_eval
# LANG: _ux_2 --> _00Jb
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01249__00Jb = (v01177__ux_2**2)
v01249__00Jb = (v01249__00Jb*_00Ja_coeff).reshape((1, 40, 30))

# op _00Jg_power_combination_eval
# LANG: _00Jf --> _00Jh
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01253__00Jh = (v01251__00Jf**2)
v01253__00Jh = (v01253__00Jh*_00Jg_coeff).reshape((1, 40, 30))

# op _00Ju_power_combination_eval
# LANG: _00GM, _00Jt --> _00Jv
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01294__00Jv = (v01293__00Jt**1)*(v01205__00GM**1)
v01294__00Jv = (v01294__00Jv*_00Ju_coeff).reshape((1, 40, 30))

# op _00KD_power_combination_eval
# LANG: _ut --> _00KE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01288__00KE = (v01196__ut**1)
v01288__00KE = (v01288__00KE*_00KD_coeff).reshape((1, 40, 30))

# op _00Kh_power_combination_eval
# LANG: _ut --> _00Ki
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01221__00Ki = (v01196__ut**1)
v01221__00Ki = (v01221__00Ki*_00Kh_coeff).reshape((1, 40, 30))

# op _00L2_single_tensor_sum_with_axis_eval
# LANG: _local_torque --> _00L3
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01234__00L3 = np.sum(v01233__local_torque, axis = (1, 2)).reshape((1,))

# op _00L6_power_combination_eval
# LANG: _00GM --> _00L7
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01269__00L7 = (v01205__00GM**1)
v01269__00L7 = (v01269__00L7*_00L6_coeff).reshape((1, 40, 30))

# op _00LA_power_combination_eval
# LANG: _00Lx, _00Lz --> _00LB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01313__00LB = (v01312__00Lx**1)*(v01314__00Lz**1)
v01313__00LB = (v01313__00LB*_00LA_coeff).reshape((1, 40, 30))

# op _00LG_power_combination_eval
# LANG: _00LF --> _00LH
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01317__00LH = (v01316__00LF**1)
v01317__00LH = (v01317__00LH*_00LG_coeff).reshape((1, 40, 30))

# op _00La_linear_combination_eval
# LANG: _00L9, _tangential_inflow_velocity --> _00Lb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01271__00Lb = _00La_constant+1*v01116__tangential_inflow_velocity+-1*v01272__00L9

# op _00Lu_power_combination_eval
# LANG: _ut, _00Lt --> _00Lv
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01310__00Lv = (v01309__00Lt**1)*(v01196__ut**1)
v01310__00Lv = (v01310__00Lv*_00Lu_coeff).reshape((1, 40, 30))

# op _00MJ_power_combination_eval
# LANG: _00GE, _axial_inflow_velocity --> _00MK
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01350__00MK = (v01106__axial_inflow_velocity**1)*(v01325__00GE**-1)
v01350__00MK = (v01350__00MK*_00MJ_coeff).reshape((1, 40, 30))

# op _00ML_power_combination_eval
# LANG: _rotor_radius --> _00MM
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01352__00MM = (v01086__rotor_radius**1)
v01352__00MM = (v01352__00MM*_00ML_coeff).reshape((1, 40, 30))

# op _00Mn_power_combination_eval
# LANG: _00Mm --> _00Mo
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01339__00Mo = (v01338__00Mm**1)
v01339__00Mo = (v01339__00Mo*_00Mn_coeff).reshape((1,))

# op _00Mx_power_combination_eval
# LANG: _00Mw --> _00My
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01344__00My = (v01343__00Mw**1)
v01344__00My = (v01344__00My*_00Mx_coeff).reshape((1,))

# op _00Oj_power_combination_eval
# LANG: _00Oi --> _00Ok
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01389__00Ok = (v01388__00Oi**1)
v01389__00Ok = (v01389__00Ok*_00Oj_coeff).reshape((1, 1))

# op _00On_power_combination_eval
# LANG: _00Om --> _00Oo
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01393__00Oo = (v01392__00Om**1)
v01393__00Oo = (v01393__00Oo*_00On_coeff).reshape((1, 1))

# op _00_D_power_combination_eval
# LANG: _00_C --> _00_E
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01773__00_E = (v01772__00_C**1)
v01773__00_E = (v01773__00_E*_00_D_coeff).reshape((1, 1))

# op _00_z_power_combination_eval
# LANG: _00_y --> _00_A
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01769__00_A = (v01768__00_y**1)
v01769__00_A = (v01769__00_A*_00_z_coeff).reshape((1, 1))

# op _00bT_power_combination_eval
# LANG: _00bS, Cl --> _00bU
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0328__00bU = (v0254_Cl**1)*(v0329__00bS**1)
v0328__00bU = (v0328__00bU*_00bT_coeff).reshape((1, 40, 100))

# op _00bX_power_combination_eval
# LANG: _00bW, Cl --> _00bY
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0395__00bY = (v0254_Cl**1)*(v0396__00bW**1)
v0395__00bY = (v0395__00bY*_00bX_coeff).reshape((1, 40, 100))

# op _00dN_power_combination_eval
# LANG: _00dM --> _00dO
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0362__00dO = (v0361__00dM**1)
v0362__00dO = (v0362__00dO*_00dN_coeff).reshape((1, 40, 100))

# op _00dR_power_combination_eval
# LANG: _ux_2 --> _00dS
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0365__00dS = (v0293__ux_2**2)
v0365__00dS = (v0365__00dS*_00dR_coeff).reshape((1, 40, 100))

# op _00dX_power_combination_eval
# LANG: _00dW --> _00dY
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0369__00dY = (v0367__00dW**2)
v0369__00dY = (v0369__00dY*_00dX_coeff).reshape((1, 40, 100))

# op _00eY_power_combination_eval
# LANG: _ut --> _00eZ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0337__00eZ = (v0312__ut**1)
v0337__00eZ = (v0337__00eZ*_00eY_coeff).reshape((1, 40, 100))

# op _00ea_power_combination_eval
# LANG: _00bs, _00e9 --> _00eb
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0410__00eb = (v0409__00e9**1)*(v0321__00bs**1)
v0410__00eb = (v0410__00eb*_00ea_coeff).reshape((1, 40, 100))

# op _00ek_linear_combination_eval
# LANG: _00ed, _00ej --> _00el
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0413__00el = _00ek_constant+1*v0412__00ed+1*v0416__00ej

# op _00fJ_single_tensor_sum_with_axis_eval
# LANG: _local_torque --> _00fK
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0350__00fK = np.sum(v0349__local_torque, axis = (1, 2)).reshape((1,))

# op _00fN_power_combination_eval
# LANG: _00bs --> _00fO
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0385__00fO = (v0321__00bs**1)
v0385__00fO = (v0385__00fO*_00fN_coeff).reshape((1, 40, 100))

# op _00fR_linear_combination_eval
# LANG: _00fQ, _tangential_inflow_velocity --> _00fS
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0387__00fS = _00fR_constant+1*v0232__tangential_inflow_velocity+-1*v0388__00fQ

# op _00fj_power_combination_eval
# LANG: _ut --> _00fk
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0404__00fk = (v0312__ut**1)
v0404__00fk = (v0404__00fk*_00fj_coeff).reshape((1, 40, 100))

# op _00ga_power_combination_eval
# LANG: _ut, _00g9 --> _00gb
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0426__00gb = (v0425__00g9**1)*(v0312__ut**1)
v0426__00gb = (v0426__00gb*_00ga_coeff).reshape((1, 40, 100))

# op _00gg_power_combination_eval
# LANG: _00gd, _00gf --> _00gh
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0429__00gh = (v0428__00gd**1)*(v0430__00gf**1)
v0429__00gh = (v0429__00gh*_00gg_coeff).reshape((1, 40, 100))

# op _00gm_power_combination_eval
# LANG: _00gl --> _00gn
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0433__00gn = (v0432__00gl**1)
v0433__00gn = (v0433__00gn*_00gm_coeff).reshape((1, 40, 100))

# op _00h3_power_combination_eval
# LANG: _00h2 --> _00h4
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0455__00h4 = (v0454__00h2**1)
v0455__00h4 = (v0455__00h4*_00h3_coeff).reshape((1,))

# op _00hd_power_combination_eval
# LANG: _00hc --> _00he
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0460__00he = (v0459__00hc**1)
v0460__00he = (v0460__00he*_00hd_coeff).reshape((1,))

# op _00hp_power_combination_eval
# LANG: _00bk, _axial_inflow_velocity --> _00hq
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0466__00hq = (v0222__axial_inflow_velocity**1)*(v0441__00bk**-1)
v0466__00hq = (v0466__00hq*_00hp_coeff).reshape((1, 40, 100))

# op _00hr_power_combination_eval
# LANG: _rotor_radius --> _00hs
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0468__00hs = (v0202__rotor_radius**1)
v0468__00hs = (v0468__00hs*_00hr_coeff).reshape((1, 40, 100))

# op _00j6_power_combination_eval
# LANG: _00j5 --> _00j7
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0507__00j7 = (v0506__00j5**1)
v0507__00j7 = (v0507__00j7*_00j6_coeff).reshape((1, 1))

# op _00ja_power_combination_eval
# LANG: _00j9 --> _00jb
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0511__00jb = (v0510__00j9**1)
v0511__00jb = (v0511__00jb*_00ja_coeff).reshape((1, 1))

# op _00sA_power_combination_eval
# LANG: _00sz --> _00sB
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0800__00sB = (v0799__00sz**1)
v0800__00sB = (v0800__00sB*_00sA_coeff).reshape((1, 1))

# op _00sE_power_combination_eval
# LANG: _00sD --> _00sF
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0804__00sF = (v0803__00sD**1)
v0804__00sF = (v0804__00sF*_00sE_coeff).reshape((1, 1))

# op _00vS expand_array_eval
# LANG: rotor_disk_tonal_spl --> _00vT
# SHAPES: (1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0903__00vT = np.einsum('bc,a->abc', v0771_rotor_disk_tonal_spl.reshape((1, 1)) ,np.ones((1,))).reshape((1, 1, 1))

# op _00vW expand_array_eval
# LANG: rotor_disk_broadband_spl --> _00vX
# SHAPES: (1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0905__00vX = np.einsum('bc,a->abc', v0890_rotor_disk_broadband_spl.reshape((1, 1)) ,np.ones((1,))).reshape((1, 1, 1))

# op _00wx_indexed_passthrough_eval
# LANG: _00ww, _00wJ, _00wV, _00x6, _00xi, _00xu, _00xG --> temp_temperature
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0963_temp_temperature__temp[i_v0962__00ww__00wx_indexed_passthrough_eval] = v0962__00ww.flatten()
v0963_temp_temperature = v0963_temp_temperature__temp.copy()
v0963_temp_temperature__temp[i_v0965__00wJ__00wx_indexed_passthrough_eval] = v0965__00wJ.flatten()
v0963_temp_temperature = v0963_temp_temperature__temp.copy()
v0963_temp_temperature__temp[i_v0967__00wV__00wx_indexed_passthrough_eval] = v0967__00wV.flatten()
v0963_temp_temperature = v0963_temp_temperature__temp.copy()
v0963_temp_temperature__temp[i_v0969__00x6__00wx_indexed_passthrough_eval] = v0969__00x6.flatten()
v0963_temp_temperature = v0963_temp_temperature__temp.copy()
v0963_temp_temperature__temp[i_v0971__00xi__00wx_indexed_passthrough_eval] = v0971__00xi.flatten()
v0963_temp_temperature = v0963_temp_temperature__temp.copy()
v0963_temp_temperature__temp[i_v0973__00xu__00wx_indexed_passthrough_eval] = v0973__00xu.flatten()
v0963_temp_temperature = v0963_temp_temperature__temp.copy()
v0963_temp_temperature__temp[i_v0975__00xG__00wx_indexed_passthrough_eval] = v0975__00xG.flatten()
v0963_temp_temperature = v0963_temp_temperature__temp.copy()

# op _013K expand_array_eval
# LANG: rotor_disk_tonal_spl --> _013L
# SHAPES: (1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01901__013L = np.einsum('bc,a->abc', v01726_rotor_disk_tonal_spl.reshape((1, 1)) ,np.ones((1,))).reshape((1, 1, 1))

# op _013O expand_array_eval
# LANG: rotor_disk_broadband_spl --> _013P
# SHAPES: (1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01903__013P = np.einsum('bc,a->abc', v01889_rotor_disk_broadband_spl.reshape((1, 1)) ,np.ones((1,))).reshape((1, 1, 1))

# op _0057_decompose_eval
# LANG: T --> _0058
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0147__0058 = ((v0342_T.flatten())[src_indices__0058__0057]).reshape((1,))

# op _00Ar_decompose_eval
# LANG: T --> _00As
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01031__00As = ((v01226_T.flatten())[src_indices__00As__00Ar]).reshape((1,))

# op _00J8_power_combination_eval
# LANG: _00GM, _00J7 --> _00J9
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01247__00J9 = (v01246__00J7**1)*(v01205__00GM**1)
v01247__00J9 = (v01247__00J9*_00J8_coeff).reshape((1, 40, 30))

# op _00JG_power_combination_eval
# LANG: _00Jv, _00JF --> _00JH
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01295__00JH = (v01294__00Jv**1)*(v01297__00JF**1)
v01295__00JH = (v01295__00JH*_00JG_coeff).reshape((1, 40, 30))

# op _00Ji_linear_combination_eval
# LANG: _00Jb, _00Jh --> _00Jj
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01250__00Jj = _00Ji_constant+1*v01249__00Jb+1*v01253__00Jh

# op _00K9_power_combination_eval
# LANG: _00Hd --> _00Ka
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01214__00Ka = (v01212__00Hd**1)
v01214__00Ka = (v01214__00Ka*_00K9_coeff).reshape((1, 40, 30))

# op _00KF_linear_combination_eval
# LANG: _00KE, _tangential_inflow_velocity --> _00KG
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01287__00KG = _00KF_constant+1*v01116__tangential_inflow_velocity+-1*v01288__00KE

# op _00Kj_linear_combination_eval
# LANG: _00Ki, _tangential_inflow_velocity --> _00Kk
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01220__00Kk = _00Kj_constant+1*v01116__tangential_inflow_velocity+-1*v01221__00Ki

# op _00Kv_power_combination_eval
# LANG: _00Hh --> _00Kw
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01281__00Kw = (v01279__00Hh**1)
v01281__00Kw = (v01281__00Kw*_00Kv_coeff).reshape((1, 40, 30))

# op _00L4_power_combination_eval
# LANG: _00L3 --> total_torque
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01235_total_torque = (v01234__00L3**1)
v01235_total_torque = (v01235_total_torque*_00L4_coeff).reshape((1,))

# op _00LC_linear_combination_eval
# LANG: _00Lv, _00LB --> _00LD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01311__00LD = _00LC_constant+1*v01310__00Lv+-1*v01313__00LB

# op _00LI_power_combination_eval
# LANG: _ux, _00LH --> _00LJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01318__00LJ = (v01317__00LH**1)*(v01164__ux**1)
v01318__00LJ = (v01318__00LJ*_00LI_coeff).reshape((1, 40, 30))

# op _00Lc_power_combination_eval
# LANG: _00L7, _00Lb --> _00Ld
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01270__00Ld = (v01269__00L7**1)*(v01271__00Lb**1)
v01270__00Ld = (v01270__00Ld*_00Lc_coeff).reshape((1, 40, 30))

# op _00Lo_power_combination_eval
# LANG: _radius --> _00Lp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01306__00Lp = (v01099__radius**1)
v01306__00Lp = (v01306__00Lp*_00Lo_coeff).reshape((1, 40, 30))

# op _00MN_power_combination_eval
# LANG: _00MK, _00MM --> _00MO
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01351__00MO = (v01350__00MK**1)*(v01352__00MM**-1)
v01351__00MO = (v01351__00MO*_00MN_coeff).reshape((1, 40, 30))

# op _00Mp_power_combination_eval
# LANG: _00Mo --> _00Mq
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01340__00Mq = (v01339__00Mo**1)
v01340__00Mq = (v01340__00Mq*_00Mp_coeff).reshape((1,))

# op _00Mz_power_combination_eval
# LANG: _00My --> _00MA
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01345__00MA = (v01344__00My**1)
v01345__00MA = (v01345__00MA*_00Mz_coeff).reshape((1,))

# op _00Op_linear_combination_eval
# LANG: _00Ok, _00Oo --> _00Oq
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01390__00Oq = _00Op_constant+1*v01389__00Ok+-1*v01393__00Oo

# op _00_F_linear_combination_eval
# LANG: _00_A, _00_E --> _00_G
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01770__00_G = _00_F_constant+1*v01769__00_A+-1*v01773__00_E

# op _00dP_power_combination_eval
# LANG: _00bs, _00dO --> _00dQ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0363__00dQ = (v0362__00dO**1)*(v0321__00bs**1)
v0363__00dQ = (v0363__00dQ*_00dP_coeff).reshape((1, 40, 100))

# op _00dZ_linear_combination_eval
# LANG: _00dS, _00dY --> _00d_
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0366__00d_ = _00dZ_constant+1*v0365__00dS+1*v0369__00dY

# op _00eQ_power_combination_eval
# LANG: _00bU --> _00eR
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0330__00eR = (v0328__00bU**1)
v0330__00eR = (v0330__00eR*_00eQ_coeff).reshape((1, 40, 100))

# op _00e__linear_combination_eval
# LANG: _00eZ, _tangential_inflow_velocity --> _00f0
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0336__00f0 = _00e__constant+1*v0232__tangential_inflow_velocity+-1*v0337__00eZ

# op _00em_power_combination_eval
# LANG: _00eb, _00el --> _00en
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0411__00en = (v0410__00eb**1)*(v0413__00el**1)
v0411__00en = (v0411__00en*_00em_coeff).reshape((1, 40, 100))

# op _00fL_power_combination_eval
# LANG: _00fK --> total_torque
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0351_total_torque = (v0350__00fK**1)
v0351_total_torque = (v0351_total_torque*_00fL_coeff).reshape((1,))

# op _00fT_power_combination_eval
# LANG: _00fO, _00fS --> _00fU
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0386__00fU = (v0385__00fO**1)*(v0387__00fS**1)
v0386__00fU = (v0386__00fU*_00fT_coeff).reshape((1, 40, 100))

# op _00fb_power_combination_eval
# LANG: _00bY --> _00fc
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0397__00fc = (v0395__00bY**1)
v0397__00fc = (v0397__00fc*_00fb_coeff).reshape((1, 40, 100))

# op _00fl_linear_combination_eval
# LANG: _00fk, _tangential_inflow_velocity --> _00fm
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0403__00fm = _00fl_constant+1*v0232__tangential_inflow_velocity+-1*v0404__00fk

# op _00g4_power_combination_eval
# LANG: _radius --> _00g5
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0422__00g5 = (v0215__radius**1)
v0422__00g5 = (v0422__00g5*_00g4_coeff).reshape((1, 40, 100))

# op _00gi_linear_combination_eval
# LANG: _00gb, _00gh --> _00gj
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0427__00gj = _00gi_constant+1*v0426__00gb+-1*v0429__00gh

# op _00go_power_combination_eval
# LANG: _ux, _00gn --> _00gp
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0434__00gp = (v0433__00gn**1)*(v0280__ux**1)
v0434__00gp = (v0434__00gp*_00go_coeff).reshape((1, 40, 100))

# op _00h5_power_combination_eval
# LANG: _00h4 --> _00h6
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0456__00h6 = (v0455__00h4**1)
v0456__00h6 = (v0456__00h6*_00h5_coeff).reshape((1,))

# op _00hf_power_combination_eval
# LANG: _00he --> _00hg
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0461__00hg = (v0460__00he**1)
v0461__00hg = (v0461__00hg*_00hf_coeff).reshape((1,))

# op _00ht_power_combination_eval
# LANG: _00hq, _00hs --> _00hu
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0467__00hu = (v0466__00hq**1)*(v0468__00hs**-1)
v0467__00hu = (v0467__00hu*_00ht_coeff).reshape((1, 40, 100))

# op _00jc_linear_combination_eval
# LANG: _00j7, _00jb --> _00jd
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0508__00jd = _00jc_constant+1*v0507__00j7+-1*v0511__00jb

# op _00sG_linear_combination_eval
# LANG: _00sB, _00sF --> _00sH
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0801__00sH = _00sG_constant+1*v0800__00sB+-1*v0804__00sF

# op _00vU_indexed_passthrough_eval
# LANG: _00vT, _00vX --> noise_components
# SHAPES: (1, 1, 1), (1, 1, 1) --> (2, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0904_noise_components__temp[i_v0903__00vT__00vU_indexed_passthrough_eval] = v0903__00vT.flatten()
v0904_noise_components = v0904_noise_components__temp.copy()
v0904_noise_components__temp[i_v0905__00vX__00vU_indexed_passthrough_eval] = v0905__00vX.flatten()
v0904_noise_components = v0904_noise_components__temp.copy()

# op _00xL single_tensor_sum_no_axis_eval
# LANG: temp_temperature --> hover_temperature
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0976_hover_temperature = np.sum(v0963_temp_temperature).reshape((1,))

# op _013M_indexed_passthrough_eval
# LANG: _013L, _013P --> noise_components
# SHAPES: (1, 1, 1), (1, 1, 1) --> (2, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01902_noise_components__temp[i_v01901__013L__013M_indexed_passthrough_eval] = v01901__013L.flatten()
v01902_noise_components = v01902_noise_components__temp.copy()
v01902_noise_components__temp[i_v01903__013P__013M_indexed_passthrough_eval] = v01903__013P.flatten()
v01902_noise_components = v01902_noise_components__temp.copy()

# op _0024_power_combination_eval
# LANG: cruise_temperature --> _0025
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v099__0025 = (v096_cruise_temperature**1)
v099__0025 = (v099__0025*_0024_coeff).reshape((1,))

# op _0059 reshape_eval
# LANG: _0058 --> _005a
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0148__005a = v0147__0058.reshape((1, 1))

# op _005b_decompose_eval
# LANG: thrust_vector --> _005c, _005i, _005n
# SHAPES: (1, 3) --> (1, 1), (1, 1), (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0150__005c = ((v0132_thrust_vector.flatten())[src_indices__005c__005b]).reshape((1, 1))
v0151__005i = ((v0132_thrust_vector.flatten())[src_indices__005i__005b]).reshape((1, 1))
v0152__005n = ((v0132_thrust_vector.flatten())[src_indices__005n__005b]).reshape((1, 1))

# op _005g reshape_eval
# LANG: _0058 --> _005h
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0154__005h = v0147__0058.reshape((1, 1))

# op _005l reshape_eval
# LANG: _0058 --> _005m
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0156__005m = v0147__0058.reshape((1, 1))

# op _008C_power_combination_eval
# LANG: temperature --> _008D
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0250__008D = (v0238_temperature**1)
v0250__008D = (v0250__008D*_008C_coeff).reshape((1, 1))

# op _00AA reshape_eval
# LANG: _00As --> _00AB
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01038__00AB = v01031__00As.reshape((1, 1))

# op _00AF reshape_eval
# LANG: _00As --> _00AG
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01040__00AG = v01031__00As.reshape((1, 1))

# op _00At reshape_eval
# LANG: _00As --> _00Au
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01032__00Au = v01031__00As.reshape((1, 1))

# op _00Av_decompose_eval
# LANG: thrust_vector --> _00Aw, _00AC, _00AH
# SHAPES: (1, 3) --> (1, 1), (1, 1), (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01034__00Aw = ((v01015_thrust_vector.flatten())[src_indices__00Aw__00Av]).reshape((1, 1))
v01035__00AC = ((v01015_thrust_vector.flatten())[src_indices__00AC__00Av]).reshape((1, 1))
v01036__00AH = ((v01015_thrust_vector.flatten())[src_indices__00AH__00Av]).reshape((1, 1))

# op _00DW_power_combination_eval
# LANG: temperature --> _00DX
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01134__00DX = (v01122_temperature**1)
v01134__00DX = (v01134__00DX*_00DW_coeff).reshape((1, 1))

# op _00ID_power_combination_eval
# LANG: _angular_speed --> _00IE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01239__00IE = (v01098__angular_speed**1)
v01239__00IE = (v01239__00IE*_00ID_coeff).reshape((1, 40, 30))

# op _00JI_power_combination_eval
# LANG: _00JH, _chord --> _00JJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01301__00JJ = (v01295__00JH**1)*(v01094__chord**1)
v01301__00JJ = (v01301__00JJ*_00JI_coeff).reshape((1, 40, 30))

# op _00Jk_power_combination_eval
# LANG: _00J9, _00Jj --> _00Jl
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01248__00Jl = (v01247__00J9**1)*(v01250__00Jj**1)
v01248__00Jl = (v01248__00Jl*_00Jk_coeff).reshape((1, 40, 30))

# op _00KB_power_combination_eval
# LANG: _ux_2 --> _00KC
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01285__00KC = (v01177__ux_2**2)
v01285__00KC = (v01285__00KC*_00KB_coeff).reshape((1, 40, 30))

# op _00KH_power_combination_eval
# LANG: _00KG --> _00KI
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01289__00KI = (v01287__00KG**2)
v01289__00KI = (v01289__00KI*_00KH_coeff).reshape((1, 40, 30))

# op _00Kb_power_combination_eval
# LANG: _00Ka --> _00Kc
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01215__00Kc = (v01214__00Ka**1)
v01215__00Kc = (v01215__00Kc*_00Kb_coeff).reshape((1, 40, 30))

# op _00Kf_power_combination_eval
# LANG: _ux_2 --> _00Kg
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01218__00Kg = (v01177__ux_2**2)
v01218__00Kg = (v01218__00Kg*_00Kf_coeff).reshape((1, 40, 30))

# op _00Kl_power_combination_eval
# LANG: _00Kk --> _00Km
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01222__00Km = (v01220__00Kk**2)
v01222__00Km = (v01222__00Km*_00Kl_coeff).reshape((1, 40, 30))

# op _00Kx_power_combination_eval
# LANG: _00Kw --> _00Ky
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01282__00Ky = (v01281__00Kw**1)
v01282__00Ky = (v01282__00Ky*_00Kx_coeff).reshape((1, 40, 30))

# op _00LK_linear_combination_eval
# LANG: _00LD, _00LJ --> _00LL
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01315__00LL = _00LK_constant+1*v01311__00LD+1*v01318__00LJ

# op _00Le_power_combination_eval
# LANG: _ut, _00Ld --> _00Lf
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01273__00Lf = (v01270__00Ld**1)*(v01196__ut**1)
v01273__00Lf = (v01273__00Lf*_00Le_coeff).reshape((1, 40, 30))

# op _00Lq_power_combination_eval
# LANG: _00Lp --> _00Lr
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01307__00Lr = (v01306__00Lp**1)
v01307__00Lr = (v01307__00Lr*_00Lq_coeff).reshape((1, 40, 30))

# op _00MB_power_combination_eval
# LANG: _00MA --> _00MC
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01346__00MC = (v01345__00MA**1)
v01346__00MC = (v01346__00MC*_00MB_coeff).reshape((1,))

# op _00MP_single_tensor_sum_with_axis_eval
# LANG: _00MO --> _00MQ
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01353__00MQ = np.sum(v01351__00MO, axis = (1, 2)).reshape((1,))

# op _00Mj_power_combination_eval
# LANG: total_torque, density --> _00Mk
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01127_density = v01127_density.reshape((1,))
v01336__00Mk = (v01235_total_torque**1)*(v01127_density**-1)
v01336__00Mk = (v01336__00Mk*_00Mj_coeff).reshape((1,))
v01127_density = v01127_density.reshape((1, 1))

# op _00Mr_power_combination_eval
# LANG: _00Mq --> _00Ms
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01341__00Ms = (v01340__00Mq**2)
v01341__00Ms = (v01341__00Ms*_00Mr_coeff).reshape((1,))

# op _00OU_power_combination_eval
# LANG: temperature --> _00OV
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01407__00OV = (v01401_temperature**1)
v01407__00OV = (v01407__00OV*_00OU_coeff).reshape((1,))

# op _00Or_linear_combination_eval
# LANG: _00Oq, rotor_disk_tonal_spl --> _00Os
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01369__00Os = _00Or_constant+1*v01726_rotor_disk_tonal_spl+1*v01390__00Oq

# op _00_H_linear_combination_eval
# LANG: _00_G, rotor_disk_broadband_spl --> _00_I
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01749__00_I = _00_H_constant+1*v01889_rotor_disk_broadband_spl+1*v01770__00_G

# op _00dj_power_combination_eval
# LANG: _angular_speed --> _00dk
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0355__00dk = (v0214__angular_speed**1)
v0355__00dk = (v0355__00dk*_00dj_coeff).reshape((1, 40, 100))

# op _00e0_power_combination_eval
# LANG: _00dQ, _00d_ --> _00e1
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0364__00e1 = (v0363__00dQ**1)*(v0366__00d_**1)
v0364__00e1 = (v0364__00e1*_00e0_coeff).reshape((1, 40, 100))

# op _00eS_power_combination_eval
# LANG: _00eR --> _00eT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0331__00eT = (v0330__00eR**1)
v0331__00eT = (v0331__00eT*_00eS_coeff).reshape((1, 40, 100))

# op _00eW_power_combination_eval
# LANG: _ux_2 --> _00eX
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0334__00eX = (v0293__ux_2**2)
v0334__00eX = (v0334__00eX*_00eW_coeff).reshape((1, 40, 100))

# op _00eo_power_combination_eval
# LANG: _00en, _chord --> _00ep
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0417__00ep = (v0411__00en**1)*(v0210__chord**1)
v0417__00ep = (v0417__00ep*_00eo_coeff).reshape((1, 40, 100))

# op _00f1_power_combination_eval
# LANG: _00f0 --> _00f2
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0338__00f2 = (v0336__00f0**2)
v0338__00f2 = (v0338__00f2*_00f1_coeff).reshape((1, 40, 100))

# op _00fV_power_combination_eval
# LANG: _ut, _00fU --> _00fW
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0389__00fW = (v0386__00fU**1)*(v0312__ut**1)
v0389__00fW = (v0389__00fW*_00fV_coeff).reshape((1, 40, 100))

# op _00fd_power_combination_eval
# LANG: _00fc --> _00fe
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0398__00fe = (v0397__00fc**1)
v0398__00fe = (v0398__00fe*_00fd_coeff).reshape((1, 40, 100))

# op _00fh_power_combination_eval
# LANG: _ux_2 --> _00fi
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0401__00fi = (v0293__ux_2**2)
v0401__00fi = (v0401__00fi*_00fh_coeff).reshape((1, 40, 100))

# op _00fn_power_combination_eval
# LANG: _00fm --> _00fo
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0405__00fo = (v0403__00fm**2)
v0405__00fo = (v0405__00fo*_00fn_coeff).reshape((1, 40, 100))

# op _00g6_power_combination_eval
# LANG: _00g5 --> _00g7
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0423__00g7 = (v0422__00g5**1)
v0423__00g7 = (v0423__00g7*_00g6_coeff).reshape((1, 40, 100))

# op _00g__power_combination_eval
# LANG: total_torque, density --> _00h0
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0243_density = v0243_density.reshape((1,))
v0452__00h0 = (v0351_total_torque**1)*(v0243_density**-1)
v0452__00h0 = (v0452__00h0*_00g__coeff).reshape((1,))
v0243_density = v0243_density.reshape((1, 1))

# op _00gq_linear_combination_eval
# LANG: _00gj, _00gp --> _00gr
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0431__00gr = _00gq_constant+1*v0427__00gj+1*v0434__00gp

# op _00h7_power_combination_eval
# LANG: _00h6 --> _00h8
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0457__00h8 = (v0456__00h6**2)
v0457__00h8 = (v0457__00h8*_00h7_coeff).reshape((1,))

# op _00hh_power_combination_eval
# LANG: _00hg --> _00hi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0462__00hi = (v0461__00hg**1)
v0462__00hi = (v0462__00hi*_00hh_coeff).reshape((1,))

# op _00hv_single_tensor_sum_with_axis_eval
# LANG: _00hu --> _00hw
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0469__00hw = np.sum(v0467__00hu, axis = (1, 2)).reshape((1,))

# op _00jH_power_combination_eval
# LANG: temperature --> _00jI
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0525__00jI = (v0519_temperature**1)
v0525__00jI = (v0525__00jI*_00jH_coeff).reshape((1,))

# op _00je_linear_combination_eval
# LANG: _00jd, rotor_disk_tonal_spl --> _00jf
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0487__00jf = _00je_constant+1*v0771_rotor_disk_tonal_spl+1*v0508__00jd

# op _00jx_power_combination_eval
# LANG: temperature --> _00jy
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0520__00jy = (v0519_temperature**1)
v0520__00jy = (v0520__00jy*_00jx_coeff).reshape((1,))

# op _00sI_linear_combination_eval
# LANG: _00sH, rotor_disk_broadband_spl --> _00sJ
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0780__00sJ = _00sI_constant+1*v0890_rotor_disk_broadband_spl+1*v0801__00sH

# op _00vY_power_combination_eval
# LANG: noise_components --> _00vZ
# SHAPES: (2, 1, 1) --> (2, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0906__00vZ = (v0904_noise_components**1)
v0906__00vZ = (v0906__00vZ*_00vY_coeff).reshape((2, 1, 1))

# op _00xN_power_combination_eval
# LANG: hover_temperature --> _00xO
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0979__00xO = (v0976_hover_temperature**1)
v0979__00xO = (v0979__00xO*_00xN_coeff).reshape((1,))

# op _00zq_power_combination_eval
# LANG: rotor_disk_origin --> _00zr
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((3,))
v01016__00zr = (v010_rotor_disk_origin**1)
v01016__00zr = (v01016__00zr*_00zq_coeff).reshape((3,))
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((1, 3))

# op _013Q_power_combination_eval
# LANG: noise_components --> _013R
# SHAPES: (2, 1, 1) --> (2, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01904__013R = (v01902_noise_components**1)
v01904__013R = (v01904__013R*_013Q_coeff).reshape((2, 1, 1))

# op _000B_power_combination_eval
# LANG: cruise_altitude --> _000C
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v051__000C = (v050_cruise_altitude**6)
v051__000C = (v051__000C*_000B_coeff).reshape((1,))

# op _000G_power_combination_eval
# LANG: cruise_altitude --> _000H
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v066__000H = (v050_cruise_altitude**6)
v066__000H = (v066__000H*_000G_coeff).reshape((1,))

# op _000Q_power_combination_eval
# LANG: cruise_altitude --> _000R
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v054__000R = (v050_cruise_altitude**5)
v054__000R = (v054__000R*_000Q_coeff).reshape((1,))

# op _000U_power_combination_eval
# LANG: cruise_altitude --> _000V
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v069__000V = (v050_cruise_altitude**5)
v069__000V = (v069__000V*_000U_coeff).reshape((1,))

# op _0011_power_combination_eval
# LANG: cruise_altitude --> _0012
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v056__0012 = (v050_cruise_altitude**4)
v056__0012 = (v056__0012*_0011_coeff).reshape((1,))

# op _0015_power_combination_eval
# LANG: cruise_altitude --> _0016
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v071__0016 = (v050_cruise_altitude**4)
v071__0016 = (v071__0016*_0015_coeff).reshape((1,))

# op _001B_power_combination_eval
# LANG: cruise_altitude --> _001C
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v062__001C = (v050_cruise_altitude**1)
v062__001C = (v062__001C*_001B_coeff).reshape((1,))

# op _001F_power_combination_eval
# LANG: cruise_altitude --> _001G
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v077__001G = (v050_cruise_altitude**1)
v077__001G = (v077__001G*_001F_coeff).reshape((1,))

# op _001N_power_combination_eval
# LANG: cruise_altitude --> _001O
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v064__001O = (v050_cruise_altitude**0)
v064__001O = (v064__001O*_001N_coeff).reshape((1,))

# op _001R_power_combination_eval
# LANG: cruise_altitude --> _001S
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v079__001S = (v050_cruise_altitude**0)
v079__001S = (v079__001S*_001R_coeff).reshape((1,))

# op _001d_power_combination_eval
# LANG: cruise_altitude --> _001e
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v058__001e = (v050_cruise_altitude**3)
v058__001e = (v058__001e*_001d_coeff).reshape((1,))

# op _001h_power_combination_eval
# LANG: cruise_altitude --> _001i
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v073__001i = (v050_cruise_altitude**3)
v073__001i = (v073__001i*_001h_coeff).reshape((1,))

# op _001p_power_combination_eval
# LANG: cruise_altitude --> _001q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v060__001q = (v050_cruise_altitude**2)
v060__001q = (v060__001q*_001p_coeff).reshape((1,))

# op _001t_power_combination_eval
# LANG: cruise_altitude --> _001u
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v075__001u = (v050_cruise_altitude**2)
v075__001u = (v075__001u*_001t_coeff).reshape((1,))

# op _0026_power_combination_eval
# LANG: _0025 --> _0027
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0100__0027 = (v099__0025**1.5)
v0100__0027 = (v0100__0027*_0026_coeff).reshape((1,))

# op _004o expand_array_eval
# LANG: rotor_disk_origin --> thrust_origin
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((3,))
v0133_thrust_origin = np.einsum('b,a->ab', v010_rotor_disk_origin.reshape((3,)) ,np.ones((1,))).reshape((1, 3))
v010_rotor_disk_origin = v010_rotor_disk_origin.reshape((1, 3))

# op _005d_power_combination_eval
# LANG: _005a, _005c --> _005e
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0149__005e = (v0148__005a**1)*(v0150__005c**1)
v0149__005e = (v0149__005e*_005d_coeff).reshape((1, 1))

# op _005j_power_combination_eval
# LANG: _005i, _005h --> _005k
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0155__005k = (v0154__005h**1)*(v0151__005i**1)
v0155__005k = (v0155__005k*_005j_coeff).reshape((1, 1))

# op _005o_power_combination_eval
# LANG: _005n, _005m --> _005p
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0157__005p = (v0156__005m**1)*(v0152__005n**1)
v0157__005p = (v0157__005p*_005o_coeff).reshape((1, 1))

# op _008E_power_combination_eval
# LANG: _008D --> speed_of_sound
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0251_speed_of_sound = (v0250__008D**0.5)
v0251_speed_of_sound = (v0251_speed_of_sound*_008E_coeff).reshape((1, 1))

# op _00AD_power_combination_eval
# LANG: _00AC, _00AB --> _00AE
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01039__00AE = (v01038__00AB**1)*(v01035__00AC**1)
v01039__00AE = (v01039__00AE*_00AD_coeff).reshape((1, 1))

# op _00AI_power_combination_eval
# LANG: _00AH, _00AG --> _00AJ
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01041__00AJ = (v01040__00AG**1)*(v01036__00AH**1)
v01041__00AJ = (v01041__00AJ*_00AI_coeff).reshape((1, 1))

# op _00Ax_power_combination_eval
# LANG: _00Au, _00Aw --> _00Ay
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01033__00Ay = (v01032__00Au**1)*(v01034__00Aw**1)
v01033__00Ay = (v01033__00Ay*_00Ax_coeff).reshape((1, 1))

# op _00DY_power_combination_eval
# LANG: _00DX --> speed_of_sound
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01135_speed_of_sound = (v01134__00DX**0.5)
v01135_speed_of_sound = (v01135_speed_of_sound*_00DY_coeff).reshape((1, 1))

# op _00IF_power_combination_eval
# LANG: _00IE --> _00IG
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01240__00IG = (v01239__00IE**1)
v01240__00IG = (v01240__00IG*_00IF_coeff).reshape((1, 40, 30))

# op _00JK_power_combination_eval
# LANG: _00JJ, _dr --> _00JL
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01302__00JL = (v01301__00JJ**1)*(v01087__dr**1)
v01302__00JL = (v01302__00JL*_00JK_coeff).reshape((1, 40, 30))

# op _00Jm_power_combination_eval
# LANG: _00Jl, _chord --> _00Jn
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01254__00Jn = (v01248__00Jl**1)*(v01094__chord**1)
v01254__00Jn = (v01254__00Jn*_00Jm_coeff).reshape((1, 40, 30))

# op _00KJ_linear_combination_eval
# LANG: _00KC, _00KI --> _00KK
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01286__00KK = _00KJ_constant+1*v01285__00KC+1*v01289__00KI

# op _00Kd_power_combination_eval
# LANG: _00GM, _00Kc --> _00Ke
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01216__00Ke = (v01215__00Kc**1)*(v01205__00GM**1)
v01216__00Ke = (v01216__00Ke*_00Kd_coeff).reshape((1, 40, 30))

# op _00Kn_linear_combination_eval
# LANG: _00Kg, _00Km --> _00Ko
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01219__00Ko = _00Kn_constant+1*v01218__00Kg+1*v01222__00Km

# op _00Kz_power_combination_eval
# LANG: _00GM, _00Ky --> _00KA
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01283__00KA = (v01282__00Ky**1)*(v01205__00GM**1)
v01283__00KA = (v01283__00KA*_00Kz_coeff).reshape((1, 40, 30))

# op _00LM_power_combination_eval
# LANG: _00Lr, _00LL --> _00LN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01308__00LN = (v01307__00Lr**1)*(v01315__00LL**1)
v01308__00LN = (v01308__00LN*_00LM_coeff).reshape((1, 40, 30))

# op _00Lg_power_combination_eval
# LANG: _00Lf, _radius --> _00Lh
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01274__00Lh = (v01273__00Lf**1)*(v01099__radius**1)
v01274__00Lh = (v01274__00Lh*_00Lg_coeff).reshape((1, 40, 30))

# op _00MD_power_combination_eval
# LANG: _00MC --> _00ME
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01347__00ME = (v01346__00MC**5)
v01347__00ME = (v01347__00ME*_00MD_coeff).reshape((1,))

# op _00MR_power_combination_eval
# LANG: _00MQ --> _00MS
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01354__00MS = (v01353__00MQ**1)
v01354__00MS = (v01354__00MS*_00MR_coeff).reshape((1,))

# op _00MZ_power_combination_eval
# LANG: C_T --> _00M_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01358__00M_ = (v01330_C_T**1)
v01358__00M_ = (v01358__00M_*_00MZ_coeff).reshape((1,))

# op _00Mt_power_combination_eval
# LANG: _00Mk, _00Ms --> _00Mu
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01337__00Mu = (v01336__00Mk**1)*(v01341__00Ms**-1)
v01337__00Mu = (v01337__00Mu*_00Mt_coeff).reshape((1,))

# op _00OW_power_combination_eval
# LANG: _00OV --> _00OX
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01408__00OX = (v01407__00OV**1.5)
v01408__00OX = (v01408__00OX*_00OW_coeff).reshape((1,))

# op _00Ot_power_combination_eval
# LANG: _00Os --> _00Ou
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01394__00Ou = (v01369__00Os**1)
v01394__00Ou = (v01394__00Ou*_00Ot_coeff).reshape((1, 1))

# op _00QB_linear_combination_eval
# LANG: rel_obs_z_pos --> _00QC
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01466__00QC = _00QB_constant+1*v01453_rel_obs_z_pos

# op _00Qt_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00Qu
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01461__00Qu = (v01453_rel_obs_z_pos**1)*(v01460_rel_obs_dist**-1)
v01461__00Qu = (v01461__00Qu*_00Qt_coeff).reshape((1, 1, 1))

# op _00_J_power_combination_eval
# LANG: _00_I --> _00_K
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01774__00_K = (v01749__00_I**1)
v01774__00_K = (v01774__00_K*_00_J_coeff).reshape((1, 1))

# op _00dl_power_combination_eval
# LANG: _00dk --> _00dm
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0356__00dm = (v0355__00dk**1)
v0356__00dm = (v0356__00dm*_00dl_coeff).reshape((1, 40, 100))

# op _00e2_power_combination_eval
# LANG: _00e1, _chord --> _00e3
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0370__00e3 = (v0364__00e1**1)*(v0210__chord**1)
v0370__00e3 = (v0370__00e3*_00e2_coeff).reshape((1, 40, 100))

# op _00eU_power_combination_eval
# LANG: _00bs, _00eT --> _00eV
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0332__00eV = (v0331__00eT**1)*(v0321__00bs**1)
v0332__00eV = (v0332__00eV*_00eU_coeff).reshape((1, 40, 100))

# op _00eq_power_combination_eval
# LANG: _00ep, _dr --> _00er
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0418__00er = (v0417__00ep**1)*(v0203__dr**1)
v0418__00er = (v0418__00er*_00eq_coeff).reshape((1, 40, 100))

# op _00f3_linear_combination_eval
# LANG: _00eX, _00f2 --> _00f4
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0335__00f4 = _00f3_constant+1*v0334__00eX+1*v0338__00f2

# op _00fX_power_combination_eval
# LANG: _00fW, _radius --> _00fY
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0390__00fY = (v0389__00fW**1)*(v0215__radius**1)
v0390__00fY = (v0390__00fY*_00fX_coeff).reshape((1, 40, 100))

# op _00ff_power_combination_eval
# LANG: _00bs, _00fe --> _00fg
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0399__00fg = (v0398__00fe**1)*(v0321__00bs**1)
v0399__00fg = (v0399__00fg*_00ff_coeff).reshape((1, 40, 100))

# op _00fp_linear_combination_eval
# LANG: _00fi, _00fo --> _00fq
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0402__00fq = _00fp_constant+1*v0401__00fi+1*v0405__00fo

# op _00gs_power_combination_eval
# LANG: _00g7, _00gr --> _00gt
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0424__00gt = (v0423__00g7**1)*(v0431__00gr**1)
v0424__00gt = (v0424__00gt*_00gs_coeff).reshape((1, 40, 100))

# op _00h9_power_combination_eval
# LANG: _00h0, _00h8 --> _00ha
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0453__00ha = (v0452__00h0**1)*(v0457__00h8**-1)
v0453__00ha = (v0453__00ha*_00h9_coeff).reshape((1,))

# op _00hF_power_combination_eval
# LANG: C_T --> _00hG
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0474__00hG = (v0446_C_T**1)
v0474__00hG = (v0474__00hG*_00hF_coeff).reshape((1,))

# op _00hj_power_combination_eval
# LANG: _00hi --> _00hk
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0463__00hk = (v0462__00hi**5)
v0463__00hk = (v0463__00hk*_00hj_coeff).reshape((1,))

# op _00hx_power_combination_eval
# LANG: _00hw --> _00hy
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0470__00hy = (v0469__00hw**1)
v0470__00hy = (v0470__00hy*_00hx_coeff).reshape((1,))

# op _00jJ_power_combination_eval
# LANG: _00jI --> _00jK
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0526__00jK = (v0525__00jI**1.5)
v0526__00jK = (v0526__00jK*_00jJ_coeff).reshape((1,))

# op _00jg_power_combination_eval
# LANG: _00jf --> _00jh
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0512__00jh = (v0487__00jf**1)
v0512__00jh = (v0512__00jh*_00jg_coeff).reshape((1, 1))

# op _00jz_power_combination_eval
# LANG: _00jy --> _00jA
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0521__00jA = (v0520__00jy**5.258643795229161)
v0521__00jA = (v0521__00jA*_00jz_coeff).reshape((1,))

# op _00lg_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00lh
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0579__00lh = (v0571_rel_obs_z_pos**1)*(v0578_rel_obs_dist**-1)
v0579__00lh = (v0579__00lh*_00lg_coeff).reshape((1, 1, 1))

# op _00lo_linear_combination_eval
# LANG: rel_obs_z_pos --> _00lp
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0584__00lp = _00lo_constant+1*v0571_rel_obs_z_pos

# op _00sK_power_combination_eval
# LANG: _00sJ --> _00sL
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0805__00sL = (v0780__00sJ**1)
v0805__00sL = (v0805__00sL*_00sK_coeff).reshape((1, 1))

# op _00ub_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00uc
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0855__00uc = (v0847_rel_obs_z_pos**1)*(v0854_rel_obs_dist**-1)
v0855__00uc = (v0855__00uc*_00ub_coeff).reshape((1, 1, 1))

# op _00uj_linear_combination_eval
# LANG: rel_obs_z_pos --> _00uk
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0860__00uk = _00uj_constant+1*v0847_rel_obs_z_pos

# op _00v__exp_a_eval
# LANG: _00vZ --> _00w0
# SHAPES: (2, 1, 1) --> (2, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0907__00w0 = _00v__exp_a_eval_a**v0906__00vZ

# op _00wC_power_combination_eval
# LANG: hover_altitude --> _00wD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0949__00wD = (v0930_hover_altitude**5)
v0949__00wD = (v0949__00wD*_00wC_coeff).reshape((1,))

# op _00wK_power_combination_eval
# LANG: hover_altitude --> _00wL
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0936__00wL = (v0930_hover_altitude**4)
v0936__00wL = (v0936__00wL*_00wK_coeff).reshape((1,))

# op _00wO_power_combination_eval
# LANG: hover_altitude --> _00wP
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0951__00wP = (v0930_hover_altitude**4)
v0951__00wP = (v0951__00wP*_00wO_coeff).reshape((1,))

# op _00wW_power_combination_eval
# LANG: hover_altitude --> _00wX
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0938__00wX = (v0930_hover_altitude**3)
v0938__00wX = (v0938__00wX*_00wW_coeff).reshape((1,))

# op _00w__power_combination_eval
# LANG: hover_altitude --> _00x0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0953__00x0 = (v0930_hover_altitude**3)
v0953__00x0 = (v0953__00x0*_00w__coeff).reshape((1,))

# op _00wj_power_combination_eval
# LANG: hover_altitude --> _00wk
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0931__00wk = (v0930_hover_altitude**6)
v0931__00wk = (v0931__00wk*_00wj_coeff).reshape((1,))

# op _00wo_power_combination_eval
# LANG: hover_altitude --> _00wp
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0946__00wp = (v0930_hover_altitude**6)
v0946__00wp = (v0946__00wp*_00wo_coeff).reshape((1,))

# op _00wy_power_combination_eval
# LANG: hover_altitude --> _00wz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0934__00wz = (v0930_hover_altitude**5)
v0934__00wz = (v0934__00wz*_00wy_coeff).reshape((1,))

# op _00x7_power_combination_eval
# LANG: hover_altitude --> _00x8
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0940__00x8 = (v0930_hover_altitude**2)
v0940__00x8 = (v0940__00x8*_00x7_coeff).reshape((1,))

# op _00xP_power_combination_eval
# LANG: _00xO --> _00xQ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0980__00xQ = (v0979__00xO**1.5)
v0980__00xQ = (v0980__00xQ*_00xP_coeff).reshape((1,))

# op _00xb_power_combination_eval
# LANG: hover_altitude --> _00xc
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0955__00xc = (v0930_hover_altitude**2)
v0955__00xc = (v0955__00xc*_00xb_coeff).reshape((1,))

# op _00xj_power_combination_eval
# LANG: hover_altitude --> _00xk
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0942__00xk = (v0930_hover_altitude**1)
v0942__00xk = (v0942__00xk*_00xj_coeff).reshape((1,))

# op _00xn_power_combination_eval
# LANG: hover_altitude --> _00xo
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0957__00xo = (v0930_hover_altitude**1)
v0957__00xo = (v0957__00xo*_00xn_coeff).reshape((1,))

# op _00xv_power_combination_eval
# LANG: hover_altitude --> _00xw
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0944__00xw = (v0930_hover_altitude**0)
v0944__00xw = (v0944__00xw*_00xv_coeff).reshape((1,))

# op _00xz_power_combination_eval
# LANG: hover_altitude --> _00xA
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0959__00xA = (v0930_hover_altitude**0)
v0959__00xA = (v0959__00xA*_00xz_coeff).reshape((1,))

# op _00zI expand_array_eval
# LANG: _00zr --> thrust_origin
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01017_thrust_origin = np.einsum('b,a->ab', v01016__00zr.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

# op _011a_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _011b
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01825__011b = (v01817_rel_obs_z_pos**1)*(v01824_rel_obs_dist**-1)
v01825__011b = (v01825__011b*_011a_coeff).reshape((1, 1, 1))

# op _011i_linear_combination_eval
# LANG: rel_obs_z_pos --> _011j
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01830__011j = _011i_constant+1*v01817_rel_obs_z_pos

# op _013S_exp_a_eval
# LANG: _013R --> _013T
# SHAPES: (2, 1, 1) --> (2, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01905__013T = _013S_exp_a_eval_a**v01904__013R

# op _000D_power_combination_eval
# LANG: _000C --> _000E
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v052__000E = (v051__000C**1)
v052__000E = (v052__000E*_000D_coeff).reshape((1,))

# op _000I_power_combination_eval
# LANG: _000H --> _000J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v067__000J = (v066__000H**1)
v067__000J = (v067__000J*_000I_coeff).reshape((1,))

# op _000S_power_combination_eval
# LANG: _000R --> _000T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v055__000T = (v054__000R**1)
v055__000T = (v055__000T*_000S_coeff).reshape((1,))

# op _000W_power_combination_eval
# LANG: _000V --> _000X
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v070__000X = (v069__000V**1)
v070__000X = (v070__000X*_000W_coeff).reshape((1,))

# op _0013_power_combination_eval
# LANG: _0012 --> _0014
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v057__0014 = (v056__0012**1)
v057__0014 = (v057__0014*_0013_coeff).reshape((1,))

# op _0017_power_combination_eval
# LANG: _0016 --> _0018
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v072__0018 = (v071__0016**1)
v072__0018 = (v072__0018*_0017_coeff).reshape((1,))

# op _001D_power_combination_eval
# LANG: _001C --> _001E
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v063__001E = (v062__001C**1)
v063__001E = (v063__001E*_001D_coeff).reshape((1,))

# op _001H_power_combination_eval
# LANG: _001G --> _001I
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v078__001I = (v077__001G**1)
v078__001I = (v078__001I*_001H_coeff).reshape((1,))

# op _001P_power_combination_eval
# LANG: _001O --> _001Q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v065__001Q = (v064__001O**1)
v065__001Q = (v065__001Q*_001P_coeff).reshape((1,))

# op _001T_power_combination_eval
# LANG: _001S --> _001U
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v080__001U = (v079__001S**1)
v080__001U = (v080__001U*_001T_coeff).reshape((1,))

# op _001f_power_combination_eval
# LANG: _001e --> _001g
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v059__001g = (v058__001e**1)
v059__001g = (v059__001g*_001f_coeff).reshape((1,))

# op _001j_power_combination_eval
# LANG: _001i --> _001k
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v074__001k = (v073__001i**1)
v074__001k = (v074__001k*_001j_coeff).reshape((1,))

# op _001r_power_combination_eval
# LANG: _001q --> _001s
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v061__001s = (v060__001q**1)
v061__001s = (v061__001s*_001r_coeff).reshape((1,))

# op _001v_power_combination_eval
# LANG: _001u --> _001w
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v076__001w = (v075__001u**1)
v076__001w = (v076__001w*_001v_coeff).reshape((1,))

# op _0028_power_combination_eval
# LANG: _0027 --> _0029
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0101__0029 = (v0100__0027**1)
v0101__0029 = (v0101__0029*_0028_coeff).reshape((1,))

# op _004M expand_scalar_eval
# LANG: speed_of_sound --> _004N
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0251_speed_of_sound = v0251_speed_of_sound.reshape((1,))
v0144__004N = np.empty((1, 40, 100))
v0144__004N.fill(v0251_speed_of_sound.item())
v0251_speed_of_sound = v0251_speed_of_sound.reshape((1, 1))

# op _005f_indexed_passthrough_eval
# LANG: _005e, _005k, _005p --> F
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0153_F__temp[i_v0149__005e__005f_indexed_passthrough_eval] = v0149__005e.flatten()
v0153_F = v0153_F__temp.copy()
v0153_F__temp[i_v0155__005k__005f_indexed_passthrough_eval] = v0155__005k.flatten()
v0153_F = v0153_F__temp.copy()
v0153_F__temp[i_v0157__005p__005f_indexed_passthrough_eval] = v0157__005p.flatten()
v0153_F = v0153_F__temp.copy()

# op _005q_linear_combination_eval
# LANG: thrust_origin, reference_point --> _005r
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0158__005r = _005q_constant+1*v0133_thrust_origin+-1*v0159_reference_point

# op _00A5 expand_scalar_eval
# LANG: speed_of_sound --> _00A6
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01135_speed_of_sound = v01135_speed_of_sound.reshape((1,))
v01028__00A6 = np.empty((1, 40, 30))
v01028__00A6.fill(v01135_speed_of_sound.item())
v01135_speed_of_sound = v01135_speed_of_sound.reshape((1, 1))

# op _00AK_linear_combination_eval
# LANG: thrust_origin, reference_point --> _00AL
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01042__00AL = _00AK_constant+1*v01017_thrust_origin+-1*v01043_reference_point

# op _00Az_indexed_passthrough_eval
# LANG: _00Ay, _00AE, _00AJ --> F
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01037_F__temp[i_v01033__00Ay__00Az_indexed_passthrough_eval] = v01033__00Ay.flatten()
v01037_F = v01037_F__temp.copy()
v01037_F__temp[i_v01039__00AE__00Az_indexed_passthrough_eval] = v01039__00AE.flatten()
v01037_F = v01037_F__temp.copy()
v01037_F__temp[i_v01041__00AJ__00Az_indexed_passthrough_eval] = v01041__00AJ.flatten()
v01037_F = v01037_F__temp.copy()

# op _00IB_power_combination_eval
# LANG: _00GM, _local_thrust --> _00IC
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01237__00IC = (v01210__local_thrust**1)*(v01205__00GM**-1)
v01237__00IC = (v01237__00IC*_00IB_coeff).reshape((1, 40, 30))

# op _00IH_power_combination_eval
# LANG: _00IG --> _00II
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01241__00II = (v01240__00IG**2)
v01241__00II = (v01241__00II*_00IH_coeff).reshape((1, 40, 30))

# op _00IL_power_combination_eval
# LANG: _rotor_radius --> _00IM
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01243__00IM = (v01086__rotor_radius**1)
v01243__00IM = (v01243__00IM*_00IL_coeff).reshape((1, 40, 30))

# op _00JM_power_combination_eval
# LANG: _00JL, _radius --> _local_torque_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01303__local_torque_2 = (v01302__00JL**1)*(v01099__radius**1)
v01303__local_torque_2 = (v01303__local_torque_2*_00JM_coeff).reshape((1, 40, 30))

# op _00Jo_power_combination_eval
# LANG: _00Jn, _dr --> _local_thrust_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01255__local_thrust_2 = (v01254__00Jn**1)*(v01087__dr**1)
v01255__local_thrust_2 = (v01255__local_thrust_2*_00Jo_coeff).reshape((1, 40, 30))

# op _00KL_power_combination_eval
# LANG: _00KA, _00KK --> _00KM
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01284__00KM = (v01283__00KA**1)*(v01286__00KK**1)
v01284__00KM = (v01284__00KM*_00KL_coeff).reshape((1, 40, 30))

# op _00Kp_power_combination_eval
# LANG: _00Ke, _00Ko --> _00Kq
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01217__00Kq = (v01216__00Ke**1)*(v01219__00Ko**1)
v01217__00Kq = (v01217__00Kq*_00Kp_coeff).reshape((1, 40, 30))

# op _00LO_power_combination_eval
# LANG: _00LN, prandtl_loss_factor --> _00LP
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01319__00LP = (v01308__00LN**1)*(v01149_prandtl_loss_factor**1)
v01319__00LP = (v01319__00LP*_00LO_coeff).reshape((1, 40, 30))

# op _00Li_power_combination_eval
# LANG: _00Lh, _dr --> _local_thrust_star
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01275__local_thrust_star = (v01274__00Lh**1)*(v01087__dr**1)
v01275__local_thrust_star = (v01275__local_thrust_star*_00Li_coeff).reshape((1, 40, 30))

# op _00MF_power_combination_eval
# LANG: _00Mu, _00ME --> C_Q
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01342_C_Q = (v01337__00Mu**1)*(v01347__00ME**-1)
v01342_C_Q = (v01342_C_Q*_00MF_coeff).reshape((1,))

# op _00MT_power_combination_eval
# LANG: _00MS --> J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01355_J = (v01354__00MS**1)
v01355_J = (v01355_J*_00MT_coeff).reshape((1,))

# op _00N0_power_combination_eval
# LANG: _00M_ --> _00N1
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01359__00N1 = (v01358__00M_**0.5)
v01359__00N1 = (v01359__00N1*_00N0_coeff).reshape((1,))

# op _00OY_power_combination_eval
# LANG: _00OX --> _00OZ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01409__00OZ = (v01408__00OX**1)
v01409__00OZ = (v01409__00OZ*_00OY_coeff).reshape((1,))

# op _00Ov_exp_a_eval
# LANG: _00Ou --> _00Ow
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01395__00Ow = _00Ov_exp_a_eval_a**v01394__00Ou

# op _00QD_power_combination_eval
# LANG: _00QC --> _00QE
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01467__00QE = (v01466__00QC**2)
v01467__00QE = (v01467__00QE*_00QD_coeff).reshape((1, 1, 1))

# op _00Qv arccos_eval
# LANG: _00Qu --> _00Qw
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01462__00Qw = np.arccos(v01461__00Qu)

# op _00Qx_linear_combination_eval
# LANG: rel_obs_z_pos --> _00Qy
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01464__00Qy = _00Qx_constant+1*v01453_rel_obs_z_pos

# op _00_L_exp_a_eval
# LANG: _00_K --> _00_M
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01775__00_M = _00_L_exp_a_eval_a**v01774__00_K

# op _00dh_power_combination_eval
# LANG: _00bs, _local_thrust --> _00di
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0353__00di = (v0326__local_thrust**1)*(v0321__00bs**-1)
v0353__00di = (v0353__00di*_00dh_coeff).reshape((1, 40, 100))

# op _00dn_power_combination_eval
# LANG: _00dm --> _00do
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0357__00do = (v0356__00dm**2)
v0357__00do = (v0357__00do*_00dn_coeff).reshape((1, 40, 100))

# op _00dr_power_combination_eval
# LANG: _rotor_radius --> _00ds
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0359__00ds = (v0202__rotor_radius**1)
v0359__00ds = (v0359__00ds*_00dr_coeff).reshape((1, 40, 100))

# op _00e4_power_combination_eval
# LANG: _00e3, _dr --> _local_thrust_2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0371__local_thrust_2 = (v0370__00e3**1)*(v0203__dr**1)
v0371__local_thrust_2 = (v0371__local_thrust_2*_00e4_coeff).reshape((1, 40, 100))

# op _00es_power_combination_eval
# LANG: _00er, _radius --> _local_torque_2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0419__local_torque_2 = (v0418__00er**1)*(v0215__radius**1)
v0419__local_torque_2 = (v0419__local_torque_2*_00es_coeff).reshape((1, 40, 100))

# op _00f5_power_combination_eval
# LANG: _00eV, _00f4 --> _00f6
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0333__00f6 = (v0332__00eV**1)*(v0335__00f4**1)
v0333__00f6 = (v0333__00f6*_00f5_coeff).reshape((1, 40, 100))

# op _00fZ_power_combination_eval
# LANG: _00fY, _dr --> _local_thrust_star
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0391__local_thrust_star = (v0390__00fY**1)*(v0203__dr**1)
v0391__local_thrust_star = (v0391__local_thrust_star*_00fZ_coeff).reshape((1, 40, 100))

# op _00fr_power_combination_eval
# LANG: _00fg, _00fq --> _00fs
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0400__00fs = (v0399__00fg**1)*(v0402__00fq**1)
v0400__00fs = (v0400__00fs*_00fr_coeff).reshape((1, 40, 100))

# op _00gu_power_combination_eval
# LANG: _00gt, prandtl_loss_factor --> _00gv
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0435__00gv = (v0424__00gt**1)*(v0265_prandtl_loss_factor**1)
v0435__00gv = (v0435__00gv*_00gu_coeff).reshape((1, 40, 100))

# op _00hH_power_combination_eval
# LANG: _00hG --> _00hI
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0475__00hI = (v0474__00hG**0.5)
v0475__00hI = (v0475__00hI*_00hH_coeff).reshape((1,))

# op _00hl_power_combination_eval
# LANG: _00ha, _00hk --> C_Q
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0458_C_Q = (v0453__00ha**1)*(v0463__00hk**-1)
v0458_C_Q = (v0458_C_Q*_00hl_coeff).reshape((1,))

# op _00hz_power_combination_eval
# LANG: _00hy --> J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0471_J = (v0470__00hy**1)
v0471_J = (v0471_J*_00hz_coeff).reshape((1,))

# op _00jB_power_combination_eval
# LANG: _00jA --> pressure
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0522_pressure = (v0521__00jA**1)
v0522_pressure = (v0522_pressure*_00jB_coeff).reshape((1,))

# op _00jL_power_combination_eval
# LANG: _00jK --> _00jM
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0527__00jM = (v0526__00jK**1)
v0527__00jM = (v0527__00jM*_00jL_coeff).reshape((1,))

# op _00ji_exp_a_eval
# LANG: _00jh --> _00jj
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0513__00jj = _00ji_exp_a_eval_a**v0512__00jh

# op _00li arccos_eval
# LANG: _00lh --> _00lj
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0580__00lj = np.arccos(v0579__00lh)

# op _00lk_linear_combination_eval
# LANG: rel_obs_z_pos --> _00ll
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0582__00ll = _00lk_constant+1*v0571_rel_obs_z_pos

# op _00lq_power_combination_eval
# LANG: _00lp --> _00lr
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0585__00lr = (v0584__00lp**2)
v0585__00lr = (v0585__00lr*_00lq_coeff).reshape((1, 1, 1))

# op _00sM_exp_a_eval
# LANG: _00sL --> _00sN
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0806__00sN = _00sM_exp_a_eval_a**v0805__00sL

# op _00ud arccos_eval
# LANG: _00uc --> _00ue
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0856__00ue = np.arccos(v0855__00uc)

# op _00uf_linear_combination_eval
# LANG: rel_obs_z_pos --> _00ug
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0858__00ug = _00uf_constant+1*v0847_rel_obs_z_pos

# op _00ul_power_combination_eval
# LANG: _00uk --> _00um
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0861__00um = (v0860__00uk**2)
v0861__00um = (v0861__00um*_00ul_coeff).reshape((1, 1, 1))

# op _00w1_single_tensor_sum_with_axis_eval
# LANG: _00w0 --> _00w2
# SHAPES: (2, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0908__00w2 = np.sum(v0907__00w0, axis = (0,)).reshape((1, 1))

# op _00wA_power_combination_eval
# LANG: _00wz --> _00wB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0935__00wB = (v0934__00wz**1)
v0935__00wB = (v0935__00wB*_00wA_coeff).reshape((1,))

# op _00wE_power_combination_eval
# LANG: _00wD --> _00wF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0950__00wF = (v0949__00wD**1)
v0950__00wF = (v0950__00wF*_00wE_coeff).reshape((1,))

# op _00wM_power_combination_eval
# LANG: _00wL --> _00wN
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0937__00wN = (v0936__00wL**1)
v0937__00wN = (v0937__00wN*_00wM_coeff).reshape((1,))

# op _00wQ_power_combination_eval
# LANG: _00wP --> _00wR
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0952__00wR = (v0951__00wP**1)
v0952__00wR = (v0952__00wR*_00wQ_coeff).reshape((1,))

# op _00wY_power_combination_eval
# LANG: _00wX --> _00wZ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0939__00wZ = (v0938__00wX**1)
v0939__00wZ = (v0939__00wZ*_00wY_coeff).reshape((1,))

# op _00wl_power_combination_eval
# LANG: _00wk --> _00wm
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0932__00wm = (v0931__00wk**1)
v0932__00wm = (v0932__00wm*_00wl_coeff).reshape((1,))

# op _00wq_power_combination_eval
# LANG: _00wp --> _00wr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0947__00wr = (v0946__00wp**1)
v0947__00wr = (v0947__00wr*_00wq_coeff).reshape((1,))

# op _00x1_power_combination_eval
# LANG: _00x0 --> _00x2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0954__00x2 = (v0953__00x0**1)
v0954__00x2 = (v0954__00x2*_00x1_coeff).reshape((1,))

# op _00x9_power_combination_eval
# LANG: _00x8 --> _00xa
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0941__00xa = (v0940__00x8**1)
v0941__00xa = (v0941__00xa*_00x9_coeff).reshape((1,))

# op _00xB_power_combination_eval
# LANG: _00xA --> _00xC
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0960__00xC = (v0959__00xA**1)
v0960__00xC = (v0960__00xC*_00xB_coeff).reshape((1,))

# op _00xR_power_combination_eval
# LANG: _00xQ --> _00xS
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0981__00xS = (v0980__00xQ**1)
v0981__00xS = (v0981__00xS*_00xR_coeff).reshape((1,))

# op _00xd_power_combination_eval
# LANG: _00xc --> _00xe
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0956__00xe = (v0955__00xc**1)
v0956__00xe = (v0956__00xe*_00xd_coeff).reshape((1,))

# op _00xl_power_combination_eval
# LANG: _00xk --> _00xm
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0943__00xm = (v0942__00xk**1)
v0943__00xm = (v0943__00xm*_00xl_coeff).reshape((1,))

# op _00xp_power_combination_eval
# LANG: _00xo --> _00xq
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0958__00xq = (v0957__00xo**1)
v0958__00xq = (v0958__00xq*_00xp_coeff).reshape((1,))

# op _00xx_power_combination_eval
# LANG: _00xw --> _00xy
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0945__00xy = (v0944__00xw**1)
v0945__00xy = (v0945__00xy*_00xx_coeff).reshape((1,))

# op _011c arccos_eval
# LANG: _011b --> _011d
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01826__011d = np.arccos(v01825__011b)

# op _011e_linear_combination_eval
# LANG: rel_obs_z_pos --> _011f
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01828__011f = _011e_constant+1*v01817_rel_obs_z_pos

# op _011k_power_combination_eval
# LANG: _011j --> _011l
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01831__011l = (v01830__011j**2)
v01831__011l = (v01831__011l*_011k_coeff).reshape((1, 1, 1))

# op _013U_single_tensor_sum_with_axis_eval
# LANG: _013T --> _013V
# SHAPES: (2, 1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01906__013V = np.sum(v01905__013T, axis = (0,)).reshape((1, 1))

# op _000F_indexed_passthrough_eval
# LANG: _000E, _000T, _0014, _001g, _001s, _001E, _001Q --> temp_density
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v053_temp_density__temp[i_v052__000E__000F_indexed_passthrough_eval] = v052__000E.flatten()
v053_temp_density = v053_temp_density__temp.copy()
v053_temp_density__temp[i_v055__000T__000F_indexed_passthrough_eval] = v055__000T.flatten()
v053_temp_density = v053_temp_density__temp.copy()
v053_temp_density__temp[i_v057__0014__000F_indexed_passthrough_eval] = v057__0014.flatten()
v053_temp_density = v053_temp_density__temp.copy()
v053_temp_density__temp[i_v059__001g__000F_indexed_passthrough_eval] = v059__001g.flatten()
v053_temp_density = v053_temp_density__temp.copy()
v053_temp_density__temp[i_v061__001s__000F_indexed_passthrough_eval] = v061__001s.flatten()
v053_temp_density = v053_temp_density__temp.copy()
v053_temp_density__temp[i_v063__001E__000F_indexed_passthrough_eval] = v063__001E.flatten()
v053_temp_density = v053_temp_density__temp.copy()
v053_temp_density__temp[i_v065__001Q__000F_indexed_passthrough_eval] = v065__001Q.flatten()
v053_temp_density = v053_temp_density__temp.copy()

# op _000K_indexed_passthrough_eval
# LANG: _000J, _000X, _0018, _001k, _001w, _001I, _001U --> temp_pressure
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v068_temp_pressure__temp[i_v067__000J__000K_indexed_passthrough_eval] = v067__000J.flatten()
v068_temp_pressure = v068_temp_pressure__temp.copy()
v068_temp_pressure__temp[i_v070__000X__000K_indexed_passthrough_eval] = v070__000X.flatten()
v068_temp_pressure = v068_temp_pressure__temp.copy()
v068_temp_pressure__temp[i_v072__0018__000K_indexed_passthrough_eval] = v072__0018.flatten()
v068_temp_pressure = v068_temp_pressure__temp.copy()
v068_temp_pressure__temp[i_v074__001k__000K_indexed_passthrough_eval] = v074__001k.flatten()
v068_temp_pressure = v068_temp_pressure__temp.copy()
v068_temp_pressure__temp[i_v076__001w__000K_indexed_passthrough_eval] = v076__001w.flatten()
v068_temp_pressure = v068_temp_pressure__temp.copy()
v068_temp_pressure__temp[i_v078__001I__000K_indexed_passthrough_eval] = v078__001I.flatten()
v068_temp_pressure = v068_temp_pressure__temp.copy()
v068_temp_pressure__temp[i_v080__001U__000K_indexed_passthrough_eval] = v080__001U.flatten()
v068_temp_pressure = v068_temp_pressure__temp.copy()

# op _002__power_combination_eval
# LANG: u --> p
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v039_p = (v028_u**1)
v039_p = (v039_p*_002__coeff).reshape((1,))

# op _002a_power_combination_eval
# LANG: _0029 --> _002b
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0102__002b = (v0101__0029**1)
v0102__002b = (v0102__002b*_002a_coeff).reshape((1,))

# op _002c_linear_combination_eval
# LANG: cruise_temperature --> _002d
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0104__002d = _002c_constant+1*v096_cruise_temperature

# op _002u_power_combination_eval
# LANG: _002t --> _002v
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v042__002v = (v023__002t**1)
v042__002v = (v042__002v*_002u_coeff).reshape((1,))

# op _0031_power_combination_eval
# LANG: u --> q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v040_q = (v028_u**1)
v040_q = (v040_q*_0031_coeff).reshape((1,))

# op _0033_power_combination_eval
# LANG: u --> r
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v041_r = (v028_u**1)
v041_r = (v041_r*_0033_coeff).reshape((1,))

# op _004U_power_combination_eval
# LANG: _004E, _004N --> mach_number
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0143_mach_number = (v0139__004E**1)*(v0144__004N**-1)
v0143_mach_number = (v0143_mach_number*_004U_coeff).reshape((1, 40, 100))

# op _005s cross_product_eval
# LANG: F, _005r --> _005t
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0160__005t = np.cross(v0158__005r, v0153_F, axisa = 1, axisb = 1, axisc = 1)

# op _00AM cross_product_eval
# LANG: F, _00AL --> _00AN
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01044__00AN = np.cross(v01042__00AL, v01037_F, axisa = 1, axisb = 1, axisc = 1)

# op _00Ad_power_combination_eval
# LANG: _00zY, _00A6 --> mach_number
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01027_mach_number = (v01023__00zY**1)*(v01028__00A6**-1)
v01027_mach_number = (v01027_mach_number*_00Ad_coeff).reshape((1, 40, 30))

# op _00IJ_power_combination_eval
# LANG: _00IC, _00II --> _00IK
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01238__00IK = (v01237__00IC**1)*(v01241__00II**-1)
v01238__00IK = (v01238__00IK*_00IJ_coeff).reshape((1, 40, 30))

# op _00IN_power_combination_eval
# LANG: _00IM --> _00IO
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01244__00IO = (v01243__00IM**4)
v01244__00IO = (v01244__00IO*_00IN_coeff).reshape((1, 40, 30))

# op _00KN_power_combination_eval
# LANG: _00KM, _chord --> _00KO
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01290__00KO = (v01284__00KM**1)*(v01094__chord**1)
v01290__00KO = (v01290__00KO*_00KN_coeff).reshape((1, 40, 30))

# op _00KR_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_2 --> _00KS
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01256__00KS = np.sum(v01255__local_thrust_2, axis = (1, 2)).reshape((1,))

# op _00KV_single_tensor_sum_with_axis_eval
# LANG: _local_torque_2 --> _00KW
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01304__00KW = np.sum(v01303__local_torque_2, axis = (1, 2)).reshape((1,))

# op _00Kr_power_combination_eval
# LANG: _00Kq, _chord --> _00Ks
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01223__00Ks = (v01217__00Kq**1)*(v01094__chord**1)
v01223__00Ks = (v01223__00Ks*_00Kr_coeff).reshape((1, 40, 30))

# op _00LQ_power_combination_eval
# LANG: _00LP, _dr --> _local_energy_loss
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01320__local_energy_loss = (v01319__00LP**1)*(v01087__dr**1)
v01320__local_energy_loss = (v01320__local_energy_loss*_00LQ_coeff).reshape((1, 40, 30))

# op _00Lk_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_star --> _00Ll
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01276__00Ll = np.sum(v01275__local_thrust_star, axis = (1, 2)).reshape((1,))

# op _00MH_power_combination_eval
# LANG: C_Q --> C_P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01348_C_P = (v01342_C_Q**1)
v01348_C_P = (v01348_C_P*_00MH_coeff).reshape((1,))

# op _00MV_power_combination_eval
# LANG: C_T, J --> _00MW
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01349__00MW = (v01330_C_T**1)*(v01355_J**1)
v01349__00MW = (v01349__00MW*_00MV_coeff).reshape((1,))

# op _00N2_power_combination_eval
# LANG: C_T, _00N1 --> _00N3
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01357__00N3 = (v01330_C_T**1)*(v01359__00N1**1)
v01357__00N3 = (v01357__00N3*_00N2_coeff).reshape((1,))

# op _00O__power_combination_eval
# LANG: _00OZ --> _00P0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01410__00P0 = (v01409__00OZ**1)
v01410__00P0 = (v01410__00P0*_00O__coeff).reshape((1,))

# op _00Ox_log10_eval
# LANG: _00Ow --> _00Oy
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01396__00Oy = np.log10(v01395__00Ow)

# op _00P1_linear_combination_eval
# LANG: temperature --> _00P2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01412__00P2 = _00P1_constant+1*v01401_temperature

# op _00QF_power_combination_eval
# LANG: _00QE --> _00QG
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01468__00QG = (v01467__00QE**0.5)
v01468__00QG = (v01468__00QG*_00QF_coeff).reshape((1, 1, 1))

# op _00Qz_power_combination_eval
# LANG: _00Qw, _00Qy --> _00QA
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01463__00QA = (v01462__00Qw**1)*(v01464__00Qy**1)
v01463__00QA = (v01463__00QA*_00Qz_coeff).reshape((1, 1, 1))

# op _00_N_log10_eval
# LANG: _00_M --> _00_O
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01776__00_O = np.log10(v01775__00_M)

# op _00dp_power_combination_eval
# LANG: _00di, _00do --> _00dq
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0354__00dq = (v0353__00di**1)*(v0357__00do**-1)
v0354__00dq = (v0354__00dq*_00dp_coeff).reshape((1, 40, 100))

# op _00dt_power_combination_eval
# LANG: _00ds --> _00du
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0360__00du = (v0359__00ds**4)
v0360__00du = (v0360__00du*_00dt_coeff).reshape((1, 40, 100))

# op _00f7_power_combination_eval
# LANG: _00f6, _chord --> _00f8
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0339__00f8 = (v0333__00f6**1)*(v0210__chord**1)
v0339__00f8 = (v0339__00f8*_00f7_coeff).reshape((1, 40, 100))

# op _00fB_single_tensor_sum_with_axis_eval
# LANG: _local_torque_2 --> _00fC
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0420__00fC = np.sum(v0419__local_torque_2, axis = (1, 2)).reshape((1,))

# op _00ft_power_combination_eval
# LANG: _00fs, _chord --> _00fu
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0406__00fu = (v0400__00fs**1)*(v0210__chord**1)
v0406__00fu = (v0406__00fu*_00ft_coeff).reshape((1, 40, 100))

# op _00fx_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_2 --> _00fy
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0372__00fy = np.sum(v0371__local_thrust_2, axis = (1, 2)).reshape((1,))

# op _00g0_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_star --> _00g1
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0392__00g1 = np.sum(v0391__local_thrust_star, axis = (1, 2)).reshape((1,))

# op _00gw_power_combination_eval
# LANG: _00gv, _dr --> _local_energy_loss
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0436__local_energy_loss = (v0435__00gv**1)*(v0203__dr**1)
v0436__local_energy_loss = (v0436__local_energy_loss*_00gw_coeff).reshape((1, 40, 100))

# op _00hB_power_combination_eval
# LANG: C_T, J --> _00hC
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0465__00hC = (v0446_C_T**1)*(v0471_J**1)
v0465__00hC = (v0465__00hC*_00hB_coeff).reshape((1,))

# op _00hJ_power_combination_eval
# LANG: C_T, _00hI --> _00hK
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0473__00hK = (v0446_C_T**1)*(v0475__00hI**1)
v0473__00hK = (v0473__00hK*_00hJ_coeff).reshape((1,))

# op _00hn_power_combination_eval
# LANG: C_Q --> C_P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0464_C_P = (v0458_C_Q**1)
v0464_C_P = (v0464_C_P*_00hn_coeff).reshape((1,))

# op _00jD_power_combination_eval
# LANG: pressure --> _00jE
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0523__00jE = (v0522_pressure**1)
v0523__00jE = (v0523__00jE*_00jD_coeff).reshape((1,))

# op _00jN_power_combination_eval
# LANG: _00jM --> _00jO
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0528__00jO = (v0527__00jM**1)
v0528__00jO = (v0528__00jO*_00jN_coeff).reshape((1,))

# op _00jP_linear_combination_eval
# LANG: temperature --> _00jQ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0530__00jQ = _00jP_constant+1*v0519_temperature

# op _00jk_log10_eval
# LANG: _00jj --> _00jl
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0514__00jl = np.log10(v0513__00jj)

# op _00lm_power_combination_eval
# LANG: _00lj, _00ll --> _00ln
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0581__00ln = (v0580__00lj**1)*(v0582__00ll**1)
v0581__00ln = (v0581__00ln*_00lm_coeff).reshape((1, 1, 1))

# op _00ls_power_combination_eval
# LANG: _00lr --> _00lt
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0586__00lt = (v0585__00lr**0.5)
v0586__00lt = (v0586__00lt*_00ls_coeff).reshape((1, 1, 1))

# op _00sO_log10_eval
# LANG: _00sN --> _00sP
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0807__00sP = np.log10(v0806__00sN)

# op _00uh_power_combination_eval
# LANG: _00ue, _00ug --> _00ui
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0857__00ui = (v0856__00ue**1)*(v0858__00ug**1)
v0857__00ui = (v0857__00ui*_00uh_coeff).reshape((1, 1, 1))

# op _00un_power_combination_eval
# LANG: _00um --> _00uo
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0862__00uo = (v0861__00um**0.5)
v0862__00uo = (v0862__00uo*_00un_coeff).reshape((1, 1, 1))

# op _00w3_log10_eval
# LANG: _00w2 --> _00w4
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0909__00w4 = np.log10(v0908__00w2)

# op _00wn_indexed_passthrough_eval
# LANG: _00wm, _00wB, _00wN, _00wZ, _00xa, _00xm, _00xy --> temp_density
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0933_temp_density__temp[i_v0932__00wm__00wn_indexed_passthrough_eval] = v0932__00wm.flatten()
v0933_temp_density = v0933_temp_density__temp.copy()
v0933_temp_density__temp[i_v0935__00wB__00wn_indexed_passthrough_eval] = v0935__00wB.flatten()
v0933_temp_density = v0933_temp_density__temp.copy()
v0933_temp_density__temp[i_v0937__00wN__00wn_indexed_passthrough_eval] = v0937__00wN.flatten()
v0933_temp_density = v0933_temp_density__temp.copy()
v0933_temp_density__temp[i_v0939__00wZ__00wn_indexed_passthrough_eval] = v0939__00wZ.flatten()
v0933_temp_density = v0933_temp_density__temp.copy()
v0933_temp_density__temp[i_v0941__00xa__00wn_indexed_passthrough_eval] = v0941__00xa.flatten()
v0933_temp_density = v0933_temp_density__temp.copy()
v0933_temp_density__temp[i_v0943__00xm__00wn_indexed_passthrough_eval] = v0943__00xm.flatten()
v0933_temp_density = v0933_temp_density__temp.copy()
v0933_temp_density__temp[i_v0945__00xy__00wn_indexed_passthrough_eval] = v0945__00xy.flatten()
v0933_temp_density = v0933_temp_density__temp.copy()

# op _00ws_indexed_passthrough_eval
# LANG: _00wr, _00wF, _00wR, _00x2, _00xe, _00xq, _00xC --> temp_pressure
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0948_temp_pressure__temp[i_v0947__00wr__00ws_indexed_passthrough_eval] = v0947__00wr.flatten()
v0948_temp_pressure = v0948_temp_pressure__temp.copy()
v0948_temp_pressure__temp[i_v0950__00wF__00ws_indexed_passthrough_eval] = v0950__00wF.flatten()
v0948_temp_pressure = v0948_temp_pressure__temp.copy()
v0948_temp_pressure__temp[i_v0952__00wR__00ws_indexed_passthrough_eval] = v0952__00wR.flatten()
v0948_temp_pressure = v0948_temp_pressure__temp.copy()
v0948_temp_pressure__temp[i_v0954__00x2__00ws_indexed_passthrough_eval] = v0954__00x2.flatten()
v0948_temp_pressure = v0948_temp_pressure__temp.copy()
v0948_temp_pressure__temp[i_v0956__00xe__00ws_indexed_passthrough_eval] = v0956__00xe.flatten()
v0948_temp_pressure = v0948_temp_pressure__temp.copy()
v0948_temp_pressure__temp[i_v0958__00xq__00ws_indexed_passthrough_eval] = v0958__00xq.flatten()
v0948_temp_pressure = v0948_temp_pressure__temp.copy()
v0948_temp_pressure__temp[i_v0960__00xC__00ws_indexed_passthrough_eval] = v0960__00xC.flatten()
v0948_temp_pressure = v0948_temp_pressure__temp.copy()

# op _00xT_power_combination_eval
# LANG: _00xS --> _00xU
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0982__00xU = (v0981__00xS**1)
v0982__00xU = (v0982__00xU*_00xT_coeff).reshape((1,))

# op _00xV_linear_combination_eval
# LANG: hover_temperature --> _00xW
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0984__00xW = _00xV_constant+1*v0976_hover_temperature

# op _00xZ_power_combination_eval
# LANG: hover_temperature --> _00x_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0985__00x_ = (v0976_hover_temperature**1)
v0985__00x_ = (v0985__00x_*_00xZ_coeff).reshape((1,))

# op _00yd_power_combination_eval
# LANG: _00y4 --> p
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0920_p = (v0914__00y4**1)
v0920_p = (v0920_p*_00yd_coeff).reshape((1,))

# op _00yf_power_combination_eval
# LANG: _00y4 --> q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0921_q = (v0914__00y4**1)
v0921_q = (v0921_q*_00yf_coeff).reshape((1,))

# op _00yh_power_combination_eval
# LANG: _00y4 --> r
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0922_r = (v0914__00y4**1)
v0922_r = (v0922_r*_00yh_coeff).reshape((1,))

# op _011g_power_combination_eval
# LANG: _011d, _011f --> _011h
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01827__011h = (v01826__011d**1)*(v01828__011f**1)
v01827__011h = (v01827__011h*_011g_coeff).reshape((1, 1, 1))

# op _011m_power_combination_eval
# LANG: _011l --> _011n
# SHAPES: (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01832__011n = (v01831__011l**0.5)
v01832__011n = (v01832__011n*_011m_coeff).reshape((1, 1, 1))

# op _013W_log10_eval
# LANG: _013V --> _013X
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01907__013X = np.log10(v01906__013V)

# op _0001_power_combination_eval
# LANG: caddee_test_input --> caddee_test_output
# SHAPES: (1,) --> (1,)
# full namespace: 
v02_caddee_test_output = (v01_caddee_test_input**1)
v02_caddee_test_output = (v02_caddee_test_output*_0001_coeff).reshape((1,))

# op _001Z single_tensor_sum_no_axis_eval
# LANG: temp_density --> cruise_density
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v098_cruise_density = np.sum(v053_temp_density).reshape((1,))

# op _0020 single_tensor_sum_no_axis_eval
# LANG: temp_pressure --> cruise_pressure
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v097_cruise_pressure = np.sum(v068_temp_pressure).reshape((1,))

# op _002e_power_combination_eval
# LANG: _002b, _002d --> cruise_dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0103_cruise_dynamic_viscosity = (v0102__002b**1)*(v0104__002d**-1)
v0103_cruise_dynamic_viscosity = (v0103_cruise_dynamic_viscosity*_002e_coeff).reshape((1,))

# op _002q_power_combination_eval
# LANG: cruise_range, cruise_speed --> cruise_time
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v019_cruise_time = (v017_cruise_range**1)*(v020_cruise_speed**-1)
v019_cruise_time = (v019_cruise_time*_002q_coeff).reshape((1,))

# op _0037_power_combination_eval
# LANG: _002v --> phi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v043_phi = (v042__002v**1)
v043_phi = (v043_phi*_0037_coeff).reshape((1,))

# op _0039_power_combination_eval
# LANG: _002x --> gamma
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v044_gamma = (v026__002x**1)
v044_gamma = (v044_gamma*_0039_coeff).reshape((1,))

# op _003b_power_combination_eval
# LANG: _002z --> psi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v045_psi = (v029__002z**1)
v045_psi = (v045_psi*_003b_coeff).reshape((1,))

# op _003f_power_combination_eval
# LANG: _0035 --> x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v047_x = (v024__0035**1)
v047_x = (v047_x*_003f_coeff).reshape((1,))

# op _003h_power_combination_eval
# LANG: _0036 --> y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v048_y = (v025__0036**1)
v048_y = (v048_y*_003h_coeff).reshape((1,))

# op _003j_power_combination_eval
# LANG: _002t --> z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v049_z = (v023__002t**1)
v049_z = (v049_z*_003j_coeff).reshape((1,))

# op _004W reshape_eval
# LANG: Re --> Re_ml_input
# SHAPES: (1, 40, 100) --> (4000, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0145_Re_ml_input = v0141_Re.reshape((4000, 1))

# op _004Y reshape_eval
# LANG: mach_number --> mach_number_ml_input
# SHAPES: (1, 40, 100) --> (4000, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0146_mach_number_ml_input = v0143_mach_number.reshape((4000, 1))

# op _005G_power_combination_eval
# LANG: p --> p1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v039_p = v039_p.reshape((1, 1))
v0169_p1 = (v039_p**1)
v0169_p1 = (v0169_p1*_005G_coeff).reshape((1, 1))
v039_p = v039_p.reshape((1,))

# op _005J_power_combination_eval
# LANG: q --> q1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v040_q = v040_q.reshape((1, 1))
v0170_q1 = (v040_q**1)
v0170_q1 = (v0170_q1*_005J_coeff).reshape((1, 1))
v040_q = v040_q.reshape((1,))

# op _005M_power_combination_eval
# LANG: r --> r1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v041_r = v041_r.reshape((1, 1))
v0171_r1 = (v041_r**1)
v0171_r1 = (v0171_r1*_005M_coeff).reshape((1, 1))
v041_r = v041_r.reshape((1,))

# op _005u_transpose_eval
# LANG: _005t --> M
# SHAPES: (1, 3) --> (3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0161_M = np.transpose(v0160__005t)

# op _00AO_transpose_eval
# LANG: _00AN --> M
# SHAPES: (1, 3) --> (3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01045_M = np.transpose(v01044__00AN)

# op _00A__power_combination_eval
# LANG: p --> p1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0920_p = v0920_p.reshape((1, 1))
v01053_p1 = (v0920_p**1)
v01053_p1 = (v01053_p1*_00A__coeff).reshape((1, 1))
v0920_p = v0920_p.reshape((1,))

# op _00Af reshape_eval
# LANG: Re --> Re_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01029_Re_ml_input = v01025_Re.reshape((1200, 1))

# op _00Ah reshape_eval
# LANG: mach_number --> mach_number_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01030_mach_number_ml_input = v01027_mach_number.reshape((1200, 1))

# op _00B2_power_combination_eval
# LANG: q --> q1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0921_q = v0921_q.reshape((1, 1))
v01054_q1 = (v0921_q**1)
v01054_q1 = (v01054_q1*_00B2_coeff).reshape((1, 1))
v0921_q = v0921_q.reshape((1,))

# op _00B5_power_combination_eval
# LANG: r --> r1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0922_r = v0922_r.reshape((1, 1))
v01055_r1 = (v0922_r**1)
v01055_r1 = (v01055_r1*_00B5_coeff).reshape((1, 1))
v0922_r = v0922_r.reshape((1,))

# op _00IP_power_combination_eval
# LANG: _00IK, _00IO --> dC_T
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01242_dC_T = (v01238__00IK**1)*(v01244__00IO**-1)
v01242_dC_T = (v01242_dC_T*_00IP_coeff).reshape((1, 40, 30))

# op _00KP_power_combination_eval
# LANG: _00KO, _dr --> _local_torque_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01291__local_torque_induced = (v01290__00KO**1)*(v01087__dr**1)
v01291__local_torque_induced = (v01291__local_torque_induced*_00KP_coeff).reshape((1, 40, 30))

# op _00KT_power_combination_eval
# LANG: _00KS --> total_thrust_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01257_total_thrust_2 = (v01256__00KS**1)
v01257_total_thrust_2 = (v01257_total_thrust_2*_00KT_coeff).reshape((1,))

# op _00KX_power_combination_eval
# LANG: _00KW --> total_torque_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01305_total_torque_2 = (v01304__00KW**1)
v01305_total_torque_2 = (v01305_total_torque_2*_00KX_coeff).reshape((1,))

# op _00Kt_power_combination_eval
# LANG: _00Ks, _dr --> _local_thrust_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01224__local_thrust_induced = (v01223__00Ks**1)*(v01087__dr**1)
v01224__local_thrust_induced = (v01224__local_thrust_induced*_00Kt_coeff).reshape((1, 40, 30))

# op _00LS_single_tensor_sum_with_axis_eval
# LANG: _local_energy_loss --> total_energy_loss
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01321_total_energy_loss = np.sum(v01320__local_energy_loss, axis = (1, 2)).reshape((1,))

# op _00Lm_power_combination_eval
# LANG: _00Ll --> total_thrust_star
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01277_total_thrust_star = (v01276__00Ll**1)
v01277_total_thrust_star = (v01277_total_thrust_star*_00Lm_coeff).reshape((1,))

# op _00MX_power_combination_eval
# LANG: C_P, _00MW --> eta
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01356_eta = (v01349__00MW**1)*(v01348_C_P**-1)
v01356_eta = (v01356_eta*_00MX_coeff).reshape((1,))

# op _00N4_power_combination_eval
# LANG: C_P, _00N3 --> FOM
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01360_FOM = (v01357__00N3**1)*(v01348_C_P**-1)
v01360_FOM = (v01360_FOM*_00N4_coeff).reshape((1,))

# op _00N8_power_combination_eval
# LANG: total_torque --> Q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01236_Q = (v01235_total_torque**1)
v01236_Q = (v01236_Q*_00N8_coeff).reshape((1,))

# op _00Na_power_combination_eval
# LANG: _local_torque --> _dQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01278__dQ = (v01233__local_torque**1)
v01278__dQ = (v01278__dQ*_00Na_coeff).reshape((1, 40, 30))

# op _00Oz_power_combination_eval
# LANG: _00Oy --> rotor_disk_tonal_spl_A_weighted
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01397_rotor_disk_tonal_spl_A_weighted = (v01396__00Oy**1)
v01397_rotor_disk_tonal_spl_A_weighted = (v01397_rotor_disk_tonal_spl_A_weighted*_00Oz_coeff).reshape((1, 1))

# op _00P3_power_combination_eval
# LANG: _00P0, _00P2 --> dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01411_dynamic_viscosity = (v01410__00P0**1)*(v01412__00P2**-1)
v01411_dynamic_viscosity = (v01411_dynamic_viscosity*_00P3_coeff).reshape((1,))

# op _00QH_power_combination_eval
# LANG: _00QA, _00QG --> rel_obs_angle
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01465_rel_obs_angle = (v01463__00QA**1)*(v01468__00QG**-1)
v01465_rel_obs_angle = (v01465_rel_obs_angle*_00QH_coeff).reshape((1, 1, 1))

# op _00_P_power_combination_eval
# LANG: _00_O --> rotor_disk_broadband_spl_A_weighted
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01777_rotor_disk_broadband_spl_A_weighted = (v01776__00_O**1)
v01777_rotor_disk_broadband_spl_A_weighted = (v01777_rotor_disk_broadband_spl_A_weighted*_00_P_coeff).reshape((1, 1))

# op _00dv_power_combination_eval
# LANG: _00dq, _00du --> dC_T
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0358_dC_T = (v0354__00dq**1)*(v0360__00du**-1)
v0358_dC_T = (v0358_dC_T*_00dv_coeff).reshape((1, 40, 100))

# op _00f9_power_combination_eval
# LANG: _00f8, _dr --> _local_thrust_induced
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0340__local_thrust_induced = (v0339__00f8**1)*(v0203__dr**1)
v0340__local_thrust_induced = (v0340__local_thrust_induced*_00f9_coeff).reshape((1, 40, 100))

# op _00fD_power_combination_eval
# LANG: _00fC --> total_torque_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0421_total_torque_2 = (v0420__00fC**1)
v0421_total_torque_2 = (v0421_total_torque_2*_00fD_coeff).reshape((1,))

# op _00fv_power_combination_eval
# LANG: _00fu, _dr --> _local_torque_induced
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0407__local_torque_induced = (v0406__00fu**1)*(v0203__dr**1)
v0407__local_torque_induced = (v0407__local_torque_induced*_00fv_coeff).reshape((1, 40, 100))

# op _00fz_power_combination_eval
# LANG: _00fy --> total_thrust_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0373_total_thrust_2 = (v0372__00fy**1)
v0373_total_thrust_2 = (v0373_total_thrust_2*_00fz_coeff).reshape((1,))

# op _00g2_power_combination_eval
# LANG: _00g1 --> total_thrust_star
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0393_total_thrust_star = (v0392__00g1**1)
v0393_total_thrust_star = (v0393_total_thrust_star*_00g2_coeff).reshape((1,))

# op _00gy_single_tensor_sum_with_axis_eval
# LANG: _local_energy_loss --> total_energy_loss
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0437_total_energy_loss = np.sum(v0436__local_energy_loss, axis = (1, 2)).reshape((1,))

# op _00hD_power_combination_eval
# LANG: C_P, _00hC --> eta
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0472_eta = (v0465__00hC**1)*(v0464_C_P**-1)
v0472_eta = (v0472_eta*_00hD_coeff).reshape((1,))

# op _00hL_power_combination_eval
# LANG: C_P, _00hK --> FOM
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0476_FOM = (v0473__00hK**1)*(v0464_C_P**-1)
v0476_FOM = (v0476_FOM*_00hL_coeff).reshape((1,))

# op _00hP_power_combination_eval
# LANG: total_torque --> Q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0352_Q = (v0351_total_torque**1)
v0352_Q = (v0352_Q*_00hP_coeff).reshape((1,))

# op _00hR_power_combination_eval
# LANG: _local_torque --> _dQ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0394__dQ = (v0349__local_torque**1)
v0394__dQ = (v0394__dQ*_00hR_coeff).reshape((1, 40, 100))

# op _00jF_power_combination_eval
# LANG: temperature, _00jE --> density
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0524_density = (v0523__00jE**1)*(v0519_temperature**-1)
v0524_density = (v0524_density*_00jF_coeff).reshape((1,))

# op _00jR_power_combination_eval
# LANG: _00jO, _00jQ --> dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0529_dynamic_viscosity = (v0528__00jO**1)*(v0530__00jQ**-1)
v0529_dynamic_viscosity = (v0529_dynamic_viscosity*_00jR_coeff).reshape((1,))

# op _00jm_power_combination_eval
# LANG: _00jl --> rotor_disk_tonal_spl_A_weighted
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0515_rotor_disk_tonal_spl_A_weighted = (v0514__00jl**1)
v0515_rotor_disk_tonal_spl_A_weighted = (v0515_rotor_disk_tonal_spl_A_weighted*_00jm_coeff).reshape((1, 1))

# op _00lu_power_combination_eval
# LANG: _00ln, _00lt --> rel_obs_angle
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0583_rel_obs_angle = (v0581__00ln**1)*(v0586__00lt**-1)
v0583_rel_obs_angle = (v0583_rel_obs_angle*_00lu_coeff).reshape((1, 1, 1))

# op _00oY_bessel_eval
# LANG: _00oX --> bessel_dummy
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0670_bessel_dummy=_00oY_bessel_eval(_00oY_bessel_eval_order,v0660__00oX)

# op _00pR_print_var_eval
# LANG: _00pQ --> _00pQ_print
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
print()
print('printing ', 'v0703__00pQ (_00pQ)')
print(v0703__00pQ)
_00pQ_print = v0703__00pQ

# op _00pr_print_var_eval
# LANG: _00pq --> _00pq_print
# SHAPES: (1, 1, 3, 2, 11) --> (1, 1, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
print()
print('printing ', 'v0685__00pq (_00pq)')
print(v0685__00pq)
_00pq_print = v0685__00pq

# op _00sQ_power_combination_eval
# LANG: _00sP --> rotor_disk_broadband_spl_A_weighted
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0808_rotor_disk_broadband_spl_A_weighted = (v0807__00sP**1)
v0808_rotor_disk_broadband_spl_A_weighted = (v0808_rotor_disk_broadband_spl_A_weighted*_00sQ_coeff).reshape((1, 1))

# op _00up_power_combination_eval
# LANG: _00ui, _00uo --> rel_obs_angle
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0859_rel_obs_angle = (v0857__00ui**1)*(v0862__00uo**-1)
v0859_rel_obs_angle = (v0859_rel_obs_angle*_00up_coeff).reshape((1, 1, 1))

# op _00w5_power_combination_eval
# LANG: _00w4 --> total_spl
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0910_total_spl = (v0909__00w4**1)
v0910_total_spl = (v0910_total_spl*_00w5_coeff).reshape((1, 1))

# op _00wd_power_combination_eval
# LANG: hover_hover_time --> hover_time
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0913_hover_time = (v0911_hover_hover_time**1)
v0913_hover_time = (v0913_hover_time*_00wd_coeff).reshape((1,))

# op _00xH single_tensor_sum_no_axis_eval
# LANG: temp_density --> hover_density
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0978_hover_density = np.sum(v0933_temp_density).reshape((1,))

# op _00xJ single_tensor_sum_no_axis_eval
# LANG: temp_pressure --> hover_pressure
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0977_hover_pressure = np.sum(v0948_temp_pressure).reshape((1,))

# op _00xX_power_combination_eval
# LANG: _00xU, _00xW --> hover_dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0983_hover_dynamic_viscosity = (v0982__00xU**1)*(v0984__00xW**-1)
v0983_hover_dynamic_viscosity = (v0983_hover_dynamic_viscosity*_00xX_coeff).reshape((1,))

# op _00y0_power_combination_eval
# LANG: _00x_ --> hover_speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0986_hover_speed_of_sound = (v0985__00x_**0.5)
v0986_hover_speed_of_sound = (v0986_hover_speed_of_sound*_00y0_coeff).reshape((1,))

# op _00yj_power_combination_eval
# LANG: _00y4 --> phi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0923_phi = (v0914__00y4**1)
v0923_phi = (v0923_phi*_00yj_coeff).reshape((1,))

# op _00yl_power_combination_eval
# LANG: _00y4 --> gamma
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0924_gamma = (v0914__00y4**1)
v0924_gamma = (v0924_gamma*_00yl_coeff).reshape((1,))

# op _00yn_power_combination_eval
# LANG: _00y4 --> psi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0925_psi = (v0914__00y4**1)
v0925_psi = (v0925_psi*_00yn_coeff).reshape((1,))

# op _00yr_power_combination_eval
# LANG: _00y4 --> x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0927_x = (v0914__00y4**1)
v0927_x = (v0927_x*_00yr_coeff).reshape((1,))

# op _00yt_power_combination_eval
# LANG: _00y5 --> y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0928_y = (v0915__00y5**1)
v0928_y = (v0928_y*_00yt_coeff).reshape((1,))

# op _00yv_power_combination_eval
# LANG: _00y6 --> z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0929_z = (v0916__00y6**1)
v0929_z = (v0929_z*_00yv_coeff).reshape((1,))

# op _011o_power_combination_eval
# LANG: _011h, _011n --> rel_obs_angle
# SHAPES: (1, 1, 1), (1, 1, 1) --> (1, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01829_rel_obs_angle = (v01827__011h**1)*(v01832__011n**-1)
v01829_rel_obs_angle = (v01829_rel_obs_angle*_011o_coeff).reshape((1, 1, 1))

# op _013Y_power_combination_eval
# LANG: _013X --> total_spl
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01908_total_spl = (v01907__013X**1)
v01908_total_spl = (v01908_total_spl*_013Y_coeff).reshape((1, 1))