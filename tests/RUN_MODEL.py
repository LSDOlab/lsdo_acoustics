

# RUN_MODEL

# system evaluation block

# op _0009_power_combination_eval
# LANG: system_representation_geometry --> design_geometry
# SHAPES: (16250, 3) --> (16250, 3)
# full namespace: system_representation.system_configurations_model
v05_design_geometry = (v04_system_representation_geometry**1)
v05_design_geometry = (v05_design_geometry*_0009_coeff).reshape((16250, 3))

# op _000g_sparsematmat_eval
# LANG: design_geometry --> _000h
# SHAPES: (16250, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v07__000h = _000g_sparsematmat_eval_mat@v05_design_geometry

# op _000k_sparsematmat_eval
# LANG: design_geometry --> _000l
# SHAPES: (16250, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v09__000l = _000k_sparsematmat_eval_mat@v05_design_geometry

# op _000i reshape_eval
# LANG: _000h --> rotor_disk_in_plane_1
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v08_rotor_disk_in_plane_1 = v07__000h.reshape((1, 3))

# op _000m reshape_eval
# LANG: _000l --> rotor_disk_in_plane_2
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v010_rotor_disk_in_plane_2 = v09__000l.reshape((1, 3))

# op _003k_power_combination_eval
# LANG: cruise_pitch_angle --> theta
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v048_theta = (v017_cruise_pitch_angle**1)
v048_theta = (v048_theta*_003k_coeff).reshape((1,))

# op _004j cross_product_eval
# LANG: rotor_disk_in_plane_1, rotor_disk_in_plane_2 --> _004k
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v0130__004k = np.cross(v010_rotor_disk_in_plane_2, v08_rotor_disk_in_plane_1, axisa = 0, axisb = 0, axisc = 0)
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _003F_sin_eval
# LANG: theta --> _003G
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v048_theta = v048_theta.reshape((1, 1))
v0111__003G = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _003J_linear_combination_eval
# LANG: theta --> _003K
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v048_theta = v048_theta.reshape((1, 1))
v0113__003K = _003J_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _003L_linear_combination_eval
# LANG: theta --> _003M
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v048_theta = v048_theta.reshape((1, 1))
v0115__003M = _003L_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _003P_sin_eval
# LANG: theta --> _003Q
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v048_theta = v048_theta.reshape((1, 1))
v0116__003Q = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _003T_cos_eval
# LANG: theta --> _003U
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v048_theta = v048_theta.reshape((1, 1))
v0118__003U = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _004l pnorm_eval
# LANG: _004k --> _004m
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0132__004m = np.linalg.norm(v0130__004k.flatten(), ord=2)

# op _000S_power_combination_eval
# LANG: cruise_altitude --> _000T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v083__000T = (v052_cruise_altitude**6)
v083__000T = (v083__000T*_000S_coeff).reshape((1,))

# op _0014_power_combination_eval
# LANG: cruise_altitude --> _0015
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v086__0015 = (v052_cruise_altitude**5)
v086__0015 = (v086__0015*_0014_coeff).reshape((1,))

# op _001E_power_combination_eval
# LANG: cruise_altitude --> _001F
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v092__001F = (v052_cruise_altitude**2)
v092__001F = (v092__001F*_001E_coeff).reshape((1,))

# op _001Q_power_combination_eval
# LANG: cruise_altitude --> _001R
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v094__001R = (v052_cruise_altitude**1)
v094__001R = (v094__001R*_001Q_coeff).reshape((1,))

# op _001g_power_combination_eval
# LANG: cruise_altitude --> _001h
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v088__001h = (v052_cruise_altitude**4)
v088__001h = (v088__001h*_001g_coeff).reshape((1,))

# op _001s_power_combination_eval
# LANG: cruise_altitude --> _001t
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v090__001t = (v052_cruise_altitude**3)
v090__001t = (v090__001t*_001s_coeff).reshape((1,))

# op _0021_power_combination_eval
# LANG: cruise_altitude --> _0022
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v096__0022 = (v052_cruise_altitude**0)
v096__0022 = (v096__0022*_0021_coeff).reshape((1,))

# op _003C_cos_eval
# LANG: theta --> _003D
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v048_theta = v048_theta.reshape((1, 1))
v0109__003D = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _003H_power_combination_eval
# LANG: _003G --> _003I
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0112__003I = (v0111__003G**1)
v0112__003I = (v0112__003I*_003H_coeff).reshape((1, 1))

# op _003N_power_combination_eval
# LANG: _003K, _003M --> _003O
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0114__003O = (v0113__003K**1)*(v0115__003M**-1)
v0114__003O = (v0114__003O*_003N_coeff).reshape((1, 1))

# op _003R_power_combination_eval
# LANG: _003Q --> _003S
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0117__003S = (v0116__003Q**1)
v0117__003S = (v0117__003S*_003R_coeff).reshape((1, 1))

# op _003V_power_combination_eval
# LANG: _003U --> _003W
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0119__003W = (v0118__003U**1)
v0119__003W = (v0119__003W*_003V_coeff).reshape((1, 1))

# op _004n expand_scalar_eval
# LANG: _004m --> _004o
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0133__004o = np.empty((3,))
v0133__004o.fill(v0132__004m.item())

# op _000U_power_combination_eval
# LANG: _000T --> _000V
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v084__000V = (v083__000T**1)
v084__000V = (v084__000V*_000U_coeff).reshape((1,))

# op _0016_power_combination_eval
# LANG: _0015 --> _0017
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v087__0017 = (v086__0015**1)
v087__0017 = (v087__0017*_0016_coeff).reshape((1,))

# op _001G_power_combination_eval
# LANG: _001F --> _001H
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v093__001H = (v092__001F**1)
v093__001H = (v093__001H*_001G_coeff).reshape((1,))

# op _001S_power_combination_eval
# LANG: _001R --> _001T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v095__001T = (v094__001R**1)
v095__001T = (v095__001T*_001S_coeff).reshape((1,))

# op _001i_power_combination_eval
# LANG: _001h --> _001j
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v089__001j = (v088__001h**1)
v089__001j = (v089__001j*_001i_coeff).reshape((1,))

# op _001u_power_combination_eval
# LANG: _001t --> _001v
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v091__001v = (v090__001t**1)
v091__001v = (v091__001v*_001u_coeff).reshape((1,))

# op _0023_power_combination_eval
# LANG: _0022 --> _0024
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v097__0024 = (v096__0022**1)
v097__0024 = (v097__0024*_0023_coeff).reshape((1,))

# op _003E_indexed_passthrough_eval
# LANG: _003D, _003I, _003O, _003S, _003W --> rotation_matrix
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0110_rotation_matrix__temp[i_v0109__003D__003E_indexed_passthrough_eval] = v0109__003D.flatten()
v0110_rotation_matrix = v0110_rotation_matrix__temp.copy()
v0110_rotation_matrix__temp[i_v0112__003I__003E_indexed_passthrough_eval] = v0112__003I.flatten()
v0110_rotation_matrix = v0110_rotation_matrix__temp.copy()
v0110_rotation_matrix__temp[i_v0114__003O__003E_indexed_passthrough_eval] = v0114__003O.flatten()
v0110_rotation_matrix = v0110_rotation_matrix__temp.copy()
v0110_rotation_matrix__temp[i_v0117__003S__003E_indexed_passthrough_eval] = v0117__003S.flatten()
v0110_rotation_matrix = v0110_rotation_matrix__temp.copy()
v0110_rotation_matrix__temp[i_v0119__003W__003E_indexed_passthrough_eval] = v0119__003W.flatten()
v0110_rotation_matrix = v0110_rotation_matrix__temp.copy()

# op _004p_power_combination_eval
# LANG: _004k, _004o --> _004q
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0131__004q = (v0130__004k**1)*(v0133__004o**-1)
v0131__004q = (v0131__004q*_004p_coeff).reshape((3,))

# op _000W_indexed_passthrough_eval
# LANG: _000V, _0017, _001j, _001v, _001H, _001T, _0024 --> temp_temperature
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v085_temp_temperature__temp[i_v084__000V__000W_indexed_passthrough_eval] = v084__000V.flatten()
v085_temp_temperature = v085_temp_temperature__temp.copy()
v085_temp_temperature__temp[i_v087__0017__000W_indexed_passthrough_eval] = v087__0017.flatten()
v085_temp_temperature = v085_temp_temperature__temp.copy()
v085_temp_temperature__temp[i_v089__001j__000W_indexed_passthrough_eval] = v089__001j.flatten()
v085_temp_temperature = v085_temp_temperature__temp.copy()
v085_temp_temperature__temp[i_v091__001v__000W_indexed_passthrough_eval] = v091__001v.flatten()
v085_temp_temperature = v085_temp_temperature__temp.copy()
v085_temp_temperature__temp[i_v093__001H__000W_indexed_passthrough_eval] = v093__001H.flatten()
v085_temp_temperature = v085_temp_temperature__temp.copy()
v085_temp_temperature__temp[i_v095__001T__000W_indexed_passthrough_eval] = v095__001T.flatten()
v085_temp_temperature = v085_temp_temperature__temp.copy()
v085_temp_temperature__temp[i_v097__0024__000W_indexed_passthrough_eval] = v097__0024.flatten()
v085_temp_temperature = v085_temp_temperature__temp.copy()

# op _004r_matvec_eval
# LANG: rotation_matrix, _004q --> _004s
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0129__004s = v0110_rotation_matrix@v0131__004q

# op _0029 single_tensor_sum_no_axis_eval
# LANG: temp_temperature --> cruise_temperature
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v098_cruise_temperature = np.sum(v085_temp_temperature).reshape((1,))

# op _002z_decompose_eval
# LANG: cruise_observer_location --> _002A, _003c, _003d
# SHAPES: (3,) --> (1,), (1,), (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v025__002A = ((v018_cruise_observer_location.flatten())[src_indices__002A__002z]).reshape((1,))
v026__003c = ((v018_cruise_observer_location.flatten())[src_indices__003c__002z]).reshape((1,))
v027__003d = ((v018_cruise_observer_location.flatten())[src_indices__003d__002z]).reshape((1,))

# op _004t expand_array_eval
# LANG: _004s --> thrust_vector
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0134_thrust_vector = np.einsum('b,a->ab', v0129__004s.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

# op _002D_power_combination_eval
# LANG: _002A --> _002E
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v028__002E = (v025__002A**1)
v028__002E = (v028__002E*_002D_coeff).reshape((1,))

# op _002n_power_combination_eval
# LANG: cruise_temperature --> _002o
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0107__002o = (v098_cruise_temperature**1)
v0107__002o = (v0107__002o*_002n_coeff).reshape((1,))

# op _0065_decompose_eval
# LANG: thrust_vector --> _0066
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0176__0066 = ((v0134_thrust_vector.flatten())[src_indices__0066__0065]).reshape((1, 3))

# op _002F_power_combination_eval
# LANG: _002A --> _002G
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v031__002G = (v025__002A**1)
v031__002G = (v031__002G*_002F_coeff).reshape((1,))

# op _002H_power_combination_eval
# LANG: _002A --> _002I
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v033__002I = (v025__002A**1)
v033__002I = (v033__002I*_002H_coeff).reshape((1,))

# op _002J_linear_combination_eval
# LANG: cruise_pitch_angle, _002E --> _002K
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v024__002K = _002J_constant+1*v017_cruise_pitch_angle+-1*v028__002E

# op _002p_power_combination_eval
# LANG: _002o --> cruise_speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0108_cruise_speed_of_sound = (v0107__002o**0.5)
v0108_cruise_speed_of_sound = (v0108_cruise_speed_of_sound*_002p_coeff).reshape((1,))

# op _0069_tensor_dot_product_eval
# LANG: projection_vector, _0066 --> _006a
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0183__006a = np.sum(v0165_projection_vector * v0176__0066, axis=1)

# op _002L_linear_combination_eval
# LANG: _002G, _002I --> _002M
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v032__002M = _002L_constant+1*v031__002G+1*v033__002I

# op _002N_cos_eval
# LANG: _002K --> _002O
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v029__002O = np.cos(v024__002K)

# op _002v_power_combination_eval
# LANG: cruise_mach_number, cruise_speed_of_sound --> cruise_speed
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v022_cruise_speed = (v0108_cruise_speed_of_sound**1)*(v020_cruise_mach_number**1)
v022_cruise_speed = (v022_cruise_speed*_002v_coeff).reshape((1,))

# op _006b expand_scalar_eval
# LANG: _006a --> _006c
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0184__006c = np.empty((1, 3))
v0184__006c.fill(v0183__006a.item())

# op _002P_power_combination_eval
# LANG: cruise_speed, _002O --> _002Q
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v023__002Q = (v022_cruise_speed**1)*(v029__002O**1)
v023__002Q = (v023__002Q*_002P_coeff).reshape((1,))

# op _002R_cos_eval
# LANG: _002M --> _002S
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v034__002S = np.cos(v032__002M)

# op _002Z_sin_eval
# LANG: _002K --> _002_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v038__002_ = np.sin(v024__002K)

# op _006d_power_combination_eval
# LANG: _0066, _006c --> _006e
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0185__006e = (v0184__006c**1)*(v0176__0066**1)
v0185__006e = (v0185__006e*_006d_coeff).reshape((1, 3))

# op _002T_power_combination_eval
# LANG: _002Q, _002S --> u
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v030_u = (v023__002Q**1)*(v034__002S**1)
v030_u = (v030_u*_002T_coeff).reshape((1,))

# op _002V_sin_eval
# LANG: _002M --> _002W
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v036__002W = np.sin(v032__002M)

# op _0030_power_combination_eval
# LANG: cruise_speed, _002_ --> _0031
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v037__0031 = (v022_cruise_speed**1)*(v038__002_**1)
v037__0031 = (v037__0031*_0030_coeff).reshape((1,))

# op _0032_cos_eval
# LANG: _002M --> _0033
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v040__0033 = np.cos(v032__002M)

# op _006f_linear_combination_eval
# LANG: projection_vector, _006e --> _006g
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0182__006g = _006f_constant+1*v0165_projection_vector+-1*v0185__006e

# op _002X_power_combination_eval
# LANG: cruise_speed, _002W --> v
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v035_v = (v022_cruise_speed**1)*(v036__002W**1)
v035_v = (v035_v*_002X_coeff).reshape((1,))

# op _0034_power_combination_eval
# LANG: _0031, _0033 --> w
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v039_w = (v037__0031**1)*(v040__0033**1)
v039_w = (v039_w*_0034_coeff).reshape((1,))

# op _005H_power_combination_eval
# LANG: u --> _005I
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v030_u = v030_u.reshape((1, 1))
v0166__005I = (v030_u**1)
v0166__005I = (v0166__005I*_005H_coeff).reshape((1, 1))
v030_u = v030_u.reshape((1,))

# op _006h pnorm_eval
# LANG: _006g --> _006i
# SHAPES: (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0187__006i = np.linalg.norm(v0182__006g.flatten(), ord=2)

# op _006j expand_scalar_eval
# LANG: _006i --> _006k
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0188__006k = np.empty((1, 3))
v0188__006k.fill(v0187__006i.item())

# op _006u_decompose_eval
# LANG: _005I --> _006v
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0167__006v = ((v0166__005I.flatten())[src_indices__006v__006u]).reshape((1, 1))

# op _006x_decompose_eval
# LANG: v --> _006y
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v035_v = v035_v.reshape((1, 1))
v0169__006y = ((v035_v.flatten())[src_indices__006y__006x]).reshape((1, 1))
v035_v = v035_v.reshape((1,))

# op _006z_decompose_eval
# LANG: w --> _006A
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v039_w = v039_w.reshape((1, 1))
v0170__006A = ((v039_w.flatten())[src_indices__006A__006z]).reshape((1, 1))
v039_w = v039_w.reshape((1,))

# op _006l_power_combination_eval
# LANG: _006g, _006k --> in_plane_ey
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0186_in_plane_ey = (v0182__006g**1)*(v0188__006k**-1)
v0186_in_plane_ey = (v0186_in_plane_ey*_006l_coeff).reshape((1, 3))

# op _006w_indexed_passthrough_eval
# LANG: _006v, _006y, _006A --> velocity_vector
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0168_velocity_vector__temp[i_v0167__006v__006w_indexed_passthrough_eval] = v0167__006v.flatten()
v0168_velocity_vector = v0168_velocity_vector__temp.copy()
v0168_velocity_vector__temp[i_v0169__006y__006w_indexed_passthrough_eval] = v0169__006y.flatten()
v0168_velocity_vector = v0168_velocity_vector__temp.copy()
v0168_velocity_vector__temp[i_v0170__006A__006w_indexed_passthrough_eval] = v0170__006A.flatten()
v0168_velocity_vector = v0168_velocity_vector__temp.copy()

# op _006B_decompose_eval
# LANG: velocity_vector --> _006C
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0174__006C = ((v0168_velocity_vector.flatten())[src_indices__006C__006B]).reshape((1, 3))

# op _006n cross_product_eval
# LANG: _0066, in_plane_ey --> in_plane_ex
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0181_in_plane_ex = np.cross(v0176__0066, v0186_in_plane_ey, axisa = 1, axisb = 1, axisc = 1)

# op _0067_power_combination_eval
# LANG: _0066 --> _0068
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0177__0068 = (v0176__0066**1)
v0177__0068 = (v0177__0068*_0067_coeff).reshape((1, 3))

# op _006D_tensor_dot_product_eval
# LANG: _006C, in_plane_ex --> _006E
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0180__006E = np.sum(v0174__006C * v0181_in_plane_ex, axis=1)

# op _004f pnorm_eval
# LANG: rotor_disk_in_plane_1 --> _004g
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v0127__004g = np.linalg.norm(v08_rotor_disk_in_plane_1.flatten(), ord=2)
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _006F_tensor_dot_product_eval
# LANG: _006C, in_plane_ey --> _006G
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0191__006G = np.sum(v0174__006C * v0186_in_plane_ey, axis=1)

# op _006H_tensor_dot_product_eval
# LANG: _006C, _0068 --> _006I
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0175__006I = np.sum(v0174__006C * v0177__0068, axis=1)

# op _006M_linear_combination_eval
# LANG: _006E --> _006N
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0189__006N = _006M_constant+-1*v0180__006E

# op _004h_power_combination_eval
# LANG: _004g --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0128_propeller_radius = (v0127__004g**1)
v0128_propeller_radius = (v0128_propeller_radius*_004h_coeff).reshape((1,))

# op _006J expand_scalar_eval
# LANG: _006I --> _006K
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0178__006K = np.empty((1, 40, 30, 1))
v0178__006K.fill(v0175__006I.item())

# op _006O expand_scalar_eval
# LANG: _006N --> _006P
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0190__006P = np.empty((1, 40, 30, 1))
v0190__006P.fill(v0189__006N.item())

# op _006Q expand_scalar_eval
# LANG: _006G --> _006R
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0192__006R = np.empty((1, 40, 30, 1))
v0192__006R.fill(v0191__006G.item())

# op _005W_power_combination_eval
# LANG: propeller_radius --> hub_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0193_hub_radius = (v0128_propeller_radius**1)
v0193_hub_radius = (v0193_hub_radius*_005W_coeff).reshape((1,))

# op _006L_indexed_passthrough_eval
# LANG: _006K, _006P, _006R --> inflow_velocity
# SHAPES: (1, 40, 30, 1), (1, 40, 30, 1), (1, 40, 30, 1) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0179_inflow_velocity__temp[i_v0178__006K__006L_indexed_passthrough_eval] = v0178__006K.flatten()
v0179_inflow_velocity = v0179_inflow_velocity__temp.copy()
v0179_inflow_velocity__temp[i_v0190__006P__006L_indexed_passthrough_eval] = v0190__006P.flatten()
v0179_inflow_velocity = v0179_inflow_velocity__temp.copy()
v0179_inflow_velocity__temp[i_v0192__006R__006L_indexed_passthrough_eval] = v0192__006R.flatten()
v0179_inflow_velocity = v0179_inflow_velocity__temp.copy()

# op _006p_decompose_eval
# LANG: rpm --> _006q
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0197__006q = ((v0164_rpm.flatten())[src_indices__006q__006p]).reshape((1, 1))

# op _008f_power_combination_eval
# LANG: z --> _008g
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0237__008g = (v0236_z**1)
v0237__008g = (v0237__008g*_008f_coeff).reshape((1, 1))

# op _006r_power_combination_eval
# LANG: _006q --> _006s
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0198__006s = (v0197__006q**1)
v0198__006s = (v0198__006s*_006r_coeff).reshape((1, 1))

# op _0075 expand_scalar_eval
# LANG: hub_radius --> _hub_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0203__hub_radius = np.empty((1, 40, 30))
v0203__hub_radius.fill(v0193_hub_radius.item())

# op _0077 expand_scalar_eval
# LANG: propeller_radius --> _rotor_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0204__rotor_radius = np.empty((1, 40, 30))
v0204__rotor_radius.fill(v0128_propeller_radius.item())

# op _007f expand_array_eval
# LANG: y_dir --> _y_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0208__y_dir = np.einsum('ad,bc->abcd', v0201_y_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _007h expand_array_eval
# LANG: z_dir --> _z_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0209__z_dir = np.einsum('ad,bc->abcd', v0202_z_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _007j_power_combination_eval
# LANG: inflow_velocity --> _inflow_velocity
# SHAPES: (1, 40, 30, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0210__inflow_velocity = (v0179_inflow_velocity**1)
v0210__inflow_velocity = (v0210__inflow_velocity*_007j_coeff).reshape((1, 40, 30, 3))

# op _008h_linear_combination_eval
# LANG: _008g --> _008i
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0238__008i = _008h_constant+-1*v0237__008g

# op _006t_indexed_passthrough_eval
# LANG: _006s --> rotational_speed
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0199_rotational_speed__temp[i_v0198__006s__006t_indexed_passthrough_eval] = v0198__006s.flatten()
v0199_rotational_speed = v0199_rotational_speed__temp.copy()

# op _007D_linear_combination_eval
# LANG: _hub_radius, _rotor_radius --> _007E
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0218__007E = _007D_constant+1*v0204__rotor_radius+-1*v0203__hub_radius

# op _007T_tensor_dot_product_eval
# LANG: _y_dir, _inflow_velocity --> _in_plane_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0225__in_plane_inflow_velocity = np.sum(v0210__inflow_velocity * v0208__y_dir, axis=3)

# op _007V_tensor_dot_product_eval
# LANG: _z_dir, _inflow_velocity --> inflow_z
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0226_inflow_z = np.sum(v0210__inflow_velocity * v0209__z_dir, axis=3)

# op _008j_power_combination_eval
# LANG: _008i --> _008k
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0239__008k = (v0238__008i**1)
v0239__008k = (v0239__008k*_008j_coeff).reshape((1, 1))

# op _007F_power_combination_eval
# LANG: _007E, _normalized_radius --> _007G
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0219__007G = (v0218__007E**1)*(v0215__normalized_radius**1)
v0219__007G = (v0219__007G*_007F_coeff).reshape((1, 40, 30))

# op _007X_power_combination_eval
# LANG: inflow_z --> _007Y
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0227__007Y = (v0226_inflow_z**1)
v0227__007Y = (v0227__007Y*_007X_coeff).reshape((1, 40, 30))

# op _007Z_cos_eval
# LANG: _theta --> _007_
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0229__007_ = np.cos(v0214__theta)

# op _007b expand_scalar_eval
# LANG: rotational_speed --> _rotational_speed
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0199_rotational_speed = v0199_rotational_speed.reshape((1,))
v0206__rotational_speed = np.empty((1, 40, 30))
v0206__rotational_speed.fill(v0199_rotational_speed.item())
v0199_rotational_speed = v0199_rotational_speed.reshape((1, 1))

# op _0082_power_combination_eval
# LANG: _in_plane_inflow_velocity --> _0083
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0231__0083 = (v0225__in_plane_inflow_velocity**1)
v0231__0083 = (v0231__0083*_0082_coeff).reshape((1, 40, 30))

# op _0084_sin_eval
# LANG: _theta --> _0085
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0233__0085 = np.sin(v0214__theta)

# op _008l_linear_combination_eval
# LANG: _008k --> temperature
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0240_temperature = _008l_constant+1*v0239__008k

# op _000s_sparsematmat_eval
# LANG: design_geometry --> _000t
# SHAPES: (16250, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v013__000t = _000s_sparsematmat_eval_mat@v05_design_geometry

# op _007B_power_combination_eval
# LANG: _rotational_speed --> _angular_speed
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0216__angular_speed = (v0206__rotational_speed**1)
v0216__angular_speed = (v0216__angular_speed*_007B_coeff).reshape((1, 40, 30))

# op _007H_linear_combination_eval
# LANG: _007G, _hub_radius --> _radius
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0217__radius = _007H_constant+1*v0203__hub_radius+1*v0219__007G

# op _0080_power_combination_eval
# LANG: _007Y, _007_ --> _0081
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0228__0081 = (v0227__007Y**1)*(v0229__007_**1)
v0228__0081 = (v0228__0081*_0080_coeff).reshape((1, 40, 30))

# op _0086_power_combination_eval
# LANG: _0083, _0085 --> _0087
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0232__0087 = (v0231__0083**1)*(v0233__0085**1)
v0232__0087 = (v0232__0087*_0086_coeff).reshape((1, 40, 30))

# op _008n_power_combination_eval
# LANG: temperature --> _008o
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0241__008o = (v0240_temperature**1)
v0241__008o = (v0241__008o*_008n_coeff).reshape((1, 1))

# op _000u reshape_eval
# LANG: _000t --> rotor_blade_chord_length
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v014_rotor_blade_chord_length = v013__000t.reshape((40, 3))

# op _000w_sparsematmat_eval
# LANG: design_geometry --> _000x
# SHAPES: (16250, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v015__000x = _000w_sparsematmat_eval_mat@v05_design_geometry

# op _007d expand_array_eval
# LANG: x_dir --> _x_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0207__x_dir = np.einsum('ad,bc->abcd', v0200_x_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _0088_linear_combination_eval
# LANG: _0081, _0087 --> _0089
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0230__0089 = _0088_constant+1*v0228__0081+1*v0232__0087

# op _008a_power_combination_eval
# LANG: _angular_speed, _radius --> _008b
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0235__008b = (v0217__radius**1)*(v0216__angular_speed**1)
v0235__008b = (v0235__008b*_008a_coeff).reshape((1, 40, 30))

# op _008p_power_combination_eval
# LANG: _008o --> _008q
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0242__008q = (v0241__008o**5.258643795229161)
v0242__008q = (v0242__008q*_008p_coeff).reshape((1, 1))

# op _000y reshape_eval
# LANG: _000x --> rotor_blade_twist
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v016_rotor_blade_twist = v015__000x.reshape((40, 3))

# op _003Y pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _003Z
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0120__003Z = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _007R_tensor_dot_product_eval
# LANG: _x_dir, _inflow_velocity --> _axial_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0224__axial_inflow_velocity = np.sum(v0210__inflow_velocity * v0207__x_dir, axis=3)

# op _008c_linear_combination_eval
# LANG: _0089, _008b --> _tangential_inflow_velocity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0234__tangential_inflow_velocity = _008c_constant+1*v0230__0089+1*v0235__008b

# op _008r_power_combination_eval
# LANG: _008q --> pressure
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0243_pressure = (v0242__008q**1)
v0243_pressure = (v0243_pressure*_008r_coeff).reshape((1, 1))

# op _008x_power_combination_eval
# LANG: temperature --> _008y
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0246__008y = (v0240_temperature**1)
v0246__008y = (v0246__008y*_008x_coeff).reshape((1, 1))

# op _003_ reshape_eval
# LANG: _003Z --> chord_profile
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0121_chord_profile = v0120__003Z.reshape((40, 1))

# op _0042_single_tensor_sum_with_axis_eval
# LANG: rotor_blade_twist --> _0043
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0122__0043 = np.sum(v016_rotor_blade_twist, axis = (1,)).reshape((40,))

# op _004E_power_combination_eval
# LANG: _axial_inflow_velocity --> _004F
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0138__004F = (v0224__axial_inflow_velocity**2)
v0138__004F = (v0138__004F*_004E_coeff).reshape((1, 40, 30))

# op _004G_power_combination_eval
# LANG: _tangential_inflow_velocity --> _004H
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0140__004H = (v0234__tangential_inflow_velocity**2)
v0140__004H = (v0140__004H*_004G_coeff).reshape((1, 40, 30))

# op _008t_power_combination_eval
# LANG: pressure --> _008u
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0244__008u = (v0243_pressure**1)
v0244__008u = (v0244__008u*_008t_coeff).reshape((1, 1))

# op _008z_power_combination_eval
# LANG: _008y --> _008A
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0247__008A = (v0246__008y**1.5)
v0247__008A = (v0247__008A*_008z_coeff).reshape((1, 1))

# op _0044 reshape_eval
# LANG: _0043 --> _0045
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0123__0045 = v0122__0043.reshape((40, 1))

# op _004I_linear_combination_eval
# LANG: _004F, _004H --> _004J
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0139__004J = _004I_constant+1*v0138__004F+1*v0140__004H

# op _007n expand_array_eval
# LANG: chord_profile --> _chord
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0121_chord_profile = v0121_chord_profile.reshape((40,))
v0212__chord = np.einsum('b,ac->abc', v0121_chord_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v0121_chord_profile = v0121_chord_profile.reshape((40, 1))

# op _008B_power_combination_eval
# LANG: _008A --> _008C
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0248__008C = (v0247__008A**1)
v0248__008C = (v0248__008C*_008B_coeff).reshape((1, 1))

# op _008v_power_combination_eval
# LANG: temperature, _008u --> density
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0245_density = (v0244__008u**1)*(v0240_temperature**-1)
v0245_density = (v0245_density*_008v_coeff).reshape((1, 1))

# op _0046_power_combination_eval
# LANG: chord_profile, _0045 --> _0047
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0124__0047 = (v0123__0045**1)*(v0121_chord_profile**-1)
v0124__0047 = (v0124__0047*_0046_coeff).reshape((40, 1))

# op _004K_power_combination_eval
# LANG: _004J --> _004L
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0141__004L = (v0139__004J**0.5)
v0141__004L = (v0141__004L*_004K_coeff).reshape((1, 40, 30))

# op _004N expand_scalar_eval
# LANG: density --> _004O
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0245_density = v0245_density.reshape((1,))
v0136__004O = np.empty((1, 40, 30))
v0136__004O.fill(v0245_density.item())
v0245_density = v0245_density.reshape((1, 1))

# op _007J_power_combination_eval
# LANG: _chord --> _007K
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0220__007K = (v0212__chord**1)
v0220__007K = (v0220__007K*_007J_coeff).reshape((1, 40, 30))

# op _008D_power_combination_eval
# LANG: _008C --> _008E
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0249__008E = (v0248__008C**1)
v0249__008E = (v0249__008E*_008D_coeff).reshape((1, 1))

# op _008F_linear_combination_eval
# LANG: temperature --> _008G
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0251__008G = _008F_constant+1*v0240_temperature

# op _0048_arcsin_eval
# LANG: _0047 --> _0049
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0125__0049 = np.arcsin(v0124__0047)

# op _004V_power_combination_eval
# LANG: _004O, _004L --> _004W
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0137__004W = (v0136__004O**1)*(v0141__004L**1)
v0137__004W = (v0137__004W*_004V_coeff).reshape((1, 40, 30))

# op _007L_power_combination_eval
# LANG: _007K --> _007M
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0221__007M = (v0220__007K**1)
v0221__007M = (v0221__007M*_007L_coeff).reshape((1, 40, 30))

# op _008H_power_combination_eval
# LANG: _008E, _008G --> dynamic_viscosity
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0250_dynamic_viscosity = (v0249__008E**1)*(v0251__008G**-1)
v0250_dynamic_viscosity = (v0250_dynamic_viscosity*_008H_coeff).reshape((1, 1))

# op _004Q expand_scalar_eval
# LANG: dynamic_viscosity --> _004R
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0250_dynamic_viscosity = v0250_dynamic_viscosity.reshape((1,))
v0144__004R = np.empty((1, 40, 30))
v0144__004R.fill(v0250_dynamic_viscosity.item())
v0250_dynamic_viscosity = v0250_dynamic_viscosity.reshape((1, 1))

# op _004X_power_combination_eval
# LANG: _004W, _chord --> _004Y
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0142__004Y = (v0137__004W**1)*(v0212__chord**1)
v0142__004Y = (v0142__004Y*_004X_coeff).reshape((1, 40, 30))

# op _004a_linear_combination_eval
# LANG: _0049 --> twist_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0126_twist_profile = _004a_constant+1*v0125__0049

# op _007N_power_combination_eval
# LANG: _007M --> _007O
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0222__007O = (v0221__007M**1)
v0222__007O = (v0222__007O*_007N_coeff).reshape((1, 40, 30))

# op _004Z_power_combination_eval
# LANG: _004Y, _004R --> Re
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0143_Re = (v0142__004Y**1)*(v0144__004R**-1)
v0143_Re = (v0143_Re*_004Z_coeff).reshape((1, 40, 30))

# op _007P_power_combination_eval
# LANG: _radius, _007O --> _blade_solidity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0223__blade_solidity = (v0222__007O**1)*(v0217__radius**-1)
v0223__blade_solidity = (v0223__blade_solidity*_007P_coeff).reshape((1, 40, 30))

# op _007l expand_array_eval
# LANG: twist_profile --> _pitch
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0126_twist_profile = v0126_twist_profile.reshape((40,))
v0211__pitch = np.einsum('b,ac->abc', v0126_twist_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v0126_twist_profile = v0126_twist_profile.reshape((40, 1))

# op _00az_bracketed_implict_eval
# LANG: Re, _hub_radius, _rotor_radius, _pitch, _chord, _radius, _blade_solidity, _axial_inflow_velocity, _tangential_inflow_velocity --> phi_distribution, alpha_distribution, Cl, Cd
# SHAPES: (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30) --> (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.phi_bracketed_search_group
_00az_bracketed.set_guess(initial_guess_v0254_phi_distribution)
_00az_bracketed_out = _00az_bracketed.solve(v0223__blade_solidity, v0224__axial_inflow_velocity, v0234__tangential_inflow_velocity, v0217__radius, v0204__rotor_radius, v0203__hub_radius, v0212__chord, v0211__pitch, v0143_Re)
v0254_phi_distribution = _00az_bracketed_out[0]
v0255_alpha_distribution = _00az_bracketed_out[1]
v0256_Cl = _00az_bracketed_out[2]
v0257_Cd = _00az_bracketed_out[3]

# op _00aI_linear_combination_eval
# LANG: _rotor_radius, _radius --> _00aJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0258__00aJ = _00aI_constant+1*v0204__rotor_radius+-1*v0217__radius

# op _00aS_linear_combination_eval
# LANG: _hub_radius, _radius --> _00aT
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0268__00aT = _00aS_constant+1*v0217__radius+-1*v0203__hub_radius

# op _00aK_power_combination_eval
# LANG: _00aJ --> _00aL
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0259__00aL = (v0258__00aJ**1)
v0259__00aL = (v0259__00aL*_00aK_coeff).reshape((1, 40, 30))

# op _00aU_power_combination_eval
# LANG: _00aT --> _00aV
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0269__00aV = (v0268__00aT**1)
v0269__00aV = (v0269__00aV*_00aU_coeff).reshape((1, 40, 30))

# op _00aM_power_combination_eval
# LANG: _00aL, _radius --> _00aN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0260__00aN = (v0259__00aL**1)*(v0217__radius**-1)
v0260__00aN = (v0260__00aN*_00aM_coeff).reshape((1, 40, 30))

# op _00aO_sin_eval
# LANG: phi_distribution --> _00aP
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0262__00aP = np.sin(v0254_phi_distribution)

# op _00aW_power_combination_eval
# LANG: _00aV, _hub_radius --> _00aX
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0270__00aX = (v0269__00aV**1)*(v0203__hub_radius**-1)
v0270__00aX = (v0270__00aX*_00aW_coeff).reshape((1, 40, 30))

# op _00aY_sin_eval
# LANG: phi_distribution --> _00aZ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0272__00aZ = np.sin(v0254_phi_distribution)

# op _00aQ_power_combination_eval
# LANG: _00aN, _00aP --> _00aR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0261__00aR = (v0260__00aN**1)*(v0262__00aP**-1)
v0261__00aR = (v0261__00aR*_00aQ_coeff).reshape((1, 40, 30))

# op _00a__power_combination_eval
# LANG: _00aX, _00aZ --> _00b0
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0271__00b0 = (v0270__00aX**1)*(v0272__00aZ**-1)
v0271__00b0 = (v0271__00b0*_00a__coeff).reshape((1, 40, 30))

# op _00b1_linear_combination_eval
# LANG: _00aR --> _00b2
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0263__00b2 = _00b1_constant+-1*v0261__00aR

# op _00b9_linear_combination_eval
# LANG: _00b0 --> _00ba
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0273__00ba = _00b9_constant+-1*v0271__00b0

# op _00b3 exp_eval
# LANG: _00b2 --> _00b4
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0264__00b4 = np.exp(v0263__00b2)

# op _00bb exp_eval
# LANG: _00ba --> _00bc
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0274__00bc = np.exp(v0273__00ba)

# op _00b5 arccos_eval
# LANG: _00b4 --> _00b6
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0265__00b6 = np.arccos(v0264__00b4)

# op _00bd arccos_eval
# LANG: _00bc --> _00be
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0275__00be = np.arccos(v0274__00bc)

# op _00b7_power_combination_eval
# LANG: _00b6 --> _00b8
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0266__00b8 = (v0265__00b6**1)
v0266__00b8 = (v0266__00b8*_00b7_coeff).reshape((1, 40, 30))

# op _00bO_sin_eval
# LANG: phi_distribution --> _00bP
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0291__00bP = np.sin(v0254_phi_distribution)

# op _00bS_cos_eval
# LANG: phi_distribution --> _00bT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0294__00bT = np.cos(v0254_phi_distribution)

# op _00bf_power_combination_eval
# LANG: _00be --> _00bg
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0276__00bg = (v0275__00be**1)
v0276__00bg = (v0276__00bg*_00bf_coeff).reshape((1, 40, 30))

# op _00bE_cos_eval
# LANG: phi_distribution --> _00bF
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0298__00bF = np.cos(v0254_phi_distribution)

# op _00bI_sin_eval
# LANG: phi_distribution --> _00bJ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0301__00bJ = np.sin(v0254_phi_distribution)

# op _00bQ_power_combination_eval
# LANG: _00bP, Cl --> _00bR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0290__00bR = (v0256_Cl**1)*(v0291__00bP**1)
v0290__00bR = (v0290__00bR*_00bQ_coeff).reshape((1, 40, 30))

# op _00bU_power_combination_eval
# LANG: _00bT, Cd --> _00bV
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0293__00bV = (v0257_Cd**1)*(v0294__00bT**1)
v0293__00bV = (v0293__00bV*_00bU_coeff).reshape((1, 40, 30))

# op _00bh_power_combination_eval
# LANG: _00b8, _00bg --> prandtl_loss_factor
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0267_prandtl_loss_factor = (v0266__00b8**1)*(v0276__00bg**1)
v0267_prandtl_loss_factor = (v0267_prandtl_loss_factor*_00bh_coeff).reshape((1, 40, 30))

# op _00cZ_power_combination_eval
# LANG: phi_distribution --> _00c_
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0317__00c_ = (v0254_phi_distribution**1)
v0317__00c_ = (v0317__00c_*_00cZ_coeff).reshape((1, 40, 30))

# op _00bG_power_combination_eval
# LANG: _00bF, Cl --> _00bH
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0297__00bH = (v0256_Cl**1)*(v0298__00bF**1)
v0297__00bH = (v0297__00bH*_00bG_coeff).reshape((1, 40, 30))

# op _00bK_power_combination_eval
# LANG: _00bJ, Cd --> _00bL
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0300__00bL = (v0257_Cd**1)*(v0301__00bJ**1)
v0300__00bL = (v0300__00bL*_00bK_coeff).reshape((1, 40, 30))

# op _00bW_linear_combination_eval
# LANG: _00bR, _00bV --> _00bX
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0292__00bX = _00bW_constant+1*v0290__00bR+1*v0293__00bV

# op _00cB_sin_eval
# LANG: phi_distribution --> _00cC
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0306__00cC = np.sin(v0254_phi_distribution)

# op _00cR_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00cS
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0311__00cS = (v0234__tangential_inflow_velocity**1)
v0311__00cS = (v0311__00cS*_00cR_coeff).reshape((1, 40, 30))

# op _00cX_power_combination_eval
# LANG: prandtl_loss_factor --> _00cY
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0315__00cY = (v0267_prandtl_loss_factor**1)
v0315__00cY = (v0315__00cY*_00cX_coeff).reshape((1, 40, 30))

# op _00cz_power_combination_eval
# LANG: prandtl_loss_factor --> _00cA
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0304__00cA = (v0267_prandtl_loss_factor**1)
v0304__00cA = (v0304__00cA*_00cz_coeff).reshape((1, 40, 30))

# op _00d0_sin_eval
# LANG: _00c_ --> _00d1
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0318__00d1 = np.sin(v0317__00c_)

# op _00kR expand_scalar_eval
# LANG: Vx --> _00kS
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0555__00kS = np.empty((1, 1))
v0555__00kS.fill(v030_u.item())

# op _00kU expand_scalar_eval
# LANG: Vy --> _00kV
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0557__00kV = np.empty((1, 1))
v0557__00kV.fill(v035_v.item())

# op _00kW expand_scalar_eval
# LANG: Vz --> _00kX
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0558__00kX = np.empty((1, 1))
v0558__00kX.fill(v039_w.item())

# op _000o_sparsematmat_eval
# LANG: design_geometry --> _000p
# SHAPES: (16250, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v011__000p = _000o_sparsematmat_eval_mat@v05_design_geometry

# op _00bM_linear_combination_eval
# LANG: _00bH, _00bL --> _00bN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0299__00bN = _00bM_constant+1*v0297__00bH+-1*v0300__00bL

# op _00cD_power_combination_eval
# LANG: _00cA, _00cC --> _00cE
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0305__00cE = (v0304__00cA**1)*(v0306__00cC**1)
v0305__00cE = (v0305__00cE*_00cD_coeff).reshape((1, 40, 30))

# op _00cF_cos_eval
# LANG: phi_distribution --> _00cG
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0308__00cG = np.cos(v0254_phi_distribution)

# op _00cT_power_combination_eval
# LANG: _00cS, _blade_solidity --> _00cU
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0312__00cU = (v0311__00cS**1)*(v0223__blade_solidity**1)
v0312__00cU = (v0312__00cU*_00cT_coeff).reshape((1, 40, 30))

# op _00cf_power_combination_eval
# LANG: prandtl_loss_factor --> _00cg
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0283__00cg = (v0267_prandtl_loss_factor**1)
v0283__00cg = (v0283__00cg*_00cf_coeff).reshape((1, 40, 30))

# op _00ch_sin_eval
# LANG: phi_distribution --> _00ci
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0285__00ci = np.sin(v0254_phi_distribution)

# op _00d2_power_combination_eval
# LANG: _00cY, _00d1 --> _00d3
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0316__00d3 = (v0315__00cY**1)*(v0318__00d1**1)
v0316__00d3 = (v0316__00d3*_00d2_coeff).reshape((1, 40, 30))

# op _00d4_power_combination_eval
# LANG: _00bX, _blade_solidity --> _00d5
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0320__00d5 = (v0223__blade_solidity**1)*(v0292__00bX**1)
v0320__00d5 = (v0320__00d5*_00d4_coeff).reshape((1, 40, 30))

# op _00kT_indexed_passthrough_eval
# LANG: _00kS, _00kV, _00kX --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0556_V_aircraft__temp[i_v0555__00kS__00kT_indexed_passthrough_eval] = v0555__00kS.flatten()
v0556_V_aircraft = v0556_V_aircraft__temp.copy()
v0556_V_aircraft__temp[i_v0557__00kV__00kT_indexed_passthrough_eval] = v0557__00kV.flatten()
v0556_V_aircraft = v0556_V_aircraft__temp.copy()
v0556_V_aircraft__temp[i_v0558__00kX__00kT_indexed_passthrough_eval] = v0558__00kX.flatten()
v0556_V_aircraft = v0556_V_aircraft__temp.copy()

# op _000q reshape_eval
# LANG: _000p --> rotor_disk_origin
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v012_rotor_disk_origin = v011__000p.reshape((1, 3))

# op _00c5_power_combination_eval
# LANG: prandtl_loss_factor --> _00c6
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0277__00c6 = (v0267_prandtl_loss_factor**1)
v0277__00c6 = (v0277__00c6*_00c5_coeff).reshape((1, 40, 30))

# op _00c9_sin_eval
# LANG: phi_distribution --> _00ca
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0280__00ca = np.sin(v0254_phi_distribution)

# op _00cH_power_combination_eval
# LANG: _00cE, _00cG --> _00cI
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0307__00cI = (v0305__00cE**1)*(v0308__00cG**1)
v0307__00cI = (v0307__00cI*_00cH_coeff).reshape((1, 40, 30))

# op _00cJ_power_combination_eval
# LANG: _00bX, _blade_solidity --> _00cK
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0310__00cK = (v0223__blade_solidity**1)*(v0292__00bX**1)
v0310__00cK = (v0310__00cK*_00cJ_coeff).reshape((1, 40, 30))

# op _00cV_power_combination_eval
# LANG: _00bX, _00cU --> _00cW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0313__00cW = (v0312__00cU**1)*(v0292__00bX**1)
v0313__00cW = (v0313__00cW*_00cV_coeff).reshape((1, 40, 30))

# op _00cj_power_combination_eval
# LANG: _00cg, _00ci --> _00ck
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0284__00ck = (v0283__00cg**1)*(v0285__00ci**1)
v0284__00ck = (v0284__00ck*_00cj_coeff).reshape((1, 40, 30))

# op _00cl_cos_eval
# LANG: phi_distribution --> _00cm
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0287__00cm = np.cos(v0254_phi_distribution)

# op _00cv_power_combination_eval
# LANG: _00bN, _blade_solidity --> _00cw
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0296__00cw = (v0223__blade_solidity**1)*(v0299__00bN**1)
v0296__00cw = (v0296__00cw*_00cv_coeff).reshape((1, 40, 30))

# op _00d6_linear_combination_eval
# LANG: _00d3, _00d5 --> _00d7
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0319__00d7 = _00d6_constant+1*v0316__00d3+1*v0320__00d5

# op _00kY expand_array_eval
# LANG: V_aircraft --> _00kZ
# SHAPES: (1, 3) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0565__00kZ = np.einsum('ab,c->abc', v0556_V_aircraft.reshape((1, 3)) ,np.ones((4,))).reshape((1, 3, 4))

# op _00l3 expand_array_eval
# LANG: time_vectors --> _00l4
# SHAPES: (4,) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0571__00l4 = np.einsum('c,ab->abc', v0570_time_vectors.reshape((4,)) ,np.ones((1, 3))).reshape((1, 3, 4))

# op _00c7_power_combination_eval
# LANG: _00c6, _tangential_inflow_velocity --> _00c8
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0278__00c8 = (v0277__00c6**1)*(v0234__tangential_inflow_velocity**1)
v0278__00c8 = (v0278__00c8*_00c7_coeff).reshape((1, 40, 30))

# op _00cL_linear_combination_eval
# LANG: _00cI, _00cK --> _00cM
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0309__00cM = _00cL_constant+1*v0307__00cI+1*v0310__00cK

# op _00cb_power_combination_eval
# LANG: _00ca --> _00cc
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0281__00cc = (v0280__00ca**2)
v0281__00cc = (v0281__00cc*_00cb_coeff).reshape((1, 40, 30))

# op _00cn_power_combination_eval
# LANG: _00ck, _00cm --> _00co
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0286__00co = (v0284__00ck**1)*(v0287__00cm**1)
v0286__00co = (v0286__00co*_00cn_coeff).reshape((1, 40, 30))

# op _00cp_power_combination_eval
# LANG: _00bX, _blade_solidity --> _00cq
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0289__00cq = (v0223__blade_solidity**1)*(v0292__00bX**1)
v0289__00cq = (v0289__00cq*_00cp_coeff).reshape((1, 40, 30))

# op _00cx_power_combination_eval
# LANG: _00cw, _tangential_inflow_velocity --> _00cy
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0302__00cy = (v0296__00cw**1)*(v0234__tangential_inflow_velocity**1)
v0302__00cy = (v0302__00cy*_00cx_coeff).reshape((1, 40, 30))

# op _00d8_power_combination_eval
# LANG: _00cW, _00d7 --> _ut
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0314__ut = (v0313__00cW**1)*(v0319__00d7**-1)
v0314__ut = (v0314__ut*_00d8_coeff).reshape((1, 40, 30))

# op _00ib_power_combination_eval
# LANG: rotor_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v0479_origin = (v012_rotor_disk_origin**1)
v0479_origin = (v0479_origin*_00ib_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _00l0 expand_array_eval
# LANG: aircraft_location --> _00l1
# SHAPES: (3, 4) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0560__00l1 = np.einsum('bc,a->abc', v0559_aircraft_location.reshape((3, 4)) ,np.ones((1,))).reshape((1, 3, 4))

# op _00l7_decompose_eval
# LANG: _00kZ --> _00l8, _00lg, _00ln
# SHAPES: (1, 3, 4) --> (1, 1, 4), (1, 1, 4), (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0566__00l8 = ((v0565__00kZ.flatten())[src_indices__00l8__00l7]).reshape((1, 1, 4))
v0567__00lg = ((v0565__00kZ.flatten())[src_indices__00lg__00l7]).reshape((1, 1, 4))
v0568__00ln = ((v0565__00kZ.flatten())[src_indices__00ln__00l7]).reshape((1, 1, 4))

# op _00l9_decompose_eval
# LANG: _00l4 --> _00la, _00lh, _00lo
# SHAPES: (1, 3, 4) --> (1, 1, 4), (1, 1, 4), (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0572__00la = ((v0571__00l4.flatten())[src_indices__00la__00l9]).reshape((1, 1, 4))
v0573__00lh = ((v0571__00l4.flatten())[src_indices__00lh__00l9]).reshape((1, 1, 4))
v0574__00lo = ((v0571__00l4.flatten())[src_indices__00lo__00l9]).reshape((1, 1, 4))

# op _00by expand_scalar_eval
# LANG: density --> _00bz
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0245_density = v0245_density.reshape((1,))
v0323__00bz = np.empty((1, 40, 30))
v0323__00bz.fill(v0245_density.item())
v0245_density = v0245_density.reshape((1, 1))

# op _00cN_power_combination_eval
# LANG: _00cy, _00cM --> _00cO
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0303__00cO = (v0302__00cy**1)*(v0309__00cM**-1)
v0303__00cO = (v0303__00cO*_00cN_coeff).reshape((1, 40, 30))

# op _00cd_power_combination_eval
# LANG: _00c8, _00cc --> _00ce
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0279__00ce = (v0278__00c8**1)*(v0281__00cc**1)
v0279__00ce = (v0279__00ce*_00cd_coeff).reshape((1, 40, 30))

# op _00cr_linear_combination_eval
# LANG: _00co, _00cq --> _00cs
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0288__00cs = _00cr_constant+1*v0286__00co+1*v0289__00cq

# op _00da_power_combination_eval
# LANG: _radius --> _00db
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0321__00db = (v0217__radius**1)
v0321__00db = (v0321__00db*_00da_coeff).reshape((1, 40, 30))

# op _00eJ_power_combination_eval
# LANG: _ut --> _00eK
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0383__00eK = (v0314__ut**1)
v0383__00eK = (v0383__00eK*_00eJ_coeff).reshape((1, 40, 30))

# op _00l5_decompose_eval
# LANG: _00l1 --> _00l6, _00lf, _00lm
# SHAPES: (1, 3, 4) --> (1, 1, 4), (1, 1, 4), (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0561__00l6 = ((v0560__00l1.flatten())[src_indices__00l6__00l5]).reshape((1, 1, 4))
v0562__00lf = ((v0560__00l1.flatten())[src_indices__00lf__00l5]).reshape((1, 1, 4))
v0563__00lm = ((v0560__00l1.flatten())[src_indices__00lm__00l5]).reshape((1, 1, 4))

# op _00lA expand_array_eval
# LANG: origin --> _00lB
# SHAPES: (3,) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0583__00lB = np.einsum('b,ac->abc', v0479_origin.reshape((3,)) ,np.ones((1, 4))).reshape((1, 3, 4))

# op _00lb_power_combination_eval
# LANG: _00l8, _00la --> _00lc
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0569__00lc = (v0566__00l8**1)*(v0572__00la**1)
v0569__00lc = (v0569__00lc*_00lb_coeff).reshape((1, 1, 4))

# op _00li_power_combination_eval
# LANG: _00lg, _00lh --> _00lj
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0576__00lj = (v0567__00lg**1)*(v0573__00lh**1)
v0576__00lj = (v0576__00lj*_00li_coeff).reshape((1, 1, 4))

# op _005Y_power_combination_eval
# LANG: propeller_radius --> _005Z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0195__005Z = (v0128_propeller_radius**1)
v0195__005Z = (v0195__005Z*_005Y_coeff).reshape((1,))

# op _00cP_linear_combination_eval
# LANG: _00cO, _axial_inflow_velocity --> _ux_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0295__ux_2 = _00cP_constant+1*v0224__axial_inflow_velocity+1*v0303__00cO

# op _00ct_power_combination_eval
# LANG: _00ce, _00cs --> _ux
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0282__ux = (v0279__00ce**1)*(v0288__00cs**-1)
v0282__ux = (v0282__ux*_00ct_coeff).reshape((1, 40, 30))

# op _00dc_power_combination_eval
# LANG: _00db, _00bz --> _00dd
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0322__00dd = (v0321__00db**1)*(v0323__00bz**1)
v0322__00dd = (v0322__00dd*_00dc_coeff).reshape((1, 40, 30))

# op _00eB_power_combination_eval
# LANG: Cd --> _00eC
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0376__00eC = (v0257_Cd**1)
v0376__00eC = (v0376__00eC*_00eB_coeff).reshape((1, 40, 30))

# op _00eL_linear_combination_eval
# LANG: _00eK, _tangential_inflow_velocity --> _00eM
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0382__00eM = _00eL_constant+1*v0234__tangential_inflow_velocity+-1*v0383__00eK

# op _00lC_decompose_eval
# LANG: _00lB --> _00lD, _00lI, _00lN
# SHAPES: (1, 3, 4) --> (1, 1, 4), (1, 1, 4), (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0584__00lD = ((v0583__00lB.flatten())[src_indices__00lD__00lC]).reshape((1, 1, 4))
v0585__00lI = ((v0583__00lB.flatten())[src_indices__00lI__00lC]).reshape((1, 1, 4))
v0586__00lN = ((v0583__00lB.flatten())[src_indices__00lN__00lC]).reshape((1, 1, 4))

# op _00ld_linear_combination_eval
# LANG: _00l6, _00lc --> aircraft_x_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0564_aircraft_x_pos = _00ld_constant+1*v0561__00l6+1*v0569__00lc

# op _00lk_linear_combination_eval
# LANG: _00lf, _00lj --> aircraft_y_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0575_aircraft_y_pos = _00lk_constant+1*v0562__00lf+1*v0576__00lj

# op _00lp_power_combination_eval
# LANG: _00ln, _00lo --> _00lq
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0578__00lq = (v0568__00ln**1)*(v0574__00lo**1)
v0578__00lq = (v0578__00lq*_00lp_coeff).reshape((1, 1, 4))

# op _005__linear_combination_eval
# LANG: _005Z, propeller_radius --> _0060
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0194__0060 = _005__constant+1*v0128_propeller_radius+-1*v0195__005Z

# op _00de_power_combination_eval
# LANG: _ux, _00dd --> _00df
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0324__00df = (v0322__00dd**1)*(v0282__ux**1)
v0324__00df = (v0324__00df*_00de_coeff).reshape((1, 40, 30))

# op _00dg_linear_combination_eval
# LANG: _ux, _axial_inflow_velocity --> _00dh
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0326__00dh = _00dg_constant+1*v0282__ux+-1*v0224__axial_inflow_velocity

# op _00eD_power_combination_eval
# LANG: _00eC --> _00eE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0377__00eE = (v0376__00eC**1)
v0377__00eE = (v0377__00eE*_00eD_coeff).reshape((1, 40, 30))

# op _00eH_power_combination_eval
# LANG: _ux_2 --> _00eI
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0380__00eI = (v0295__ux_2**2)
v0380__00eI = (v0380__00eI*_00eH_coeff).reshape((1, 40, 30))

# op _00eN_power_combination_eval
# LANG: _00eM --> _00eO
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0384__00eO = (v0382__00eM**2)
v0384__00eO = (v0384__00eO*_00eN_coeff).reshape((1, 40, 30))

# op _00lE_linear_combination_eval
# LANG: aircraft_x_pos, _00lD --> _00lF
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0582__00lF = _00lE_constant+1*v0564_aircraft_x_pos+1*v0584__00lD

# op _00lJ_linear_combination_eval
# LANG: aircraft_y_pos, _00lI --> _00lK
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0590__00lK = _00lJ_constant+1*v0575_aircraft_y_pos+1*v0585__00lI

# op _00lr_linear_combination_eval
# LANG: _00lm, _00lq --> aircraft_z_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0577_aircraft_z_pos = _00lr_constant+1*v0563__00lm+1*v0578__00lq

# op _00lt expand_array_eval
# LANG: init_obs_x_loc --> _00lu
# SHAPES: (4,) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0580__00lu = np.einsum('c,ab->abc', v0579_init_obs_x_loc.reshape((4,)) ,np.ones((1, 1))).reshape((1, 1, 4))

# op _00lv expand_array_eval
# LANG: init_obs_y_loc --> _00lw
# SHAPES: (4,) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0588__00lw = np.einsum('c,ab->abc', v0587_init_obs_y_loc.reshape((4,)) ,np.ones((1, 1))).reshape((1, 1, 4))

# op _0061_power_combination_eval
# LANG: _0060 --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0196_dr = (v0194__0060**1)
v0196_dr = (v0196_dr*_0061_coeff).reshape((1,))

# op _00di_power_combination_eval
# LANG: _00df, _00dh --> _00dj
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0325__00dj = (v0324__00df**1)*(v0326__00dh**1)
v0325__00dj = (v0325__00dj*_00di_coeff).reshape((1, 40, 30))

# op _00eF_power_combination_eval
# LANG: _00bz, _00eE --> _00eG
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0378__00eG = (v0377__00eE**1)*(v0323__00bz**1)
v0378__00eG = (v0378__00eG*_00eF_coeff).reshape((1, 40, 30))

# op _00eP_linear_combination_eval
# LANG: _00eI, _00eO --> _00eQ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0381__00eQ = _00eP_constant+1*v0380__00eI+1*v0384__00eO

# op _00kc_power_combination_eval
# LANG: altitude --> _00kd
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0538__00kd = (v052_cruise_altitude**1)
v0538__00kd = (v0538__00kd*_00kc_coeff).reshape((1,))

# op _00lG_linear_combination_eval
# LANG: _00lu, _00lF --> rel_obs_x_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0581_rel_obs_x_pos = _00lG_constant+1*v0580__00lu+-1*v0582__00lF

# op _00lL_linear_combination_eval
# LANG: _00lw, _00lK --> rel_obs_y_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0589_rel_obs_y_pos = _00lL_constant+1*v0588__00lw+-1*v0590__00lK

# op _00lO_linear_combination_eval
# LANG: aircraft_z_pos, _00lN --> _00lP
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0594__00lP = _00lO_constant+1*v0577_aircraft_z_pos+1*v0586__00lN

# op _00lx expand_array_eval
# LANG: init_obs_z_loc --> _00ly
# SHAPES: (4,) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0592__00ly = np.einsum('c,ab->abc', v0591_init_obs_z_loc.reshape((4,)) ,np.ones((1, 1))).reshape((1, 1, 4))

# op _0079 expand_scalar_eval
# LANG: dr --> _dr
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0205__dr = np.empty((1, 40, 30))
v0205__dr.fill(v0196_dr.item())

# op _00dk_power_combination_eval
# LANG: _00dj, prandtl_loss_factor --> _00dl
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0327__00dl = (v0325__00dj**1)*(v0267_prandtl_loss_factor**1)
v0327__00dl = (v0327__00dl*_00dk_coeff).reshape((1, 40, 30))

# op _00eR_power_combination_eval
# LANG: _00eG, _00eQ --> _00eS
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0379__00eS = (v0378__00eG**1)*(v0381__00eQ**1)
v0379__00eS = (v0379__00eS*_00eR_coeff).reshape((1, 40, 30))

# op _00ke_linear_combination_eval
# LANG: _00kd --> _00kf
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0539__00kf = _00ke_constant+-1*v0538__00kd

# op _00lQ_linear_combination_eval
# LANG: _00ly, _00lP --> rel_obs_z_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0593_rel_obs_z_pos = _00lQ_constant+1*v0592__00ly+-1*v0594__00lP

# op _00lU_power_combination_eval
# LANG: rel_obs_x_pos --> _00lV
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0596__00lV = (v0581_rel_obs_x_pos**2)
v0596__00lV = (v0596__00lV*_00lU_coeff).reshape((1, 1, 4))

# op _00lW_power_combination_eval
# LANG: rel_obs_y_pos --> _00lX
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0598__00lX = (v0589_rel_obs_y_pos**2)
v0598__00lX = (v0598__00lX*_00lW_coeff).reshape((1, 1, 4))

# op _00dm_power_combination_eval
# LANG: _00dl, _dr --> _local_thrust
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0328__local_thrust = (v0327__00dl**1)*(v0205__dr**1)
v0328__local_thrust = (v0328__local_thrust*_00dm_coeff).reshape((1, 40, 30))

# op _00eT_power_combination_eval
# LANG: _00eS, _chord --> _00eU
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0385__00eU = (v0379__00eS**1)*(v0212__chord**1)
v0385__00eU = (v0385__00eU*_00eT_coeff).reshape((1, 40, 30))

# op _00kg_power_combination_eval
# LANG: _00kf --> _00kh
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0540__00kh = (v0539__00kf**1)
v0540__00kh = (v0540__00kh*_00kg_coeff).reshape((1,))

# op _00lY_linear_combination_eval
# LANG: _00lV, _00lX --> _00lZ
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0597__00lZ = _00lY_constant+1*v0596__00lV+1*v0598__00lX

# op _00l__power_combination_eval
# LANG: rel_obs_z_pos --> _00m0
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0600__00m0 = (v0593_rel_obs_z_pos**2)
v0600__00m0 = (v0600__00m0*_00l__coeff).reshape((1, 1, 4))

# op _00os expand_scalar_eval
# LANG: Vx --> _00ot
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0656__00ot = np.empty((1, 4))
v0656__00ot.fill(v030_u.item())

# op _00ov expand_scalar_eval
# LANG: Vy --> _00ow
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0659__00ow = np.empty((1, 4))
v0659__00ow.fill(v035_v.item())

# op _00oy expand_scalar_eval
# LANG: Vz --> _00oz
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0661__00oz = np.empty((1, 4))
v0661__00oz.fill(v039_w.item())

# op _00eV_power_combination_eval
# LANG: _00eU, _dr --> _dD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0386__dD = (v0385__00eU**1)*(v0205__dr**1)
v0386__dD = (v0386__dD*_00eV_coeff).reshape((1, 40, 30))

# op _00hU_power_combination_eval
# LANG: _local_thrust --> _dT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0329__dT = (v0328__local_thrust**1)
v0329__dT = (v0329__dT*_00hU_coeff).reshape((1, 40, 30))

# op _00ki_linear_combination_eval
# LANG: _00kh --> temperature
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0541_temperature = _00ki_constant+1*v0540__00kh

# op _00m1_linear_combination_eval
# LANG: _00lZ, _00m0 --> _00m2
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0599__00m2 = _00m1_constant+1*v0597__00lZ+1*v0600__00m0

# op _00oC reshape_eval
# LANG: _00ot --> _00oD
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0657__00oD = v0656__00ot.reshape((1, 1, 4))

# op _00oF reshape_eval
# LANG: _00ow --> _00oG
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0660__00oG = v0659__00ow.reshape((1, 1, 4))

# op _00oH reshape_eval
# LANG: _00oz --> _00oI
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0662__00oI = v0661__00oz.reshape((1, 1, 4))

# op _00i8_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00i9
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v0480__00i9 = (v08_rotor_disk_in_plane_1**1)
v0480__00i9 = (v0480__00i9*_00i8_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _00ie_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _00if
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v0495__00if = (v010_rotor_disk_in_plane_2**1)
v0495__00if = (v0495__00if*_00ie_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _00kG_power_combination_eval
# LANG: temperature --> _00kH
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0553__00kH = (v0541_temperature**1)
v0553__00kH = (v0553__00kH*_00kG_coeff).reshape((1,))

# op _00lT_indexed_passthrough_eval
# LANG: rel_obs_x_pos, rel_obs_y_pos, rel_obs_z_pos --> rel_obs_position
# SHAPES: (1, 1, 4), (1, 1, 4), (1, 1, 4) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0595_rel_obs_position__temp[i_v0581_rel_obs_x_pos__00lT_indexed_passthrough_eval] = v0581_rel_obs_x_pos.flatten()
v0595_rel_obs_position = v0595_rel_obs_position__temp.copy()
v0595_rel_obs_position__temp[i_v0589_rel_obs_y_pos__00lT_indexed_passthrough_eval] = v0589_rel_obs_y_pos.flatten()
v0595_rel_obs_position = v0595_rel_obs_position__temp.copy()
v0595_rel_obs_position__temp[i_v0593_rel_obs_z_pos__00lT_indexed_passthrough_eval] = v0593_rel_obs_z_pos.flatten()
v0595_rel_obs_position = v0595_rel_obs_position__temp.copy()

# op _00m3_power_combination_eval
# LANG: _00m2 --> rel_obs_dist
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0601_rel_obs_dist = (v0599__00m2**0.5)
v0601_rel_obs_dist = (v0601_rel_obs_dist*_00m3_coeff).reshape((1, 1, 4))

# op _00mL expand_array_eval
# LANG: _dD --> _00mM
# SHAPES: (1, 40, 30) --> (1, 2, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0620__00mM = np.einsum('acd,b->abcd', v0386__dD.reshape((1, 40, 30)) ,np.ones((2,))).reshape((1, 2, 40, 30))

# op _00mO expand_array_eval
# LANG: _dT --> _00mP
# SHAPES: (1, 40, 30) --> (1, 2, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0622__00mP = np.einsum('acd,b->abcd', v0329__dT.reshape((1, 40, 30)) ,np.ones((2,))).reshape((1, 2, 40, 30))

# op _00o7 reshape_eval
# LANG: rpm --> _00o8
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0667__00o8 = v0164_rpm.reshape((1,))

# op _00oE_indexed_passthrough_eval
# LANG: _00oD, _00oG, _00oI --> aircraft_vel
# SHAPES: (1, 1, 4), (1, 1, 4), (1, 1, 4) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0658_aircraft_vel__temp[i_v0657__00oD__00oE_indexed_passthrough_eval] = v0657__00oD.flatten()
v0658_aircraft_vel = v0658_aircraft_vel__temp.copy()
v0658_aircraft_vel__temp[i_v0660__00oG__00oE_indexed_passthrough_eval] = v0660__00oG.flatten()
v0658_aircraft_vel = v0658_aircraft_vel__temp.copy()
v0658_aircraft_vel__temp[i_v0662__00oI__00oE_indexed_passthrough_eval] = v0662__00oI.flatten()
v0658_aircraft_vel = v0658_aircraft_vel__temp.copy()

# op _00iH cross_product_eval
# LANG: _00i9, _00if --> _00iI
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0496__00iI = np.cross(v0495__00if, v0480__00i9, axisa = 0, axisb = 0, axisc = 0)

# op _00kI_power_combination_eval
# LANG: _00kH --> speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0554_speed_of_sound = (v0553__00kH**0.5)
v0554_speed_of_sound = (v0554_speed_of_sound*_00kI_coeff).reshape((1,))

# op _00mQ_single_tensor_sum_with_axis_eval
# LANG: _00mM --> aaa
# SHAPES: (1, 2, 40, 30) --> (1, 2, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0621_aaa = np.sum(v0620__00mM, axis = (2,)).reshape((1, 2, 30))

# op _00mS_single_tensor_sum_with_axis_eval
# LANG: _00mP --> bbb
# SHAPES: (1, 2, 40, 30) --> (1, 2, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0623_bbb = np.sum(v0622__00mP, axis = (2,)).reshape((1, 2, 30))

# op _00mZ_sin_eval
# LANG: n_theta_prod --> _00m_
# SHAPES: (11, 30) --> (11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0633__00m_ = np.sin(v0626_n_theta_prod)

# op _00o9_power_combination_eval
# LANG: _00o8 --> _00oa
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0668__00oa = (v0667__00o8**1)
v0668__00oa = (v0668__00oa*_00o9_coeff).reshape((1,))

# op _00oJ_tensor_dot_product_eval
# LANG: aircraft_vel, rel_obs_position --> _00oK
# SHAPES: (1, 3, 4), (1, 3, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0681__00oK = np.sum(v0658_aircraft_vel * v0595_rel_obs_position, axis=1)

# op _00op reshape_eval
# LANG: rel_obs_dist --> _00oq
# SHAPES: (1, 1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0679__00oq = v0601_rel_obs_dist.reshape((1, 4))

# op _00iD_cos_eval
# LANG: theta --> _00iE
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v048_theta = v048_theta.reshape((1, 1))
v0492__00iE = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00iJ pnorm_eval
# LANG: _00iI --> _00iK
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0498__00iK = np.linalg.norm(v0496__00iI.flatten(), ord=2)

# op _00im_linear_combination_eval
# LANG: theta --> _00in
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v048_theta = v048_theta.reshape((1, 1))
v0483__00in = _00im_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _00io_linear_combination_eval
# LANG: theta --> _00ip
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v048_theta = v048_theta.reshape((1, 1))
v0485__00ip = _00io_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _00iv_sin_eval
# LANG: theta --> _00iw
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v048_theta = v048_theta.reshape((1, 1))
v0488__00iw = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00iz_sin_eval
# LANG: theta --> _00iA
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v048_theta = v048_theta.reshape((1, 1))
v0490__00iA = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00mV_cos_eval
# LANG: n_theta_prod --> _00mW
# SHAPES: (11, 30) --> (11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0627__00mW = np.cos(v0626_n_theta_prod)

# op _00n0 expand_array_eval
# LANG: _00m_ --> _00n1
# SHAPES: (11, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0634__00n1 = np.einsum('cd,ab->abcd', v0633__00m_.reshape((11, 30)) ,np.ones((1, 2))).reshape((1, 2, 11, 30))

# op _00na expand_array_eval
# LANG: bbb --> _00nb
# SHAPES: (1, 2, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0631__00nb = np.einsum('abd,c->abcd', v0623_bbb.reshape((1, 2, 30)) ,np.ones((11,))).reshape((1, 2, 11, 30))

# op _00ng expand_array_eval
# LANG: aaa --> _00nh
# SHAPES: (1, 2, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0636__00nh = np.einsum('abd,c->abcd', v0621_aaa.reshape((1, 2, 30)) ,np.ones((11,))).reshape((1, 2, 11, 30))

# op _00oL_power_combination_eval
# LANG: _00oq, _00oK --> _00oM
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0682__00oM = (v0681__00oK**1)*(v0679__00oq**-1)
v0682__00oM = (v0682__00oM*_00oL_coeff).reshape((1, 4))

# op _00oN expand_scalar_eval
# LANG: speed_of_sound --> _00oO
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0684__00oO = np.empty((1, 4))
v0684__00oO.fill(v0554_speed_of_sound.item())

# op _00ob_power_combination_eval
# LANG: _00oa --> _00oc
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0669__00oc = (v0668__00oa**1)
v0669__00oc = (v0669__00oc*_00ob_coeff).reshape((1,))

# op _00iB_power_combination_eval
# LANG: _00iA --> _00iC
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0491__00iC = (v0490__00iA**1)
v0491__00iC = (v0491__00iC*_00iB_coeff).reshape((1, 1))

# op _00iF_power_combination_eval
# LANG: _00iE --> _00iG
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0493__00iG = (v0492__00iE**1)
v0493__00iG = (v0493__00iG*_00iF_coeff).reshape((1, 1))

# op _00iL expand_scalar_eval
# LANG: _00iK --> _00iM
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0499__00iM = np.empty((3,))
v0499__00iM.fill(v0498__00iK.item())

# op _00ig pnorm_eval
# LANG: _00i9 --> _00ih
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0481__00ih = np.linalg.norm(v0480__00i9.flatten(), ord=2)

# op _00iq_power_combination_eval
# LANG: _00in, _00ip --> _00ir
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0484__00ir = (v0483__00in**1)*(v0485__00ip**-1)
v0484__00ir = (v0484__00ir*_00iq_coeff).reshape((1, 1))

# op _00it_cos_eval
# LANG: theta --> _00iu
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v048_theta = v048_theta.reshape((1, 1))
v0487__00iu = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00ix_power_combination_eval
# LANG: _00iw --> _00iy
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0489__00iy = (v0488__00iw**1)
v0489__00iy = (v0489__00iy*_00ix_coeff).reshape((1, 1))

# op _00mX expand_array_eval
# LANG: _00mW --> _00mY
# SHAPES: (11, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0628__00mY = np.einsum('cd,ab->abcd', v0627__00mW.reshape((11, 30)) ,np.ones((1, 2))).reshape((1, 2, 11, 30))

# op _00n2 expand_array_eval
# LANG: bbb --> _00n3
# SHAPES: (1, 2, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0624__00n3 = np.einsum('abd,c->abcd', v0623_bbb.reshape((1, 2, 30)) ,np.ones((11,))).reshape((1, 2, 11, 30))

# op _00n6 expand_array_eval
# LANG: aaa --> _00n7
# SHAPES: (1, 2, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0629__00n7 = np.einsum('abd,c->abcd', v0621_aaa.reshape((1, 2, 30)) ,np.ones((11,))).reshape((1, 2, 11, 30))

# op _00nc_power_combination_eval
# LANG: _00nb, _00n1 --> _00nd
# SHAPES: (1, 2, 11, 30), (1, 2, 11, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0632__00nd = (v0631__00nb**1)*(v0634__00n1**1)
v0632__00nd = (v0632__00nd*_00nc_coeff).reshape((1, 2, 11, 30))

# op _00ni_power_combination_eval
# LANG: _00n1, _00nh --> _00nj
# SHAPES: (1, 2, 11, 30), (1, 2, 11, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0637__00nj = (v0636__00nh**1)*(v0634__00n1**1)
v0637__00nj = (v0637__00nj*_00ni_coeff).reshape((1, 2, 11, 30))

# op _00oP_power_combination_eval
# LANG: _00oM, _00oO --> _00oQ
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0683__00oQ = (v0682__00oM**1)*(v0684__00oO**-1)
v0683__00oQ = (v0683__00oQ*_00oP_coeff).reshape((1, 4))

# op _00od_power_combination_eval
# LANG: _00oc --> _00oe
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0670__00oe = (v0669__00oc**1)
v0670__00oe = (v0670__00oe*_00od_coeff).reshape((1,))

# op _00iN_power_combination_eval
# LANG: _00iI, _00iM --> _00iO
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0497__00iO = (v0496__00iI**1)*(v0499__00iM**-1)
v0497__00iO = (v0497__00iO*_00iN_coeff).reshape((3,))

# op _00ii_power_combination_eval
# LANG: _00ih --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0482_propeller_radius = (v0481__00ih**1)
v0482_propeller_radius = (v0482_propeller_radius*_00ii_coeff).reshape((1,))

# op _00is_indexed_passthrough_eval
# LANG: _00ir, _00iu, _00iy, _00iC, _00iG --> rot_mat
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0486_rot_mat__temp[i_v0484__00ir__00is_indexed_passthrough_eval] = v0484__00ir.flatten()
v0486_rot_mat = v0486_rot_mat__temp.copy()
v0486_rot_mat__temp[i_v0487__00iu__00is_indexed_passthrough_eval] = v0487__00iu.flatten()
v0486_rot_mat = v0486_rot_mat__temp.copy()
v0486_rot_mat__temp[i_v0489__00iy__00is_indexed_passthrough_eval] = v0489__00iy.flatten()
v0486_rot_mat = v0486_rot_mat__temp.copy()
v0486_rot_mat__temp[i_v0491__00iC__00is_indexed_passthrough_eval] = v0491__00iC.flatten()
v0486_rot_mat = v0486_rot_mat__temp.copy()
v0486_rot_mat__temp[i_v0493__00iG__00is_indexed_passthrough_eval] = v0493__00iG.flatten()
v0486_rot_mat = v0486_rot_mat__temp.copy()

# op _00n4_power_combination_eval
# LANG: _00n3, _00mY --> aT_integrand
# SHAPES: (1, 2, 11, 30), (1, 2, 11, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0625_aT_integrand = (v0624__00n3**1)*(v0628__00mY**1)
v0625_aT_integrand = (v0625_aT_integrand*_00n4_coeff).reshape((1, 2, 11, 30))

# op _00n8_power_combination_eval
# LANG: _00mY, _00n7 --> aD_integrand
# SHAPES: (1, 2, 11, 30), (1, 2, 11, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0630_aD_integrand = (v0629__00n7**1)*(v0628__00mY**1)
v0630_aD_integrand = (v0630_aD_integrand*_00n8_coeff).reshape((1, 2, 11, 30))

# op _00ne_power_combination_eval
# LANG: _00nd --> bT_integrand
# SHAPES: (1, 2, 11, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0635_bT_integrand = (v0632__00nd**1)
v0635_bT_integrand = (v0635_bT_integrand*_00ne_coeff).reshape((1, 2, 11, 30))

# op _00nk_power_combination_eval
# LANG: _00nj --> bD_integrand
# SHAPES: (1, 2, 11, 30) --> (1, 2, 11, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0638_bD_integrand = (v0637__00nj**1)
v0638_bD_integrand = (v0638_bD_integrand*_00nk_coeff).reshape((1, 2, 11, 30))

# op _00oR_linear_combination_eval
# LANG: _00oQ --> _00oS
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0685__00oS = _00oR_constant+-1*v0683__00oQ

# op _00o_ expand_array_eval
# LANG: in_plane_ex --> _00p0
# SHAPES: (1, 3) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0702__00p0 = np.einsum('ab,c->abc', v0181_in_plane_ex.reshape((1, 3)) ,np.ones((4,))).reshape((1, 3, 4))

# op _00p9 expand_scalar_eval
# LANG: _00oe --> _00pa
# SHAPES: (1,) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0671__00pa = np.empty((1, 4, 3, 2, 11))
v0671__00pa.fill(v0670__00oe.item())

# op _00iP_matvec_eval
# LANG: rot_mat, _00iO --> thrust_dir
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0494_thrust_dir = v0486_rot_mat@v0497__00iO

# op _00nC_single_tensor_sum_with_axis_eval
# LANG: aD_integrand --> _00nD
# SHAPES: (1, 2, 11, 30) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0644__00nD = np.sum(v0630_aD_integrand, axis = (3,)).reshape((1, 2, 11))

# op _00nM_single_tensor_sum_with_axis_eval
# LANG: bT_integrand --> _00nN
# SHAPES: (1, 2, 11, 30) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0648__00nN = np.sum(v0635_bT_integrand, axis = (3,)).reshape((1, 2, 11))

# op _00nW_single_tensor_sum_with_axis_eval
# LANG: bD_integrand --> _00nX
# SHAPES: (1, 2, 11, 30) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0652__00nX = np.sum(v0638_bD_integrand, axis = (3,)).reshape((1, 2, 11))

# op _00ns_single_tensor_sum_with_axis_eval
# LANG: aT_integrand --> _00nt
# SHAPES: (1, 2, 11, 30) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0639__00nt = np.sum(v0625_aT_integrand, axis = (3,)).reshape((1, 2, 11))

# op _00oT_power_combination_eval
# LANG: _00oq, _00oS --> _00oU
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0680__00oU = (v0679__00oq**1)*(v0685__00oS**1)
v0680__00oU = (v0680__00oU*_00oT_coeff).reshape((1, 4))

# op _00p1_tensor_dot_product_eval
# LANG: _00p0, rel_obs_position --> _00p2
# SHAPES: (1, 3, 4), (1, 3, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0701__00p2 = np.sum(v0595_rel_obs_position * v0702__00p0, axis=1)

# op _00pR_power_combination_eval
# LANG: n_var, _00pa --> _00pS
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0697__00pS = (v0665_n_var**1)*(v0671__00pa**1)
v0697__00pS = (v0697__00pS*_00pR_coeff).reshape((1, 4, 3, 2, 11))

# op _00pj expand_scalar_eval
# LANG: propeller_radius --> _00pk
# SHAPES: (1,) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0699__00pk = np.empty((1, 4, 3, 2, 11))
v0699__00pk.fill(v0482_propeller_radius.item())

# op _00nE_power_combination_eval
# LANG: _00nD --> _00nF
# SHAPES: (1, 2, 11) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0645__00nF = (v0644__00nD**1)
v0645__00nF = (v0645__00nF*_00nE_coeff).reshape((1, 2, 11))

# op _00nG expand_scalar_eval
# LANG: dtheta --> _00nH
# SHAPES: (1,) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0647__00nH = np.empty((1, 2, 11))
v0647__00nH.fill(v0642_dtheta.item())

# op _00nO_power_combination_eval
# LANG: _00nN --> _00nP
# SHAPES: (1, 2, 11) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0649__00nP = (v0648__00nN**1)
v0649__00nP = (v0649__00nP*_00nO_coeff).reshape((1, 2, 11))

# op _00nQ expand_scalar_eval
# LANG: dtheta --> _00nR
# SHAPES: (1,) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0651__00nR = np.empty((1, 2, 11))
v0651__00nR.fill(v0642_dtheta.item())

# op _00nY_power_combination_eval
# LANG: _00nX --> _00nZ
# SHAPES: (1, 2, 11) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0653__00nZ = (v0652__00nX**1)
v0653__00nZ = (v0653__00nZ*_00nY_coeff).reshape((1, 2, 11))

# op _00n_ expand_scalar_eval
# LANG: dtheta --> _00o0
# SHAPES: (1,) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0655__00o0 = np.empty((1, 2, 11))
v0655__00o0.fill(v0642_dtheta.item())

# op _00nu_power_combination_eval
# LANG: _00nt --> _00nv
# SHAPES: (1, 2, 11) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0640__00nv = (v0639__00nt**1)
v0640__00nv = (v0640__00nv*_00nu_coeff).reshape((1, 2, 11))

# op _00nw expand_scalar_eval
# LANG: dtheta --> _00nx
# SHAPES: (1,) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0643__00nx = np.empty((1, 2, 11))
v0643__00nx.fill(v0642_dtheta.item())

# op _00oX expand_array_eval
# LANG: thrust_dir --> _00oY
# SHAPES: (3,) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0674__00oY = np.einsum('b,ac->abc', v0494_thrust_dir.reshape((3,)) ,np.ones((1, 4))).reshape((1, 3, 4))

# op _00pT_power_combination_eval
# LANG: _00pS, _00pk --> _00pU
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0698__00pU = (v0697__00pS**1)*(v0699__00pk**1)
v0698__00pU = (v0698__00pU*_00pT_coeff).reshape((1, 4, 3, 2, 11))

# op _00pd expand_array_eval
# LANG: _00p2 --> _00pe
# SHAPES: (1, 4) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0703__00pe = np.einsum('ab,cde->abcde', v0701__00p2.reshape((1, 4)) ,np.ones((3, 2, 11))).reshape((1, 4, 3, 2, 11))

# op _00pf expand_scalar_eval
# LANG: speed_of_sound --> _00pg
# SHAPES: (1,) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0677__00pg = np.empty((1, 4, 3, 2, 11))
v0677__00pg.fill(v0554_speed_of_sound.item())

# op _00ph expand_array_eval
# LANG: _00oU --> _00pi
# SHAPES: (1, 4) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0686__00pi = np.einsum('ab,cde->abcde', v0680__00oU.reshape((1, 4)) ,np.ones((3, 2, 11))).reshape((1, 4, 3, 2, 11))

# op _00nI_power_combination_eval
# LANG: _00nF, _00nH --> aD
# SHAPES: (1, 2, 11), (1, 2, 11) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0646_aD = (v0645__00nF**1)*(v0647__00nH**1)
v0646_aD = (v0646_aD*_00nI_coeff).reshape((1, 2, 11))

# op _00nS_power_combination_eval
# LANG: _00nP, _00nR --> bT
# SHAPES: (1, 2, 11), (1, 2, 11) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0650_bT = (v0649__00nP**1)*(v0651__00nR**1)
v0650_bT = (v0650_bT*_00nS_coeff).reshape((1, 2, 11))

# op _00ny_power_combination_eval
# LANG: _00nv, _00nx --> aT
# SHAPES: (1, 2, 11), (1, 2, 11) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0641_aT = (v0640__00nv**1)*(v0643__00nx**1)
v0641_aT = (v0641_aT*_00ny_coeff).reshape((1, 2, 11))

# op _00o1_power_combination_eval
# LANG: _00nZ, _00o0 --> bD
# SHAPES: (1, 2, 11), (1, 2, 11) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0654_bD = (v0653__00nZ**1)*(v0655__00o0**1)
v0654_bD = (v0654_bD*_00o1_coeff).reshape((1, 2, 11))

# op _00p3_tensor_dot_product_eval
# LANG: _00oY, rel_obs_position --> _00p4
# SHAPES: (1, 3, 4), (1, 3, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0673__00p4 = np.sum(v0595_rel_obs_position * v0674__00oY, axis=1)

# op _00pV_power_combination_eval
# LANG: _00pU, _00pe --> _00pW
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0700__00pW = (v0698__00pU**1)*(v0703__00pe**1)
v0700__00pW = (v0700__00pW*_00pV_coeff).reshape((1, 4, 3, 2, 11))

# op _00pX_power_combination_eval
# LANG: _00pg, _00pi --> _00pY
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0705__00pY = (v0677__00pg**1)*(v0686__00pi**1)
v0705__00pY = (v0705__00pY*_00pX_coeff).reshape((1, 4, 3, 2, 11))

# op _00qA_exp_a_eval
# LANG: lam_var --> _00qB
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0731__00qB = _00qA_exp_a_eval_a**v0710_lam_var

# op _00rx_exp_a_eval
# LANG: lam_var --> _00ry
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0764__00ry = _00rx_exp_a_eval_a**v0710_lam_var

# op _00pD_power_combination_eval
# LANG: n_var, _00pa --> _00pE
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0666__00pE = (v0665_n_var**1)*(v0671__00pa**1)
v0666__00pE = (v0666__00pE*_00pD_coeff).reshape((1, 4, 3, 2, 11))

# op _00pH_power_combination_eval
# LANG: _00pi --> _00pI
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0687__00pI = (v0686__00pi**2)
v0687__00pI = (v0687__00pI*_00pH_coeff).reshape((1, 4, 3, 2, 11))

# op _00pZ_power_combination_eval
# LANG: _00pW, _00pY --> _00p_
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0704__00p_ = (v0700__00pW**1)*(v0705__00pY**-1)
v0704__00p_ = (v0704__00p_*_00pZ_coeff).reshape((1, 4, 3, 2, 11))

# op _00pb expand_array_eval
# LANG: _00p4 --> _00pc
# SHAPES: (1, 4) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0675__00pc = np.einsum('ab,cde->abcde', v0673__00p4.reshape((1, 4)) ,np.ones((3, 2, 11))).reshape((1, 4, 3, 2, 11))

# op _00pl expand_array_eval
# LANG: aT --> _00pm
# SHAPES: (1, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0695__00pm = np.einsum('ade,bc->abcde', v0641_aT.reshape((1, 2, 11)) ,np.ones((4, 3))).reshape((1, 4, 3, 2, 11))

# op _00pn expand_array_eval
# LANG: bT --> _00po
# SHAPES: (1, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0691__00po = np.einsum('ade,bc->abcde', v0650_bT.reshape((1, 2, 11)) ,np.ones((4, 3))).reshape((1, 4, 3, 2, 11))

# op _00pp expand_array_eval
# LANG: aD --> _00pq
# SHAPES: (1, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0724__00pq = np.einsum('ade,bc->abcde', v0646_aD.reshape((1, 2, 11)) ,np.ones((4, 3))).reshape((1, 4, 3, 2, 11))

# op _00pr expand_array_eval
# LANG: bD --> _00ps
# SHAPES: (1, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0721__00ps = np.einsum('ade,bc->abcde', v0654_bD.reshape((1, 2, 11)) ,np.ones((4, 3))).reshape((1, 4, 3, 2, 11))

# op _00qC_power_combination_eval
# LANG: A_lin_comb_sign_matrix, _00qB --> _00qD
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0730__00qD = (v0708_A_lin_comb_sign_matrix**1)*(v0731__00qB**1)
v0730__00qD = (v0730__00qD*_00qC_coeff).reshape((1, 4, 3, 2, 11))

# op _00qE_linear_combination_eval
# LANG: n_var, lam_var --> _00qF
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0733__00qF = _00qE_constant+1*v0665_n_var+1*v0710_lam_var

# op _00qg_exp_a_eval
# LANG: lam_var --> _00qh
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0711__00qh = _00qg_exp_a_eval_a**v0710_lam_var

# op _00rB_linear_combination_eval
# LANG: n_var, lam_var --> _00rC
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0766__00rC = _00rB_constant+1*v0665_n_var+1*v0710_lam_var

# op _00rd_exp_a_eval
# LANG: lam_var --> _00re
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0748__00re = _00rd_exp_a_eval_a**v0710_lam_var

# op _00rz_power_combination_eval
# LANG: B_lin_comb_sign_matrix, _00ry --> _00rA
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0763__00rA = (v0746_B_lin_comb_sign_matrix**1)*(v0764__00ry**1)
v0763__00rA = (v0763__00rA*_00rz_coeff).reshape((1, 4, 3, 2, 11))

# op _00pF_power_combination_eval
# LANG: _00pE, _00pc --> _00pG
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0672__00pG = (v0666__00pE**1)*(v0675__00pc**1)
v0672__00pG = (v0672__00pG*_00pF_coeff).reshape((1, 4, 3, 2, 11))

# op _00pJ_power_combination_eval
# LANG: _00pg, _00pI --> _00pK
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0678__00pK = (v0677__00pg**1)*(v0687__00pI**1)
v0678__00pK = (v0678__00pK*_00pJ_coeff).reshape((1, 4, 3, 2, 11))

# op _00pN_power_combination_eval
# LANG: _00pi, _00pk --> _00pO
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0717__00pO = (v0699__00pk**1)*(v0686__00pi**1)
v0717__00pO = (v0717__00pO*_00pN_coeff).reshape((1, 4, 3, 2, 11))

# op _00q0_power_combination_eval
# LANG: coeff_sign_matrix_even, _00po --> _00q1
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0690__00q1 = (v0689_coeff_sign_matrix_even**1)*(v0691__00po**1)
v0690__00q1 = (v0690__00q1*_00q0_coeff).reshape((1, 4, 3, 2, 11))

# op _00q2_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00pm --> _00q3
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0694__00q3 = (v0693_coeff_sign_matrix_odd**1)*(v0695__00pm**1)
v0694__00q3 = (v0694__00q3*_00q2_coeff).reshape((1, 4, 3, 2, 11))

# op _00q6_power_combination_eval
# LANG: coeff_sign_matrix_even, _00ps --> _00q7
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0720__00q7 = (v0689_coeff_sign_matrix_even**1)*(v0721__00ps**1)
v0720__00q7 = (v0720__00q7*_00q6_coeff).reshape((1, 4, 3, 2, 11))

# op _00q8_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00pq --> _00q9
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0723__00q9 = (v0693_coeff_sign_matrix_odd**1)*(v0724__00pq**1)
v0723__00q9 = (v0723__00q9*_00q8_coeff).reshape((1, 4, 3, 2, 11))

# op _00qG_power_combination_eval
# LANG: _00qD, _00qF --> _00qH
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0732__00qH = (v0730__00qD**1)*(v0733__00qF**1)
v0732__00qH = (v0732__00qH*_00qG_coeff).reshape((1, 4, 3, 2, 11))

# op _00qI_bessel_eval
# LANG: _00p_ --> _00qJ
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0735__00qJ=_00qI_bessel_eval(_00qI_bessel_eval_order,v0704__00p_)

# op _00qY_power_combination_eval
# LANG: coeff_sign_matrix_even, _00pm --> _00qZ
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0740__00qZ = (v0689_coeff_sign_matrix_even**1)*(v0695__00pm**1)
v0740__00qZ = (v0740__00qZ*_00qY_coeff).reshape((1, 4, 3, 2, 11))

# op _00q__power_combination_eval
# LANG: _00po, coeff_sign_matrix_odd --> _00r0
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0742__00r0 = (v0693_coeff_sign_matrix_odd**1)*(v0691__00po**1)
v0742__00r0 = (v0742__00r0*_00q__coeff).reshape((1, 4, 3, 2, 11))

# op _00qi_power_combination_eval
# LANG: A_lin_comb_sign_matrix, _00qh --> _00qj
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0709__00qj = (v0708_A_lin_comb_sign_matrix**1)*(v0711__00qh**1)
v0709__00qj = (v0709__00qj*_00qi_coeff).reshape((1, 4, 3, 2, 11))

# op _00qk_bessel_eval
# LANG: _00p_ --> _00ql
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0713__00ql=_00qk_bessel_eval(_00qk_bessel_eval_order,v0704__00p_)

# op _00qu_linear_combination_eval
# LANG: n_var, lam_var --> _00qv
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0726__00qv = _00qu_constant+1*v0665_n_var+-1*v0710_lam_var

# op _00qw_bessel_eval
# LANG: _00p_ --> _00qx
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0728__00qx=_00qw_bessel_eval(_00qw_bessel_eval_order,v0704__00p_)

# op _00r3_power_combination_eval
# LANG: coeff_sign_matrix_even, _00pq --> _00r4
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0755__00r4 = (v0689_coeff_sign_matrix_even**1)*(v0724__00pq**1)
v0755__00r4 = (v0755__00r4*_00r3_coeff).reshape((1, 4, 3, 2, 11))

# op _00r5_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00ps --> _00r6
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0757__00r6 = (v0693_coeff_sign_matrix_odd**1)*(v0721__00ps**1)
v0757__00r6 = (v0757__00r6*_00r5_coeff).reshape((1, 4, 3, 2, 11))

# op _00rD_power_combination_eval
# LANG: _00rA, _00rC --> _00rE
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0765__00rE = (v0763__00rA**1)*(v0766__00rC**1)
v0765__00rE = (v0765__00rE*_00rD_coeff).reshape((1, 4, 3, 2, 11))

# op _00rF_bessel_eval
# LANG: _00p_ --> _00rG
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0768__00rG=_00rF_bessel_eval(_00rF_bessel_eval_order,v0704__00p_)

# op _00rf_power_combination_eval
# LANG: B_lin_comb_sign_matrix, _00re --> _00rg
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0747__00rg = (v0746_B_lin_comb_sign_matrix**1)*(v0748__00re**1)
v0747__00rg = (v0747__00rg*_00rf_coeff).reshape((1, 4, 3, 2, 11))

# op _00rh_bessel_eval
# LANG: _00p_ --> _00ri
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0750__00ri=_00rh_bessel_eval(_00rh_bessel_eval_order,v0704__00p_)

# op _00rr_linear_combination_eval
# LANG: n_var, lam_var --> _00rs
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0759__00rs = _00rr_constant+1*v0665_n_var+-1*v0710_lam_var

# op _00rt_bessel_eval
# LANG: _00p_ --> _00ru
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0761__00ru=_00rt_bessel_eval(_00rt_bessel_eval_order,v0704__00p_)

# op _00uB expand_scalar_eval
# LANG: Vy --> _00uC
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0847__00uC = np.empty((1, 1))
v0847__00uC.fill(v035_v.item())

# op _00uD expand_scalar_eval
# LANG: Vz --> _00uE
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0848__00uE = np.empty((1, 1))
v0848__00uE.fill(v039_w.item())

# op _00uy expand_scalar_eval
# LANG: Vx --> _00uz
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0845__00uz = np.empty((1, 1))
v0845__00uz.fill(v030_u.item())

# op _00pL_power_combination_eval
# LANG: _00pG, _00pK --> _00pM
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0676__00pM = (v0672__00pG**1)*(v0678__00pK**-1)
v0676__00pM = (v0676__00pM*_00pL_coeff).reshape((1, 4, 3, 2, 11))

# op _00pP_power_combination_eval
# LANG: _00pO --> _00pQ
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0718__00pQ = (v0717__00pO**-1)
v0718__00pQ = (v0718__00pQ*_00pP_coeff).reshape((1, 4, 3, 2, 11))

# op _00q4_linear_combination_eval
# LANG: _00q1, _00q3 --> _00q5
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0692__00q5 = _00q4_constant+1*v0690__00q1+1*v0694__00q3

# op _00qK_power_combination_eval
# LANG: _00qH, _00qJ --> _00qL
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0734__00qL = (v0732__00qH**1)*(v0735__00qJ**1)
v0734__00qL = (v0734__00qL*_00qK_coeff).reshape((1, 4, 3, 2, 11))

# op _00qa_linear_combination_eval
# LANG: _00q7, _00q9 --> _00qb
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0722__00qb = _00qa_constant+1*v0720__00q7+1*v0723__00q9

# op _00qe_bessel_eval
# LANG: _00p_ --> _00qf
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0706__00qf=_00qe_bessel_eval(_00qe_bessel_eval_order,v0704__00p_)

# op _00qm_power_combination_eval
# LANG: _00qj, _00ql --> _00qn
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0712__00qn = (v0709__00qj**1)*(v0713__00ql**1)
v0712__00qn = (v0712__00qn*_00qm_coeff).reshape((1, 4, 3, 2, 11))

# op _00qy_power_combination_eval
# LANG: _00qv, _00qx --> _00qz
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0727__00qz = (v0726__00qv**1)*(v0728__00qx**1)
v0727__00qz = (v0727__00qz*_00qy_coeff).reshape((1, 4, 3, 2, 11))

# op _00r1_linear_combination_eval
# LANG: _00qZ, _00r0 --> _00r2
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0741__00r2 = _00r1_constant+1*v0740__00qZ+1*v0742__00r0

# op _00r7_linear_combination_eval
# LANG: _00r4, _00r6 --> _00r8
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0756__00r8 = _00r7_constant+1*v0755__00r4+1*v0757__00r6

# op _00rH_power_combination_eval
# LANG: _00rE, _00rG --> _00rI
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0767__00rI = (v0765__00rE**1)*(v0768__00rG**1)
v0767__00rI = (v0767__00rI*_00rH_coeff).reshape((1, 4, 3, 2, 11))

# op _00rb_bessel_eval
# LANG: _00p_ --> _00rc
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0744__00rc=_00rb_bessel_eval(_00rb_bessel_eval_order,v0704__00p_)

# op _00rj_power_combination_eval
# LANG: _00rg, _00ri --> _00rk
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0749__00rk = (v0747__00rg**1)*(v0750__00ri**1)
v0749__00rk = (v0749__00rk*_00rj_coeff).reshape((1, 4, 3, 2, 11))

# op _00rv_power_combination_eval
# LANG: _00rs, _00ru --> _00rw
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0760__00rw = (v0759__00rs**1)*(v0761__00ru**1)
v0760__00rw = (v0760__00rw*_00rv_coeff).reshape((1, 4, 3, 2, 11))

# op _00uA_indexed_passthrough_eval
# LANG: _00uz, _00uC, _00uE --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0846_V_aircraft__temp[i_v0845__00uz__00uA_indexed_passthrough_eval] = v0845__00uz.flatten()
v0846_V_aircraft = v0846_V_aircraft__temp.copy()
v0846_V_aircraft__temp[i_v0847__00uC__00uA_indexed_passthrough_eval] = v0847__00uC.flatten()
v0846_V_aircraft = v0846_V_aircraft__temp.copy()
v0846_V_aircraft__temp[i_v0848__00uE__00uA_indexed_passthrough_eval] = v0848__00uE.flatten()
v0846_V_aircraft = v0846_V_aircraft__temp.copy()

# op _00qM_linear_combination_eval
# LANG: _00qz, _00qL --> _00qN
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0729__00qN = _00qM_constant+1*v0727__00qz+1*v0734__00qL

# op _00qc_power_combination_eval
# LANG: _00pM, _00q5 --> _00qd
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0688__00qd = (v0676__00pM**1)*(v0692__00q5**1)
v0688__00qd = (v0688__00qd*_00qc_coeff).reshape((1, 4, 3, 2, 11))

# op _00qo_linear_combination_eval
# LANG: _00qf, _00qn --> _00qp
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0707__00qp = _00qo_constant+1*v0706__00qf+1*v0712__00qn

# op _00qs_power_combination_eval
# LANG: _00pQ, _00qb --> _00qt
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0719__00qt = (v0718__00pQ**1)*(v0722__00qb**1)
v0719__00qt = (v0719__00qt*_00qs_coeff).reshape((1, 4, 3, 2, 11))

# op _00r9_power_combination_eval
# LANG: _00pM, _00r2 --> _00ra
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0739__00ra = (v0676__00pM**1)*(v0741__00r2**1)
v0739__00ra = (v0739__00ra*_00r9_coeff).reshape((1, 4, 3, 2, 11))

# op _00rJ_linear_combination_eval
# LANG: _00rw, _00rI --> _00rK
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0762__00rK = _00rJ_constant+1*v0760__00rw+1*v0767__00rI

# op _00rl_linear_combination_eval
# LANG: _00rc, _00rk --> _00rm
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0745__00rm = _00rl_constant+1*v0744__00rc+1*v0749__00rk

# op _00rp_power_combination_eval
# LANG: _00pQ, _00r8 --> _00rq
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0754__00rq = (v0718__00pQ**1)*(v0756__00r8**1)
v0754__00rq = (v0754__00rq*_00rp_coeff).reshape((1, 4, 3, 2, 11))

# op _00uF expand_array_eval
# LANG: V_aircraft --> _00uG
# SHAPES: (1, 3) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0855__00uG = np.einsum('ab,c->abc', v0846_V_aircraft.reshape((1, 3)) ,np.ones((4,))).reshape((1, 3, 4))

# op _00uL expand_array_eval
# LANG: time_vectors --> _00uM
# SHAPES: (4,) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0861__00uM = np.einsum('c,ab->abc', v0860_time_vectors.reshape((4,)) ,np.ones((1, 3))).reshape((1, 3, 4))

# op _00qO_power_combination_eval
# LANG: _00qt, _00qN --> _00qP
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0725__00qP = (v0719__00qt**1)*(v0729__00qN**1)
v0725__00qP = (v0725__00qP*_00qO_coeff).reshape((1, 4, 3, 2, 11))

# op _00qq_power_combination_eval
# LANG: _00qd, _00qp --> _00qr
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0696__00qr = (v0688__00qd**1)*(v0707__00qp**1)
v0696__00qr = (v0696__00qr*_00qq_coeff).reshape((1, 4, 3, 2, 11))

# op _00rL_power_combination_eval
# LANG: _00rq, _00rK --> _00rM
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0758__00rM = (v0754__00rq**1)*(v0762__00rK**1)
v0758__00rM = (v0758__00rM*_00rL_coeff).reshape((1, 4, 3, 2, 11))

# op _00rn_power_combination_eval
# LANG: _00ra, _00rm --> _00ro
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0743__00ro = (v0739__00ra**1)*(v0745__00rm**1)
v0743__00ro = (v0743__00ro*_00rn_coeff).reshape((1, 4, 3, 2, 11))

# op _00sC_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _00sD
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v0807__00sD = (v010_rotor_disk_in_plane_2**1)
v0807__00sD = (v0807__00sD*_00sC_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _00sw_power_combination_eval
# LANG: rotor_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v0788_origin = (v012_rotor_disk_origin**1)
v0788_origin = (v0788_origin*_00sw_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _00sz_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00sA
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v0789__00sA = (v08_rotor_disk_in_plane_1**1)
v0789__00sA = (v0789__00sA*_00sz_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _00uI expand_array_eval
# LANG: aircraft_location --> _00uJ
# SHAPES: (3, 4) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0850__00uJ = np.einsum('bc,a->abc', v0849_aircraft_location.reshape((3, 4)) ,np.ones((1,))).reshape((1, 3, 4))

# op _00uP_decompose_eval
# LANG: _00uG --> _00uQ, _00uY, _00v4
# SHAPES: (1, 3, 4) --> (1, 1, 4), (1, 1, 4), (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0856__00uQ = ((v0855__00uG.flatten())[src_indices__00uQ__00uP]).reshape((1, 1, 4))
v0857__00uY = ((v0855__00uG.flatten())[src_indices__00uY__00uP]).reshape((1, 1, 4))
v0858__00v4 = ((v0855__00uG.flatten())[src_indices__00v4__00uP]).reshape((1, 1, 4))

# op _00uR_decompose_eval
# LANG: _00uM --> _00uS, _00uZ, _00v5
# SHAPES: (1, 3, 4) --> (1, 1, 4), (1, 1, 4), (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0862__00uS = ((v0861__00uM.flatten())[src_indices__00uS__00uR]).reshape((1, 1, 4))
v0863__00uZ = ((v0861__00uM.flatten())[src_indices__00uZ__00uR]).reshape((1, 1, 4))
v0864__00v5 = ((v0861__00uM.flatten())[src_indices__00v5__00uR]).reshape((1, 1, 4))

# op _00bo_power_combination_eval
# LANG: _angular_speed --> _00bp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0442__00bp = (v0216__angular_speed**1)
v0442__00bp = (v0442__00bp*_00bo_coeff).reshape((1, 40, 30))

# op _00qQ_power_combination_eval
# LANG: term_1_coeff_A, _00qr --> _00qR
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0664__00qR = (v0663_term_1_coeff_A**1)*(v0696__00qr**1)
v0664__00qR = (v0664__00qR*_00qQ_coeff).reshape((1, 4, 3, 2, 11))

# op _00qS_power_combination_eval
# LANG: term_2_coeff_A, _00qP --> _00qT
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0716__00qT = (v0715_term_2_coeff_A**1)*(v0725__00qP**1)
v0716__00qT = (v0716__00qT*_00qS_coeff).reshape((1, 4, 3, 2, 11))

# op _00rN_power_combination_eval
# LANG: term_1_coeff_B, _00ro --> _00rO
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0738__00rO = (v0737_term_1_coeff_B**1)*(v0743__00ro**1)
v0738__00rO = (v0738__00rO*_00rN_coeff).reshape((1, 4, 3, 2, 11))

# op _00rP_power_combination_eval
# LANG: term_2_coeff_B, _00rM --> _00rQ
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0753__00rQ = (v0752_term_2_coeff_B**1)*(v0758__00rM**1)
v0753__00rQ = (v0753__00rQ*_00rP_coeff).reshape((1, 4, 3, 2, 11))

# op _00tb cross_product_eval
# LANG: _00sA, _00sD --> _00tc
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0808__00tc = np.cross(v0807__00sD, v0789__00sA, axisa = 0, axisb = 0, axisc = 0)

# op _00uN_decompose_eval
# LANG: _00uJ --> _00uO, _00uX, _00v3
# SHAPES: (1, 3, 4) --> (1, 1, 4), (1, 1, 4), (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0851__00uO = ((v0850__00uJ.flatten())[src_indices__00uO__00uN]).reshape((1, 1, 4))
v0852__00uX = ((v0850__00uJ.flatten())[src_indices__00uX__00uN]).reshape((1, 1, 4))
v0853__00v3 = ((v0850__00uJ.flatten())[src_indices__00v3__00uN]).reshape((1, 1, 4))

# op _00uT_power_combination_eval
# LANG: _00uQ, _00uS --> _00uU
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0859__00uU = (v0856__00uQ**1)*(v0862__00uS**1)
v0859__00uU = (v0859__00uU*_00uT_coeff).reshape((1, 1, 4))

# op _00u__power_combination_eval
# LANG: _00uY, _00uZ --> _00v0
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0866__00v0 = (v0857__00uY**1)*(v0863__00uZ**1)
v0866__00v0 = (v0866__00v0*_00u__coeff).reshape((1, 1, 4))

# op _00vh expand_array_eval
# LANG: origin --> _00vi
# SHAPES: (3,) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0873__00vi = np.einsum('b,ac->abc', v0788_origin.reshape((3,)) ,np.ones((1, 4))).reshape((1, 3, 4))

# op _00bq_power_combination_eval
# LANG: _00bp --> _00br
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0443__00br = (v0442__00bp**1)
v0443__00br = (v0443__00br*_00bq_coeff).reshape((1, 40, 30))

# op _00qU_linear_combination_eval
# LANG: _00qR, _00qT --> _00qV
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0714__00qV = _00qU_constant+1*v0664__00qR+1*v0716__00qT

# op _00rR_linear_combination_eval
# LANG: _00rO, _00rQ --> _00rS
# SHAPES: (1, 4, 3, 2, 11), (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0751__00rS = _00rR_constant+1*v0738__00rO+1*v0753__00rQ

# op _00sE pnorm_eval
# LANG: _00sA --> _00sF
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0790__00sF = np.linalg.norm(v0789__00sA.flatten(), ord=2)

# op _00sJ pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00sK
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0792__00sK = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00sR_linear_combination_eval
# LANG: theta --> _00sS
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0795__00sS = _00sR_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _00sT_linear_combination_eval
# LANG: theta --> _00sU
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0797__00sU = _00sT_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _00s__sin_eval
# LANG: theta --> _00t0
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0800__00t0 = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00t3_sin_eval
# LANG: theta --> _00t4
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0802__00t4 = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00t7_cos_eval
# LANG: theta --> _00t8
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0804__00t8 = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00td pnorm_eval
# LANG: _00tc --> _00te
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0810__00te = np.linalg.norm(v0808__00tc.flatten(), ord=2)

# op _00uV_linear_combination_eval
# LANG: _00uO, _00uU --> aircraft_x_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0854_aircraft_x_pos = _00uV_constant+1*v0851__00uO+1*v0859__00uU

# op _00v1_linear_combination_eval
# LANG: _00uX, _00v0 --> aircraft_y_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0865_aircraft_y_pos = _00v1_constant+1*v0852__00uX+1*v0866__00v0

# op _00v6_power_combination_eval
# LANG: _00v4, _00v5 --> _00v7
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0868__00v7 = (v0858__00v4**1)*(v0864__00v5**1)
v0868__00v7 = (v0868__00v7*_00v6_coeff).reshape((1, 1, 4))

# op _00vj_decompose_eval
# LANG: _00vi --> _00vk, _00vp, _00vu
# SHAPES: (1, 3, 4) --> (1, 1, 4), (1, 1, 4), (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0874__00vk = ((v0873__00vi.flatten())[src_indices__00vk__00vj]).reshape((1, 1, 4))
v0875__00vp = ((v0873__00vi.flatten())[src_indices__00vp__00vj]).reshape((1, 1, 4))
v0876__00vu = ((v0873__00vi.flatten())[src_indices__00vu__00vj]).reshape((1, 1, 4))

# op _00gJ_single_tensor_sum_with_axis_eval
# LANG: _00br --> _00gK
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0444__00gK = np.sum(v0443__00br, axis = (1, 2)).reshape((1,))

# op _00gT_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00gU
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0449__00gU = np.sum(v0204__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00qW_power_combination_eval
# LANG: _00qV --> An
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0736_An = (v0714__00qV**1)
v0736_An = (v0736_An*_00qW_coeff).reshape((1, 4, 3, 2, 11))

# op _00rT_power_combination_eval
# LANG: _00rS --> Bn
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0769_Bn = (v0751__00rS**1)
v0769_Bn = (v0769_Bn*_00rT_coeff).reshape((1, 4, 3, 2, 11))

# op _00sG_power_combination_eval
# LANG: _00sF --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0791_propeller_radius = (v0790__00sF**1)
v0791_propeller_radius = (v0791_propeller_radius*_00sG_coeff).reshape((1,))

# op _00sL reshape_eval
# LANG: _00sK --> _00sM
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0793__00sM = v0792__00sK.reshape((40, 1))

# op _00sV_power_combination_eval
# LANG: _00sS, _00sU --> _00sW
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0796__00sW = (v0795__00sS**1)*(v0797__00sU**-1)
v0796__00sW = (v0796__00sW*_00sV_coeff).reshape((1, 1))

# op _00sY_cos_eval
# LANG: theta --> _00sZ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0799__00sZ = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00t1_power_combination_eval
# LANG: _00t0 --> _00t2
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0801__00t2 = (v0800__00t0**1)
v0801__00t2 = (v0801__00t2*_00t1_coeff).reshape((1, 1))

# op _00t5_power_combination_eval
# LANG: _00t4 --> _00t6
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0803__00t6 = (v0802__00t4**1)
v0803__00t6 = (v0803__00t6*_00t5_coeff).reshape((1, 1))

# op _00t9_power_combination_eval
# LANG: _00t8 --> _00ta
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0805__00ta = (v0804__00t8**1)
v0805__00ta = (v0805__00ta*_00t9_coeff).reshape((1, 1))

# op _00tf expand_scalar_eval
# LANG: _00te --> _00tg
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0811__00tg = np.empty((3,))
v0811__00tg.fill(v0810__00te.item())

# op _00v8_linear_combination_eval
# LANG: _00v3, _00v7 --> aircraft_z_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0867_aircraft_z_pos = _00v8_constant+1*v0853__00v3+1*v0868__00v7

# op _00va expand_array_eval
# LANG: init_obs_x_loc --> _00vb
# SHAPES: (4,) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0870__00vb = np.einsum('c,ab->abc', v0869_init_obs_x_loc.reshape((4,)) ,np.ones((1, 1))).reshape((1, 1, 4))

# op _00vc expand_array_eval
# LANG: init_obs_y_loc --> _00vd
# SHAPES: (4,) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0878__00vd = np.einsum('c,ab->abc', v0877_init_obs_y_loc.reshape((4,)) ,np.ones((1, 1))).reshape((1, 1, 4))

# op _00vl_linear_combination_eval
# LANG: aircraft_x_pos, _00vk --> _00vm
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0872__00vm = _00vl_constant+1*v0854_aircraft_x_pos+1*v0874__00vk

# op _00vq_linear_combination_eval
# LANG: aircraft_y_pos, _00vp --> _00vr
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0880__00vr = _00vq_constant+1*v0865_aircraft_y_pos+1*v0875__00vp

# op _00fM_single_tensor_sum_with_axis_eval
# LANG: _local_thrust --> _00fN
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0343__00fN = np.sum(v0328__local_thrust, axis = (1, 2)).reshape((1,))

# op _00gL_power_combination_eval
# LANG: _00gK --> _00gM
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0445__00gM = (v0444__00gK**1)
v0445__00gM = (v0445__00gM*_00gL_coeff).reshape((1,))

# op _00gV_power_combination_eval
# LANG: _00gU --> _00gW
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0450__00gW = (v0449__00gU**1)
v0450__00gW = (v0450__00gW*_00gV_coeff).reshape((1,))

# op _00rV_single_tensor_sum_with_axis_eval
# LANG: An --> _00rW
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0770__00rW = np.sum(v0736_An, axis = (4,)).reshape((1, 4, 3, 2))

# op _00rX_single_tensor_sum_with_axis_eval
# LANG: Bn --> _00rY
# SHAPES: (1, 4, 3, 2, 11) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0773__00rY = np.sum(v0769_Bn, axis = (4,)).reshape((1, 4, 3, 2))

# op _00sN_power_combination_eval
# LANG: _00sM --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0794_chord_profile = (v0793__00sM**1)
v0794_chord_profile = (v0794_chord_profile*_00sN_coeff).reshape((40, 1))

# op _00sX_indexed_passthrough_eval
# LANG: _00sW, _00sZ, _00t2, _00t6, _00ta --> rot_mat
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0798_rot_mat__temp[i_v0796__00sW__00sX_indexed_passthrough_eval] = v0796__00sW.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()
v0798_rot_mat__temp[i_v0799__00sZ__00sX_indexed_passthrough_eval] = v0799__00sZ.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()
v0798_rot_mat__temp[i_v0801__00t2__00sX_indexed_passthrough_eval] = v0801__00t2.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()
v0798_rot_mat__temp[i_v0803__00t6__00sX_indexed_passthrough_eval] = v0803__00t6.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()
v0798_rot_mat__temp[i_v0805__00ta__00sX_indexed_passthrough_eval] = v0805__00ta.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()

# op _00th_power_combination_eval
# LANG: _00tc, _00tg --> _00ti
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0809__00ti = (v0808__00tc**1)*(v0811__00tg**-1)
v0809__00ti = (v0809__00ti*_00th_coeff).reshape((3,))

# op _00tn_power_combination_eval
# LANG: propeller_radius --> _00to
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0812__00to = (v0791_propeller_radius**1)
v0812__00to = (v0812__00to*_00tn_coeff).reshape((1,))

# op _00ve expand_array_eval
# LANG: init_obs_z_loc --> _00vf
# SHAPES: (4,) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0882__00vf = np.einsum('c,ab->abc', v0881_init_obs_z_loc.reshape((4,)) ,np.ones((1, 1))).reshape((1, 1, 4))

# op _00vn_linear_combination_eval
# LANG: _00vb, _00vm --> rel_obs_x_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0871_rel_obs_x_pos = _00vn_constant+1*v0870__00vb+-1*v0872__00vm

# op _00vs_linear_combination_eval
# LANG: _00vd, _00vr --> rel_obs_y_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0879_rel_obs_y_pos = _00vs_constant+1*v0878__00vd+-1*v0880__00vr

# op _00vv_linear_combination_eval
# LANG: aircraft_z_pos, _00vu --> _00vw
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0884__00vw = _00vv_constant+1*v0867_aircraft_z_pos+1*v0876__00vu

# op _00fO_power_combination_eval
# LANG: _00fN --> T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0344_T = (v0343__00fN**1)
v0344_T = (v0344_T*_00fO_coeff).reshape((1,))

# op _00gN_power_combination_eval
# LANG: _00gM --> _00gO
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0446__00gO = (v0445__00gM**1)
v0446__00gO = (v0446__00gO*_00gN_coeff).reshape((1,))

# op _00gX_power_combination_eval
# LANG: _00gW --> _00gY
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0451__00gY = (v0450__00gW**1)
v0451__00gY = (v0451__00gY*_00gX_coeff).reshape((1,))

# op _00rZ_power_combination_eval
# LANG: _00rW --> _00r_
# SHAPES: (1, 4, 3, 2) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0771__00r_ = (v0770__00rW**2)
v0771__00r_ = (v0771__00r_*_00rZ_coeff).reshape((1, 4, 3, 2))

# op _00s0_power_combination_eval
# LANG: _00rY --> _00s1
# SHAPES: (1, 4, 3, 2) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0774__00s1 = (v0773__00rY**2)
v0774__00s1 = (v0774__00s1*_00s0_coeff).reshape((1, 4, 3, 2))

# op _00tj_matvec_eval
# LANG: rot_mat, _00ti --> thrust_dir
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0806_thrust_dir = v0798_rot_mat@v0809__00ti

# op _00tp_power_combination_eval
# LANG: _00to --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0813_dr = (v0812__00to**1)
v0813_dr = (v0813_dr*_00tp_coeff).reshape((1,))

# op _00vB_power_combination_eval
# LANG: rel_obs_x_pos --> _00vC
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0886__00vC = (v0871_rel_obs_x_pos**2)
v0886__00vC = (v0886__00vC*_00vB_coeff).reshape((1, 1, 4))

# op _00vD_power_combination_eval
# LANG: rel_obs_y_pos --> _00vE
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0888__00vE = (v0879_rel_obs_y_pos**2)
v0888__00vE = (v0888__00vE*_00vD_coeff).reshape((1, 1, 4))

# op _00vx_linear_combination_eval
# LANG: _00vf, _00vw --> rel_obs_z_pos
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0883_rel_obs_z_pos = _00vx_constant+1*v0882__00vf+-1*v0884__00vw

# op _00wK single_tensor_sum_no_axis_eval
# LANG: chord_profile --> _00wL
# SHAPES: (40, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0910__00wL = np.sum(v0794_chord_profile).reshape((1,))

# op _00wt_power_combination_eval
# LANG: rpm --> _00wu
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0164_rpm = v0164_rpm.reshape((1,))
v0918__00wu = (v0164_rpm**1)
v0918__00wu = (v0918__00wu*_00wt_coeff).reshape((1,))
v0164_rpm = v0164_rpm.reshape((1, 1))

# op _00gH_power_combination_eval
# LANG: T, density --> _00gI
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0245_density = v0245_density.reshape((1,))
v0440__00gI = (v0344_T**1)*(v0245_density**-1)
v0440__00gI = (v0440__00gI*_00gH_coeff).reshape((1,))
v0245_density = v0245_density.reshape((1, 1))

# op _00gP_power_combination_eval
# LANG: _00gO --> _00gQ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0447__00gQ = (v0446__00gO**2)
v0447__00gQ = (v0447__00gQ*_00gP_coeff).reshape((1,))

# op _00gZ_power_combination_eval
# LANG: _00gY --> _00g_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0452__00g_ = (v0451__00gY**1)
v0452__00g_ = (v0452__00g_*_00gZ_coeff).reshape((1,))

# op _00s2_linear_combination_eval
# LANG: _00r_, _00s1 --> _00s3
# SHAPES: (1, 4, 3, 2), (1, 4, 3, 2) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0772__00s3 = _00s2_constant+1*v0771__00r_+1*v0774__00s1

# op _00vA_indexed_passthrough_eval
# LANG: rel_obs_x_pos, rel_obs_y_pos, rel_obs_z_pos --> rel_obs_position
# SHAPES: (1, 1, 4), (1, 1, 4), (1, 1, 4) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0885_rel_obs_position__temp[i_v0871_rel_obs_x_pos__00vA_indexed_passthrough_eval] = v0871_rel_obs_x_pos.flatten()
v0885_rel_obs_position = v0885_rel_obs_position__temp.copy()
v0885_rel_obs_position__temp[i_v0879_rel_obs_y_pos__00vA_indexed_passthrough_eval] = v0879_rel_obs_y_pos.flatten()
v0885_rel_obs_position = v0885_rel_obs_position__temp.copy()
v0885_rel_obs_position__temp[i_v0883_rel_obs_z_pos__00vA_indexed_passthrough_eval] = v0883_rel_obs_z_pos.flatten()
v0885_rel_obs_position = v0885_rel_obs_position__temp.copy()

# op _00vF_linear_combination_eval
# LANG: _00vC, _00vE --> _00vG
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0887__00vG = _00vF_constant+1*v0886__00vC+1*v0888__00vE

# op _00vH_power_combination_eval
# LANG: rel_obs_z_pos --> _00vI
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0890__00vI = (v0883_rel_obs_z_pos**2)
v0890__00vI = (v0890__00vI*_00vH_coeff).reshape((1, 1, 4))

# op _00vO expand_array_eval
# LANG: thrust_dir --> _00vP
# SHAPES: (3,) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0893__00vP = np.einsum('b,ac->abc', v0806_thrust_dir.reshape((3,)) ,np.ones((1, 4))).reshape((1, 3, 4))

# op _00wM_power_combination_eval
# LANG: _00wL, dr --> _00wN
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0911__00wN = (v0910__00wL**1)*(v0813_dr**1)
v0911__00wN = (v0911__00wN*_00wM_coeff).reshape((1,))

# op _00wS expand_scalar_eval
# LANG: propeller_radius --> _00wT
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0915__00wT = np.empty((1, 4))
v0915__00wT.fill(v0791_propeller_radius.item())

# op _00wv_power_combination_eval
# LANG: _00wu --> _00ww
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0919__00ww = (v0918__00wu**1)
v0919__00ww = (v0919__00ww*_00wv_coeff).reshape((1,))

# op _00gR_power_combination_eval
# LANG: _00gI, _00gQ --> _00gS
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0441__00gS = (v0440__00gI**1)*(v0447__00gQ**-1)
v0441__00gS = (v0441__00gS*_00gR_coeff).reshape((1,))

# op _00h0_power_combination_eval
# LANG: _00g_ --> _00h1
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0453__00h1 = (v0452__00g_**4)
v0453__00h1 = (v0453__00h1*_00h0_coeff).reshape((1,))

# op _00jd_power_combination_eval
# LANG: rpm --> _00je
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0508__00je = (v0164_rpm**1)
v0508__00je = (v0508__00je*_00jd_coeff).reshape((1, 1))

# op _00s4_power_combination_eval
# LANG: _00s3 --> _00s5
# SHAPES: (1, 4, 3, 2) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0775__00s5 = (v0772__00s3**1)
v0775__00s5 = (v0775__00s5*_00s4_coeff).reshape((1, 4, 3, 2))

# op _00tt_power_combination_eval
# LANG: rpm --> _00tu
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0815__00tu = (v0164_rpm**1)
v0815__00tu = (v0815__00tu*_00tt_coeff).reshape((1, 1))

# op _00vJ_linear_combination_eval
# LANG: _00vG, _00vI --> _00vK
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0889__00vK = _00vJ_constant+1*v0887__00vG+1*v0890__00vI

# op _00vQ_tensor_dot_product_eval
# LANG: rel_obs_position, _00vP --> normal_proj
# SHAPES: (1, 3, 4), (1, 3, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0892_normal_proj = np.sum(v0885_rel_obs_position * v0893__00vP, axis=1)

# op _00wO expand_scalar_eval
# LANG: _00wN --> _00wP
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0912__00wP = np.empty((1, 4))
v0912__00wP.fill(v0911__00wN.item())

# op _00wU_power_combination_eval
# LANG: _00wT --> _00wV
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0916__00wV = (v0915__00wT**2)
v0916__00wV = (v0916__00wV*_00wU_coeff).reshape((1, 4))

# op _00wx_power_combination_eval
# LANG: _00ww --> _00wy
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0920__00wy = (v0919__00ww**1)
v0920__00wy = (v0920__00wy*_00wx_coeff).reshape((1,))

# op _00wz expand_scalar_eval
# LANG: propeller_radius --> _00wA
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0922__00wA = np.empty((1,))
v0922__00wA.fill(v0791_propeller_radius.item())

# op _00h2_power_combination_eval
# LANG: _00gS, _00h1 --> C_T
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0448_C_T = (v0441__00gS**1)*(v0453__00h1**-1)
v0448_C_T = (v0448_C_T*_00h2_coeff).reshape((1,))

# op _00jf_power_combination_eval
# LANG: _00je --> _00jg
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0509__00jg = (v0508__00je**1)
v0509__00jg = (v0509__00jg*_00jf_coeff).reshape((1, 1))

# op _00s6_log10_eval
# LANG: _00s5 --> _00s7
# SHAPES: (1, 4, 3, 2) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0776__00s7 = np.log10(v0775__00s5)

# op _00tv_power_combination_eval
# LANG: _00tu --> _00tw
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0816__00tw = (v0815__00tu**1)
v0816__00tw = (v0816__00tw*_00tv_coeff).reshape((1, 1))

# op _00vL_power_combination_eval
# LANG: _00vK --> rel_obs_dist
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0891_rel_obs_dist = (v0889__00vK**0.5)
v0891_rel_obs_dist = (v0891_rel_obs_dist*_00vL_coeff).reshape((1, 1, 4))

# op _00vW expand_array_eval
# LANG: normal_proj --> _00vX
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0894__00vX = np.einsum('ac,b->abc', v0892_normal_proj.reshape((1, 4)) ,np.ones((1,))).reshape((1, 1, 4))

# op _00wB_power_combination_eval
# LANG: _00wy, _00wA --> _00wC
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0921__00wC = (v0920__00wy**1)*(v0922__00wA**1)
v0921__00wC = (v0921__00wC*_00wB_coeff).reshape((1,))

# op _00wQ_power_combination_eval
# LANG: _00wP --> Ab
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0913_Ab = (v0912__00wP**1)
v0913_Ab = (v0913_Ab*_00wQ_coeff).reshape((1, 4))

# op _00wW_power_combination_eval
# LANG: _00wV --> _00wX
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0917__00wX = (v0916__00wV**1)
v0917__00wX = (v0917__00wX*_00wW_coeff).reshape((1, 4))

# op _00jh_power_combination_eval
# LANG: _00jg --> _00ji
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0510__00ji = (v0509__00jg**1)
v0510__00ji = (v0510__00ji*_00jh_coeff).reshape((1, 1))

# op _00s8_power_combination_eval
# LANG: _00s7 --> bladeSPL
# SHAPES: (1, 4, 3, 2) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0777_bladeSPL = (v0776__00s7**1)
v0777_bladeSPL = (v0777_bladeSPL*_00s8_coeff).reshape((1, 4, 3, 2))

# op _00tx_power_combination_eval
# LANG: _00tw --> _00ty
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0817__00ty = (v0816__00tw**1)
v0817__00ty = (v0817__00ty*_00tx_coeff).reshape((1, 1))

# op _00vY_power_combination_eval
# LANG: rel_obs_dist, _00vX --> _00vZ
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0895__00vZ = (v0894__00vX**1)*(v0891_rel_obs_dist**-1)
v0895__00vZ = (v0895__00vZ*_00vY_coeff).reshape((1, 1, 4))

# op _00wD expand_scalar_eval
# LANG: _00wC --> _00wE
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0923__00wE = np.empty((1, 4))
v0923__00wE.fill(v0921__00wC.item())

# op _00wG expand_scalar_eval
# LANG: CT --> _00wH
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0928__00wH = np.empty((1, 4))
v0928__00wH.fill(v0448_C_T.item())

# op _00wY_power_combination_eval
# LANG: Ab, _00wX --> sigma
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0914_sigma = (v0913_Ab**1)*(v0917__00wX**-1)
v0914_sigma = (v0914_sigma*_00wY_coeff).reshape((1, 4))

# op _00js_power_combination_eval
# LANG: _00ji --> _00jt
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0517__00jt = (v0510__00ji**2)
v0517__00jt = (v0517__00jt*_00js_coeff).reshape((1, 1))

# op _00jw_power_combination_eval
# LANG: _00ji --> _00jx
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0520__00jx = (v0510__00ji**2)
v0520__00jx = (v0520__00jx*_00jw_coeff).reshape((1, 1))

# op _00sa_power_combination_eval
# LANG: bladeSPL --> _00sb
# SHAPES: (1, 4, 3, 2) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0778__00sb = (v0777_bladeSPL**1)
v0778__00sb = (v0778__00sb*_00sa_coeff).reshape((1, 4, 3, 2))

# op _00tI_power_combination_eval
# LANG: _00ty --> _00tJ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0824__00tJ = (v0817__00ty**2)
v0824__00tJ = (v0824__00tJ*_00tI_coeff).reshape((1, 1))

# op _00tM_power_combination_eval
# LANG: _00ty --> _00tN
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0827__00tN = (v0817__00ty**2)
v0827__00tN = (v0827__00tN*_00tM_coeff).reshape((1, 1))

# op _00v__arcsin_eval
# LANG: _00vZ --> _00w0
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0896__00w0 = np.arcsin(v0895__00vZ)

# op _00w__power_combination_eval
# LANG: _00wE --> _00x0
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0924__00x0 = (v0923__00wE**3.68)
v0924__00x0 = (v0924__00x0*_00w__coeff).reshape((1, 4))

# op _00x1_power_combination_eval
# LANG: Ab --> _00x2
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0926__00x2 = (v0913_Ab**0.9)
v0926__00x2 = (v0926__00x2*_00x1_coeff).reshape((1, 4))

# op _00x5_power_combination_eval
# LANG: sigma, _00wH --> _00x6
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0929__00x6 = (v0928__00wH**1)*(v0914_sigma**-1)
v0929__00x6 = (v0929__00x6*_00x5_coeff).reshape((1, 4))

# op _00xh_power_combination_eval
# LANG: _00wE --> _00xi
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0941__00xi = (v0923__00wE**7.44)
v0941__00xi = (v0941__00xi*_00xh_coeff).reshape((1, 4))

# op _00xj_power_combination_eval
# LANG: Ab --> _00xk
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0943__00xk = (v0913_Ab**0.9)
v0943__00xk = (v0943__00xk*_00xj_coeff).reshape((1, 4))

# op _00xn_power_combination_eval
# LANG: sigma, _00wH --> _00xo
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0945__00xo = (v0928__00wH**1)*(v0914_sigma**-1)
v0945__00xo = (v0945__00xo*_00xn_coeff).reshape((1, 4))

# op _00ju_linear_combination_eval
# LANG: _00jt --> _00jv
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0518__00jv = _00ju_constant+1*v0517__00jt

# op _00jy_linear_combination_eval
# LANG: _00jx --> _00jz
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0521__00jz = _00jy_constant+1*v0520__00jx

# op _00sc_exp_a_eval
# LANG: _00sb --> _00sd
# SHAPES: (1, 4, 3, 2) --> (1, 4, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0779__00sd = _00sc_exp_a_eval_a**v0778__00sb

# op _00tK_linear_combination_eval
# LANG: _00tJ --> _00tL
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0825__00tL = _00tK_constant+1*v0824__00tJ

# op _00tO_linear_combination_eval
# LANG: _00tN --> _00tP
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0828__00tP = _00tO_constant+1*v0827__00tN

# op _00w7 reshape_eval
# LANG: _00w0 --> rel_angle_plane
# SHAPES: (1, 1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0897_rel_angle_plane = v0896__00w0.reshape((1, 4))

# op _00x3_power_combination_eval
# LANG: _00x0, _00x2 --> _00x4
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0925__00x4 = (v0924__00x0**1)*(v0926__00x2**1)
v0925__00x4 = (v0925__00x4*_00x3_coeff).reshape((1, 4))

# op _00x7_power_combination_eval
# LANG: _00x6 --> _00x8
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0930__00x8 = (v0929__00x6**1.6)
v0930__00x8 = (v0930__00x8*_00x7_coeff).reshape((1, 4))

# op _00xL_linear_combination_eval
# LANG: Ab --> _00xM
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0951__00xM = _00xL_constant+1*v0913_Ab

# op _00xl_power_combination_eval
# LANG: _00xi, _00xk --> _00xm
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0942__00xm = (v0941__00xi**1)*(v0943__00xk**1)
v0942__00xm = (v0942__00xm*_00xl_coeff).reshape((1, 4))

# op _00xp_power_combination_eval
# LANG: _00xo --> _00xq
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0946__00xq = (v0945__00xo**1.6)
v0946__00xq = (v0946__00xq*_00xp_coeff).reshape((1, 4))

# op _00xz_linear_combination_eval
# LANG: Ab --> _00xA
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0935__00xA = _00xz_constant+-1*v0913_Ab

# op _00jA_power_combination_eval
# LANG: _00jv, _00jz --> _00jB
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0519__00jB = (v0518__00jv**1)*(v0521__00jz**1)
v0519__00jB = (v0519__00jB*_00jA_coeff).reshape((1, 1))

# op _00jo_power_combination_eval
# LANG: _00ji --> _00jp
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0514__00jp = (v0510__00ji**2)
v0514__00jp = (v0514__00jp*_00jo_coeff).reshape((1, 1))

# op _00se_single_tensor_sum_with_axis_eval
# LANG: _00sd --> _00sf
# SHAPES: (1, 4, 3, 2) --> (1, 4, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0780__00sf = np.sum(v0779__00sd, axis = (3,)).reshape((1, 4, 3))

# op _00tE_power_combination_eval
# LANG: _00ty --> _00tF
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0821__00tF = (v0817__00ty**2)
v0821__00tF = (v0821__00tF*_00tE_coeff).reshape((1, 1))

# op _00tQ_power_combination_eval
# LANG: _00tL, _00tP --> _00tR
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0826__00tR = (v0825__00tL**1)*(v0828__00tP**1)
v0826__00tR = (v0826__00tR*_00tQ_coeff).reshape((1, 1))

# op _00x9_power_combination_eval
# LANG: _00x4, _00x8 --> _00xa
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0927__00xa = (v0925__00x4**1)*(v0930__00x8**1)
v0927__00xa = (v0927__00xa*_00x9_coeff).reshape((1, 4))

# op _00xB_power_combination_eval
# LANG: _00xA --> _00xC
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0936__00xC = (v0935__00xA**1)
v0936__00xC = (v0936__00xC*_00xB_coeff).reshape((1, 4))

# op _00xN_power_combination_eval
# LANG: _00xM --> _00xO
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0952__00xO = (v0951__00xM**1)
v0952__00xO = (v0952__00xO*_00xN_coeff).reshape((1, 4))

# op _00xr_power_combination_eval
# LANG: _00xm, _00xq --> _00xs
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0944__00xs = (v0942__00xm**1)*(v0946__00xq**1)
v0944__00xs = (v0944__00xs*_00xr_coeff).reshape((1, 4))

# op _00yn_power_combination_eval
# LANG: rel_angle_plane --> _00yo
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0968__00yo = (v0897_rel_angle_plane**2)
v0968__00yo = (v0968__00yo*_00yn_coeff).reshape((1, 4))

# op _00dE_power_combination_eval
# LANG: _radius --> _00dF
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0345__00dF = (v0217__radius**2)
v0345__00dF = (v0345__00dF*_00dE_coeff).reshape((1, 40, 30))

# op _00jC_power_combination_eval
# LANG: _00jB --> _00jD
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0522__00jD = (v0519__00jB**0.5)
v0522__00jD = (v0522__00jD*_00jC_coeff).reshape((1, 1))

# op _00jG_power_combination_eval
# LANG: _00ji --> _00jH
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0524__00jH = (v0510__00ji**2)
v0524__00jH = (v0524__00jH*_00jG_coeff).reshape((1, 1))

# op _00jq_linear_combination_eval
# LANG: _00jp --> _00jr
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0515__00jr = _00jq_constant+1*v0514__00jp

# op _00sg_log10_eval
# LANG: _00sf --> _00sh
# SHAPES: (1, 4, 3) --> (1, 4, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0781__00sh = np.log10(v0780__00sf)

# op _00tG_linear_combination_eval
# LANG: _00tF --> _00tH
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0822__00tH = _00tG_constant+1*v0821__00tF

# op _00tS_power_combination_eval
# LANG: _00tR --> _00tT
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0829__00tT = (v0826__00tR**0.5)
v0829__00tT = (v0829__00tT*_00tS_coeff).reshape((1, 1))

# op _00tW_power_combination_eval
# LANG: _00ty --> _00tX
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0831__00tX = (v0817__00ty**2)
v0831__00tX = (v0831__00tX*_00tW_coeff).reshape((1, 1))

# op _00xD_tanh_eval
# LANG: _00xC --> _00xE
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0937__00xE = np.tanh(v0936__00xC)

# op _00xP_tanh_eval
# LANG: _00xO --> _00xQ
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0953__00xQ = np.tanh(v0952__00xO)

# op _00xb_log10_eval
# LANG: _00xa --> _00xc
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0931__00xc = np.log10(v0927__00xa)

# op _00xt_log10_eval
# LANG: _00xs --> _00xu
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0947__00xu = np.log10(v0944__00xs)

# op _00yp_power_combination_eval
# LANG: _00yo --> _00yq
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0969__00yq = (v0968__00yo**0.5)
v0969__00yq = (v0969__00yq*_00yp_coeff).reshape((1, 4))

# op _00dG_power_combination_eval
# LANG: _00dF --> _00dH
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0346__00dH = (v0345__00dF**1)
v0346__00dH = (v0346__00dH*_00dG_coeff).reshape((1, 40, 30))

# op _00jE_power_combination_eval
# LANG: _00jr, _00jD --> _00jF
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0516__00jF = (v0515__00jr**1)*(v0522__00jD**1)
v0516__00jF = (v0516__00jF*_00jE_coeff).reshape((1, 1))

# op _00jI_linear_combination_eval
# LANG: _00jH --> _00jJ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0525__00jJ = _00jI_constant+1*v0524__00jH

# op _00jk_power_combination_eval
# LANG: _00ji --> _00jl
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0511__00jl = (v0510__00ji**4)
v0511__00jl = (v0511__00jl*_00jk_coeff).reshape((1, 1))

# op _00si_power_combination_eval
# LANG: _00sh --> _00sj
# SHAPES: (1, 4, 3) --> (1, 4, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0782__00sj = (v0781__00sh**1)
v0782__00sj = (v0782__00sj*_00si_coeff).reshape((1, 4, 3))

# op _00tA_power_combination_eval
# LANG: _00ty --> _00tB
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0818__00tB = (v0817__00ty**4)
v0818__00tB = (v0818__00tB*_00tA_coeff).reshape((1, 1))

# op _00tU_power_combination_eval
# LANG: _00tH, _00tT --> _00tV
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0823__00tV = (v0822__00tH**1)*(v0829__00tT**1)
v0823__00tV = (v0823__00tV*_00tU_coeff).reshape((1, 1))

# op _00tY_linear_combination_eval
# LANG: _00tX --> _00tZ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0832__00tZ = _00tY_constant+1*v0831__00tX

# op _00xF_power_combination_eval
# LANG: _00xE --> _00xG
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0938__00xG = (v0937__00xE**1)
v0938__00xG = (v0938__00xG*_00xF_coeff).reshape((1, 4))

# op _00xR_power_combination_eval
# LANG: _00xQ --> _00xS
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0954__00xS = (v0953__00xQ**1)
v0954__00xS = (v0954__00xS*_00xR_coeff).reshape((1, 4))

# op _00xZ_power_combination_eval
# LANG: propeller_radius --> _00x_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0964__00x_ = (v0791_propeller_radius**1)
v0964__00x_ = (v0964__00x_*_00xZ_coeff).reshape((1,))

# op _00xd_power_combination_eval
# LANG: _00xc --> _00xe
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0932__00xe = (v0931__00xc**1)
v0932__00xe = (v0932__00xe*_00xd_coeff).reshape((1, 4))

# op _00xv_power_combination_eval
# LANG: _00xu --> _00xw
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0948__00xw = (v0947__00xu**1)
v0948__00xw = (v0948__00xw*_00xv_coeff).reshape((1, 4))

# op _00y9_power_combination_eval
# LANG: rel_angle_plane --> _00ya
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0957__00ya = (v0897_rel_angle_plane**2.0)
v0957__00ya = (v0957__00ya*_00y9_coeff).reshape((1, 4))

# op _00yr_sin_eval
# LANG: _00yq --> _00ys
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0970__00ys = np.sin(v0969__00yq)

# op _00dI_power_combination_eval
# LANG: _00bz, _00dH --> _00dJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0347__00dJ = (v0346__00dH**1)*(v0323__00bz**1)
v0347__00dJ = (v0347__00dJ*_00dI_coeff).reshape((1, 40, 30))

# op _00jK_power_combination_eval
# LANG: _00jF, _00jJ --> _00jL
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0523__00jL = (v0516__00jF**1)*(v0525__00jJ**1)
v0523__00jL = (v0523__00jL*_00jK_coeff).reshape((1, 1))

# op _00jm_power_combination_eval
# LANG: _00jl --> _00jn
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0512__00jn = (v0511__00jl**1)
v0512__00jn = (v0512__00jn*_00jm_coeff).reshape((1, 1))

# op _00sk_power_combination_eval
# LANG: _00sj --> _00sl
# SHAPES: (1, 4, 3) --> (1, 4, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0783__00sl = (v0782__00sj**1)
v0783__00sl = (v0783__00sl*_00sk_coeff).reshape((1, 4, 3))

# op _00tC_power_combination_eval
# LANG: _00tB --> _00tD
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0819__00tD = (v0818__00tB**1)
v0819__00tD = (v0819__00tD*_00tC_coeff).reshape((1, 1))

# op _00t__power_combination_eval
# LANG: _00tV, _00tZ --> _00u0
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0830__00u0 = (v0823__00tV**1)*(v0832__00tZ**1)
v0830__00u0 = (v0830__00u0*_00t__coeff).reshape((1, 1))

# op _00xH_linear_combination_eval
# LANG: _00xG --> _00xI
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0939__00xI = _00xH_constant+1*v0938__00xG

# op _00xT_linear_combination_eval
# LANG: _00xS --> _00xU
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0955__00xU = _00xT_constant+1*v0954__00xS

# op _00xf_linear_combination_eval
# LANG: _00xe --> _00xg
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0933__00xg = _00xf_constant+1*v0932__00xe

# op _00xx_linear_combination_eval
# LANG: _00xw --> _00xy
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0949__00xy = _00xx_constant+1*v0948__00xw

# op _00y0 expand_scalar_eval
# LANG: _00x_ --> _00y1
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0965__00y1 = np.empty((1, 4))
v0965__00y1.fill(v0964__00x_.item())

# op _00y3 reshape_eval
# LANG: rel_obs_dist --> _00y4
# SHAPES: (1, 1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0962__00y4 = v0891_rel_obs_dist.reshape((1, 4))

# op _00yb_power_combination_eval
# LANG: _00ya --> _00yc
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0958__00yc = (v0957__00ya**0.5)
v0958__00yc = (v0958__00yc*_00yb_coeff).reshape((1, 4))

# op _00yt_linear_combination_eval
# LANG: _00ys --> _00yu
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0971__00yu = _00yt_constant+-1*v0970__00ys

# op _00dK_power_combination_eval
# LANG: _ux, _00dJ --> _00dL
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0348__00dL = (v0347__00dJ**1)*(v0282__ux**1)
v0348__00dL = (v0348__00dL*_00dK_coeff).reshape((1, 40, 30))

# op _00jM_power_combination_eval
# LANG: _00jn, _00jL --> _00jN
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0513__00jN = (v0512__00jn**1)*(v0523__00jL**-1)
v0513__00jN = (v0513__00jN*_00jM_coeff).reshape((1, 1))

# op _00sm_exp_a_eval
# LANG: _00sl --> _00sn
# SHAPES: (1, 4, 3) --> (1, 4, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0784__00sn = _00sm_exp_a_eval_a**v0783__00sl

# op _00u1_power_combination_eval
# LANG: _00tD, _00u0 --> _00u2
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0820__00u2 = (v0819__00tD**1)*(v0830__00u0**-1)
v0820__00u2 = (v0820__00u2*_00u1_coeff).reshape((1, 1))

# op _00xJ_power_combination_eval
# LANG: _00xg, _00xI --> _00xK
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0934__00xK = (v0933__00xg**1)*(v0939__00xI**1)
v0934__00xK = (v0934__00xK*_00xJ_coeff).reshape((1, 4))

# op _00xV_power_combination_eval
# LANG: _00xy, _00xU --> _00xW
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0950__00xW = (v0949__00xy**1)*(v0955__00xU**1)
v0950__00xW = (v0950__00xW*_00xV_coeff).reshape((1, 4))

# op _00yd_sin_eval
# LANG: _00yc --> _00ye
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0959__00ye = np.sin(v0958__00yc)

# op _00yj_power_combination_eval
# LANG: _00y4, _00y1 --> _00yk
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0963__00yk = (v0962__00y4**1)*(v0965__00y1**-1)
v0963__00yk = (v0963__00yk*_00yj_coeff).reshape((1, 4))

# op _00yv_power_combination_eval
# LANG: _00yu --> _00yw
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0972__00yw = (v0971__00yu**1)
v0972__00yw = (v0972__00yw*_00yv_coeff).reshape((1, 4))

# op _00dM_power_combination_eval
# LANG: _ut, _00dL --> _00dN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0349__00dN = (v0348__00dL**1)*(v0314__ut**1)
v0349__00dN = (v0349__00dN*_00dM_coeff).reshape((1, 40, 30))

# op _00el_power_combination_eval
# LANG: _ut --> _00em
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0417__00em = (v0314__ut**1)
v0417__00em = (v0417__00em*_00el_coeff).reshape((1, 40, 30))

# op _00jO_log10_eval
# LANG: _00jN --> _00jP
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0526__00jP = np.log10(v0513__00jN)

# op _00jS_log10_eval
# LANG: RA_1000 --> _00jT
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0530__00jT = np.log10(v0529_RA_1000)

# op _00so_single_tensor_sum_with_axis_eval
# LANG: _00sn --> _00sp
# SHAPES: (1, 4, 3) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0785__00sp = np.sum(v0784__00sn, axis = (2,)).reshape((1, 4))

# op _00u3_log10_eval
# LANG: _00u2 --> _00u4
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0833__00u4 = np.log10(v0820__00u2)

# op _00u7_log10_eval
# LANG: RA_1000 --> _00u8
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0837__00u8 = np.log10(v0836_RA_1000)

# op _00xX_linear_combination_eval
# LANG: _00xK, _00xW --> _00xY
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0940__00xY = _00xX_constant+1*v0934__00xK+1*v0950__00xW

# op _00yf_power_combination_eval
# LANG: _00ye --> _00yg
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0960__00yg = (v0959__00ye**0.031)
v0960__00yg = (v0960__00yg*_00yf_coeff).reshape((1, 4))

# op _00yl_log10_eval
# LANG: _00yk --> _00ym
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0966__00ym = np.log10(v0963__00yk)

# op _00yx_linear_combination_eval
# LANG: _00yw --> _00yy
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0973__00yy = _00yx_constant+1*v0972__00yw

# op _00dO_power_combination_eval
# LANG: _00dN, prandtl_loss_factor --> _00dP
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0350__00dP = (v0349__00dN**1)*(v0267_prandtl_loss_factor**1)
v0350__00dP = (v0350__00dP*_00dO_coeff).reshape((1, 40, 30))

# op _00d__power_combination_eval
# LANG: _ut --> _00e0
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0370__00e0 = (v0314__ut**1)
v0370__00e0 = (v0370__00e0*_00d__coeff).reshape((1, 40, 30))

# op _00ed_power_combination_eval
# LANG: _00bX --> _00ee
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0410__00ee = (v0292__00bX**1)
v0410__00ee = (v0410__00ee*_00ed_coeff).reshape((1, 40, 30))

# op _00en_linear_combination_eval
# LANG: _00em, _tangential_inflow_velocity --> _00eo
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0416__00eo = _00en_constant+1*v0234__tangential_inflow_velocity+-1*v0417__00em

# op _00jQ_power_combination_eval
# LANG: _00jP --> _00jR
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0527__00jR = (v0526__00jP**1)
v0527__00jR = (v0527__00jR*_00jQ_coeff).reshape((1, 1))

# op _00jU_power_combination_eval
# LANG: _00jT --> _00jV
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0531__00jV = (v0530__00jT**1)
v0531__00jV = (v0531__00jV*_00jU_coeff).reshape((1, 1))

# op _00sq_log10_eval
# LANG: _00sp --> _00sr
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0786__00sr = np.log10(v0785__00sp)

# op _00u5_power_combination_eval
# LANG: _00u4 --> _00u6
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0834__00u6 = (v0833__00u4**1)
v0834__00u6 = (v0834__00u6*_00u5_coeff).reshape((1, 1))

# op _00u9_power_combination_eval
# LANG: _00u8 --> _00ua
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0838__00ua = (v0837__00u8**1)
v0838__00ua = (v0838__00ua*_00u9_coeff).reshape((1, 1))

# op _00yh_power_combination_eval
# LANG: _00xY, _00yg --> _00yi
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0956__00yi = (v0940__00xY**1)*(v0960__00yg**1)
v0956__00yi = (v0956__00yi*_00yh_coeff).reshape((1, 4))

# op _00yz_power_combination_eval
# LANG: _00ym, _00yy --> _00yA
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0967__00yA = (v0966__00ym**1)*(v0973__00yy**1)
v0967__00yA = (v0967__00yA*_00yz_coeff).reshape((1, 4))

# op _00bY_cos_eval
# LANG: phi_distribution --> _00bZ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0331__00bZ = np.cos(v0254_phi_distribution)

# op _00c1_sin_eval
# LANG: phi_distribution --> _00c2
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0398__00c2 = np.sin(v0254_phi_distribution)

# op _00dQ_power_combination_eval
# LANG: _00dP, _dr --> _local_torque
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0351__local_torque = (v0350__00dP**1)*(v0205__dr**1)
v0351__local_torque = (v0351__local_torque*_00dQ_coeff).reshape((1, 40, 30))

# op _00dS_power_combination_eval
# LANG: _00bN --> _00dT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0363__00dT = (v0299__00bN**1)
v0363__00dT = (v0363__00dT*_00dS_coeff).reshape((1, 40, 30))

# op _00e1_linear_combination_eval
# LANG: _00e0, _tangential_inflow_velocity --> _00e2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0369__00e2 = _00e1_constant+1*v0234__tangential_inflow_velocity+-1*v0370__00e0

# op _00ef_power_combination_eval
# LANG: _00ee --> _00eg
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0411__00eg = (v0410__00ee**1)
v0411__00eg = (v0411__00eg*_00ef_coeff).reshape((1, 40, 30))

# op _00ej_power_combination_eval
# LANG: _ux_2 --> _00ek
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0414__00ek = (v0295__ux_2**2)
v0414__00ek = (v0414__00ek*_00ej_coeff).reshape((1, 40, 30))

# op _00ep_power_combination_eval
# LANG: _00eo --> _00eq
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0418__00eq = (v0416__00eo**2)
v0418__00eq = (v0418__00eq*_00ep_coeff).reshape((1, 40, 30))

# op _00fW_power_combination_eval
# LANG: _ut --> _00fX
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0390__00fX = (v0314__ut**1)
v0390__00fX = (v0390__00fX*_00fW_coeff).reshape((1, 40, 30))

# op _00gf_power_combination_eval
# LANG: _ux, _tangential_inflow_velocity --> _00gg
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0427__00gg = (v0234__tangential_inflow_velocity**1)*(v0282__ux**1)
v0427__00gg = (v0427__00gg*_00gf_coeff).reshape((1, 40, 30))

# op _00gj_power_combination_eval
# LANG: _axial_inflow_velocity --> _00gk
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0430__00gk = (v0224__axial_inflow_velocity**1)
v0430__00gk = (v0430__00gk*_00gj_coeff).reshape((1, 40, 30))

# op _00gl_power_combination_eval
# LANG: _ux --> _00gm
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0432__00gm = (v0282__ux**2)
v0432__00gm = (v0432__00gm*_00gl_coeff).reshape((1, 40, 30))

# op _00gr_power_combination_eval
# LANG: _axial_inflow_velocity --> _00gs
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0434__00gs = (v0224__axial_inflow_velocity**2)
v0434__00gs = (v0434__00gs*_00gr_coeff).reshape((1, 40, 30))

# op _00h8_single_tensor_sum_with_axis_eval
# LANG: _00br --> _00h9
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0456__00h9 = np.sum(v0443__00br, axis = (1, 2)).reshape((1,))

# op _00hi_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00hj
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0461__00hj = np.sum(v0204__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00jW_linear_combination_eval
# LANG: _00jR, _00jV --> _00jX
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0528__00jX = _00jW_constant+1*v0527__00jR+-1*v0531__00jV

# op _00ss_power_combination_eval
# LANG: _00sr --> rotor_disk_tonal_spl
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0787_rotor_disk_tonal_spl = (v0786__00sr**1)
v0787_rotor_disk_tonal_spl = (v0787_rotor_disk_tonal_spl*_00ss_coeff).reshape((1, 4))

# op _00ub_linear_combination_eval
# LANG: _00u6, _00ua --> _00uc
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0835__00uc = _00ub_constant+1*v0834__00u6+-1*v0838__00ua

# op _00yB_linear_combination_eval
# LANG: _00yi, _00yA --> rotor_disk_broadband_spl
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.gl_spl_model
v0961_rotor_disk_broadband_spl = _00yB_constant+1*v0956__00yi+-1*v0967__00yA

# op _00b__power_combination_eval
# LANG: _00bZ, Cl --> _00c0
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0330__00c0 = (v0256_Cl**1)*(v0331__00bZ**1)
v0330__00c0 = (v0330__00c0*_00b__coeff).reshape((1, 40, 30))

# op _00c3_power_combination_eval
# LANG: _00c2, Cl --> _00c4
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0397__00c4 = (v0256_Cl**1)*(v0398__00c2**1)
v0397__00c4 = (v0397__00c4*_00c3_coeff).reshape((1, 40, 30))

# op _00dU_power_combination_eval
# LANG: _00dT --> _00dV
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0364__00dV = (v0363__00dT**1)
v0364__00dV = (v0364__00dV*_00dU_coeff).reshape((1, 40, 30))

# op _00dY_power_combination_eval
# LANG: _ux_2 --> _00dZ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0367__00dZ = (v0295__ux_2**2)
v0367__00dZ = (v0367__00dZ*_00dY_coeff).reshape((1, 40, 30))

# op _00e3_power_combination_eval
# LANG: _00e2 --> _00e4
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0371__00e4 = (v0369__00e2**2)
v0371__00e4 = (v0371__00e4*_00e3_coeff).reshape((1, 40, 30))

# op _00eh_power_combination_eval
# LANG: _00bz, _00eg --> _00ei
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0412__00ei = (v0411__00eg**1)*(v0323__00bz**1)
v0412__00ei = (v0412__00ei*_00eh_coeff).reshape((1, 40, 30))

# op _00er_linear_combination_eval
# LANG: _00ek, _00eq --> _00es
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0415__00es = _00er_constant+1*v0414__00ek+1*v0418__00eq

# op _00f4_power_combination_eval
# LANG: _ut --> _00f5
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0339__00f5 = (v0314__ut**1)
v0339__00f5 = (v0339__00f5*_00f4_coeff).reshape((1, 40, 30))

# op _00fQ_single_tensor_sum_with_axis_eval
# LANG: _local_torque --> _00fR
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0352__00fR = np.sum(v0351__local_torque, axis = (1, 2)).reshape((1,))

# op _00fU_power_combination_eval
# LANG: _00bz --> _00fV
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0387__00fV = (v0323__00bz**1)
v0387__00fV = (v0387__00fV*_00fU_coeff).reshape((1, 40, 30))

# op _00fY_linear_combination_eval
# LANG: _00fX, _tangential_inflow_velocity --> _00fZ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0389__00fZ = _00fY_constant+1*v0234__tangential_inflow_velocity+-1*v0390__00fX

# op _00fq_power_combination_eval
# LANG: _ut --> _00fr
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0406__00fr = (v0314__ut**1)
v0406__00fr = (v0406__00fr*_00fq_coeff).reshape((1, 40, 30))

# op _00gh_power_combination_eval
# LANG: _ut, _00gg --> _00gi
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0428__00gi = (v0427__00gg**1)*(v0314__ut**1)
v0428__00gi = (v0428__00gi*_00gh_coeff).reshape((1, 40, 30))

# op _00gn_power_combination_eval
# LANG: _00gk, _00gm --> _00go
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0431__00go = (v0430__00gk**1)*(v0432__00gm**1)
v0431__00go = (v0431__00go*_00gn_coeff).reshape((1, 40, 30))

# op _00gt_power_combination_eval
# LANG: _00gs --> _00gu
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0435__00gu = (v0434__00gs**1)
v0435__00gu = (v0435__00gu*_00gt_coeff).reshape((1, 40, 30))

# op _00ha_power_combination_eval
# LANG: _00h9 --> _00hb
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0457__00hb = (v0456__00h9**1)
v0457__00hb = (v0457__00hb*_00ha_coeff).reshape((1,))

# op _00hk_power_combination_eval
# LANG: _00hj --> _00hl
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0462__00hl = (v0461__00hj**1)
v0462__00hl = (v0462__00hl*_00hk_coeff).reshape((1,))

# op _00hw_power_combination_eval
# LANG: _00br, _axial_inflow_velocity --> _00hx
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0468__00hx = (v0224__axial_inflow_velocity**1)*(v0443__00br**-1)
v0468__00hx = (v0468__00hx*_00hw_coeff).reshape((1, 40, 30))

# op _00hy_power_combination_eval
# LANG: _rotor_radius --> _00hz
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0470__00hz = (v0204__rotor_radius**1)
v0470__00hz = (v0470__00hz*_00hy_coeff).reshape((1, 40, 30))

# op _00jY reshape_eval
# LANG: _00jX --> _00jZ
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0532__00jZ = v0528__00jX.reshape((1,))

# op _00ud reshape_eval
# LANG: _00uc --> _00ue
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0839__00ue = v0835__00uc.reshape((1,))

# op _00yG expand_array_eval
# LANG: rotor_disk_tonal_spl --> _00yH
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0974__00yH = np.einsum('bc,a->abc', v0787_rotor_disk_tonal_spl.reshape((1, 4)) ,np.ones((1,))).reshape((1, 1, 4))

# op _00yK expand_array_eval
# LANG: rotor_disk_broadband_spl --> _00yL
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0976__00yL = np.einsum('bc,a->abc', v0961_rotor_disk_broadband_spl.reshape((1, 4)) ,np.ones((1,))).reshape((1, 1, 4))

# op _005e_decompose_eval
# LANG: T --> _005f
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0149__005f = ((v0344_T.flatten())[src_indices__005f__005e]).reshape((1,))

# op _00dW_power_combination_eval
# LANG: _00bz, _00dV --> _00dX
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0365__00dX = (v0364__00dV**1)*(v0323__00bz**1)
v0365__00dX = (v0365__00dX*_00dW_coeff).reshape((1, 40, 30))

# op _00e5_linear_combination_eval
# LANG: _00dZ, _00e4 --> _00e6
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0368__00e6 = _00e5_constant+1*v0367__00dZ+1*v0371__00e4

# op _00eX_power_combination_eval
# LANG: _00c0 --> _00eY
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0332__00eY = (v0330__00c0**1)
v0332__00eY = (v0332__00eY*_00eX_coeff).reshape((1, 40, 30))

# op _00et_power_combination_eval
# LANG: _00ei, _00es --> _00eu
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0413__00eu = (v0412__00ei**1)*(v0415__00es**1)
v0413__00eu = (v0413__00eu*_00et_coeff).reshape((1, 40, 30))

# op _00f6_linear_combination_eval
# LANG: _00f5, _tangential_inflow_velocity --> _00f7
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0338__00f7 = _00f6_constant+1*v0234__tangential_inflow_velocity+-1*v0339__00f5

# op _00fS_power_combination_eval
# LANG: _00fR --> total_torque
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0353_total_torque = (v0352__00fR**1)
v0353_total_torque = (v0353_total_torque*_00fS_coeff).reshape((1,))

# op _00f__power_combination_eval
# LANG: _00fV, _00fZ --> _00g0
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0388__00g0 = (v0387__00fV**1)*(v0389__00fZ**1)
v0388__00g0 = (v0388__00g0*_00f__coeff).reshape((1, 40, 30))

# op _00fi_power_combination_eval
# LANG: _00c4 --> _00fj
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0399__00fj = (v0397__00c4**1)
v0399__00fj = (v0399__00fj*_00fi_coeff).reshape((1, 40, 30))

# op _00fs_linear_combination_eval
# LANG: _00fr, _tangential_inflow_velocity --> _00ft
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0405__00ft = _00fs_constant+1*v0234__tangential_inflow_velocity+-1*v0406__00fr

# op _00gb_power_combination_eval
# LANG: _radius --> _00gc
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0424__00gc = (v0217__radius**1)
v0424__00gc = (v0424__00gc*_00gb_coeff).reshape((1, 40, 30))

# op _00gp_linear_combination_eval
# LANG: _00gi, _00go --> _00gq
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0429__00gq = _00gp_constant+1*v0428__00gi+-1*v0431__00go

# op _00gv_power_combination_eval
# LANG: _ux, _00gu --> _00gw
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0436__00gw = (v0435__00gu**1)*(v0282__ux**1)
v0436__00gw = (v0436__00gw*_00gv_coeff).reshape((1, 40, 30))

# op _00hA_power_combination_eval
# LANG: _00hx, _00hz --> _00hB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0469__00hB = (v0468__00hx**1)*(v0470__00hz**-1)
v0469__00hB = (v0469__00hB*_00hA_coeff).reshape((1, 40, 30))

# op _00hc_power_combination_eval
# LANG: _00hb --> _00hd
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0458__00hd = (v0457__00hb**1)
v0458__00hd = (v0458__00hd*_00hc_coeff).reshape((1,))

# op _00hm_power_combination_eval
# LANG: _00hl --> _00hn
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0463__00hn = (v0462__00hl**1)
v0463__00hn = (v0463__00hn*_00hm_coeff).reshape((1,))

# op _00j_ expand_scalar_eval
# LANG: _00jZ --> _00k0
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0533__00k0 = np.empty((1, 4))
v0533__00k0.fill(v0532__00jZ.item())

# op _00m6 expand_array_eval
# LANG: thrust_dir --> _00m7
# SHAPES: (3,) --> (1, 3, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0603__00m7 = np.einsum('b,ac->abc', v0494_thrust_dir.reshape((3,)) ,np.ones((1, 4))).reshape((1, 3, 4))

# op _00uf expand_scalar_eval
# LANG: _00ue --> _00ug
# SHAPES: (1,) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0840__00ug = np.empty((1, 4))
v0840__00ug.fill(v0839__00ue.item())

# op _00yI_indexed_passthrough_eval
# LANG: _00yH, _00yL --> noise_components
# SHAPES: (1, 1, 4), (1, 1, 4) --> (2, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0975_noise_components__temp[i_v0974__00yH__00yI_indexed_passthrough_eval] = v0974__00yH.flatten()
v0975_noise_components = v0975_noise_components__temp.copy()
v0975_noise_components__temp[i_v0976__00yL__00yI_indexed_passthrough_eval] = v0976__00yL.flatten()
v0975_noise_components = v0975_noise_components__temp.copy()

# op _002b_power_combination_eval
# LANG: cruise_temperature --> _002c
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0101__002c = (v098_cruise_temperature**1)
v0101__002c = (v0101__002c*_002b_coeff).reshape((1,))

# op _005g reshape_eval
# LANG: _005f --> _005h
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0150__005h = v0149__005f.reshape((1, 1))

# op _005i_decompose_eval
# LANG: thrust_vector --> _005j, _005p, _005u
# SHAPES: (1, 3) --> (1, 1), (1, 1), (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0152__005j = ((v0134_thrust_vector.flatten())[src_indices__005j__005i]).reshape((1, 1))
v0153__005p = ((v0134_thrust_vector.flatten())[src_indices__005p__005i]).reshape((1, 1))
v0154__005u = ((v0134_thrust_vector.flatten())[src_indices__005u__005i]).reshape((1, 1))

# op _005n reshape_eval
# LANG: _005f --> _005o
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0156__005o = v0149__005f.reshape((1, 1))

# op _005s reshape_eval
# LANG: _005f --> _005t
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0158__005t = v0149__005f.reshape((1, 1))

# op _008J_power_combination_eval
# LANG: temperature --> _008K
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0252__008K = (v0240_temperature**1)
v0252__008K = (v0252__008K*_008J_coeff).reshape((1, 1))

# op _00dq_power_combination_eval
# LANG: _angular_speed --> _00dr
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0357__00dr = (v0216__angular_speed**1)
v0357__00dr = (v0357__00dr*_00dq_coeff).reshape((1, 40, 30))

# op _00e7_power_combination_eval
# LANG: _00dX, _00e6 --> _00e8
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0366__00e8 = (v0365__00dX**1)*(v0368__00e6**1)
v0366__00e8 = (v0366__00e8*_00e7_coeff).reshape((1, 40, 30))

# op _00eZ_power_combination_eval
# LANG: _00eY --> _00e_
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0333__00e_ = (v0332__00eY**1)
v0333__00e_ = (v0333__00e_*_00eZ_coeff).reshape((1, 40, 30))

# op _00ev_power_combination_eval
# LANG: _00eu, _chord --> _00ew
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0419__00ew = (v0413__00eu**1)*(v0212__chord**1)
v0419__00ew = (v0419__00ew*_00ev_coeff).reshape((1, 40, 30))

# op _00f2_power_combination_eval
# LANG: _ux_2 --> _00f3
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0336__00f3 = (v0295__ux_2**2)
v0336__00f3 = (v0336__00f3*_00f2_coeff).reshape((1, 40, 30))

# op _00f8_power_combination_eval
# LANG: _00f7 --> _00f9
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0340__00f9 = (v0338__00f7**2)
v0340__00f9 = (v0340__00f9*_00f8_coeff).reshape((1, 40, 30))

# op _00fk_power_combination_eval
# LANG: _00fj --> _00fl
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0400__00fl = (v0399__00fj**1)
v0400__00fl = (v0400__00fl*_00fk_coeff).reshape((1, 40, 30))

# op _00fo_power_combination_eval
# LANG: _ux_2 --> _00fp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0403__00fp = (v0295__ux_2**2)
v0403__00fp = (v0403__00fp*_00fo_coeff).reshape((1, 40, 30))

# op _00fu_power_combination_eval
# LANG: _00ft --> _00fv
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0407__00fv = (v0405__00ft**2)
v0407__00fv = (v0407__00fv*_00fu_coeff).reshape((1, 40, 30))

# op _00g1_power_combination_eval
# LANG: _ut, _00g0 --> _00g2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0391__00g2 = (v0388__00g0**1)*(v0314__ut**1)
v0391__00g2 = (v0391__00g2*_00g1_coeff).reshape((1, 40, 30))

# op _00gd_power_combination_eval
# LANG: _00gc --> _00ge
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0425__00ge = (v0424__00gc**1)
v0425__00ge = (v0425__00ge*_00gd_coeff).reshape((1, 40, 30))

# op _00gx_linear_combination_eval
# LANG: _00gq, _00gw --> _00gy
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0433__00gy = _00gx_constant+1*v0429__00gq+1*v0436__00gw

# op _00h6_power_combination_eval
# LANG: total_torque, density --> _00h7
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0245_density = v0245_density.reshape((1,))
v0454__00h7 = (v0353_total_torque**1)*(v0245_density**-1)
v0454__00h7 = (v0454__00h7*_00h6_coeff).reshape((1,))
v0245_density = v0245_density.reshape((1, 1))

# op _00hC_single_tensor_sum_with_axis_eval
# LANG: _00hB --> _00hD
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0471__00hD = np.sum(v0469__00hB, axis = (1, 2)).reshape((1,))

# op _00he_power_combination_eval
# LANG: _00hd --> _00hf
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0459__00hf = (v0458__00hd**2)
v0459__00hf = (v0459__00hf*_00he_coeff).reshape((1,))

# op _00ho_power_combination_eval
# LANG: _00hn --> _00hp
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0464__00hp = (v0463__00hn**1)
v0464__00hp = (v0464__00hp*_00ho_coeff).reshape((1,))

# op _00iW_power_combination_eval
# LANG: Vx --> _00iX
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0500__00iX = (v030_u**2)
v0500__00iX = (v0500__00iX*_00iW_coeff).reshape((1,))

# op _00iY_power_combination_eval
# LANG: Vy --> _00iZ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0502__00iZ = (v035_v**2)
v0502__00iZ = (v0502__00iZ*_00iY_coeff).reshape((1,))

# op _00k1_linear_combination_eval
# LANG: _00k0, rotor_disk_tonal_spl --> _00k2
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0507__00k2 = _00k1_constant+1*v0787_rotor_disk_tonal_spl+1*v0533__00k0

# op _00kk_power_combination_eval
# LANG: temperature --> _00kl
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0542__00kl = (v0541_temperature**1)
v0542__00kl = (v0542__00kl*_00kk_coeff).reshape((1,))

# op _00ku_power_combination_eval
# LANG: temperature --> _00kv
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0547__00kv = (v0541_temperature**1)
v0547__00kv = (v0547__00kv*_00ku_coeff).reshape((1,))

# op _00m8_tensor_dot_product_eval
# LANG: rel_obs_position, _00m7 --> normal_proj
# SHAPES: (1, 3, 4), (1, 3, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0602_normal_proj = np.sum(v0595_rel_obs_position * v0603__00m7, axis=1)

# op _00uh_linear_combination_eval
# LANG: _00ug, rotor_disk_broadband_spl --> _00ui
# SHAPES: (1, 4), (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0814__00ui = _00uh_constant+1*v0961_rotor_disk_broadband_spl+1*v0840__00ug

# op _00yM_power_combination_eval
# LANG: noise_components --> _00yN
# SHAPES: (2, 1, 4) --> (2, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0977__00yN = (v0975_noise_components**1)
v0977__00yN = (v0977__00yN*_00yM_coeff).reshape((2, 1, 4))

# op _000I_power_combination_eval
# LANG: cruise_altitude --> _000J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v053__000J = (v052_cruise_altitude**6)
v053__000J = (v053__000J*_000I_coeff).reshape((1,))

# op _000N_power_combination_eval
# LANG: cruise_altitude --> _000O
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v068__000O = (v052_cruise_altitude**6)
v068__000O = (v068__000O*_000N_coeff).reshape((1,))

# op _000X_power_combination_eval
# LANG: cruise_altitude --> _000Y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v056__000Y = (v052_cruise_altitude**5)
v056__000Y = (v056__000Y*_000X_coeff).reshape((1,))

# op _0010_power_combination_eval
# LANG: cruise_altitude --> _0011
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v071__0011 = (v052_cruise_altitude**5)
v071__0011 = (v071__0011*_0010_coeff).reshape((1,))

# op _0018_power_combination_eval
# LANG: cruise_altitude --> _0019
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v058__0019 = (v052_cruise_altitude**4)
v058__0019 = (v058__0019*_0018_coeff).reshape((1,))

# op _001A_power_combination_eval
# LANG: cruise_altitude --> _001B
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v077__001B = (v052_cruise_altitude**2)
v077__001B = (v077__001B*_001A_coeff).reshape((1,))

# op _001I_power_combination_eval
# LANG: cruise_altitude --> _001J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v064__001J = (v052_cruise_altitude**1)
v064__001J = (v064__001J*_001I_coeff).reshape((1,))

# op _001M_power_combination_eval
# LANG: cruise_altitude --> _001N
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v079__001N = (v052_cruise_altitude**1)
v079__001N = (v079__001N*_001M_coeff).reshape((1,))

# op _001U_power_combination_eval
# LANG: cruise_altitude --> _001V
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v066__001V = (v052_cruise_altitude**0)
v066__001V = (v066__001V*_001U_coeff).reshape((1,))

# op _001Y_power_combination_eval
# LANG: cruise_altitude --> _001Z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v081__001Z = (v052_cruise_altitude**0)
v081__001Z = (v081__001Z*_001Y_coeff).reshape((1,))

# op _001c_power_combination_eval
# LANG: cruise_altitude --> _001d
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v073__001d = (v052_cruise_altitude**4)
v073__001d = (v073__001d*_001c_coeff).reshape((1,))

# op _001k_power_combination_eval
# LANG: cruise_altitude --> _001l
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v060__001l = (v052_cruise_altitude**3)
v060__001l = (v060__001l*_001k_coeff).reshape((1,))

# op _001o_power_combination_eval
# LANG: cruise_altitude --> _001p
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v075__001p = (v052_cruise_altitude**3)
v075__001p = (v075__001p*_001o_coeff).reshape((1,))

# op _001w_power_combination_eval
# LANG: cruise_altitude --> _001x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v062__001x = (v052_cruise_altitude**2)
v062__001x = (v062__001x*_001w_coeff).reshape((1,))

# op _002d_power_combination_eval
# LANG: _002c --> _002e
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0102__002e = (v0101__002c**1.5)
v0102__002e = (v0102__002e*_002d_coeff).reshape((1,))

# op _004v expand_array_eval
# LANG: rotor_disk_origin --> thrust_origin
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v0135_thrust_origin = np.einsum('b,a->ab', v012_rotor_disk_origin.reshape((3,)) ,np.ones((1,))).reshape((1, 3))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _005k_power_combination_eval
# LANG: _005h, _005j --> _005l
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0151__005l = (v0150__005h**1)*(v0152__005j**1)
v0151__005l = (v0151__005l*_005k_coeff).reshape((1, 1))

# op _005q_power_combination_eval
# LANG: _005p, _005o --> _005r
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0157__005r = (v0156__005o**1)*(v0153__005p**1)
v0157__005r = (v0157__005r*_005q_coeff).reshape((1, 1))

# op _005v_power_combination_eval
# LANG: _005u, _005t --> _005w
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0159__005w = (v0158__005t**1)*(v0154__005u**1)
v0159__005w = (v0159__005w*_005v_coeff).reshape((1, 1))

# op _008L_power_combination_eval
# LANG: _008K --> speed_of_sound
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0253_speed_of_sound = (v0252__008K**0.5)
v0253_speed_of_sound = (v0253_speed_of_sound*_008L_coeff).reshape((1, 1))

# op _00ds_power_combination_eval
# LANG: _00dr --> _00dt
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0358__00dt = (v0357__00dr**1)
v0358__00dt = (v0358__00dt*_00ds_coeff).reshape((1, 40, 30))

# op _00e9_power_combination_eval
# LANG: _00e8, _chord --> _00ea
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0372__00ea = (v0366__00e8**1)*(v0212__chord**1)
v0372__00ea = (v0372__00ea*_00e9_coeff).reshape((1, 40, 30))

# op _00ex_power_combination_eval
# LANG: _00ew, _dr --> _00ey
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0420__00ey = (v0419__00ew**1)*(v0205__dr**1)
v0420__00ey = (v0420__00ey*_00ex_coeff).reshape((1, 40, 30))

# op _00f0_power_combination_eval
# LANG: _00bz, _00e_ --> _00f1
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0334__00f1 = (v0333__00e_**1)*(v0323__00bz**1)
v0334__00f1 = (v0334__00f1*_00f0_coeff).reshape((1, 40, 30))

# op _00fa_linear_combination_eval
# LANG: _00f3, _00f9 --> _00fb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0337__00fb = _00fa_constant+1*v0336__00f3+1*v0340__00f9

# op _00fm_power_combination_eval
# LANG: _00bz, _00fl --> _00fn
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0401__00fn = (v0400__00fl**1)*(v0323__00bz**1)
v0401__00fn = (v0401__00fn*_00fm_coeff).reshape((1, 40, 30))

# op _00fw_linear_combination_eval
# LANG: _00fp, _00fv --> _00fx
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0404__00fx = _00fw_constant+1*v0403__00fp+1*v0407__00fv

# op _00g3_power_combination_eval
# LANG: _00g2, _radius --> _00g4
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0392__00g4 = (v0391__00g2**1)*(v0217__radius**1)
v0392__00g4 = (v0392__00g4*_00g3_coeff).reshape((1, 40, 30))

# op _00gz_power_combination_eval
# LANG: _00ge, _00gy --> _00gA
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0426__00gA = (v0425__00ge**1)*(v0433__00gy**1)
v0426__00gA = (v0426__00gA*_00gz_coeff).reshape((1, 40, 30))

# op _00hE_power_combination_eval
# LANG: _00hD --> _00hF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0472__00hF = (v0471__00hD**1)
v0472__00hF = (v0472__00hF*_00hE_coeff).reshape((1,))

# op _00hM_power_combination_eval
# LANG: C_T --> _00hN
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0476__00hN = (v0448_C_T**1)
v0476__00hN = (v0476__00hN*_00hM_coeff).reshape((1,))

# op _00hg_power_combination_eval
# LANG: _00h7, _00hf --> _00hh
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0455__00hh = (v0454__00h7**1)*(v0459__00hf**-1)
v0455__00hh = (v0455__00hh*_00hg_coeff).reshape((1,))

# op _00hq_power_combination_eval
# LANG: _00hp --> _00hr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0465__00hr = (v0464__00hp**5)
v0465__00hr = (v0465__00hr*_00hq_coeff).reshape((1,))

# op _00i__linear_combination_eval
# LANG: _00iX, _00iZ --> _00j0
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0501__00j0 = _00i__constant+1*v0500__00iX+1*v0502__00iZ

# op _00j1_power_combination_eval
# LANG: Vz --> _00j2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0504__00j2 = (v039_w**2)
v0504__00j2 = (v0504__00j2*_00j1_coeff).reshape((1,))

# op _00k3_power_combination_eval
# LANG: _00k2 --> _00k4
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0534__00k4 = (v0507__00k2**1)
v0534__00k4 = (v0534__00k4*_00k3_coeff).reshape((1, 4))

# op _00km_power_combination_eval
# LANG: _00kl --> _00kn
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0543__00kn = (v0542__00kl**5.258643795229161)
v0543__00kn = (v0543__00kn*_00km_coeff).reshape((1,))

# op _00kw_power_combination_eval
# LANG: _00kv --> _00kx
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0548__00kx = (v0547__00kv**1.5)
v0548__00kx = (v0548__00kx*_00kw_coeff).reshape((1,))

# op _00mC_linear_combination_eval
# LANG: rel_obs_z_pos --> _00mD
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0617__00mD = _00mC_constant+1*v0593_rel_obs_z_pos

# op _00me expand_array_eval
# LANG: normal_proj --> _00mf
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0604__00mf = np.einsum('ac,b->abc', v0602_normal_proj.reshape((1, 4)) ,np.ones((1,))).reshape((1, 1, 4))

# op _00mk expand_array_eval
# LANG: normal_proj --> _00ml
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0608__00ml = np.einsum('ac,b->abc', v0602_normal_proj.reshape((1, 4)) ,np.ones((1,))).reshape((1, 1, 4))

# op _00mu_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00mv
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0612__00mv = (v0593_rel_obs_z_pos**1)*(v0601_rel_obs_dist**-1)
v0612__00mv = (v0612__00mv*_00mu_coeff).reshape((1, 1, 4))

# op _00uj_power_combination_eval
# LANG: _00ui --> _00uk
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0841__00uk = (v0814__00ui**1)
v0841__00uk = (v0841__00uk*_00uj_coeff).reshape((1, 4))

# op _00w1 expand_array_eval
# LANG: normal_proj --> _00w2
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0898__00w2 = np.einsum('ac,b->abc', v0892_normal_proj.reshape((1, 4)) ,np.ones((1,))).reshape((1, 1, 4))

# op _00wb_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00wc
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0902__00wc = (v0883_rel_obs_z_pos**1)*(v0891_rel_obs_dist**-1)
v0902__00wc = (v0902__00wc*_00wb_coeff).reshape((1, 1, 4))

# op _00wj_linear_combination_eval
# LANG: rel_obs_z_pos --> _00wk
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0907__00wk = _00wj_constant+1*v0883_rel_obs_z_pos

# op _00yO_exp_a_eval
# LANG: _00yN --> _00yP
# SHAPES: (2, 1, 4) --> (2, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0978__00yP = _00yO_exp_a_eval_a**v0977__00yN

# op _000K_power_combination_eval
# LANG: _000J --> _000L
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v054__000L = (v053__000J**1)
v054__000L = (v054__000L*_000K_coeff).reshape((1,))

# op _000P_power_combination_eval
# LANG: _000O --> _000Q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v069__000Q = (v068__000O**1)
v069__000Q = (v069__000Q*_000P_coeff).reshape((1,))

# op _000Z_power_combination_eval
# LANG: _000Y --> _000_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v057__000_ = (v056__000Y**1)
v057__000_ = (v057__000_*_000Z_coeff).reshape((1,))

# op _0012_power_combination_eval
# LANG: _0011 --> _0013
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v072__0013 = (v071__0011**1)
v072__0013 = (v072__0013*_0012_coeff).reshape((1,))

# op _001C_power_combination_eval
# LANG: _001B --> _001D
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v078__001D = (v077__001B**1)
v078__001D = (v078__001D*_001C_coeff).reshape((1,))

# op _001K_power_combination_eval
# LANG: _001J --> _001L
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v065__001L = (v064__001J**1)
v065__001L = (v065__001L*_001K_coeff).reshape((1,))

# op _001O_power_combination_eval
# LANG: _001N --> _001P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v080__001P = (v079__001N**1)
v080__001P = (v080__001P*_001O_coeff).reshape((1,))

# op _001W_power_combination_eval
# LANG: _001V --> _001X
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v067__001X = (v066__001V**1)
v067__001X = (v067__001X*_001W_coeff).reshape((1,))

# op _001__power_combination_eval
# LANG: _001Z --> _0020
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v082__0020 = (v081__001Z**1)
v082__0020 = (v082__0020*_001__coeff).reshape((1,))

# op _001a_power_combination_eval
# LANG: _0019 --> _001b
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v059__001b = (v058__0019**1)
v059__001b = (v059__001b*_001a_coeff).reshape((1,))

# op _001e_power_combination_eval
# LANG: _001d --> _001f
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v074__001f = (v073__001d**1)
v074__001f = (v074__001f*_001e_coeff).reshape((1,))

# op _001m_power_combination_eval
# LANG: _001l --> _001n
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v061__001n = (v060__001l**1)
v061__001n = (v061__001n*_001m_coeff).reshape((1,))

# op _001q_power_combination_eval
# LANG: _001p --> _001r
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v076__001r = (v075__001p**1)
v076__001r = (v076__001r*_001q_coeff).reshape((1,))

# op _001y_power_combination_eval
# LANG: _001x --> _001z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v063__001z = (v062__001x**1)
v063__001z = (v063__001z*_001y_coeff).reshape((1,))

# op _002f_power_combination_eval
# LANG: _002e --> _002g
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0103__002g = (v0102__002e**1)
v0103__002g = (v0103__002g*_002f_coeff).reshape((1,))

# op _004T expand_scalar_eval
# LANG: speed_of_sound --> _004U
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0253_speed_of_sound = v0253_speed_of_sound.reshape((1,))
v0146__004U = np.empty((1, 40, 30))
v0146__004U.fill(v0253_speed_of_sound.item())
v0253_speed_of_sound = v0253_speed_of_sound.reshape((1, 1))

# op _005m_indexed_passthrough_eval
# LANG: _005l, _005r, _005w --> F
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0155_F__temp[i_v0151__005l__005m_indexed_passthrough_eval] = v0151__005l.flatten()
v0155_F = v0155_F__temp.copy()
v0155_F__temp[i_v0157__005r__005m_indexed_passthrough_eval] = v0157__005r.flatten()
v0155_F = v0155_F__temp.copy()
v0155_F__temp[i_v0159__005w__005m_indexed_passthrough_eval] = v0159__005w.flatten()
v0155_F = v0155_F__temp.copy()

# op _005x_linear_combination_eval
# LANG: thrust_origin, reference_point --> _005y
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0160__005y = _005x_constant+1*v0135_thrust_origin+-1*v0161_reference_point

# op _00do_power_combination_eval
# LANG: _00bz, _local_thrust --> _00dp
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0355__00dp = (v0328__local_thrust**1)*(v0323__00bz**-1)
v0355__00dp = (v0355__00dp*_00do_coeff).reshape((1, 40, 30))

# op _00du_power_combination_eval
# LANG: _00dt --> _00dv
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0359__00dv = (v0358__00dt**2)
v0359__00dv = (v0359__00dv*_00du_coeff).reshape((1, 40, 30))

# op _00dy_power_combination_eval
# LANG: _rotor_radius --> _00dz
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0361__00dz = (v0204__rotor_radius**1)
v0361__00dz = (v0361__00dz*_00dy_coeff).reshape((1, 40, 30))

# op _00eb_power_combination_eval
# LANG: _00ea, _dr --> _local_thrust_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0373__local_thrust_2 = (v0372__00ea**1)*(v0205__dr**1)
v0373__local_thrust_2 = (v0373__local_thrust_2*_00eb_coeff).reshape((1, 40, 30))

# op _00ez_power_combination_eval
# LANG: _00ey, _radius --> _local_torque_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0421__local_torque_2 = (v0420__00ey**1)*(v0217__radius**1)
v0421__local_torque_2 = (v0421__local_torque_2*_00ez_coeff).reshape((1, 40, 30))

# op _00fc_power_combination_eval
# LANG: _00f1, _00fb --> _00fd
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0335__00fd = (v0334__00f1**1)*(v0337__00fb**1)
v0335__00fd = (v0335__00fd*_00fc_coeff).reshape((1, 40, 30))

# op _00fy_power_combination_eval
# LANG: _00fn, _00fx --> _00fz
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0402__00fz = (v0401__00fn**1)*(v0404__00fx**1)
v0402__00fz = (v0402__00fz*_00fy_coeff).reshape((1, 40, 30))

# op _00g5_power_combination_eval
# LANG: _00g4, _dr --> _local_thrust_star
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0393__local_thrust_star = (v0392__00g4**1)*(v0205__dr**1)
v0393__local_thrust_star = (v0393__local_thrust_star*_00g5_coeff).reshape((1, 40, 30))

# op _00gB_power_combination_eval
# LANG: _00gA, prandtl_loss_factor --> _00gC
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0437__00gC = (v0426__00gA**1)*(v0267_prandtl_loss_factor**1)
v0437__00gC = (v0437__00gC*_00gB_coeff).reshape((1, 40, 30))

# op _00hG_power_combination_eval
# LANG: _00hF --> J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0473_J = (v0472__00hF**1)
v0473_J = (v0473_J*_00hG_coeff).reshape((1,))

# op _00hO_power_combination_eval
# LANG: _00hN --> _00hP
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0477__00hP = (v0476__00hN**0.5)
v0477__00hP = (v0477__00hP*_00hO_coeff).reshape((1,))

# op _00hs_power_combination_eval
# LANG: _00hh, _00hr --> C_Q
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0460_C_Q = (v0455__00hh**1)*(v0465__00hr**-1)
v0460_C_Q = (v0460_C_Q*_00hs_coeff).reshape((1,))

# op _00j3_linear_combination_eval
# LANG: _00j0, _00j2 --> _00j4
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0503__00j4 = _00j3_constant+1*v0501__00j0+1*v0504__00j2

# op _00k5_exp_a_eval
# LANG: _00k4 --> _00k6
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0535__00k6 = _00k5_exp_a_eval_a**v0534__00k4

# op _00ko_power_combination_eval
# LANG: _00kn --> pressure
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0544_pressure = (v0543__00kn**1)
v0544_pressure = (v0544_pressure*_00ko_coeff).reshape((1,))

# op _00ky_power_combination_eval
# LANG: _00kx --> _00kz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0549__00kz = (v0548__00kx**1)
v0549__00kz = (v0549__00kz*_00ky_coeff).reshape((1,))

# op _00mE_power_combination_eval
# LANG: _00mD --> _00mF
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0618__00mF = (v0617__00mD**2)
v0618__00mF = (v0618__00mF*_00mE_coeff).reshape((1, 1, 4))

# op _00mg_power_combination_eval
# LANG: rel_obs_dist, _00mf --> _00mh
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0605__00mh = (v0604__00mf**1)*(v0601_rel_obs_dist**-1)
v0605__00mh = (v0605__00mh*_00mg_coeff).reshape((1, 1, 4))

# op _00mm_power_combination_eval
# LANG: rel_obs_dist, _00ml --> _00mn
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0609__00mn = (v0608__00ml**1)*(v0601_rel_obs_dist**-1)
v0609__00mn = (v0609__00mn*_00mm_coeff).reshape((1, 1, 4))

# op _00mw arccos_eval
# LANG: _00mv --> _00mx
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0613__00mx = np.arccos(v0612__00mv)

# op _00my_linear_combination_eval
# LANG: rel_obs_z_pos --> _00mz
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0615__00mz = _00my_constant+1*v0593_rel_obs_z_pos

# op _00ul_exp_a_eval
# LANG: _00uk --> _00um
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0842__00um = _00ul_exp_a_eval_a**v0841__00uk

# op _00w3_power_combination_eval
# LANG: rel_obs_dist, _00w2 --> _00w4
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0899__00w4 = (v0898__00w2**1)*(v0891_rel_obs_dist**-1)
v0899__00w4 = (v0899__00w4*_00w3_coeff).reshape((1, 1, 4))

# op _00wd arccos_eval
# LANG: _00wc --> _00we
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0903__00we = np.arccos(v0902__00wc)

# op _00wf_linear_combination_eval
# LANG: rel_obs_z_pos --> _00wg
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0905__00wg = _00wf_constant+1*v0883_rel_obs_z_pos

# op _00wl_power_combination_eval
# LANG: _00wk --> _00wm
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0908__00wm = (v0907__00wk**2)
v0908__00wm = (v0908__00wm*_00wl_coeff).reshape((1, 1, 4))

# op _00yQ_single_tensor_sum_with_axis_eval
# LANG: _00yP --> _00yR
# SHAPES: (2, 1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0979__00yR = np.sum(v0978__00yP, axis = (0,)).reshape((1, 4))

# op _000M_indexed_passthrough_eval
# LANG: _000L, _000_, _001b, _001n, _001z, _001L, _001X --> temp_density
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v055_temp_density__temp[i_v054__000L__000M_indexed_passthrough_eval] = v054__000L.flatten()
v055_temp_density = v055_temp_density__temp.copy()
v055_temp_density__temp[i_v057__000___000M_indexed_passthrough_eval] = v057__000_.flatten()
v055_temp_density = v055_temp_density__temp.copy()
v055_temp_density__temp[i_v059__001b__000M_indexed_passthrough_eval] = v059__001b.flatten()
v055_temp_density = v055_temp_density__temp.copy()
v055_temp_density__temp[i_v061__001n__000M_indexed_passthrough_eval] = v061__001n.flatten()
v055_temp_density = v055_temp_density__temp.copy()
v055_temp_density__temp[i_v063__001z__000M_indexed_passthrough_eval] = v063__001z.flatten()
v055_temp_density = v055_temp_density__temp.copy()
v055_temp_density__temp[i_v065__001L__000M_indexed_passthrough_eval] = v065__001L.flatten()
v055_temp_density = v055_temp_density__temp.copy()
v055_temp_density__temp[i_v067__001X__000M_indexed_passthrough_eval] = v067__001X.flatten()
v055_temp_density = v055_temp_density__temp.copy()

# op _000R_indexed_passthrough_eval
# LANG: _000Q, _0013, _001f, _001r, _001D, _001P, _0020 --> temp_pressure
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v070_temp_pressure__temp[i_v069__000Q__000R_indexed_passthrough_eval] = v069__000Q.flatten()
v070_temp_pressure = v070_temp_pressure__temp.copy()
v070_temp_pressure__temp[i_v072__0013__000R_indexed_passthrough_eval] = v072__0013.flatten()
v070_temp_pressure = v070_temp_pressure__temp.copy()
v070_temp_pressure__temp[i_v074__001f__000R_indexed_passthrough_eval] = v074__001f.flatten()
v070_temp_pressure = v070_temp_pressure__temp.copy()
v070_temp_pressure__temp[i_v076__001r__000R_indexed_passthrough_eval] = v076__001r.flatten()
v070_temp_pressure = v070_temp_pressure__temp.copy()
v070_temp_pressure__temp[i_v078__001D__000R_indexed_passthrough_eval] = v078__001D.flatten()
v070_temp_pressure = v070_temp_pressure__temp.copy()
v070_temp_pressure__temp[i_v080__001P__000R_indexed_passthrough_eval] = v080__001P.flatten()
v070_temp_pressure = v070_temp_pressure__temp.copy()
v070_temp_pressure__temp[i_v082__0020__000R_indexed_passthrough_eval] = v082__0020.flatten()
v070_temp_pressure = v070_temp_pressure__temp.copy()

# op _002B_power_combination_eval
# LANG: _002A --> _002C
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v044__002C = (v025__002A**1)
v044__002C = (v044__002C*_002B_coeff).reshape((1,))

# op _002h_power_combination_eval
# LANG: _002g --> _002i
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0104__002i = (v0103__002g**1)
v0104__002i = (v0104__002i*_002h_coeff).reshape((1,))

# op _002j_linear_combination_eval
# LANG: cruise_temperature --> _002k
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0106__002k = _002j_constant+1*v098_cruise_temperature

# op _0036_power_combination_eval
# LANG: u --> p
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v041_p = (v030_u**1)
v041_p = (v041_p*_0036_coeff).reshape((1,))

# op _0038_power_combination_eval
# LANG: u --> q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v042_q = (v030_u**1)
v042_q = (v042_q*_0038_coeff).reshape((1,))

# op _003a_power_combination_eval
# LANG: u --> r
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v043_r = (v030_u**1)
v043_r = (v043_r*_003a_coeff).reshape((1,))

# op _0050_power_combination_eval
# LANG: _004L, _004U --> mach_number
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0145_mach_number = (v0141__004L**1)*(v0146__004U**-1)
v0145_mach_number = (v0145_mach_number*_0050_coeff).reshape((1, 40, 30))

# op _005z cross_product_eval
# LANG: F, _005y --> _005A
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0162__005A = np.cross(v0160__005y, v0155_F, axisa = 1, axisb = 1, axisc = 1)

# op _00dA_power_combination_eval
# LANG: _00dz --> _00dB
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0362__00dB = (v0361__00dz**4)
v0362__00dB = (v0362__00dB*_00dA_coeff).reshape((1, 40, 30))

# op _00dw_power_combination_eval
# LANG: _00dp, _00dv --> _00dx
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0356__00dx = (v0355__00dp**1)*(v0359__00dv**-1)
v0356__00dx = (v0356__00dx*_00dw_coeff).reshape((1, 40, 30))

# op _00fA_power_combination_eval
# LANG: _00fz, _chord --> _00fB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0408__00fB = (v0402__00fz**1)*(v0212__chord**1)
v0408__00fB = (v0408__00fB*_00fA_coeff).reshape((1, 40, 30))

# op _00fE_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_2 --> _00fF
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0374__00fF = np.sum(v0373__local_thrust_2, axis = (1, 2)).reshape((1,))

# op _00fI_single_tensor_sum_with_axis_eval
# LANG: _local_torque_2 --> _00fJ
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0422__00fJ = np.sum(v0421__local_torque_2, axis = (1, 2)).reshape((1,))

# op _00fe_power_combination_eval
# LANG: _00fd, _chord --> _00ff
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0341__00ff = (v0335__00fd**1)*(v0212__chord**1)
v0341__00ff = (v0341__00ff*_00fe_coeff).reshape((1, 40, 30))

# op _00g7_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_star --> _00g8
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0394__00g8 = np.sum(v0393__local_thrust_star, axis = (1, 2)).reshape((1,))

# op _00gD_power_combination_eval
# LANG: _00gC, _dr --> _local_energy_loss
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0438__local_energy_loss = (v0437__00gC**1)*(v0205__dr**1)
v0438__local_energy_loss = (v0438__local_energy_loss*_00gD_coeff).reshape((1, 40, 30))

# op _00hI_power_combination_eval
# LANG: C_T, J --> _00hJ
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0467__00hJ = (v0448_C_T**1)*(v0473_J**1)
v0467__00hJ = (v0467__00hJ*_00hI_coeff).reshape((1,))

# op _00hQ_power_combination_eval
# LANG: C_T, _00hP --> _00hR
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0475__00hR = (v0448_C_T**1)*(v0477__00hP**1)
v0475__00hR = (v0475__00hR*_00hQ_coeff).reshape((1,))

# op _00hu_power_combination_eval
# LANG: C_Q --> C_P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0466_C_P = (v0460_C_Q**1)
v0466_C_P = (v0466_C_P*_00hu_coeff).reshape((1,))

# op _00j5_power_combination_eval
# LANG: _00j4 --> _00j6
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0505__00j6 = (v0503__00j4**0.5)
v0505__00j6 = (v0505__00j6*_00j5_coeff).reshape((1,))

# op _00k7_log10_eval
# LANG: _00k6 --> _00k8
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0536__00k8 = np.log10(v0535__00k6)

# op _00kA_power_combination_eval
# LANG: _00kz --> _00kB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0550__00kB = (v0549__00kz**1)
v0550__00kB = (v0550__00kB*_00kA_coeff).reshape((1,))

# op _00kC_linear_combination_eval
# LANG: temperature --> _00kD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0552__00kD = _00kC_constant+1*v0541_temperature

# op _00kq_power_combination_eval
# LANG: pressure --> _00kr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0545__00kr = (v0544_pressure**1)
v0545__00kr = (v0545__00kr*_00kq_coeff).reshape((1,))

# op _00mA_power_combination_eval
# LANG: _00mx, _00mz --> _00mB
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0614__00mB = (v0613__00mx**1)*(v0615__00mz**1)
v0614__00mB = (v0614__00mB*_00mA_coeff).reshape((1, 1, 4))

# op _00mG_power_combination_eval
# LANG: _00mF --> _00mH
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0619__00mH = (v0618__00mF**0.5)
v0619__00mH = (v0619__00mH*_00mG_coeff).reshape((1, 1, 4))

# op _00mi_arcsin_eval
# LANG: _00mh --> _00mj
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0606__00mj = np.arcsin(v0605__00mh)

# op _00mo arccos_eval
# LANG: _00mn --> _00mp
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0610__00mp = np.arccos(v0609__00mn)

# op _00un_log10_eval
# LANG: _00um --> _00uo
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0843__00uo = np.log10(v0842__00um)

# op _00w5 arccos_eval
# LANG: _00w4 --> _00w6
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0900__00w6 = np.arccos(v0899__00w4)

# op _00wh_power_combination_eval
# LANG: _00we, _00wg --> _00wi
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0904__00wi = (v0903__00we**1)*(v0905__00wg**1)
v0904__00wi = (v0904__00wi*_00wh_coeff).reshape((1, 1, 4))

# op _00wn_power_combination_eval
# LANG: _00wm --> _00wo
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0909__00wo = (v0908__00wm**0.5)
v0909__00wo = (v0909__00wo*_00wn_coeff).reshape((1, 1, 4))

# op _00yS_log10_eval
# LANG: _00yR --> _00yT
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0980__00yT = np.log10(v0979__00yR)

# op _0001_power_combination_eval
# LANG: caddee_test_input --> caddee_test_output
# SHAPES: (1,) --> (1,)
# full namespace: 
v02_caddee_test_output = (v01_caddee_test_input**1)
v02_caddee_test_output = (v02_caddee_test_output*_0001_coeff).reshape((1,))

# op _000d_power_combination_eval
# LANG: design_geometry --> design_geometry_0
# SHAPES: (16250, 3) --> (16250, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v06_design_geometry_0 = (v05_design_geometry**1)
v06_design_geometry_0 = (v06_design_geometry_0*_000d_coeff).reshape((16250, 3))

# op _0025 single_tensor_sum_no_axis_eval
# LANG: temp_density --> cruise_density
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0100_cruise_density = np.sum(v055_temp_density).reshape((1,))

# op _0027 single_tensor_sum_no_axis_eval
# LANG: temp_pressure --> cruise_pressure
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v099_cruise_pressure = np.sum(v070_temp_pressure).reshape((1,))

# op _002l_power_combination_eval
# LANG: _002i, _002k --> cruise_dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation.atmosphere_model
v0105_cruise_dynamic_viscosity = (v0104__002i**1)*(v0106__002k**-1)
v0105_cruise_dynamic_viscosity = (v0105_cruise_dynamic_viscosity*_002l_coeff).reshape((1,))

# op _002x_power_combination_eval
# LANG: cruise_range, cruise_speed --> cruise_time
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v021_cruise_time = (v019_cruise_range**1)*(v022_cruise_speed**-1)
v021_cruise_time = (v021_cruise_time*_002x_coeff).reshape((1,))

# op _003e_power_combination_eval
# LANG: _002C --> phi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v045_phi = (v044__002C**1)
v045_phi = (v045_phi*_003e_coeff).reshape((1,))

# op _003g_power_combination_eval
# LANG: _002E --> gamma
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v046_gamma = (v028__002E**1)
v046_gamma = (v046_gamma*_003g_coeff).reshape((1,))

# op _003i_power_combination_eval
# LANG: _002G --> psi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v047_psi = (v031__002G**1)
v047_psi = (v047_psi*_003i_coeff).reshape((1,))

# op _003m_power_combination_eval
# LANG: _003c --> x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v049_x = (v026__003c**1)
v049_x = (v049_x*_003m_coeff).reshape((1,))

# op _003o_power_combination_eval
# LANG: _003d --> y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v050_y = (v027__003d**1)
v050_y = (v050_y*_003o_coeff).reshape((1,))

# op _003q_power_combination_eval
# LANG: _002A --> z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.cruise_ac_states_operation
v051_z = (v025__002A**1)
v051_z = (v051_z*_003q_coeff).reshape((1,))

# op _0052 reshape_eval
# LANG: Re --> Re_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0147_Re_ml_input = v0143_Re.reshape((1200, 1))

# op _0054 reshape_eval
# LANG: mach_number --> mach_number_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0148_mach_number_ml_input = v0145_mach_number.reshape((1200, 1))

# op _005B_transpose_eval
# LANG: _005A --> M
# SHAPES: (1, 3) --> (3, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0163_M = np.transpose(v0162__005A)

# op _005N_power_combination_eval
# LANG: p --> p1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v041_p = v041_p.reshape((1, 1))
v0171_p1 = (v041_p**1)
v0171_p1 = (v0171_p1*_005N_coeff).reshape((1, 1))
v041_p = v041_p.reshape((1,))

# op _005Q_power_combination_eval
# LANG: q --> q1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v042_q = v042_q.reshape((1, 1))
v0172_q1 = (v042_q**1)
v0172_q1 = (v0172_q1*_005Q_coeff).reshape((1, 1))
v042_q = v042_q.reshape((1,))

# op _005T_power_combination_eval
# LANG: r --> r1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v043_r = v043_r.reshape((1, 1))
v0173_r1 = (v043_r**1)
v0173_r1 = (v0173_r1*_005T_coeff).reshape((1, 1))
v043_r = v043_r.reshape((1,))

# op _00dC_power_combination_eval
# LANG: _00dx, _00dB --> dC_T
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0360_dC_T = (v0356__00dx**1)*(v0362__00dB**-1)
v0360_dC_T = (v0360_dC_T*_00dC_coeff).reshape((1, 40, 30))

# op _00fC_power_combination_eval
# LANG: _00fB, _dr --> _local_torque_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0409__local_torque_induced = (v0408__00fB**1)*(v0205__dr**1)
v0409__local_torque_induced = (v0409__local_torque_induced*_00fC_coeff).reshape((1, 40, 30))

# op _00fG_power_combination_eval
# LANG: _00fF --> total_thrust_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0375_total_thrust_2 = (v0374__00fF**1)
v0375_total_thrust_2 = (v0375_total_thrust_2*_00fG_coeff).reshape((1,))

# op _00fK_power_combination_eval
# LANG: _00fJ --> total_torque_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0423_total_torque_2 = (v0422__00fJ**1)
v0423_total_torque_2 = (v0423_total_torque_2*_00fK_coeff).reshape((1,))

# op _00fg_power_combination_eval
# LANG: _00ff, _dr --> _local_thrust_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0342__local_thrust_induced = (v0341__00ff**1)*(v0205__dr**1)
v0342__local_thrust_induced = (v0342__local_thrust_induced*_00fg_coeff).reshape((1, 40, 30))

# op _00g9_power_combination_eval
# LANG: _00g8 --> total_thrust_star
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0395_total_thrust_star = (v0394__00g8**1)
v0395_total_thrust_star = (v0395_total_thrust_star*_00g9_coeff).reshape((1,))

# op _00gF_single_tensor_sum_with_axis_eval
# LANG: _local_energy_loss --> total_energy_loss
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0439_total_energy_loss = np.sum(v0438__local_energy_loss, axis = (1, 2)).reshape((1,))

# op _00hK_power_combination_eval
# LANG: C_P, _00hJ --> eta
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0474_eta = (v0467__00hJ**1)*(v0466_C_P**-1)
v0474_eta = (v0474_eta*_00hK_coeff).reshape((1,))

# op _00hS_power_combination_eval
# LANG: C_P, _00hR --> FOM
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0478_FOM = (v0475__00hR**1)*(v0466_C_P**-1)
v0478_FOM = (v0478_FOM*_00hS_coeff).reshape((1,))

# op _00hW_power_combination_eval
# LANG: total_torque --> Q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0354_Q = (v0353_total_torque**1)
v0354_Q = (v0354_Q*_00hW_coeff).reshape((1,))

# op _00hY_power_combination_eval
# LANG: _local_torque --> _dQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0396__dQ = (v0351__local_torque**1)
v0396__dQ = (v0396__dQ*_00hY_coeff).reshape((1, 40, 30))

# op _00j7_power_combination_eval
# LANG: _00j6, speed_of_sound --> mach_number
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0506_mach_number = (v0505__00j6**1)*(v0554_speed_of_sound**-1)
v0506_mach_number = (v0506_mach_number*_00j7_coeff).reshape((1,))

# op _00k9_power_combination_eval
# LANG: _00k8 --> rotor_disk_tonal_spl_A_weighted
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0537_rotor_disk_tonal_spl_A_weighted = (v0536__00k8**1)
v0537_rotor_disk_tonal_spl_A_weighted = (v0537_rotor_disk_tonal_spl_A_weighted*_00k9_coeff).reshape((1, 4))

# op _00kE_power_combination_eval
# LANG: _00kB, _00kD --> dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0551_dynamic_viscosity = (v0550__00kB**1)*(v0552__00kD**-1)
v0551_dynamic_viscosity = (v0551_dynamic_viscosity*_00kE_coeff).reshape((1,))

# op _00ks_power_combination_eval
# LANG: temperature, _00kr --> density
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0546_density = (v0545__00kr**1)*(v0541_temperature**-1)
v0546_density = (v0546_density*_00ks_coeff).reshape((1,))

# op _00mI_power_combination_eval
# LANG: _00mB, _00mH --> rel_obs_angle
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0616_rel_obs_angle = (v0614__00mB**1)*(v0619__00mH**-1)
v0616_rel_obs_angle = (v0616_rel_obs_angle*_00mI_coeff).reshape((1, 1, 4))

# op _00mq reshape_eval
# LANG: _00mj --> rel_angle_plane
# SHAPES: (1, 1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0607_rel_angle_plane = v0606__00mj.reshape((1, 4))

# op _00ms reshape_eval
# LANG: _00mp --> rel_angle_normal
# SHAPES: (1, 1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0611_rel_angle_normal = v0610__00mp.reshape((1, 4))

# op _00up_power_combination_eval
# LANG: _00uo --> rotor_disk_broadband_spl_A_weighted
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model
v0844_rotor_disk_broadband_spl_A_weighted = (v0843__00uo**1)
v0844_rotor_disk_broadband_spl_A_weighted = (v0844_rotor_disk_broadband_spl_A_weighted*_00up_coeff).reshape((1, 4))

# op _00w9 reshape_eval
# LANG: _00w6 --> rel_angle_normal
# SHAPES: (1, 1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0901_rel_angle_normal = v0900__00w6.reshape((1, 4))

# op _00wp_power_combination_eval
# LANG: _00wi, _00wo --> rel_obs_angle
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_GL_broadband_model.steady_observer_location_model
v0906_rel_obs_angle = (v0904__00wi**1)*(v0909__00wo**-1)
v0906_rel_obs_angle = (v0906_rel_obs_angle*_00wp_coeff).reshape((1, 1, 4))

# op _00yU_power_combination_eval
# LANG: _00yT --> total_spl
# SHAPES: (1, 4) --> (1, 4)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0981_total_spl = (v0980__00yT**1)
v0981_total_spl = (v0981_total_spl*_00yU_coeff).reshape((1, 4))