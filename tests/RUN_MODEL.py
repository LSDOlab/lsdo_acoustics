

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

# op _00Aw_decompose_eval
# LANG: hover_observer_location --> _00Ax, _00Ay, _00Az
# SHAPES: (3,) --> (1,), (1,), (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0974__00Ax = ((v0972_hover_observer_location.flatten())[src_indices__00Ax__00Aw]).reshape((1,))
v0975__00Ay = ((v0972_hover_observer_location.flatten())[src_indices__00Ay__00Aw]).reshape((1,))
v0976__00Az = ((v0972_hover_observer_location.flatten())[src_indices__00Az__00Aw]).reshape((1,))

# op _00BN_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00BO
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v01066__00BO = (v08_rotor_disk_in_plane_1**1)
v01066__00BO = (v01066__00BO*_00BN_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _00BQ_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _00BR
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v01070__00BR = (v010_rotor_disk_in_plane_2**1)
v01070__00BR = (v01070__00BR*_00BQ_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _00AS_power_combination_eval
# LANG: _00Ax --> theta
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0986_theta = (v0974__00Ax**1)
v0986_theta = (v0986_theta*_00AS_coeff).reshape((1,))

# op _00BZ cross_product_eval
# LANG: _00BO, _00BR --> _00B_
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01071__00B_ = np.cross(v01070__00BR, v01066__00BO, axisa = 0, axisb = 0, axisc = 0)

# op _00Bc_sin_eval
# LANG: theta --> _00Bd
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0986_theta = v0986_theta.reshape((1, 1))
v01049__00Bd = np.sin(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _00Bg_linear_combination_eval
# LANG: theta --> _00Bh
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0986_theta = v0986_theta.reshape((1, 1))
v01051__00Bh = _00Bg_constant+1*v0986_theta
v0986_theta = v0986_theta.reshape((1,))

# op _00Bi_linear_combination_eval
# LANG: theta --> _00Bj
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0986_theta = v0986_theta.reshape((1, 1))
v01053__00Bj = _00Bi_constant+1*v0986_theta
v0986_theta = v0986_theta.reshape((1,))

# op _00Bm_sin_eval
# LANG: theta --> _00Bn
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0986_theta = v0986_theta.reshape((1, 1))
v01054__00Bn = np.sin(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _00Bq_cos_eval
# LANG: theta --> _00Br
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0986_theta = v0986_theta.reshape((1, 1))
v01056__00Br = np.cos(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _00C0 pnorm_eval
# LANG: _00B_ --> _00C1
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01073__00C1 = np.linalg.norm(v01071__00B_.flatten(), ord=2)

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

# op _00B9_cos_eval
# LANG: theta --> _00Ba
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0986_theta = v0986_theta.reshape((1, 1))
v01047__00Ba = np.cos(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _00Be_power_combination_eval
# LANG: _00Bd --> _00Bf
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01050__00Bf = (v01049__00Bd**1)
v01050__00Bf = (v01050__00Bf*_00Be_coeff).reshape((1, 1))

# op _00Bk_power_combination_eval
# LANG: _00Bh, _00Bj --> _00Bl
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01052__00Bl = (v01051__00Bh**1)*(v01053__00Bj**-1)
v01052__00Bl = (v01052__00Bl*_00Bk_coeff).reshape((1, 1))

# op _00Bo_power_combination_eval
# LANG: _00Bn --> _00Bp
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01055__00Bp = (v01054__00Bn**1)
v01055__00Bp = (v01055__00Bp*_00Bo_coeff).reshape((1, 1))

# op _00Bs_power_combination_eval
# LANG: _00Br --> _00Bt
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01057__00Bt = (v01056__00Br**1)
v01057__00Bt = (v01057__00Bt*_00Bs_coeff).reshape((1, 1))

# op _00C2 expand_scalar_eval
# LANG: _00C1 --> _00C3
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01074__00C3 = np.empty((3,))
v01074__00C3.fill(v01073__00C1.item())

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

# op _00Bb_indexed_passthrough_eval
# LANG: _00Ba, _00Bf, _00Bl, _00Bp, _00Bt --> rotation_matrix
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01048_rotation_matrix__temp[i_v01047__00Ba__00Bb_indexed_passthrough_eval] = v01047__00Ba.flatten()
v01048_rotation_matrix = v01048_rotation_matrix__temp.copy()
v01048_rotation_matrix__temp[i_v01050__00Bf__00Bb_indexed_passthrough_eval] = v01050__00Bf.flatten()
v01048_rotation_matrix = v01048_rotation_matrix__temp.copy()
v01048_rotation_matrix__temp[i_v01052__00Bl__00Bb_indexed_passthrough_eval] = v01052__00Bl.flatten()
v01048_rotation_matrix = v01048_rotation_matrix__temp.copy()
v01048_rotation_matrix__temp[i_v01055__00Bp__00Bb_indexed_passthrough_eval] = v01055__00Bp.flatten()
v01048_rotation_matrix = v01048_rotation_matrix__temp.copy()
v01048_rotation_matrix__temp[i_v01057__00Bt__00Bb_indexed_passthrough_eval] = v01057__00Bt.flatten()
v01048_rotation_matrix = v01048_rotation_matrix__temp.copy()

# op _00C4_power_combination_eval
# LANG: _00B_, _00C3 --> _00C5
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01072__00C5 = (v01071__00B_**1)*(v01074__00C3**-1)
v01072__00C5 = (v01072__00C5*_00C4_coeff).reshape((3,))

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

# op _00C6_matvec_eval
# LANG: rotation_matrix, _00C5 --> _00C7
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01069__00C7 = v01048_rotation_matrix@v01072__00C5

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

# op _00C8 expand_array_eval
# LANG: _00C7 --> thrust_vector
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01075_thrust_vector = np.einsum('b,a->ab', v01069__00C7.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

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

# op _00DL_decompose_eval
# LANG: thrust_vector --> _00DM
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01118__00DM = ((v01075_thrust_vector.flatten())[src_indices__00DM__00DL]).reshape((1, 3))

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

# op _00DP_tensor_dot_product_eval
# LANG: projection_vector, _00DM --> _00DQ
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01125__00DQ = np.sum(v01107_projection_vector * v01118__00DM, axis=1)

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

# op _00DR expand_scalar_eval
# LANG: _00DQ --> _00DS
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01126__00DS = np.empty((1, 3))
v01126__00DS.fill(v01125__00DQ.item())

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

# op _00DT_power_combination_eval
# LANG: _00DM, _00DS --> _00DU
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01127__00DU = (v01126__00DS**1)*(v01118__00DM**1)
v01127__00DU = (v01127__00DU*_00DT_coeff).reshape((1, 3))

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

# op _00AA_power_combination_eval
# LANG: _00Ax --> u
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0977_u = (v0974__00Ax**1)
v0977_u = (v0977_u*_00AA_coeff).reshape((1,))

# op _00DV_linear_combination_eval
# LANG: projection_vector, _00DU --> _00DW
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01124__00DW = _00DV_constant+1*v01107_projection_vector+-1*v01127__00DU

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

# op _00AC_power_combination_eval
# LANG: _00Ax --> v
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0978_v = (v0974__00Ax**1)
v0978_v = (v0978_v*_00AC_coeff).reshape((1,))

# op _00AE_power_combination_eval
# LANG: _00Ax --> w
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0979_w = (v0974__00Ax**1)
v0979_w = (v0979_w*_00AE_coeff).reshape((1,))

# op _00DX pnorm_eval
# LANG: _00DW --> _00DY
# SHAPES: (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01129__00DY = np.linalg.norm(v01124__00DW.flatten(), ord=2)

# op _00Dm_power_combination_eval
# LANG: u --> _00Dn
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0977_u = v0977_u.reshape((1, 1))
v01108__00Dn = (v0977_u**1)
v01108__00Dn = (v01108__00Dn*_00Dm_coeff).reshape((1, 1))
v0977_u = v0977_u.reshape((1,))

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

# op _00DZ expand_scalar_eval
# LANG: _00DY --> _00D_
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01130__00D_ = np.empty((1, 3))
v01130__00D_.fill(v01129__00DY.item())

# op _00E9_decompose_eval
# LANG: _00Dn --> _00Ea
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01109__00Ea = ((v01108__00Dn.flatten())[src_indices__00Ea__00E9]).reshape((1, 1))

# op _00Ec_decompose_eval
# LANG: v --> _00Ed
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0978_v = v0978_v.reshape((1, 1))
v01111__00Ed = ((v0978_v.flatten())[src_indices__00Ed__00Ec]).reshape((1, 1))
v0978_v = v0978_v.reshape((1,))

# op _00Ee_decompose_eval
# LANG: w --> _00Ef
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0979_w = v0979_w.reshape((1, 1))
v01112__00Ef = ((v0979_w.flatten())[src_indices__00Ef__00Ee]).reshape((1, 1))
v0979_w = v0979_w.reshape((1,))

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

# op _00E0_power_combination_eval
# LANG: _00DW, _00D_ --> in_plane_ey
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01128_in_plane_ey = (v01124__00DW**1)*(v01130__00D_**-1)
v01128_in_plane_ey = (v01128_in_plane_ey*_00E0_coeff).reshape((1, 3))

# op _00Eb_indexed_passthrough_eval
# LANG: _00Ea, _00Ed, _00Ef --> velocity_vector
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01110_velocity_vector__temp[i_v01109__00Ea__00Eb_indexed_passthrough_eval] = v01109__00Ea.flatten()
v01110_velocity_vector = v01110_velocity_vector__temp.copy()
v01110_velocity_vector__temp[i_v01111__00Ed__00Eb_indexed_passthrough_eval] = v01111__00Ed.flatten()
v01110_velocity_vector = v01110_velocity_vector__temp.copy()
v01110_velocity_vector__temp[i_v01112__00Ef__00Eb_indexed_passthrough_eval] = v01112__00Ef.flatten()
v01110_velocity_vector = v01110_velocity_vector__temp.copy()

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

# op _00E2 cross_product_eval
# LANG: _00DM, in_plane_ey --> in_plane_ex
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01123_in_plane_ex = np.cross(v01118__00DM, v01128_in_plane_ey, axisa = 1, axisb = 1, axisc = 1)

# op _00Eg_decompose_eval
# LANG: velocity_vector --> _00Eh
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01116__00Eh = ((v01110_velocity_vector.flatten())[src_indices__00Eh__00Eg]).reshape((1, 3))

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

# op _00DN_power_combination_eval
# LANG: _00DM --> _00DO
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01119__00DO = (v01118__00DM**1)
v01119__00DO = (v01119__00DO*_00DN_coeff).reshape((1, 3))

# op _00Ei_tensor_dot_product_eval
# LANG: _00Eh, in_plane_ex --> _00Ej
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01122__00Ej = np.sum(v01116__00Eh * v01123_in_plane_ex, axis=1)

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

# op _00BV pnorm_eval
# LANG: _00BO --> _00BW
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01067__00BW = np.linalg.norm(v01066__00BO.flatten(), ord=2)

# op _00Ek_tensor_dot_product_eval
# LANG: _00Eh, in_plane_ey --> _00El
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01133__00El = np.sum(v01116__00Eh * v01128_in_plane_ey, axis=1)

# op _00Em_tensor_dot_product_eval
# LANG: _00Eh, _00DO --> _00En
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01117__00En = np.sum(v01116__00Eh * v01119__00DO, axis=1)

# op _00Er_linear_combination_eval
# LANG: _00Ej --> _00Es
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01131__00Es = _00Er_constant+-1*v01122__00Ej

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

# op _00BX_power_combination_eval
# LANG: _00BW --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01068_propeller_radius = (v01067__00BW**1)
v01068_propeller_radius = (v01068_propeller_radius*_00BX_coeff).reshape((1,))

# op _00Eo expand_scalar_eval
# LANG: _00En --> _00Ep
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01120__00Ep = np.empty((1, 40, 30, 1))
v01120__00Ep.fill(v01117__00En.item())

# op _00Et expand_scalar_eval
# LANG: _00Es --> _00Eu
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01132__00Eu = np.empty((1, 40, 30, 1))
v01132__00Eu.fill(v01131__00Es.item())

# op _00Ev expand_scalar_eval
# LANG: _00El --> _00Ew
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01134__00Ew = np.empty((1, 40, 30, 1))
v01134__00Ew.fill(v01133__00El.item())

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

# op _00DB_power_combination_eval
# LANG: propeller_radius --> hub_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01135_hub_radius = (v01068_propeller_radius**1)
v01135_hub_radius = (v01135_hub_radius*_00DB_coeff).reshape((1,))

# op _00E4_decompose_eval
# LANG: rpm --> _00E5
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01139__00E5 = ((v01106_rpm.flatten())[src_indices__00E5__00E4]).reshape((1, 1))

# op _00Eq_indexed_passthrough_eval
# LANG: _00Ep, _00Eu, _00Ew --> inflow_velocity
# SHAPES: (1, 40, 30, 1), (1, 40, 30, 1), (1, 40, 30, 1) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01121_inflow_velocity__temp[i_v01120__00Ep__00Eq_indexed_passthrough_eval] = v01120__00Ep.flatten()
v01121_inflow_velocity = v01121_inflow_velocity__temp.copy()
v01121_inflow_velocity__temp[i_v01132__00Eu__00Eq_indexed_passthrough_eval] = v01132__00Eu.flatten()
v01121_inflow_velocity = v01121_inflow_velocity__temp.copy()
v01121_inflow_velocity__temp[i_v01134__00Ew__00Eq_indexed_passthrough_eval] = v01134__00Ew.flatten()
v01121_inflow_velocity = v01121_inflow_velocity__temp.copy()

# op _00FV_power_combination_eval
# LANG: z --> _00FW
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01179__00FW = (v01178_z**1)
v01179__00FW = (v01179__00FW*_00FV_coeff).reshape((1, 1))

# op _004h_power_combination_eval
# LANG: _004g --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0128_propeller_radius = (v0127__004g**1)
v0128_propeller_radius = (v0128_propeller_radius*_004h_coeff).reshape((1,))

# op _006J expand_scalar_eval
# LANG: _006I --> _006K
# SHAPES: (1,) --> (1, 40, 100, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0178__006K = np.empty((1, 40, 100, 1))
v0178__006K.fill(v0175__006I.item())

# op _006O expand_scalar_eval
# LANG: _006N --> _006P
# SHAPES: (1,) --> (1, 40, 100, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0190__006P = np.empty((1, 40, 100, 1))
v0190__006P.fill(v0189__006N.item())

# op _006Q expand_scalar_eval
# LANG: _006G --> _006R
# SHAPES: (1,) --> (1, 40, 100, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0192__006R = np.empty((1, 40, 100, 1))
v0192__006R.fill(v0191__006G.item())

# op _00E6_power_combination_eval
# LANG: _00E5 --> _00E7
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01140__00E7 = (v01139__00E5**1)
v01140__00E7 = (v01140__00E7*_00E6_coeff).reshape((1, 1))

# op _00EL expand_scalar_eval
# LANG: hub_radius --> _hub_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01145__hub_radius = np.empty((1, 40, 30))
v01145__hub_radius.fill(v01135_hub_radius.item())

# op _00EN expand_scalar_eval
# LANG: propeller_radius --> _rotor_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01146__rotor_radius = np.empty((1, 40, 30))
v01146__rotor_radius.fill(v01068_propeller_radius.item())

# op _00EV expand_array_eval
# LANG: y_dir --> _y_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01150__y_dir = np.einsum('ad,bc->abcd', v01143_y_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _00EX expand_array_eval
# LANG: z_dir --> _z_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01151__z_dir = np.einsum('ad,bc->abcd', v01144_z_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _00EZ_power_combination_eval
# LANG: inflow_velocity --> _inflow_velocity
# SHAPES: (1, 40, 30, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01152__inflow_velocity = (v01121_inflow_velocity**1)
v01152__inflow_velocity = (v01152__inflow_velocity*_00EZ_coeff).reshape((1, 40, 30, 3))

# op _00FX_linear_combination_eval
# LANG: _00FW --> _00FY
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01180__00FY = _00FX_constant+-1*v01179__00FW

# op _005W_power_combination_eval
# LANG: propeller_radius --> hub_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0193_hub_radius = (v0128_propeller_radius**1)
v0193_hub_radius = (v0193_hub_radius*_005W_coeff).reshape((1,))

# op _006L_indexed_passthrough_eval
# LANG: _006K, _006P, _006R --> inflow_velocity
# SHAPES: (1, 40, 100, 1), (1, 40, 100, 1), (1, 40, 100, 1) --> (1, 40, 100, 3)
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

# op _00E8_indexed_passthrough_eval
# LANG: _00E7 --> rotational_speed
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01141_rotational_speed__temp[i_v01140__00E7__00E8_indexed_passthrough_eval] = v01140__00E7.flatten()
v01141_rotational_speed = v01141_rotational_speed__temp.copy()

# op _00FA_tensor_dot_product_eval
# LANG: _z_dir, _inflow_velocity --> inflow_z
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01168_inflow_z = np.sum(v01152__inflow_velocity * v01151__z_dir, axis=3)

# op _00FZ_power_combination_eval
# LANG: _00FY --> _00F_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01181__00F_ = (v01180__00FY**1)
v01181__00F_ = (v01181__00F_*_00FZ_coeff).reshape((1, 1))

# op _00Fi_linear_combination_eval
# LANG: _hub_radius, _rotor_radius --> _00Fj
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01160__00Fj = _00Fi_constant+1*v01146__rotor_radius+-1*v01145__hub_radius

# op _00Fy_tensor_dot_product_eval
# LANG: _y_dir, _inflow_velocity --> _in_plane_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01167__in_plane_inflow_velocity = np.sum(v01152__inflow_velocity * v01150__y_dir, axis=3)

# op _000s_sparsematmat_eval
# LANG: design_geometry --> _000t
# SHAPES: (16250, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v013__000t = _000s_sparsematmat_eval_mat@v05_design_geometry

# op _006r_power_combination_eval
# LANG: _006q --> _006s
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0198__006s = (v0197__006q**1)
v0198__006s = (v0198__006s*_006r_coeff).reshape((1, 1))

# op _0075 expand_scalar_eval
# LANG: hub_radius --> _hub_radius
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0203__hub_radius = np.empty((1, 40, 100))
v0203__hub_radius.fill(v0193_hub_radius.item())

# op _0077 expand_scalar_eval
# LANG: propeller_radius --> _rotor_radius
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0204__rotor_radius = np.empty((1, 40, 100))
v0204__rotor_radius.fill(v0128_propeller_radius.item())

# op _007f expand_array_eval
# LANG: y_dir --> _y_dir
# SHAPES: (1, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0208__y_dir = np.einsum('ad,bc->abcd', v0201_y_dir.reshape((1, 3)) ,np.ones((40, 100))).reshape((1, 40, 100, 3))

# op _007h expand_array_eval
# LANG: z_dir --> _z_dir
# SHAPES: (1, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0209__z_dir = np.einsum('ad,bc->abcd', v0202_z_dir.reshape((1, 3)) ,np.ones((40, 100))).reshape((1, 40, 100, 3))

# op _007j_power_combination_eval
# LANG: inflow_velocity --> _inflow_velocity
# SHAPES: (1, 40, 100, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0210__inflow_velocity = (v0179_inflow_velocity**1)
v0210__inflow_velocity = (v0210__inflow_velocity*_007j_coeff).reshape((1, 40, 100, 3))

# op _008h_linear_combination_eval
# LANG: _008g --> _008i
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0238__008i = _008h_constant+-1*v0237__008g

# op _00ER expand_scalar_eval
# LANG: rotational_speed --> _rotational_speed
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01141_rotational_speed = v01141_rotational_speed.reshape((1,))
v01148__rotational_speed = np.empty((1, 40, 30))
v01148__rotational_speed.fill(v01141_rotational_speed.item())
v01141_rotational_speed = v01141_rotational_speed.reshape((1, 1))

# op _00FC_power_combination_eval
# LANG: inflow_z --> _00FD
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01169__00FD = (v01168_inflow_z**1)
v01169__00FD = (v01169__00FD*_00FC_coeff).reshape((1, 40, 30))

# op _00FE_cos_eval
# LANG: _theta --> _00FF
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01171__00FF = np.cos(v01156__theta)

# op _00FI_power_combination_eval
# LANG: _in_plane_inflow_velocity --> _00FJ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01173__00FJ = (v01167__in_plane_inflow_velocity**1)
v01173__00FJ = (v01173__00FJ*_00FI_coeff).reshape((1, 40, 30))

# op _00FK_sin_eval
# LANG: _theta --> _00FL
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01175__00FL = np.sin(v01156__theta)

# op _00Fk_power_combination_eval
# LANG: _00Fj, _normalized_radius --> _00Fl
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01161__00Fl = (v01160__00Fj**1)*(v01157__normalized_radius**1)
v01161__00Fl = (v01161__00Fl*_00Fk_coeff).reshape((1, 40, 30))

# op _00G0_linear_combination_eval
# LANG: _00F_ --> temperature
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01182_temperature = _00G0_constant+1*v01181__00F_

# op _000u reshape_eval
# LANG: _000t --> rotor_blade_chord_length
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v014_rotor_blade_chord_length = v013__000t.reshape((40, 3))

# op _006t_indexed_passthrough_eval
# LANG: _006s --> rotational_speed
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0199_rotational_speed__temp[i_v0198__006s__006t_indexed_passthrough_eval] = v0198__006s.flatten()
v0199_rotational_speed = v0199_rotational_speed__temp.copy()

# op _007D_linear_combination_eval
# LANG: _hub_radius, _rotor_radius --> _007E
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0218__007E = _007D_constant+1*v0204__rotor_radius+-1*v0203__hub_radius

# op _007T_tensor_dot_product_eval
# LANG: _y_dir, _inflow_velocity --> _in_plane_inflow_velocity
# SHAPES: (1, 40, 100, 3), (1, 40, 100, 3) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0225__in_plane_inflow_velocity = np.sum(v0210__inflow_velocity * v0208__y_dir, axis=3)

# op _007V_tensor_dot_product_eval
# LANG: _z_dir, _inflow_velocity --> inflow_z
# SHAPES: (1, 40, 100, 3), (1, 40, 100, 3) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0226_inflow_z = np.sum(v0210__inflow_velocity * v0209__z_dir, axis=3)

# op _008j_power_combination_eval
# LANG: _008i --> _008k
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0239__008k = (v0238__008i**1)
v0239__008k = (v0239__008k*_008j_coeff).reshape((1, 1))

# op _00FG_power_combination_eval
# LANG: _00FD, _00FF --> _00FH
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01170__00FH = (v01169__00FD**1)*(v01171__00FF**1)
v01170__00FH = (v01170__00FH*_00FG_coeff).reshape((1, 40, 30))

# op _00FM_power_combination_eval
# LANG: _00FJ, _00FL --> _00FN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01174__00FN = (v01173__00FJ**1)*(v01175__00FL**1)
v01174__00FN = (v01174__00FN*_00FM_coeff).reshape((1, 40, 30))

# op _00Fg_power_combination_eval
# LANG: _rotational_speed --> _angular_speed
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01158__angular_speed = (v01148__rotational_speed**1)
v01158__angular_speed = (v01158__angular_speed*_00Fg_coeff).reshape((1, 40, 30))

# op _00Fm_linear_combination_eval
# LANG: _00Fl, _hub_radius --> _radius
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01159__radius = _00Fm_constant+1*v01145__hub_radius+1*v01161__00Fl

# op _00G2_power_combination_eval
# LANG: temperature --> _00G3
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01183__00G3 = (v01182_temperature**1)
v01183__00G3 = (v01183__00G3*_00G2_coeff).reshape((1, 1))

# op _000w_sparsematmat_eval
# LANG: design_geometry --> _000x
# SHAPES: (16250, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v015__000x = _000w_sparsematmat_eval_mat@v05_design_geometry

# op _007F_power_combination_eval
# LANG: _007E, _normalized_radius --> _007G
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0219__007G = (v0218__007E**1)*(v0215__normalized_radius**1)
v0219__007G = (v0219__007G*_007F_coeff).reshape((1, 40, 100))

# op _007X_power_combination_eval
# LANG: inflow_z --> _007Y
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0227__007Y = (v0226_inflow_z**1)
v0227__007Y = (v0227__007Y*_007X_coeff).reshape((1, 40, 100))

# op _007Z_cos_eval
# LANG: _theta --> _007_
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0229__007_ = np.cos(v0214__theta)

# op _007b expand_scalar_eval
# LANG: rotational_speed --> _rotational_speed
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0199_rotational_speed = v0199_rotational_speed.reshape((1,))
v0206__rotational_speed = np.empty((1, 40, 100))
v0206__rotational_speed.fill(v0199_rotational_speed.item())
v0199_rotational_speed = v0199_rotational_speed.reshape((1, 1))

# op _0082_power_combination_eval
# LANG: _in_plane_inflow_velocity --> _0083
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0231__0083 = (v0225__in_plane_inflow_velocity**1)
v0231__0083 = (v0231__0083*_0082_coeff).reshape((1, 40, 100))

# op _0084_sin_eval
# LANG: _theta --> _0085
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0233__0085 = np.sin(v0214__theta)

# op _008l_linear_combination_eval
# LANG: _008k --> temperature
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0240_temperature = _008l_constant+1*v0239__008k

# op _00Bv pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00Bw
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01058__00Bw = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00ET expand_array_eval
# LANG: x_dir --> _x_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01149__x_dir = np.einsum('ad,bc->abcd', v01142_x_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _00FO_linear_combination_eval
# LANG: _00FH, _00FN --> _00FP
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01172__00FP = _00FO_constant+1*v01170__00FH+1*v01174__00FN

# op _00FQ_power_combination_eval
# LANG: _angular_speed, _radius --> _00FR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01177__00FR = (v01159__radius**1)*(v01158__angular_speed**1)
v01177__00FR = (v01177__00FR*_00FQ_coeff).reshape((1, 40, 30))

# op _00G4_power_combination_eval
# LANG: _00G3 --> _00G5
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01184__00G5 = (v01183__00G3**5.258643795229161)
v01184__00G5 = (v01184__00G5*_00G4_coeff).reshape((1, 1))

# op _000y reshape_eval
# LANG: _000x --> rotor_blade_twist
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v016_rotor_blade_twist = v015__000x.reshape((40, 3))

# op _007B_power_combination_eval
# LANG: _rotational_speed --> _angular_speed
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0216__angular_speed = (v0206__rotational_speed**1)
v0216__angular_speed = (v0216__angular_speed*_007B_coeff).reshape((1, 40, 100))

# op _007H_linear_combination_eval
# LANG: _007G, _hub_radius --> _radius
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0217__radius = _007H_constant+1*v0203__hub_radius+1*v0219__007G

# op _0080_power_combination_eval
# LANG: _007Y, _007_ --> _0081
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0228__0081 = (v0227__007Y**1)*(v0229__007_**1)
v0228__0081 = (v0228__0081*_0080_coeff).reshape((1, 40, 100))

# op _0086_power_combination_eval
# LANG: _0083, _0085 --> _0087
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0232__0087 = (v0231__0083**1)*(v0233__0085**1)
v0232__0087 = (v0232__0087*_0086_coeff).reshape((1, 40, 100))

# op _008n_power_combination_eval
# LANG: temperature --> _008o
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0241__008o = (v0240_temperature**1)
v0241__008o = (v0241__008o*_008n_coeff).reshape((1, 1))

# op _00Bx reshape_eval
# LANG: _00Bw --> _00By
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01059__00By = v01058__00Bw.reshape((40, 1))

# op _00FS_linear_combination_eval
# LANG: _00FP, _00FR --> _tangential_inflow_velocity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01176__tangential_inflow_velocity = _00FS_constant+1*v01172__00FP+1*v01177__00FR

# op _00Fw_tensor_dot_product_eval
# LANG: _x_dir, _inflow_velocity --> _axial_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01166__axial_inflow_velocity = np.sum(v01152__inflow_velocity * v01149__x_dir, axis=3)

# op _00G6_power_combination_eval
# LANG: _00G5 --> pressure
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01185_pressure = (v01184__00G5**1)
v01185_pressure = (v01185_pressure*_00G6_coeff).reshape((1, 1))

# op _00Gc_power_combination_eval
# LANG: temperature --> _00Gd
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01188__00Gd = (v01182_temperature**1)
v01188__00Gd = (v01188__00Gd*_00Gc_coeff).reshape((1, 1))

# op _007d expand_array_eval
# LANG: x_dir --> _x_dir
# SHAPES: (1, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0207__x_dir = np.einsum('ad,bc->abcd', v0200_x_dir.reshape((1, 3)) ,np.ones((40, 100))).reshape((1, 40, 100, 3))

# op _0088_linear_combination_eval
# LANG: _0081, _0087 --> _0089
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0230__0089 = _0088_constant+1*v0228__0081+1*v0232__0087

# op _008a_power_combination_eval
# LANG: _angular_speed, _radius --> _008b
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0235__008b = (v0217__radius**1)*(v0216__angular_speed**1)
v0235__008b = (v0235__008b*_008a_coeff).reshape((1, 40, 100))

# op _008p_power_combination_eval
# LANG: _008o --> _008q
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0242__008q = (v0241__008o**5.258643795229161)
v0242__008q = (v0242__008q*_008p_coeff).reshape((1, 1))

# op _00BC_single_tensor_sum_with_axis_eval
# LANG: rotor_blade_twist --> _00BD
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01061__00BD = np.sum(v016_rotor_blade_twist, axis = (1,)).reshape((40,))

# op _00Bz_power_combination_eval
# LANG: _00By --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01060_chord_profile = (v01059__00By**1)
v01060_chord_profile = (v01060_chord_profile*_00Bz_coeff).reshape((40, 1))

# op _00Cj_power_combination_eval
# LANG: _axial_inflow_velocity --> _00Ck
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01080__00Ck = (v01166__axial_inflow_velocity**2)
v01080__00Ck = (v01080__00Ck*_00Cj_coeff).reshape((1, 40, 30))

# op _00Cl_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00Cm
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01082__00Cm = (v01176__tangential_inflow_velocity**2)
v01082__00Cm = (v01082__00Cm*_00Cl_coeff).reshape((1, 40, 30))

# op _00G8_power_combination_eval
# LANG: pressure --> _00G9
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01186__00G9 = (v01185_pressure**1)
v01186__00G9 = (v01186__00G9*_00G8_coeff).reshape((1, 1))

# op _00Ge_power_combination_eval
# LANG: _00Gd --> _00Gf
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01189__00Gf = (v01188__00Gd**1.5)
v01189__00Gf = (v01189__00Gf*_00Ge_coeff).reshape((1, 1))

# op _003Y pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _003Z
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0120__003Z = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _007R_tensor_dot_product_eval
# LANG: _x_dir, _inflow_velocity --> _axial_inflow_velocity
# SHAPES: (1, 40, 100, 3), (1, 40, 100, 3) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0224__axial_inflow_velocity = np.sum(v0210__inflow_velocity * v0207__x_dir, axis=3)

# op _008c_linear_combination_eval
# LANG: _0089, _008b --> _tangential_inflow_velocity
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
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

# op _00BE reshape_eval
# LANG: _00BD --> _00BF
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01062__00BF = v01061__00BD.reshape((40, 1))

# op _00Cn_linear_combination_eval
# LANG: _00Ck, _00Cm --> _00Co
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01081__00Co = _00Cn_constant+1*v01080__00Ck+1*v01082__00Cm

# op _00F2 expand_array_eval
# LANG: chord_profile --> _chord
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01060_chord_profile = v01060_chord_profile.reshape((40,))
v01154__chord = np.einsum('b,ac->abc', v01060_chord_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v01060_chord_profile = v01060_chord_profile.reshape((40, 1))

# op _00Ga_power_combination_eval
# LANG: temperature, _00G9 --> density
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01187_density = (v01186__00G9**1)*(v01182_temperature**-1)
v01187_density = (v01187_density*_00Ga_coeff).reshape((1, 1))

# op _00Gg_power_combination_eval
# LANG: _00Gf --> _00Gh
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01190__00Gh = (v01189__00Gf**1)
v01190__00Gh = (v01190__00Gh*_00Gg_coeff).reshape((1, 1))

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
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0138__004F = (v0224__axial_inflow_velocity**2)
v0138__004F = (v0138__004F*_004E_coeff).reshape((1, 40, 100))

# op _004G_power_combination_eval
# LANG: _tangential_inflow_velocity --> _004H
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0140__004H = (v0234__tangential_inflow_velocity**2)
v0140__004H = (v0140__004H*_004G_coeff).reshape((1, 40, 100))

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

# op _00BG_power_combination_eval
# LANG: _00By, _00BF --> _00BH
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01063__00BH = (v01062__00BF**1)*(v01059__00By**-1)
v01063__00BH = (v01063__00BH*_00BG_coeff).reshape((40, 1))

# op _00Cp_power_combination_eval
# LANG: _00Co --> _00Cq
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01083__00Cq = (v01081__00Co**0.5)
v01083__00Cq = (v01083__00Cq*_00Cp_coeff).reshape((1, 40, 30))

# op _00Cs expand_scalar_eval
# LANG: density --> _00Ct
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01187_density = v01187_density.reshape((1,))
v01078__00Ct = np.empty((1, 40, 30))
v01078__00Ct.fill(v01187_density.item())
v01187_density = v01187_density.reshape((1, 1))

# op _00Fo_power_combination_eval
# LANG: _chord --> _00Fp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01162__00Fp = (v01154__chord**1)
v01162__00Fp = (v01162__00Fp*_00Fo_coeff).reshape((1, 40, 30))

# op _00Gi_power_combination_eval
# LANG: _00Gh --> _00Gj
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01191__00Gj = (v01190__00Gh**1)
v01191__00Gj = (v01191__00Gj*_00Gi_coeff).reshape((1, 1))

# op _00Gk_linear_combination_eval
# LANG: temperature --> _00Gl
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01193__00Gl = _00Gk_constant+1*v01182_temperature

# op _0044 reshape_eval
# LANG: _0043 --> _0045
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0123__0045 = v0122__0043.reshape((40, 1))

# op _004I_linear_combination_eval
# LANG: _004F, _004H --> _004J
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0139__004J = _004I_constant+1*v0138__004F+1*v0140__004H

# op _007n expand_array_eval
# LANG: chord_profile --> _chord
# SHAPES: (40,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0121_chord_profile = v0121_chord_profile.reshape((40,))
v0212__chord = np.einsum('b,ac->abc', v0121_chord_profile.reshape((40,)) ,np.ones((1, 100))).reshape((1, 40, 100))
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

# op _00BI_arcsin_eval
# LANG: _00BH --> _00BJ
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01064__00BJ = np.arcsin(v01063__00BH)

# op _00CA_power_combination_eval
# LANG: _00Ct, _00Cq --> _00CB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01079__00CB = (v01078__00Ct**1)*(v01083__00Cq**1)
v01079__00CB = (v01079__00CB*_00CA_coeff).reshape((1, 40, 30))

# op _00Fq_power_combination_eval
# LANG: _00Fp --> _00Fr
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01163__00Fr = (v01162__00Fp**1)
v01163__00Fr = (v01163__00Fr*_00Fq_coeff).reshape((1, 40, 30))

# op _00Gm_power_combination_eval
# LANG: _00Gj, _00Gl --> dynamic_viscosity
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01192_dynamic_viscosity = (v01191__00Gj**1)*(v01193__00Gl**-1)
v01192_dynamic_viscosity = (v01192_dynamic_viscosity*_00Gm_coeff).reshape((1, 1))

# op _0046_power_combination_eval
# LANG: chord_profile, _0045 --> _0047
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0124__0047 = (v0123__0045**1)*(v0121_chord_profile**-1)
v0124__0047 = (v0124__0047*_0046_coeff).reshape((40, 1))

# op _004K_power_combination_eval
# LANG: _004J --> _004L
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0141__004L = (v0139__004J**0.5)
v0141__004L = (v0141__004L*_004K_coeff).reshape((1, 40, 100))

# op _004N expand_scalar_eval
# LANG: density --> _004O
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0245_density = v0245_density.reshape((1,))
v0136__004O = np.empty((1, 40, 100))
v0136__004O.fill(v0245_density.item())
v0245_density = v0245_density.reshape((1, 1))

# op _007J_power_combination_eval
# LANG: _chord --> _007K
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0220__007K = (v0212__chord**1)
v0220__007K = (v0220__007K*_007J_coeff).reshape((1, 40, 100))

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

# op _00BK_linear_combination_eval
# LANG: _00BJ --> twist_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01065_twist_profile = _00BK_constant+1*v01064__00BJ

# op _00CC_power_combination_eval
# LANG: _00CB, _chord --> _00CD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01084__00CD = (v01079__00CB**1)*(v01154__chord**1)
v01084__00CD = (v01084__00CD*_00CC_coeff).reshape((1, 40, 30))

# op _00Cv expand_scalar_eval
# LANG: dynamic_viscosity --> _00Cw
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01192_dynamic_viscosity = v01192_dynamic_viscosity.reshape((1,))
v01086__00Cw = np.empty((1, 40, 30))
v01086__00Cw.fill(v01192_dynamic_viscosity.item())
v01192_dynamic_viscosity = v01192_dynamic_viscosity.reshape((1, 1))

# op _00Fs_power_combination_eval
# LANG: _00Fr --> _00Ft
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01164__00Ft = (v01163__00Fr**1)
v01164__00Ft = (v01164__00Ft*_00Fs_coeff).reshape((1, 40, 30))

# op _0048_arcsin_eval
# LANG: _0047 --> _0049
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0125__0049 = np.arcsin(v0124__0047)

# op _004V_power_combination_eval
# LANG: _004O, _004L --> _004W
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0137__004W = (v0136__004O**1)*(v0141__004L**1)
v0137__004W = (v0137__004W*_004V_coeff).reshape((1, 40, 100))

# op _007L_power_combination_eval
# LANG: _007K --> _007M
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0221__007M = (v0220__007K**1)
v0221__007M = (v0221__007M*_007L_coeff).reshape((1, 40, 100))

# op _008H_power_combination_eval
# LANG: _008E, _008G --> dynamic_viscosity
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.atmosphere_model
v0250_dynamic_viscosity = (v0249__008E**1)*(v0251__008G**-1)
v0250_dynamic_viscosity = (v0250_dynamic_viscosity*_008H_coeff).reshape((1, 1))

# op _00CE_power_combination_eval
# LANG: _00CD, _00Cw --> Re
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01085_Re = (v01084__00CD**1)*(v01086__00Cw**-1)
v01085_Re = (v01085_Re*_00CE_coeff).reshape((1, 40, 30))

# op _00F0 expand_array_eval
# LANG: twist_profile --> _pitch
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01065_twist_profile = v01065_twist_profile.reshape((40,))
v01153__pitch = np.einsum('b,ac->abc', v01065_twist_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v01065_twist_profile = v01065_twist_profile.reshape((40, 1))

# op _00Fu_power_combination_eval
# LANG: _radius, _00Ft --> _blade_solidity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01165__blade_solidity = (v01164__00Ft**1)*(v01159__radius**-1)
v01165__blade_solidity = (v01165__blade_solidity*_00Fu_coeff).reshape((1, 40, 30))

# op _004Q expand_scalar_eval
# LANG: dynamic_viscosity --> _004R
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0250_dynamic_viscosity = v0250_dynamic_viscosity.reshape((1,))
v0144__004R = np.empty((1, 40, 100))
v0144__004R.fill(v0250_dynamic_viscosity.item())
v0250_dynamic_viscosity = v0250_dynamic_viscosity.reshape((1, 1))

# op _004X_power_combination_eval
# LANG: _004W, _chord --> _004Y
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0142__004Y = (v0137__004W**1)*(v0212__chord**1)
v0142__004Y = (v0142__004Y*_004X_coeff).reshape((1, 40, 100))

# op _004a_linear_combination_eval
# LANG: _0049 --> twist_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0126_twist_profile = _004a_constant+1*v0125__0049

# op _007N_power_combination_eval
# LANG: _007M --> _007O
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0222__007O = (v0221__007M**1)
v0222__007O = (v0222__007O*_007N_coeff).reshape((1, 40, 100))

# op _00Ie_bracketed_implict_eval
# LANG: Re, _hub_radius, _rotor_radius, _pitch, _chord, _radius, _blade_solidity, _axial_inflow_velocity, _tangential_inflow_velocity --> phi_distribution, alpha_distribution, Cl, Cd
# SHAPES: (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30) --> (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.phi_bracketed_search_group
_00Ie_bracketed.set_guess(initial_guess_v01196_phi_distribution)
_00Ie_bracketed_out = _00Ie_bracketed.solve(v01165__blade_solidity, v01166__axial_inflow_velocity, v01176__tangential_inflow_velocity, v01159__radius, v01146__rotor_radius, v01145__hub_radius, v01154__chord, v01153__pitch, v01085_Re)
v01196_phi_distribution = _00Ie_bracketed_out[0]
v01197_alpha_distribution = _00Ie_bracketed_out[1]
v01198_Cl = _00Ie_bracketed_out[2]
v01199_Cd = _00Ie_bracketed_out[3]

# op _004Z_power_combination_eval
# LANG: _004Y, _004R --> Re
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0143_Re = (v0142__004Y**1)*(v0144__004R**-1)
v0143_Re = (v0143_Re*_004Z_coeff).reshape((1, 40, 100))

# op _007P_power_combination_eval
# LANG: _radius, _007O --> _blade_solidity
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_pre_process_model
v0223__blade_solidity = (v0222__007O**1)*(v0217__radius**-1)
v0223__blade_solidity = (v0223__blade_solidity*_007P_coeff).reshape((1, 40, 100))

# op _007l expand_array_eval
# LANG: twist_profile --> _pitch
# SHAPES: (40,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0126_twist_profile = v0126_twist_profile.reshape((40,))
v0211__pitch = np.einsum('b,ac->abc', v0126_twist_profile.reshape((40,)) ,np.ones((1, 100))).reshape((1, 40, 100))
v0126_twist_profile = v0126_twist_profile.reshape((40, 1))

# op _00az_bracketed_implict_eval
# LANG: Re, _hub_radius, _rotor_radius, _pitch, _chord, _radius, _blade_solidity, _axial_inflow_velocity, _tangential_inflow_velocity --> phi_distribution, alpha_distribution, Cl, Cd
# SHAPES: (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100) --> (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.phi_bracketed_search_group
_00az_bracketed.set_guess(initial_guess_v0254_phi_distribution)
_00az_bracketed_out = _00az_bracketed.solve(v0223__blade_solidity, v0224__axial_inflow_velocity, v0234__tangential_inflow_velocity, v0217__radius, v0204__rotor_radius, v0203__hub_radius, v0212__chord, v0211__pitch, v0143_Re)
v0254_phi_distribution = _00az_bracketed_out[0]
v0255_alpha_distribution = _00az_bracketed_out[1]
v0256_Cl = _00az_bracketed_out[2]
v0257_Cd = _00az_bracketed_out[3]

# op _00In_linear_combination_eval
# LANG: _rotor_radius, _radius --> _00Io
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01200__00Io = _00In_constant+1*v01146__rotor_radius+-1*v01159__radius

# op _00Ix_linear_combination_eval
# LANG: _hub_radius, _radius --> _00Iy
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01210__00Iy = _00Ix_constant+1*v01159__radius+-1*v01145__hub_radius

# op _00Ip_power_combination_eval
# LANG: _00Io --> _00Iq
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01201__00Iq = (v01200__00Io**1)
v01201__00Iq = (v01201__00Iq*_00Ip_coeff).reshape((1, 40, 30))

# op _00Iz_power_combination_eval
# LANG: _00Iy --> _00IA
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01211__00IA = (v01210__00Iy**1)
v01211__00IA = (v01211__00IA*_00Iz_coeff).reshape((1, 40, 30))

# op _00Ur_power_combination_eval
# LANG: rpm --> _00Us
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01106_rpm = v01106_rpm.reshape((1,))
v01577__00Us = (v01106_rpm**1)
v01577__00Us = (v01577__00Us*_00Ur_coeff).reshape((1,))
v01106_rpm = v01106_rpm.reshape((1, 1))

# op _00IB_power_combination_eval
# LANG: _00IA, _hub_radius --> _00IC
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01212__00IC = (v01211__00IA**1)*(v01145__hub_radius**-1)
v01212__00IC = (v01212__00IC*_00IB_coeff).reshape((1, 40, 30))

# op _00ID_sin_eval
# LANG: phi_distribution --> _00IE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01214__00IE = np.sin(v01196_phi_distribution)

# op _00Ir_power_combination_eval
# LANG: _00Iq, _radius --> _00Is
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01202__00Is = (v01201__00Iq**1)*(v01159__radius**-1)
v01202__00Is = (v01202__00Is*_00Ir_coeff).reshape((1, 40, 30))

# op _00It_sin_eval
# LANG: phi_distribution --> _00Iu
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01204__00Iu = np.sin(v01196_phi_distribution)

# op _00PH_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00PI
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v01422__00PI = (v08_rotor_disk_in_plane_1**1)
v01422__00PI = (v01422__00PI*_00PH_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _00Ut_power_combination_eval
# LANG: _00Us --> _00Uu
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01578__00Uu = (v01577__00Us**1)
v01578__00Uu = (v01578__00Uu*_00Ut_coeff).reshape((1,))

# op _00aI_linear_combination_eval
# LANG: _rotor_radius, _radius --> _00aJ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0258__00aJ = _00aI_constant+1*v0204__rotor_radius+-1*v0217__radius

# op _00aS_linear_combination_eval
# LANG: _hub_radius, _radius --> _00aT
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0268__00aT = _00aS_constant+1*v0217__radius+-1*v0203__hub_radius

# op _00IF_power_combination_eval
# LANG: _00IC, _00IE --> _00IG
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01213__00IG = (v01212__00IC**1)*(v01214__00IE**-1)
v01213__00IG = (v01213__00IG*_00IF_coeff).reshape((1, 40, 30))

# op _00Iv_power_combination_eval
# LANG: _00Is, _00Iu --> _00Iw
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01203__00Iw = (v01202__00Is**1)*(v01204__00Iu**-1)
v01203__00Iw = (v01203__00Iw*_00Iv_coeff).reshape((1, 40, 30))

# op _00PP pnorm_eval
# LANG: _00PI --> _00PQ
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01423__00PQ = np.linalg.norm(v01422__00PI.flatten(), ord=2)

# op _00PU pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00PV
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01425__00PV = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00Uv_power_combination_eval
# LANG: _00Uu --> _00Uw
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01579__00Uw = (v01578__00Uu**1)
v01579__00Uw = (v01579__00Uw*_00Uv_coeff).reshape((1,))

# op _00aK_power_combination_eval
# LANG: _00aJ --> _00aL
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0259__00aL = (v0258__00aJ**1)
v0259__00aL = (v0259__00aL*_00aK_coeff).reshape((1, 40, 100))

# op _00aU_power_combination_eval
# LANG: _00aT --> _00aV
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0269__00aV = (v0268__00aT**1)
v0269__00aV = (v0269__00aV*_00aU_coeff).reshape((1, 40, 100))

# op _00IH_linear_combination_eval
# LANG: _00Iw --> _00II
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01205__00II = _00IH_constant+-1*v01203__00Iw

# op _00IP_linear_combination_eval
# LANG: _00IG --> _00IQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01215__00IQ = _00IP_constant+-1*v01213__00IG

# op _00PR_power_combination_eval
# LANG: _00PQ --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01424_propeller_radius = (v01423__00PQ**1)
v01424_propeller_radius = (v01424_propeller_radius*_00PR_coeff).reshape((1,))

# op _00PW reshape_eval
# LANG: _00PV --> _00PX
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01426__00PX = v01425__00PV.reshape((40, 1))

# op _00UW expand_array_eval
# LANG: nondim_sectional_radius --> _00UX
# SHAPES: (40,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01569__00UX = np.einsum('d,abce->abcde', v01568_nondim_sectional_radius.reshape((40,)) ,np.ones((1, 2, 3, 11))).reshape((1, 2, 3, 40, 11))

# op _00UY expand_scalar_eval
# LANG: _00Uw --> _00UZ
# SHAPES: (1,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01580__00UZ = np.empty((1, 2, 3, 40, 11))
v01580__00UZ.fill(v01579__00Uw.item())

# op _00aM_power_combination_eval
# LANG: _00aL, _radius --> _00aN
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0260__00aN = (v0259__00aL**1)*(v0217__radius**-1)
v0260__00aN = (v0260__00aN*_00aM_coeff).reshape((1, 40, 100))

# op _00aO_sin_eval
# LANG: phi_distribution --> _00aP
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0262__00aP = np.sin(v0254_phi_distribution)

# op _00aW_power_combination_eval
# LANG: _00aV, _hub_radius --> _00aX
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0270__00aX = (v0269__00aV**1)*(v0203__hub_radius**-1)
v0270__00aX = (v0270__00aX*_00aW_coeff).reshape((1, 40, 100))

# op _00aY_sin_eval
# LANG: phi_distribution --> _00aZ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0272__00aZ = np.sin(v0254_phi_distribution)

# op _00IJ exp_eval
# LANG: _00II --> _00IK
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01206__00IK = np.exp(v01205__00II)

# op _00IR exp_eval
# LANG: _00IQ --> _00IS
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01216__00IS = np.exp(v01215__00IQ)

# op _00PY_power_combination_eval
# LANG: _00PX --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01427_chord_profile = (v01426__00PX**1)
v01427_chord_profile = (v01427_chord_profile*_00PY_coeff).reshape((40, 1))

# op _00U_ expand_scalar_eval
# LANG: propeller_radius --> _00V0
# SHAPES: (1,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01589__00V0 = np.empty((1, 2, 3, 40, 11))
v01589__00V0.fill(v01424_propeller_radius.item())

# op _00V9_decompose_eval
# LANG: _00UX --> _00Va
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01587__00Va = ((v01569__00UX.flatten())[src_indices__00Va__00V9]).reshape((1, 2, 3, 40, 10))

# op _00Vb_decompose_eval
# LANG: _00UZ --> _00Vc
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01581__00Vc = ((v01580__00UZ.flatten())[src_indices__00Vc__00Vb]).reshape((1, 2, 3, 40, 10))

# op _00aQ_power_combination_eval
# LANG: _00aN, _00aP --> _00aR
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0261__00aR = (v0260__00aN**1)*(v0262__00aP**-1)
v0261__00aR = (v0261__00aR*_00aQ_coeff).reshape((1, 40, 100))

# op _00a__power_combination_eval
# LANG: _00aX, _00aZ --> _00b0
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0271__00b0 = (v0270__00aX**1)*(v0272__00aZ**-1)
v0271__00b0 = (v0271__00b0*_00a__coeff).reshape((1, 40, 100))

# op _00IL arccos_eval
# LANG: _00IK --> _00IM
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01207__00IM = np.arccos(v01206__00IK)

# op _00IT arccos_eval
# LANG: _00IS --> _00IU
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01217__00IU = np.arccos(v01216__00IS)

# op _00V3 expand_array_eval
# LANG: chord_profile --> _00V4
# SHAPES: (40,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01427_chord_profile = v01427_chord_profile.reshape((40,))
v01583__00V4 = np.einsum('d,abce->abcde', v01427_chord_profile.reshape((40,)) ,np.ones((1, 2, 3, 11))).reshape((1, 2, 3, 40, 11))
v01427_chord_profile = v01427_chord_profile.reshape((40, 1))

# op _00VO_decompose_eval
# LANG: lam_var --> _00VP
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01575__00VP = ((v01574_lam_var.flatten())[src_indices__00VP__00VO]).reshape((1, 2, 3, 40, 10))

# op _00VQ_power_combination_eval
# LANG: _00Vc, _00Va --> _00VR
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01586__00VR = (v01581__00Vc**1)*(v01587__00Va**1)
v01586__00VR = (v01586__00VR*_00VQ_coeff).reshape((1, 2, 3, 40, 10))

# op _00Vd_decompose_eval
# LANG: _00V0 --> _00Ve
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01590__00Ve = ((v01589__00V0.flatten())[src_indices__00Ve__00Vd]).reshape((1, 2, 3, 40, 10))

# op _00b1_linear_combination_eval
# LANG: _00aR --> _00b2
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0263__00b2 = _00b1_constant+-1*v0261__00aR

# op _00b9_linear_combination_eval
# LANG: _00b0 --> _00ba
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0273__00ba = _00b9_constant+-1*v0271__00b0

# op _00IN_power_combination_eval
# LANG: _00IM --> _00IO
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01208__00IO = (v01207__00IM**1)
v01208__00IO = (v01208__00IO*_00IN_coeff).reshape((1, 40, 30))

# op _00IV_power_combination_eval
# LANG: _00IU --> _00IW
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01218__00IW = (v01217__00IU**1)
v01218__00IW = (v01218__00IW*_00IV_coeff).reshape((1, 40, 30))

# op _00Jt_sin_eval
# LANG: phi_distribution --> _00Ju
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01233__00Ju = np.sin(v01196_phi_distribution)

# op _00Jx_cos_eval
# LANG: phi_distribution --> _00Jy
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01236__00Jy = np.cos(v01196_phi_distribution)

# op _00RI_power_combination_eval
# LANG: altitude --> _00RJ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01478__00RJ = (v0990_hover_altitude**1)
v01478__00RJ = (v01478__00RJ*_00RI_coeff).reshape((1,))

# op _00VS_power_combination_eval
# LANG: _00VR, _00Ve --> _00VT
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01588__00VT = (v01586__00VR**1)*(v01590__00Ve**1)
v01588__00VT = (v01588__00VT*_00VS_coeff).reshape((1, 2, 3, 40, 10))

# op _00VU_power_combination_eval
# LANG: _00VP, _00Vc --> _00VV
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01576__00VV = (v01575__00VP**1)*(v01581__00Vc**1)
v01576__00VV = (v01576__00VV*_00VU_coeff).reshape((1, 2, 3, 40, 10))

# op _00Vh_decompose_eval
# LANG: _00V4 --> _00Vi
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01584__00Vi = ((v01583__00V4.flatten())[src_indices__00Vi__00Vh]).reshape((1, 2, 3, 40, 10))

# op _00b3 exp_eval
# LANG: _00b2 --> _00b4
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0264__00b4 = np.exp(v0263__00b2)

# op _00bb exp_eval
# LANG: _00ba --> _00bc
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0274__00bc = np.exp(v0273__00ba)

# op _00IX_power_combination_eval
# LANG: _00IO, _00IW --> prandtl_loss_factor
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01209_prandtl_loss_factor = (v01208__00IO**1)*(v01218__00IW**1)
v01209_prandtl_loss_factor = (v01209_prandtl_loss_factor*_00IX_coeff).reshape((1, 40, 30))

# op _00Jj_cos_eval
# LANG: phi_distribution --> _00Jk
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01240__00Jk = np.cos(v01196_phi_distribution)

# op _00Jn_sin_eval
# LANG: phi_distribution --> _00Jo
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01243__00Jo = np.sin(v01196_phi_distribution)

# op _00Jv_power_combination_eval
# LANG: _00Ju, Cl --> _00Jw
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01232__00Jw = (v01198_Cl**1)*(v01233__00Ju**1)
v01232__00Jw = (v01232__00Jw*_00Jv_coeff).reshape((1, 40, 30))

# op _00Jz_power_combination_eval
# LANG: _00Jy, Cd --> _00JA
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01235__00JA = (v01199_Cd**1)*(v01236__00Jy**1)
v01235__00JA = (v01235__00JA*_00Jz_coeff).reshape((1, 40, 30))

# op _00KE_power_combination_eval
# LANG: phi_distribution --> _00KF
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01259__00KF = (v01196_phi_distribution**1)
v01259__00KF = (v01259__00KF*_00KE_coeff).reshape((1, 40, 30))

# op _00RK_linear_combination_eval
# LANG: _00RJ --> _00RL
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01479__00RL = _00RK_constant+-1*v01478__00RJ

# op _00VW_power_combination_eval
# LANG: _00VV, _00Vi --> _00VX
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01582__00VX = (v01576__00VV**1)*(v01584__00Vi**1)
v01582__00VX = (v01582__00VX*_00VW_coeff).reshape((1, 2, 3, 40, 10))

# op _00VY_power_combination_eval
# LANG: _00VT --> _00VZ
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01591__00VZ = (v01588__00VT**1)
v01591__00VZ = (v01591__00VZ*_00VY_coeff).reshape((1, 2, 3, 40, 10))

# op _00b5 arccos_eval
# LANG: _00b4 --> _00b6
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0265__00b6 = np.arccos(v0264__00b4)

# op _00bd arccos_eval
# LANG: _00bc --> _00be
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0275__00be = np.arccos(v0274__00bc)

# op _00JB_linear_combination_eval
# LANG: _00Jw, _00JA --> _00JC
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01234__00JC = _00JB_constant+1*v01232__00Jw+1*v01235__00JA

# op _00Jl_power_combination_eval
# LANG: _00Jk, Cl --> _00Jm
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01239__00Jm = (v01198_Cl**1)*(v01240__00Jk**1)
v01239__00Jm = (v01239__00Jm*_00Jl_coeff).reshape((1, 40, 30))

# op _00Jp_power_combination_eval
# LANG: _00Jo, Cd --> _00Jq
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01242__00Jq = (v01199_Cd**1)*(v01243__00Jo**1)
v01242__00Jq = (v01242__00Jq*_00Jp_coeff).reshape((1, 40, 30))

# op _00KC_power_combination_eval
# LANG: prandtl_loss_factor --> _00KD
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01257__00KD = (v01209_prandtl_loss_factor**1)
v01257__00KD = (v01257__00KD*_00KC_coeff).reshape((1, 40, 30))

# op _00KG_sin_eval
# LANG: _00KF --> _00KH
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01260__00KH = np.sin(v01259__00KF)

# op _00Ke_power_combination_eval
# LANG: prandtl_loss_factor --> _00Kf
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01246__00Kf = (v01209_prandtl_loss_factor**1)
v01246__00Kf = (v01246__00Kf*_00Ke_coeff).reshape((1, 40, 30))

# op _00Kg_sin_eval
# LANG: phi_distribution --> _00Kh
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01248__00Kh = np.sin(v01196_phi_distribution)

# op _00Kw_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00Kx
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01253__00Kx = (v01176__tangential_inflow_velocity**1)
v01253__00Kx = (v01253__00Kx*_00Kw_coeff).reshape((1, 40, 30))

# op _00RM_power_combination_eval
# LANG: _00RL --> _00RN
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01480__00RN = (v01479__00RL**1)
v01480__00RN = (v01480__00RN*_00RM_coeff).reshape((1,))

# op _00V__power_combination_eval
# LANG: _00VX, _00VZ --> _00W0
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01585__00W0 = (v01582__00VX**1)*(v01591__00VZ**-1)
v01585__00W0 = (v01585__00W0*_00V__coeff).reshape((1, 2, 3, 40, 10))

# op _00b7_power_combination_eval
# LANG: _00b6 --> _00b8
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0266__00b8 = (v0265__00b6**1)
v0266__00b8 = (v0266__00b8*_00b7_coeff).reshape((1, 40, 100))

# op _00bO_sin_eval
# LANG: phi_distribution --> _00bP
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0291__00bP = np.sin(v0254_phi_distribution)

# op _00bS_cos_eval
# LANG: phi_distribution --> _00bT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0294__00bT = np.cos(v0254_phi_distribution)

# op _00bf_power_combination_eval
# LANG: _00be --> _00bg
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0276__00bg = (v0275__00be**1)
v0276__00bg = (v0276__00bg*_00bf_coeff).reshape((1, 40, 100))

# op _00Jr_linear_combination_eval
# LANG: _00Jm, _00Jq --> _00Js
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01241__00Js = _00Jr_constant+1*v01239__00Jm+-1*v01242__00Jq

# op _00KI_power_combination_eval
# LANG: _00KD, _00KH --> _00KJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01258__00KJ = (v01257__00KD**1)*(v01260__00KH**1)
v01258__00KJ = (v01258__00KJ*_00KI_coeff).reshape((1, 40, 30))

# op _00KK_power_combination_eval
# LANG: _00JC, _blade_solidity --> _00KL
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01262__00KL = (v01165__blade_solidity**1)*(v01234__00JC**1)
v01262__00KL = (v01262__00KL*_00KK_coeff).reshape((1, 40, 30))

# op _00Ki_power_combination_eval
# LANG: _00Kf, _00Kh --> _00Kj
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01247__00Kj = (v01246__00Kf**1)*(v01248__00Kh**1)
v01247__00Kj = (v01247__00Kj*_00Ki_coeff).reshape((1, 40, 30))

# op _00Kk_cos_eval
# LANG: phi_distribution --> _00Kl
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01250__00Kl = np.cos(v01196_phi_distribution)

# op _00Ky_power_combination_eval
# LANG: _00Kx, _blade_solidity --> _00Kz
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01254__00Kz = (v01253__00Kx**1)*(v01165__blade_solidity**1)
v01254__00Kz = (v01254__00Kz*_00Ky_coeff).reshape((1, 40, 30))

# op _00RO_linear_combination_eval
# LANG: _00RN --> temperature
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01481_temperature = _00RO_constant+1*v01480__00RN

# op _00Vm_decompose_eval
# LANG: phi --> _00Vn
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01564__00Vn = ((v01196_phi_distribution.flatten())[src_indices__00Vn__00Vm]).reshape((1, 40, 1))

# op _00XI_bessel_eval
# LANG: _00W0 --> _00XJ
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01671__00XJ=_00XI_bessel_eval(0,v01585__00W0)

# op _00XK_bessel_eval
# LANG: _00W0 --> _00XL
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01673__00XL=_00XK_bessel_eval(1,v01585__00W0)

# op _00bE_cos_eval
# LANG: phi_distribution --> _00bF
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0298__00bF = np.cos(v0254_phi_distribution)

# op _00bI_sin_eval
# LANG: phi_distribution --> _00bJ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0301__00bJ = np.sin(v0254_phi_distribution)

# op _00bQ_power_combination_eval
# LANG: _00bP, Cl --> _00bR
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0290__00bR = (v0256_Cl**1)*(v0291__00bP**1)
v0290__00bR = (v0290__00bR*_00bQ_coeff).reshape((1, 40, 100))

# op _00bU_power_combination_eval
# LANG: _00bT, Cd --> _00bV
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0293__00bV = (v0257_Cd**1)*(v0294__00bT**1)
v0293__00bV = (v0293__00bV*_00bU_coeff).reshape((1, 40, 100))

# op _00bh_power_combination_eval
# LANG: _00b8, _00bg --> prandtl_loss_factor
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.prandtl_loss_factor_model
v0267_prandtl_loss_factor = (v0266__00b8**1)*(v0276__00bg**1)
v0267_prandtl_loss_factor = (v0267_prandtl_loss_factor*_00bh_coeff).reshape((1, 40, 100))

# op _00cZ_power_combination_eval
# LANG: phi_distribution --> _00c_
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0317__00c_ = (v0254_phi_distribution**1)
v0317__00c_ = (v0317__00c_*_00cZ_coeff).reshape((1, 40, 100))

# op _00KA_power_combination_eval
# LANG: _00JC, _00Kz --> _00KB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01255__00KB = (v01254__00Kz**1)*(v01234__00JC**1)
v01255__00KB = (v01255__00KB*_00KA_coeff).reshape((1, 40, 30))

# op _00KM_linear_combination_eval
# LANG: _00KJ, _00KL --> _00KN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01261__00KN = _00KM_constant+1*v01258__00KJ+1*v01262__00KL

# op _00Ka_power_combination_eval
# LANG: _00Js, _blade_solidity --> _00Kb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01238__00Kb = (v01165__blade_solidity**1)*(v01241__00Js**1)
v01238__00Kb = (v01238__00Kb*_00Ka_coeff).reshape((1, 40, 30))

# op _00Km_power_combination_eval
# LANG: _00Kj, _00Kl --> _00Kn
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01249__00Kn = (v01247__00Kj**1)*(v01250__00Kl**1)
v01249__00Kn = (v01249__00Kn*_00Km_coeff).reshape((1, 40, 30))

# op _00Ko_power_combination_eval
# LANG: _00JC, _blade_solidity --> _00Kp
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01252__00Kp = (v01165__blade_solidity**1)*(v01234__00JC**1)
v01252__00Kp = (v01252__00Kp*_00Ko_coeff).reshape((1, 40, 30))

# op _00RQ_power_combination_eval
# LANG: temperature --> _00RR
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01482__00RR = (v01481_temperature**1)
v01482__00RR = (v01482__00RR*_00RQ_coeff).reshape((1,))

# op _00Vo reshape_eval
# LANG: _00Vn --> _00Vp
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01565__00Vp = v01564__00Vn.reshape((1, 40))

# op _00XE_bessel_eval
# LANG: _00W0 --> _00XF
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01668__00XF=_00XE_bessel_eval(1,v01585__00W0)

# op _00XM_power_combination_eval
# LANG: _00XJ, _00XL --> _00XN
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01672__00XN = (v01671__00XJ**1)*(v01673__00XL**1)
v01672__00XN = (v01672__00XN*_00XM_coeff).reshape((1, 2, 3, 40, 10))

# op _00XO_bessel_eval
# LANG: _00W0 --> _00XP
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01675__00XP=_00XO_bessel_eval(1,v01585__00W0)

# op _00XU_bessel_eval
# LANG: _00W0 --> _00XV
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01677__00XV=_00XU_bessel_eval(1,v01585__00W0)

# op _00bG_power_combination_eval
# LANG: _00bF, Cl --> _00bH
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0297__00bH = (v0256_Cl**1)*(v0298__00bF**1)
v0297__00bH = (v0297__00bH*_00bG_coeff).reshape((1, 40, 100))

# op _00bK_power_combination_eval
# LANG: _00bJ, Cd --> _00bL
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0300__00bL = (v0257_Cd**1)*(v0301__00bJ**1)
v0300__00bL = (v0300__00bL*_00bK_coeff).reshape((1, 40, 100))

# op _00bW_linear_combination_eval
# LANG: _00bR, _00bV --> _00bX
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0292__00bX = _00bW_constant+1*v0290__00bR+1*v0293__00bV

# op _00cB_sin_eval
# LANG: phi_distribution --> _00cC
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0306__00cC = np.sin(v0254_phi_distribution)

# op _00cR_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00cS
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0311__00cS = (v0234__tangential_inflow_velocity**1)
v0311__00cS = (v0311__00cS*_00cR_coeff).reshape((1, 40, 100))

# op _00cX_power_combination_eval
# LANG: prandtl_loss_factor --> _00cY
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0315__00cY = (v0267_prandtl_loss_factor**1)
v0315__00cY = (v0315__00cY*_00cX_coeff).reshape((1, 40, 100))

# op _00cz_power_combination_eval
# LANG: prandtl_loss_factor --> _00cA
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0304__00cA = (v0267_prandtl_loss_factor**1)
v0304__00cA = (v0304__00cA*_00cz_coeff).reshape((1, 40, 100))

# op _00d0_sin_eval
# LANG: _00c_ --> _00d1
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0318__00d1 = np.sin(v0317__00c_)

# op _00KO_power_combination_eval
# LANG: _00KB, _00KN --> _ut
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01256__ut = (v01255__00KB**1)*(v01261__00KN**-1)
v01256__ut = (v01256__ut*_00KO_coeff).reshape((1, 40, 30))

# op _00Kc_power_combination_eval
# LANG: _00Kb, _tangential_inflow_velocity --> _00Kd
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01244__00Kd = (v01238__00Kb**1)*(v01176__tangential_inflow_velocity**1)
v01244__00Kd = (v01244__00Kd*_00Kc_coeff).reshape((1, 40, 30))

# op _00Kq_linear_combination_eval
# LANG: _00Kn, _00Kp --> _00Kr
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01251__00Kr = _00Kq_constant+1*v01249__00Kn+1*v01252__00Kp

# op _00RS_power_combination_eval
# LANG: _00RR --> _00RT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01483__00RT = (v01482__00RR**5.258643795229161)
v01483__00RT = (v01483__00RT*_00RS_coeff).reshape((1,))

# op _00Vq expand_array_eval
# LANG: _00Vp --> _00Vr
# SHAPES: (1, 40) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01566__00Vr = np.einsum('ad,bce->abcde', v01565__00Vp.reshape((1, 40)) ,np.ones((2, 3, 11))).reshape((1, 2, 3, 40, 11))

# op _00XG_power_combination_eval
# LANG: _00XF --> _00XH
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01669__00XH = (v01668__00XF**3)
v01669__00XH = (v01669__00XH*_00XG_coeff).reshape((1, 2, 3, 40, 10))

# op _00XQ_power_combination_eval
# LANG: _00XN, _00XP --> _00XR
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01674__00XR = (v01672__00XN**1)*(v01675__00XP**1)
v01674__00XR = (v01674__00XR*_00XQ_coeff).reshape((1, 2, 3, 40, 10))

# op _00XW_power_combination_eval
# LANG: _00XV --> _00XX
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01678__00XX = (v01677__00XV**2)
v01678__00XX = (v01678__00XX*_00XW_coeff).reshape((1, 2, 3, 40, 10))

# op _00XY_bessel_eval
# LANG: _00W0 --> _00XZ
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01680__00XZ=_00XY_bessel_eval(0,v01585__00W0)

# op _00Y3_bessel_eval
# LANG: _00W0 --> _00Y4
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01682__00Y4=_00Y3_bessel_eval(0,v01585__00W0)

# op _00Y5_bessel_eval
# LANG: _00W0 --> _00Y6
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01684__00Y6=_00Y5_bessel_eval(0,v01585__00W0)

# op _00bM_linear_combination_eval
# LANG: _00bH, _00bL --> _00bN
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0299__00bN = _00bM_constant+1*v0297__00bH+-1*v0300__00bL

# op _00cD_power_combination_eval
# LANG: _00cA, _00cC --> _00cE
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0305__00cE = (v0304__00cA**1)*(v0306__00cC**1)
v0305__00cE = (v0305__00cE*_00cD_coeff).reshape((1, 40, 100))

# op _00cF_cos_eval
# LANG: phi_distribution --> _00cG
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0308__00cG = np.cos(v0254_phi_distribution)

# op _00cT_power_combination_eval
# LANG: _00cS, _blade_solidity --> _00cU
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0312__00cU = (v0311__00cS**1)*(v0223__blade_solidity**1)
v0312__00cU = (v0312__00cU*_00cT_coeff).reshape((1, 40, 100))

# op _00cf_power_combination_eval
# LANG: prandtl_loss_factor --> _00cg
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0283__00cg = (v0267_prandtl_loss_factor**1)
v0283__00cg = (v0283__00cg*_00cf_coeff).reshape((1, 40, 100))

# op _00ch_sin_eval
# LANG: phi_distribution --> _00ci
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0285__00ci = np.sin(v0254_phi_distribution)

# op _00d2_power_combination_eval
# LANG: _00cY, _00d1 --> _00d3
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0316__00d3 = (v0315__00cY**1)*(v0318__00d1**1)
v0316__00d3 = (v0316__00d3*_00d2_coeff).reshape((1, 40, 100))

# op _00d4_power_combination_eval
# LANG: _00bX, _blade_solidity --> _00d5
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0320__00d5 = (v0223__blade_solidity**1)*(v0292__00bX**1)
v0320__00d5 = (v0320__00d5*_00d4_coeff).reshape((1, 40, 100))

# op _00JV_power_combination_eval
# LANG: prandtl_loss_factor --> _00JW
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01225__00JW = (v01209_prandtl_loss_factor**1)
v01225__00JW = (v01225__00JW*_00JV_coeff).reshape((1, 40, 30))

# op _00JX_sin_eval
# LANG: phi_distribution --> _00JY
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01227__00JY = np.sin(v01196_phi_distribution)

# op _00Ks_power_combination_eval
# LANG: _00Kd, _00Kr --> _00Kt
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01245__00Kt = (v01244__00Kd**1)*(v01251__00Kr**-1)
v01245__00Kt = (v01245__00Kt*_00Ks_coeff).reshape((1, 40, 30))

# op _00Mo_power_combination_eval
# LANG: _ut --> _00Mp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01325__00Mp = (v01256__ut**1)
v01325__00Mp = (v01325__00Mp*_00Mo_coeff).reshape((1, 40, 30))

# op _00RU_power_combination_eval
# LANG: _00RT --> pressure
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01484_pressure = (v01483__00RT**1)
v01484_pressure = (v01484_pressure*_00RU_coeff).reshape((1,))

# op _00Sm expand_scalar_eval
# LANG: Vx --> _00Sn
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01495__00Sn = np.empty((1, 1))
v01495__00Sn.fill(v0977_u.item())

# op _00Sp expand_scalar_eval
# LANG: Vy --> _00Sq
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01497__00Sq = np.empty((1, 1))
v01497__00Sq.fill(v0978_v.item())

# op _00Sr expand_scalar_eval
# LANG: Vz --> _00Ss
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01498__00Ss = np.empty((1, 1))
v01498__00Ss.fill(v0979_w.item())

# op _00Vs_power_combination_eval
# LANG: _00Vr, _00UX --> lambda_test
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01567_lambda_test = (v01566__00Vr**1)*(v01569__00UX**1)
v01567_lambda_test = (v01567_lambda_test*_00Vs_coeff).reshape((1, 2, 3, 40, 11))

# op _00XS_linear_combination_eval
# LANG: _00XH, _00XR --> _00XT
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01670__00XT = _00XS_constant+1*v01669__00XH+1*v01674__00XR

# op _00X__power_combination_eval
# LANG: _00XX, _00XZ --> _00Y0
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01679__00Y0 = (v01678__00XX**1)*(v01680__00XZ**1)
v01679__00Y0 = (v01679__00Y0*_00X__coeff).reshape((1, 2, 3, 40, 10))

# op _00Y7_power_combination_eval
# LANG: _00Y4, _00Y6 --> _00Y8
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01683__00Y8 = (v01682__00Y4**1)*(v01684__00Y6**1)
v01683__00Y8 = (v01683__00Y8*_00Y7_coeff).reshape((1, 2, 3, 40, 10))

# op _00Y9_bessel_eval
# LANG: _00W0 --> _00Ya
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01686__00Ya=_00Y9_bessel_eval(1,v01585__00W0)

# op _00Yf_bessel_eval
# LANG: _00W0 --> _00Yg
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01688__00Yg=_00Yf_bessel_eval(0,v01585__00W0)

# op _00c5_power_combination_eval
# LANG: prandtl_loss_factor --> _00c6
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0277__00c6 = (v0267_prandtl_loss_factor**1)
v0277__00c6 = (v0277__00c6*_00c5_coeff).reshape((1, 40, 100))

# op _00c9_sin_eval
# LANG: phi_distribution --> _00ca
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0280__00ca = np.sin(v0254_phi_distribution)

# op _00cH_power_combination_eval
# LANG: _00cE, _00cG --> _00cI
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0307__00cI = (v0305__00cE**1)*(v0308__00cG**1)
v0307__00cI = (v0307__00cI*_00cH_coeff).reshape((1, 40, 100))

# op _00cJ_power_combination_eval
# LANG: _00bX, _blade_solidity --> _00cK
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0310__00cK = (v0223__blade_solidity**1)*(v0292__00bX**1)
v0310__00cK = (v0310__00cK*_00cJ_coeff).reshape((1, 40, 100))

# op _00cV_power_combination_eval
# LANG: _00bX, _00cU --> _00cW
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0313__00cW = (v0312__00cU**1)*(v0292__00bX**1)
v0313__00cW = (v0313__00cW*_00cV_coeff).reshape((1, 40, 100))

# op _00cj_power_combination_eval
# LANG: _00cg, _00ci --> _00ck
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0284__00ck = (v0283__00cg**1)*(v0285__00ci**1)
v0284__00ck = (v0284__00ck*_00cj_coeff).reshape((1, 40, 100))

# op _00cl_cos_eval
# LANG: phi_distribution --> _00cm
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0287__00cm = np.cos(v0254_phi_distribution)

# op _00cv_power_combination_eval
# LANG: _00bN, _blade_solidity --> _00cw
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0296__00cw = (v0223__blade_solidity**1)*(v0299__00bN**1)
v0296__00cw = (v0296__00cw*_00cv_coeff).reshape((1, 40, 100))

# op _00d6_linear_combination_eval
# LANG: _00d3, _00d5 --> _00d7
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0319__00d7 = _00d6_constant+1*v0316__00d3+1*v0320__00d5

# op _000o_sparsematmat_eval
# LANG: design_geometry --> _000p
# SHAPES: (16250, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v011__000p = _000o_sparsematmat_eval_mat@v05_design_geometry

# op _00JL_power_combination_eval
# LANG: prandtl_loss_factor --> _00JM
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01219__00JM = (v01209_prandtl_loss_factor**1)
v01219__00JM = (v01219__00JM*_00JL_coeff).reshape((1, 40, 30))

# op _00JP_sin_eval
# LANG: phi_distribution --> _00JQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01222__00JQ = np.sin(v01196_phi_distribution)

# op _00JZ_power_combination_eval
# LANG: _00JW, _00JY --> _00J_
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01226__00J_ = (v01225__00JW**1)*(v01227__00JY**1)
v01226__00J_ = (v01226__00J_*_00JZ_coeff).reshape((1, 40, 30))

# op _00K0_cos_eval
# LANG: phi_distribution --> _00K1
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01229__00K1 = np.cos(v01196_phi_distribution)

# op _00Ku_linear_combination_eval
# LANG: _00Kt, _axial_inflow_velocity --> _ux_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01237__ux_2 = _00Ku_constant+1*v01166__axial_inflow_velocity+1*v01245__00Kt

# op _00Mg_power_combination_eval
# LANG: Cd --> _00Mh
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01318__00Mh = (v01199_Cd**1)
v01318__00Mh = (v01318__00Mh*_00Mg_coeff).reshape((1, 40, 30))

# op _00Mq_linear_combination_eval
# LANG: _00Mp, _tangential_inflow_velocity --> _00Mr
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01324__00Mr = _00Mq_constant+1*v01176__tangential_inflow_velocity+-1*v01325__00Mp

# op _00RW_power_combination_eval
# LANG: pressure --> _00RX
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01485__00RX = (v01484_pressure**1)
v01485__00RX = (v01485__00RX*_00RW_coeff).reshape((1,))

# op _00So_indexed_passthrough_eval
# LANG: _00Sn, _00Sq, _00Ss --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01496_V_aircraft__temp[i_v01495__00Sn__00So_indexed_passthrough_eval] = v01495__00Sn.flatten()
v01496_V_aircraft = v01496_V_aircraft__temp.copy()
v01496_V_aircraft__temp[i_v01497__00Sq__00So_indexed_passthrough_eval] = v01497__00Sq.flatten()
v01496_V_aircraft = v01496_V_aircraft__temp.copy()
v01496_V_aircraft__temp[i_v01498__00Ss__00So_indexed_passthrough_eval] = v01498__00Ss.flatten()
v01496_V_aircraft = v01496_V_aircraft__temp.copy()

# op _00Vw_decompose_eval
# LANG: lambda_test --> _00Vx
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01652__00Vx = ((v01567_lambda_test.flatten())[src_indices__00Vx__00Vw]).reshape((1, 2, 3, 40, 10))

# op _00W3_bessel_eval
# LANG: _00W0 --> _00W4
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01594__00W4=_00W3_bessel_eval(1,v01585__00W0)

# op _00W9_bessel_eval
# LANG: _00W0 --> _00Wa
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01597__00Wa=_00W9_bessel_eval(1,v01585__00W0)

# op _00WJ_bessel_eval
# LANG: _00W0 --> _00WK
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01616__00WK=_00WJ_bessel_eval(1,v01585__00W0)

# op _00WP_bessel_eval
# LANG: _00W0 --> _00WQ
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01619__00WQ=_00WP_bessel_eval(0,v01585__00W0)

# op _00Y1_linear_combination_eval
# LANG: _00XT, _00Y0 --> _00Y2
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01676__00Y2 = _00Y1_constant+1*v01670__00XT+1*v01679__00Y0

# op _00Yb_power_combination_eval
# LANG: _00Y8, _00Ya --> _00Yc
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01685__00Yc = (v01683__00Y8**1)*(v01686__00Ya**1)
v01685__00Yc = (v01685__00Yc*_00Yb_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yh_power_combination_eval
# LANG: _00Yg --> _00Yi
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01689__00Yi = (v01688__00Yg**2)
v01689__00Yi = (v01689__00Yi*_00Yh_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yj_bessel_eval
# LANG: _00W0 --> _00Yk
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01691__00Yk=_00Yj_bessel_eval(1,v01585__00W0)

# op _00Yp_bessel_eval
# LANG: _00W0 --> _00Yq
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01693__00Yq=_00Yp_bessel_eval(0,v01585__00W0)

# op _00Yr_bessel_eval
# LANG: _00W0 --> _00Ys
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01695__00Ys=_00Yr_bessel_eval(1,v01585__00W0)

# op _00c7_power_combination_eval
# LANG: _00c6, _tangential_inflow_velocity --> _00c8
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0278__00c8 = (v0277__00c6**1)*(v0234__tangential_inflow_velocity**1)
v0278__00c8 = (v0278__00c8*_00c7_coeff).reshape((1, 40, 100))

# op _00cL_linear_combination_eval
# LANG: _00cI, _00cK --> _00cM
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0309__00cM = _00cL_constant+1*v0307__00cI+1*v0310__00cK

# op _00cb_power_combination_eval
# LANG: _00ca --> _00cc
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0281__00cc = (v0280__00ca**2)
v0281__00cc = (v0281__00cc*_00cb_coeff).reshape((1, 40, 100))

# op _00cn_power_combination_eval
# LANG: _00ck, _00cm --> _00co
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0286__00co = (v0284__00ck**1)*(v0287__00cm**1)
v0286__00co = (v0286__00co*_00cn_coeff).reshape((1, 40, 100))

# op _00cp_power_combination_eval
# LANG: _00bX, _blade_solidity --> _00cq
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0289__00cq = (v0223__blade_solidity**1)*(v0292__00bX**1)
v0289__00cq = (v0289__00cq*_00cp_coeff).reshape((1, 40, 100))

# op _00cx_power_combination_eval
# LANG: _00cw, _tangential_inflow_velocity --> _00cy
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0302__00cy = (v0296__00cw**1)*(v0234__tangential_inflow_velocity**1)
v0302__00cy = (v0302__00cy*_00cx_coeff).reshape((1, 40, 100))

# op _00d8_power_combination_eval
# LANG: _00cW, _00d7 --> _ut
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0314__ut = (v0313__00cW**1)*(v0319__00d7**-1)
v0314__ut = (v0314__ut*_00d8_coeff).reshape((1, 40, 100))

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

# op _000q reshape_eval
# LANG: _000p --> rotor_disk_origin
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v012_rotor_disk_origin = v011__000p.reshape((1, 3))

# op _00DD_power_combination_eval
# LANG: propeller_radius --> _00DE
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01137__00DE = (v01068_propeller_radius**1)
v01137__00DE = (v01137__00DE*_00DD_coeff).reshape((1,))

# op _00JN_power_combination_eval
# LANG: _00JM, _tangential_inflow_velocity --> _00JO
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01220__00JO = (v01219__00JM**1)*(v01176__tangential_inflow_velocity**1)
v01220__00JO = (v01220__00JO*_00JN_coeff).reshape((1, 40, 30))

# op _00JR_power_combination_eval
# LANG: _00JQ --> _00JS
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01223__00JS = (v01222__00JQ**2)
v01223__00JS = (v01223__00JS*_00JR_coeff).reshape((1, 40, 30))

# op _00Jd expand_scalar_eval
# LANG: density --> _00Je
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01187_density = v01187_density.reshape((1,))
v01265__00Je = np.empty((1, 40, 30))
v01265__00Je.fill(v01187_density.item())
v01187_density = v01187_density.reshape((1, 1))

# op _00K2_power_combination_eval
# LANG: _00J_, _00K1 --> _00K3
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01228__00K3 = (v01226__00J_**1)*(v01229__00K1**1)
v01228__00K3 = (v01228__00K3*_00K2_coeff).reshape((1, 40, 30))

# op _00K4_power_combination_eval
# LANG: _00JC, _blade_solidity --> _00K5
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01231__00K5 = (v01165__blade_solidity**1)*(v01234__00JC**1)
v01231__00K5 = (v01231__00K5*_00K4_coeff).reshape((1, 40, 30))

# op _00Mi_power_combination_eval
# LANG: _00Mh --> _00Mj
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01319__00Mj = (v01318__00Mh**1)
v01319__00Mj = (v01319__00Mj*_00Mi_coeff).reshape((1, 40, 30))

# op _00Mm_power_combination_eval
# LANG: _ux_2 --> _00Mn
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01322__00Mn = (v01237__ux_2**2)
v01322__00Mn = (v01322__00Mn*_00Mm_coeff).reshape((1, 40, 30))

# op _00Ms_power_combination_eval
# LANG: _00Mr --> _00Mt
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01326__00Mt = (v01324__00Mr**2)
v01326__00Mt = (v01326__00Mt*_00Ms_coeff).reshape((1, 40, 30))

# op _00RY_power_combination_eval
# LANG: temperature, _00RX --> density
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01486_density = (v01485__00RX**1)*(v01481_temperature**-1)
v01486_density = (v01486_density*_00RY_coeff).reshape((1,))

# op _00St expand_array_eval
# LANG: V_aircraft --> _00Su
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01505__00Su = np.einsum('ab,c->abc', v01496_V_aircraft.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _00Sz expand_array_eval
# LANG: time_vectors --> _00SA
# SHAPES: (2,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01511__00SA = np.einsum('c,ab->abc', v01510_time_vectors.reshape((2,)) ,np.ones((1, 3))).reshape((1, 3, 2))

# op _00W1_bessel_eval
# LANG: _00W0 --> _00W2
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01592__00W2=_00W1_bessel_eval(0,v01585__00W0)

# op _00W5_power_combination_eval
# LANG: _00W4 --> _00W6
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01595__00W6 = (v01594__00W4**2)
v01595__00W6 = (v01595__00W6*_00W5_coeff).reshape((1, 2, 3, 40, 10))

# op _00WH_bessel_eval
# LANG: _00W0 --> _00WI
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01614__00WI=_00WH_bessel_eval(0,v01585__00W0)

# op _00WL_power_combination_eval
# LANG: _00WK --> _00WM
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01617__00WM = (v01616__00WK**2)
v01617__00WM = (v01617__00WM*_00WL_coeff).reshape((1, 2, 3, 40, 10))

# op _00WR_power_combination_eval
# LANG: _00WQ --> _00WS
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01620__00WS = (v01619__00WQ**2)
v01620__00WS = (v01620__00WS*_00WR_coeff).reshape((1, 2, 3, 40, 10))

# op _00WT_bessel_eval
# LANG: _00W0 --> _00WU
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01622__00WU=_00WT_bessel_eval(1,v01585__00W0)

# op _00WZ_bessel_eval
# LANG: _00W0 --> _00W_
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01624__00W_=_00WZ_bessel_eval(1,v01585__00W0)

# op _00Wb_power_combination_eval
# LANG: _00Wa --> _00Wc
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01598__00Wc = (v01597__00Wa**2)
v01598__00Wc = (v01598__00Wc*_00Wb_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wd_bessel_eval
# LANG: _00W0 --> _00We
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01600__00We=_00Wd_bessel_eval(1,v01585__00W0)

# op _00Wj_bessel_eval
# LANG: _00W0 --> _00Wk
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01602__00Wk=_00Wj_bessel_eval(0,v01585__00W0)

# op _00Wl_bessel_eval
# LANG: _00W0 --> _00Wm
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01604__00Wm=_00Wl_bessel_eval(1,v01585__00W0)

# op _00YB_bessel_eval
# LANG: _00W0 --> _00YC
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01699__00YC=_00YB_bessel_eval(0,v01585__00W0)

# op _00YD_bessel_eval
# LANG: _00W0 --> _00YE
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01701__00YE=_00YD_bessel_eval(1,v01585__00W0)

# op _00Yd_linear_combination_eval
# LANG: _00Y2, _00Yc --> _00Ye
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01681__00Ye = _00Yd_constant+1*v01676__00Y2+1*v01685__00Yc

# op _00Yl_power_combination_eval
# LANG: _00Yi, _00Yk --> _00Ym
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01690__00Ym = (v01689__00Yi**1)*(v01691__00Yk**1)
v01690__00Ym = (v01690__00Ym*_00Yl_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yt_power_combination_eval
# LANG: _00Yq, _00Ys --> _00Yu
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01694__00Yu = (v01693__00Yq**1)*(v01695__00Ys**1)
v01694__00Yu = (v01694__00Yu*_00Yt_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yv_bessel_eval
# LANG: _00W0 --> _00Yw
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01697__00Yw=_00Yv_bessel_eval(1,v01585__00W0)

# op _00Zi_power_combination_eval
# LANG: _00Vc, _00Vx --> _00Zj
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01653__00Zj = (v01652__00Vx**1)*(v01581__00Vc**1)
v01653__00Zj = (v01653__00Zj*_00Zi_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zs_power_combination_eval
# LANG: _00Vc, _00Va --> _00Zt
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01647__00Zt = (v01581__00Vc**1)*(v01587__00Va**1)
v01647__00Zt = (v01647__00Zt*_00Zs_coeff).reshape((1, 2, 3, 40, 10))

# op _00by expand_scalar_eval
# LANG: density --> _00bz
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0245_density = v0245_density.reshape((1,))
v0323__00bz = np.empty((1, 40, 100))
v0323__00bz.fill(v0245_density.item())
v0245_density = v0245_density.reshape((1, 1))

# op _00cN_power_combination_eval
# LANG: _00cy, _00cM --> _00cO
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0303__00cO = (v0302__00cy**1)*(v0309__00cM**-1)
v0303__00cO = (v0303__00cO*_00cN_coeff).reshape((1, 40, 100))

# op _00cd_power_combination_eval
# LANG: _00c8, _00cc --> _00ce
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0279__00ce = (v0278__00c8**1)*(v0281__00cc**1)
v0279__00ce = (v0279__00ce*_00cd_coeff).reshape((1, 40, 100))

# op _00cr_linear_combination_eval
# LANG: _00co, _00cq --> _00cs
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0288__00cs = _00cr_constant+1*v0286__00co+1*v0289__00cq

# op _00da_power_combination_eval
# LANG: _radius --> _00db
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0321__00db = (v0217__radius**1)
v0321__00db = (v0321__00db*_00da_coeff).reshape((1, 40, 100))

# op _00eJ_power_combination_eval
# LANG: _ut --> _00eK
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0383__00eK = (v0314__ut**1)
v0383__00eK = (v0383__00eK*_00eJ_coeff).reshape((1, 40, 100))

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

# op _005Y_power_combination_eval
# LANG: propeller_radius --> _005Z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0195__005Z = (v0128_propeller_radius**1)
v0195__005Z = (v0195__005Z*_005Y_coeff).reshape((1,))

# op _00DF_linear_combination_eval
# LANG: _00DE, propeller_radius --> _00DG
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01136__00DG = _00DF_constant+1*v01068_propeller_radius+-1*v01137__00DE

# op _00JT_power_combination_eval
# LANG: _00JO, _00JS --> _00JU
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01221__00JU = (v01220__00JO**1)*(v01223__00JS**1)
v01221__00JU = (v01221__00JU*_00JT_coeff).reshape((1, 40, 30))

# op _00K6_linear_combination_eval
# LANG: _00K3, _00K5 --> _00K7
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01230__00K7 = _00K6_constant+1*v01228__00K3+1*v01231__00K5

# op _00KQ_power_combination_eval
# LANG: _radius --> _00KR
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01263__00KR = (v01159__radius**1)
v01263__00KR = (v01263__00KR*_00KQ_coeff).reshape((1, 40, 30))

# op _00Mk_power_combination_eval
# LANG: _00Je, _00Mj --> _00Ml
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01320__00Ml = (v01319__00Mj**1)*(v01265__00Je**1)
v01320__00Ml = (v01320__00Ml*_00Mk_coeff).reshape((1, 40, 30))

# op _00Mu_linear_combination_eval
# LANG: _00Mn, _00Mt --> _00Mv
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01323__00Mv = _00Mu_constant+1*v01322__00Mn+1*v01326__00Mt

# op _00PK_power_combination_eval
# LANG: rotor_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v01421_origin = (v012_rotor_disk_origin**1)
v01421_origin = (v01421_origin*_00PK_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _00PN_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _00PO
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v01440__00PO = (v010_rotor_disk_in_plane_2**1)
v01440__00PO = (v01440__00PO*_00PN_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _00SD_decompose_eval
# LANG: _00Su --> _00SE, _00SM, _00ST
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01506__00SE = ((v01505__00Su.flatten())[src_indices__00SE__00SD]).reshape((1, 1, 2))
v01507__00SM = ((v01505__00Su.flatten())[src_indices__00SM__00SD]).reshape((1, 1, 2))
v01508__00ST = ((v01505__00Su.flatten())[src_indices__00ST__00SD]).reshape((1, 1, 2))

# op _00SF_decompose_eval
# LANG: _00SA --> _00SG, _00SN, _00SU
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01512__00SG = ((v01511__00SA.flatten())[src_indices__00SG__00SF]).reshape((1, 1, 2))
v01513__00SN = ((v01511__00SA.flatten())[src_indices__00SN__00SF]).reshape((1, 1, 2))
v01514__00SU = ((v01511__00SA.flatten())[src_indices__00SU__00SF]).reshape((1, 1, 2))

# op _00Sw expand_array_eval
# LANG: aircraft_location --> _00Sx
# SHAPES: (3, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01500__00Sx = np.einsum('bc,a->abc', v01499_aircraft_location.reshape((3, 2)) ,np.ones((1,))).reshape((1, 3, 2))

# op _00V5 expand_scalar_eval
# LANG: density --> _00V6
# SHAPES: (1,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01644__00V6 = np.empty((1, 2, 3, 40, 11))
v01644__00V6.fill(v01486_density.item())

# op _00W7_power_combination_eval
# LANG: _00W2, _00W6 --> _00W8
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01593__00W8 = (v01592__00W2**1)*(v01595__00W6**1)
v01593__00W8 = (v01593__00W8*_00W7_coeff).reshape((1, 2, 3, 40, 10))

# op _00WN_power_combination_eval
# LANG: _00WI, _00WM --> _00WO
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01615__00WO = (v01614__00WI**1)*(v01617__00WM**1)
v01615__00WO = (v01615__00WO*_00WN_coeff).reshape((1, 2, 3, 40, 10))

# op _00WV_power_combination_eval
# LANG: _00WS, _00WU --> _00WW
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01621__00WW = (v01620__00WS**1)*(v01622__00WU**1)
v01621__00WW = (v01621__00WW*_00WV_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wf_power_combination_eval
# LANG: _00Wc, _00We --> _00Wg
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01599__00Wg = (v01598__00Wc**1)*(v01600__00We**1)
v01599__00Wg = (v01599__00Wg*_00Wf_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wn_power_combination_eval
# LANG: _00Wk, _00Wm --> _00Wo
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01603__00Wo = (v01602__00Wk**1)*(v01604__00Wm**1)
v01603__00Wo = (v01603__00Wo*_00Wn_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wp_bessel_eval
# LANG: _00W0 --> _00Wq
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01606__00Wq=_00Wp_bessel_eval(0,v01585__00W0)

# op _00Wv_bessel_eval
# LANG: _00W0 --> _00Ww
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01608__00Ww=_00Wv_bessel_eval(1,v01585__00W0)

# op _00Wx_bessel_eval
# LANG: _00W0 --> _00Wy
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01610__00Wy=_00Wx_bessel_eval(0,v01585__00W0)

# op _00X0_power_combination_eval
# LANG: _00W_ --> _00X1
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01625__00X1 = (v01624__00W_**2)
v01625__00X1 = (v01625__00X1*_00X0_coeff).reshape((1, 2, 3, 40, 10))

# op _00X2_bessel_eval
# LANG: _00W0 --> _00X3
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01627__00X3=_00X2_bessel_eval(1,v01585__00W0)

# op _00Xa_bessel_eval
# LANG: _00W0 --> _00Xb
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01631__00Xb=_00Xa_bessel_eval(1,v01585__00W0)

# op _00YF_power_combination_eval
# LANG: _00YC, _00YE --> _00YG
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01700__00YG = (v01699__00YC**1)*(v01701__00YE**1)
v01700__00YG = (v01700__00YG*_00YF_coeff).reshape((1, 2, 3, 40, 10))

# op _00YH_bessel_eval
# LANG: _00W0 --> _00YI
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01703__00YI=_00YH_bessel_eval(1,v01585__00W0)

# op _00YP_bessel_eval
# LANG: _00W0 --> _00YQ
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01707__00YQ=_00YP_bessel_eval(1,v01585__00W0)

# op _00Yn_linear_combination_eval
# LANG: _00Ye, _00Ym --> _00Yo
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01687__00Yo = _00Yn_constant+1*v01681__00Ye+1*v01690__00Ym

# op _00Yx_power_combination_eval
# LANG: _00Yu, _00Yw --> _00Yy
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01696__00Yy = (v01694__00Yu**1)*(v01697__00Yw**1)
v01696__00Yy = (v01696__00Yy*_00Yx_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zk_power_combination_eval
# LANG: _00Ve, _00Zj --> _00Zl
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01654__00Zl = (v01653__00Zj**1)*(v01590__00Ve**1)
v01654__00Zl = (v01654__00Zl*_00Zk_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zu_power_combination_eval
# LANG: _00Ve, _00Zt --> _00Zv
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01648__00Zv = (v01647__00Zt**1)*(v01590__00Ve**1)
v01648__00Zv = (v01648__00Zv*_00Zu_coeff).reshape((1, 2, 3, 40, 10))

# op _00cP_linear_combination_eval
# LANG: _00cO, _axial_inflow_velocity --> _ux_2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0295__ux_2 = _00cP_constant+1*v0224__axial_inflow_velocity+1*v0303__00cO

# op _00ct_power_combination_eval
# LANG: _00ce, _00cs --> _ux
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0282__ux = (v0279__00ce**1)*(v0288__00cs**-1)
v0282__ux = (v0282__ux*_00ct_coeff).reshape((1, 40, 100))

# op _00dc_power_combination_eval
# LANG: _00db, _00bz --> _00dd
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0322__00dd = (v0321__00db**1)*(v0323__00bz**1)
v0322__00dd = (v0322__00dd*_00dc_coeff).reshape((1, 40, 100))

# op _00eB_power_combination_eval
# LANG: Cd --> _00eC
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0376__00eC = (v0257_Cd**1)
v0376__00eC = (v0376__00eC*_00eB_coeff).reshape((1, 40, 100))

# op _00eL_linear_combination_eval
# LANG: _00eK, _tangential_inflow_velocity --> _00eM
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0382__00eM = _00eL_constant+1*v0234__tangential_inflow_velocity+-1*v0383__00eK

# op _00kY expand_array_eval
# LANG: V_aircraft --> _00kZ
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0565__00kZ = np.einsum('ab,c->abc', v0556_V_aircraft.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _00l3 expand_array_eval
# LANG: time_vectors --> _00l4
# SHAPES: (2,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0571__00l4 = np.einsum('c,ab->abc', v0570_time_vectors.reshape((2,)) ,np.ones((1, 3))).reshape((1, 3, 2))

# op _005__linear_combination_eval
# LANG: _005Z, propeller_radius --> _0060
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0194__0060 = _005__constant+1*v0128_propeller_radius+-1*v0195__005Z

# op _00DH_power_combination_eval
# LANG: _00DG --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01138_dr = (v01136__00DG**1)
v01138_dr = (v01138_dr*_00DH_coeff).reshape((1,))

# op _00K8_power_combination_eval
# LANG: _00JU, _00K7 --> _ux
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01224__ux = (v01221__00JU**1)*(v01230__00K7**-1)
v01224__ux = (v01224__ux*_00K8_coeff).reshape((1, 40, 30))

# op _00KS_power_combination_eval
# LANG: _00KR, _00Je --> _00KT
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01264__00KT = (v01263__00KR**1)*(v01265__00Je**1)
v01264__00KT = (v01264__00KT*_00KS_coeff).reshape((1, 40, 30))

# op _00Mw_power_combination_eval
# LANG: _00Ml, _00Mv --> _00Mx
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01321__00Mx = (v01320__00Ml**1)*(v01323__00Mv**1)
v01321__00Mx = (v01321__00Mx*_00Mw_coeff).reshape((1, 40, 30))

# op _00QD_power_combination_eval
# LANG: propeller_radius --> _00QE
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01445__00QE = (v01424_propeller_radius**1)
v01445__00QE = (v01445__00QE*_00QD_coeff).reshape((1,))

# op _00Qm cross_product_eval
# LANG: _00PI, _00PO --> _00Qn
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01441__00Qn = np.cross(v01440__00PO, v01422__00PI, axisa = 0, axisb = 0, axisc = 0)

# op _00SB_decompose_eval
# LANG: _00Sx --> _00SC, _00SL, _00SS
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01501__00SC = ((v01500__00Sx.flatten())[src_indices__00SC__00SB]).reshape((1, 1, 2))
v01502__00SL = ((v01500__00Sx.flatten())[src_indices__00SL__00SB]).reshape((1, 1, 2))
v01503__00SS = ((v01500__00Sx.flatten())[src_indices__00SS__00SB]).reshape((1, 1, 2))

# op _00SH_power_combination_eval
# LANG: _00SE, _00SG --> _00SI
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01509__00SI = (v01506__00SE**1)*(v01512__00SG**1)
v01509__00SI = (v01509__00SI*_00SH_coeff).reshape((1, 1, 2))

# op _00SO_power_combination_eval
# LANG: _00SM, _00SN --> _00SP
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01516__00SP = (v01507__00SM**1)*(v01513__00SN**1)
v01516__00SP = (v01516__00SP*_00SO_coeff).reshape((1, 1, 2))

# op _00T5 expand_array_eval
# LANG: origin --> _00T6
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01523__00T6 = np.einsum('b,ac->abc', v01421_origin.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00Vj_decompose_eval
# LANG: _00V6 --> _00Vk
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01645__00Vk = ((v01644__00V6.flatten())[src_indices__00Vk__00Vj]).reshape((1, 2, 3, 40, 10))

# op _00WB_bessel_eval
# LANG: _00W0 --> _00WC
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01612__00WC=_00WB_bessel_eval(1,v01585__00W0)

# op _00WX_linear_combination_eval
# LANG: _00WO, _00WW --> _00WY
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01618__00WY = _00WX_constant+1*v01615__00WO+1*v01621__00WW

# op _00Wh_linear_combination_eval
# LANG: _00W8, _00Wg --> _00Wi
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01596__00Wi = _00Wh_constant+1*v01593__00W8+-1*v01599__00Wg

# op _00Wr_power_combination_eval
# LANG: _00Wo, _00Wq --> _00Ws
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01605__00Ws = (v01603__00Wo**1)*(v01606__00Wq**1)
v01605__00Ws = (v01605__00Ws*_00Wr_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wz_power_combination_eval
# LANG: _00Ww, _00Wy --> _00WA
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01609__00WA = (v01608__00Ww**1)*(v01610__00Wy**1)
v01609__00WA = (v01609__00WA*_00Wz_coeff).reshape((1, 2, 3, 40, 10))

# op _00X4_power_combination_eval
# LANG: _00X1, _00X3 --> _00X5
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01626__00X5 = (v01625__00X1**1)*(v01627__00X3**1)
v01626__00X5 = (v01626__00X5*_00X4_coeff).reshape((1, 2, 3, 40, 10))

# op _00X8_bessel_eval
# LANG: _00W0 --> _00X9
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01629__00X9=_00X8_bessel_eval(0,v01585__00W0)

# op _00Xc_power_combination_eval
# LANG: _00Xb --> _00Xd
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01632__00Xd = (v01631__00Xb**2)
v01632__00Xd = (v01632__00Xd*_00Xc_coeff).reshape((1, 2, 3, 40, 10))

# op _00Xk_bessel_eval
# LANG: _00W0 --> _00Xl
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01634__00Xl=_00Xk_bessel_eval(1,v01585__00W0)

# op _00Xm_bessel_eval
# LANG: _00W0 --> _00Xn
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01636__00Xn=_00Xm_bessel_eval(0,v01585__00W0)

# op _00Xs_bessel_eval
# LANG: _00W0 --> _00Xt
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01639__00Xt=_00Xs_bessel_eval(0,v01585__00W0)

# op _00Xu_bessel_eval
# LANG: _00W0 --> _00Xv
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01641__00Xv=_00Xu_bessel_eval(1,v01585__00W0)

# op _00YJ_power_combination_eval
# LANG: _00YG, _00YI --> _00YK
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01702__00YK = (v01700__00YG**1)*(v01703__00YI**1)
v01702__00YK = (v01702__00YK*_00YJ_coeff).reshape((1, 2, 3, 40, 10))

# op _00YN_bessel_eval
# LANG: _00W0 --> _00YO
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01705__00YO=_00YN_bessel_eval(1,v01585__00W0)

# op _00YR_power_combination_eval
# LANG: _00YQ --> _00YS
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01708__00YS = (v01707__00YQ**2)
v01708__00YS = (v01708__00YS*_00YR_coeff).reshape((1, 2, 3, 40, 10))

# op _00YZ_bessel_eval
# LANG: _00W0 --> _00Y_
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01711__00Y_=_00YZ_bessel_eval(1,v01585__00W0)

# op _00Yz_linear_combination_eval
# LANG: _00Yo, _00Yy --> _00YA
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01692__00YA = _00Yz_constant+1*v01687__00Yo+-1*v01696__00Yy

# op _00Z0_bessel_eval
# LANG: _00W0 --> _00Z1
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01713__00Z1=_00Z0_bessel_eval(0,v01585__00W0)

# op _00Z6_bessel_eval
# LANG: _00W0 --> _00Z7
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01716__00Z7=_00Z6_bessel_eval(0,v01585__00W0)

# op _00Z8_bessel_eval
# LANG: _00W0 --> _00Z9
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01718__00Z9=_00Z8_bessel_eval(1,v01585__00W0)

# op _00Zm_power_combination_eval
# LANG: _00VP, _00Zl --> _00Zn
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01655__00Zn = (v01654__00Zl**1)*(v01575__00VP**-1)
v01655__00Zn = (v01655__00Zn*_00Zm_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zw_linear_combination_eval
# LANG: _00Zv --> _00Zx
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01649__00Zx = _00Zw_constant+1*v01648__00Zv

# op _00de_power_combination_eval
# LANG: _ux, _00dd --> _00df
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0324__00df = (v0322__00dd**1)*(v0282__ux**1)
v0324__00df = (v0324__00df*_00de_coeff).reshape((1, 40, 100))

# op _00dg_linear_combination_eval
# LANG: _ux, _axial_inflow_velocity --> _00dh
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0326__00dh = _00dg_constant+1*v0282__ux+-1*v0224__axial_inflow_velocity

# op _00eD_power_combination_eval
# LANG: _00eC --> _00eE
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0377__00eE = (v0376__00eC**1)
v0377__00eE = (v0377__00eE*_00eD_coeff).reshape((1, 40, 100))

# op _00eH_power_combination_eval
# LANG: _ux_2 --> _00eI
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0380__00eI = (v0295__ux_2**2)
v0380__00eI = (v0380__00eI*_00eH_coeff).reshape((1, 40, 100))

# op _00eN_power_combination_eval
# LANG: _00eM --> _00eO
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0384__00eO = (v0382__00eM**2)
v0384__00eO = (v0384__00eO*_00eN_coeff).reshape((1, 40, 100))

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
# SHAPES: (3, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0560__00l1 = np.einsum('bc,a->abc', v0559_aircraft_location.reshape((3, 2)) ,np.ones((1,))).reshape((1, 3, 2))

# op _00l7_decompose_eval
# LANG: _00kZ --> _00l8, _00lg, _00ln
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0566__00l8 = ((v0565__00kZ.flatten())[src_indices__00l8__00l7]).reshape((1, 1, 2))
v0567__00lg = ((v0565__00kZ.flatten())[src_indices__00lg__00l7]).reshape((1, 1, 2))
v0568__00ln = ((v0565__00kZ.flatten())[src_indices__00ln__00l7]).reshape((1, 1, 2))

# op _00l9_decompose_eval
# LANG: _00l4 --> _00la, _00lh, _00lo
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0572__00la = ((v0571__00l4.flatten())[src_indices__00la__00l9]).reshape((1, 1, 2))
v0573__00lh = ((v0571__00l4.flatten())[src_indices__00lh__00l9]).reshape((1, 1, 2))
v0574__00lo = ((v0571__00l4.flatten())[src_indices__00lo__00l9]).reshape((1, 1, 2))

# op _0061_power_combination_eval
# LANG: _0060 --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0196_dr = (v0194__0060**1)
v0196_dr = (v0196_dr*_0061_coeff).reshape((1,))

# op _00EP expand_scalar_eval
# LANG: dr --> _dr
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01147__dr = np.empty((1, 40, 30))
v01147__dr.fill(v01138_dr.item())

# op _00KU_power_combination_eval
# LANG: _ux, _00KT --> _00KV
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01266__00KV = (v01264__00KT**1)*(v01224__ux**1)
v01266__00KV = (v01266__00KV*_00KU_coeff).reshape((1, 40, 30))

# op _00KW_linear_combination_eval
# LANG: _ux, _axial_inflow_velocity --> _00KX
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01268__00KX = _00KW_constant+1*v01224__ux+-1*v01166__axial_inflow_velocity

# op _00My_power_combination_eval
# LANG: _00Mx, _chord --> _00Mz
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01327__00Mz = (v01321__00Mx**1)*(v01154__chord**1)
v01327__00Mz = (v01327__00Mz*_00My_coeff).reshape((1, 40, 30))

# op _00Q1_linear_combination_eval
# LANG: theta --> _00Q2
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0986_theta = v0986_theta.reshape((1, 1))
v01428__00Q2 = _00Q1_constant+1*v0986_theta
v0986_theta = v0986_theta.reshape((1,))

# op _00Q3_linear_combination_eval
# LANG: theta --> _00Q4
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0986_theta = v0986_theta.reshape((1, 1))
v01430__00Q4 = _00Q3_constant+1*v0986_theta
v0986_theta = v0986_theta.reshape((1,))

# op _00QF_power_combination_eval
# LANG: _00QE --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01446_dr = (v01445__00QE**1)
v01446_dr = (v01446_dr*_00QF_coeff).reshape((1,))

# op _00Qa_sin_eval
# LANG: theta --> _00Qb
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0986_theta = v0986_theta.reshape((1, 1))
v01433__00Qb = np.sin(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _00Qe_sin_eval
# LANG: theta --> _00Qf
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0986_theta = v0986_theta.reshape((1, 1))
v01435__00Qf = np.sin(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _00Qi_cos_eval
# LANG: theta --> _00Qj
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0986_theta = v0986_theta.reshape((1, 1))
v01437__00Qj = np.cos(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _00Qo pnorm_eval
# LANG: _00Qn --> _00Qp
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01443__00Qp = np.linalg.norm(v01441__00Qn.flatten(), ord=2)

# op _00SJ_linear_combination_eval
# LANG: _00SC, _00SI --> aircraft_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01504_aircraft_x_pos = _00SJ_constant+1*v01501__00SC+1*v01509__00SI

# op _00SQ_linear_combination_eval
# LANG: _00SL, _00SP --> aircraft_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01515_aircraft_y_pos = _00SQ_constant+1*v01502__00SL+1*v01516__00SP

# op _00SV_power_combination_eval
# LANG: _00ST, _00SU --> _00SW
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01518__00SW = (v01508__00ST**1)*(v01514__00SU**1)
v01518__00SW = (v01518__00SW*_00SV_coeff).reshape((1, 1, 2))

# op _00T7_decompose_eval
# LANG: _00T6 --> _00T8, _00Td, _00Ti
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01524__00T8 = ((v01523__00T6.flatten())[src_indices__00T8__00T7]).reshape((1, 1, 2))
v01525__00Td = ((v01523__00T6.flatten())[src_indices__00Td__00T7]).reshape((1, 1, 2))
v01526__00Ti = ((v01523__00T6.flatten())[src_indices__00Ti__00T7]).reshape((1, 1, 2))

# op _00WD_power_combination_eval
# LANG: _00WA, _00WC --> _00WE
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01611__00WE = (v01609__00WA**1)*(v01612__00WC**1)
v01611__00WE = (v01611__00WE*_00WD_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wt_linear_combination_eval
# LANG: _00Wi, _00Ws --> _00Wu
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01601__00Wu = _00Wt_constant+1*v01596__00Wi+1*v01605__00Ws

# op _00X6_linear_combination_eval
# LANG: _00WY, _00X5 --> _00X7
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01623__00X7 = _00X6_constant+1*v01618__00WY+-1*v01626__00X5

# op _00Xe_power_combination_eval
# LANG: _00X9, _00Xd --> _00Xf
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01630__00Xf = (v01629__00X9**1)*(v01632__00Xd**1)
v01630__00Xf = (v01630__00Xf*_00Xe_coeff).reshape((1, 2, 3, 40, 10))

# op _00Xo_linear_combination_eval
# LANG: _00Xl, _00Xn --> _00Xp
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01635__00Xp = _00Xo_constant+1*v01634__00Xl+1*v01636__00Xn

# op _00Xw_linear_combination_eval
# LANG: _00Xt, _00Xv --> _00Xx
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01640__00Xx = _00Xw_constant+1*v01639__00Xt+-1*v01641__00Xv

# op _00YL_linear_combination_eval
# LANG: _00YA, _00YK --> _00YM
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01698__00YM = _00YL_constant+1*v01692__00YA+-1*v01702__00YK

# op _00YT_power_combination_eval
# LANG: _00YO, _00YS --> _00YU
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01706__00YU = (v01705__00YO**1)*(v01708__00YS**1)
v01706__00YU = (v01706__00YU*_00YT_coeff).reshape((1, 2, 3, 40, 10))

# op _00Z2_linear_combination_eval
# LANG: _00Y_, _00Z1 --> _00Z3
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01712__00Z3 = _00Z2_constant+1*v01711__00Y_+1*v01713__00Z1

# op _00Za_linear_combination_eval
# LANG: _00Z7, _00Z9 --> _00Zb
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01717__00Zb = _00Za_constant+1*v01716__00Z7+-1*v01718__00Z9

# op _00Zo_power_combination_eval
# LANG: _00Zn --> _00Zp
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01656__00Zp = (v01655__00Zn**1)
v01656__00Zp = (v01656__00Zp*_00Zo_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zy_power_combination_eval
# LANG: _00Vk, _00Zx --> _00Zz
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01646__00Zz = (v01645__00Vk**1)*(v01649__00Zx**1)
v01646__00Zz = (v01646__00Zz*_00Zy_coeff).reshape((1, 2, 3, 40, 10))

# op _00di_power_combination_eval
# LANG: _00df, _00dh --> _00dj
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0325__00dj = (v0324__00df**1)*(v0326__00dh**1)
v0325__00dj = (v0325__00dj*_00di_coeff).reshape((1, 40, 100))

# op _00eF_power_combination_eval
# LANG: _00bz, _00eE --> _00eG
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0378__00eG = (v0377__00eE**1)*(v0323__00bz**1)
v0378__00eG = (v0378__00eG*_00eF_coeff).reshape((1, 40, 100))

# op _00eP_linear_combination_eval
# LANG: _00eI, _00eO --> _00eQ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0381__00eQ = _00eP_constant+1*v0380__00eI+1*v0384__00eO

# op _00l5_decompose_eval
# LANG: _00l1 --> _00l6, _00lf, _00lm
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0561__00l6 = ((v0560__00l1.flatten())[src_indices__00l6__00l5]).reshape((1, 1, 2))
v0562__00lf = ((v0560__00l1.flatten())[src_indices__00lf__00l5]).reshape((1, 1, 2))
v0563__00lm = ((v0560__00l1.flatten())[src_indices__00lm__00l5]).reshape((1, 1, 2))

# op _00lA expand_array_eval
# LANG: origin --> _00lB
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0583__00lB = np.einsum('b,ac->abc', v0479_origin.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00lb_power_combination_eval
# LANG: _00l8, _00la --> _00lc
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0569__00lc = (v0566__00l8**1)*(v0572__00la**1)
v0569__00lc = (v0569__00lc*_00lb_coeff).reshape((1, 1, 2))

# op _00li_power_combination_eval
# LANG: _00lg, _00lh --> _00lj
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0576__00lj = (v0567__00lg**1)*(v0573__00lh**1)
v0576__00lj = (v0576__00lj*_00li_coeff).reshape((1, 1, 2))

# op _0079 expand_scalar_eval
# LANG: dr --> _dr
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0205__dr = np.empty((1, 40, 100))
v0205__dr.fill(v0196_dr.item())

# op _00KY_power_combination_eval
# LANG: _00KV, _00KX --> _00KZ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01267__00KZ = (v01266__00KV**1)*(v01268__00KX**1)
v01267__00KZ = (v01267__00KZ*_00KY_coeff).reshape((1, 40, 30))

# op _00MA_power_combination_eval
# LANG: _00Mz, _dr --> _dD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01328__dD = (v01327__00Mz**1)*(v01147__dr**1)
v01328__dD = (v01328__dD*_00MA_coeff).reshape((1, 40, 30))

# op _00Q5_power_combination_eval
# LANG: _00Q2, _00Q4 --> _00Q6
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01429__00Q6 = (v01428__00Q2**1)*(v01430__00Q4**-1)
v01429__00Q6 = (v01429__00Q6*_00Q5_coeff).reshape((1, 1))

# op _00Q8_cos_eval
# LANG: theta --> _00Q9
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0986_theta = v0986_theta.reshape((1, 1))
v01432__00Q9 = np.cos(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _00Qc_power_combination_eval
# LANG: _00Qb --> _00Qd
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01434__00Qd = (v01433__00Qb**1)
v01434__00Qd = (v01434__00Qd*_00Qc_coeff).reshape((1, 1))

# op _00Qg_power_combination_eval
# LANG: _00Qf --> _00Qh
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01436__00Qh = (v01435__00Qf**1)
v01436__00Qh = (v01436__00Qh*_00Qg_coeff).reshape((1, 1))

# op _00Qk_power_combination_eval
# LANG: _00Qj --> _00Ql
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01438__00Ql = (v01437__00Qj**1)
v01438__00Ql = (v01438__00Ql*_00Qk_coeff).reshape((1, 1))

# op _00Qq expand_scalar_eval
# LANG: _00Qp --> _00Qr
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01444__00Qr = np.empty((3,))
v01444__00Qr.fill(v01443__00Qp.item())

# op _00SX_linear_combination_eval
# LANG: _00SS, _00SW --> aircraft_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01517_aircraft_z_pos = _00SX_constant+1*v01503__00SS+1*v01518__00SW

# op _00SZ expand_array_eval
# LANG: init_obs_x_loc --> _00S_
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01520__00S_ = np.einsum('c,ab->abc', v01519_init_obs_x_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00T0 expand_array_eval
# LANG: init_obs_y_loc --> _00T1
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01528__00T1 = np.einsum('c,ab->abc', v01527_init_obs_y_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00T9_linear_combination_eval
# LANG: aircraft_x_pos, _00T8 --> _00Ta
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01522__00Ta = _00T9_constant+1*v01504_aircraft_x_pos+1*v01524__00T8

# op _00Te_linear_combination_eval
# LANG: aircraft_y_pos, _00Td --> _00Tf
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01530__00Tf = _00Te_constant+1*v01515_aircraft_y_pos+1*v01525__00Td

# op _00UI expand_scalar_eval
# LANG: dr --> _00UJ
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01563__00UJ = np.empty((1, 40, 30))
v01563__00UJ.fill(v01446_dr.item())

# op _00WF_linear_combination_eval
# LANG: _00Wu, _00WE --> _00WG
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01607__00WG = _00WF_constant+1*v01601__00Wu+-1*v01611__00WE

# op _00Xg_linear_combination_eval
# LANG: _00X7, _00Xf --> _00Xh
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01628__00Xh = _00Xg_constant+1*v01623__00X7+-1*v01630__00Xf

# op _00Xq_power_combination_eval
# LANG: _00Xp --> _00Xr
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01637__00Xr = (v01635__00Xp**2)
v01637__00Xr = (v01637__00Xr*_00Xq_coeff).reshape((1, 2, 3, 40, 10))

# op _00Xy_power_combination_eval
# LANG: _00Xx --> _00Xz
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01642__00Xz = (v01640__00Xx**2)
v01642__00Xz = (v01642__00Xz*_00Xy_coeff).reshape((1, 2, 3, 40, 10))

# op _00YV_linear_combination_eval
# LANG: _00YM, _00YU --> _00YW
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01704__00YW = _00YV_constant+1*v01698__00YM+1*v01706__00YU

# op _00Z4_power_combination_eval
# LANG: _00Z3 --> _00Z5
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01714__00Z5 = (v01712__00Z3**2)
v01714__00Z5 = (v01714__00Z5*_00Z4_coeff).reshape((1, 2, 3, 40, 10))

# op _00ZA_power_combination_eval
# LANG: _00Vi, _00Zz --> _00ZB
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01650__00ZB = (v01646__00Zz**1)*(v01584__00Vi**1)
v01650__00ZB = (v01650__00ZB*_00ZA_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zc_power_combination_eval
# LANG: _00Zb --> _00Zd
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01719__00Zd = (v01717__00Zb**2)
v01719__00Zd = (v01719__00Zd*_00Zc_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zq_power_combination_eval
# LANG: _00Zp --> _00Zr
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01657__00Zr = (v01656__00Zp**1)
v01657__00Zr = (v01657__00Zr*_00Zq_coeff).reshape((1, 2, 3, 40, 10))

# op _00dk_power_combination_eval
# LANG: _00dj, prandtl_loss_factor --> _00dl
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0327__00dl = (v0325__00dj**1)*(v0267_prandtl_loss_factor**1)
v0327__00dl = (v0327__00dl*_00dk_coeff).reshape((1, 40, 100))

# op _00eR_power_combination_eval
# LANG: _00eG, _00eQ --> _00eS
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0379__00eS = (v0378__00eG**1)*(v0381__00eQ**1)
v0379__00eS = (v0379__00eS*_00eR_coeff).reshape((1, 40, 100))

# op _00lC_decompose_eval
# LANG: _00lB --> _00lD, _00lI, _00lN
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0584__00lD = ((v0583__00lB.flatten())[src_indices__00lD__00lC]).reshape((1, 1, 2))
v0585__00lI = ((v0583__00lB.flatten())[src_indices__00lI__00lC]).reshape((1, 1, 2))
v0586__00lN = ((v0583__00lB.flatten())[src_indices__00lN__00lC]).reshape((1, 1, 2))

# op _00ld_linear_combination_eval
# LANG: _00l6, _00lc --> aircraft_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0564_aircraft_x_pos = _00ld_constant+1*v0561__00l6+1*v0569__00lc

# op _00lk_linear_combination_eval
# LANG: _00lf, _00lj --> aircraft_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0575_aircraft_y_pos = _00lk_constant+1*v0562__00lf+1*v0576__00lj

# op _00lp_power_combination_eval
# LANG: _00ln, _00lo --> _00lq
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0578__00lq = (v0568__00ln**1)*(v0574__00lo**1)
v0578__00lq = (v0578__00lq*_00lp_coeff).reshape((1, 1, 2))

# op _00K__power_combination_eval
# LANG: _00KZ, prandtl_loss_factor --> _00L0
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01269__00L0 = (v01267__00KZ**1)*(v01209_prandtl_loss_factor**1)
v01269__00L0 = (v01269__00L0*_00K__coeff).reshape((1, 40, 30))

# op _00Q7_indexed_passthrough_eval
# LANG: _00Q6, _00Q9, _00Qd, _00Qh, _00Ql --> rot_mat
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01431_rot_mat__temp[i_v01429__00Q6__00Q7_indexed_passthrough_eval] = v01429__00Q6.flatten()
v01431_rot_mat = v01431_rot_mat__temp.copy()
v01431_rot_mat__temp[i_v01432__00Q9__00Q7_indexed_passthrough_eval] = v01432__00Q9.flatten()
v01431_rot_mat = v01431_rot_mat__temp.copy()
v01431_rot_mat__temp[i_v01434__00Qd__00Q7_indexed_passthrough_eval] = v01434__00Qd.flatten()
v01431_rot_mat = v01431_rot_mat__temp.copy()
v01431_rot_mat__temp[i_v01436__00Qh__00Q7_indexed_passthrough_eval] = v01436__00Qh.flatten()
v01431_rot_mat = v01431_rot_mat__temp.copy()
v01431_rot_mat__temp[i_v01438__00Ql__00Q7_indexed_passthrough_eval] = v01438__00Ql.flatten()
v01431_rot_mat = v01431_rot_mat__temp.copy()

# op _00Qs_power_combination_eval
# LANG: _00Qn, _00Qr --> _00Qt
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01442__00Qt = (v01441__00Qn**1)*(v01444__00Qr**-1)
v01442__00Qt = (v01442__00Qt*_00Qs_coeff).reshape((3,))

# op _00T2 expand_array_eval
# LANG: init_obs_z_loc --> _00T3
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01532__00T3 = np.einsum('c,ab->abc', v01531_init_obs_z_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00Tb_linear_combination_eval
# LANG: _00S_, _00Ta --> rel_obs_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01521_rel_obs_x_pos = _00Tb_constant+1*v01520__00S_+-1*v01522__00Ta

# op _00Tg_linear_combination_eval
# LANG: _00T1, _00Tf --> rel_obs_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01529_rel_obs_y_pos = _00Tg_constant+1*v01528__00T1+-1*v01530__00Tf

# op _00Tj_linear_combination_eval
# LANG: aircraft_z_pos, _00Ti --> _00Tk
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01534__00Tk = _00Tj_constant+1*v01517_aircraft_z_pos+1*v01526__00Ti

# op _00UK_power_combination_eval
# LANG: _00UJ, _dD --> bbb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01562_bbb = (v01328__dD**1)*(v01563__00UJ**-1)
v01562_bbb = (v01562_bbb*_00UK_coeff).reshape((1, 40, 30))

# op _00XA_linear_combination_eval
# LANG: _00Xr, _00Xz --> _00XB
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01638__00XB = _00XA_constant+1*v01637__00Xr+1*v01642__00Xz

# op _00Xi_linear_combination_eval
# LANG: _00WG, _00Xh --> _00Xj
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01613__00Xj = _00Xi_constant+1*v01607__00WG+-1*v01628__00Xh

# op _00YX_linear_combination_eval
# LANG: _00YW --> _00YY
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01709__00YY = _00YX_constant+-1*v01704__00YW

# op _00ZC_power_combination_eval
# LANG: _00ZB, _00Zr --> _00ZD
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01651__00ZD = (v01650__00ZB**1)*(v01657__00Zr**1)
v01651__00ZD = (v01651__00ZD*_00ZC_coeff).reshape((1, 2, 3, 40, 10))

# op _00Ze_linear_combination_eval
# LANG: _00Z5, _00Zd --> _00Zf
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01715__00Zf = _00Ze_constant+1*v01714__00Z5+1*v01719__00Zd

# op _00dm_power_combination_eval
# LANG: _00dl, _dr --> _local_thrust
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0328__local_thrust = (v0327__00dl**1)*(v0205__dr**1)
v0328__local_thrust = (v0328__local_thrust*_00dm_coeff).reshape((1, 40, 100))

# op _00eT_power_combination_eval
# LANG: _00eS, _chord --> _00eU
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0385__00eU = (v0379__00eS**1)*(v0212__chord**1)
v0385__00eU = (v0385__00eU*_00eT_coeff).reshape((1, 40, 100))

# op _00lE_linear_combination_eval
# LANG: aircraft_x_pos, _00lD --> _00lF
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0582__00lF = _00lE_constant+1*v0564_aircraft_x_pos+1*v0584__00lD

# op _00lJ_linear_combination_eval
# LANG: aircraft_y_pos, _00lI --> _00lK
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0590__00lK = _00lJ_constant+1*v0575_aircraft_y_pos+1*v0585__00lI

# op _00lr_linear_combination_eval
# LANG: _00lm, _00lq --> aircraft_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0577_aircraft_z_pos = _00lr_constant+1*v0563__00lm+1*v0578__00lq

# op _00lt expand_array_eval
# LANG: init_obs_x_loc --> _00lu
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0580__00lu = np.einsum('c,ab->abc', v0579_init_obs_x_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00lv expand_array_eval
# LANG: init_obs_y_loc --> _00lw
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0588__00lw = np.einsum('c,ab->abc', v0587_init_obs_y_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00L1_power_combination_eval
# LANG: _00L0, _dr --> _local_thrust
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01270__local_thrust = (v01269__00L0**1)*(v01147__dr**1)
v01270__local_thrust = (v01270__local_thrust*_00L1_coeff).reshape((1, 40, 30))

# op _00Qu_matvec_eval
# LANG: rot_mat, _00Qt --> thrust_dir
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01439_thrust_dir = v01431_rot_mat@v01442__00Qt

# op _00Tl_linear_combination_eval
# LANG: _00T3, _00Tk --> rel_obs_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01533_rel_obs_z_pos = _00Tl_constant+1*v01532__00T3+-1*v01534__00Tk

# op _00Tp_power_combination_eval
# LANG: rel_obs_x_pos --> _00Tq
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01536__00Tq = (v01521_rel_obs_x_pos**2)
v01536__00Tq = (v01536__00Tq*_00Tp_coeff).reshape((1, 1, 2))

# op _00Tr_power_combination_eval
# LANG: rel_obs_y_pos --> _00Ts
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01538__00Ts = (v01529_rel_obs_y_pos**2)
v01538__00Ts = (v01538__00Ts*_00Tr_coeff).reshape((1, 1, 2))

# op _00UQ_decompose_eval
# LANG: bbb --> _00UR
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01662__00UR = ((v01562_bbb.flatten())[src_indices__00UR__00UQ]).reshape((1, 40, 1))

# op _00Vu_decompose_eval
# LANG: _00Vr --> _00Vv
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01660__00Vv = ((v01566__00Vr.flatten())[src_indices__00Vv__00Vu]).reshape((1, 2, 3, 40, 10))

# op _00XC_power_combination_eval
# LANG: _00Xj, _00XB --> _00XD
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01633__00XD = (v01613__00Xj**1)*(v01638__00XB**-1)
v01633__00XD = (v01633__00XD*_00XC_coeff).reshape((1, 2, 3, 40, 10))

# op _00ZE_power_combination_eval
# LANG: _00ZD --> _00ZF
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01658__00ZF = (v01651__00ZD**1)
v01658__00ZF = (v01658__00ZF*_00ZE_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zg_power_combination_eval
# LANG: _00YY, _00Zf --> _00Zh
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01710__00Zh = (v01709__00YY**1)*(v01715__00Zf**-1)
v01710__00Zh = (v01710__00Zh*_00Zg_coeff).reshape((1, 2, 3, 40, 10))

# op _00eV_power_combination_eval
# LANG: _00eU, _dr --> _dD
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0386__dD = (v0385__00eU**1)*(v0205__dr**1)
v0386__dD = (v0386__dD*_00eV_coeff).reshape((1, 40, 100))

# op _00hU_power_combination_eval
# LANG: _local_thrust --> _dT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0329__dT = (v0328__local_thrust**1)
v0329__dT = (v0329__dT*_00hU_coeff).reshape((1, 40, 100))

# op _00kc_power_combination_eval
# LANG: altitude --> _00kd
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0538__00kd = (v052_cruise_altitude**1)
v0538__00kd = (v0538__00kd*_00kc_coeff).reshape((1,))

# op _00lG_linear_combination_eval
# LANG: _00lu, _00lF --> rel_obs_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0581_rel_obs_x_pos = _00lG_constant+1*v0580__00lu+-1*v0582__00lF

# op _00lL_linear_combination_eval
# LANG: _00lw, _00lK --> rel_obs_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0589_rel_obs_y_pos = _00lL_constant+1*v0588__00lw+-1*v0590__00lK

# op _00lO_linear_combination_eval
# LANG: aircraft_z_pos, _00lN --> _00lP
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0594__00lP = _00lO_constant+1*v0577_aircraft_z_pos+1*v0586__00lN

# op _00lx expand_array_eval
# LANG: init_obs_z_loc --> _00ly
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0592__00ly = np.einsum('c,ab->abc', v0591_init_obs_z_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00Pz_power_combination_eval
# LANG: _local_thrust --> _dT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01271__dT = (v01270__local_thrust**1)
v01271__dT = (v01271__dT*_00Pz_coeff).reshape((1, 40, 30))

# op _00TC expand_array_eval
# LANG: thrust_dir --> _00TD
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01543__00TD = np.einsum('b,ac->abc', v01439_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00To_indexed_passthrough_eval
# LANG: rel_obs_x_pos, rel_obs_y_pos, rel_obs_z_pos --> rel_obs_position
# SHAPES: (1, 1, 2), (1, 1, 2), (1, 1, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01535_rel_obs_position__temp[i_v01521_rel_obs_x_pos__00To_indexed_passthrough_eval] = v01521_rel_obs_x_pos.flatten()
v01535_rel_obs_position = v01535_rel_obs_position__temp.copy()
v01535_rel_obs_position__temp[i_v01529_rel_obs_y_pos__00To_indexed_passthrough_eval] = v01529_rel_obs_y_pos.flatten()
v01535_rel_obs_position = v01535_rel_obs_position__temp.copy()
v01535_rel_obs_position__temp[i_v01533_rel_obs_z_pos__00To_indexed_passthrough_eval] = v01533_rel_obs_z_pos.flatten()
v01535_rel_obs_position = v01535_rel_obs_position__temp.copy()

# op _00Tt_linear_combination_eval
# LANG: _00Tq, _00Ts --> _00Tu
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01537__00Tu = _00Tt_constant+1*v01536__00Tq+1*v01538__00Ts

# op _00Tv_power_combination_eval
# LANG: rel_obs_z_pos --> _00Tw
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01540__00Tw = (v01533_rel_obs_z_pos**2)
v01540__00Tw = (v01540__00Tw*_00Tv_coeff).reshape((1, 1, 2))

# op _00UE expand_scalar_eval
# LANG: dr --> _00UF
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01561__00UF = np.empty((1, 40, 30))
v01561__00UF.fill(v01446_dr.item())

# op _00US reshape_eval
# LANG: _00UR --> _00UT
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01663__00UT = v01662__00UR.reshape((1, 40))

# op _00ZG_power_combination_eval
# LANG: _00XD, _00ZF --> _00ZH
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01643__00ZH = (v01633__00XD**1)*(v01658__00ZF**1)
v01643__00ZH = (v01643__00ZH*_00ZG_coeff).reshape((1, 2, 3, 40, 10))

# op _00ZI_power_combination_eval
# LANG: _00ZF, _00Zh --> _00ZJ
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01720__00ZJ = (v01710__00Zh**1)*(v01658__00ZF**1)
v01720__00ZJ = (v01720__00ZJ*_00ZI_coeff).reshape((1, 2, 3, 40, 10))

# op _00ZO_sin_eval
# LANG: _00Vv --> _00ZP
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01667__00ZP = np.sin(v01660__00Vv)

# op _00ZX_sin_eval
# LANG: _00Vv --> _00ZY
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01725__00ZY = np.sin(v01660__00Vv)

# op _00ke_linear_combination_eval
# LANG: _00kd --> _00kf
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0539__00kf = _00ke_constant+-1*v0538__00kd

# op _00lQ_linear_combination_eval
# LANG: _00ly, _00lP --> rel_obs_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0593_rel_obs_z_pos = _00lQ_constant+1*v0592__00ly+-1*v0594__00lP

# op _00lU_power_combination_eval
# LANG: rel_obs_x_pos --> _00lV
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0596__00lV = (v0581_rel_obs_x_pos**2)
v0596__00lV = (v0596__00lV*_00lU_coeff).reshape((1, 1, 2))

# op _00lW_power_combination_eval
# LANG: rel_obs_y_pos --> _00lX
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0598__00lX = (v0589_rel_obs_y_pos**2)
v0598__00lX = (v0598__00lX*_00lW_coeff).reshape((1, 1, 2))

# op _00mL expand_array_eval
# LANG: _dD --> _00mM
# SHAPES: (1, 40, 100) --> (1, 2, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0620__00mM = np.einsum('acd,b->abcd', v0386__dD.reshape((1, 40, 100)) ,np.ones((2,))).reshape((1, 2, 40, 100))

# op _00mO expand_array_eval
# LANG: _dT --> _00mP
# SHAPES: (1, 40, 100) --> (1, 2, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0622__00mP = np.einsum('acd,b->abcd', v0329__dT.reshape((1, 40, 100)) ,np.ones((2,))).reshape((1, 2, 40, 100))

# op _00TE_tensor_dot_product_eval
# LANG: rel_obs_position, _00TD --> normal_proj
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01542_normal_proj = np.sum(v01535_rel_obs_position * v01543__00TD, axis=1)

# op _00Tx_linear_combination_eval
# LANG: _00Tu, _00Tw --> _00Ty
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01539__00Ty = _00Tx_constant+1*v01537__00Tu+1*v01540__00Tw

# op _00UG_power_combination_eval
# LANG: _00UF, _dT --> aaa
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01560_aaa = (v01271__dT**1)*(v01561__00UF**-1)
v01560_aaa = (v01560_aaa*_00UG_coeff).reshape((1, 40, 30))

# op _00VL expand_array_eval
# LANG: _00UT --> _00VM
# SHAPES: (1, 40) --> (1, 2, 3, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01664__00VM = np.einsum('ad,bce->abcde', v01663__00UT.reshape((1, 40)) ,np.ones((2, 3, 1))).reshape((1, 2, 3, 40, 1))

# op _00ZQ_power_combination_eval
# LANG: _00ZH, _00ZP --> _00ZR
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01666__00ZR = (v01643__00ZH**1)*(v01667__00ZP**1)
v01666__00ZR = (v01666__00ZR*_00ZQ_coeff).reshape((1, 2, 3, 40, 10))

# op _00ZZ_power_combination_eval
# LANG: _00ZJ, _00ZY --> _00Z_
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01724__00Z_ = (v01720__00ZJ**1)*(v01725__00ZY**1)
v01724__00Z_ = (v01724__00Z_*_00ZZ_coeff).reshape((1, 2, 3, 40, 10))

# op _00kg_power_combination_eval
# LANG: _00kf --> _00kh
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0540__00kh = (v0539__00kf**1)
v0540__00kh = (v0540__00kh*_00kg_coeff).reshape((1,))

# op _00lY_linear_combination_eval
# LANG: _00lV, _00lX --> _00lZ
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0597__00lZ = _00lY_constant+1*v0596__00lV+1*v0598__00lX

# op _00l__power_combination_eval
# LANG: rel_obs_z_pos --> _00m0
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0600__00m0 = (v0593_rel_obs_z_pos**2)
v0600__00m0 = (v0600__00m0*_00l__coeff).reshape((1, 1, 2))

# op _00mQ_single_tensor_sum_with_axis_eval
# LANG: _00mM --> aaa
# SHAPES: (1, 2, 40, 100) --> (1, 2, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0621_aaa = np.sum(v0620__00mM, axis = (2,)).reshape((1, 2, 100))

# op _00mS_single_tensor_sum_with_axis_eval
# LANG: _00mP --> bbb
# SHAPES: (1, 2, 40, 100) --> (1, 2, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0623_bbb = np.sum(v0622__00mP, axis = (2,)).reshape((1, 2, 100))

# op _00mZ_sin_eval
# LANG: n_theta_prod --> _00m_
# SHAPES: (11, 100) --> (11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0633__00m_ = np.sin(v0626_n_theta_prod)

# op _00oU expand_scalar_eval
# LANG: Vx --> _00oV
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0672__00oV = np.empty((1, 2))
v0672__00oV.fill(v030_u.item())

# op _00oX expand_scalar_eval
# LANG: Vy --> _00oY
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0675__00oY = np.empty((1, 2))
v0675__00oY.fill(v035_v.item())

# op _00o_ expand_scalar_eval
# LANG: Vz --> _00p0
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0677__00p0 = np.empty((1, 2))
v0677__00p0.fill(v039_w.item())

# op _00TQ expand_array_eval
# LANG: normal_proj --> _00TR
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01548__00TR = np.einsum('ac,b->abc', v01542_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00Tz_power_combination_eval
# LANG: _00Ty --> rel_obs_dist
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01541_rel_obs_dist = (v01539__00Ty**0.5)
v01541_rel_obs_dist = (v01541_rel_obs_dist*_00Tz_coeff).reshape((1, 1, 2))

# op _00UM_decompose_eval
# LANG: aaa --> _00UN
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01570__00UN = ((v01560_aaa.flatten())[src_indices__00UN__00UM]).reshape((1, 40, 1))

# op _00VN_indexed_passthrough_eval
# LANG: _00VM, _00ZR --> dDdR_real_exp
# SHAPES: (1, 2, 3, 40, 1), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01665_dDdR_real_exp__temp[i_v01664__00VM__00VN_indexed_passthrough_eval] = v01664__00VM.flatten()
v01665_dDdR_real_exp = v01665_dDdR_real_exp__temp.copy()
v01665_dDdR_real_exp__temp[i_v01666__00ZR__00VN_indexed_passthrough_eval] = v01666__00ZR.flatten()
v01665_dDdR_real_exp = v01665_dDdR_real_exp__temp.copy()

# op _00_0_indexed_passthrough_eval
# LANG: _00Z_ --> dDdR_imag_exp
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01726_dDdR_imag_exp__temp[i_v01724__00Z___00_0_indexed_passthrough_eval] = v01724__00Z_.flatten()
v01726_dDdR_imag_exp = v01726_dDdR_imag_exp__temp.copy()

# op _00ki_linear_combination_eval
# LANG: _00kh --> temperature
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.atmosphere_model
v0541_temperature = _00ki_constant+1*v0540__00kh

# op _00m1_linear_combination_eval
# LANG: _00lZ, _00m0 --> _00m2
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0599__00m2 = _00m1_constant+1*v0597__00lZ+1*v0600__00m0

# op _00mV_cos_eval
# LANG: n_theta_prod --> _00mW
# SHAPES: (11, 100) --> (11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0627__00mW = np.cos(v0626_n_theta_prod)

# op _00n0 expand_array_eval
# LANG: _00m_ --> _00n1
# SHAPES: (11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0634__00n1 = np.einsum('cd,ab->abcd', v0633__00m_.reshape((11, 100)) ,np.ones((1, 2))).reshape((1, 2, 11, 100))

# op _00na expand_array_eval
# LANG: bbb --> _00nb
# SHAPES: (1, 2, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0631__00nb = np.einsum('abd,c->abcd', v0623_bbb.reshape((1, 2, 100)) ,np.ones((11,))).reshape((1, 2, 11, 100))

# op _00ng expand_array_eval
# LANG: aaa --> _00nh
# SHAPES: (1, 2, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0636__00nh = np.einsum('abd,c->abcd', v0621_aaa.reshape((1, 2, 100)) ,np.ones((11,))).reshape((1, 2, 11, 100))

# op _00p3 reshape_eval
# LANG: _00oV --> _00p4
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0673__00p4 = v0672__00oV.reshape((1, 1, 2))

# op _00p6 reshape_eval
# LANG: _00oY --> _00p7
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0676__00p7 = v0675__00oY.reshape((1, 1, 2))

# op _00p8 reshape_eval
# LANG: _00p0 --> _00p9
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0678__00p9 = v0677__00p0.reshape((1, 1, 2))

# op _00TS_power_combination_eval
# LANG: rel_obs_dist, _00TR --> _00TT
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01549__00TT = (v01548__00TR**1)*(v01541_rel_obs_dist**-1)
v01549__00TT = (v01549__00TT*_00TS_coeff).reshape((1, 1, 2))

# op _00UO reshape_eval
# LANG: _00UN --> _00UP
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01571__00UP = v01570__00UN.reshape((1, 40))

# op _00ZK_cos_eval
# LANG: _00Vv --> _00ZL
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01661__00ZL = np.cos(v01660__00Vv)

# op _00ZS_cos_eval
# LANG: _00Vv --> _00ZT
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01722__00ZT = np.cos(v01660__00Vv)

# op _00_7_power_combination_eval
# LANG: dDdR_real_exp, real_weighting --> _00_8
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01738__00_8 = (v01729_real_weighting**1)*(v01665_dDdR_real_exp**1)
v01738__00_8 = (v01738__00_8*_00_7_coeff).reshape((1, 2, 3, 40, 11))

# op _00_9_power_combination_eval
# LANG: dDdR_imag_exp, imag_weighting --> _00_a
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01740__00_a = (v01732_imag_weighting**1)*(v01726_dDdR_imag_exp**1)
v01740__00_a = (v01740__00_a*_00_9_coeff).reshape((1, 2, 3, 40, 11))

# op _00_j_power_combination_eval
# LANG: dDdR_imag_exp, real_weighting --> _00_k
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01770__00_k = (v01729_real_weighting**1)*(v01726_dDdR_imag_exp**1)
v01770__00_k = (v01770__00_k*_00_j_coeff).reshape((1, 2, 3, 40, 11))

# op _00_l_power_combination_eval
# LANG: dDdR_real_exp, imag_weighting --> _00_m
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01772__00_m = (v01732_imag_weighting**1)*(v01665_dDdR_real_exp**1)
v01772__00_m = (v01772__00_m*_00_l_coeff).reshape((1, 2, 3, 40, 11))

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
# SHAPES: (1, 1, 2), (1, 1, 2), (1, 1, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0595_rel_obs_position__temp[i_v0581_rel_obs_x_pos__00lT_indexed_passthrough_eval] = v0581_rel_obs_x_pos.flatten()
v0595_rel_obs_position = v0595_rel_obs_position__temp.copy()
v0595_rel_obs_position__temp[i_v0589_rel_obs_y_pos__00lT_indexed_passthrough_eval] = v0589_rel_obs_y_pos.flatten()
v0595_rel_obs_position = v0595_rel_obs_position__temp.copy()
v0595_rel_obs_position__temp[i_v0593_rel_obs_z_pos__00lT_indexed_passthrough_eval] = v0593_rel_obs_z_pos.flatten()
v0595_rel_obs_position = v0595_rel_obs_position__temp.copy()

# op _00m3_power_combination_eval
# LANG: _00m2 --> rel_obs_dist
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0601_rel_obs_dist = (v0599__00m2**0.5)
v0601_rel_obs_dist = (v0601_rel_obs_dist*_00m3_coeff).reshape((1, 1, 2))

# op _00mX expand_array_eval
# LANG: _00mW --> _00mY
# SHAPES: (11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0628__00mY = np.einsum('cd,ab->abcd', v0627__00mW.reshape((11, 100)) ,np.ones((1, 2))).reshape((1, 2, 11, 100))

# op _00n2 expand_array_eval
# LANG: bbb --> _00n3
# SHAPES: (1, 2, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0624__00n3 = np.einsum('abd,c->abcd', v0623_bbb.reshape((1, 2, 100)) ,np.ones((11,))).reshape((1, 2, 11, 100))

# op _00n6 expand_array_eval
# LANG: aaa --> _00n7
# SHAPES: (1, 2, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0629__00n7 = np.einsum('abd,c->abcd', v0621_aaa.reshape((1, 2, 100)) ,np.ones((11,))).reshape((1, 2, 11, 100))

# op _00nc_power_combination_eval
# LANG: _00nb, _00n1 --> _00nd
# SHAPES: (1, 2, 11, 100), (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0632__00nd = (v0631__00nb**1)*(v0634__00n1**1)
v0632__00nd = (v0632__00nd*_00nc_coeff).reshape((1, 2, 11, 100))

# op _00ni_power_combination_eval
# LANG: _00n1, _00nh --> _00nj
# SHAPES: (1, 2, 11, 100), (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0637__00nj = (v0636__00nh**1)*(v0634__00n1**1)
v0637__00nj = (v0637__00nj*_00ni_coeff).reshape((1, 2, 11, 100))

# op _00oz reshape_eval
# LANG: rpm --> _00oA
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0683__00oA = v0164_rpm.reshape((1,))

# op _00p5_indexed_passthrough_eval
# LANG: _00p4, _00p7, _00p9 --> aircraft_vel
# SHAPES: (1, 1, 2), (1, 1, 2), (1, 1, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0674_aircraft_vel__temp[i_v0673__00p4__00p5_indexed_passthrough_eval] = v0673__00p4.flatten()
v0674_aircraft_vel = v0674_aircraft_vel__temp.copy()
v0674_aircraft_vel__temp[i_v0676__00p7__00p5_indexed_passthrough_eval] = v0676__00p7.flatten()
v0674_aircraft_vel = v0674_aircraft_vel__temp.copy()
v0674_aircraft_vel__temp[i_v0678__00p9__00p5_indexed_passthrough_eval] = v0678__00p9.flatten()
v0674_aircraft_vel = v0674_aircraft_vel__temp.copy()

# op _00Sb_power_combination_eval
# LANG: temperature --> _00Sc
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01493__00Sc = (v01481_temperature**1)
v01493__00Sc = (v01493__00Sc*_00Sb_coeff).reshape((1,))

# op _00TU arccos_eval
# LANG: _00TT --> _00TV
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01550__00TV = np.arccos(v01549__00TT)

# op _00VI expand_array_eval
# LANG: _00UP --> _00VJ
# SHAPES: (1, 40) --> (1, 2, 3, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01572__00VJ = np.einsum('ad,bce->abcde', v01571__00UP.reshape((1, 40)) ,np.ones((2, 3, 1))).reshape((1, 2, 3, 40, 1))

# op _00ZM_power_combination_eval
# LANG: _00ZH, _00ZL --> _00ZN
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01659__00ZN = (v01643__00ZH**1)*(v01661__00ZL**1)
v01659__00ZN = (v01659__00ZN*_00ZM_coeff).reshape((1, 2, 3, 40, 10))

# op _00ZU_power_combination_eval
# LANG: _00ZJ, _00ZT --> _00ZV
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01721__00ZV = (v01720__00ZJ**1)*(v01722__00ZT**1)
v01721__00ZV = (v01721__00ZV*_00ZU_coeff).reshape((1, 2, 3, 40, 10))

# op _00_H_linear_combination_eval
# LANG: lam_var, n_var --> _00_I
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01743__00_I = _00_H_constant+1*v01742_n_var+-1*v01574_lam_var

# op _00_P_power_combination_eval
# LANG: n_var --> _00_Q
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01748__00_Q = (v01742_n_var**1)
v01748__00_Q = (v01748__00_Q*_00_P_coeff).reshape((1, 2, 3, 40, 11))

# op _00_b_linear_combination_eval
# LANG: _00_8, _00_a --> _00_c
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01739__00_c = _00_b_constant+1*v01738__00_8+1*v01740__00_a

# op _00_n_linear_combination_eval
# LANG: _00_k, _00_m --> _00_o
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01771__00_o = _00_n_constant+1*v01770__00_k+1*v01772__00_m

# op _00_p_power_combination_eval
# LANG: n_var --> _00_q
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01753__00_q = (v01742_n_var**1)
v01753__00_q = (v01753__00_q*_00_p_coeff).reshape((1, 2, 3, 40, 11))

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

# op _00n4_power_combination_eval
# LANG: _00n3, _00mY --> aT_integrand
# SHAPES: (1, 2, 11, 100), (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0625_aT_integrand = (v0624__00n3**1)*(v0628__00mY**1)
v0625_aT_integrand = (v0625_aT_integrand*_00n4_coeff).reshape((1, 2, 11, 100))

# op _00n8_power_combination_eval
# LANG: _00mY, _00n7 --> aD_integrand
# SHAPES: (1, 2, 11, 100), (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0630_aD_integrand = (v0629__00n7**1)*(v0628__00mY**1)
v0630_aD_integrand = (v0630_aD_integrand*_00n8_coeff).reshape((1, 2, 11, 100))

# op _00ne_power_combination_eval
# LANG: _00nd --> bT_integrand
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0635_bT_integrand = (v0632__00nd**1)
v0635_bT_integrand = (v0635_bT_integrand*_00ne_coeff).reshape((1, 2, 11, 100))

# op _00nk_power_combination_eval
# LANG: _00nj --> bD_integrand
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model
v0638_bD_integrand = (v0637__00nj**1)
v0638_bD_integrand = (v0638_bD_integrand*_00nk_coeff).reshape((1, 2, 11, 100))

# op _00oB_power_combination_eval
# LANG: _00oA --> _00oC
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0684__00oC = (v0683__00oA**1)
v0684__00oC = (v0684__00oC*_00oB_coeff).reshape((1,))

# op _00oR reshape_eval
# LANG: rel_obs_dist --> _00oS
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0695__00oS = v0601_rel_obs_dist.reshape((1, 2))

# op _00pa_tensor_dot_product_eval
# LANG: aircraft_vel, rel_obs_position --> _00pb
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0697__00pb = np.sum(v0674_aircraft_vel * v0595_rel_obs_position, axis=1)

# op _010a_linear_combination_eval
# LANG: lam_var, n_var --> _010b
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01774__010b = _010a_constant+1*v01742_n_var+-1*v01574_lam_var

# op _010i_power_combination_eval
# LANG: n_var --> _010j
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01778__010j = (v01742_n_var**1)
v01778__010j = (v01778__010j*_010i_coeff).reshape((1, 2, 3, 40, 11))

# op _00Sd_power_combination_eval
# LANG: _00Sc --> speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01494_speed_of_sound = (v01493__00Sc**0.5)
v01494_speed_of_sound = (v01494_speed_of_sound*_00Sd_coeff).reshape((1,))

# op _00TY reshape_eval
# LANG: _00TV --> rel_angle_normal
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01551_rel_angle_normal = v01550__00TV.reshape((1, 2))

# op _00VK_indexed_passthrough_eval
# LANG: _00VJ, _00ZN --> dTdR_real_exp
# SHAPES: (1, 2, 3, 40, 1), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01573_dTdR_real_exp__temp[i_v01572__00VJ__00VK_indexed_passthrough_eval] = v01572__00VJ.flatten()
v01573_dTdR_real_exp = v01573_dTdR_real_exp__temp.copy()
v01573_dTdR_real_exp__temp[i_v01659__00ZN__00VK_indexed_passthrough_eval] = v01659__00ZN.flatten()
v01573_dTdR_real_exp = v01573_dTdR_real_exp__temp.copy()

# op _00ZW_indexed_passthrough_eval
# LANG: _00ZV --> dTdR_imag_exp
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01723_dTdR_imag_exp__temp[i_v01721__00ZV__00ZW_indexed_passthrough_eval] = v01721__00ZV.flatten()
v01723_dTdR_imag_exp = v01723_dTdR_imag_exp__temp.copy()

# op _00_J_power_combination_eval
# LANG: _00_c, _00_I --> _00_K
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01741__00_K = (v01739__00_c**1)*(v01743__00_I**1)
v01741__00_K = (v01741__00_K*_00_J_coeff).reshape((1, 2, 3, 40, 11))

# op _00_R_power_combination_eval
# LANG: _00UZ, _00_Q --> _00_S
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01749__00_S = (v01748__00_Q**1)*(v01580__00UZ**1)
v01749__00_S = (v01749__00_S*_00_R_coeff).reshape((1, 2, 3, 40, 11))

# op _00_r_power_combination_eval
# LANG: _00UZ, _00_q --> _00_s
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01754__00_s = (v01753__00_q**1)*(v01580__00UZ**1)
v01754__00_s = (v01754__00_s*_00_r_coeff).reshape((1, 2, 3, 40, 11))

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

# op _00nJ_decompose_eval
# LANG: aD_integrand --> _00nK, _00nL
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 99), (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0648__00nK = ((v0630_aD_integrand.flatten())[src_indices__00nK__00nJ]).reshape((1, 2, 11, 99))
v0649__00nL = ((v0630_aD_integrand.flatten())[src_indices__00nL__00nJ]).reshape((1, 2, 11, 99))

# op _00n__decompose_eval
# LANG: bT_integrand --> _00o0, _00o1
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 99), (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0656__00o0 = ((v0635_bT_integrand.flatten())[src_indices__00o0__00n_]).reshape((1, 2, 11, 99))
v0657__00o1 = ((v0635_bT_integrand.flatten())[src_indices__00o1__00n_]).reshape((1, 2, 11, 99))

# op _00ns_decompose_eval
# LANG: aT_integrand --> _00nt, _00nu
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 99), (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0639__00nt = ((v0625_aT_integrand.flatten())[src_indices__00nt__00ns]).reshape((1, 2, 11, 99))
v0640__00nu = ((v0625_aT_integrand.flatten())[src_indices__00nu__00ns]).reshape((1, 2, 11, 99))

# op _00oD_power_combination_eval
# LANG: _00oC --> _00oE
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0685__00oE = (v0684__00oC**1)
v0685__00oE = (v0685__00oE*_00oD_coeff).reshape((1,))

# op _00og_decompose_eval
# LANG: bD_integrand --> _00oh, _00oi
# SHAPES: (1, 2, 11, 100) --> (1, 2, 11, 99), (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0664__00oh = ((v0638_bD_integrand.flatten())[src_indices__00oh__00og]).reshape((1, 2, 11, 99))
v0665__00oi = ((v0638_bD_integrand.flatten())[src_indices__00oi__00og]).reshape((1, 2, 11, 99))

# op _00pc_power_combination_eval
# LANG: _00oS, _00pb --> _00pd
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0698__00pd = (v0697__00pb**1)*(v0695__00oS**-1)
v0698__00pd = (v0698__00pd*_00pc_coeff).reshape((1, 2))

# op _00pe expand_scalar_eval
# LANG: speed_of_sound --> _00pf
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0700__00pf = np.empty((1, 2))
v0700__00pf.fill(v0554_speed_of_sound.item())

# op _010c_power_combination_eval
# LANG: _00_o, _010b --> _010d
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01773__010d = (v01771__00_o**1)*(v01774__010b**1)
v01773__010d = (v01773__010d*_010c_coeff).reshape((1, 2, 3, 40, 11))

# op _010k_power_combination_eval
# LANG: _00UZ, _010j --> _010l
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01779__010l = (v01778__010j**1)*(v01580__00UZ**1)
v01779__010l = (v01779__010l*_010k_coeff).reshape((1, 2, 3, 40, 11))

# op _00UU expand_array_eval
# LANG: rel_angle_normal --> _00UV
# SHAPES: (1, 2) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01735__00UV = np.einsum('ab,cde->abcde', v01551_rel_angle_normal.reshape((1, 2)) ,np.ones((3, 40, 11))).reshape((1, 2, 3, 40, 11))

# op _00V1 expand_scalar_eval
# LANG: speed_of_sound --> _00V2
# SHAPES: (1,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01746__00V2 = np.empty((1, 2, 3, 40, 11))
v01746__00V2.fill(v01494_speed_of_sound.item())

# op _00_1_power_combination_eval
# LANG: dTdR_real_exp, real_weighting --> _00_2
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01730__00_2 = (v01729_real_weighting**1)*(v01573_dTdR_real_exp**1)
v01730__00_2 = (v01730__00_2*_00_1_coeff).reshape((1, 2, 3, 40, 11))

# op _00_3_power_combination_eval
# LANG: dTdR_imag_exp, imag_weighting --> _00_4
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01733__00_4 = (v01732_imag_weighting**1)*(v01723_dTdR_imag_exp**1)
v01733__00_4 = (v01733__00_4*_00_3_coeff).reshape((1, 2, 3, 40, 11))

# op _00_L_power_combination_eval
# LANG: _00_K --> _00_M
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01744__00_M = (v01741__00_K**1)
v01744__00_M = (v01744__00_M*_00_L_coeff).reshape((1, 2, 3, 40, 11))

# op _00_T_power_combination_eval
# LANG: _00UX, _00_S --> _00_U
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01750__00_U = (v01749__00_S**1)*(v01569__00UX**1)
v01750__00_U = (v01750__00_U*_00_T_coeff).reshape((1, 2, 3, 40, 11))

# op _00_d_power_combination_eval
# LANG: dTdR_imag_exp, real_weighting --> _00_e
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01764__00_e = (v01729_real_weighting**1)*(v01723_dTdR_imag_exp**1)
v01764__00_e = (v01764__00_e*_00_d_coeff).reshape((1, 2, 3, 40, 11))

# op _00_f_power_combination_eval
# LANG: dTdR_real_exp, imag_weighting --> _00_g
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01766__00_g = (v01732_imag_weighting**1)*(v01573_dTdR_real_exp**1)
v01766__00_g = (v01766__00_g*_00_f_coeff).reshape((1, 2, 3, 40, 11))

# op _00_t_power_combination_eval
# LANG: _00UX, _00_s --> _00_u
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01755__00_u = (v01754__00_s**1)*(v01569__00UX**1)
v01755__00_u = (v01755__00_u*_00_t_coeff).reshape((1, 2, 3, 40, 11))

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

# op _00nM_linear_combination_eval
# LANG: _00nK, _00nL --> _00nN
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0650__00nN = _00nM_constant+1*v0648__00nK+1*v0649__00nL

# op _00nv_linear_combination_eval
# LANG: _00nt, _00nu --> _00nw
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0641__00nw = _00nv_constant+1*v0639__00nt+1*v0640__00nu

# op _00o2_linear_combination_eval
# LANG: _00o0, _00o1 --> _00o3
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0658__00o3 = _00o2_constant+1*v0656__00o0+1*v0657__00o1

# op _00oF_power_combination_eval
# LANG: _00oE --> _00oG
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0686__00oG = (v0685__00oE**1)
v0686__00oG = (v0686__00oG*_00oF_coeff).reshape((1,))

# op _00oj_linear_combination_eval
# LANG: _00oh, _00oi --> _00ok
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0666__00ok = _00oj_constant+1*v0664__00oh+1*v0665__00oi

# op _00pg_power_combination_eval
# LANG: _00pd, _00pf --> _00ph
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0699__00ph = (v0698__00pd**1)*(v0700__00pf**-1)
v0699__00ph = (v0699__00ph*_00pg_coeff).reshape((1, 2))

# op _010e_power_combination_eval
# LANG: _010d --> _010f
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01775__010f = (v01773__010d**1)
v01775__010f = (v01775__010f*_010e_coeff).reshape((1, 2, 3, 40, 11))

# op _010m_power_combination_eval
# LANG: _00UX, _010l --> _010n
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01780__010n = (v01779__010l**1)*(v01569__00UX**1)
v01780__010n = (v01780__010n*_010m_coeff).reshape((1, 2, 3, 40, 11))

# op _00_5_linear_combination_eval
# LANG: _00_2, _00_4 --> _00_6
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01731__00_6 = _00_5_constant+1*v01730__00_2+1*v01733__00_4

# op _00_D_cos_eval
# LANG: _00UV --> _00_E
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01736__00_E = np.cos(v01735__00UV)

# op _00_N_power_combination_eval
# LANG: _00_M, _00V2 --> _00_O
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01745__00_O = (v01744__00_M**1)*(v01746__00V2**1)
v01745__00_O = (v01745__00_O*_00_N_coeff).reshape((1, 2, 3, 40, 11))

# op _00_V_power_combination_eval
# LANG: _00V0, _00_U --> _00_W
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01751__00_W = (v01750__00_U**1)*(v01589__00V0**1)
v01751__00_W = (v01751__00_W*_00_V_coeff).reshape((1, 2, 3, 40, 11))

# op _00_h_linear_combination_eval
# LANG: _00_e, _00_g --> _00_i
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01765__00_i = _00_h_constant+1*v01764__00_e+1*v01766__00_g

# op _00_v_power_combination_eval
# LANG: _00V0, _00_u --> _00_w
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01756__00_w = (v01755__00_u**1)*(v01589__00V0**1)
v01756__00_w = (v01756__00_w*_00_v_coeff).reshape((1, 2, 3, 40, 11))

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

# op _00nO_power_combination_eval
# LANG: _00nN --> _00nP
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0651__00nP = (v0650__00nN**1)
v0651__00nP = (v0651__00nP*_00nO_coeff).reshape((1, 2, 11, 99))

# op _00nQ expand_scalar_eval
# LANG: dtheta --> _00nR
# SHAPES: (1,) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0653__00nR = np.empty((1, 2, 11, 99))
v0653__00nR.fill(v0644_dtheta.item())

# op _00nx_power_combination_eval
# LANG: _00nw --> _00ny
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0642__00ny = (v0641__00nw**1)
v0642__00ny = (v0642__00ny*_00nx_coeff).reshape((1, 2, 11, 99))

# op _00nz expand_scalar_eval
# LANG: dtheta --> _00nA
# SHAPES: (1,) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0645__00nA = np.empty((1, 2, 11, 99))
v0645__00nA.fill(v0644_dtheta.item())

# op _00o4_power_combination_eval
# LANG: _00o3 --> _00o5
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0659__00o5 = (v0658__00o3**1)
v0659__00o5 = (v0659__00o5*_00o4_coeff).reshape((1, 2, 11, 99))

# op _00o6 expand_scalar_eval
# LANG: dtheta --> _00o7
# SHAPES: (1,) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0661__00o7 = np.empty((1, 2, 11, 99))
v0661__00o7.fill(v0644_dtheta.item())

# op _00ol_power_combination_eval
# LANG: _00ok --> _00om
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0667__00om = (v0666__00ok**1)
v0667__00om = (v0667__00om*_00ol_coeff).reshape((1, 2, 11, 99))

# op _00on expand_scalar_eval
# LANG: dtheta --> _00oo
# SHAPES: (1,) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0669__00oo = np.empty((1, 2, 11, 99))
v0669__00oo.fill(v0644_dtheta.item())

# op _00pB expand_scalar_eval
# LANG: _00oG --> _00pC
# SHAPES: (1,) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0687__00pC = np.empty((1, 2, 3, 2, 11))
v0687__00pC.fill(v0686__00oG.item())

# op _00pi_linear_combination_eval
# LANG: _00ph --> _00pj
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0701__00pj = _00pi_constant+-1*v0699__00ph

# op _00pr expand_array_eval
# LANG: in_plane_ex --> _00ps
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0718__00ps = np.einsum('ab,c->abc', v0181_in_plane_ex.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _0106_cos_eval
# LANG: _00UV --> _0107
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01768__0107 = np.cos(v01735__00UV)

# op _010g_power_combination_eval
# LANG: _00V2, _010f --> _010h
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01776__010h = (v01775__010f**1)*(v01746__00V2**1)
v01776__010h = (v01776__010h*_010g_coeff).reshape((1, 2, 3, 40, 11))

# op _010o_power_combination_eval
# LANG: _00V0, _010n --> _010p
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01781__010p = (v01780__010n**1)*(v01589__00V0**1)
v01781__010p = (v01781__010p*_010o_coeff).reshape((1, 2, 3, 40, 11))

# op _014a expand_scalar_eval
# LANG: Vx --> _014b
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01886__014b = np.empty((1, 1))
v01886__014b.fill(v0977_u.item())

# op _014d expand_scalar_eval
# LANG: Vy --> _014e
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01888__014e = np.empty((1, 1))
v01888__014e.fill(v0978_v.item())

# op _014f expand_scalar_eval
# LANG: Vz --> _014g
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01889__014g = np.empty((1, 1))
v01889__014g.fill(v0979_w.item())

# op _00_F_power_combination_eval
# LANG: _00_6, _00_E --> _00_G
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01734__00_G = (v01731__00_6**1)*(v01736__00_E**1)
v01734__00_G = (v01734__00_G*_00_F_coeff).reshape((1, 2, 3, 40, 11))

# op _00_X_power_combination_eval
# LANG: _00_O, _00_W --> _00_Y
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01747__00_Y = (v01745__00_O**1)*(v01751__00_W**-1)
v01747__00_Y = (v01747__00_Y*_00_X_coeff).reshape((1, 2, 3, 40, 11))

# op _00_x_power_combination_eval
# LANG: _00V2, _00_w --> _00_y
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01757__00_y = (v01756__00_w**1)*(v01746__00V2**-1)
v01757__00_y = (v01757__00_y*_00_x_coeff).reshape((1, 2, 3, 40, 11))

# op _00_z_sin_eval
# LANG: _00UV --> _00_A
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01759__00_A = np.sin(v01735__00UV)

# op _00iP_matvec_eval
# LANG: rot_mat, _00iO --> thrust_dir
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0494_thrust_dir = v0486_rot_mat@v0497__00iO

# op _00nB_power_combination_eval
# LANG: _00ny, _00nA --> _00nC
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0643__00nC = (v0642__00ny**1)*(v0645__00nA**1)
v0643__00nC = (v0643__00nC*_00nB_coeff).reshape((1, 2, 11, 99))

# op _00nS_power_combination_eval
# LANG: _00nP, _00nR --> _00nT
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0652__00nT = (v0651__00nP**1)*(v0653__00nR**1)
v0652__00nT = (v0652__00nT*_00nS_coeff).reshape((1, 2, 11, 99))

# op _00o8_power_combination_eval
# LANG: _00o5, _00o7 --> _00o9
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0660__00o9 = (v0659__00o5**1)*(v0661__00o7**1)
v0660__00o9 = (v0660__00o9*_00o8_coeff).reshape((1, 2, 11, 99))

# op _00op_power_combination_eval
# LANG: _00om, _00oo --> _00oq
# SHAPES: (1, 2, 11, 99), (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0668__00oq = (v0667__00om**1)*(v0669__00oo**1)
v0668__00oq = (v0668__00oq*_00op_coeff).reshape((1, 2, 11, 99))

# op _00pL expand_scalar_eval
# LANG: propeller_radius --> _00pM
# SHAPES: (1,) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0715__00pM = np.empty((1, 2, 3, 2, 11))
v0715__00pM.fill(v0482_propeller_radius.item())

# op _00pk_power_combination_eval
# LANG: _00oS, _00pj --> _00pl
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0696__00pl = (v0695__00oS**1)*(v0701__00pj**1)
v0696__00pl = (v0696__00pl*_00pk_coeff).reshape((1, 2))

# op _00pt_tensor_dot_product_eval
# LANG: _00ps, rel_obs_position --> _00pu
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0717__00pu = np.sum(v0595_rel_obs_position * v0718__00ps, axis=1)

# op _00qi_power_combination_eval
# LANG: n_var, _00pC --> _00qj
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0713__00qj = (v0681_n_var**1)*(v0687__00pC**1)
v0713__00qj = (v0713__00qj*_00qi_coeff).reshape((1, 2, 3, 2, 11))

# op _0108_power_combination_eval
# LANG: _00_i, _0107 --> _0109
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01767__0109 = (v01765__00_i**1)*(v01768__0107**1)
v01767__0109 = (v01767__0109*_0108_coeff).reshape((1, 2, 3, 40, 11))

# op _010q_power_combination_eval
# LANG: _010h, _010p --> _010r
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01777__010r = (v01776__010h**1)*(v01781__010p**-1)
v01777__010r = (v01777__010r*_010q_coeff).reshape((1, 2, 3, 40, 11))

# op _014c_indexed_passthrough_eval
# LANG: _014b, _014e, _014g --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01887_V_aircraft__temp[i_v01886__014b__014c_indexed_passthrough_eval] = v01886__014b.flatten()
v01887_V_aircraft = v01887_V_aircraft__temp.copy()
v01887_V_aircraft__temp[i_v01888__014e__014c_indexed_passthrough_eval] = v01888__014e.flatten()
v01887_V_aircraft = v01887_V_aircraft__temp.copy()
v01887_V_aircraft__temp[i_v01889__014g__014c_indexed_passthrough_eval] = v01889__014g.flatten()
v01887_V_aircraft = v01887_V_aircraft__temp.copy()

# op _00_B_power_combination_eval
# LANG: _00_y, _00_A --> _00_C
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01758__00_C = (v01757__00_y**1)*(v01759__00_A**1)
v01758__00_C = (v01758__00_C*_00_B_coeff).reshape((1, 2, 3, 40, 11))

# op _00_Z_linear_combination_eval
# LANG: _00_G, _00_Y --> _00__
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01737__00__ = _00_Z_constant+1*v01734__00_G+-1*v01747__00_Y

# op _00nD_power_combination_eval
# LANG: _00nC --> _00nE
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0646__00nE = (v0643__00nC**1)
v0646__00nE = (v0646__00nE*_00nD_coeff).reshape((1, 2, 11, 99))

# op _00nU_power_combination_eval
# LANG: _00nT --> _00nV
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0654__00nV = (v0652__00nT**1)
v0654__00nV = (v0654__00nV*_00nU_coeff).reshape((1, 2, 11, 99))

# op _00oa_power_combination_eval
# LANG: _00o9 --> _00ob
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0662__00ob = (v0660__00o9**1)
v0662__00ob = (v0662__00ob*_00oa_coeff).reshape((1, 2, 11, 99))

# op _00or_power_combination_eval
# LANG: _00oq --> _00os
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11, 99)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0670__00os = (v0668__00oq**1)
v0670__00os = (v0670__00os*_00or_coeff).reshape((1, 2, 11, 99))

# op _00pF expand_array_eval
# LANG: _00pu --> _00pG
# SHAPES: (1, 2) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0719__00pG = np.einsum('ab,cde->abcde', v0717__00pu.reshape((1, 2)) ,np.ones((3, 2, 11))).reshape((1, 2, 3, 2, 11))

# op _00pH expand_scalar_eval
# LANG: speed_of_sound --> _00pI
# SHAPES: (1,) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0693__00pI = np.empty((1, 2, 3, 2, 11))
v0693__00pI.fill(v0554_speed_of_sound.item())

# op _00pJ expand_array_eval
# LANG: _00pl --> _00pK
# SHAPES: (1, 2) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0702__00pK = np.einsum('ab,cde->abcde', v0696__00pl.reshape((1, 2)) ,np.ones((3, 2, 11))).reshape((1, 2, 3, 2, 11))

# op _00po expand_array_eval
# LANG: thrust_dir --> _00pp
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0690__00pp = np.einsum('b,ac->abc', v0494_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00qk_power_combination_eval
# LANG: _00qj, _00pM --> _00ql
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0714__00ql = (v0713__00qj**1)*(v0715__00pM**1)
v0714__00ql = (v0714__00ql*_00qk_coeff).reshape((1, 2, 3, 2, 11))

# op _010s_linear_combination_eval
# LANG: _0109, _010r --> _010t
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01769__010t = _010s_constant+1*v01767__0109+-1*v01777__010r

# op _014h expand_array_eval
# LANG: V_aircraft --> _014i
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01896__014i = np.einsum('ab,c->abc', v01887_V_aircraft.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _014n expand_array_eval
# LANG: time_vectors --> _014o
# SHAPES: (2,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01902__014o = np.einsum('c,ab->abc', v01901_time_vectors.reshape((2,)) ,np.ones((1, 3))).reshape((1, 3, 2))

# op _00nF_single_tensor_sum_with_axis_eval
# LANG: _00nE --> aT
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aT_load_integration_model
v0647_aT = np.sum(v0646__00nE, axis = (3,)).reshape((1, 2, 11))

# op _00nW_single_tensor_sum_with_axis_eval
# LANG: _00nV --> aD
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.aD_load_integration_model
v0655_aD = np.sum(v0654__00nV, axis = (3,)).reshape((1, 2, 11))

# op _00oc_single_tensor_sum_with_axis_eval
# LANG: _00ob --> bT
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bT_load_integration_model
v0663_bT = np.sum(v0662__00ob, axis = (3,)).reshape((1, 2, 11))

# op _00ot_single_tensor_sum_with_axis_eval
# LANG: _00os --> bD
# SHAPES: (1, 2, 11, 99) --> (1, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.load_integration_model.bD_load_integration_model
v0671_bD = np.sum(v0670__00os, axis = (3,)).reshape((1, 2, 11))

# op _00pv_tensor_dot_product_eval
# LANG: _00pp, rel_obs_position --> _00pw
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0689__00pw = np.sum(v0595_rel_obs_position * v0690__00pp, axis=1)

# op _00qm_power_combination_eval
# LANG: _00ql, _00pG --> _00qn
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0716__00qn = (v0714__00ql**1)*(v0719__00pG**1)
v0716__00qn = (v0716__00qn*_00qm_coeff).reshape((1, 2, 3, 2, 11))

# op _00qo_power_combination_eval
# LANG: _00pI, _00pK --> _00qp
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0721__00qp = (v0693__00pI**1)*(v0702__00pK**1)
v0721__00qp = (v0721__00qp*_00qo_coeff).reshape((1, 2, 3, 2, 11))

# op _00r1_exp_a_eval
# LANG: lam_var --> _00r2
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0747__00r2 = _00r1_exp_a_eval_a**v0726_lam_var

# op _00rZ_exp_a_eval
# LANG: lam_var --> _00r_
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0780__00r_ = _00rZ_exp_a_eval_a**v0726_lam_var

# op _0100_power_combination_eval
# LANG: coeff_matrix_A, _00__ --> _0101
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01728__0101 = (v01727_coeff_matrix_A**1)*(v01737__00__**1)
v01728__0101 = (v01728__0101*_0100_coeff).reshape((1, 2, 3, 40, 11))

# op _0102_bessel_eval
# LANG: _00_C --> _0103
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01760__0103=_0102_bessel_eval(_0102_bessel_eval_order,v01758__00_C)

# op _010u_power_combination_eval
# LANG: coeff_matrix_B, _010t --> _010v
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01763__010v = (v01762_coeff_matrix_B**1)*(v01769__010t**1)
v01763__010v = (v01763__010v*_010u_coeff).reshape((1, 2, 3, 40, 11))

# op _010w_bessel_eval
# LANG: _00_C --> _010x
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01783__010x=_010w_bessel_eval(_010w_bessel_eval_order,v01758__00_C)

# op _0128_power_combination_eval
# LANG: rotor_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v01829_origin = (v012_rotor_disk_origin**1)
v01829_origin = (v01829_origin*_0128_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _012b_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _012c
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v01830__012c = (v08_rotor_disk_in_plane_1**1)
v01830__012c = (v01830__012c*_012b_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _012e_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _012f
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v01848__012f = (v010_rotor_disk_in_plane_2**1)
v01848__012f = (v01848__012f*_012e_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _014k expand_array_eval
# LANG: aircraft_location --> _014l
# SHAPES: (3, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01891__014l = np.einsum('bc,a->abc', v01890_aircraft_location.reshape((3, 2)) ,np.ones((1,))).reshape((1, 3, 2))

# op _014r_decompose_eval
# LANG: _014i --> _014s, _014A, _014H
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01897__014s = ((v01896__014i.flatten())[src_indices__014s__014r]).reshape((1, 1, 2))
v01898__014A = ((v01896__014i.flatten())[src_indices__014A__014r]).reshape((1, 1, 2))
v01899__014H = ((v01896__014i.flatten())[src_indices__014H__014r]).reshape((1, 1, 2))

# op _014t_decompose_eval
# LANG: _014o --> _014u, _014B, _014I
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01903__014u = ((v01902__014o.flatten())[src_indices__014u__014t]).reshape((1, 1, 2))
v01904__014B = ((v01902__014o.flatten())[src_indices__014B__014t]).reshape((1, 1, 2))
v01905__014I = ((v01902__014o.flatten())[src_indices__014I__014t]).reshape((1, 1, 2))

# op _00J3_power_combination_eval
# LANG: _angular_speed --> _00J4
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01384__00J4 = (v01158__angular_speed**1)
v01384__00J4 = (v01384__00J4*_00J3_coeff).reshape((1, 40, 30))

# op _00pD expand_array_eval
# LANG: _00pw --> _00pE
# SHAPES: (1, 2) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0691__00pE = np.einsum('ab,cde->abcde', v0689__00pw.reshape((1, 2)) ,np.ones((3, 2, 11))).reshape((1, 2, 3, 2, 11))

# op _00pN expand_array_eval
# LANG: aT --> _00pO
# SHAPES: (1, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0711__00pO = np.einsum('ade,bc->abcde', v0647_aT.reshape((1, 2, 11)) ,np.ones((2, 3))).reshape((1, 2, 3, 2, 11))

# op _00pP expand_array_eval
# LANG: bT --> _00pQ
# SHAPES: (1, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0707__00pQ = np.einsum('ade,bc->abcde', v0663_bT.reshape((1, 2, 11)) ,np.ones((2, 3))).reshape((1, 2, 3, 2, 11))

# op _00pR expand_array_eval
# LANG: aD --> _00pS
# SHAPES: (1, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0740__00pS = np.einsum('ade,bc->abcde', v0655_aD.reshape((1, 2, 11)) ,np.ones((2, 3))).reshape((1, 2, 3, 2, 11))

# op _00pT expand_array_eval
# LANG: bD --> _00pU
# SHAPES: (1, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0737__00pU = np.einsum('ade,bc->abcde', v0671_bD.reshape((1, 2, 11)) ,np.ones((2, 3))).reshape((1, 2, 3, 2, 11))

# op _00q4_power_combination_eval
# LANG: n_var, _00pC --> _00q5
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0682__00q5 = (v0681_n_var**1)*(v0687__00pC**1)
v0682__00q5 = (v0682__00q5*_00q4_coeff).reshape((1, 2, 3, 2, 11))

# op _00q8_power_combination_eval
# LANG: _00pK --> _00q9
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0703__00q9 = (v0702__00pK**2)
v0703__00q9 = (v0703__00q9*_00q8_coeff).reshape((1, 2, 3, 2, 11))

# op _00qI_exp_a_eval
# LANG: lam_var --> _00qJ
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0727__00qJ = _00qI_exp_a_eval_a**v0726_lam_var

# op _00qq_power_combination_eval
# LANG: _00qn, _00qp --> _00qr
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0720__00qr = (v0716__00qn**1)*(v0721__00qp**-1)
v0720__00qr = (v0720__00qr*_00qq_coeff).reshape((1, 2, 3, 2, 11))

# op _00r3_power_combination_eval
# LANG: A_lin_comb_sign_matrix, _00r2 --> _00r4
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0746__00r4 = (v0724_A_lin_comb_sign_matrix**1)*(v0747__00r2**1)
v0746__00r4 = (v0746__00r4*_00r3_coeff).reshape((1, 2, 3, 2, 11))

# op _00r5_linear_combination_eval
# LANG: n_var, lam_var --> _00r6
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0749__00r6 = _00r5_constant+1*v0681_n_var+1*v0726_lam_var

# op _00rF_exp_a_eval
# LANG: lam_var --> _00rG
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0764__00rG = _00rF_exp_a_eval_a**v0726_lam_var

# op _00s0_power_combination_eval
# LANG: B_lin_comb_sign_matrix, _00r_ --> _00s1
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0779__00s1 = (v0762_B_lin_comb_sign_matrix**1)*(v0780__00r_**1)
v0779__00s1 = (v0779__00s1*_00s0_coeff).reshape((1, 2, 3, 2, 11))

# op _00s2_linear_combination_eval
# LANG: n_var, lam_var --> _00s3
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0782__00s3 = _00s2_constant+1*v0681_n_var+1*v0726_lam_var

# op _0104_power_combination_eval
# LANG: _0101, _0103 --> _0105
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01752__0105 = (v01728__0101**1)*(v01760__0103**1)
v01752__0105 = (v01752__0105*_0104_coeff).reshape((1, 2, 3, 40, 11))

# op _010y_power_combination_eval
# LANG: _010v, _010x --> _010z
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01782__010z = (v01763__010v**1)*(v01783__010x**1)
v01782__010z = (v01782__010z*_010y_coeff).reshape((1, 2, 3, 40, 11))

# op _012O cross_product_eval
# LANG: _012c, _012f --> _012P
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01849__012P = np.cross(v01848__012f, v01830__012c, axisa = 0, axisb = 0, axisc = 0)

# op _014C_power_combination_eval
# LANG: _014A, _014B --> _014D
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01907__014D = (v01898__014A**1)*(v01904__014B**1)
v01907__014D = (v01907__014D*_014C_coeff).reshape((1, 1, 2))

# op _014U expand_array_eval
# LANG: origin --> _014V
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01914__014V = np.einsum('b,ac->abc', v01829_origin.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _014p_decompose_eval
# LANG: _014l --> _014q, _014z, _014G
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01892__014q = ((v01891__014l.flatten())[src_indices__014q__014p]).reshape((1, 1, 2))
v01893__014z = ((v01891__014l.flatten())[src_indices__014z__014p]).reshape((1, 1, 2))
v01894__014G = ((v01891__014l.flatten())[src_indices__014G__014p]).reshape((1, 1, 2))

# op _014v_power_combination_eval
# LANG: _014s, _014u --> _014w
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01900__014w = (v01897__014s**1)*(v01903__014u**1)
v01900__014w = (v01900__014w*_014v_coeff).reshape((1, 1, 2))

# op _00J5_power_combination_eval
# LANG: _00J4 --> _00J6
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01385__00J6 = (v01384__00J4**1)
v01385__00J6 = (v01385__00J6*_00J5_coeff).reshape((1, 40, 30))

# op _00q6_power_combination_eval
# LANG: _00q5, _00pE --> _00q7
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0688__00q7 = (v0682__00q5**1)*(v0691__00pE**1)
v0688__00q7 = (v0688__00q7*_00q6_coeff).reshape((1, 2, 3, 2, 11))

# op _00qA_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00pS --> _00qB
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0739__00qB = (v0709_coeff_sign_matrix_odd**1)*(v0740__00pS**1)
v0739__00qB = (v0739__00qB*_00qA_coeff).reshape((1, 2, 3, 2, 11))

# op _00qK_power_combination_eval
# LANG: A_lin_comb_sign_matrix, _00qJ --> _00qL
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0725__00qL = (v0724_A_lin_comb_sign_matrix**1)*(v0727__00qJ**1)
v0725__00qL = (v0725__00qL*_00qK_coeff).reshape((1, 2, 3, 2, 11))

# op _00qM_bessel_eval
# LANG: _00qr --> _00qN
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0729__00qN=_00qM_bessel_eval(_00qM_bessel_eval_order,v0720__00qr)

# op _00qW_linear_combination_eval
# LANG: n_var, lam_var --> _00qX
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0742__00qX = _00qW_constant+1*v0681_n_var+-1*v0726_lam_var

# op _00qY_bessel_eval
# LANG: _00qr --> _00qZ
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0744__00qZ=_00qY_bessel_eval(_00qY_bessel_eval_order,v0720__00qr)

# op _00qa_power_combination_eval
# LANG: _00pI, _00q9 --> _00qb
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0694__00qb = (v0693__00pI**1)*(v0703__00q9**1)
v0694__00qb = (v0694__00qb*_00qa_coeff).reshape((1, 2, 3, 2, 11))

# op _00qe_power_combination_eval
# LANG: _00pK, _00pM --> _00qf
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0733__00qf = (v0715__00pM**1)*(v0702__00pK**1)
v0733__00qf = (v0733__00qf*_00qe_coeff).reshape((1, 2, 3, 2, 11))

# op _00qs_power_combination_eval
# LANG: coeff_sign_matrix_even, _00pQ --> _00qt
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0706__00qt = (v0705_coeff_sign_matrix_even**1)*(v0707__00pQ**1)
v0706__00qt = (v0706__00qt*_00qs_coeff).reshape((1, 2, 3, 2, 11))

# op _00qu_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00pO --> _00qv
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0710__00qv = (v0709_coeff_sign_matrix_odd**1)*(v0711__00pO**1)
v0710__00qv = (v0710__00qv*_00qu_coeff).reshape((1, 2, 3, 2, 11))

# op _00qy_power_combination_eval
# LANG: coeff_sign_matrix_even, _00pU --> _00qz
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0736__00qz = (v0705_coeff_sign_matrix_even**1)*(v0737__00pU**1)
v0736__00qz = (v0736__00qz*_00qy_coeff).reshape((1, 2, 3, 2, 11))

# op _00r7_power_combination_eval
# LANG: _00r4, _00r6 --> _00r8
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0748__00r8 = (v0746__00r4**1)*(v0749__00r6**1)
v0748__00r8 = (v0748__00r8*_00r7_coeff).reshape((1, 2, 3, 2, 11))

# op _00r9_bessel_eval
# LANG: _00qr --> _00ra
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0751__00ra=_00r9_bessel_eval(_00r9_bessel_eval_order,v0720__00qr)

# op _00rH_power_combination_eval
# LANG: B_lin_comb_sign_matrix, _00rG --> _00rI
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0763__00rI = (v0762_B_lin_comb_sign_matrix**1)*(v0764__00rG**1)
v0763__00rI = (v0763__00rI*_00rH_coeff).reshape((1, 2, 3, 2, 11))

# op _00rJ_bessel_eval
# LANG: _00qr --> _00rK
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0766__00rK=_00rJ_bessel_eval(_00rJ_bessel_eval_order,v0720__00qr)

# op _00rT_linear_combination_eval
# LANG: n_var, lam_var --> _00rU
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0775__00rU = _00rT_constant+1*v0681_n_var+-1*v0726_lam_var

# op _00rV_bessel_eval
# LANG: _00qr --> _00rW
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0777__00rW=_00rV_bessel_eval(_00rV_bessel_eval_order,v0720__00qr)

# op _00rp_power_combination_eval
# LANG: coeff_sign_matrix_even, _00pO --> _00rq
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0756__00rq = (v0705_coeff_sign_matrix_even**1)*(v0711__00pO**1)
v0756__00rq = (v0756__00rq*_00rp_coeff).reshape((1, 2, 3, 2, 11))

# op _00rr_power_combination_eval
# LANG: _00pQ, coeff_sign_matrix_odd --> _00rs
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0758__00rs = (v0709_coeff_sign_matrix_odd**1)*(v0707__00pQ**1)
v0758__00rs = (v0758__00rs*_00rr_coeff).reshape((1, 2, 3, 2, 11))

# op _00rv_power_combination_eval
# LANG: coeff_sign_matrix_even, _00pS --> _00rw
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0771__00rw = (v0705_coeff_sign_matrix_even**1)*(v0740__00pS**1)
v0771__00rw = (v0771__00rw*_00rv_coeff).reshape((1, 2, 3, 2, 11))

# op _00rx_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00pU --> _00ry
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0773__00ry = (v0709_coeff_sign_matrix_odd**1)*(v0737__00pU**1)
v0773__00ry = (v0773__00ry*_00rx_coeff).reshape((1, 2, 3, 2, 11))

# op _00s4_power_combination_eval
# LANG: _00s1, _00s3 --> _00s5
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0781__00s5 = (v0779__00s1**1)*(v0782__00s3**1)
v0781__00s5 = (v0781__00s5*_00s4_coeff).reshape((1, 2, 3, 2, 11))

# op _00s6_bessel_eval
# LANG: _00qr --> _00s7
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0784__00s7=_00s6_bessel_eval(_00s6_bessel_eval_order,v0720__00qr)

# op _00v3 expand_scalar_eval
# LANG: Vx --> _00v4
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0861__00v4 = np.empty((1, 1))
v0861__00v4.fill(v030_u.item())

# op _00v6 expand_scalar_eval
# LANG: Vy --> _00v7
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0863__00v7 = np.empty((1, 1))
v0863__00v7.fill(v035_v.item())

# op _00v8 expand_scalar_eval
# LANG: Vz --> _00v9
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0864__00v9 = np.empty((1, 1))
v0864__00v9.fill(v039_w.item())

# op _010A_single_tensor_sum_with_axis_eval
# LANG: _0105 --> An
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01761_An = np.sum(v01752__0105, axis = (4,)).reshape((1, 2, 3, 40))

# op _010C_single_tensor_sum_with_axis_eval
# LANG: _010z --> Bn
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01784_Bn = np.sum(v01782__010z, axis = (4,)).reshape((1, 2, 3, 40))

# op _012C_sin_eval
# LANG: theta --> _012D
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0986_theta = v0986_theta.reshape((1, 1))
v01841__012D = np.sin(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _012G_sin_eval
# LANG: theta --> _012H
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0986_theta = v0986_theta.reshape((1, 1))
v01843__012H = np.sin(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _012K_cos_eval
# LANG: theta --> _012L
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0986_theta = v0986_theta.reshape((1, 1))
v01845__012L = np.cos(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _012Q pnorm_eval
# LANG: _012P --> _012R
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01851__012R = np.linalg.norm(v01849__012P.flatten(), ord=2)

# op _012g pnorm_eval
# LANG: _012c --> _012h
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01831__012h = np.linalg.norm(v01830__012c.flatten(), ord=2)

# op _012l pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _012m
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01833__012m = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _012t_linear_combination_eval
# LANG: theta --> _012u
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0986_theta = v0986_theta.reshape((1, 1))
v01836__012u = _012t_constant+1*v0986_theta
v0986_theta = v0986_theta.reshape((1,))

# op _012v_linear_combination_eval
# LANG: theta --> _012w
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0986_theta = v0986_theta.reshape((1, 1))
v01838__012w = _012v_constant+1*v0986_theta
v0986_theta = v0986_theta.reshape((1,))

# op _014E_linear_combination_eval
# LANG: _014z, _014D --> aircraft_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01906_aircraft_y_pos = _014E_constant+1*v01893__014z+1*v01907__014D

# op _014J_power_combination_eval
# LANG: _014H, _014I --> _014K
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01909__014K = (v01899__014H**1)*(v01905__014I**1)
v01909__014K = (v01909__014K*_014J_coeff).reshape((1, 1, 2))

# op _014W_decompose_eval
# LANG: _014V --> _014X, _0151, _0156
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01915__014X = ((v01914__014V.flatten())[src_indices__014X__014W]).reshape((1, 1, 2))
v01916__0151 = ((v01914__014V.flatten())[src_indices__0151__014W]).reshape((1, 1, 2))
v01917__0156 = ((v01914__014V.flatten())[src_indices__0156__014W]).reshape((1, 1, 2))

# op _014x_linear_combination_eval
# LANG: _014q, _014w --> aircraft_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01895_aircraft_x_pos = _014x_constant+1*v01892__014q+1*v01900__014w

# op _00Oo_single_tensor_sum_with_axis_eval
# LANG: _00J6 --> _00Op
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01386__00Op = np.sum(v01385__00J6, axis = (1, 2)).reshape((1,))

# op _00Oy_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00Oz
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01391__00Oz = np.sum(v01146__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00Un reshape_eval
# LANG: rel_obs_dist --> _00Uo
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01791__00Uo = v01541_rel_obs_dist.reshape((1, 2))

# op _00qC_linear_combination_eval
# LANG: _00qz, _00qB --> _00qD
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0738__00qD = _00qC_constant+1*v0736__00qz+1*v0739__00qB

# op _00qG_bessel_eval
# LANG: _00qr --> _00qH
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0722__00qH=_00qG_bessel_eval(_00qG_bessel_eval_order,v0720__00qr)

# op _00qO_power_combination_eval
# LANG: _00qL, _00qN --> _00qP
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0728__00qP = (v0725__00qL**1)*(v0729__00qN**1)
v0728__00qP = (v0728__00qP*_00qO_coeff).reshape((1, 2, 3, 2, 11))

# op _00q__power_combination_eval
# LANG: _00qX, _00qZ --> _00r0
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0743__00r0 = (v0742__00qX**1)*(v0744__00qZ**1)
v0743__00r0 = (v0743__00r0*_00q__coeff).reshape((1, 2, 3, 2, 11))

# op _00qc_power_combination_eval
# LANG: _00q7, _00qb --> _00qd
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0692__00qd = (v0688__00q7**1)*(v0694__00qb**-1)
v0692__00qd = (v0692__00qd*_00qc_coeff).reshape((1, 2, 3, 2, 11))

# op _00qg_power_combination_eval
# LANG: _00qf --> _00qh
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0734__00qh = (v0733__00qf**-1)
v0734__00qh = (v0734__00qh*_00qg_coeff).reshape((1, 2, 3, 2, 11))

# op _00qw_linear_combination_eval
# LANG: _00qt, _00qv --> _00qx
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0708__00qx = _00qw_constant+1*v0706__00qt+1*v0710__00qv

# op _00rD_bessel_eval
# LANG: _00qr --> _00rE
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0760__00rE=_00rD_bessel_eval(_00rD_bessel_eval_order,v0720__00qr)

# op _00rL_power_combination_eval
# LANG: _00rI, _00rK --> _00rM
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0765__00rM = (v0763__00rI**1)*(v0766__00rK**1)
v0765__00rM = (v0765__00rM*_00rL_coeff).reshape((1, 2, 3, 2, 11))

# op _00rX_power_combination_eval
# LANG: _00rU, _00rW --> _00rY
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0776__00rY = (v0775__00rU**1)*(v0777__00rW**1)
v0776__00rY = (v0776__00rY*_00rX_coeff).reshape((1, 2, 3, 2, 11))

# op _00rb_power_combination_eval
# LANG: _00r8, _00ra --> _00rc
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0750__00rc = (v0748__00r8**1)*(v0751__00ra**1)
v0750__00rc = (v0750__00rc*_00rb_coeff).reshape((1, 2, 3, 2, 11))

# op _00rt_linear_combination_eval
# LANG: _00rq, _00rs --> _00ru
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0757__00ru = _00rt_constant+1*v0756__00rq+1*v0758__00rs

# op _00rz_linear_combination_eval
# LANG: _00rw, _00ry --> _00rA
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0772__00rA = _00rz_constant+1*v0771__00rw+1*v0773__00ry

# op _00s8_power_combination_eval
# LANG: _00s5, _00s7 --> _00s9
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0783__00s9 = (v0781__00s5**1)*(v0784__00s7**1)
v0783__00s9 = (v0783__00s9*_00s8_coeff).reshape((1, 2, 3, 2, 11))

# op _00v5_indexed_passthrough_eval
# LANG: _00v4, _00v7, _00v9 --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0862_V_aircraft__temp[i_v0861__00v4__00v5_indexed_passthrough_eval] = v0861__00v4.flatten()
v0862_V_aircraft = v0862_V_aircraft__temp.copy()
v0862_V_aircraft__temp[i_v0863__00v7__00v5_indexed_passthrough_eval] = v0863__00v7.flatten()
v0862_V_aircraft = v0862_V_aircraft__temp.copy()
v0862_V_aircraft__temp[i_v0864__00v9__00v5_indexed_passthrough_eval] = v0864__00v9.flatten()
v0862_V_aircraft = v0862_V_aircraft__temp.copy()

# op _010I_decompose_eval
# LANG: n_var --> _010J
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01785__010J = ((v01742_n_var.flatten())[src_indices__010J__010I]).reshape((1, 2, 3, 1, 1))

# op _011F_decompose_eval
# LANG: An --> _011G, _011H
# SHAPES: (1, 2, 3, 40) --> (1, 2, 3, 39), (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01815__011G = ((v01761_An.flatten())[src_indices__011G__011F]).reshape((1, 2, 3, 39))
v01816__011H = ((v01761_An.flatten())[src_indices__011H__011F]).reshape((1, 2, 3, 39))

# op _011U_decompose_eval
# LANG: Bn --> _011V, _011W
# SHAPES: (1, 2, 3, 40) --> (1, 2, 3, 39), (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01822__011V = ((v01784_Bn.flatten())[src_indices__011V__011U]).reshape((1, 2, 3, 39))
v01823__011W = ((v01784_Bn.flatten())[src_indices__011W__011U]).reshape((1, 2, 3, 39))

# op _012A_cos_eval
# LANG: theta --> _012B
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0986_theta = v0986_theta.reshape((1, 1))
v01840__012B = np.cos(v0986_theta)
v0986_theta = v0986_theta.reshape((1,))

# op _012E_power_combination_eval
# LANG: _012D --> _012F
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01842__012F = (v01841__012D**1)
v01842__012F = (v01842__012F*_012E_coeff).reshape((1, 1))

# op _012I_power_combination_eval
# LANG: _012H --> _012J
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01844__012J = (v01843__012H**1)
v01844__012J = (v01844__012J*_012I_coeff).reshape((1, 1))

# op _012M_power_combination_eval
# LANG: _012L --> _012N
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01846__012N = (v01845__012L**1)
v01846__012N = (v01846__012N*_012M_coeff).reshape((1, 1))

# op _012S expand_scalar_eval
# LANG: _012R --> _012T
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01852__012T = np.empty((3,))
v01852__012T.fill(v01851__012R.item())

# op _012i_power_combination_eval
# LANG: _012h --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01832_propeller_radius = (v01831__012h**1)
v01832_propeller_radius = (v01832_propeller_radius*_012i_coeff).reshape((1,))

# op _012n reshape_eval
# LANG: _012m --> _012o
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01834__012o = v01833__012m.reshape((40, 1))

# op _012x_power_combination_eval
# LANG: _012u, _012w --> _012y
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01837__012y = (v01836__012u**1)*(v01838__012w**-1)
v01837__012y = (v01837__012y*_012x_coeff).reshape((1, 1))

# op _014L_linear_combination_eval
# LANG: _014G, _014K --> aircraft_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01908_aircraft_z_pos = _014L_constant+1*v01894__014G+1*v01909__014K

# op _014N expand_array_eval
# LANG: init_obs_x_loc --> _014O
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01911__014O = np.einsum('c,ab->abc', v01910_init_obs_x_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _014P expand_array_eval
# LANG: init_obs_y_loc --> _014Q
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01919__014Q = np.einsum('c,ab->abc', v01918_init_obs_y_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _014Y_linear_combination_eval
# LANG: aircraft_x_pos, _014X --> _014Z
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01913__014Z = _014Y_constant+1*v01895_aircraft_x_pos+1*v01915__014X

# op _0152_linear_combination_eval
# LANG: aircraft_y_pos, _0151 --> _0153
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01921__0153 = _0152_constant+1*v01906_aircraft_y_pos+1*v01916__0151

# op _00Nr_single_tensor_sum_with_axis_eval
# LANG: _local_thrust --> _00Ns
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01285__00Ns = np.sum(v01270__local_thrust, axis = (1, 2)).reshape((1,))

# op _00OA_power_combination_eval
# LANG: _00Oz --> _00OB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01392__00OB = (v01391__00Oz**1)
v01392__00OB = (v01392__00OB*_00OA_coeff).reshape((1,))

# op _00Oq_power_combination_eval
# LANG: _00Op --> _00Or
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01387__00Or = (v01386__00Op**1)
v01387__00Or = (v01387__00Or*_00Oq_coeff).reshape((1,))

# op _00qE_power_combination_eval
# LANG: _00qd, _00qx --> _00qF
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0704__00qF = (v0692__00qd**1)*(v0708__00qx**1)
v0704__00qF = (v0704__00qF*_00qE_coeff).reshape((1, 2, 3, 2, 11))

# op _00qQ_linear_combination_eval
# LANG: _00qH, _00qP --> _00qR
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0723__00qR = _00qQ_constant+1*v0722__00qH+1*v0728__00qP

# op _00qU_power_combination_eval
# LANG: _00qh, _00qD --> _00qV
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0735__00qV = (v0734__00qh**1)*(v0738__00qD**1)
v0735__00qV = (v0735__00qV*_00qU_coeff).reshape((1, 2, 3, 2, 11))

# op _00rB_power_combination_eval
# LANG: _00qd, _00ru --> _00rC
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0755__00rC = (v0692__00qd**1)*(v0757__00ru**1)
v0755__00rC = (v0755__00rC*_00rB_coeff).reshape((1, 2, 3, 2, 11))

# op _00rN_linear_combination_eval
# LANG: _00rE, _00rM --> _00rO
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0761__00rO = _00rN_constant+1*v0760__00rE+1*v0765__00rM

# op _00rR_power_combination_eval
# LANG: _00qh, _00rA --> _00rS
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0770__00rS = (v0734__00qh**1)*(v0772__00rA**1)
v0770__00rS = (v0770__00rS*_00rR_coeff).reshape((1, 2, 3, 2, 11))

# op _00rd_linear_combination_eval
# LANG: _00r0, _00rc --> _00re
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0745__00re = _00rd_constant+1*v0743__00r0+1*v0750__00rc

# op _00sa_linear_combination_eval
# LANG: _00rY, _00s9 --> _00sb
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0778__00sb = _00sa_constant+1*v0776__00rY+1*v0783__00s9

# op _00va expand_array_eval
# LANG: V_aircraft --> _00vb
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0871__00vb = np.einsum('ab,c->abc', v0862_V_aircraft.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _00vg expand_array_eval
# LANG: time_vectors --> _00vh
# SHAPES: (2,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0877__00vh = np.einsum('c,ab->abc', v0876_time_vectors.reshape((2,)) ,np.ones((1, 3))).reshape((1, 3, 2))

# op _010K reshape_eval
# LANG: _010J --> _010L
# SHAPES: (1, 2, 3, 1, 1) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01786__010L = v01785__010J.reshape((1, 2, 3))

# op _010O expand_array_eval
# LANG: _00Uo --> _010P
# SHAPES: (1, 2) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01792__010P = np.einsum('ab,c->abc', v01791__00Uo.reshape((1, 2)) ,np.ones((3,))).reshape((1, 2, 3))

# op _011I_linear_combination_eval
# LANG: _011G, _011H --> _011J
# SHAPES: (1, 2, 3, 39), (1, 2, 3, 39) --> (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01817__011J = _011I_constant+1*v01815__011G+1*v01816__011H

# op _011K expand_scalar_eval
# LANG: dr --> _011L
# SHAPES: (1,) --> (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01819__011L = np.empty((1, 2, 3, 39))
v01819__011L.fill(v01446_dr.item())

# op _011X_linear_combination_eval
# LANG: _011V, _011W --> _011Y
# SHAPES: (1, 2, 3, 39), (1, 2, 3, 39) --> (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01824__011Y = _011X_constant+1*v01822__011V+1*v01823__011W

# op _011Z expand_scalar_eval
# LANG: dr --> _011_
# SHAPES: (1,) --> (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01826__011_ = np.empty((1, 2, 3, 39))
v01826__011_.fill(v01446_dr.item())

# op _012U_power_combination_eval
# LANG: _012P, _012T --> _012V
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01850__012V = (v01849__012P**1)*(v01852__012T**-1)
v01850__012V = (v01850__012V*_012U_coeff).reshape((3,))

# op _012__power_combination_eval
# LANG: propeller_radius --> _0130
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01853__0130 = (v01832_propeller_radius**1)
v01853__0130 = (v01853__0130*_012__coeff).reshape((1,))

# op _012p_power_combination_eval
# LANG: _012o --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01835_chord_profile = (v01834__012o**1)
v01835_chord_profile = (v01835_chord_profile*_012p_coeff).reshape((40, 1))

# op _012z_indexed_passthrough_eval
# LANG: _012y, _012B, _012F, _012J, _012N --> rot_mat
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01839_rot_mat__temp[i_v01837__012y__012z_indexed_passthrough_eval] = v01837__012y.flatten()
v01839_rot_mat = v01839_rot_mat__temp.copy()
v01839_rot_mat__temp[i_v01840__012B__012z_indexed_passthrough_eval] = v01840__012B.flatten()
v01839_rot_mat = v01839_rot_mat__temp.copy()
v01839_rot_mat__temp[i_v01842__012F__012z_indexed_passthrough_eval] = v01842__012F.flatten()
v01839_rot_mat = v01839_rot_mat__temp.copy()
v01839_rot_mat__temp[i_v01844__012J__012z_indexed_passthrough_eval] = v01844__012J.flatten()
v01839_rot_mat = v01839_rot_mat__temp.copy()
v01839_rot_mat__temp[i_v01846__012N__012z_indexed_passthrough_eval] = v01846__012N.flatten()
v01839_rot_mat = v01839_rot_mat__temp.copy()

# op _014R expand_array_eval
# LANG: init_obs_z_loc --> _014S
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01923__014S = np.einsum('c,ab->abc', v01922_init_obs_z_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _014__linear_combination_eval
# LANG: _014O, _014Z --> rel_obs_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01912_rel_obs_x_pos = _014__constant+1*v01911__014O+-1*v01913__014Z

# op _0154_linear_combination_eval
# LANG: _014Q, _0153 --> rel_obs_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01920_rel_obs_y_pos = _0154_constant+1*v01919__014Q+-1*v01921__0153

# op _0157_linear_combination_eval
# LANG: aircraft_z_pos, _0156 --> _0158
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01925__0158 = _0157_constant+1*v01908_aircraft_z_pos+1*v01917__0156

# op _00Nt_power_combination_eval
# LANG: _00Ns --> T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01286_T = (v01285__00Ns**1)
v01286_T = (v01286_T*_00Nt_coeff).reshape((1,))

# op _00OC_power_combination_eval
# LANG: _00OB --> _00OD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01393__00OD = (v01392__00OB**1)
v01393__00OD = (v01393__00OD*_00OC_coeff).reshape((1,))

# op _00Os_power_combination_eval
# LANG: _00Or --> _00Ot
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01388__00Ot = (v01387__00Or**1)
v01388__00Ot = (v01388__00Ot*_00Os_coeff).reshape((1,))

# op _00QJ_power_combination_eval
# LANG: rpm --> _00QK
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01448__00QK = (v01106_rpm**1)
v01448__00QK = (v01448__00QK*_00QJ_coeff).reshape((1, 1))

# op _00qS_power_combination_eval
# LANG: _00qF, _00qR --> _00qT
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0712__00qT = (v0704__00qF**1)*(v0723__00qR**1)
v0712__00qT = (v0712__00qT*_00qS_coeff).reshape((1, 2, 3, 2, 11))

# op _00rP_power_combination_eval
# LANG: _00rC, _00rO --> _00rQ
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0759__00rQ = (v0755__00rC**1)*(v0761__00rO**1)
v0759__00rQ = (v0759__00rQ*_00rP_coeff).reshape((1, 2, 3, 2, 11))

# op _00rf_power_combination_eval
# LANG: _00qV, _00re --> _00rg
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0741__00rg = (v0735__00qV**1)*(v0745__00re**1)
v0741__00rg = (v0741__00rg*_00rf_coeff).reshape((1, 2, 3, 2, 11))

# op _00sc_power_combination_eval
# LANG: _00rS, _00sb --> _00sd
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0774__00sd = (v0770__00rS**1)*(v0778__00sb**1)
v0774__00sd = (v0774__00sd*_00sc_coeff).reshape((1, 2, 3, 2, 11))

# op _00t1_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00t2
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v0805__00t2 = (v08_rotor_disk_in_plane_1**1)
v0805__00t2 = (v0805__00t2*_00t1_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _00t4_power_combination_eval
# LANG: rotor_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v0804_origin = (v012_rotor_disk_origin**1)
v0804_origin = (v0804_origin*_00t4_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _00t7_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _00t8
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v0823__00t8 = (v010_rotor_disk_in_plane_2**1)
v0823__00t8 = (v0823__00t8*_00t7_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _00vd expand_array_eval
# LANG: aircraft_location --> _00ve
# SHAPES: (3, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0866__00ve = np.einsum('bc,a->abc', v0865_aircraft_location.reshape((3, 2)) ,np.ones((1,))).reshape((1, 3, 2))

# op _00vk_decompose_eval
# LANG: _00vb --> _00vl, _00vt, _00vA
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0872__00vl = ((v0871__00vb.flatten())[src_indices__00vl__00vk]).reshape((1, 1, 2))
v0873__00vt = ((v0871__00vb.flatten())[src_indices__00vt__00vk]).reshape((1, 1, 2))
v0874__00vA = ((v0871__00vb.flatten())[src_indices__00vA__00vk]).reshape((1, 1, 2))

# op _00vm_decompose_eval
# LANG: _00vh --> _00vn, _00vu, _00vB
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0878__00vn = ((v0877__00vh.flatten())[src_indices__00vn__00vm]).reshape((1, 1, 2))
v0879__00vu = ((v0877__00vh.flatten())[src_indices__00vu__00vm]).reshape((1, 1, 2))
v0880__00vB = ((v0877__00vh.flatten())[src_indices__00vB__00vm]).reshape((1, 1, 2))

# op _010M expand_scalar_eval
# LANG: _00Uw --> _010N
# SHAPES: (1,) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01789__010N = np.empty((1, 2, 3))
v01789__010N.fill(v01579__00Uw.item())

# op _010Q expand_scalar_eval
# LANG: speed_of_sound --> _010R
# SHAPES: (1,) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01795__010R = np.empty((1, 2, 3))
v01795__010R.fill(v01494_speed_of_sound.item())

# op _010S_power_combination_eval
# LANG: _010L --> _010T
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01787__010T = (v01786__010L**1)
v01787__010T = (v01787__010T*_010S_coeff).reshape((1, 2, 3))

# op _010W_power_combination_eval
# LANG: _010P --> _010X
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01793__010X = (v01792__010P**1)
v01793__010X = (v01793__010X*_010W_coeff).reshape((1, 2, 3))

# op _0113_power_combination_eval
# LANG: _010L --> _0114
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01799__0114 = (v01786__010L**1)
v01799__0114 = (v01799__0114*_0113_coeff).reshape((1, 2, 3))

# op _0117_power_combination_eval
# LANG: _010P --> _0118
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01802__0118 = (v01792__010P**1)
v01802__0118 = (v01802__0118*_0117_coeff).reshape((1, 2, 3))

# op _011M_power_combination_eval
# LANG: _011J, _011L --> _011N
# SHAPES: (1, 2, 3, 39), (1, 2, 3, 39) --> (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01818__011N = (v01817__011J**1)*(v01819__011L**1)
v01818__011N = (v01818__011N*_011M_coeff).reshape((1, 2, 3, 39))

# op _0120_power_combination_eval
# LANG: _011Y, _011_ --> _0121
# SHAPES: (1, 2, 3, 39), (1, 2, 3, 39) --> (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01825__0121 = (v01824__011Y**1)*(v01826__011_**1)
v01825__0121 = (v01825__0121*_0120_coeff).reshape((1, 2, 3, 39))

# op _012W_matvec_eval
# LANG: rot_mat, _012V --> thrust_dir
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01847_thrust_dir = v01839_rot_mat@v01850__012V

# op _0131_power_combination_eval
# LANG: _0130 --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01854_dr = (v01853__0130**1)
v01854_dr = (v01854_dr*_0131_coeff).reshape((1,))

# op _0135_power_combination_eval
# LANG: rpm --> _0136
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01856__0136 = (v01106_rpm**1)
v01856__0136 = (v01856__0136*_0135_coeff).reshape((1, 1))

# op _0159_linear_combination_eval
# LANG: _014S, _0158 --> rel_obs_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01924_rel_obs_z_pos = _0159_constant+1*v01923__014S+-1*v01925__0158

# op _015d_power_combination_eval
# LANG: rel_obs_x_pos --> _015e
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01927__015e = (v01912_rel_obs_x_pos**2)
v01927__015e = (v01927__015e*_015d_coeff).reshape((1, 1, 2))

# op _015f_power_combination_eval
# LANG: rel_obs_y_pos --> _015g
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01929__015g = (v01920_rel_obs_y_pos**2)
v01929__015g = (v01929__015g*_015f_coeff).reshape((1, 1, 2))

# op _0165_power_combination_eval
# LANG: rpm --> _0166
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01106_rpm = v01106_rpm.reshape((1,))
v01959__0166 = (v01106_rpm**1)
v01959__0166 = (v01959__0166*_0165_coeff).reshape((1,))
v01106_rpm = v01106_rpm.reshape((1, 1))

# op _016m single_tensor_sum_no_axis_eval
# LANG: chord_profile --> _016n
# SHAPES: (40, 1) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01951__016n = np.sum(v01835_chord_profile).reshape((1,))

# op _00OE_power_combination_eval
# LANG: _00OD --> _00OF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01394__00OF = (v01393__00OD**1)
v01394__00OF = (v01394__00OF*_00OE_coeff).reshape((1,))

# op _00Om_power_combination_eval
# LANG: T, density --> _00On
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01187_density = v01187_density.reshape((1,))
v01382__00On = (v01286_T**1)*(v01187_density**-1)
v01382__00On = (v01382__00On*_00Om_coeff).reshape((1,))
v01187_density = v01187_density.reshape((1, 1))

# op _00Ou_power_combination_eval
# LANG: _00Ot --> _00Ov
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01389__00Ov = (v01388__00Ot**2)
v01389__00Ov = (v01389__00Ov*_00Ou_coeff).reshape((1,))

# op _00QL_power_combination_eval
# LANG: _00QK --> _00QM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01449__00QM = (v01448__00QK**1)
v01449__00QM = (v01449__00QM*_00QL_coeff).reshape((1, 1))

# op _00rh_power_combination_eval
# LANG: term_1_coeff_A, _00qT --> _00ri
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0680__00ri = (v0679_term_1_coeff_A**1)*(v0712__00qT**1)
v0680__00ri = (v0680__00ri*_00rh_coeff).reshape((1, 2, 3, 2, 11))

# op _00rj_power_combination_eval
# LANG: term_2_coeff_A, _00rg --> _00rk
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0732__00rk = (v0731_term_2_coeff_A**1)*(v0741__00rg**1)
v0732__00rk = (v0732__00rk*_00rj_coeff).reshape((1, 2, 3, 2, 11))

# op _00se_power_combination_eval
# LANG: term_1_coeff_B, _00rQ --> _00sf
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0754__00sf = (v0753_term_1_coeff_B**1)*(v0759__00rQ**1)
v0754__00sf = (v0754__00sf*_00se_coeff).reshape((1, 2, 3, 2, 11))

# op _00sg_power_combination_eval
# LANG: term_2_coeff_B, _00sd --> _00sh
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0769__00sh = (v0768_term_2_coeff_B**1)*(v0774__00sd**1)
v0769__00sh = (v0769__00sh*_00sg_coeff).reshape((1, 2, 3, 2, 11))

# op _00t9 pnorm_eval
# LANG: _00t2 --> _00ta
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0806__00ta = np.linalg.norm(v0805__00t2.flatten(), ord=2)

# op _00tH cross_product_eval
# LANG: _00t2, _00t8 --> _00tI
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0824__00tI = np.cross(v0823__00t8, v0805__00t2, axisa = 0, axisb = 0, axisc = 0)

# op _00vN expand_array_eval
# LANG: origin --> _00vO
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0889__00vO = np.einsum('b,ac->abc', v0804_origin.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00vi_decompose_eval
# LANG: _00ve --> _00vj, _00vs, _00vz
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0867__00vj = ((v0866__00ve.flatten())[src_indices__00vj__00vi]).reshape((1, 1, 2))
v0868__00vs = ((v0866__00ve.flatten())[src_indices__00vs__00vi]).reshape((1, 1, 2))
v0869__00vz = ((v0866__00ve.flatten())[src_indices__00vz__00vi]).reshape((1, 1, 2))

# op _00vo_power_combination_eval
# LANG: _00vl, _00vn --> _00vp
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0875__00vp = (v0872__00vl**1)*(v0878__00vn**1)
v0875__00vp = (v0875__00vp*_00vo_coeff).reshape((1, 1, 2))

# op _00vv_power_combination_eval
# LANG: _00vt, _00vu --> _00vw
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0882__00vw = (v0873__00vt**1)*(v0879__00vu**1)
v0882__00vw = (v0882__00vw*_00vv_coeff).reshape((1, 1, 2))

# op _010U_power_combination_eval
# LANG: _010T, _010N --> _010V
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01788__010V = (v01787__010T**1)*(v01789__010N**1)
v01788__010V = (v01788__010V*_010U_coeff).reshape((1, 2, 3))

# op _010Y_power_combination_eval
# LANG: _010X, _010R --> _010Z
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01794__010Z = (v01793__010X**1)*(v01795__010R**1)
v01794__010Z = (v01794__010Z*_010Y_coeff).reshape((1, 2, 3))

# op _0115_power_combination_eval
# LANG: _010N, _0114 --> _0116
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01800__0116 = (v01799__0114**1)*(v01789__010N**1)
v01800__0116 = (v01800__0116*_0115_coeff).reshape((1, 2, 3))

# op _0119_power_combination_eval
# LANG: _010R, _0118 --> _011a
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01803__011a = (v01802__0118**1)*(v01795__010R**1)
v01803__011a = (v01803__011a*_0119_coeff).reshape((1, 2, 3))

# op _011O_power_combination_eval
# LANG: _011N --> _011P
# SHAPES: (1, 2, 3, 39) --> (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01820__011P = (v01818__011N**1)
v01820__011P = (v01820__011P*_011O_coeff).reshape((1, 2, 3, 39))

# op _0122_power_combination_eval
# LANG: _0121 --> _0123
# SHAPES: (1, 2, 3, 39) --> (1, 2, 3, 39)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01827__0123 = (v01825__0121**1)
v01827__0123 = (v01827__0123*_0122_coeff).reshape((1, 2, 3, 39))

# op _0137_power_combination_eval
# LANG: _0136 --> _0138
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01857__0138 = (v01856__0136**1)
v01857__0138 = (v01857__0138*_0137_coeff).reshape((1, 1))

# op _015c_indexed_passthrough_eval
# LANG: rel_obs_x_pos, rel_obs_y_pos, rel_obs_z_pos --> rel_obs_position
# SHAPES: (1, 1, 2), (1, 1, 2), (1, 1, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01926_rel_obs_position__temp[i_v01912_rel_obs_x_pos__015c_indexed_passthrough_eval] = v01912_rel_obs_x_pos.flatten()
v01926_rel_obs_position = v01926_rel_obs_position__temp.copy()
v01926_rel_obs_position__temp[i_v01920_rel_obs_y_pos__015c_indexed_passthrough_eval] = v01920_rel_obs_y_pos.flatten()
v01926_rel_obs_position = v01926_rel_obs_position__temp.copy()
v01926_rel_obs_position__temp[i_v01924_rel_obs_z_pos__015c_indexed_passthrough_eval] = v01924_rel_obs_z_pos.flatten()
v01926_rel_obs_position = v01926_rel_obs_position__temp.copy()

# op _015h_linear_combination_eval
# LANG: _015e, _015g --> _015i
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01928__015i = _015h_constant+1*v01927__015e+1*v01929__015g

# op _015j_power_combination_eval
# LANG: rel_obs_z_pos --> _015k
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01931__015k = (v01924_rel_obs_z_pos**2)
v01931__015k = (v01931__015k*_015j_coeff).reshape((1, 1, 2))

# op _015q expand_array_eval
# LANG: thrust_dir --> _015r
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01934__015r = np.einsum('b,ac->abc', v01847_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _0167_power_combination_eval
# LANG: _0166 --> _0168
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01960__0168 = (v01959__0166**1)
v01960__0168 = (v01960__0168*_0167_coeff).reshape((1,))

# op _016o_power_combination_eval
# LANG: _016n, dr --> _016p
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01952__016p = (v01951__016n**1)*(v01854_dr**1)
v01952__016p = (v01952__016p*_016o_coeff).reshape((1,))

# op _016u expand_scalar_eval
# LANG: propeller_radius --> _016v
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01956__016v = np.empty((1, 2))
v01956__016v.fill(v01832_propeller_radius.item())

# op _00OG_power_combination_eval
# LANG: _00OF --> _00OH
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01395__00OH = (v01394__00OF**4)
v01395__00OH = (v01395__00OH*_00OG_coeff).reshape((1,))

# op _00Ow_power_combination_eval
# LANG: _00On, _00Ov --> _00Ox
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01383__00Ox = (v01382__00On**1)*(v01389__00Ov**-1)
v01383__00Ox = (v01383__00Ox*_00Ow_coeff).reshape((1,))

# op _00QN_power_combination_eval
# LANG: _00QM --> _00QO
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01450__00QO = (v01449__00QM**1)
v01450__00QO = (v01450__00QO*_00QN_coeff).reshape((1, 1))

# op _00rl_linear_combination_eval
# LANG: _00ri, _00rk --> _00rm
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0730__00rm = _00rl_constant+1*v0680__00ri+1*v0732__00rk

# op _00si_linear_combination_eval
# LANG: _00sf, _00sh --> _00sj
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0767__00sj = _00si_constant+1*v0754__00sf+1*v0769__00sh

# op _00tD_cos_eval
# LANG: theta --> _00tE
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0820__00tE = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00tJ pnorm_eval
# LANG: _00tI --> _00tK
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0826__00tK = np.linalg.norm(v0824__00tI.flatten(), ord=2)

# op _00tb_power_combination_eval
# LANG: _00ta --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0807_propeller_radius = (v0806__00ta**1)
v0807_propeller_radius = (v0807_propeller_radius*_00tb_coeff).reshape((1,))

# op _00tm_linear_combination_eval
# LANG: theta --> _00tn
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0811__00tn = _00tm_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _00to_linear_combination_eval
# LANG: theta --> _00tp
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0813__00tp = _00to_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _00tv_sin_eval
# LANG: theta --> _00tw
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0816__00tw = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00tz_sin_eval
# LANG: theta --> _00tA
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0818__00tA = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00vC_power_combination_eval
# LANG: _00vA, _00vB --> _00vD
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0884__00vD = (v0874__00vA**1)*(v0880__00vB**1)
v0884__00vD = (v0884__00vD*_00vC_coeff).reshape((1, 1, 2))

# op _00vP_decompose_eval
# LANG: _00vO --> _00vQ, _00vV, _00v_
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0890__00vQ = ((v0889__00vO.flatten())[src_indices__00vQ__00vP]).reshape((1, 1, 2))
v0891__00vV = ((v0889__00vO.flatten())[src_indices__00vV__00vP]).reshape((1, 1, 2))
v0892__00v_ = ((v0889__00vO.flatten())[src_indices__00v___00vP]).reshape((1, 1, 2))

# op _00vq_linear_combination_eval
# LANG: _00vj, _00vp --> aircraft_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0870_aircraft_x_pos = _00vq_constant+1*v0867__00vj+1*v0875__00vp

# op _00vx_linear_combination_eval
# LANG: _00vs, _00vw --> aircraft_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0881_aircraft_y_pos = _00vx_constant+1*v0868__00vs+1*v0882__00vw

# op _010__power_combination_eval
# LANG: _010V, _010Z --> _0110
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01790__0110 = (v01788__010V**1)*(v01794__010Z**-1)
v01790__0110 = (v01790__0110*_010__coeff).reshape((1, 2, 3))

# op _011Q_single_tensor_sum_with_axis_eval
# LANG: _011P --> C_real_integrand
# SHAPES: (1, 2, 3, 39) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01821_C_real_integrand = np.sum(v01820__011P, axis = (3,)).reshape((1, 2, 3))

# op _011b_power_combination_eval
# LANG: _0116, _011a --> _011c
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01801__011c = (v01800__0116**1)*(v01803__011a**-1)
v01801__011c = (v01801__011c*_011b_coeff).reshape((1, 2, 3))

# op _0124_single_tensor_sum_with_axis_eval
# LANG: _0123 --> C_imag_integrand
# SHAPES: (1, 2, 3, 39) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01828_C_imag_integrand = np.sum(v01827__0123, axis = (3,)).reshape((1, 2, 3))

# op _0139_power_combination_eval
# LANG: _0138 --> _013a
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01858__013a = (v01857__0138**1)
v01858__013a = (v01858__013a*_0139_coeff).reshape((1, 1))

# op _015l_linear_combination_eval
# LANG: _015i, _015k --> _015m
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01930__015m = _015l_constant+1*v01928__015i+1*v01931__015k

# op _015s_tensor_dot_product_eval
# LANG: rel_obs_position, _015r --> normal_proj
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01933_normal_proj = np.sum(v01926_rel_obs_position * v01934__015r, axis=1)

# op _0169_power_combination_eval
# LANG: _0168 --> _016a
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01961__016a = (v01960__0168**1)
v01961__016a = (v01961__016a*_0169_coeff).reshape((1,))

# op _016b expand_scalar_eval
# LANG: propeller_radius --> _016c
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01963__016c = np.empty((1,))
v01963__016c.fill(v01832_propeller_radius.item())

# op _016q expand_scalar_eval
# LANG: _016p --> _016r
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01953__016r = np.empty((1, 2))
v01953__016r.fill(v01952__016p.item())

# op _016w_power_combination_eval
# LANG: _016v --> _016x
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01957__016x = (v01956__016v**2)
v01957__016x = (v01957__016x*_016w_coeff).reshape((1, 2))

# op _00OI_power_combination_eval
# LANG: _00Ox, _00OH --> C_T
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01390_C_T = (v01383__00Ox**1)*(v01395__00OH**-1)
v01390_C_T = (v01390_C_T*_00OI_coeff).reshape((1,))

# op _00QY_power_combination_eval
# LANG: _00QO --> _00QZ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01457__00QZ = (v01450__00QO**2)
v01457__00QZ = (v01457__00QZ*_00QY_coeff).reshape((1, 1))

# op _00R1_power_combination_eval
# LANG: _00QO --> _00R2
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01460__00R2 = (v01450__00QO**2)
v01460__00R2 = (v01460__00R2*_00R1_coeff).reshape((1, 1))

# op _00bo_power_combination_eval
# LANG: _angular_speed --> _00bp
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0442__00bp = (v0216__angular_speed**1)
v0442__00bp = (v0442__00bp*_00bo_coeff).reshape((1, 40, 100))

# op _00rn_power_combination_eval
# LANG: _00rm --> An
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0752_An = (v0730__00rm**1)
v0752_An = (v0752_An*_00rn_coeff).reshape((1, 2, 3, 2, 11))

# op _00sk_power_combination_eval
# LANG: _00sj --> Bn
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0785_Bn = (v0767__00sj**1)
v0785_Bn = (v0785_Bn*_00sk_coeff).reshape((1, 2, 3, 2, 11))

# op _00tB_power_combination_eval
# LANG: _00tA --> _00tC
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0819__00tC = (v0818__00tA**1)
v0819__00tC = (v0819__00tC*_00tB_coeff).reshape((1, 1))

# op _00tF_power_combination_eval
# LANG: _00tE --> _00tG
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0821__00tG = (v0820__00tE**1)
v0821__00tG = (v0821__00tG*_00tF_coeff).reshape((1, 1))

# op _00tL expand_scalar_eval
# LANG: _00tK --> _00tM
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0827__00tM = np.empty((3,))
v0827__00tM.fill(v0826__00tK.item())

# op _00tS_power_combination_eval
# LANG: propeller_radius --> _00tT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0828__00tT = (v0807_propeller_radius**1)
v0828__00tT = (v0828__00tT*_00tS_coeff).reshape((1,))

# op _00te pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00tf
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0808__00tf = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00tq_power_combination_eval
# LANG: _00tn, _00tp --> _00tr
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0812__00tr = (v0811__00tn**1)*(v0813__00tp**-1)
v0812__00tr = (v0812__00tr*_00tq_coeff).reshape((1, 1))

# op _00tt_cos_eval
# LANG: theta --> _00tu
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0815__00tu = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00tx_power_combination_eval
# LANG: _00tw --> _00ty
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0817__00ty = (v0816__00tw**1)
v0817__00ty = (v0817__00ty*_00tx_coeff).reshape((1, 1))

# op _00vE_linear_combination_eval
# LANG: _00vz, _00vD --> aircraft_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0883_aircraft_z_pos = _00vE_constant+1*v0869__00vz+1*v0884__00vD

# op _00vG expand_array_eval
# LANG: init_obs_x_loc --> _00vH
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0886__00vH = np.einsum('c,ab->abc', v0885_init_obs_x_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00vI expand_array_eval
# LANG: init_obs_y_loc --> _00vJ
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0894__00vJ = np.einsum('c,ab->abc', v0893_init_obs_y_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00vR_linear_combination_eval
# LANG: aircraft_x_pos, _00vQ --> _00vS
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0888__00vS = _00vR_constant+1*v0870_aircraft_x_pos+1*v0890__00vQ

# op _00vW_linear_combination_eval
# LANG: aircraft_y_pos, _00vV --> _00vX
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0896__00vX = _00vW_constant+1*v0881_aircraft_y_pos+1*v0891__00vV

# op _0111_power_combination_eval
# LANG: _0110, C_real_integrand --> _0112
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01796__0112 = (v01790__0110**1)*(v01821_C_real_integrand**1)
v01796__0112 = (v01796__0112*_0111_coeff).reshape((1, 2, 3))

# op _011d_power_combination_eval
# LANG: _011c, C_imag_integrand --> _011e
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01804__011e = (v01801__011c**1)*(v01828_C_imag_integrand**1)
v01804__011e = (v01804__011e*_011d_coeff).reshape((1, 2, 3))

# op _013k_power_combination_eval
# LANG: _013a --> _013l
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01865__013l = (v01858__013a**2)
v01865__013l = (v01865__013l*_013k_coeff).reshape((1, 1))

# op _013o_power_combination_eval
# LANG: _013a --> _013p
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01868__013p = (v01858__013a**2)
v01868__013p = (v01868__013p*_013o_coeff).reshape((1, 1))

# op _015n_power_combination_eval
# LANG: _015m --> rel_obs_dist
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01932_rel_obs_dist = (v01930__015m**0.5)
v01932_rel_obs_dist = (v01932_rel_obs_dist*_015n_coeff).reshape((1, 1, 2))

# op _015y expand_array_eval
# LANG: normal_proj --> _015z
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01935__015z = np.einsum('ac,b->abc', v01933_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _016d_power_combination_eval
# LANG: _016a, _016c --> _016e
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01962__016e = (v01961__016a**1)*(v01963__016c**1)
v01962__016e = (v01962__016e*_016d_coeff).reshape((1,))

# op _016s_power_combination_eval
# LANG: _016r --> Ab
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01954_Ab = (v01953__016r**1)
v01954_Ab = (v01954_Ab*_016s_coeff).reshape((1, 2))

# op _016y_power_combination_eval
# LANG: _016x --> _016z
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01958__016z = (v01957__016x**1)
v01958__016z = (v01958__016z*_016y_coeff).reshape((1, 2))

# op _00Q__linear_combination_eval
# LANG: _00QZ --> _00R0
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01458__00R0 = _00Q__constant+1*v01457__00QZ

# op _00R3_linear_combination_eval
# LANG: _00R2 --> _00R4
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01461__00R4 = _00R3_constant+1*v01460__00R2

# op _00bq_power_combination_eval
# LANG: _00bp --> _00br
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0443__00br = (v0442__00bp**1)
v0443__00br = (v0443__00br*_00bq_coeff).reshape((1, 40, 100))

# op _00sm_single_tensor_sum_with_axis_eval
# LANG: An --> _00sn
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0786__00sn = np.sum(v0752_An, axis = (4,)).reshape((1, 2, 3, 2))

# op _00so_single_tensor_sum_with_axis_eval
# LANG: Bn --> _00sp
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0789__00sp = np.sum(v0785_Bn, axis = (4,)).reshape((1, 2, 3, 2))

# op _00tN_power_combination_eval
# LANG: _00tI, _00tM --> _00tO
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0825__00tO = (v0824__00tI**1)*(v0827__00tM**-1)
v0825__00tO = (v0825__00tO*_00tN_coeff).reshape((3,))

# op _00tU_power_combination_eval
# LANG: _00tT --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0829_dr = (v0828__00tT**1)
v0829_dr = (v0829_dr*_00tU_coeff).reshape((1,))

# op _00tg reshape_eval
# LANG: _00tf --> _00th
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0809__00th = v0808__00tf.reshape((40, 1))

# op _00ts_indexed_passthrough_eval
# LANG: _00tr, _00tu, _00ty, _00tC, _00tG --> rot_mat
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0814_rot_mat__temp[i_v0812__00tr__00ts_indexed_passthrough_eval] = v0812__00tr.flatten()
v0814_rot_mat = v0814_rot_mat__temp.copy()
v0814_rot_mat__temp[i_v0815__00tu__00ts_indexed_passthrough_eval] = v0815__00tu.flatten()
v0814_rot_mat = v0814_rot_mat__temp.copy()
v0814_rot_mat__temp[i_v0817__00ty__00ts_indexed_passthrough_eval] = v0817__00ty.flatten()
v0814_rot_mat = v0814_rot_mat__temp.copy()
v0814_rot_mat__temp[i_v0819__00tC__00ts_indexed_passthrough_eval] = v0819__00tC.flatten()
v0814_rot_mat = v0814_rot_mat__temp.copy()
v0814_rot_mat__temp[i_v0821__00tG__00ts_indexed_passthrough_eval] = v0821__00tG.flatten()
v0814_rot_mat = v0814_rot_mat__temp.copy()

# op _00vK expand_array_eval
# LANG: init_obs_z_loc --> _00vL
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0898__00vL = np.einsum('c,ab->abc', v0897_init_obs_z_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00vT_linear_combination_eval
# LANG: _00vH, _00vS --> rel_obs_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0887_rel_obs_x_pos = _00vT_constant+1*v0886__00vH+-1*v0888__00vS

# op _00vY_linear_combination_eval
# LANG: _00vJ, _00vX --> rel_obs_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0895_rel_obs_y_pos = _00vY_constant+1*v0894__00vJ+-1*v0896__00vX

# op _00w0_linear_combination_eval
# LANG: aircraft_z_pos, _00v_ --> _00w1
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0900__00w1 = _00w0_constant+1*v0883_aircraft_z_pos+1*v0892__00v_

# op _00wY reshape_eval
# LANG: rpm --> _00wZ
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0931__00wZ = v0164_rpm.reshape((1,))

# op _011f_power_combination_eval
# LANG: _0112 --> _011g
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01797__011g = (v01796__0112**2)
v01797__011g = (v01797__011g*_011f_coeff).reshape((1, 2, 3))

# op _011h_power_combination_eval
# LANG: _011e --> _011i
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01805__011i = (v01804__011e**2)
v01805__011i = (v01805__011i*_011h_coeff).reshape((1, 2, 3))

# op _013m_linear_combination_eval
# LANG: _013l --> _013n
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01866__013n = _013m_constant+1*v01865__013l

# op _013q_linear_combination_eval
# LANG: _013p --> _013r
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01869__013r = _013q_constant+1*v01868__013p

# op _015A_power_combination_eval
# LANG: rel_obs_dist, _015z --> _015B
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01936__015B = (v01935__015z**1)*(v01932_rel_obs_dist**-1)
v01936__015B = (v01936__015B*_015A_coeff).reshape((1, 1, 2))

# op _016A_power_combination_eval
# LANG: Ab, _016z --> sigma
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01955_sigma = (v01954_Ab**1)*(v01958__016z**-1)
v01955_sigma = (v01955_sigma*_016A_coeff).reshape((1, 2))

# op _016f expand_scalar_eval
# LANG: _016e --> _016g
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01964__016g = np.empty((1, 2))
v01964__016g.fill(v01962__016e.item())

# op _016i expand_scalar_eval
# LANG: CT --> _016j
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01969__016j = np.empty((1, 2))
v01969__016j.fill(v01390_C_T.item())

# op _00QU_power_combination_eval
# LANG: _00QO --> _00QV
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01454__00QV = (v01450__00QO**2)
v01454__00QV = (v01454__00QV*_00QU_coeff).reshape((1, 1))

# op _00R5_power_combination_eval
# LANG: _00R0, _00R4 --> _00R6
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01459__00R6 = (v01458__00R0**1)*(v01461__00R4**1)
v01459__00R6 = (v01459__00R6*_00R5_coeff).reshape((1, 1))

# op _00gJ_single_tensor_sum_with_axis_eval
# LANG: _00br --> _00gK
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0444__00gK = np.sum(v0443__00br, axis = (1, 2)).reshape((1,))

# op _00gT_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00gU
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0449__00gU = np.sum(v0204__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00sq_power_combination_eval
# LANG: _00sn --> _00sr
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0787__00sr = (v0786__00sn**2)
v0787__00sr = (v0787__00sr*_00sq_coeff).reshape((1, 2, 3, 2))

# op _00ss_power_combination_eval
# LANG: _00sp --> _00st
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0790__00st = (v0789__00sp**2)
v0790__00st = (v0790__00st*_00ss_coeff).reshape((1, 2, 3, 2))

# op _00tP_matvec_eval
# LANG: rot_mat, _00tO --> thrust_dir
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0822_thrust_dir = v0814_rot_mat@v0825__00tO

# op _00ti_power_combination_eval
# LANG: _00th --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0810_chord_profile = (v0809__00th**1)
v0810_chord_profile = (v0810_chord_profile*_00ti_coeff).reshape((40, 1))

# op _00w2_linear_combination_eval
# LANG: _00vL, _00w1 --> rel_obs_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0899_rel_obs_z_pos = _00w2_constant+1*v0898__00vL+-1*v0900__00w1

# op _00w6_power_combination_eval
# LANG: rel_obs_x_pos --> _00w7
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0902__00w7 = (v0887_rel_obs_x_pos**2)
v0902__00w7 = (v0902__00w7*_00w6_coeff).reshape((1, 1, 2))

# op _00w8_power_combination_eval
# LANG: rel_obs_y_pos --> _00w9
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0904__00w9 = (v0895_rel_obs_y_pos**2)
v0904__00w9 = (v0904__00w9*_00w8_coeff).reshape((1, 1, 2))

# op _00w__power_combination_eval
# LANG: _00wZ --> _00x0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0932__00x0 = (v0931__00wZ**1)
v0932__00x0 = (v0932__00x0*_00w__coeff).reshape((1,))

# op _00xn expand_scalar_eval
# LANG: dr --> _00xo
# SHAPES: (1,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0927__00xo = np.empty((40, 1))
v0927__00xo.fill(v0829_dr.item())

# op _011j_linear_combination_eval
# LANG: _011g, _011i --> _011k
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01798__011k = _011j_constant+1*v01797__011g+1*v01805__011i

# op _013g_power_combination_eval
# LANG: _013a --> _013h
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01862__013h = (v01858__013a**2)
v01862__013h = (v01862__013h*_013g_coeff).reshape((1, 1))

# op _013s_power_combination_eval
# LANG: _013n, _013r --> _013t
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01867__013t = (v01866__013n**1)*(v01869__013r**1)
v01867__013t = (v01867__013t*_013s_coeff).reshape((1, 1))

# op _015C_arcsin_eval
# LANG: _015B --> _015D
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01937__015D = np.arcsin(v01936__015B)

# op _016C_power_combination_eval
# LANG: _016g --> _016D
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01965__016D = (v01964__016g**3.68)
v01965__016D = (v01965__016D*_016C_coeff).reshape((1, 2))

# op _016E_power_combination_eval
# LANG: Ab --> _016F
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01967__016F = (v01954_Ab**0.9)
v01967__016F = (v01967__016F*_016E_coeff).reshape((1, 2))

# op _016I_power_combination_eval
# LANG: sigma, _016j --> _016J
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01970__016J = (v01969__016j**1)*(v01955_sigma**-1)
v01970__016J = (v01970__016J*_016I_coeff).reshape((1, 2))

# op _016U_power_combination_eval
# LANG: _016g --> _016V
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01982__016V = (v01964__016g**7.44)
v01982__016V = (v01982__016V*_016U_coeff).reshape((1, 2))

# op _016W_power_combination_eval
# LANG: Ab --> _016X
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01984__016X = (v01954_Ab**0.9)
v01984__016X = (v01984__016X*_016W_coeff).reshape((1, 2))

# op _016__power_combination_eval
# LANG: sigma, _016j --> _0170
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01986__0170 = (v01969__016j**1)*(v01955_sigma**-1)
v01986__0170 = (v01986__0170*_016__coeff).reshape((1, 2))

# op _00QW_linear_combination_eval
# LANG: _00QV --> _00QX
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01455__00QX = _00QW_constant+1*v01454__00QV

# op _00R7_power_combination_eval
# LANG: _00R6 --> _00R8
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01462__00R8 = (v01459__00R6**0.5)
v01462__00R8 = (v01462__00R8*_00R7_coeff).reshape((1, 1))

# op _00Rb_power_combination_eval
# LANG: _00QO --> _00Rc
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01464__00Rc = (v01450__00QO**2)
v01464__00Rc = (v01464__00Rc*_00Rb_coeff).reshape((1, 1))

# op _00fM_single_tensor_sum_with_axis_eval
# LANG: _local_thrust --> _00fN
# SHAPES: (1, 40, 100) --> (1,)
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

# op _00su_linear_combination_eval
# LANG: _00sr, _00st --> _00sv
# SHAPES: (1, 2, 3, 2), (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0788__00sv = _00su_constant+1*v0787__00sr+1*v0790__00st

# op _00w5_indexed_passthrough_eval
# LANG: rel_obs_x_pos, rel_obs_y_pos, rel_obs_z_pos --> rel_obs_position
# SHAPES: (1, 1, 2), (1, 1, 2), (1, 1, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0901_rel_obs_position__temp[i_v0887_rel_obs_x_pos__00w5_indexed_passthrough_eval] = v0887_rel_obs_x_pos.flatten()
v0901_rel_obs_position = v0901_rel_obs_position__temp.copy()
v0901_rel_obs_position__temp[i_v0895_rel_obs_y_pos__00w5_indexed_passthrough_eval] = v0895_rel_obs_y_pos.flatten()
v0901_rel_obs_position = v0901_rel_obs_position__temp.copy()
v0901_rel_obs_position__temp[i_v0899_rel_obs_z_pos__00w5_indexed_passthrough_eval] = v0899_rel_obs_z_pos.flatten()
v0901_rel_obs_position = v0901_rel_obs_position__temp.copy()

# op _00wa_linear_combination_eval
# LANG: _00w7, _00w9 --> _00wb
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0903__00wb = _00wa_constant+1*v0902__00w7+1*v0904__00w9

# op _00wc_power_combination_eval
# LANG: rel_obs_z_pos --> _00wd
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0906__00wd = (v0899_rel_obs_z_pos**2)
v0906__00wd = (v0906__00wd*_00wc_coeff).reshape((1, 1, 2))

# op _00wj expand_array_eval
# LANG: thrust_dir --> _00wk
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0909__00wk = np.einsum('b,ac->abc', v0822_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00x1_power_combination_eval
# LANG: _00x0 --> _00x2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0933__00x2 = (v0932__00x0**1)
v0933__00x2 = (v0933__00x2*_00x1_coeff).reshape((1,))

# op _00xp_power_combination_eval
# LANG: _00xo, chord_profile --> _00xq
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0926__00xq = (v0810_chord_profile**1)*(v0927__00xo**1)
v0926__00xq = (v0926__00xq*_00xp_coeff).reshape((40, 1))

# op _011l_power_combination_eval
# LANG: _011k --> _011m
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01806__011m = (v01798__011k**1)
v01806__011m = (v01806__011m*_011l_coeff).reshape((1, 2, 3))

# op _013i_linear_combination_eval
# LANG: _013h --> _013j
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01863__013j = _013i_constant+1*v01862__013h

# op _013u_power_combination_eval
# LANG: _013t --> _013v
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01870__013v = (v01867__013t**0.5)
v01870__013v = (v01870__013v*_013u_coeff).reshape((1, 1))

# op _013y_power_combination_eval
# LANG: _013a --> _013z
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01872__013z = (v01858__013a**2)
v01872__013z = (v01872__013z*_013y_coeff).reshape((1, 1))

# op _015K reshape_eval
# LANG: _015D --> rel_angle_plane
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01938_rel_angle_plane = v01937__015D.reshape((1, 2))

# op _016G_power_combination_eval
# LANG: _016D, _016F --> _016H
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01966__016H = (v01965__016D**1)*(v01967__016F**1)
v01966__016H = (v01966__016H*_016G_coeff).reshape((1, 2))

# op _016K_power_combination_eval
# LANG: _016J --> _016L
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01971__016L = (v01970__016J**1.6)
v01971__016L = (v01971__016L*_016K_coeff).reshape((1, 2))

# op _016Y_power_combination_eval
# LANG: _016V, _016X --> _016Z
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01983__016Z = (v01982__016V**1)*(v01984__016X**1)
v01983__016Z = (v01983__016Z*_016Y_coeff).reshape((1, 2))

# op _0171_power_combination_eval
# LANG: _0170 --> _0172
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01987__0172 = (v01986__0170**1.6)
v01987__0172 = (v01987__0172*_0171_coeff).reshape((1, 2))

# op _017b_linear_combination_eval
# LANG: Ab --> _017c
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01976__017c = _017b_constant+-1*v01954_Ab

# op _017n_linear_combination_eval
# LANG: Ab --> _017o
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01992__017o = _017n_constant+1*v01954_Ab

# op _00QQ_power_combination_eval
# LANG: _00QO --> _00QR
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01451__00QR = (v01450__00QO**4)
v01451__00QR = (v01451__00QR*_00QQ_coeff).reshape((1, 1))

# op _00R9_power_combination_eval
# LANG: _00QX, _00R8 --> _00Ra
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01456__00Ra = (v01455__00QX**1)*(v01462__00R8**1)
v01456__00Ra = (v01456__00Ra*_00R9_coeff).reshape((1, 1))

# op _00Rd_linear_combination_eval
# LANG: _00Rc --> _00Re
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01465__00Re = _00Rd_constant+1*v01464__00Rc

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

# op _00jd_power_combination_eval
# LANG: rpm --> _00je
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0508__00je = (v0164_rpm**1)
v0508__00je = (v0508__00je*_00jd_coeff).reshape((1, 1))

# op _00sw_power_combination_eval
# LANG: _00sv --> _00sx
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0791__00sx = (v0788__00sv**1)
v0791__00sx = (v0791__00sx*_00sw_coeff).reshape((1, 2, 3, 2))

# op _00tZ_power_combination_eval
# LANG: rpm --> _00t_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0831__00t_ = (v0164_rpm**1)
v0831__00t_ = (v0831__00t_*_00tZ_coeff).reshape((1, 1))

# op _00we_linear_combination_eval
# LANG: _00wb, _00wd --> _00wf
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0905__00wf = _00we_constant+1*v0903__00wb+1*v0906__00wd

# op _00wl_tensor_dot_product_eval
# LANG: rel_obs_position, _00wk --> normal_proj
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0908_normal_proj = np.sum(v0901_rel_obs_position * v0909__00wk, axis=1)

# op _00x3_power_combination_eval
# LANG: _00x2 --> _00x4
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0934__00x4 = (v0933__00x2**1)
v0934__00x4 = (v0934__00x4*_00x3_coeff).reshape((1,))

# op _00xr_single_tensor_sum_with_axis_eval
# LANG: _00xq --> _00xs
# SHAPES: (40, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0928__00xs = np.sum(v0926__00xq, axis = (0,)).reshape((1,))

# op _011n_power_combination_eval
# LANG: _011m --> _011o
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01807__011o = (v01806__011m**1)
v01807__011o = (v01807__011o*_011n_coeff).reshape((1, 2, 3))

# op _013A_linear_combination_eval
# LANG: _013z --> _013B
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01873__013B = _013A_constant+1*v01872__013z

# op _013c_power_combination_eval
# LANG: _013a --> _013d
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01859__013d = (v01858__013a**4)
v01859__013d = (v01859__013d*_013c_coeff).reshape((1, 1))

# op _013w_power_combination_eval
# LANG: _013j, _013v --> _013x
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01864__013x = (v01863__013j**1)*(v01870__013v**1)
v01864__013x = (v01864__013x*_013w_coeff).reshape((1, 1))

# op _016M_power_combination_eval
# LANG: _016H, _016L --> _016N
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01968__016N = (v01966__016H**1)*(v01971__016L**1)
v01968__016N = (v01968__016N*_016M_coeff).reshape((1, 2))

# op _0173_power_combination_eval
# LANG: _016Z, _0172 --> _0174
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01985__0174 = (v01983__016Z**1)*(v01987__0172**1)
v01985__0174 = (v01985__0174*_0173_coeff).reshape((1, 2))

# op _017__power_combination_eval
# LANG: rel_angle_plane --> _0180
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02009__0180 = (v01938_rel_angle_plane**2)
v02009__0180 = (v02009__0180*_017__coeff).reshape((1, 2))

# op _017d_power_combination_eval
# LANG: _017c --> _017e
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01977__017e = (v01976__017c**1)
v01977__017e = (v01977__017e*_017d_coeff).reshape((1, 2))

# op _017p_power_combination_eval
# LANG: _017o --> _017q
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01993__017q = (v01992__017o**1)
v01993__017q = (v01993__017q*_017p_coeff).reshape((1, 2))

# op _00QS_power_combination_eval
# LANG: _00QR --> _00QT
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01452__00QT = (v01451__00QR**1)
v01452__00QT = (v01452__00QT*_00QS_coeff).reshape((1, 1))

# op _00Rf_power_combination_eval
# LANG: _00Ra, _00Re --> _00Rg
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01463__00Rg = (v01456__00Ra**1)*(v01465__00Re**1)
v01463__00Rg = (v01463__00Rg*_00Rf_coeff).reshape((1, 1))

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

# op _00jf_power_combination_eval
# LANG: _00je --> _00jg
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0509__00jg = (v0508__00je**1)
v0509__00jg = (v0509__00jg*_00jf_coeff).reshape((1, 1))

# op _00sy_log10_eval
# LANG: _00sx --> _00sz
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0792__00sz = np.log10(v0791__00sx)

# op _00u0_power_combination_eval
# LANG: _00t_ --> _00u1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0832__00u1 = (v0831__00t_**1)
v0832__00u1 = (v0832__00u1*_00u0_coeff).reshape((1, 1))

# op _00wg_power_combination_eval
# LANG: _00wf --> rel_obs_dist
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0907_rel_obs_dist = (v0905__00wf**0.5)
v0907_rel_obs_dist = (v0907_rel_obs_dist*_00wg_coeff).reshape((1, 1, 2))

# op _00wr expand_array_eval
# LANG: normal_proj --> _00ws
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0910__00ws = np.einsum('ac,b->abc', v0908_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00x5_linear_combination_eval
# LANG: _00x4 --> _00x6
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0935__00x6 = _00x5_constant+1*v0934__00x4

# op _00xt_power_combination_eval
# LANG: _00xs --> _00xu
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0929__00xu = (v0928__00xs**1)
v0929__00xu = (v0929__00xu*_00xt_coeff).reshape((1,))

# op _011p_log10_eval
# LANG: _011o --> _011q
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01808__011q = np.log10(v01807__011o)

# op _013C_power_combination_eval
# LANG: _013x, _013B --> _013D
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01871__013D = (v01864__013x**1)*(v01873__013B**1)
v01871__013D = (v01871__013D*_013C_coeff).reshape((1, 1))

# op _013e_power_combination_eval
# LANG: _013d --> _013f
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01860__013f = (v01859__013d**1)
v01860__013f = (v01860__013f*_013e_coeff).reshape((1, 1))

# op _016O_log10_eval
# LANG: _016N --> _016P
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01972__016P = np.log10(v01968__016N)

# op _0175_log10_eval
# LANG: _0174 --> _0176
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01988__0176 = np.log10(v01985__0174)

# op _017f_tanh_eval
# LANG: _017e --> _017g
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01978__017g = np.tanh(v01977__017e)

# op _017r_tanh_eval
# LANG: _017q --> _017s
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01994__017s = np.tanh(v01993__017q)

# op _0181_power_combination_eval
# LANG: _0180 --> _0182
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02010__0182 = (v02009__0180**0.5)
v02010__0182 = (v02010__0182*_0181_coeff).reshape((1, 2))

# op _00Rh_power_combination_eval
# LANG: _00QT, _00Rg --> _00Ri
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01453__00Ri = (v01452__00QT**1)*(v01463__00Rg**-1)
v01453__00Ri = (v01453__00Ri*_00Rh_coeff).reshape((1, 1))

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

# op _00jh_power_combination_eval
# LANG: _00jg --> _00ji
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0510__00ji = (v0509__00jg**1)
v0510__00ji = (v0510__00ji*_00jh_coeff).reshape((1, 1))

# op _00sA_power_combination_eval
# LANG: _00sz --> bladeSPL
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0793_bladeSPL = (v0792__00sz**1)
v0793_bladeSPL = (v0793_bladeSPL*_00sA_coeff).reshape((1, 2, 3, 2))

# op _00u2_power_combination_eval
# LANG: _00u1 --> _00u3
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0833__00u3 = (v0832__00u1**1)
v0833__00u3 = (v0833__00u3*_00u2_coeff).reshape((1, 1))

# op _00wt_power_combination_eval
# LANG: rel_obs_dist, _00ws --> _00wu
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0911__00wu = (v0910__00ws**1)*(v0907_rel_obs_dist**-1)
v0911__00wu = (v0911__00wu*_00wt_coeff).reshape((1, 1, 2))

# op _00x7 expand_scalar_eval
# LANG: _00x6 --> _00x8
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0936__00x8 = np.empty((1, 2))
v0936__00x8.fill(v0935__00x6.item())

# op _00xa expand_scalar_eval
# LANG: propeller_radius --> _00xb
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0939__00xb = np.empty((1, 2))
v0939__00xb.fill(v0807_propeller_radius.item())

# op _00xv expand_scalar_eval
# LANG: _00xu --> Ab
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0930_Ab = np.empty((1, 2))
v0930_Ab.fill(v0929__00xu.item())

# op _011r_power_combination_eval
# LANG: _011q --> _011s
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01809__011s = (v01808__011q**1)
v01809__011s = (v01809__011s*_011r_coeff).reshape((1, 2, 3))

# op _013E_power_combination_eval
# LANG: _013f, _013D --> _013F
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01861__013F = (v01860__013f**1)*(v01871__013D**-1)
v01861__013F = (v01861__013F*_013E_coeff).reshape((1, 1))

# op _016Q_power_combination_eval
# LANG: _016P --> _016R
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01973__016R = (v01972__016P**1)
v01973__016R = (v01973__016R*_016Q_coeff).reshape((1, 2))

# op _0177_power_combination_eval
# LANG: _0176 --> _0178
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01989__0178 = (v01988__0176**1)
v01989__0178 = (v01989__0178*_0177_coeff).reshape((1, 2))

# op _017B_power_combination_eval
# LANG: propeller_radius --> _017C
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02005__017C = (v01832_propeller_radius**1)
v02005__017C = (v02005__017C*_017B_coeff).reshape((1,))

# op _017M_power_combination_eval
# LANG: rel_angle_plane --> _017N
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01998__017N = (v01938_rel_angle_plane**2.0)
v01998__017N = (v01998__017N*_017M_coeff).reshape((1, 2))

# op _017h_power_combination_eval
# LANG: _017g --> _017i
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01979__017i = (v01978__017g**1)
v01979__017i = (v01979__017i*_017h_coeff).reshape((1, 2))

# op _017t_power_combination_eval
# LANG: _017s --> _017u
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01995__017u = (v01994__017s**1)
v01995__017u = (v01995__017u*_017t_coeff).reshape((1, 2))

# op _0183_sin_eval
# LANG: _0182 --> _0184
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02011__0184 = np.sin(v02010__0182)

# op _00Rj_log10_eval
# LANG: _00Ri --> _00Rk
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01466__00Rk = np.log10(v01453__00Ri)

# op _00Rn_log10_eval
# LANG: RA_1000 --> _00Ro
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01470__00Ro = np.log10(v01469_RA_1000)

# op _00h2_power_combination_eval
# LANG: _00gS, _00h1 --> C_T
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0448_C_T = (v0441__00gS**1)*(v0453__00h1**-1)
v0448_C_T = (v0448_C_T*_00h2_coeff).reshape((1,))

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

# op _00sC_power_combination_eval
# LANG: bladeSPL --> _00sD
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0794__00sD = (v0793_bladeSPL**1)
v0794__00sD = (v0794__00sD*_00sC_coeff).reshape((1, 2, 3, 2))

# op _00ud_power_combination_eval
# LANG: _00u3 --> _00ue
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0840__00ue = (v0833__00u3**2)
v0840__00ue = (v0840__00ue*_00ud_coeff).reshape((1, 1))

# op _00uh_power_combination_eval
# LANG: _00u3 --> _00ui
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0843__00ui = (v0833__00u3**2)
v0843__00ui = (v0843__00ui*_00uh_coeff).reshape((1, 1))

# op _00wv_arcsin_eval
# LANG: _00wu --> _00ww
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0912__00ww = np.arcsin(v0911__00wu)

# op _00xj_linear_combination_eval
# LANG: _00x8 --> _00xk
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0937__00xk = _00xj_constant+1*v0936__00x8

# op _00xx_power_combination_eval
# LANG: Ab --> _00xy
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0945__00xy = (v0930_Ab**1)
v0945__00xy = (v0945__00xy*_00xx_coeff).reshape((1, 2))

# op _00xz_power_combination_eval
# LANG: _00xb --> _00xA
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0947__00xA = (v0939__00xb**2)
v0947__00xA = (v0947__00xA*_00xz_coeff).reshape((1, 2))

# op _011t_power_combination_eval
# LANG: _011s --> _011u
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01810__011u = (v01809__011s**1)
v01810__011u = (v01810__011u*_011t_coeff).reshape((1, 2, 3))

# op _013G_log10_eval
# LANG: _013F --> _013H
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01874__013H = np.log10(v01861__013F)

# op _013K_log10_eval
# LANG: RA_1000 --> _013L
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01878__013L = np.log10(v01877_RA_1000)

# op _016S_linear_combination_eval
# LANG: _016R --> _016T
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01974__016T = _016S_constant+1*v01973__016R

# op _0179_linear_combination_eval
# LANG: _0178 --> _017a
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01990__017a = _0179_constant+1*v01989__0178

# op _017D expand_scalar_eval
# LANG: _017C --> _017E
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02006__017E = np.empty((1, 2))
v02006__017E.fill(v02005__017C.item())

# op _017G reshape_eval
# LANG: rel_obs_dist --> _017H
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02003__017H = v01932_rel_obs_dist.reshape((1, 2))

# op _017O_power_combination_eval
# LANG: _017N --> _017P
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01999__017P = (v01998__017N**0.5)
v01999__017P = (v01999__017P*_017O_coeff).reshape((1, 2))

# op _017j_linear_combination_eval
# LANG: _017i --> _017k
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01980__017k = _017j_constant+1*v01979__017i

# op _017v_linear_combination_eval
# LANG: _017u --> _017w
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01996__017w = _017v_constant+1*v01995__017u

# op _0185_linear_combination_eval
# LANG: _0184 --> _0186
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02012__0186 = _0185_constant+-1*v02011__0184

# op _00Rl_power_combination_eval
# LANG: _00Rk --> _00Rm
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01467__00Rm = (v01466__00Rk**1)
v01467__00Rm = (v01467__00Rm*_00Rl_coeff).reshape((1, 1))

# op _00Rp_power_combination_eval
# LANG: _00Ro --> _00Rq
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01471__00Rq = (v01470__00Ro**1)
v01471__00Rq = (v01471__00Rq*_00Rp_coeff).reshape((1, 1))

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

# op _00sE_exp_a_eval
# LANG: _00sD --> _00sF
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0795__00sF = _00sE_exp_a_eval_a**v0794__00sD

# op _00uf_linear_combination_eval
# LANG: _00ue --> _00ug
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0841__00ug = _00uf_constant+1*v0840__00ue

# op _00uj_linear_combination_eval
# LANG: _00ui --> _00uk
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0844__00uk = _00uj_constant+1*v0843__00ui

# op _00wD reshape_eval
# LANG: _00ww --> rel_angle_plane
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0913_rel_angle_plane = v0912__00ww.reshape((1, 2))

# op _00xB_power_combination_eval
# LANG: _00xy, _00xA --> _00xC
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0946__00xC = (v0945__00xy**1)*(v0947__00xA**-1)
v0946__00xC = (v0946__00xC*_00xB_coeff).reshape((1, 2))

# op _00xE expand_scalar_eval
# LANG: CT --> _00xF
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0943__00xF = np.empty((1, 2))
v0943__00xF.fill(v0448_C_T.item())

# op _00xG_power_combination_eval
# LANG: _00xk, _00xb --> _00xH
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0938__00xH = (v0937__00xk**1)*(v0939__00xb**1)
v0938__00xH = (v0938__00xH*_00xG_coeff).reshape((1, 2))

# op _011v_exp_a_eval
# LANG: _011u --> _011w
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01811__011w = _011v_exp_a_eval_a**v01810__011u

# op _013I_power_combination_eval
# LANG: _013H --> _013J
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01875__013J = (v01874__013H**1)
v01875__013J = (v01875__013J*_013I_coeff).reshape((1, 1))

# op _013M_power_combination_eval
# LANG: _013L --> _013N
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01879__013N = (v01878__013L**1)
v01879__013N = (v01879__013N*_013M_coeff).reshape((1, 1))

# op _017Q_sin_eval
# LANG: _017P --> _017R
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02000__017R = np.sin(v01999__017P)

# op _017W_power_combination_eval
# LANG: _017H, _017E --> _017X
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02004__017X = (v02003__017H**1)*(v02006__017E**-1)
v02004__017X = (v02004__017X*_017W_coeff).reshape((1, 2))

# op _017l_power_combination_eval
# LANG: _016T, _017k --> _017m
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01975__017m = (v01974__016T**1)*(v01980__017k**1)
v01975__017m = (v01975__017m*_017l_coeff).reshape((1, 2))

# op _017x_power_combination_eval
# LANG: _017a, _017w --> _017y
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01991__017y = (v01990__017a**1)*(v01996__017w**1)
v01991__017y = (v01991__017y*_017x_coeff).reshape((1, 2))

# op _0187_power_combination_eval
# LANG: _0186 --> _0188
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02013__0188 = (v02012__0186**1)
v02013__0188 = (v02013__0188*_0187_coeff).reshape((1, 2))

# op _00Rr_linear_combination_eval
# LANG: _00Rm, _00Rq --> _00Rs
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01468__00Rs = _00Rr_constant+1*v01467__00Rm+-1*v01471__00Rq

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

# op _00sG_single_tensor_sum_with_axis_eval
# LANG: _00sF --> _00sH
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0796__00sH = np.sum(v0795__00sF, axis = (3,)).reshape((1, 2, 3))

# op _00u9_power_combination_eval
# LANG: _00u3 --> _00ua
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0837__00ua = (v0833__00u3**2)
v0837__00ua = (v0837__00ua*_00u9_coeff).reshape((1, 1))

# op _00ul_power_combination_eval
# LANG: _00ug, _00uk --> _00um
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0842__00um = (v0841__00ug**1)*(v0844__00uk**1)
v0842__00um = (v0842__00um*_00ul_coeff).reshape((1, 1))

# op _00xI_power_combination_eval
# LANG: _00xH --> _00xJ
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0940__00xJ = (v0938__00xH**6)
v0940__00xJ = (v0940__00xJ*_00xI_coeff).reshape((1, 2))

# op _00xM_power_combination_eval
# LANG: _00xF, _00xC --> _00xN
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0944__00xN = (v0943__00xF**1)*(v0946__00xC**-1)
v0944__00xN = (v0944__00xN*_00xM_coeff).reshape((1, 2))

# op _00x__power_combination_eval
# LANG: rel_angle_plane --> _00y0
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0954__00y0 = (v0913_rel_angle_plane**2)
v0954__00y0 = (v0954__00y0*_00x__coeff).reshape((1, 2))

# op _011x_single_tensor_sum_with_axis_eval
# LANG: _011w --> _011y
# SHAPES: (1, 2, 3) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01812__011y = np.sum(v01811__011w, axis = (2,)).reshape((1, 2))

# op _013O_linear_combination_eval
# LANG: _013J, _013N --> _013P
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01876__013P = _013O_constant+1*v01875__013J+-1*v01879__013N

# op _017S_power_combination_eval
# LANG: _017R --> _017T
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02001__017T = (v02000__017R**0.031)
v02001__017T = (v02001__017T*_017S_coeff).reshape((1, 2))

# op _017Y_log10_eval
# LANG: _017X --> _017Z
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02007__017Z = np.log10(v02004__017X)

# op _017z_linear_combination_eval
# LANG: _017m, _017y --> _017A
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01981__017A = _017z_constant+1*v01975__017m+1*v01991__017y

# op _0189_linear_combination_eval
# LANG: _0188 --> _018a
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02014__018a = _0189_constant+1*v02013__0188

# op _00Lj_power_combination_eval
# LANG: _radius --> _00Lk
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01287__00Lk = (v01159__radius**2)
v01287__00Lk = (v01287__00Lk*_00Lj_coeff).reshape((1, 40, 30))

# op _00Rt reshape_eval
# LANG: _00Rs --> _00Ru
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01472__00Ru = v01468__00Rs.reshape((1,))

# op _00dE_power_combination_eval
# LANG: _radius --> _00dF
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0345__00dF = (v0217__radius**2)
v0345__00dF = (v0345__00dF*_00dE_coeff).reshape((1, 40, 100))

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

# op _00sI_log10_eval
# LANG: _00sH --> _00sJ
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0797__00sJ = np.log10(v0796__00sH)

# op _00ub_linear_combination_eval
# LANG: _00ua --> _00uc
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0838__00uc = _00ub_constant+1*v0837__00ua

# op _00un_power_combination_eval
# LANG: _00um --> _00uo
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0845__00uo = (v0842__00um**0.5)
v0845__00uo = (v0845__00uo*_00un_coeff).reshape((1, 1))

# op _00ur_power_combination_eval
# LANG: _00u3 --> _00us
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0847__00us = (v0833__00u3**2)
v0847__00us = (v0847__00us*_00ur_coeff).reshape((1, 1))

# op _00xK_power_combination_eval
# LANG: Ab, _00xJ --> _00xL
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0941__00xL = (v0940__00xJ**1)*(v0930_Ab**1)
v0941__00xL = (v0941__00xL*_00xK_coeff).reshape((1, 2))

# op _00xO_power_combination_eval
# LANG: _00xN --> _00xP
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0948__00xP = (v0944__00xN**2)
v0948__00xP = (v0948__00xP*_00xO_coeff).reshape((1, 2))

# op _00xd reshape_eval
# LANG: rel_obs_dist --> _00xe
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0958__00xe = v0907_rel_obs_dist.reshape((1, 2))

# op _00y1_power_combination_eval
# LANG: _00y0 --> _00y2
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0955__00y2 = (v0954__00y0**0.5)
v0955__00y2 = (v0955__00y2*_00y1_coeff).reshape((1, 2))

# op _011z_log10_eval
# LANG: _011y --> _011A
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01813__011A = np.log10(v01812__011y)

# op _013Q reshape_eval
# LANG: _013P --> _013R
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01880__013R = v01876__013P.reshape((1,))

# op _017U_power_combination_eval
# LANG: _017A, _017T --> _017V
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01997__017V = (v01981__017A**1)*(v02001__017T**1)
v01997__017V = (v01997__017V*_017U_coeff).reshape((1, 2))

# op _018b_power_combination_eval
# LANG: _017Z, _018a --> _018c
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02008__018c = (v02007__017Z**1)*(v02014__018a**1)
v02008__018c = (v02008__018c*_018b_coeff).reshape((1, 2))

# op _00Ll_power_combination_eval
# LANG: _00Lk --> _00Lm
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01288__00Lm = (v01287__00Lk**1)
v01288__00Lm = (v01288__00Lm*_00Ll_coeff).reshape((1, 40, 30))

# op _00Rv expand_scalar_eval
# LANG: _00Ru --> _00Rw
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01473__00Rw = np.empty((1, 2))
v01473__00Rw.fill(v01472__00Ru.item())

# op _00dG_power_combination_eval
# LANG: _00dF --> _00dH
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0346__00dH = (v0345__00dF**1)
v0346__00dH = (v0346__00dH*_00dG_coeff).reshape((1, 40, 100))

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

# op _00sK_power_combination_eval
# LANG: _00sJ --> _00sL
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0798__00sL = (v0797__00sJ**1)
v0798__00sL = (v0798__00sL*_00sK_coeff).reshape((1, 2, 3))

# op _00u5_power_combination_eval
# LANG: _00u3 --> _00u6
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0834__00u6 = (v0833__00u3**4)
v0834__00u6 = (v0834__00u6*_00u5_coeff).reshape((1, 1))

# op _00up_power_combination_eval
# LANG: _00uc, _00uo --> _00uq
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0839__00uq = (v0838__00uc**1)*(v0845__00uo**1)
v0839__00uq = (v0839__00uq*_00up_coeff).reshape((1, 1))

# op _00ut_linear_combination_eval
# LANG: _00us --> _00uu
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0848__00uu = _00ut_constant+1*v0847__00us

# op _00xQ_power_combination_eval
# LANG: _00xL, _00xP --> _00xR
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0942__00xR = (v0941__00xL**1)*(v0948__00xP**1)
v0942__00xR = (v0942__00xR*_00xQ_coeff).reshape((1, 2))

# op _00y3_sin_eval
# LANG: _00y2 --> _00y4
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0956__00y4 = np.sin(v0955__00y2)

# op _00y5_power_combination_eval
# LANG: _00xe --> _00y6
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0959__00y6 = (v0958__00xe**1)
v0959__00y6 = (v0959__00y6*_00y5_coeff).reshape((1, 2))

# op _011B_power_combination_eval
# LANG: _011A --> rotor_disk_tonal_spl
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01814_rotor_disk_tonal_spl = (v01813__011A**1)
v01814_rotor_disk_tonal_spl = (v01814_rotor_disk_tonal_spl*_011B_coeff).reshape((1, 2))

# op _013S expand_scalar_eval
# LANG: _013R --> _013T
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01881__013T = np.empty((1, 2))
v01881__013T.fill(v01880__013R.item())

# op _018d_linear_combination_eval
# LANG: _017V, _018c --> rotor_disk_broadband_spl
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v02002_rotor_disk_broadband_spl = _018d_constant+1*v01997__017V+-1*v02008__018c

# op _00Ln_power_combination_eval
# LANG: _00Je, _00Lm --> _00Lo
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01289__00Lo = (v01288__00Lm**1)*(v01265__00Je**1)
v01289__00Lo = (v01289__00Lo*_00Ln_coeff).reshape((1, 40, 30))

# op _00Rx_linear_combination_eval
# LANG: _00Rw, rotor_disk_tonal_spl --> _00Ry
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01447__00Ry = _00Rx_constant+1*v01814_rotor_disk_tonal_spl+1*v01473__00Rw

# op _00dI_power_combination_eval
# LANG: _00bz, _00dH --> _00dJ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0347__00dJ = (v0346__00dH**1)*(v0323__00bz**1)
v0347__00dJ = (v0347__00dJ*_00dI_coeff).reshape((1, 40, 100))

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

# op _00sM_power_combination_eval
# LANG: _00sL --> _00sN
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0799__00sN = (v0798__00sL**1)
v0799__00sN = (v0799__00sN*_00sM_coeff).reshape((1, 2, 3))

# op _00u7_power_combination_eval
# LANG: _00u6 --> _00u8
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0835__00u8 = (v0834__00u6**1)
v0835__00u8 = (v0835__00u8*_00u7_coeff).reshape((1, 1))

# op _00uv_power_combination_eval
# LANG: _00uq, _00uu --> _00uw
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0846__00uw = (v0839__00uq**1)*(v0848__00uu**1)
v0846__00uw = (v0846__00uw*_00uv_coeff).reshape((1, 1))

# op _00xS_linear_combination_eval
# LANG: _00xR --> _00xT
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0949__00xT = _00xS_constant+1*v0942__00xR

# op _00y7_power_combination_eval
# LANG: _00y4, _00y6 --> _00y8
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0957__00y8 = (v0956__00y4**1)*(v0959__00y6**-1)
v0957__00y8 = (v0957__00y8*_00y7_coeff).reshape((1, 2))

# op _013U_linear_combination_eval
# LANG: _013T, rotor_disk_broadband_spl --> _013V
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01855__013V = _013U_constant+1*v02002_rotor_disk_broadband_spl+1*v01881__013T

# op _00Lp_power_combination_eval
# LANG: _ux, _00Lo --> _00Lq
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01290__00Lq = (v01289__00Lo**1)*(v01224__ux**1)
v01290__00Lq = (v01290__00Lq*_00Lp_coeff).reshape((1, 40, 30))

# op _00Rz_power_combination_eval
# LANG: _00Ry --> _00RA
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01474__00RA = (v01447__00Ry**1)
v01474__00RA = (v01474__00RA*_00Rz_coeff).reshape((1, 2))

# op _00dK_power_combination_eval
# LANG: _ux, _00dJ --> _00dL
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0348__00dL = (v0347__00dJ**1)*(v0282__ux**1)
v0348__00dL = (v0348__00dL*_00dK_coeff).reshape((1, 40, 100))

# op _00jM_power_combination_eval
# LANG: _00jn, _00jL --> _00jN
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0513__00jN = (v0512__00jn**1)*(v0523__00jL**-1)
v0513__00jN = (v0513__00jN*_00jM_coeff).reshape((1, 1))

# op _00sO_exp_a_eval
# LANG: _00sN --> _00sP
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0800__00sP = _00sO_exp_a_eval_a**v0799__00sN

# op _00ux_power_combination_eval
# LANG: _00u8, _00uw --> _00uy
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0836__00uy = (v0835__00u8**1)*(v0846__00uw**-1)
v0836__00uy = (v0836__00uy*_00ux_coeff).reshape((1, 1))

# op _00xU_log10_eval
# LANG: _00xT --> _00xV
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0950__00xV = np.log10(v0949__00xT)

# op _00y9_linear_combination_eval
# LANG: _00y8 --> _00ya
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0960__00ya = _00y9_constant+1*v0957__00y8

# op _013W_power_combination_eval
# LANG: _013V --> _013X
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01882__013X = (v01855__013V**1)
v01882__013X = (v01882__013X*_013W_coeff).reshape((1, 2))

# op _00Lr_power_combination_eval
# LANG: _ut, _00Lq --> _00Ls
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01291__00Ls = (v01290__00Lq**1)*(v01256__ut**1)
v01291__00Ls = (v01291__00Ls*_00Lr_coeff).reshape((1, 40, 30))

# op _00M0_power_combination_eval
# LANG: _ut --> _00M1
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01359__00M1 = (v01256__ut**1)
v01359__00M1 = (v01359__00M1*_00M0_coeff).reshape((1, 40, 30))

# op _00RB_exp_a_eval
# LANG: _00RA --> _00RC
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01475__00RC = _00RB_exp_a_eval_a**v01474__00RA

# op _00dM_power_combination_eval
# LANG: _ut, _00dL --> _00dN
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0349__00dN = (v0348__00dL**1)*(v0314__ut**1)
v0349__00dN = (v0349__00dN*_00dM_coeff).reshape((1, 40, 100))

# op _00el_power_combination_eval
# LANG: _ut --> _00em
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0417__00em = (v0314__ut**1)
v0417__00em = (v0417__00em*_00el_coeff).reshape((1, 40, 100))

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

# op _00sQ_single_tensor_sum_with_axis_eval
# LANG: _00sP --> _00sR
# SHAPES: (1, 2, 3) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0801__00sR = np.sum(v0800__00sP, axis = (2,)).reshape((1, 2))

# op _00uD_log10_eval
# LANG: RA_1000 --> _00uE
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0853__00uE = np.log10(v0852_RA_1000)

# op _00uz_log10_eval
# LANG: _00uy --> _00uA
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0849__00uA = np.log10(v0836__00uy)

# op _00xW_power_combination_eval
# LANG: _00xV --> _00xX
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0951__00xX = (v0950__00xV**1)
v0951__00xX = (v0951__00xX*_00xW_coeff).reshape((1, 2))

# op _00yb_log10_eval
# LANG: _00ya --> _00yc
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0961__00yc = np.log10(v0960__00ya)

# op _013Y_exp_a_eval
# LANG: _013X --> _013Z
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01883__013Z = _013Y_exp_a_eval_a**v01882__013X

# op _00A5_power_combination_eval
# LANG: hover_altitude --> _00A6
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01034__00A6 = (v0990_hover_altitude**0)
v01034__00A6 = (v01034__00A6*_00A5_coeff).reshape((1,))

# op _00LF_power_combination_eval
# LANG: _ut --> _00LG
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01312__00LG = (v01256__ut**1)
v01312__00LG = (v01312__00LG*_00LF_coeff).reshape((1, 40, 30))

# op _00LT_power_combination_eval
# LANG: _00JC --> _00LU
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01352__00LU = (v01234__00JC**1)
v01352__00LU = (v01352__00LU*_00LT_coeff).reshape((1, 40, 30))

# op _00Lt_power_combination_eval
# LANG: _00Ls, prandtl_loss_factor --> _00Lu
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01292__00Lu = (v01291__00Ls**1)*(v01209_prandtl_loss_factor**1)
v01292__00Lu = (v01292__00Lu*_00Lt_coeff).reshape((1, 40, 30))

# op _00M2_linear_combination_eval
# LANG: _00M1, _tangential_inflow_velocity --> _00M3
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01358__00M3 = _00M2_constant+1*v01176__tangential_inflow_velocity+-1*v01359__00M1

# op _00RD_log10_eval
# LANG: _00RC --> _00RE
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01476__00RE = np.log10(v01475__00RC)

# op _00dO_power_combination_eval
# LANG: _00dN, prandtl_loss_factor --> _00dP
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0350__00dP = (v0349__00dN**1)*(v0267_prandtl_loss_factor**1)
v0350__00dP = (v0350__00dP*_00dO_coeff).reshape((1, 40, 100))

# op _00d__power_combination_eval
# LANG: _ut --> _00e0
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0370__00e0 = (v0314__ut**1)
v0370__00e0 = (v0370__00e0*_00d__coeff).reshape((1, 40, 100))

# op _00ed_power_combination_eval
# LANG: _00bX --> _00ee
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0410__00ee = (v0292__00bX**1)
v0410__00ee = (v0410__00ee*_00ed_coeff).reshape((1, 40, 100))

# op _00en_linear_combination_eval
# LANG: _00em, _tangential_inflow_velocity --> _00eo
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
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

# op _00sS_log10_eval
# LANG: _00sR --> _00sT
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0802__00sT = np.log10(v0801__00sR)

# op _00uB_power_combination_eval
# LANG: _00uA --> _00uC
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0850__00uC = (v0849__00uA**1)
v0850__00uC = (v0850__00uC*_00uB_coeff).reshape((1, 1))

# op _00uF_power_combination_eval
# LANG: _00uE --> _00uG
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0854__00uG = (v0853__00uE**1)
v0854__00uG = (v0854__00uG*_00uF_coeff).reshape((1, 1))

# op _00xY_linear_combination_eval
# LANG: _00xX --> _00xZ
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0952__00xZ = _00xY_constant+1*v0951__00xX

# op _00yW_power_combination_eval
# LANG: hover_altitude --> _00yX
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01021__00yX = (v0990_hover_altitude**6)
v01021__00yX = (v01021__00yX*_00yW_coeff).reshape((1,))

# op _00yd_power_combination_eval
# LANG: _00yc --> _00ye
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0962__00ye = (v0961__00yc**1)
v0962__00ye = (v0962__00ye*_00yd_coeff).reshape((1, 2))

# op _00z8_power_combination_eval
# LANG: hover_altitude --> _00z9
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01024__00z9 = (v0990_hover_altitude**5)
v01024__00z9 = (v01024__00z9*_00z8_coeff).reshape((1,))

# op _00zI_power_combination_eval
# LANG: hover_altitude --> _00zJ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01030__00zJ = (v0990_hover_altitude**2)
v01030__00zJ = (v01030__00zJ*_00zI_coeff).reshape((1,))

# op _00zU_power_combination_eval
# LANG: hover_altitude --> _00zV
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01032__00zV = (v0990_hover_altitude**1)
v01032__00zV = (v01032__00zV*_00zU_coeff).reshape((1,))

# op _00zk_power_combination_eval
# LANG: hover_altitude --> _00zl
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01026__00zl = (v0990_hover_altitude**4)
v01026__00zl = (v01026__00zl*_00zk_coeff).reshape((1,))

# op _00zw_power_combination_eval
# LANG: hover_altitude --> _00zx
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01028__00zx = (v0990_hover_altitude**3)
v01028__00zx = (v01028__00zx*_00zw_coeff).reshape((1,))

# op _013__log10_eval
# LANG: _013Z --> _0140
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01884__0140 = np.log10(v01883__013Z)

# op _00A7_power_combination_eval
# LANG: _00A6 --> _00A8
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01035__00A8 = (v01034__00A6**1)
v01035__00A8 = (v01035__00A8*_00A7_coeff).reshape((1,))

# op _00JD_cos_eval
# LANG: phi_distribution --> _00JE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01273__00JE = np.cos(v01196_phi_distribution)

# op _00JH_sin_eval
# LANG: phi_distribution --> _00JI
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01340__00JI = np.sin(v01196_phi_distribution)

# op _00LH_linear_combination_eval
# LANG: _00LG, _tangential_inflow_velocity --> _00LI
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01311__00LI = _00LH_constant+1*v01176__tangential_inflow_velocity+-1*v01312__00LG

# op _00LV_power_combination_eval
# LANG: _00LU --> _00LW
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01353__00LW = (v01352__00LU**1)
v01353__00LW = (v01353__00LW*_00LV_coeff).reshape((1, 40, 30))

# op _00LZ_power_combination_eval
# LANG: _ux_2 --> _00L_
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01356__00L_ = (v01237__ux_2**2)
v01356__00L_ = (v01356__00L_*_00LZ_coeff).reshape((1, 40, 30))

# op _00Lv_power_combination_eval
# LANG: _00Lu, _dr --> _local_torque
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01293__local_torque = (v01292__00Lu**1)*(v01147__dr**1)
v01293__local_torque = (v01293__local_torque*_00Lv_coeff).reshape((1, 40, 30))

# op _00Lx_power_combination_eval
# LANG: _00Js --> _00Ly
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01305__00Ly = (v01241__00Js**1)
v01305__00Ly = (v01305__00Ly*_00Lx_coeff).reshape((1, 40, 30))

# op _00M4_power_combination_eval
# LANG: _00M3 --> _00M5
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01360__00M5 = (v01358__00M3**2)
v01360__00M5 = (v01360__00M5*_00M4_coeff).reshape((1, 40, 30))

# op _00NB_power_combination_eval
# LANG: _ut --> _00NC
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01332__00NC = (v01256__ut**1)
v01332__00NC = (v01332__00NC*_00NB_coeff).reshape((1, 40, 30))

# op _00NV_power_combination_eval
# LANG: _ux, _tangential_inflow_velocity --> _00NW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01369__00NW = (v01176__tangential_inflow_velocity**1)*(v01224__ux**1)
v01369__00NW = (v01369__00NW*_00NV_coeff).reshape((1, 40, 30))

# op _00NZ_power_combination_eval
# LANG: _axial_inflow_velocity --> _00N_
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01372__00N_ = (v01166__axial_inflow_velocity**1)
v01372__00N_ = (v01372__00N_*_00NZ_coeff).reshape((1, 40, 30))

# op _00O0_power_combination_eval
# LANG: _ux --> _00O1
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01374__00O1 = (v01224__ux**2)
v01374__00O1 = (v01374__00O1*_00O0_coeff).reshape((1, 40, 30))

# op _00O6_power_combination_eval
# LANG: _axial_inflow_velocity --> _00O7
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01376__00O7 = (v01166__axial_inflow_velocity**2)
v01376__00O7 = (v01376__00O7*_00O6_coeff).reshape((1, 40, 30))

# op _00OO_single_tensor_sum_with_axis_eval
# LANG: _00J6 --> _00OP
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01398__00OP = np.sum(v01385__00J6, axis = (1, 2)).reshape((1,))

# op _00OY_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00OZ
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01403__00OZ = np.sum(v01146__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00RF_power_combination_eval
# LANG: _00RE --> rotor_disk_tonal_spl_A_weighted
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01477_rotor_disk_tonal_spl_A_weighted = (v01476__00RE**1)
v01477_rotor_disk_tonal_spl_A_weighted = (v01477_rotor_disk_tonal_spl_A_weighted*_00RF_coeff).reshape((1, 2))

# op _00bY_cos_eval
# LANG: phi_distribution --> _00bZ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0331__00bZ = np.cos(v0254_phi_distribution)

# op _00c1_sin_eval
# LANG: phi_distribution --> _00c2
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0398__00c2 = np.sin(v0254_phi_distribution)

# op _00dQ_power_combination_eval
# LANG: _00dP, _dr --> _local_torque
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0351__local_torque = (v0350__00dP**1)*(v0205__dr**1)
v0351__local_torque = (v0351__local_torque*_00dQ_coeff).reshape((1, 40, 100))

# op _00dS_power_combination_eval
# LANG: _00bN --> _00dT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0363__00dT = (v0299__00bN**1)
v0363__00dT = (v0363__00dT*_00dS_coeff).reshape((1, 40, 100))

# op _00e1_linear_combination_eval
# LANG: _00e0, _tangential_inflow_velocity --> _00e2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0369__00e2 = _00e1_constant+1*v0234__tangential_inflow_velocity+-1*v0370__00e0

# op _00ef_power_combination_eval
# LANG: _00ee --> _00eg
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0411__00eg = (v0410__00ee**1)
v0411__00eg = (v0411__00eg*_00ef_coeff).reshape((1, 40, 100))

# op _00ej_power_combination_eval
# LANG: _ux_2 --> _00ek
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0414__00ek = (v0295__ux_2**2)
v0414__00ek = (v0414__00ek*_00ej_coeff).reshape((1, 40, 100))

# op _00ep_power_combination_eval
# LANG: _00eo --> _00eq
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0418__00eq = (v0416__00eo**2)
v0418__00eq = (v0418__00eq*_00ep_coeff).reshape((1, 40, 100))

# op _00fW_power_combination_eval
# LANG: _ut --> _00fX
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0390__00fX = (v0314__ut**1)
v0390__00fX = (v0390__00fX*_00fW_coeff).reshape((1, 40, 100))

# op _00gf_power_combination_eval
# LANG: _ux, _tangential_inflow_velocity --> _00gg
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0427__00gg = (v0234__tangential_inflow_velocity**1)*(v0282__ux**1)
v0427__00gg = (v0427__00gg*_00gf_coeff).reshape((1, 40, 100))

# op _00gj_power_combination_eval
# LANG: _axial_inflow_velocity --> _00gk
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0430__00gk = (v0224__axial_inflow_velocity**1)
v0430__00gk = (v0430__00gk*_00gj_coeff).reshape((1, 40, 100))

# op _00gl_power_combination_eval
# LANG: _ux --> _00gm
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0432__00gm = (v0282__ux**2)
v0432__00gm = (v0432__00gm*_00gl_coeff).reshape((1, 40, 100))

# op _00gr_power_combination_eval
# LANG: _axial_inflow_velocity --> _00gs
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0434__00gs = (v0224__axial_inflow_velocity**2)
v0434__00gs = (v0434__00gs*_00gr_coeff).reshape((1, 40, 100))

# op _00h8_single_tensor_sum_with_axis_eval
# LANG: _00br --> _00h9
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0456__00h9 = np.sum(v0443__00br, axis = (1, 2)).reshape((1,))

# op _00hi_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00hj
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0461__00hj = np.sum(v0204__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00jW_linear_combination_eval
# LANG: _00jR, _00jV --> _00jX
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0528__00jX = _00jW_constant+1*v0527__00jR+-1*v0531__00jV

# op _00sU_power_combination_eval
# LANG: _00sT --> rotor_disk_tonal_spl
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0803_rotor_disk_tonal_spl = (v0802__00sT**1)
v0803_rotor_disk_tonal_spl = (v0803_rotor_disk_tonal_spl*_00sU_coeff).reshape((1, 2))

# op _00uH_linear_combination_eval
# LANG: _00uC, _00uG --> _00uI
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0851__00uI = _00uH_constant+1*v0850__00uC+-1*v0854__00uG

# op _00yY_power_combination_eval
# LANG: _00yX --> _00yZ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01022__00yZ = (v01021__00yX**1)
v01022__00yZ = (v01022__00yZ*_00yY_coeff).reshape((1,))

# op _00yf_linear_combination_eval
# LANG: _00xZ, _00ye --> rotor_disk_broadband_spl
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0953_rotor_disk_broadband_spl = _00yf_constant+1*v0952__00xZ+1*v0962__00ye

# op _00zK_power_combination_eval
# LANG: _00zJ --> _00zL
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01031__00zL = (v01030__00zJ**1)
v01031__00zL = (v01031__00zL*_00zK_coeff).reshape((1,))

# op _00zW_power_combination_eval
# LANG: _00zV --> _00zX
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01033__00zX = (v01032__00zV**1)
v01033__00zX = (v01033__00zX*_00zW_coeff).reshape((1,))

# op _00za_power_combination_eval
# LANG: _00z9 --> _00zb
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01025__00zb = (v01024__00z9**1)
v01025__00zb = (v01025__00zb*_00za_coeff).reshape((1,))

# op _00zm_power_combination_eval
# LANG: _00zl --> _00zn
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01027__00zn = (v01026__00zl**1)
v01027__00zn = (v01027__00zn*_00zm_coeff).reshape((1,))

# op _00zy_power_combination_eval
# LANG: _00zx --> _00zz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01029__00zz = (v01028__00zx**1)
v01029__00zz = (v01029__00zz*_00zy_coeff).reshape((1,))

# op _0141_power_combination_eval
# LANG: _0140 --> rotor_disk_broadband_spl_A_weighted
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01885_rotor_disk_broadband_spl_A_weighted = (v01884__0140**1)
v01885_rotor_disk_broadband_spl_A_weighted = (v01885_rotor_disk_broadband_spl_A_weighted*_0141_coeff).reshape((1, 2))

# op _00JF_power_combination_eval
# LANG: _00JE, Cl --> _00JG
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01272__00JG = (v01198_Cl**1)*(v01273__00JE**1)
v01272__00JG = (v01272__00JG*_00JF_coeff).reshape((1, 40, 30))

# op _00JJ_power_combination_eval
# LANG: _00JI, Cl --> _00JK
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01339__00JK = (v01198_Cl**1)*(v01340__00JI**1)
v01339__00JK = (v01339__00JK*_00JJ_coeff).reshape((1, 40, 30))

# op _00LD_power_combination_eval
# LANG: _ux_2 --> _00LE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01309__00LE = (v01237__ux_2**2)
v01309__00LE = (v01309__00LE*_00LD_coeff).reshape((1, 40, 30))

# op _00LJ_power_combination_eval
# LANG: _00LI --> _00LK
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01313__00LK = (v01311__00LI**2)
v01313__00LK = (v01313__00LK*_00LJ_coeff).reshape((1, 40, 30))

# op _00LX_power_combination_eval
# LANG: _00Je, _00LW --> _00LY
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01354__00LY = (v01353__00LW**1)*(v01265__00Je**1)
v01354__00LY = (v01354__00LY*_00LX_coeff).reshape((1, 40, 30))

# op _00Lz_power_combination_eval
# LANG: _00Ly --> _00LA
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01306__00LA = (v01305__00Ly**1)
v01306__00LA = (v01306__00LA*_00Lz_coeff).reshape((1, 40, 30))

# op _00M6_linear_combination_eval
# LANG: _00L_, _00M5 --> _00M7
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01357__00M7 = _00M6_constant+1*v01356__00L_+1*v01360__00M5

# op _00MK_power_combination_eval
# LANG: _ut --> _00ML
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01281__00ML = (v01256__ut**1)
v01281__00ML = (v01281__00ML*_00MK_coeff).reshape((1, 40, 30))

# op _00N5_power_combination_eval
# LANG: _ut --> _00N6
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01348__00N6 = (v01256__ut**1)
v01348__00N6 = (v01348__00N6*_00N5_coeff).reshape((1, 40, 30))

# op _00ND_linear_combination_eval
# LANG: _00NC, _tangential_inflow_velocity --> _00NE
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01331__00NE = _00ND_constant+1*v01176__tangential_inflow_velocity+-1*v01332__00NC

# op _00NX_power_combination_eval
# LANG: _ut, _00NW --> _00NY
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01370__00NY = (v01369__00NW**1)*(v01256__ut**1)
v01370__00NY = (v01370__00NY*_00NX_coeff).reshape((1, 40, 30))

# op _00Nv_single_tensor_sum_with_axis_eval
# LANG: _local_torque --> _00Nw
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01294__00Nw = np.sum(v01293__local_torque, axis = (1, 2)).reshape((1,))

# op _00Nz_power_combination_eval
# LANG: _00Je --> _00NA
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01329__00NA = (v01265__00Je**1)
v01329__00NA = (v01329__00NA*_00Nz_coeff).reshape((1, 40, 30))

# op _00O2_power_combination_eval
# LANG: _00N_, _00O1 --> _00O3
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01373__00O3 = (v01372__00N_**1)*(v01374__00O1**1)
v01373__00O3 = (v01373__00O3*_00O2_coeff).reshape((1, 40, 30))

# op _00O8_power_combination_eval
# LANG: _00O7 --> _00O9
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01377__00O9 = (v01376__00O7**1)
v01377__00O9 = (v01377__00O9*_00O8_coeff).reshape((1, 40, 30))

# op _00OQ_power_combination_eval
# LANG: _00OP --> _00OR
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01399__00OR = (v01398__00OP**1)
v01399__00OR = (v01399__00OR*_00OQ_coeff).reshape((1,))

# op _00O__power_combination_eval
# LANG: _00OZ --> _00P0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01404__00P0 = (v01403__00OZ**1)
v01404__00P0 = (v01404__00P0*_00O__coeff).reshape((1,))

# op _00Pb_power_combination_eval
# LANG: _00J6, _axial_inflow_velocity --> _00Pc
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01410__00Pc = (v01166__axial_inflow_velocity**1)*(v01385__00J6**-1)
v01410__00Pc = (v01410__00Pc*_00Pb_coeff).reshape((1, 40, 30))

# op _00Pd_power_combination_eval
# LANG: _rotor_radius --> _00Pe
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01412__00Pe = (v01146__rotor_radius**1)
v01412__00Pe = (v01412__00Pe*_00Pd_coeff).reshape((1, 40, 30))

# op _00b__power_combination_eval
# LANG: _00bZ, Cl --> _00c0
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0330__00c0 = (v0256_Cl**1)*(v0331__00bZ**1)
v0330__00c0 = (v0330__00c0*_00b__coeff).reshape((1, 40, 100))

# op _00c3_power_combination_eval
# LANG: _00c2, Cl --> _00c4
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0397__00c4 = (v0256_Cl**1)*(v0398__00c2**1)
v0397__00c4 = (v0397__00c4*_00c3_coeff).reshape((1, 40, 100))

# op _00dU_power_combination_eval
# LANG: _00dT --> _00dV
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0364__00dV = (v0363__00dT**1)
v0364__00dV = (v0364__00dV*_00dU_coeff).reshape((1, 40, 100))

# op _00dY_power_combination_eval
# LANG: _ux_2 --> _00dZ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0367__00dZ = (v0295__ux_2**2)
v0367__00dZ = (v0367__00dZ*_00dY_coeff).reshape((1, 40, 100))

# op _00e3_power_combination_eval
# LANG: _00e2 --> _00e4
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0371__00e4 = (v0369__00e2**2)
v0371__00e4 = (v0371__00e4*_00e3_coeff).reshape((1, 40, 100))

# op _00eh_power_combination_eval
# LANG: _00bz, _00eg --> _00ei
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0412__00ei = (v0411__00eg**1)*(v0323__00bz**1)
v0412__00ei = (v0412__00ei*_00eh_coeff).reshape((1, 40, 100))

# op _00er_linear_combination_eval
# LANG: _00ek, _00eq --> _00es
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0415__00es = _00er_constant+1*v0414__00ek+1*v0418__00eq

# op _00f4_power_combination_eval
# LANG: _ut --> _00f5
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0339__00f5 = (v0314__ut**1)
v0339__00f5 = (v0339__00f5*_00f4_coeff).reshape((1, 40, 100))

# op _00fQ_single_tensor_sum_with_axis_eval
# LANG: _local_torque --> _00fR
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0352__00fR = np.sum(v0351__local_torque, axis = (1, 2)).reshape((1,))

# op _00fU_power_combination_eval
# LANG: _00bz --> _00fV
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0387__00fV = (v0323__00bz**1)
v0387__00fV = (v0387__00fV*_00fU_coeff).reshape((1, 40, 100))

# op _00fY_linear_combination_eval
# LANG: _00fX, _tangential_inflow_velocity --> _00fZ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0389__00fZ = _00fY_constant+1*v0234__tangential_inflow_velocity+-1*v0390__00fX

# op _00fq_power_combination_eval
# LANG: _ut --> _00fr
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0406__00fr = (v0314__ut**1)
v0406__00fr = (v0406__00fr*_00fq_coeff).reshape((1, 40, 100))

# op _00gh_power_combination_eval
# LANG: _ut, _00gg --> _00gi
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0428__00gi = (v0427__00gg**1)*(v0314__ut**1)
v0428__00gi = (v0428__00gi*_00gh_coeff).reshape((1, 40, 100))

# op _00gn_power_combination_eval
# LANG: _00gk, _00gm --> _00go
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0431__00go = (v0430__00gk**1)*(v0432__00gm**1)
v0431__00go = (v0431__00go*_00gn_coeff).reshape((1, 40, 100))

# op _00gt_power_combination_eval
# LANG: _00gs --> _00gu
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0435__00gu = (v0434__00gs**1)
v0435__00gu = (v0435__00gu*_00gt_coeff).reshape((1, 40, 100))

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
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0468__00hx = (v0224__axial_inflow_velocity**1)*(v0443__00br**-1)
v0468__00hx = (v0468__00hx*_00hw_coeff).reshape((1, 40, 100))

# op _00hy_power_combination_eval
# LANG: _rotor_radius --> _00hz
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0470__00hz = (v0204__rotor_radius**1)
v0470__00hz = (v0470__00hz*_00hy_coeff).reshape((1, 40, 100))

# op _00jY reshape_eval
# LANG: _00jX --> _00jZ
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0532__00jZ = v0528__00jX.reshape((1,))

# op _00uJ reshape_eval
# LANG: _00uI --> _00uK
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0855__00uK = v0851__00uI.reshape((1,))

# op _00y__indexed_passthrough_eval
# LANG: _00yZ, _00zb, _00zn, _00zz, _00zL, _00zX, _00A8 --> temp_temperature
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01023_temp_temperature__temp[i_v01022__00yZ__00y__indexed_passthrough_eval] = v01022__00yZ.flatten()
v01023_temp_temperature = v01023_temp_temperature__temp.copy()
v01023_temp_temperature__temp[i_v01025__00zb__00y__indexed_passthrough_eval] = v01025__00zb.flatten()
v01023_temp_temperature = v01023_temp_temperature__temp.copy()
v01023_temp_temperature__temp[i_v01027__00zn__00y__indexed_passthrough_eval] = v01027__00zn.flatten()
v01023_temp_temperature = v01023_temp_temperature__temp.copy()
v01023_temp_temperature__temp[i_v01029__00zz__00y__indexed_passthrough_eval] = v01029__00zz.flatten()
v01023_temp_temperature = v01023_temp_temperature__temp.copy()
v01023_temp_temperature__temp[i_v01031__00zL__00y__indexed_passthrough_eval] = v01031__00zL.flatten()
v01023_temp_temperature = v01023_temp_temperature__temp.copy()
v01023_temp_temperature__temp[i_v01033__00zX__00y__indexed_passthrough_eval] = v01033__00zX.flatten()
v01023_temp_temperature = v01023_temp_temperature__temp.copy()
v01023_temp_temperature__temp[i_v01035__00A8__00y__indexed_passthrough_eval] = v01035__00A8.flatten()
v01023_temp_temperature = v01023_temp_temperature__temp.copy()

# op _00yk expand_array_eval
# LANG: rotor_disk_tonal_spl --> _00yl
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0963__00yl = np.einsum('bc,a->abc', v0803_rotor_disk_tonal_spl.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00yo expand_array_eval
# LANG: rotor_disk_broadband_spl --> _00yp
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0965__00yp = np.einsum('bc,a->abc', v0953_rotor_disk_broadband_spl.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _018A expand_array_eval
# LANG: rotor_disk_tonal_spl_A_weighted --> _018B
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02023__018B = np.einsum('bc,a->abc', v01477_rotor_disk_tonal_spl_A_weighted.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _018E expand_array_eval
# LANG: rotor_disk_broadband_spl_A_weighted --> _018F
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02025__018F = np.einsum('bc,a->abc', v01885_rotor_disk_broadband_spl_A_weighted.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _018i expand_array_eval
# LANG: rotor_disk_tonal_spl --> _018j
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02015__018j = np.einsum('bc,a->abc', v01814_rotor_disk_tonal_spl.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _018m expand_array_eval
# LANG: rotor_disk_broadband_spl --> _018n
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02017__018n = np.einsum('bc,a->abc', v02002_rotor_disk_broadband_spl.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _005e_decompose_eval
# LANG: T --> _005f
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0149__005f = ((v0344_T.flatten())[src_indices__005f__005e]).reshape((1,))

# op _00Ad single_tensor_sum_no_axis_eval
# LANG: temp_temperature --> hover_temperature
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01036_hover_temperature = np.sum(v01023_temp_temperature).reshape((1,))

# op _00CU_decompose_eval
# LANG: T --> _00CV
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01091__00CV = ((v01286_T.flatten())[src_indices__00CV__00CU]).reshape((1,))

# op _00LB_power_combination_eval
# LANG: _00Je, _00LA --> _00LC
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01307__00LC = (v01306__00LA**1)*(v01265__00Je**1)
v01307__00LC = (v01307__00LC*_00LB_coeff).reshape((1, 40, 30))

# op _00LL_linear_combination_eval
# LANG: _00LE, _00LK --> _00LM
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01310__00LM = _00LL_constant+1*v01309__00LE+1*v01313__00LK

# op _00M8_power_combination_eval
# LANG: _00LY, _00M7 --> _00M9
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01355__00M9 = (v01354__00LY**1)*(v01357__00M7**1)
v01355__00M9 = (v01355__00M9*_00M8_coeff).reshape((1, 40, 30))

# op _00MC_power_combination_eval
# LANG: _00JG --> _00MD
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01274__00MD = (v01272__00JG**1)
v01274__00MD = (v01274__00MD*_00MC_coeff).reshape((1, 40, 30))

# op _00MM_linear_combination_eval
# LANG: _00ML, _tangential_inflow_velocity --> _00MN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01280__00MN = _00MM_constant+1*v01176__tangential_inflow_velocity+-1*v01281__00ML

# op _00MY_power_combination_eval
# LANG: _00JK --> _00MZ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01341__00MZ = (v01339__00JK**1)
v01341__00MZ = (v01341__00MZ*_00MY_coeff).reshape((1, 40, 30))

# op _00N7_linear_combination_eval
# LANG: _00N6, _tangential_inflow_velocity --> _00N8
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01347__00N8 = _00N7_constant+1*v01176__tangential_inflow_velocity+-1*v01348__00N6

# op _00NF_power_combination_eval
# LANG: _00NA, _00NE --> _00NG
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01330__00NG = (v01329__00NA**1)*(v01331__00NE**1)
v01330__00NG = (v01330__00NG*_00NF_coeff).reshape((1, 40, 30))

# op _00NR_power_combination_eval
# LANG: _radius --> _00NS
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01366__00NS = (v01159__radius**1)
v01366__00NS = (v01366__00NS*_00NR_coeff).reshape((1, 40, 30))

# op _00Nx_power_combination_eval
# LANG: _00Nw --> total_torque
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01295_total_torque = (v01294__00Nw**1)
v01295_total_torque = (v01295_total_torque*_00Nx_coeff).reshape((1,))

# op _00O4_linear_combination_eval
# LANG: _00NY, _00O3 --> _00O5
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01371__00O5 = _00O4_constant+1*v01370__00NY+-1*v01373__00O3

# op _00OS_power_combination_eval
# LANG: _00OR --> _00OT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01400__00OT = (v01399__00OR**1)
v01400__00OT = (v01400__00OT*_00OS_coeff).reshape((1,))

# op _00Oa_power_combination_eval
# LANG: _ux, _00O9 --> _00Ob
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01378__00Ob = (v01377__00O9**1)*(v01224__ux**1)
v01378__00Ob = (v01378__00Ob*_00Oa_coeff).reshape((1, 40, 30))

# op _00P1_power_combination_eval
# LANG: _00P0 --> _00P2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01405__00P2 = (v01404__00P0**1)
v01405__00P2 = (v01405__00P2*_00P1_coeff).reshape((1,))

# op _00Pf_power_combination_eval
# LANG: _00Pc, _00Pe --> _00Pg
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01411__00Pg = (v01410__00Pc**1)*(v01412__00Pe**-1)
v01411__00Pg = (v01411__00Pg*_00Pf_coeff).reshape((1, 40, 30))

# op _00dW_power_combination_eval
# LANG: _00bz, _00dV --> _00dX
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0365__00dX = (v0364__00dV**1)*(v0323__00bz**1)
v0365__00dX = (v0365__00dX*_00dW_coeff).reshape((1, 40, 100))

# op _00e5_linear_combination_eval
# LANG: _00dZ, _00e4 --> _00e6
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0368__00e6 = _00e5_constant+1*v0367__00dZ+1*v0371__00e4

# op _00eX_power_combination_eval
# LANG: _00c0 --> _00eY
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0332__00eY = (v0330__00c0**1)
v0332__00eY = (v0332__00eY*_00eX_coeff).reshape((1, 40, 100))

# op _00et_power_combination_eval
# LANG: _00ei, _00es --> _00eu
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0413__00eu = (v0412__00ei**1)*(v0415__00es**1)
v0413__00eu = (v0413__00eu*_00et_coeff).reshape((1, 40, 100))

# op _00f6_linear_combination_eval
# LANG: _00f5, _tangential_inflow_velocity --> _00f7
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
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
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0388__00g0 = (v0387__00fV**1)*(v0389__00fZ**1)
v0388__00g0 = (v0388__00g0*_00f__coeff).reshape((1, 40, 100))

# op _00fi_power_combination_eval
# LANG: _00c4 --> _00fj
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0399__00fj = (v0397__00c4**1)
v0399__00fj = (v0399__00fj*_00fi_coeff).reshape((1, 40, 100))

# op _00fs_linear_combination_eval
# LANG: _00fr, _tangential_inflow_velocity --> _00ft
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0405__00ft = _00fs_constant+1*v0234__tangential_inflow_velocity+-1*v0406__00fr

# op _00gb_power_combination_eval
# LANG: _radius --> _00gc
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0424__00gc = (v0217__radius**1)
v0424__00gc = (v0424__00gc*_00gb_coeff).reshape((1, 40, 100))

# op _00gp_linear_combination_eval
# LANG: _00gi, _00go --> _00gq
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0429__00gq = _00gp_constant+1*v0428__00gi+-1*v0431__00go

# op _00gv_power_combination_eval
# LANG: _ux, _00gu --> _00gw
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0436__00gw = (v0435__00gu**1)*(v0282__ux**1)
v0436__00gw = (v0436__00gw*_00gv_coeff).reshape((1, 40, 100))

# op _00hA_power_combination_eval
# LANG: _00hx, _00hz --> _00hB
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0469__00hB = (v0468__00hx**1)*(v0470__00hz**-1)
v0469__00hB = (v0469__00hB*_00hA_coeff).reshape((1, 40, 100))

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
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0533__00k0 = np.empty((1, 2))
v0533__00k0.fill(v0532__00jZ.item())

# op _00m6 expand_array_eval
# LANG: thrust_dir --> _00m7
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0603__00m7 = np.einsum('b,ac->abc', v0494_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00uL expand_scalar_eval
# LANG: _00uK --> _00uM
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0856__00uM = np.empty((1, 2))
v0856__00uM.fill(v0855__00uK.item())

# op _00ym_indexed_passthrough_eval
# LANG: _00yl, _00yp --> noise_components
# SHAPES: (1, 1, 2), (1, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0964_noise_components__temp[i_v0963__00yl__00ym_indexed_passthrough_eval] = v0963__00yl.flatten()
v0964_noise_components = v0964_noise_components__temp.copy()
v0964_noise_components__temp[i_v0965__00yp__00ym_indexed_passthrough_eval] = v0965__00yp.flatten()
v0964_noise_components = v0964_noise_components__temp.copy()

# op _018C_indexed_passthrough_eval
# LANG: _018B, _018F --> A_weighted_noise_components
# SHAPES: (1, 1, 2), (1, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02024_A_weighted_noise_components__temp[i_v02023__018B__018C_indexed_passthrough_eval] = v02023__018B.flatten()
v02024_A_weighted_noise_components = v02024_A_weighted_noise_components__temp.copy()
v02024_A_weighted_noise_components__temp[i_v02025__018F__018C_indexed_passthrough_eval] = v02025__018F.flatten()
v02024_A_weighted_noise_components = v02024_A_weighted_noise_components__temp.copy()

# op _018k_indexed_passthrough_eval
# LANG: _018j, _018n --> noise_components
# SHAPES: (1, 1, 2), (1, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02016_noise_components__temp[i_v02015__018j__018k_indexed_passthrough_eval] = v02015__018j.flatten()
v02016_noise_components = v02016_noise_components__temp.copy()
v02016_noise_components__temp[i_v02017__018n__018k_indexed_passthrough_eval] = v02017__018n.flatten()
v02016_noise_components = v02016_noise_components__temp.copy()

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

# op _00Af_power_combination_eval
# LANG: hover_temperature --> _00Ag
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01039__00Ag = (v01036_hover_temperature**1)
v01039__00Ag = (v01039__00Ag*_00Af_coeff).reshape((1,))

# op _00BT_power_combination_eval
# LANG: rotor_disk_origin --> _00BU
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v01076__00BU = (v012_rotor_disk_origin**1)
v01076__00BU = (v01076__00BU*_00BT_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _00CW reshape_eval
# LANG: _00CV --> _00CX
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01092__00CX = v01091__00CV.reshape((1, 1))

# op _00CY_decompose_eval
# LANG: thrust_vector --> _00CZ, _00D4, _00D9
# SHAPES: (1, 3) --> (1, 1), (1, 1), (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01094__00CZ = ((v01075_thrust_vector.flatten())[src_indices__00CZ__00CY]).reshape((1, 1))
v01095__00D4 = ((v01075_thrust_vector.flatten())[src_indices__00D4__00CY]).reshape((1, 1))
v01096__00D9 = ((v01075_thrust_vector.flatten())[src_indices__00D9__00CY]).reshape((1, 1))

# op _00D2 reshape_eval
# LANG: _00CV --> _00D3
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01098__00D3 = v01091__00CV.reshape((1, 1))

# op _00D7 reshape_eval
# LANG: _00CV --> _00D8
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01100__00D8 = v01091__00CV.reshape((1, 1))

# op _00Go_power_combination_eval
# LANG: temperature --> _00Gp
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01194__00Gp = (v01182_temperature**1)
v01194__00Gp = (v01194__00Gp*_00Go_coeff).reshape((1, 1))

# op _00L5_power_combination_eval
# LANG: _angular_speed --> _00L6
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01299__00L6 = (v01158__angular_speed**1)
v01299__00L6 = (v01299__00L6*_00L5_coeff).reshape((1, 40, 30))

# op _00LN_power_combination_eval
# LANG: _00LC, _00LM --> _00LO
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01308__00LO = (v01307__00LC**1)*(v01310__00LM**1)
v01308__00LO = (v01308__00LO*_00LN_coeff).reshape((1, 40, 30))

# op _00ME_power_combination_eval
# LANG: _00MD --> _00MF
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01275__00MF = (v01274__00MD**1)
v01275__00MF = (v01275__00MF*_00ME_coeff).reshape((1, 40, 30))

# op _00MI_power_combination_eval
# LANG: _ux_2 --> _00MJ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01278__00MJ = (v01237__ux_2**2)
v01278__00MJ = (v01278__00MJ*_00MI_coeff).reshape((1, 40, 30))

# op _00MO_power_combination_eval
# LANG: _00MN --> _00MP
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01282__00MP = (v01280__00MN**2)
v01282__00MP = (v01282__00MP*_00MO_coeff).reshape((1, 40, 30))

# op _00M__power_combination_eval
# LANG: _00MZ --> _00N0
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01342__00N0 = (v01341__00MZ**1)
v01342__00N0 = (v01342__00N0*_00M__coeff).reshape((1, 40, 30))

# op _00Ma_power_combination_eval
# LANG: _00M9, _chord --> _00Mb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01361__00Mb = (v01355__00M9**1)*(v01154__chord**1)
v01361__00Mb = (v01361__00Mb*_00Ma_coeff).reshape((1, 40, 30))

# op _00N3_power_combination_eval
# LANG: _ux_2 --> _00N4
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01345__00N4 = (v01237__ux_2**2)
v01345__00N4 = (v01345__00N4*_00N3_coeff).reshape((1, 40, 30))

# op _00N9_power_combination_eval
# LANG: _00N8 --> _00Na
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01349__00Na = (v01347__00N8**2)
v01349__00Na = (v01349__00Na*_00N9_coeff).reshape((1, 40, 30))

# op _00NH_power_combination_eval
# LANG: _ut, _00NG --> _00NI
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01333__00NI = (v01330__00NG**1)*(v01256__ut**1)
v01333__00NI = (v01333__00NI*_00NH_coeff).reshape((1, 40, 30))

# op _00NT_power_combination_eval
# LANG: _00NS --> _00NU
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01367__00NU = (v01366__00NS**1)
v01367__00NU = (v01367__00NU*_00NT_coeff).reshape((1, 40, 30))

# op _00OM_power_combination_eval
# LANG: total_torque, density --> _00ON
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01187_density = v01187_density.reshape((1,))
v01396__00ON = (v01295_total_torque**1)*(v01187_density**-1)
v01396__00ON = (v01396__00ON*_00OM_coeff).reshape((1,))
v01187_density = v01187_density.reshape((1, 1))

# op _00OU_power_combination_eval
# LANG: _00OT --> _00OV
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01401__00OV = (v01400__00OT**2)
v01401__00OV = (v01401__00OV*_00OU_coeff).reshape((1,))

# op _00Oc_linear_combination_eval
# LANG: _00O5, _00Ob --> _00Od
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01375__00Od = _00Oc_constant+1*v01371__00O5+1*v01378__00Ob

# op _00P3_power_combination_eval
# LANG: _00P2 --> _00P4
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01406__00P4 = (v01405__00P2**1)
v01406__00P4 = (v01406__00P4*_00P3_coeff).reshape((1,))

# op _00Ph_single_tensor_sum_with_axis_eval
# LANG: _00Pg --> _00Pi
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01413__00Pi = np.sum(v01411__00Pg, axis = (1, 2)).reshape((1,))

# op _00R__power_combination_eval
# LANG: temperature --> _00S0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01487__00S0 = (v01481_temperature**1)
v01487__00S0 = (v01487__00S0*_00R__coeff).reshape((1,))

# op _00dq_power_combination_eval
# LANG: _angular_speed --> _00dr
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0357__00dr = (v0216__angular_speed**1)
v0357__00dr = (v0357__00dr*_00dq_coeff).reshape((1, 40, 100))

# op _00e7_power_combination_eval
# LANG: _00dX, _00e6 --> _00e8
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0366__00e8 = (v0365__00dX**1)*(v0368__00e6**1)
v0366__00e8 = (v0366__00e8*_00e7_coeff).reshape((1, 40, 100))

# op _00eZ_power_combination_eval
# LANG: _00eY --> _00e_
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0333__00e_ = (v0332__00eY**1)
v0333__00e_ = (v0333__00e_*_00eZ_coeff).reshape((1, 40, 100))

# op _00ev_power_combination_eval
# LANG: _00eu, _chord --> _00ew
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0419__00ew = (v0413__00eu**1)*(v0212__chord**1)
v0419__00ew = (v0419__00ew*_00ev_coeff).reshape((1, 40, 100))

# op _00f2_power_combination_eval
# LANG: _ux_2 --> _00f3
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0336__00f3 = (v0295__ux_2**2)
v0336__00f3 = (v0336__00f3*_00f2_coeff).reshape((1, 40, 100))

# op _00f8_power_combination_eval
# LANG: _00f7 --> _00f9
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0340__00f9 = (v0338__00f7**2)
v0340__00f9 = (v0340__00f9*_00f8_coeff).reshape((1, 40, 100))

# op _00fk_power_combination_eval
# LANG: _00fj --> _00fl
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0400__00fl = (v0399__00fj**1)
v0400__00fl = (v0400__00fl*_00fk_coeff).reshape((1, 40, 100))

# op _00fo_power_combination_eval
# LANG: _ux_2 --> _00fp
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0403__00fp = (v0295__ux_2**2)
v0403__00fp = (v0403__00fp*_00fo_coeff).reshape((1, 40, 100))

# op _00fu_power_combination_eval
# LANG: _00ft --> _00fv
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0407__00fv = (v0405__00ft**2)
v0407__00fv = (v0407__00fv*_00fu_coeff).reshape((1, 40, 100))

# op _00g1_power_combination_eval
# LANG: _ut, _00g0 --> _00g2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0391__00g2 = (v0388__00g0**1)*(v0314__ut**1)
v0391__00g2 = (v0391__00g2*_00g1_coeff).reshape((1, 40, 100))

# op _00gd_power_combination_eval
# LANG: _00gc --> _00ge
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0425__00ge = (v0424__00gc**1)
v0425__00ge = (v0425__00ge*_00gd_coeff).reshape((1, 40, 100))

# op _00gx_linear_combination_eval
# LANG: _00gq, _00gw --> _00gy
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
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
# SHAPES: (1, 40, 100) --> (1,)
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
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0507__00k2 = _00k1_constant+1*v0803_rotor_disk_tonal_spl+1*v0533__00k0

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
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0602_normal_proj = np.sum(v0595_rel_obs_position * v0603__00m7, axis=1)

# op _00uN_linear_combination_eval
# LANG: _00uM, rotor_disk_broadband_spl --> _00uO
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0830__00uO = _00uN_constant+1*v0953_rotor_disk_broadband_spl+1*v0856__00uM

# op _00yq_power_combination_eval
# LANG: noise_components --> _00yr
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0966__00yr = (v0964_noise_components**1)
v0966__00yr = (v0966__00yr*_00yq_coeff).reshape((2, 1, 2))

# op _018G_power_combination_eval
# LANG: A_weighted_noise_components --> _018H
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02026__018H = (v02024_A_weighted_noise_components**1)
v02026__018H = (v02026__018H*_018G_coeff).reshape((2, 1, 2))

# op _018o_power_combination_eval
# LANG: noise_components --> _018p
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02018__018p = (v02016_noise_components**1)
v02018__018p = (v02018__018p*_018o_coeff).reshape((2, 1, 2))

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

# op _00A1_power_combination_eval
# LANG: hover_altitude --> _00A2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01019__00A2 = (v0990_hover_altitude**0)
v01019__00A2 = (v01019__00A2*_00A1_coeff).reshape((1,))

# op _00Ah_power_combination_eval
# LANG: _00Ag --> _00Ai
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01040__00Ai = (v01039__00Ag**1.5)
v01040__00Ai = (v01040__00Ai*_00Ah_coeff).reshape((1,))

# op _00C__power_combination_eval
# LANG: _00CX, _00CZ --> _00D0
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01093__00D0 = (v01092__00CX**1)*(v01094__00CZ**1)
v01093__00D0 = (v01093__00D0*_00C__coeff).reshape((1, 1))

# op _00Ca expand_array_eval
# LANG: _00BU --> thrust_origin
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01077_thrust_origin = np.einsum('b,a->ab', v01076__00BU.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

# op _00D5_power_combination_eval
# LANG: _00D4, _00D3 --> _00D6
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01099__00D6 = (v01098__00D3**1)*(v01095__00D4**1)
v01099__00D6 = (v01099__00D6*_00D5_coeff).reshape((1, 1))

# op _00Da_power_combination_eval
# LANG: _00D9, _00D8 --> _00Db
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01101__00Db = (v01100__00D8**1)*(v01096__00D9**1)
v01101__00Db = (v01101__00Db*_00Da_coeff).reshape((1, 1))

# op _00Gq_power_combination_eval
# LANG: _00Gp --> speed_of_sound
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01195_speed_of_sound = (v01194__00Gp**0.5)
v01195_speed_of_sound = (v01195_speed_of_sound*_00Gq_coeff).reshape((1, 1))

# op _00L7_power_combination_eval
# LANG: _00L6 --> _00L8
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01300__00L8 = (v01299__00L6**1)
v01300__00L8 = (v01300__00L8*_00L7_coeff).reshape((1, 40, 30))

# op _00LP_power_combination_eval
# LANG: _00LO, _chord --> _00LQ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01314__00LQ = (v01308__00LO**1)*(v01154__chord**1)
v01314__00LQ = (v01314__00LQ*_00LP_coeff).reshape((1, 40, 30))

# op _00MG_power_combination_eval
# LANG: _00Je, _00MF --> _00MH
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01276__00MH = (v01275__00MF**1)*(v01265__00Je**1)
v01276__00MH = (v01276__00MH*_00MG_coeff).reshape((1, 40, 30))

# op _00MQ_linear_combination_eval
# LANG: _00MJ, _00MP --> _00MR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01279__00MR = _00MQ_constant+1*v01278__00MJ+1*v01282__00MP

# op _00Mc_power_combination_eval
# LANG: _00Mb, _dr --> _00Md
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01362__00Md = (v01361__00Mb**1)*(v01147__dr**1)
v01362__00Md = (v01362__00Md*_00Mc_coeff).reshape((1, 40, 30))

# op _00N1_power_combination_eval
# LANG: _00Je, _00N0 --> _00N2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01343__00N2 = (v01342__00N0**1)*(v01265__00Je**1)
v01343__00N2 = (v01343__00N2*_00N1_coeff).reshape((1, 40, 30))

# op _00NJ_power_combination_eval
# LANG: _00NI, _radius --> _00NK
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01334__00NK = (v01333__00NI**1)*(v01159__radius**1)
v01334__00NK = (v01334__00NK*_00NJ_coeff).reshape((1, 40, 30))

# op _00Nb_linear_combination_eval
# LANG: _00N4, _00Na --> _00Nc
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01346__00Nc = _00Nb_constant+1*v01345__00N4+1*v01349__00Na

# op _00OW_power_combination_eval
# LANG: _00ON, _00OV --> _00OX
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01397__00OX = (v01396__00ON**1)*(v01401__00OV**-1)
v01397__00OX = (v01397__00OX*_00OW_coeff).reshape((1,))

# op _00Oe_power_combination_eval
# LANG: _00NU, _00Od --> _00Of
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01368__00Of = (v01367__00NU**1)*(v01375__00Od**1)
v01368__00Of = (v01368__00Of*_00Oe_coeff).reshape((1, 40, 30))

# op _00P5_power_combination_eval
# LANG: _00P4 --> _00P6
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01407__00P6 = (v01406__00P4**5)
v01407__00P6 = (v01407__00P6*_00P5_coeff).reshape((1,))

# op _00Pj_power_combination_eval
# LANG: _00Pi --> _00Pk
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01414__00Pk = (v01413__00Pi**1)
v01414__00Pk = (v01414__00Pk*_00Pj_coeff).reshape((1,))

# op _00Pr_power_combination_eval
# LANG: C_T --> _00Ps
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01418__00Ps = (v01390_C_T**1)
v01418__00Ps = (v01418__00Ps*_00Pr_coeff).reshape((1,))

# op _00S1_power_combination_eval
# LANG: _00S0 --> _00S2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01488__00S2 = (v01487__00S0**1.5)
v01488__00S2 = (v01488__00S2*_00S1_coeff).reshape((1,))

# op _00TK expand_array_eval
# LANG: normal_proj --> _00TL
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01544__00TL = np.einsum('ac,b->abc', v01542_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00T__power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00U0
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01552__00U0 = (v01533_rel_obs_z_pos**1)*(v01541_rel_obs_dist**-1)
v01552__00U0 = (v01552__00U0*_00T__coeff).reshape((1, 1, 2))

# op _00U7_linear_combination_eval
# LANG: rel_obs_z_pos --> _00U8
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01557__00U8 = _00U7_constant+1*v01533_rel_obs_z_pos

# op _00ds_power_combination_eval
# LANG: _00dr --> _00dt
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0358__00dt = (v0357__00dr**1)
v0358__00dt = (v0358__00dt*_00ds_coeff).reshape((1, 40, 100))

# op _00e9_power_combination_eval
# LANG: _00e8, _chord --> _00ea
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0372__00ea = (v0366__00e8**1)*(v0212__chord**1)
v0372__00ea = (v0372__00ea*_00e9_coeff).reshape((1, 40, 100))

# op _00ex_power_combination_eval
# LANG: _00ew, _dr --> _00ey
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0420__00ey = (v0419__00ew**1)*(v0205__dr**1)
v0420__00ey = (v0420__00ey*_00ex_coeff).reshape((1, 40, 100))

# op _00f0_power_combination_eval
# LANG: _00bz, _00e_ --> _00f1
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0334__00f1 = (v0333__00e_**1)*(v0323__00bz**1)
v0334__00f1 = (v0334__00f1*_00f0_coeff).reshape((1, 40, 100))

# op _00fa_linear_combination_eval
# LANG: _00f3, _00f9 --> _00fb
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0337__00fb = _00fa_constant+1*v0336__00f3+1*v0340__00f9

# op _00fm_power_combination_eval
# LANG: _00bz, _00fl --> _00fn
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0401__00fn = (v0400__00fl**1)*(v0323__00bz**1)
v0401__00fn = (v0401__00fn*_00fm_coeff).reshape((1, 40, 100))

# op _00fw_linear_combination_eval
# LANG: _00fp, _00fv --> _00fx
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0404__00fx = _00fw_constant+1*v0403__00fp+1*v0407__00fv

# op _00g3_power_combination_eval
# LANG: _00g2, _radius --> _00g4
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0392__00g4 = (v0391__00g2**1)*(v0217__radius**1)
v0392__00g4 = (v0392__00g4*_00g3_coeff).reshape((1, 40, 100))

# op _00gz_power_combination_eval
# LANG: _00ge, _00gy --> _00gA
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0426__00gA = (v0425__00ge**1)*(v0433__00gy**1)
v0426__00gA = (v0426__00gA*_00gz_coeff).reshape((1, 40, 100))

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
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0534__00k4 = (v0507__00k2**1)
v0534__00k4 = (v0534__00k4*_00k3_coeff).reshape((1, 2))

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
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0617__00mD = _00mC_constant+1*v0593_rel_obs_z_pos

# op _00me expand_array_eval
# LANG: normal_proj --> _00mf
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0604__00mf = np.einsum('ac,b->abc', v0602_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00mk expand_array_eval
# LANG: normal_proj --> _00ml
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0608__00ml = np.einsum('ac,b->abc', v0602_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00mu_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00mv
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0612__00mv = (v0593_rel_obs_z_pos**1)*(v0601_rel_obs_dist**-1)
v0612__00mv = (v0612__00mv*_00mu_coeff).reshape((1, 1, 2))

# op _00uP_power_combination_eval
# LANG: _00uO --> _00uQ
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0857__00uQ = (v0830__00uO**1)
v0857__00uQ = (v0857__00uQ*_00uP_coeff).reshape((1, 2))

# op _00wH_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00wI
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0918__00wI = (v0899_rel_obs_z_pos**1)*(v0907_rel_obs_dist**-1)
v0918__00wI = (v0918__00wI*_00wH_coeff).reshape((1, 1, 2))

# op _00wP_linear_combination_eval
# LANG: rel_obs_z_pos --> _00wQ
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0923__00wQ = _00wP_constant+1*v0899_rel_obs_z_pos

# op _00wx expand_array_eval
# LANG: normal_proj --> _00wy
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0914__00wy = np.einsum('ac,b->abc', v0908_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00yM_power_combination_eval
# LANG: hover_altitude --> _00yN
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0991__00yN = (v0990_hover_altitude**6)
v0991__00yN = (v0991__00yN*_00yM_coeff).reshape((1,))

# op _00yR_power_combination_eval
# LANG: hover_altitude --> _00yS
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01006__00yS = (v0990_hover_altitude**6)
v01006__00yS = (v01006__00yS*_00yR_coeff).reshape((1,))

# op _00ys_exp_a_eval
# LANG: _00yr --> _00yt
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0967__00yt = _00ys_exp_a_eval_a**v0966__00yr

# op _00z0_power_combination_eval
# LANG: hover_altitude --> _00z1
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0994__00z1 = (v0990_hover_altitude**5)
v0994__00z1 = (v0994__00z1*_00z0_coeff).reshape((1,))

# op _00z4_power_combination_eval
# LANG: hover_altitude --> _00z5
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01009__00z5 = (v0990_hover_altitude**5)
v01009__00z5 = (v01009__00z5*_00z4_coeff).reshape((1,))

# op _00zA_power_combination_eval
# LANG: hover_altitude --> _00zB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01000__00zB = (v0990_hover_altitude**2)
v01000__00zB = (v01000__00zB*_00zA_coeff).reshape((1,))

# op _00zE_power_combination_eval
# LANG: hover_altitude --> _00zF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01015__00zF = (v0990_hover_altitude**2)
v01015__00zF = (v01015__00zF*_00zE_coeff).reshape((1,))

# op _00zM_power_combination_eval
# LANG: hover_altitude --> _00zN
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01002__00zN = (v0990_hover_altitude**1)
v01002__00zN = (v01002__00zN*_00zM_coeff).reshape((1,))

# op _00zQ_power_combination_eval
# LANG: hover_altitude --> _00zR
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01017__00zR = (v0990_hover_altitude**1)
v01017__00zR = (v01017__00zR*_00zQ_coeff).reshape((1,))

# op _00zY_power_combination_eval
# LANG: hover_altitude --> _00zZ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01004__00zZ = (v0990_hover_altitude**0)
v01004__00zZ = (v01004__00zZ*_00zY_coeff).reshape((1,))

# op _00zc_power_combination_eval
# LANG: hover_altitude --> _00zd
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0996__00zd = (v0990_hover_altitude**4)
v0996__00zd = (v0996__00zd*_00zc_coeff).reshape((1,))

# op _00zg_power_combination_eval
# LANG: hover_altitude --> _00zh
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01011__00zh = (v0990_hover_altitude**4)
v01011__00zh = (v01011__00zh*_00zg_coeff).reshape((1,))

# op _00zo_power_combination_eval
# LANG: hover_altitude --> _00zp
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0998__00zp = (v0990_hover_altitude**3)
v0998__00zp = (v0998__00zp*_00zo_coeff).reshape((1,))

# op _00zs_power_combination_eval
# LANG: hover_altitude --> _00zt
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01013__00zt = (v0990_hover_altitude**3)
v01013__00zt = (v01013__00zt*_00zs_coeff).reshape((1,))

# op _015E expand_array_eval
# LANG: normal_proj --> _015F
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01939__015F = np.einsum('ac,b->abc', v01933_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _015O_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _015P
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01943__015P = (v01924_rel_obs_z_pos**1)*(v01932_rel_obs_dist**-1)
v01943__015P = (v01943__015P*_015O_coeff).reshape((1, 1, 2))

# op _015W_linear_combination_eval
# LANG: rel_obs_z_pos --> _015X
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01948__015X = _015W_constant+1*v01924_rel_obs_z_pos

# op _018I_exp_a_eval
# LANG: _018H --> _018J
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02027__018J = _018I_exp_a_eval_a**v02026__018H

# op _018q_exp_a_eval
# LANG: _018p --> _018r
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02019__018r = _018q_exp_a_eval_a**v02018__018p

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
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0253_speed_of_sound = v0253_speed_of_sound.reshape((1,))
v0146__004U = np.empty((1, 40, 100))
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

# op _00A3_power_combination_eval
# LANG: _00A2 --> _00A4
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01020__00A4 = (v01019__00A2**1)
v01020__00A4 = (v01020__00A4*_00A3_coeff).reshape((1,))

# op _00Aj_power_combination_eval
# LANG: _00Ai --> _00Ak
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01041__00Ak = (v01040__00Ai**1)
v01041__00Ak = (v01041__00Ak*_00Aj_coeff).reshape((1,))

# op _00Cy expand_scalar_eval
# LANG: speed_of_sound --> _00Cz
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01195_speed_of_sound = v01195_speed_of_sound.reshape((1,))
v01088__00Cz = np.empty((1, 40, 30))
v01088__00Cz.fill(v01195_speed_of_sound.item())
v01195_speed_of_sound = v01195_speed_of_sound.reshape((1, 1))

# op _00D1_indexed_passthrough_eval
# LANG: _00D0, _00D6, _00Db --> F
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01097_F__temp[i_v01093__00D0__00D1_indexed_passthrough_eval] = v01093__00D0.flatten()
v01097_F = v01097_F__temp.copy()
v01097_F__temp[i_v01099__00D6__00D1_indexed_passthrough_eval] = v01099__00D6.flatten()
v01097_F = v01097_F__temp.copy()
v01097_F__temp[i_v01101__00Db__00D1_indexed_passthrough_eval] = v01101__00Db.flatten()
v01097_F = v01097_F__temp.copy()

# op _00Dc_linear_combination_eval
# LANG: thrust_origin, reference_point --> _00Dd
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01102__00Dd = _00Dc_constant+1*v01077_thrust_origin+-1*v01103_reference_point

# op _00L3_power_combination_eval
# LANG: _00Je, _local_thrust --> _00L4
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01297__00L4 = (v01270__local_thrust**1)*(v01265__00Je**-1)
v01297__00L4 = (v01297__00L4*_00L3_coeff).reshape((1, 40, 30))

# op _00L9_power_combination_eval
# LANG: _00L8 --> _00La
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01301__00La = (v01300__00L8**2)
v01301__00La = (v01301__00La*_00L9_coeff).reshape((1, 40, 30))

# op _00LR_power_combination_eval
# LANG: _00LQ, _dr --> _local_thrust_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01315__local_thrust_2 = (v01314__00LQ**1)*(v01147__dr**1)
v01315__local_thrust_2 = (v01315__local_thrust_2*_00LR_coeff).reshape((1, 40, 30))

# op _00Ld_power_combination_eval
# LANG: _rotor_radius --> _00Le
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01303__00Le = (v01146__rotor_radius**1)
v01303__00Le = (v01303__00Le*_00Ld_coeff).reshape((1, 40, 30))

# op _00MS_power_combination_eval
# LANG: _00MH, _00MR --> _00MT
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01277__00MT = (v01276__00MH**1)*(v01279__00MR**1)
v01277__00MT = (v01277__00MT*_00MS_coeff).reshape((1, 40, 30))

# op _00Me_power_combination_eval
# LANG: _00Md, _radius --> _local_torque_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01363__local_torque_2 = (v01362__00Md**1)*(v01159__radius**1)
v01363__local_torque_2 = (v01363__local_torque_2*_00Me_coeff).reshape((1, 40, 30))

# op _00NL_power_combination_eval
# LANG: _00NK, _dr --> _local_thrust_star
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01335__local_thrust_star = (v01334__00NK**1)*(v01147__dr**1)
v01335__local_thrust_star = (v01335__local_thrust_star*_00NL_coeff).reshape((1, 40, 30))

# op _00Nd_power_combination_eval
# LANG: _00N2, _00Nc --> _00Ne
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01344__00Ne = (v01343__00N2**1)*(v01346__00Nc**1)
v01344__00Ne = (v01344__00Ne*_00Nd_coeff).reshape((1, 40, 30))

# op _00Og_power_combination_eval
# LANG: _00Of, prandtl_loss_factor --> _00Oh
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01379__00Oh = (v01368__00Of**1)*(v01209_prandtl_loss_factor**1)
v01379__00Oh = (v01379__00Oh*_00Og_coeff).reshape((1, 40, 30))

# op _00P7_power_combination_eval
# LANG: _00OX, _00P6 --> C_Q
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01402_C_Q = (v01397__00OX**1)*(v01407__00P6**-1)
v01402_C_Q = (v01402_C_Q*_00P7_coeff).reshape((1,))

# op _00Pl_power_combination_eval
# LANG: _00Pk --> J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01415_J = (v01414__00Pk**1)
v01415_J = (v01415_J*_00Pl_coeff).reshape((1,))

# op _00Pt_power_combination_eval
# LANG: _00Ps --> _00Pu
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01419__00Pu = (v01418__00Ps**0.5)
v01419__00Pu = (v01419__00Pu*_00Pt_coeff).reshape((1,))

# op _00S3_power_combination_eval
# LANG: _00S2 --> _00S4
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01489__00S4 = (v01488__00S2**1)
v01489__00S4 = (v01489__00S4*_00S3_coeff).reshape((1,))

# op _00TM_power_combination_eval
# LANG: rel_obs_dist, _00TL --> _00TN
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01545__00TN = (v01544__00TL**1)*(v01541_rel_obs_dist**-1)
v01545__00TN = (v01545__00TN*_00TM_coeff).reshape((1, 1, 2))

# op _00U1 arccos_eval
# LANG: _00U0 --> _00U2
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01553__00U2 = np.arccos(v01552__00U0)

# op _00U3_linear_combination_eval
# LANG: rel_obs_z_pos --> _00U4
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01555__00U4 = _00U3_constant+1*v01533_rel_obs_z_pos

# op _00U9_power_combination_eval
# LANG: _00U8 --> _00Ua
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01558__00Ua = (v01557__00U8**2)
v01558__00Ua = (v01558__00Ua*_00U9_coeff).reshape((1, 1, 2))

# op _00do_power_combination_eval
# LANG: _00bz, _local_thrust --> _00dp
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0355__00dp = (v0328__local_thrust**1)*(v0323__00bz**-1)
v0355__00dp = (v0355__00dp*_00do_coeff).reshape((1, 40, 100))

# op _00du_power_combination_eval
# LANG: _00dt --> _00dv
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0359__00dv = (v0358__00dt**2)
v0359__00dv = (v0359__00dv*_00du_coeff).reshape((1, 40, 100))

# op _00dy_power_combination_eval
# LANG: _rotor_radius --> _00dz
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0361__00dz = (v0204__rotor_radius**1)
v0361__00dz = (v0361__00dz*_00dy_coeff).reshape((1, 40, 100))

# op _00eb_power_combination_eval
# LANG: _00ea, _dr --> _local_thrust_2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0373__local_thrust_2 = (v0372__00ea**1)*(v0205__dr**1)
v0373__local_thrust_2 = (v0373__local_thrust_2*_00eb_coeff).reshape((1, 40, 100))

# op _00ez_power_combination_eval
# LANG: _00ey, _radius --> _local_torque_2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0421__local_torque_2 = (v0420__00ey**1)*(v0217__radius**1)
v0421__local_torque_2 = (v0421__local_torque_2*_00ez_coeff).reshape((1, 40, 100))

# op _00fc_power_combination_eval
# LANG: _00f1, _00fb --> _00fd
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0335__00fd = (v0334__00f1**1)*(v0337__00fb**1)
v0335__00fd = (v0335__00fd*_00fc_coeff).reshape((1, 40, 100))

# op _00fy_power_combination_eval
# LANG: _00fn, _00fx --> _00fz
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0402__00fz = (v0401__00fn**1)*(v0404__00fx**1)
v0402__00fz = (v0402__00fz*_00fy_coeff).reshape((1, 40, 100))

# op _00g5_power_combination_eval
# LANG: _00g4, _dr --> _local_thrust_star
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0393__local_thrust_star = (v0392__00g4**1)*(v0205__dr**1)
v0393__local_thrust_star = (v0393__local_thrust_star*_00g5_coeff).reshape((1, 40, 100))

# op _00gB_power_combination_eval
# LANG: _00gA, prandtl_loss_factor --> _00gC
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0437__00gC = (v0426__00gA**1)*(v0267_prandtl_loss_factor**1)
v0437__00gC = (v0437__00gC*_00gB_coeff).reshape((1, 40, 100))

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
# SHAPES: (1, 2) --> (1, 2)
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
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0618__00mF = (v0617__00mD**2)
v0618__00mF = (v0618__00mF*_00mE_coeff).reshape((1, 1, 2))

# op _00mg_power_combination_eval
# LANG: rel_obs_dist, _00mf --> _00mh
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0605__00mh = (v0604__00mf**1)*(v0601_rel_obs_dist**-1)
v0605__00mh = (v0605__00mh*_00mg_coeff).reshape((1, 1, 2))

# op _00mm_power_combination_eval
# LANG: rel_obs_dist, _00ml --> _00mn
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0609__00mn = (v0608__00ml**1)*(v0601_rel_obs_dist**-1)
v0609__00mn = (v0609__00mn*_00mm_coeff).reshape((1, 1, 2))

# op _00mw arccos_eval
# LANG: _00mv --> _00mx
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0613__00mx = np.arccos(v0612__00mv)

# op _00my_linear_combination_eval
# LANG: rel_obs_z_pos --> _00mz
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0615__00mz = _00my_constant+1*v0593_rel_obs_z_pos

# op _00uR_exp_a_eval
# LANG: _00uQ --> _00uS
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0858__00uS = _00uR_exp_a_eval_a**v0857__00uQ

# op _00wJ arccos_eval
# LANG: _00wI --> _00wK
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0919__00wK = np.arccos(v0918__00wI)

# op _00wL_linear_combination_eval
# LANG: rel_obs_z_pos --> _00wM
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0921__00wM = _00wL_constant+1*v0899_rel_obs_z_pos

# op _00wR_power_combination_eval
# LANG: _00wQ --> _00wS
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0924__00wS = (v0923__00wQ**2)
v0924__00wS = (v0924__00wS*_00wR_coeff).reshape((1, 1, 2))

# op _00wz_power_combination_eval
# LANG: rel_obs_dist, _00wy --> _00wA
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0915__00wA = (v0914__00wy**1)*(v0907_rel_obs_dist**-1)
v0915__00wA = (v0915__00wA*_00wz_coeff).reshape((1, 1, 2))

# op _00yO_power_combination_eval
# LANG: _00yN --> _00yP
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0992__00yP = (v0991__00yN**1)
v0992__00yP = (v0992__00yP*_00yO_coeff).reshape((1,))

# op _00yT_power_combination_eval
# LANG: _00yS --> _00yU
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01007__00yU = (v01006__00yS**1)
v01007__00yU = (v01007__00yU*_00yT_coeff).reshape((1,))

# op _00yu_single_tensor_sum_with_axis_eval
# LANG: _00yt --> _00yv
# SHAPES: (2, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0968__00yv = np.sum(v0967__00yt, axis = (0,)).reshape((1, 2))

# op _00z2_power_combination_eval
# LANG: _00z1 --> _00z3
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0995__00z3 = (v0994__00z1**1)
v0995__00z3 = (v0995__00z3*_00z2_coeff).reshape((1,))

# op _00z6_power_combination_eval
# LANG: _00z5 --> _00z7
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01010__00z7 = (v01009__00z5**1)
v01010__00z7 = (v01010__00z7*_00z6_coeff).reshape((1,))

# op _00zC_power_combination_eval
# LANG: _00zB --> _00zD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01001__00zD = (v01000__00zB**1)
v01001__00zD = (v01001__00zD*_00zC_coeff).reshape((1,))

# op _00zG_power_combination_eval
# LANG: _00zF --> _00zH
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01016__00zH = (v01015__00zF**1)
v01016__00zH = (v01016__00zH*_00zG_coeff).reshape((1,))

# op _00zO_power_combination_eval
# LANG: _00zN --> _00zP
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01003__00zP = (v01002__00zN**1)
v01003__00zP = (v01003__00zP*_00zO_coeff).reshape((1,))

# op _00zS_power_combination_eval
# LANG: _00zR --> _00zT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01018__00zT = (v01017__00zR**1)
v01018__00zT = (v01018__00zT*_00zS_coeff).reshape((1,))

# op _00z__power_combination_eval
# LANG: _00zZ --> _00A0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01005__00A0 = (v01004__00zZ**1)
v01005__00A0 = (v01005__00A0*_00z__coeff).reshape((1,))

# op _00ze_power_combination_eval
# LANG: _00zd --> _00zf
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0997__00zf = (v0996__00zd**1)
v0997__00zf = (v0997__00zf*_00ze_coeff).reshape((1,))

# op _00zi_power_combination_eval
# LANG: _00zh --> _00zj
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01012__00zj = (v01011__00zh**1)
v01012__00zj = (v01012__00zj*_00zi_coeff).reshape((1,))

# op _00zq_power_combination_eval
# LANG: _00zp --> _00zr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0999__00zr = (v0998__00zp**1)
v0999__00zr = (v0999__00zr*_00zq_coeff).reshape((1,))

# op _00zu_power_combination_eval
# LANG: _00zt --> _00zv
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01014__00zv = (v01013__00zt**1)
v01014__00zv = (v01014__00zv*_00zu_coeff).reshape((1,))

# op _015G_power_combination_eval
# LANG: rel_obs_dist, _015F --> _015H
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01940__015H = (v01939__015F**1)*(v01932_rel_obs_dist**-1)
v01940__015H = (v01940__015H*_015G_coeff).reshape((1, 1, 2))

# op _015Q arccos_eval
# LANG: _015P --> _015R
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01944__015R = np.arccos(v01943__015P)

# op _015S_linear_combination_eval
# LANG: rel_obs_z_pos --> _015T
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01946__015T = _015S_constant+1*v01924_rel_obs_z_pos

# op _015Y_power_combination_eval
# LANG: _015X --> _015Z
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01949__015Z = (v01948__015X**2)
v01949__015Z = (v01949__015Z*_015Y_coeff).reshape((1, 1, 2))

# op _018K_single_tensor_sum_with_axis_eval
# LANG: _018J --> _018L
# SHAPES: (2, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02028__018L = np.sum(v02027__018J, axis = (0,)).reshape((1, 2))

# op _018s_single_tensor_sum_with_axis_eval
# LANG: _018r --> _018t
# SHAPES: (2, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02020__018t = np.sum(v02019__018r, axis = (0,)).reshape((1, 2))

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
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0145_mach_number = (v0141__004L**1)*(v0146__004U**-1)
v0145_mach_number = (v0145_mach_number*_0050_coeff).reshape((1, 40, 100))

# op _005z cross_product_eval
# LANG: F, _005y --> _005A
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0162__005A = np.cross(v0160__005y, v0155_F, axisa = 1, axisb = 1, axisc = 1)

# op _00AG_power_combination_eval
# LANG: _00Ax --> p
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0980_p = (v0974__00Ax**1)
v0980_p = (v0980_p*_00AG_coeff).reshape((1,))

# op _00AI_power_combination_eval
# LANG: _00Ax --> q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0981_q = (v0974__00Ax**1)
v0981_q = (v0981_q*_00AI_coeff).reshape((1,))

# op _00AK_power_combination_eval
# LANG: _00Ax --> r
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0982_r = (v0974__00Ax**1)
v0982_r = (v0982_r*_00AK_coeff).reshape((1,))

# op _00Al_power_combination_eval
# LANG: _00Ak --> _00Am
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01042__00Am = (v01041__00Ak**1)
v01042__00Am = (v01042__00Am*_00Al_coeff).reshape((1,))

# op _00An_linear_combination_eval
# LANG: hover_temperature --> _00Ao
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01044__00Ao = _00An_constant+1*v01036_hover_temperature

# op _00Ar_power_combination_eval
# LANG: hover_temperature --> _00As
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01045__00As = (v01036_hover_temperature**1)
v01045__00As = (v01045__00As*_00Ar_coeff).reshape((1,))

# op _00CG_power_combination_eval
# LANG: _00Cq, _00Cz --> mach_number
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01087_mach_number = (v01083__00Cq**1)*(v01088__00Cz**-1)
v01087_mach_number = (v01087_mach_number*_00CG_coeff).reshape((1, 40, 30))

# op _00De cross_product_eval
# LANG: F, _00Dd --> _00Df
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01104__00Df = np.cross(v01102__00Dd, v01097_F, axisa = 1, axisb = 1, axisc = 1)

# op _00Lb_power_combination_eval
# LANG: _00L4, _00La --> _00Lc
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01298__00Lc = (v01297__00L4**1)*(v01301__00La**-1)
v01298__00Lc = (v01298__00Lc*_00Lb_coeff).reshape((1, 40, 30))

# op _00Lf_power_combination_eval
# LANG: _00Le --> _00Lg
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01304__00Lg = (v01303__00Le**4)
v01304__00Lg = (v01304__00Lg*_00Lf_coeff).reshape((1, 40, 30))

# op _00MU_power_combination_eval
# LANG: _00MT, _chord --> _00MV
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01283__00MV = (v01277__00MT**1)*(v01154__chord**1)
v01283__00MV = (v01283__00MV*_00MU_coeff).reshape((1, 40, 30))

# op _00NN_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_star --> _00NO
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01336__00NO = np.sum(v01335__local_thrust_star, axis = (1, 2)).reshape((1,))

# op _00Nf_power_combination_eval
# LANG: _00Ne, _chord --> _00Ng
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01350__00Ng = (v01344__00Ne**1)*(v01154__chord**1)
v01350__00Ng = (v01350__00Ng*_00Nf_coeff).reshape((1, 40, 30))

# op _00Nj_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_2 --> _00Nk
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01316__00Nk = np.sum(v01315__local_thrust_2, axis = (1, 2)).reshape((1,))

# op _00Nn_single_tensor_sum_with_axis_eval
# LANG: _local_torque_2 --> _00No
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01364__00No = np.sum(v01363__local_torque_2, axis = (1, 2)).reshape((1,))

# op _00Oi_power_combination_eval
# LANG: _00Oh, _dr --> _local_energy_loss
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01380__local_energy_loss = (v01379__00Oh**1)*(v01147__dr**1)
v01380__local_energy_loss = (v01380__local_energy_loss*_00Oi_coeff).reshape((1, 40, 30))

# op _00P9_power_combination_eval
# LANG: C_Q --> C_P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01408_C_P = (v01402_C_Q**1)
v01408_C_P = (v01408_C_P*_00P9_coeff).reshape((1,))

# op _00Pn_power_combination_eval
# LANG: C_T, J --> _00Po
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01409__00Po = (v01390_C_T**1)*(v01415_J**1)
v01409__00Po = (v01409__00Po*_00Pn_coeff).reshape((1,))

# op _00Pv_power_combination_eval
# LANG: C_T, _00Pu --> _00Pw
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01417__00Pw = (v01390_C_T**1)*(v01419__00Pu**1)
v01417__00Pw = (v01417__00Pw*_00Pv_coeff).reshape((1,))

# op _00S5_power_combination_eval
# LANG: _00S4 --> _00S6
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01490__00S6 = (v01489__00S4**1)
v01490__00S6 = (v01490__00S6*_00S5_coeff).reshape((1,))

# op _00S7_linear_combination_eval
# LANG: temperature --> _00S8
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01492__00S8 = _00S7_constant+1*v01481_temperature

# op _00TO_arcsin_eval
# LANG: _00TN --> _00TP
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01546__00TP = np.arcsin(v01545__00TN)

# op _00U5_power_combination_eval
# LANG: _00U2, _00U4 --> _00U6
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01554__00U6 = (v01553__00U2**1)*(v01555__00U4**1)
v01554__00U6 = (v01554__00U6*_00U5_coeff).reshape((1, 1, 2))

# op _00Ub_power_combination_eval
# LANG: _00Ua --> _00Uc
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01559__00Uc = (v01558__00Ua**0.5)
v01559__00Uc = (v01559__00Uc*_00Ub_coeff).reshape((1, 1, 2))

# op _00dA_power_combination_eval
# LANG: _00dz --> _00dB
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0362__00dB = (v0361__00dz**4)
v0362__00dB = (v0362__00dB*_00dA_coeff).reshape((1, 40, 100))

# op _00dw_power_combination_eval
# LANG: _00dp, _00dv --> _00dx
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0356__00dx = (v0355__00dp**1)*(v0359__00dv**-1)
v0356__00dx = (v0356__00dx*_00dw_coeff).reshape((1, 40, 100))

# op _00fA_power_combination_eval
# LANG: _00fz, _chord --> _00fB
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0408__00fB = (v0402__00fz**1)*(v0212__chord**1)
v0408__00fB = (v0408__00fB*_00fA_coeff).reshape((1, 40, 100))

# op _00fE_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_2 --> _00fF
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0374__00fF = np.sum(v0373__local_thrust_2, axis = (1, 2)).reshape((1,))

# op _00fI_single_tensor_sum_with_axis_eval
# LANG: _local_torque_2 --> _00fJ
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0422__00fJ = np.sum(v0421__local_torque_2, axis = (1, 2)).reshape((1,))

# op _00fe_power_combination_eval
# LANG: _00fd, _chord --> _00ff
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0341__00ff = (v0335__00fd**1)*(v0212__chord**1)
v0341__00ff = (v0341__00ff*_00fe_coeff).reshape((1, 40, 100))

# op _00g7_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_star --> _00g8
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0394__00g8 = np.sum(v0393__local_thrust_star, axis = (1, 2)).reshape((1,))

# op _00gD_power_combination_eval
# LANG: _00gC, _dr --> _local_energy_loss
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0438__local_energy_loss = (v0437__00gC**1)*(v0205__dr**1)
v0438__local_energy_loss = (v0438__local_energy_loss*_00gD_coeff).reshape((1, 40, 100))

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
# SHAPES: (1, 2) --> (1, 2)
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
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0614__00mB = (v0613__00mx**1)*(v0615__00mz**1)
v0614__00mB = (v0614__00mB*_00mA_coeff).reshape((1, 1, 2))

# op _00mG_power_combination_eval
# LANG: _00mF --> _00mH
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0619__00mH = (v0618__00mF**0.5)
v0619__00mH = (v0619__00mH*_00mG_coeff).reshape((1, 1, 2))

# op _00mi_arcsin_eval
# LANG: _00mh --> _00mj
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0606__00mj = np.arcsin(v0605__00mh)

# op _00mo arccos_eval
# LANG: _00mn --> _00mp
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0610__00mp = np.arccos(v0609__00mn)

# op _00uT_log10_eval
# LANG: _00uS --> _00uU
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0859__00uU = np.log10(v0858__00uS)

# op _00wB arccos_eval
# LANG: _00wA --> _00wC
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0916__00wC = np.arccos(v0915__00wA)

# op _00wN_power_combination_eval
# LANG: _00wK, _00wM --> _00wO
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0920__00wO = (v0919__00wK**1)*(v0921__00wM**1)
v0920__00wO = (v0920__00wO*_00wN_coeff).reshape((1, 1, 2))

# op _00wT_power_combination_eval
# LANG: _00wS --> _00wU
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0925__00wU = (v0924__00wS**0.5)
v0925__00wU = (v0925__00wU*_00wT_coeff).reshape((1, 1, 2))

# op _00yQ_indexed_passthrough_eval
# LANG: _00yP, _00z3, _00zf, _00zr, _00zD, _00zP, _00A0 --> temp_density
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0993_temp_density__temp[i_v0992__00yP__00yQ_indexed_passthrough_eval] = v0992__00yP.flatten()
v0993_temp_density = v0993_temp_density__temp.copy()
v0993_temp_density__temp[i_v0995__00z3__00yQ_indexed_passthrough_eval] = v0995__00z3.flatten()
v0993_temp_density = v0993_temp_density__temp.copy()
v0993_temp_density__temp[i_v0997__00zf__00yQ_indexed_passthrough_eval] = v0997__00zf.flatten()
v0993_temp_density = v0993_temp_density__temp.copy()
v0993_temp_density__temp[i_v0999__00zr__00yQ_indexed_passthrough_eval] = v0999__00zr.flatten()
v0993_temp_density = v0993_temp_density__temp.copy()
v0993_temp_density__temp[i_v01001__00zD__00yQ_indexed_passthrough_eval] = v01001__00zD.flatten()
v0993_temp_density = v0993_temp_density__temp.copy()
v0993_temp_density__temp[i_v01003__00zP__00yQ_indexed_passthrough_eval] = v01003__00zP.flatten()
v0993_temp_density = v0993_temp_density__temp.copy()
v0993_temp_density__temp[i_v01005__00A0__00yQ_indexed_passthrough_eval] = v01005__00A0.flatten()
v0993_temp_density = v0993_temp_density__temp.copy()

# op _00yV_indexed_passthrough_eval
# LANG: _00yU, _00z7, _00zj, _00zv, _00zH, _00zT, _00A4 --> temp_pressure
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01008_temp_pressure__temp[i_v01007__00yU__00yV_indexed_passthrough_eval] = v01007__00yU.flatten()
v01008_temp_pressure = v01008_temp_pressure__temp.copy()
v01008_temp_pressure__temp[i_v01010__00z7__00yV_indexed_passthrough_eval] = v01010__00z7.flatten()
v01008_temp_pressure = v01008_temp_pressure__temp.copy()
v01008_temp_pressure__temp[i_v01012__00zj__00yV_indexed_passthrough_eval] = v01012__00zj.flatten()
v01008_temp_pressure = v01008_temp_pressure__temp.copy()
v01008_temp_pressure__temp[i_v01014__00zv__00yV_indexed_passthrough_eval] = v01014__00zv.flatten()
v01008_temp_pressure = v01008_temp_pressure__temp.copy()
v01008_temp_pressure__temp[i_v01016__00zH__00yV_indexed_passthrough_eval] = v01016__00zH.flatten()
v01008_temp_pressure = v01008_temp_pressure__temp.copy()
v01008_temp_pressure__temp[i_v01018__00zT__00yV_indexed_passthrough_eval] = v01018__00zT.flatten()
v01008_temp_pressure = v01008_temp_pressure__temp.copy()
v01008_temp_pressure__temp[i_v01020__00A4__00yV_indexed_passthrough_eval] = v01020__00A4.flatten()
v01008_temp_pressure = v01008_temp_pressure__temp.copy()

# op _00yw_log10_eval
# LANG: _00yv --> _00yx
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0969__00yx = np.log10(v0968__00yv)

# op _015I arccos_eval
# LANG: _015H --> _015J
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01941__015J = np.arccos(v01940__015H)

# op _015U_power_combination_eval
# LANG: _015R, _015T --> _015V
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01945__015V = (v01944__015R**1)*(v01946__015T**1)
v01945__015V = (v01945__015V*_015U_coeff).reshape((1, 1, 2))

# op _015__power_combination_eval
# LANG: _015Z --> _0160
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01950__0160 = (v01949__015Z**0.5)
v01950__0160 = (v01950__0160*_015__coeff).reshape((1, 1, 2))

# op _018M_log10_eval
# LANG: _018L --> _018N
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02029__018N = np.log10(v02028__018L)

# op _018u_log10_eval
# LANG: _018t --> _018v
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02021__018v = np.log10(v02020__018t)

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
# SHAPES: (1, 40, 100) --> (4000, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0147_Re_ml_input = v0143_Re.reshape((4000, 1))

# op _0054 reshape_eval
# LANG: mach_number --> mach_number_ml_input
# SHAPES: (1, 40, 100) --> (4000, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0148_mach_number_ml_input = v0145_mach_number.reshape((4000, 1))

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

# op _00A9 single_tensor_sum_no_axis_eval
# LANG: temp_density --> hover_density
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01038_hover_density = np.sum(v0993_temp_density).reshape((1,))

# op _00AM_power_combination_eval
# LANG: _00Ax --> phi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0983_phi = (v0974__00Ax**1)
v0983_phi = (v0983_phi*_00AM_coeff).reshape((1,))

# op _00AO_power_combination_eval
# LANG: _00Ax --> gamma
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0984_gamma = (v0974__00Ax**1)
v0984_gamma = (v0984_gamma*_00AO_coeff).reshape((1,))

# op _00AQ_power_combination_eval
# LANG: _00Ax --> psi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0985_psi = (v0974__00Ax**1)
v0985_psi = (v0985_psi*_00AQ_coeff).reshape((1,))

# op _00AU_power_combination_eval
# LANG: _00Ax --> x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0987_x = (v0974__00Ax**1)
v0987_x = (v0987_x*_00AU_coeff).reshape((1,))

# op _00AW_power_combination_eval
# LANG: _00Ay --> y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0988_y = (v0975__00Ay**1)
v0988_y = (v0988_y*_00AW_coeff).reshape((1,))

# op _00AY_power_combination_eval
# LANG: _00Az --> z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0989_z = (v0976__00Az**1)
v0989_z = (v0989_z*_00AY_coeff).reshape((1,))

# op _00Ab single_tensor_sum_no_axis_eval
# LANG: temp_pressure --> hover_pressure
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01037_hover_pressure = np.sum(v01008_temp_pressure).reshape((1,))

# op _00Ap_power_combination_eval
# LANG: _00Am, _00Ao --> hover_dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01043_hover_dynamic_viscosity = (v01042__00Am**1)*(v01044__00Ao**-1)
v01043_hover_dynamic_viscosity = (v01043_hover_dynamic_viscosity*_00Ap_coeff).reshape((1,))

# op _00At_power_combination_eval
# LANG: _00As --> hover_speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01046_hover_speed_of_sound = (v01045__00As**0.5)
v01046_hover_speed_of_sound = (v01046_hover_speed_of_sound*_00At_coeff).reshape((1,))

# op _00CI reshape_eval
# LANG: Re --> Re_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01089_Re_ml_input = v01085_Re.reshape((1200, 1))

# op _00CK reshape_eval
# LANG: mach_number --> mach_number_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01090_mach_number_ml_input = v01087_mach_number.reshape((1200, 1))

# op _00Dg_transpose_eval
# LANG: _00Df --> M
# SHAPES: (1, 3) --> (3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01105_M = np.transpose(v01104__00Df)

# op _00Ds_power_combination_eval
# LANG: p --> p1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0980_p = v0980_p.reshape((1, 1))
v01113_p1 = (v0980_p**1)
v01113_p1 = (v01113_p1*_00Ds_coeff).reshape((1, 1))
v0980_p = v0980_p.reshape((1,))

# op _00Dv_power_combination_eval
# LANG: q --> q1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0981_q = v0981_q.reshape((1, 1))
v01114_q1 = (v0981_q**1)
v01114_q1 = (v01114_q1*_00Dv_coeff).reshape((1, 1))
v0981_q = v0981_q.reshape((1,))

# op _00Dy_power_combination_eval
# LANG: r --> r1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0982_r = v0982_r.reshape((1, 1))
v01115_r1 = (v0982_r**1)
v01115_r1 = (v01115_r1*_00Dy_coeff).reshape((1, 1))
v0982_r = v0982_r.reshape((1,))

# op _00Lh_power_combination_eval
# LANG: _00Lc, _00Lg --> dC_T
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01302_dC_T = (v01298__00Lc**1)*(v01304__00Lg**-1)
v01302_dC_T = (v01302_dC_T*_00Lh_coeff).reshape((1, 40, 30))

# op _00MW_power_combination_eval
# LANG: _00MV, _dr --> _local_thrust_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01284__local_thrust_induced = (v01283__00MV**1)*(v01147__dr**1)
v01284__local_thrust_induced = (v01284__local_thrust_induced*_00MW_coeff).reshape((1, 40, 30))

# op _00NP_power_combination_eval
# LANG: _00NO --> total_thrust_star
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01337_total_thrust_star = (v01336__00NO**1)
v01337_total_thrust_star = (v01337_total_thrust_star*_00NP_coeff).reshape((1,))

# op _00Nh_power_combination_eval
# LANG: _00Ng, _dr --> _local_torque_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01351__local_torque_induced = (v01350__00Ng**1)*(v01147__dr**1)
v01351__local_torque_induced = (v01351__local_torque_induced*_00Nh_coeff).reshape((1, 40, 30))

# op _00Nl_power_combination_eval
# LANG: _00Nk --> total_thrust_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01317_total_thrust_2 = (v01316__00Nk**1)
v01317_total_thrust_2 = (v01317_total_thrust_2*_00Nl_coeff).reshape((1,))

# op _00Np_power_combination_eval
# LANG: _00No --> total_torque_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01365_total_torque_2 = (v01364__00No**1)
v01365_total_torque_2 = (v01365_total_torque_2*_00Np_coeff).reshape((1,))

# op _00Ok_single_tensor_sum_with_axis_eval
# LANG: _local_energy_loss --> total_energy_loss
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01381_total_energy_loss = np.sum(v01380__local_energy_loss, axis = (1, 2)).reshape((1,))

# op _00PB_power_combination_eval
# LANG: total_torque --> Q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01296_Q = (v01295_total_torque**1)
v01296_Q = (v01296_Q*_00PB_coeff).reshape((1,))

# op _00PD_power_combination_eval
# LANG: _local_torque --> _dQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01338__dQ = (v01293__local_torque**1)
v01338__dQ = (v01338__dQ*_00PD_coeff).reshape((1, 40, 30))

# op _00Pp_power_combination_eval
# LANG: C_P, _00Po --> eta
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01416_eta = (v01409__00Po**1)*(v01408_C_P**-1)
v01416_eta = (v01416_eta*_00Pp_coeff).reshape((1,))

# op _00Px_power_combination_eval
# LANG: C_P, _00Pw --> FOM
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01420_FOM = (v01417__00Pw**1)*(v01408_C_P**-1)
v01420_FOM = (v01420_FOM*_00Px_coeff).reshape((1,))

# op _00S9_power_combination_eval
# LANG: _00S6, _00S8 --> dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01491_dynamic_viscosity = (v01490__00S6**1)*(v01492__00S8**-1)
v01491_dynamic_viscosity = (v01491_dynamic_viscosity*_00S9_coeff).reshape((1,))

# op _00TW reshape_eval
# LANG: _00TP --> rel_angle_plane
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01547_rel_angle_plane = v01546__00TP.reshape((1, 2))

# op _00Ud_power_combination_eval
# LANG: _00U6, _00Uc --> rel_obs_angle
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01556_rel_obs_angle = (v01554__00U6**1)*(v01559__00Uc**-1)
v01556_rel_obs_angle = (v01556_rel_obs_angle*_00Ud_coeff).reshape((1, 1, 2))

# op _00dC_power_combination_eval
# LANG: _00dx, _00dB --> dC_T
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0360_dC_T = (v0356__00dx**1)*(v0362__00dB**-1)
v0360_dC_T = (v0360_dC_T*_00dC_coeff).reshape((1, 40, 100))

# op _00fC_power_combination_eval
# LANG: _00fB, _dr --> _local_torque_induced
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0409__local_torque_induced = (v0408__00fB**1)*(v0205__dr**1)
v0409__local_torque_induced = (v0409__local_torque_induced*_00fC_coeff).reshape((1, 40, 100))

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
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0342__local_thrust_induced = (v0341__00ff**1)*(v0205__dr**1)
v0342__local_thrust_induced = (v0342__local_thrust_induced*_00fg_coeff).reshape((1, 40, 100))

# op _00g9_power_combination_eval
# LANG: _00g8 --> total_thrust_star
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0395_total_thrust_star = (v0394__00g8**1)
v0395_total_thrust_star = (v0395_total_thrust_star*_00g9_coeff).reshape((1,))

# op _00gF_single_tensor_sum_with_axis_eval
# LANG: _local_energy_loss --> total_energy_loss
# SHAPES: (1, 40, 100) --> (1,)
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
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0396__dQ = (v0351__local_torque**1)
v0396__dQ = (v0396__dQ*_00hY_coeff).reshape((1, 40, 100))

# op _00j7_power_combination_eval
# LANG: _00j6, speed_of_sound --> mach_number
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0506_mach_number = (v0505__00j6**1)*(v0554_speed_of_sound**-1)
v0506_mach_number = (v0506_mach_number*_00j7_coeff).reshape((1,))

# op _00k9_power_combination_eval
# LANG: _00k8 --> rotor_disk_tonal_spl_A_weighted
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0537_rotor_disk_tonal_spl_A_weighted = (v0536__00k8**1)
v0537_rotor_disk_tonal_spl_A_weighted = (v0537_rotor_disk_tonal_spl_A_weighted*_00k9_coeff).reshape((1, 2))

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
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0616_rel_obs_angle = (v0614__00mB**1)*(v0619__00mH**-1)
v0616_rel_obs_angle = (v0616_rel_obs_angle*_00mI_coeff).reshape((1, 1, 2))

# op _00mq reshape_eval
# LANG: _00mj --> rel_angle_plane
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0607_rel_angle_plane = v0606__00mj.reshape((1, 2))

# op _00ms reshape_eval
# LANG: _00mp --> rel_angle_normal
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0611_rel_angle_normal = v0610__00mp.reshape((1, 2))

# op _00uV_power_combination_eval
# LANG: _00uU --> rotor_disk_broadband_spl_A_weighted
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0860_rotor_disk_broadband_spl_A_weighted = (v0859__00uU**1)
v0860_rotor_disk_broadband_spl_A_weighted = (v0860_rotor_disk_broadband_spl_A_weighted*_00uV_coeff).reshape((1, 2))

# op _00wF reshape_eval
# LANG: _00wC --> rel_angle_normal
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0917_rel_angle_normal = v0916__00wC.reshape((1, 2))

# op _00wV_power_combination_eval
# LANG: _00wO, _00wU --> rel_obs_angle
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0922_rel_obs_angle = (v0920__00wO**1)*(v0925__00wU**-1)
v0922_rel_obs_angle = (v0922_rel_obs_angle*_00wV_coeff).reshape((1, 1, 2))

# op _00yG_power_combination_eval
# LANG: hover_hover_time --> hover_time
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0973_hover_time = (v0971_hover_hover_time**1)
v0973_hover_time = (v0973_hover_time*_00yG_coeff).reshape((1,))

# op _00yy_power_combination_eval
# LANG: _00yx --> total_spl
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0970_total_spl = (v0969__00yx**1)
v0970_total_spl = (v0970_total_spl*_00yy_coeff).reshape((1, 2))

# op _015M reshape_eval
# LANG: _015J --> rel_angle_normal
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01942_rel_angle_normal = v01941__015J.reshape((1, 2))

# op _0161_power_combination_eval
# LANG: _015V, _0160 --> rel_obs_angle
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01947_rel_obs_angle = (v01945__015V**1)*(v01950__0160**-1)
v01947_rel_obs_angle = (v01947_rel_obs_angle*_0161_coeff).reshape((1, 1, 2))

# op _018O_power_combination_eval
# LANG: _018N --> A_weighted_total_spl
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02030_A_weighted_total_spl = (v02029__018N**1)
v02030_A_weighted_total_spl = (v02030_A_weighted_total_spl*_018O_coeff).reshape((1, 2))

# op _018w_power_combination_eval
# LANG: _018v --> total_spl
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02022_total_spl = (v02021__018v**1)
v02022_total_spl = (v02022_total_spl*_018w_coeff).reshape((1, 2))