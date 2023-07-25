

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

# op _00A4_decompose_eval
# LANG: hover_observer_location --> _00A5, _00A6, _00A7
# SHAPES: (3,) --> (1,), (1,), (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0958__00A5 = ((v0956_hover_observer_location.flatten())[src_indices__00A5__00A4]).reshape((1,))
v0959__00A6 = ((v0956_hover_observer_location.flatten())[src_indices__00A6__00A4]).reshape((1,))
v0960__00A7 = ((v0956_hover_observer_location.flatten())[src_indices__00A7__00A4]).reshape((1,))

# op _00Bl_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00Bm
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v01050__00Bm = (v08_rotor_disk_in_plane_1**1)
v01050__00Bm = (v01050__00Bm*_00Bl_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _00Bo_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _00Bp
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v01054__00Bp = (v010_rotor_disk_in_plane_2**1)
v01054__00Bp = (v01054__00Bp*_00Bo_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _00Aq_power_combination_eval
# LANG: _00A5 --> theta
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0970_theta = (v0958__00A5**1)
v0970_theta = (v0970_theta*_00Aq_coeff).reshape((1,))

# op _00Bx cross_product_eval
# LANG: _00Bm, _00Bp --> _00By
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01055__00By = np.cross(v01054__00Bp, v01050__00Bm, axisa = 0, axisb = 0, axisc = 0)

# op _00AL_sin_eval
# LANG: theta --> _00AM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0970_theta = v0970_theta.reshape((1, 1))
v01033__00AM = np.sin(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _00AP_linear_combination_eval
# LANG: theta --> _00AQ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0970_theta = v0970_theta.reshape((1, 1))
v01035__00AQ = _00AP_constant+1*v0970_theta
v0970_theta = v0970_theta.reshape((1,))

# op _00AR_linear_combination_eval
# LANG: theta --> _00AS
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0970_theta = v0970_theta.reshape((1, 1))
v01037__00AS = _00AR_constant+1*v0970_theta
v0970_theta = v0970_theta.reshape((1,))

# op _00AV_sin_eval
# LANG: theta --> _00AW
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0970_theta = v0970_theta.reshape((1, 1))
v01038__00AW = np.sin(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _00AZ_cos_eval
# LANG: theta --> _00A_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0970_theta = v0970_theta.reshape((1, 1))
v01040__00A_ = np.cos(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _00Bz pnorm_eval
# LANG: _00By --> _00BA
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01057__00BA = np.linalg.norm(v01055__00By.flatten(), ord=2)

# op _00AI_cos_eval
# LANG: theta --> _00AJ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v0970_theta = v0970_theta.reshape((1, 1))
v01031__00AJ = np.cos(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _00AN_power_combination_eval
# LANG: _00AM --> _00AO
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01034__00AO = (v01033__00AM**1)
v01034__00AO = (v01034__00AO*_00AN_coeff).reshape((1, 1))

# op _00AT_power_combination_eval
# LANG: _00AQ, _00AS --> _00AU
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01036__00AU = (v01035__00AQ**1)*(v01037__00AS**-1)
v01036__00AU = (v01036__00AU*_00AT_coeff).reshape((1, 1))

# op _00AX_power_combination_eval
# LANG: _00AW --> _00AY
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01039__00AY = (v01038__00AW**1)
v01039__00AY = (v01039__00AY*_00AX_coeff).reshape((1, 1))

# op _00B0_power_combination_eval
# LANG: _00A_ --> _00B1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01041__00B1 = (v01040__00A_**1)
v01041__00B1 = (v01041__00B1*_00B0_coeff).reshape((1, 1))

# op _00BB expand_scalar_eval
# LANG: _00BA --> _00BC
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01058__00BC = np.empty((3,))
v01058__00BC.fill(v01057__00BA.item())

# op _00AK_indexed_passthrough_eval
# LANG: _00AJ, _00AO, _00AU, _00AY, _00B1 --> rotation_matrix
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01032_rotation_matrix__temp[i_v01031__00AJ__00AK_indexed_passthrough_eval] = v01031__00AJ.flatten()
v01032_rotation_matrix = v01032_rotation_matrix__temp.copy()
v01032_rotation_matrix__temp[i_v01034__00AO__00AK_indexed_passthrough_eval] = v01034__00AO.flatten()
v01032_rotation_matrix = v01032_rotation_matrix__temp.copy()
v01032_rotation_matrix__temp[i_v01036__00AU__00AK_indexed_passthrough_eval] = v01036__00AU.flatten()
v01032_rotation_matrix = v01032_rotation_matrix__temp.copy()
v01032_rotation_matrix__temp[i_v01039__00AY__00AK_indexed_passthrough_eval] = v01039__00AY.flatten()
v01032_rotation_matrix = v01032_rotation_matrix__temp.copy()
v01032_rotation_matrix__temp[i_v01041__00B1__00AK_indexed_passthrough_eval] = v01041__00B1.flatten()
v01032_rotation_matrix = v01032_rotation_matrix__temp.copy()

# op _00BD_power_combination_eval
# LANG: _00By, _00BC --> _00BE
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01056__00BE = (v01055__00By**1)*(v01058__00BC**-1)
v01056__00BE = (v01056__00BE*_00BD_coeff).reshape((3,))

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

# op _00BF_matvec_eval
# LANG: rotation_matrix, _00BE --> _00BG
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01053__00BG = v01032_rotation_matrix@v01056__00BE

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

# op _00BH expand_array_eval
# LANG: _00BG --> thrust_vector
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01059_thrust_vector = np.einsum('b,a->ab', v01053__00BG.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

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

# op _00Dj_decompose_eval
# LANG: thrust_vector --> _00Dk
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01102__00Dk = ((v01059_thrust_vector.flatten())[src_indices__00Dk__00Dj]).reshape((1, 3))

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

# op _00Dn_tensor_dot_product_eval
# LANG: projection_vector, _00Dk --> _00Do
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01109__00Do = np.sum(v01091_projection_vector * v01102__00Dk, axis=1)

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

# op _00Dp expand_scalar_eval
# LANG: _00Do --> _00Dq
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01110__00Dq = np.empty((1, 3))
v01110__00Dq.fill(v01109__00Do.item())

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

# op _00Dr_power_combination_eval
# LANG: _00Dk, _00Dq --> _00Ds
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01111__00Ds = (v01110__00Dq**1)*(v01102__00Dk**1)
v01111__00Ds = (v01111__00Ds*_00Dr_coeff).reshape((1, 3))

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

# op _00A8_power_combination_eval
# LANG: _00A5 --> u
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0961_u = (v0958__00A5**1)
v0961_u = (v0961_u*_00A8_coeff).reshape((1,))

# op _00Dt_linear_combination_eval
# LANG: projection_vector, _00Ds --> _00Du
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01108__00Du = _00Dt_constant+1*v01091_projection_vector+-1*v01111__00Ds

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

# op _00Aa_power_combination_eval
# LANG: _00A5 --> v
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0962_v = (v0958__00A5**1)
v0962_v = (v0962_v*_00Aa_coeff).reshape((1,))

# op _00Ac_power_combination_eval
# LANG: _00A5 --> w
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0963_w = (v0958__00A5**1)
v0963_w = (v0963_w*_00Ac_coeff).reshape((1,))

# op _00CV_power_combination_eval
# LANG: u --> _00CW
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0961_u = v0961_u.reshape((1, 1))
v01092__00CW = (v0961_u**1)
v01092__00CW = (v01092__00CW*_00CV_coeff).reshape((1, 1))
v0961_u = v0961_u.reshape((1,))

# op _00Dv pnorm_eval
# LANG: _00Du --> _00Dw
# SHAPES: (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01113__00Dw = np.linalg.norm(v01108__00Du.flatten(), ord=2)

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

# op _00DI_decompose_eval
# LANG: _00CW --> _00DJ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01093__00DJ = ((v01092__00CW.flatten())[src_indices__00DJ__00DI]).reshape((1, 1))

# op _00DL_decompose_eval
# LANG: v --> _00DM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0962_v = v0962_v.reshape((1, 1))
v01095__00DM = ((v0962_v.flatten())[src_indices__00DM__00DL]).reshape((1, 1))
v0962_v = v0962_v.reshape((1,))

# op _00DN_decompose_eval
# LANG: w --> _00DO
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0963_w = v0963_w.reshape((1, 1))
v01096__00DO = ((v0963_w.flatten())[src_indices__00DO__00DN]).reshape((1, 1))
v0963_w = v0963_w.reshape((1,))

# op _00Dx expand_scalar_eval
# LANG: _00Dw --> _00Dy
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01114__00Dy = np.empty((1, 3))
v01114__00Dy.fill(v01113__00Dw.item())

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

# op _00DK_indexed_passthrough_eval
# LANG: _00DJ, _00DM, _00DO --> velocity_vector
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01094_velocity_vector__temp[i_v01093__00DJ__00DK_indexed_passthrough_eval] = v01093__00DJ.flatten()
v01094_velocity_vector = v01094_velocity_vector__temp.copy()
v01094_velocity_vector__temp[i_v01095__00DM__00DK_indexed_passthrough_eval] = v01095__00DM.flatten()
v01094_velocity_vector = v01094_velocity_vector__temp.copy()
v01094_velocity_vector__temp[i_v01096__00DO__00DK_indexed_passthrough_eval] = v01096__00DO.flatten()
v01094_velocity_vector = v01094_velocity_vector__temp.copy()

# op _00Dz_power_combination_eval
# LANG: _00Du, _00Dy --> in_plane_ey
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01112_in_plane_ey = (v01108__00Du**1)*(v01114__00Dy**-1)
v01112_in_plane_ey = (v01112_in_plane_ey*_00Dz_coeff).reshape((1, 3))

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

# op _00DB cross_product_eval
# LANG: _00Dk, in_plane_ey --> in_plane_ex
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01107_in_plane_ex = np.cross(v01102__00Dk, v01112_in_plane_ey, axisa = 1, axisb = 1, axisc = 1)

# op _00DP_decompose_eval
# LANG: velocity_vector --> _00DQ
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01100__00DQ = ((v01094_velocity_vector.flatten())[src_indices__00DQ__00DP]).reshape((1, 3))

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

# op _00DR_tensor_dot_product_eval
# LANG: _00DQ, in_plane_ex --> _00DS
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01106__00DS = np.sum(v01100__00DQ * v01107_in_plane_ex, axis=1)

# op _00Dl_power_combination_eval
# LANG: _00Dk --> _00Dm
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01103__00Dm = (v01102__00Dk**1)
v01103__00Dm = (v01103__00Dm*_00Dl_coeff).reshape((1, 3))

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

# op _00Bt pnorm_eval
# LANG: _00Bm --> _00Bu
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01051__00Bu = np.linalg.norm(v01050__00Bm.flatten(), ord=2)

# op _00DT_tensor_dot_product_eval
# LANG: _00DQ, in_plane_ey --> _00DU
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01117__00DU = np.sum(v01100__00DQ * v01112_in_plane_ey, axis=1)

# op _00DV_tensor_dot_product_eval
# LANG: _00DQ, _00Dm --> _00DW
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01101__00DW = np.sum(v01100__00DQ * v01103__00Dm, axis=1)

# op _00D__linear_combination_eval
# LANG: _00DS --> _00E0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01115__00E0 = _00D__constant+-1*v01106__00DS

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

# op _00Bv_power_combination_eval
# LANG: _00Bu --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01052_propeller_radius = (v01051__00Bu**1)
v01052_propeller_radius = (v01052_propeller_radius*_00Bv_coeff).reshape((1,))

# op _00DX expand_scalar_eval
# LANG: _00DW --> _00DY
# SHAPES: (1,) --> (1, 40, 100, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01104__00DY = np.empty((1, 40, 100, 1))
v01104__00DY.fill(v01101__00DW.item())

# op _00E1 expand_scalar_eval
# LANG: _00E0 --> _00E2
# SHAPES: (1,) --> (1, 40, 100, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01116__00E2 = np.empty((1, 40, 100, 1))
v01116__00E2.fill(v01115__00E0.item())

# op _00E3 expand_scalar_eval
# LANG: _00DU --> _00E4
# SHAPES: (1,) --> (1, 40, 100, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01118__00E4 = np.empty((1, 40, 100, 1))
v01118__00E4.fill(v01117__00DU.item())

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

# op _00D9_power_combination_eval
# LANG: propeller_radius --> hub_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01119_hub_radius = (v01052_propeller_radius**1)
v01119_hub_radius = (v01119_hub_radius*_00D9_coeff).reshape((1,))

# op _00DD_decompose_eval
# LANG: rpm --> _00DE
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01123__00DE = ((v01090_rpm.flatten())[src_indices__00DE__00DD]).reshape((1, 1))

# op _00DZ_indexed_passthrough_eval
# LANG: _00DY, _00E2, _00E4 --> inflow_velocity
# SHAPES: (1, 40, 100, 1), (1, 40, 100, 1), (1, 40, 100, 1) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01105_inflow_velocity__temp[i_v01104__00DY__00DZ_indexed_passthrough_eval] = v01104__00DY.flatten()
v01105_inflow_velocity = v01105_inflow_velocity__temp.copy()
v01105_inflow_velocity__temp[i_v01116__00E2__00DZ_indexed_passthrough_eval] = v01116__00E2.flatten()
v01105_inflow_velocity = v01105_inflow_velocity__temp.copy()
v01105_inflow_velocity__temp[i_v01118__00E4__00DZ_indexed_passthrough_eval] = v01118__00E4.flatten()
v01105_inflow_velocity = v01105_inflow_velocity__temp.copy()

# op _00Ft_power_combination_eval
# LANG: z --> _00Fu
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01163__00Fu = (v01162_z**1)
v01163__00Fu = (v01163__00Fu*_00Ft_coeff).reshape((1, 1))

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

# op _00DF_power_combination_eval
# LANG: _00DE --> _00DG
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01124__00DG = (v01123__00DE**1)
v01124__00DG = (v01124__00DG*_00DF_coeff).reshape((1, 1))

# op _00Ej expand_scalar_eval
# LANG: hub_radius --> _hub_radius
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01129__hub_radius = np.empty((1, 40, 100))
v01129__hub_radius.fill(v01119_hub_radius.item())

# op _00El expand_scalar_eval
# LANG: propeller_radius --> _rotor_radius
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01130__rotor_radius = np.empty((1, 40, 100))
v01130__rotor_radius.fill(v01052_propeller_radius.item())

# op _00Et expand_array_eval
# LANG: y_dir --> _y_dir
# SHAPES: (1, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01134__y_dir = np.einsum('ad,bc->abcd', v01127_y_dir.reshape((1, 3)) ,np.ones((40, 100))).reshape((1, 40, 100, 3))

# op _00Ev expand_array_eval
# LANG: z_dir --> _z_dir
# SHAPES: (1, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01135__z_dir = np.einsum('ad,bc->abcd', v01128_z_dir.reshape((1, 3)) ,np.ones((40, 100))).reshape((1, 40, 100, 3))

# op _00Ex_power_combination_eval
# LANG: inflow_velocity --> _inflow_velocity
# SHAPES: (1, 40, 100, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01136__inflow_velocity = (v01105_inflow_velocity**1)
v01136__inflow_velocity = (v01136__inflow_velocity*_00Ex_coeff).reshape((1, 40, 100, 3))

# op _00Fv_linear_combination_eval
# LANG: _00Fu --> _00Fw
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01164__00Fw = _00Fv_constant+-1*v01163__00Fu

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

# op _00DH_indexed_passthrough_eval
# LANG: _00DG --> rotational_speed
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01125_rotational_speed__temp[i_v01124__00DG__00DH_indexed_passthrough_eval] = v01124__00DG.flatten()
v01125_rotational_speed = v01125_rotational_speed__temp.copy()

# op _00ER_linear_combination_eval
# LANG: _hub_radius, _rotor_radius --> _00ES
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01144__00ES = _00ER_constant+1*v01130__rotor_radius+-1*v01129__hub_radius

# op _00F6_tensor_dot_product_eval
# LANG: _y_dir, _inflow_velocity --> _in_plane_inflow_velocity
# SHAPES: (1, 40, 100, 3), (1, 40, 100, 3) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01151__in_plane_inflow_velocity = np.sum(v01136__inflow_velocity * v01134__y_dir, axis=3)

# op _00F8_tensor_dot_product_eval
# LANG: _z_dir, _inflow_velocity --> inflow_z
# SHAPES: (1, 40, 100, 3), (1, 40, 100, 3) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01152_inflow_z = np.sum(v01136__inflow_velocity * v01135__z_dir, axis=3)

# op _00Fx_power_combination_eval
# LANG: _00Fw --> _00Fy
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01165__00Fy = (v01164__00Fw**1)
v01165__00Fy = (v01165__00Fy*_00Fx_coeff).reshape((1, 1))

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

# op _000s_sparsematmat_eval
# LANG: design_geometry --> _000t
# SHAPES: (16250, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v013__000t = _000s_sparsematmat_eval_mat@v05_design_geometry

# op _00ET_power_combination_eval
# LANG: _00ES, _normalized_radius --> _00EU
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01145__00EU = (v01144__00ES**1)*(v01141__normalized_radius**1)
v01145__00EU = (v01145__00EU*_00ET_coeff).reshape((1, 40, 100))

# op _00Ep expand_scalar_eval
# LANG: rotational_speed --> _rotational_speed
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01125_rotational_speed = v01125_rotational_speed.reshape((1,))
v01132__rotational_speed = np.empty((1, 40, 100))
v01132__rotational_speed.fill(v01125_rotational_speed.item())
v01125_rotational_speed = v01125_rotational_speed.reshape((1, 1))

# op _00Fa_power_combination_eval
# LANG: inflow_z --> _00Fb
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01153__00Fb = (v01152_inflow_z**1)
v01153__00Fb = (v01153__00Fb*_00Fa_coeff).reshape((1, 40, 100))

# op _00Fc_cos_eval
# LANG: _theta --> _00Fd
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01155__00Fd = np.cos(v01140__theta)

# op _00Fg_power_combination_eval
# LANG: _in_plane_inflow_velocity --> _00Fh
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01157__00Fh = (v01151__in_plane_inflow_velocity**1)
v01157__00Fh = (v01157__00Fh*_00Fg_coeff).reshape((1, 40, 100))

# op _00Fi_sin_eval
# LANG: _theta --> _00Fj
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01159__00Fj = np.sin(v01140__theta)

# op _00Fz_linear_combination_eval
# LANG: _00Fy --> temperature
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01166_temperature = _00Fz_constant+1*v01165__00Fy

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

# op _000u reshape_eval
# LANG: _000t --> rotor_blade_chord_length
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v014_rotor_blade_chord_length = v013__000t.reshape((40, 3))

# op _00EP_power_combination_eval
# LANG: _rotational_speed --> _angular_speed
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01142__angular_speed = (v01132__rotational_speed**1)
v01142__angular_speed = (v01142__angular_speed*_00EP_coeff).reshape((1, 40, 100))

# op _00EV_linear_combination_eval
# LANG: _00EU, _hub_radius --> _radius
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01143__radius = _00EV_constant+1*v01129__hub_radius+1*v01145__00EU

# op _00FB_power_combination_eval
# LANG: temperature --> _00FC
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01167__00FC = (v01166_temperature**1)
v01167__00FC = (v01167__00FC*_00FB_coeff).reshape((1, 1))

# op _00Fe_power_combination_eval
# LANG: _00Fb, _00Fd --> _00Ff
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01154__00Ff = (v01153__00Fb**1)*(v01155__00Fd**1)
v01154__00Ff = (v01154__00Ff*_00Fe_coeff).reshape((1, 40, 100))

# op _00Fk_power_combination_eval
# LANG: _00Fh, _00Fj --> _00Fl
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01158__00Fl = (v01157__00Fh**1)*(v01159__00Fj**1)
v01158__00Fl = (v01158__00Fl*_00Fk_coeff).reshape((1, 40, 100))

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

# op _000w_sparsematmat_eval
# LANG: design_geometry --> _000x
# SHAPES: (16250, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v015__000x = _000w_sparsematmat_eval_mat@v05_design_geometry

# op _00B3 pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00B4
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01042__00B4 = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00Er expand_array_eval
# LANG: x_dir --> _x_dir
# SHAPES: (1, 3) --> (1, 40, 100, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01133__x_dir = np.einsum('ad,bc->abcd', v01126_x_dir.reshape((1, 3)) ,np.ones((40, 100))).reshape((1, 40, 100, 3))

# op _00FD_power_combination_eval
# LANG: _00FC --> _00FE
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01168__00FE = (v01167__00FC**5.258643795229161)
v01168__00FE = (v01168__00FE*_00FD_coeff).reshape((1, 1))

# op _00Fm_linear_combination_eval
# LANG: _00Ff, _00Fl --> _00Fn
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01156__00Fn = _00Fm_constant+1*v01154__00Ff+1*v01158__00Fl

# op _00Fo_power_combination_eval
# LANG: _angular_speed, _radius --> _00Fp
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01161__00Fp = (v01143__radius**1)*(v01142__angular_speed**1)
v01161__00Fp = (v01161__00Fp*_00Fo_coeff).reshape((1, 40, 100))

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

# op _000y reshape_eval
# LANG: _000x --> rotor_blade_twist
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v016_rotor_blade_twist = v015__000x.reshape((40, 3))

# op _00B5 reshape_eval
# LANG: _00B4 --> _00B6
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01043__00B6 = v01042__00B4.reshape((40, 1))

# op _00F4_tensor_dot_product_eval
# LANG: _x_dir, _inflow_velocity --> _axial_inflow_velocity
# SHAPES: (1, 40, 100, 3), (1, 40, 100, 3) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01150__axial_inflow_velocity = np.sum(v01136__inflow_velocity * v01133__x_dir, axis=3)

# op _00FF_power_combination_eval
# LANG: _00FE --> pressure
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01169_pressure = (v01168__00FE**1)
v01169_pressure = (v01169_pressure*_00FF_coeff).reshape((1, 1))

# op _00FL_power_combination_eval
# LANG: temperature --> _00FM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01172__00FM = (v01166_temperature**1)
v01172__00FM = (v01172__00FM*_00FL_coeff).reshape((1, 1))

# op _00Fq_linear_combination_eval
# LANG: _00Fn, _00Fp --> _tangential_inflow_velocity
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01160__tangential_inflow_velocity = _00Fq_constant+1*v01156__00Fn+1*v01161__00Fp

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

# op _00B7_power_combination_eval
# LANG: _00B6 --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01044_chord_profile = (v01043__00B6**1)
v01044_chord_profile = (v01044_chord_profile*_00B7_coeff).reshape((40, 1))

# op _00BS_power_combination_eval
# LANG: _axial_inflow_velocity --> _00BT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01064__00BT = (v01150__axial_inflow_velocity**2)
v01064__00BT = (v01064__00BT*_00BS_coeff).reshape((1, 40, 100))

# op _00BU_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00BV
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01066__00BV = (v01160__tangential_inflow_velocity**2)
v01066__00BV = (v01066__00BV*_00BU_coeff).reshape((1, 40, 100))

# op _00Ba_single_tensor_sum_with_axis_eval
# LANG: rotor_blade_twist --> _00Bb
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01045__00Bb = np.sum(v016_rotor_blade_twist, axis = (1,)).reshape((40,))

# op _00FH_power_combination_eval
# LANG: pressure --> _00FI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01170__00FI = (v01169_pressure**1)
v01170__00FI = (v01170__00FI*_00FH_coeff).reshape((1, 1))

# op _00FN_power_combination_eval
# LANG: _00FM --> _00FO
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01173__00FO = (v01172__00FM**1.5)
v01173__00FO = (v01173__00FO*_00FN_coeff).reshape((1, 1))

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

# op _00BW_linear_combination_eval
# LANG: _00BT, _00BV --> _00BX
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01065__00BX = _00BW_constant+1*v01064__00BT+1*v01066__00BV

# op _00Bc reshape_eval
# LANG: _00Bb --> _00Bd
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01046__00Bd = v01045__00Bb.reshape((40, 1))

# op _00EB expand_array_eval
# LANG: chord_profile --> _chord
# SHAPES: (40,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01044_chord_profile = v01044_chord_profile.reshape((40,))
v01138__chord = np.einsum('b,ac->abc', v01044_chord_profile.reshape((40,)) ,np.ones((1, 100))).reshape((1, 40, 100))
v01044_chord_profile = v01044_chord_profile.reshape((40, 1))

# op _00FJ_power_combination_eval
# LANG: temperature, _00FI --> density
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01171_density = (v01170__00FI**1)*(v01166_temperature**-1)
v01171_density = (v01171_density*_00FJ_coeff).reshape((1, 1))

# op _00FP_power_combination_eval
# LANG: _00FO --> _00FQ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01174__00FQ = (v01173__00FO**1)
v01174__00FQ = (v01174__00FQ*_00FP_coeff).reshape((1, 1))

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

# op _00BY_power_combination_eval
# LANG: _00BX --> _00BZ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01067__00BZ = (v01065__00BX**0.5)
v01067__00BZ = (v01067__00BZ*_00BY_coeff).reshape((1, 40, 100))

# op _00Be_power_combination_eval
# LANG: _00B6, _00Bd --> _00Bf
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01047__00Bf = (v01046__00Bd**1)*(v01043__00B6**-1)
v01047__00Bf = (v01047__00Bf*_00Be_coeff).reshape((40, 1))

# op _00C0 expand_scalar_eval
# LANG: density --> _00C1
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01171_density = v01171_density.reshape((1,))
v01062__00C1 = np.empty((1, 40, 100))
v01062__00C1.fill(v01171_density.item())
v01171_density = v01171_density.reshape((1, 1))

# op _00EX_power_combination_eval
# LANG: _chord --> _00EY
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01146__00EY = (v01138__chord**1)
v01146__00EY = (v01146__00EY*_00EX_coeff).reshape((1, 40, 100))

# op _00FR_power_combination_eval
# LANG: _00FQ --> _00FS
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01175__00FS = (v01174__00FQ**1)
v01175__00FS = (v01175__00FS*_00FR_coeff).reshape((1, 1))

# op _00FT_linear_combination_eval
# LANG: temperature --> _00FU
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01177__00FU = _00FT_constant+1*v01166_temperature

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

# op _00Bg_arcsin_eval
# LANG: _00Bf --> _00Bh
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01048__00Bh = np.arcsin(v01047__00Bf)

# op _00C8_power_combination_eval
# LANG: _00C1, _00BZ --> _00C9
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01063__00C9 = (v01062__00C1**1)*(v01067__00BZ**1)
v01063__00C9 = (v01063__00C9*_00C8_coeff).reshape((1, 40, 100))

# op _00EZ_power_combination_eval
# LANG: _00EY --> _00E_
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01147__00E_ = (v01146__00EY**1)
v01147__00E_ = (v01147__00E_*_00EZ_coeff).reshape((1, 40, 100))

# op _00FV_power_combination_eval
# LANG: _00FS, _00FU --> dynamic_viscosity
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01176_dynamic_viscosity = (v01175__00FS**1)*(v01177__00FU**-1)
v01176_dynamic_viscosity = (v01176_dynamic_viscosity*_00FV_coeff).reshape((1, 1))

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

# op _00Bi_linear_combination_eval
# LANG: _00Bh --> twist_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01049_twist_profile = _00Bi_constant+1*v01048__00Bh

# op _00C3 expand_scalar_eval
# LANG: dynamic_viscosity --> _00C4
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01176_dynamic_viscosity = v01176_dynamic_viscosity.reshape((1,))
v01070__00C4 = np.empty((1, 40, 100))
v01070__00C4.fill(v01176_dynamic_viscosity.item())
v01176_dynamic_viscosity = v01176_dynamic_viscosity.reshape((1, 1))

# op _00Ca_power_combination_eval
# LANG: _00C9, _chord --> _00Cb
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01068__00Cb = (v01063__00C9**1)*(v01138__chord**1)
v01068__00Cb = (v01068__00Cb*_00Ca_coeff).reshape((1, 40, 100))

# op _00F0_power_combination_eval
# LANG: _00E_ --> _00F1
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01148__00F1 = (v01147__00E_**1)
v01148__00F1 = (v01148__00F1*_00F0_coeff).reshape((1, 40, 100))

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

# op _00Cc_power_combination_eval
# LANG: _00Cb, _00C4 --> Re
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01069_Re = (v01068__00Cb**1)*(v01070__00C4**-1)
v01069_Re = (v01069_Re*_00Cc_coeff).reshape((1, 40, 100))

# op _00Ez expand_array_eval
# LANG: twist_profile --> _pitch
# SHAPES: (40,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01049_twist_profile = v01049_twist_profile.reshape((40,))
v01137__pitch = np.einsum('b,ac->abc', v01049_twist_profile.reshape((40,)) ,np.ones((1, 100))).reshape((1, 40, 100))
v01049_twist_profile = v01049_twist_profile.reshape((40, 1))

# op _00F2_power_combination_eval
# LANG: _radius, _00F1 --> _blade_solidity
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_pre_process_model
v01149__blade_solidity = (v01148__00F1**1)*(v01143__radius**-1)
v01149__blade_solidity = (v01149__blade_solidity*_00F2_coeff).reshape((1, 40, 100))

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

# op _00HN_bracketed_implict_eval
# LANG: Re, _hub_radius, _rotor_radius, _pitch, _chord, _radius, _blade_solidity, _axial_inflow_velocity, _tangential_inflow_velocity --> phi_distribution, alpha_distribution, Cl, Cd
# SHAPES: (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100) --> (1, 40, 100), (1, 40, 100), (1, 40, 100), (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.phi_bracketed_search_group
_00HN_bracketed.set_guess(initial_guess_v01180_phi_distribution)
_00HN_bracketed_out = _00HN_bracketed.solve(v01149__blade_solidity, v01150__axial_inflow_velocity, v01160__tangential_inflow_velocity, v01143__radius, v01130__rotor_radius, v01129__hub_radius, v01138__chord, v01137__pitch, v01069_Re)
v01180_phi_distribution = _00HN_bracketed_out[0]
v01181_alpha_distribution = _00HN_bracketed_out[1]
v01182_Cl = _00HN_bracketed_out[2]
v01183_Cd = _00HN_bracketed_out[3]

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

# op _00HW_linear_combination_eval
# LANG: _rotor_radius, _radius --> _00HX
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01184__00HX = _00HW_constant+1*v01130__rotor_radius+-1*v01143__radius

# op _00I5_linear_combination_eval
# LANG: _hub_radius, _radius --> _00I6
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01194__00I6 = _00I5_constant+1*v01143__radius+-1*v01129__hub_radius

# op _00HY_power_combination_eval
# LANG: _00HX --> _00HZ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01185__00HZ = (v01184__00HX**1)
v01185__00HZ = (v01185__00HZ*_00HY_coeff).reshape((1, 40, 100))

# op _00I7_power_combination_eval
# LANG: _00I6 --> _00I8
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01195__00I8 = (v01194__00I6**1)
v01195__00I8 = (v01195__00I8*_00I7_coeff).reshape((1, 40, 100))

# op _00T__power_combination_eval
# LANG: rpm --> _00U0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01090_rpm = v01090_rpm.reshape((1,))
v01561__00U0 = (v01090_rpm**1)
v01561__00U0 = (v01561__00U0*_00T__coeff).reshape((1,))
v01090_rpm = v01090_rpm.reshape((1, 1))

# op _00H__power_combination_eval
# LANG: _00HZ, _radius --> _00I0
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01186__00I0 = (v01185__00HZ**1)*(v01143__radius**-1)
v01186__00I0 = (v01186__00I0*_00H__coeff).reshape((1, 40, 100))

# op _00I1_sin_eval
# LANG: phi_distribution --> _00I2
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01188__00I2 = np.sin(v01180_phi_distribution)

# op _00I9_power_combination_eval
# LANG: _00I8, _hub_radius --> _00Ia
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01196__00Ia = (v01195__00I8**1)*(v01129__hub_radius**-1)
v01196__00Ia = (v01196__00Ia*_00I9_coeff).reshape((1, 40, 100))

# op _00Ib_sin_eval
# LANG: phi_distribution --> _00Ic
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01198__00Ic = np.sin(v01180_phi_distribution)

# op _00Pf_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00Pg
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v01406__00Pg = (v08_rotor_disk_in_plane_1**1)
v01406__00Pg = (v01406__00Pg*_00Pf_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _00U1_power_combination_eval
# LANG: _00U0 --> _00U2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01562__00U2 = (v01561__00U0**1)
v01562__00U2 = (v01562__00U2*_00U1_coeff).reshape((1,))

# op _00I3_power_combination_eval
# LANG: _00I0, _00I2 --> _00I4
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01187__00I4 = (v01186__00I0**1)*(v01188__00I2**-1)
v01187__00I4 = (v01187__00I4*_00I3_coeff).reshape((1, 40, 100))

# op _00Id_power_combination_eval
# LANG: _00Ia, _00Ic --> _00Ie
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01197__00Ie = (v01196__00Ia**1)*(v01198__00Ic**-1)
v01197__00Ie = (v01197__00Ie*_00Id_coeff).reshape((1, 40, 100))

# op _00Pn pnorm_eval
# LANG: _00Pg --> _00Po
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01407__00Po = np.linalg.norm(v01406__00Pg.flatten(), ord=2)

# op _00Ps pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00Pt
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01409__00Pt = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00U3_power_combination_eval
# LANG: _00U2 --> _00U4
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01563__00U4 = (v01562__00U2**1)
v01563__00U4 = (v01563__00U4*_00U3_coeff).reshape((1,))

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

# op _00If_linear_combination_eval
# LANG: _00I4 --> _00Ig
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01189__00Ig = _00If_constant+-1*v01187__00I4

# op _00In_linear_combination_eval
# LANG: _00Ie --> _00Io
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01199__00Io = _00In_constant+-1*v01197__00Ie

# op _00Pp_power_combination_eval
# LANG: _00Po --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01408_propeller_radius = (v01407__00Po**1)
v01408_propeller_radius = (v01408_propeller_radius*_00Pp_coeff).reshape((1,))

# op _00Pu reshape_eval
# LANG: _00Pt --> _00Pv
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01410__00Pv = v01409__00Pt.reshape((40, 1))

# op _00Uu expand_array_eval
# LANG: nondim_sectional_radius --> _00Uv
# SHAPES: (40,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01553__00Uv = np.einsum('d,abce->abcde', v01552_nondim_sectional_radius.reshape((40,)) ,np.ones((1, 2, 3, 11))).reshape((1, 2, 3, 40, 11))

# op _00Uw expand_scalar_eval
# LANG: _00U4 --> _00Ux
# SHAPES: (1,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01564__00Ux = np.empty((1, 2, 3, 40, 11))
v01564__00Ux.fill(v01563__00U4.item())

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

# op _00Ih exp_eval
# LANG: _00Ig --> _00Ii
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01190__00Ii = np.exp(v01189__00Ig)

# op _00Ip exp_eval
# LANG: _00Io --> _00Iq
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01200__00Iq = np.exp(v01199__00Io)

# op _00Pw_power_combination_eval
# LANG: _00Pv --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01411_chord_profile = (v01410__00Pv**1)
v01411_chord_profile = (v01411_chord_profile*_00Pw_coeff).reshape((40, 1))

# op _00UI_decompose_eval
# LANG: _00Uv --> _00UJ
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01571__00UJ = ((v01553__00Uv.flatten())[src_indices__00UJ__00UI]).reshape((1, 2, 3, 40, 10))

# op _00UK_decompose_eval
# LANG: _00Ux --> _00UL
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01565__00UL = ((v01564__00Ux.flatten())[src_indices__00UL__00UK]).reshape((1, 2, 3, 40, 10))

# op _00Uy expand_scalar_eval
# LANG: propeller_radius --> _00Uz
# SHAPES: (1,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01573__00Uz = np.empty((1, 2, 3, 40, 11))
v01573__00Uz.fill(v01408_propeller_radius.item())

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

# op _00Ij arccos_eval
# LANG: _00Ii --> _00Ik
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01191__00Ik = np.arccos(v01190__00Ii)

# op _00Ir arccos_eval
# LANG: _00Iq --> _00Is
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01201__00Is = np.arccos(v01200__00Iq)

# op _00UC expand_array_eval
# LANG: chord_profile --> _00UD
# SHAPES: (40,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01411_chord_profile = v01411_chord_profile.reshape((40,))
v01567__00UD = np.einsum('d,abce->abcde', v01411_chord_profile.reshape((40,)) ,np.ones((1, 2, 3, 11))).reshape((1, 2, 3, 40, 11))
v01411_chord_profile = v01411_chord_profile.reshape((40, 1))

# op _00UM_decompose_eval
# LANG: _00Uz --> _00UN
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01574__00UN = ((v01573__00Uz.flatten())[src_indices__00UN__00UM]).reshape((1, 2, 3, 40, 10))

# op _00Vm_decompose_eval
# LANG: lam_var --> _00Vn
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01559__00Vn = ((v01558_lam_var.flatten())[src_indices__00Vn__00Vm]).reshape((1, 2, 3, 40, 10))

# op _00Vo_power_combination_eval
# LANG: _00UL, _00UJ --> _00Vp
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01570__00Vp = (v01565__00UL**1)*(v01571__00UJ**1)
v01570__00Vp = (v01570__00Vp*_00Vo_coeff).reshape((1, 2, 3, 40, 10))

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

# op _00Il_power_combination_eval
# LANG: _00Ik --> _00Im
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01192__00Im = (v01191__00Ik**1)
v01192__00Im = (v01192__00Im*_00Il_coeff).reshape((1, 40, 100))

# op _00It_power_combination_eval
# LANG: _00Is --> _00Iu
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01202__00Iu = (v01201__00Is**1)
v01202__00Iu = (v01202__00Iu*_00It_coeff).reshape((1, 40, 100))

# op _00J1_sin_eval
# LANG: phi_distribution --> _00J2
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01217__00J2 = np.sin(v01180_phi_distribution)

# op _00J5_cos_eval
# LANG: phi_distribution --> _00J6
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01220__00J6 = np.cos(v01180_phi_distribution)

# op _00Rg_power_combination_eval
# LANG: altitude --> _00Rh
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01462__00Rh = (v0974_hover_altitude**1)
v01462__00Rh = (v01462__00Rh*_00Rg_coeff).reshape((1,))

# op _00UQ_decompose_eval
# LANG: _00UD --> _00UR
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01568__00UR = ((v01567__00UD.flatten())[src_indices__00UR__00UQ]).reshape((1, 2, 3, 40, 10))

# op _00Vq_power_combination_eval
# LANG: _00Vp, _00UN --> _00Vr
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01572__00Vr = (v01570__00Vp**1)*(v01574__00UN**1)
v01572__00Vr = (v01572__00Vr*_00Vq_coeff).reshape((1, 2, 3, 40, 10))

# op _00Vs_power_combination_eval
# LANG: _00Vn, _00UL --> _00Vt
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01560__00Vt = (v01559__00Vn**1)*(v01565__00UL**1)
v01560__00Vt = (v01560__00Vt*_00Vs_coeff).reshape((1, 2, 3, 40, 10))

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

# op _00IS_cos_eval
# LANG: phi_distribution --> _00IT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01224__00IT = np.cos(v01180_phi_distribution)

# op _00IW_sin_eval
# LANG: phi_distribution --> _00IX
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01227__00IX = np.sin(v01180_phi_distribution)

# op _00Iv_power_combination_eval
# LANG: _00Im, _00Iu --> prandtl_loss_factor
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.prandtl_loss_factor_model
v01193_prandtl_loss_factor = (v01192__00Im**1)*(v01202__00Iu**1)
v01193_prandtl_loss_factor = (v01193_prandtl_loss_factor*_00Iv_coeff).reshape((1, 40, 100))

# op _00J3_power_combination_eval
# LANG: _00J2, Cl --> _00J4
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01216__00J4 = (v01182_Cl**1)*(v01217__00J2**1)
v01216__00J4 = (v01216__00J4*_00J3_coeff).reshape((1, 40, 100))

# op _00J7_power_combination_eval
# LANG: _00J6, Cd --> _00J8
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01219__00J8 = (v01183_Cd**1)*(v01220__00J6**1)
v01219__00J8 = (v01219__00J8*_00J7_coeff).reshape((1, 40, 100))

# op _00Kc_power_combination_eval
# LANG: phi_distribution --> _00Kd
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01243__00Kd = (v01180_phi_distribution**1)
v01243__00Kd = (v01243__00Kd*_00Kc_coeff).reshape((1, 40, 100))

# op _00Ri_linear_combination_eval
# LANG: _00Rh --> _00Rj
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01463__00Rj = _00Ri_constant+-1*v01462__00Rh

# op _00Vu_power_combination_eval
# LANG: _00Vt, _00UR --> _00Vv
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01566__00Vv = (v01560__00Vt**1)*(v01568__00UR**1)
v01566__00Vv = (v01566__00Vv*_00Vu_coeff).reshape((1, 2, 3, 40, 10))

# op _00Vw_power_combination_eval
# LANG: _00Vr --> _00Vx
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01575__00Vx = (v01572__00Vr**1)
v01575__00Vx = (v01575__00Vx*_00Vw_coeff).reshape((1, 2, 3, 40, 10))

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

# op _00IU_power_combination_eval
# LANG: _00IT, Cl --> _00IV
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01223__00IV = (v01182_Cl**1)*(v01224__00IT**1)
v01223__00IV = (v01223__00IV*_00IU_coeff).reshape((1, 40, 100))

# op _00IY_power_combination_eval
# LANG: _00IX, Cd --> _00IZ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01226__00IZ = (v01183_Cd**1)*(v01227__00IX**1)
v01226__00IZ = (v01226__00IZ*_00IY_coeff).reshape((1, 40, 100))

# op _00J9_linear_combination_eval
# LANG: _00J4, _00J8 --> _00Ja
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01218__00Ja = _00J9_constant+1*v01216__00J4+1*v01219__00J8

# op _00JN_power_combination_eval
# LANG: prandtl_loss_factor --> _00JO
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01230__00JO = (v01193_prandtl_loss_factor**1)
v01230__00JO = (v01230__00JO*_00JN_coeff).reshape((1, 40, 100))

# op _00JP_sin_eval
# LANG: phi_distribution --> _00JQ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01232__00JQ = np.sin(v01180_phi_distribution)

# op _00K4_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00K5
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01237__00K5 = (v01160__tangential_inflow_velocity**1)
v01237__00K5 = (v01237__00K5*_00K4_coeff).reshape((1, 40, 100))

# op _00Ka_power_combination_eval
# LANG: prandtl_loss_factor --> _00Kb
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01241__00Kb = (v01193_prandtl_loss_factor**1)
v01241__00Kb = (v01241__00Kb*_00Ka_coeff).reshape((1, 40, 100))

# op _00Ke_sin_eval
# LANG: _00Kd --> _00Kf
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01244__00Kf = np.sin(v01243__00Kd)

# op _00Rk_power_combination_eval
# LANG: _00Rj --> _00Rl
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01464__00Rl = (v01463__00Rj**1)
v01464__00Rl = (v01464__00Rl*_00Rk_coeff).reshape((1,))

# op _00Vy_power_combination_eval
# LANG: _00Vv, _00Vx --> _00Vz
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01569__00Vz = (v01566__00Vv**1)*(v01575__00Vx**-1)
v01569__00Vz = (v01569__00Vz*_00Vy_coeff).reshape((1, 2, 3, 40, 10))

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

# op _00I__linear_combination_eval
# LANG: _00IV, _00IZ --> _00J0
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01225__00J0 = _00I__constant+1*v01223__00IV+-1*v01226__00IZ

# op _00JR_power_combination_eval
# LANG: _00JO, _00JQ --> _00JS
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01231__00JS = (v01230__00JO**1)*(v01232__00JQ**1)
v01231__00JS = (v01231__00JS*_00JR_coeff).reshape((1, 40, 100))

# op _00JT_cos_eval
# LANG: phi_distribution --> _00JU
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01234__00JU = np.cos(v01180_phi_distribution)

# op _00K6_power_combination_eval
# LANG: _00K5, _blade_solidity --> _00K7
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01238__00K7 = (v01237__00K5**1)*(v01149__blade_solidity**1)
v01238__00K7 = (v01238__00K7*_00K6_coeff).reshape((1, 40, 100))

# op _00Kg_power_combination_eval
# LANG: _00Kb, _00Kf --> _00Kh
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01242__00Kh = (v01241__00Kb**1)*(v01244__00Kf**1)
v01242__00Kh = (v01242__00Kh*_00Kg_coeff).reshape((1, 40, 100))

# op _00Ki_power_combination_eval
# LANG: _00Ja, _blade_solidity --> _00Kj
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01246__00Kj = (v01149__blade_solidity**1)*(v01218__00Ja**1)
v01246__00Kj = (v01246__00Kj*_00Ki_coeff).reshape((1, 40, 100))

# op _00Rm_linear_combination_eval
# LANG: _00Rl --> temperature
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01465_temperature = _00Rm_constant+1*v01464__00Rl

# op _00UV_decompose_eval
# LANG: phi --> _00UW
# SHAPES: (1, 40, 100) --> (1, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01548__00UW = ((v01180_phi_distribution.flatten())[src_indices__00UW__00UV]).reshape((1, 40, 1))

# op _00Xg_bessel_eval
# LANG: _00Vz --> _00Xh
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01655__00Xh=_00Xg_bessel_eval(0,v01569__00Vz)

# op _00Xi_bessel_eval
# LANG: _00Vz --> _00Xj
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01657__00Xj=_00Xi_bessel_eval(1,v01569__00Vz)

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

# op _00JJ_power_combination_eval
# LANG: _00J0, _blade_solidity --> _00JK
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01222__00JK = (v01149__blade_solidity**1)*(v01225__00J0**1)
v01222__00JK = (v01222__00JK*_00JJ_coeff).reshape((1, 40, 100))

# op _00JV_power_combination_eval
# LANG: _00JS, _00JU --> _00JW
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01233__00JW = (v01231__00JS**1)*(v01234__00JU**1)
v01233__00JW = (v01233__00JW*_00JV_coeff).reshape((1, 40, 100))

# op _00JX_power_combination_eval
# LANG: _00Ja, _blade_solidity --> _00JY
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01236__00JY = (v01149__blade_solidity**1)*(v01218__00Ja**1)
v01236__00JY = (v01236__00JY*_00JX_coeff).reshape((1, 40, 100))

# op _00K8_power_combination_eval
# LANG: _00Ja, _00K7 --> _00K9
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01239__00K9 = (v01238__00K7**1)*(v01218__00Ja**1)
v01239__00K9 = (v01239__00K9*_00K8_coeff).reshape((1, 40, 100))

# op _00Kk_linear_combination_eval
# LANG: _00Kh, _00Kj --> _00Kl
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01245__00Kl = _00Kk_constant+1*v01242__00Kh+1*v01246__00Kj

# op _00Ro_power_combination_eval
# LANG: temperature --> _00Rp
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01466__00Rp = (v01465_temperature**1)
v01466__00Rp = (v01466__00Rp*_00Ro_coeff).reshape((1,))

# op _00UX reshape_eval
# LANG: _00UW --> _00UY
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01549__00UY = v01548__00UW.reshape((1, 40))

# op _00Xc_bessel_eval
# LANG: _00Vz --> _00Xd
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01652__00Xd=_00Xc_bessel_eval(1,v01569__00Vz)

# op _00Xk_power_combination_eval
# LANG: _00Xh, _00Xj --> _00Xl
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01656__00Xl = (v01655__00Xh**1)*(v01657__00Xj**1)
v01656__00Xl = (v01656__00Xl*_00Xk_coeff).reshape((1, 2, 3, 40, 10))

# op _00Xm_bessel_eval
# LANG: _00Vz --> _00Xn
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01659__00Xn=_00Xm_bessel_eval(1,v01569__00Vz)

# op _00Xs_bessel_eval
# LANG: _00Vz --> _00Xt
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01661__00Xt=_00Xs_bessel_eval(1,v01569__00Vz)

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

# op _00JL_power_combination_eval
# LANG: _00JK, _tangential_inflow_velocity --> _00JM
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01228__00JM = (v01222__00JK**1)*(v01160__tangential_inflow_velocity**1)
v01228__00JM = (v01228__00JM*_00JL_coeff).reshape((1, 40, 100))

# op _00JZ_linear_combination_eval
# LANG: _00JW, _00JY --> _00J_
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01235__00J_ = _00JZ_constant+1*v01233__00JW+1*v01236__00JY

# op _00Km_power_combination_eval
# LANG: _00K9, _00Kl --> _ut
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01240__ut = (v01239__00K9**1)*(v01245__00Kl**-1)
v01240__ut = (v01240__ut*_00Km_coeff).reshape((1, 40, 100))

# op _00Rq_power_combination_eval
# LANG: _00Rp --> _00Rr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01467__00Rr = (v01466__00Rp**5.258643795229161)
v01467__00Rr = (v01467__00Rr*_00Rq_coeff).reshape((1,))

# op _00UZ expand_array_eval
# LANG: _00UY --> _00U_
# SHAPES: (1, 40) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01550__00U_ = np.einsum('ad,bce->abcde', v01549__00UY.reshape((1, 40)) ,np.ones((2, 3, 11))).reshape((1, 2, 3, 40, 11))

# op _00XC_bessel_eval
# LANG: _00Vz --> _00XD
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01666__00XD=_00XC_bessel_eval(0,v01569__00Vz)

# op _00XE_bessel_eval
# LANG: _00Vz --> _00XF
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01668__00XF=_00XE_bessel_eval(0,v01569__00Vz)

# op _00Xe_power_combination_eval
# LANG: _00Xd --> _00Xf
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01653__00Xf = (v01652__00Xd**3)
v01653__00Xf = (v01653__00Xf*_00Xe_coeff).reshape((1, 2, 3, 40, 10))

# op _00Xo_power_combination_eval
# LANG: _00Xl, _00Xn --> _00Xp
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01658__00Xp = (v01656__00Xl**1)*(v01659__00Xn**1)
v01658__00Xp = (v01658__00Xp*_00Xo_coeff).reshape((1, 2, 3, 40, 10))

# op _00Xu_power_combination_eval
# LANG: _00Xt --> _00Xv
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01662__00Xv = (v01661__00Xt**2)
v01662__00Xv = (v01662__00Xv*_00Xu_coeff).reshape((1, 2, 3, 40, 10))

# op _00Xw_bessel_eval
# LANG: _00Vz --> _00Xx
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01664__00Xx=_00Xw_bessel_eval(0,v01569__00Vz)

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

# op _00Jt_power_combination_eval
# LANG: prandtl_loss_factor --> _00Ju
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01209__00Ju = (v01193_prandtl_loss_factor**1)
v01209__00Ju = (v01209__00Ju*_00Jt_coeff).reshape((1, 40, 100))

# op _00Jv_sin_eval
# LANG: phi_distribution --> _00Jw
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01211__00Jw = np.sin(v01180_phi_distribution)

# op _00K0_power_combination_eval
# LANG: _00JM, _00J_ --> _00K1
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01229__00K1 = (v01228__00JM**1)*(v01235__00J_**-1)
v01229__00K1 = (v01229__00K1*_00K0_coeff).reshape((1, 40, 100))

# op _00LX_power_combination_eval
# LANG: _ut --> _00LY
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01309__00LY = (v01240__ut**1)
v01309__00LY = (v01309__00LY*_00LX_coeff).reshape((1, 40, 100))

# op _00RV expand_scalar_eval
# LANG: Vx --> _00RW
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01479__00RW = np.empty((1, 1))
v01479__00RW.fill(v0961_u.item())

# op _00RY expand_scalar_eval
# LANG: Vy --> _00RZ
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01481__00RZ = np.empty((1, 1))
v01481__00RZ.fill(v0962_v.item())

# op _00R_ expand_scalar_eval
# LANG: Vz --> _00S0
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01482__00S0 = np.empty((1, 1))
v01482__00S0.fill(v0963_w.item())

# op _00Rs_power_combination_eval
# LANG: _00Rr --> pressure
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01468_pressure = (v01467__00Rr**1)
v01468_pressure = (v01468_pressure*_00Rs_coeff).reshape((1,))

# op _00V0_power_combination_eval
# LANG: _00U_, _00Uv --> lambda_test
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01551_lambda_test = (v01550__00U_**1)*(v01553__00Uv**1)
v01551_lambda_test = (v01551_lambda_test*_00V0_coeff).reshape((1, 2, 3, 40, 11))

# op _00XG_power_combination_eval
# LANG: _00XD, _00XF --> _00XH
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01667__00XH = (v01666__00XD**1)*(v01668__00XF**1)
v01667__00XH = (v01667__00XH*_00XG_coeff).reshape((1, 2, 3, 40, 10))

# op _00XI_bessel_eval
# LANG: _00Vz --> _00XJ
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01670__00XJ=_00XI_bessel_eval(1,v01569__00Vz)

# op _00XO_bessel_eval
# LANG: _00Vz --> _00XP
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01672__00XP=_00XO_bessel_eval(0,v01569__00Vz)

# op _00Xq_linear_combination_eval
# LANG: _00Xf, _00Xp --> _00Xr
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01654__00Xr = _00Xq_constant+1*v01653__00Xf+1*v01658__00Xp

# op _00Xy_power_combination_eval
# LANG: _00Xv, _00Xx --> _00Xz
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01663__00Xz = (v01662__00Xv**1)*(v01664__00Xx**1)
v01663__00Xz = (v01663__00Xz*_00Xy_coeff).reshape((1, 2, 3, 40, 10))

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

# op _00Jj_power_combination_eval
# LANG: prandtl_loss_factor --> _00Jk
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01203__00Jk = (v01193_prandtl_loss_factor**1)
v01203__00Jk = (v01203__00Jk*_00Jj_coeff).reshape((1, 40, 100))

# op _00Jn_sin_eval
# LANG: phi_distribution --> _00Jo
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01206__00Jo = np.sin(v01180_phi_distribution)

# op _00Jx_power_combination_eval
# LANG: _00Ju, _00Jw --> _00Jy
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01210__00Jy = (v01209__00Ju**1)*(v01211__00Jw**1)
v01210__00Jy = (v01210__00Jy*_00Jx_coeff).reshape((1, 40, 100))

# op _00Jz_cos_eval
# LANG: phi_distribution --> _00JA
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01213__00JA = np.cos(v01180_phi_distribution)

# op _00K2_linear_combination_eval
# LANG: _00K1, _axial_inflow_velocity --> _ux_2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01221__ux_2 = _00K2_constant+1*v01150__axial_inflow_velocity+1*v01229__00K1

# op _00LP_power_combination_eval
# LANG: Cd --> _00LQ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01302__00LQ = (v01183_Cd**1)
v01302__00LQ = (v01302__00LQ*_00LP_coeff).reshape((1, 40, 100))

# op _00LZ_linear_combination_eval
# LANG: _00LY, _tangential_inflow_velocity --> _00L_
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01308__00L_ = _00LZ_constant+1*v01160__tangential_inflow_velocity+-1*v01309__00LY

# op _00RX_indexed_passthrough_eval
# LANG: _00RW, _00RZ, _00S0 --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01480_V_aircraft__temp[i_v01479__00RW__00RX_indexed_passthrough_eval] = v01479__00RW.flatten()
v01480_V_aircraft = v01480_V_aircraft__temp.copy()
v01480_V_aircraft__temp[i_v01481__00RZ__00RX_indexed_passthrough_eval] = v01481__00RZ.flatten()
v01480_V_aircraft = v01480_V_aircraft__temp.copy()
v01480_V_aircraft__temp[i_v01482__00S0__00RX_indexed_passthrough_eval] = v01482__00S0.flatten()
v01480_V_aircraft = v01480_V_aircraft__temp.copy()

# op _00Ru_power_combination_eval
# LANG: pressure --> _00Rv
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01469__00Rv = (v01468_pressure**1)
v01469__00Rv = (v01469__00Rv*_00Ru_coeff).reshape((1,))

# op _00V4_decompose_eval
# LANG: lambda_test --> _00V5
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01636__00V5 = ((v01551_lambda_test.flatten())[src_indices__00V5__00V4]).reshape((1, 2, 3, 40, 10))

# op _00VC_bessel_eval
# LANG: _00Vz --> _00VD
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01578__00VD=_00VC_bessel_eval(1,v01569__00Vz)

# op _00VI_bessel_eval
# LANG: _00Vz --> _00VJ
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01581__00VJ=_00VI_bessel_eval(1,v01569__00Vz)

# op _00Wh_bessel_eval
# LANG: _00Vz --> _00Wi
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01600__00Wi=_00Wh_bessel_eval(1,v01569__00Vz)

# op _00Wn_bessel_eval
# LANG: _00Vz --> _00Wo
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01603__00Wo=_00Wn_bessel_eval(0,v01569__00Vz)

# op _00XA_linear_combination_eval
# LANG: _00Xr, _00Xz --> _00XB
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01660__00XB = _00XA_constant+1*v01654__00Xr+1*v01663__00Xz

# op _00XK_power_combination_eval
# LANG: _00XH, _00XJ --> _00XL
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01669__00XL = (v01667__00XH**1)*(v01670__00XJ**1)
v01669__00XL = (v01669__00XL*_00XK_coeff).reshape((1, 2, 3, 40, 10))

# op _00XQ_power_combination_eval
# LANG: _00XP --> _00XR
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01673__00XR = (v01672__00XP**2)
v01673__00XR = (v01673__00XR*_00XQ_coeff).reshape((1, 2, 3, 40, 10))

# op _00XS_bessel_eval
# LANG: _00Vz --> _00XT
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01675__00XT=_00XS_bessel_eval(1,v01569__00Vz)

# op _00XY_bessel_eval
# LANG: _00Vz --> _00XZ
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01677__00XZ=_00XY_bessel_eval(0,v01569__00Vz)

# op _00X__bessel_eval
# LANG: _00Vz --> _00Y0
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01679__00Y0=_00X__bessel_eval(1,v01569__00Vz)

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
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0565__00kZ = np.einsum('ab,c->abc', v0556_V_aircraft.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _00l3 expand_array_eval
# LANG: time_vectors --> _00l4
# SHAPES: (2,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0571__00l4 = np.einsum('c,ab->abc', v0570_time_vectors.reshape((2,)) ,np.ones((1, 3))).reshape((1, 3, 2))

# op _00Db_power_combination_eval
# LANG: propeller_radius --> _00Dc
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01121__00Dc = (v01052_propeller_radius**1)
v01121__00Dc = (v01121__00Dc*_00Db_coeff).reshape((1,))

# op _00IM expand_scalar_eval
# LANG: density --> _00IN
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01171_density = v01171_density.reshape((1,))
v01249__00IN = np.empty((1, 40, 100))
v01249__00IN.fill(v01171_density.item())
v01171_density = v01171_density.reshape((1, 1))

# op _00JB_power_combination_eval
# LANG: _00Jy, _00JA --> _00JC
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01212__00JC = (v01210__00Jy**1)*(v01213__00JA**1)
v01212__00JC = (v01212__00JC*_00JB_coeff).reshape((1, 40, 100))

# op _00JD_power_combination_eval
# LANG: _00Ja, _blade_solidity --> _00JE
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01215__00JE = (v01149__blade_solidity**1)*(v01218__00Ja**1)
v01215__00JE = (v01215__00JE*_00JD_coeff).reshape((1, 40, 100))

# op _00Jl_power_combination_eval
# LANG: _00Jk, _tangential_inflow_velocity --> _00Jm
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01204__00Jm = (v01203__00Jk**1)*(v01160__tangential_inflow_velocity**1)
v01204__00Jm = (v01204__00Jm*_00Jl_coeff).reshape((1, 40, 100))

# op _00Jp_power_combination_eval
# LANG: _00Jo --> _00Jq
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01207__00Jq = (v01206__00Jo**2)
v01207__00Jq = (v01207__00Jq*_00Jp_coeff).reshape((1, 40, 100))

# op _00LR_power_combination_eval
# LANG: _00LQ --> _00LS
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01303__00LS = (v01302__00LQ**1)
v01303__00LS = (v01303__00LS*_00LR_coeff).reshape((1, 40, 100))

# op _00LV_power_combination_eval
# LANG: _ux_2 --> _00LW
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01306__00LW = (v01221__ux_2**2)
v01306__00LW = (v01306__00LW*_00LV_coeff).reshape((1, 40, 100))

# op _00M0_power_combination_eval
# LANG: _00L_ --> _00M1
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01310__00M1 = (v01308__00L_**2)
v01310__00M1 = (v01310__00M1*_00M0_coeff).reshape((1, 40, 100))

# op _00Rw_power_combination_eval
# LANG: temperature, _00Rv --> density
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01470_density = (v01469__00Rv**1)*(v01465_temperature**-1)
v01470_density = (v01470_density*_00Rw_coeff).reshape((1,))

# op _00S1 expand_array_eval
# LANG: V_aircraft --> _00S2
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01489__00S2 = np.einsum('ab,c->abc', v01480_V_aircraft.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _00S7 expand_array_eval
# LANG: time_vectors --> _00S8
# SHAPES: (2,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01495__00S8 = np.einsum('c,ab->abc', v01494_time_vectors.reshape((2,)) ,np.ones((1, 3))).reshape((1, 3, 2))

# op _00VA_bessel_eval
# LANG: _00Vz --> _00VB
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01576__00VB=_00VA_bessel_eval(0,v01569__00Vz)

# op _00VE_power_combination_eval
# LANG: _00VD --> _00VF
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01579__00VF = (v01578__00VD**2)
v01579__00VF = (v01579__00VF*_00VE_coeff).reshape((1, 2, 3, 40, 10))

# op _00VK_power_combination_eval
# LANG: _00VJ --> _00VL
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01582__00VL = (v01581__00VJ**2)
v01582__00VL = (v01582__00VL*_00VK_coeff).reshape((1, 2, 3, 40, 10))

# op _00VM_bessel_eval
# LANG: _00Vz --> _00VN
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01584__00VN=_00VM_bessel_eval(1,v01569__00Vz)

# op _00VS_bessel_eval
# LANG: _00Vz --> _00VT
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01586__00VT=_00VS_bessel_eval(0,v01569__00Vz)

# op _00VU_bessel_eval
# LANG: _00Vz --> _00VV
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01588__00VV=_00VU_bessel_eval(1,v01569__00Vz)

# op _00Wf_bessel_eval
# LANG: _00Vz --> _00Wg
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01598__00Wg=_00Wf_bessel_eval(0,v01569__00Vz)

# op _00Wj_power_combination_eval
# LANG: _00Wi --> _00Wk
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01601__00Wk = (v01600__00Wi**2)
v01601__00Wk = (v01601__00Wk*_00Wj_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wp_power_combination_eval
# LANG: _00Wo --> _00Wq
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01604__00Wq = (v01603__00Wo**2)
v01604__00Wq = (v01604__00Wq*_00Wp_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wr_bessel_eval
# LANG: _00Vz --> _00Ws
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01606__00Ws=_00Wr_bessel_eval(1,v01569__00Vz)

# op _00Wx_bessel_eval
# LANG: _00Vz --> _00Wy
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01608__00Wy=_00Wx_bessel_eval(1,v01569__00Vz)

# op _00XM_linear_combination_eval
# LANG: _00XB, _00XL --> _00XN
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01665__00XN = _00XM_constant+1*v01660__00XB+1*v01669__00XL

# op _00XU_power_combination_eval
# LANG: _00XR, _00XT --> _00XV
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01674__00XV = (v01673__00XR**1)*(v01675__00XT**1)
v01674__00XV = (v01674__00XV*_00XU_coeff).reshape((1, 2, 3, 40, 10))

# op _00Y1_power_combination_eval
# LANG: _00XZ, _00Y0 --> _00Y2
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01678__00Y2 = (v01677__00XZ**1)*(v01679__00Y0**1)
v01678__00Y2 = (v01678__00Y2*_00Y1_coeff).reshape((1, 2, 3, 40, 10))

# op _00Y3_bessel_eval
# LANG: _00Vz --> _00Y4
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01681__00Y4=_00Y3_bessel_eval(1,v01569__00Vz)

# op _00Y9_bessel_eval
# LANG: _00Vz --> _00Ya
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01683__00Ya=_00Y9_bessel_eval(0,v01569__00Vz)

# op _00YR_power_combination_eval
# LANG: _00UL, _00V5 --> _00YS
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01637__00YS = (v01636__00V5**1)*(v01565__00UL**1)
v01637__00YS = (v01637__00YS*_00YR_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yb_bessel_eval
# LANG: _00Vz --> _00Yc
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01685__00Yc=_00Yb_bessel_eval(1,v01569__00Vz)

# op _00Z0_power_combination_eval
# LANG: _00UL, _00UJ --> _00Z1
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01631__00Z1 = (v01565__00UL**1)*(v01571__00UJ**1)
v01631__00Z1 = (v01631__00Z1*_00Z0_coeff).reshape((1, 2, 3, 40, 10))

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

# op _00Dd_linear_combination_eval
# LANG: _00Dc, propeller_radius --> _00De
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01120__00De = _00Dd_constant+1*v01052_propeller_radius+-1*v01121__00Dc

# op _00JF_linear_combination_eval
# LANG: _00JC, _00JE --> _00JG
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01214__00JG = _00JF_constant+1*v01212__00JC+1*v01215__00JE

# op _00Jr_power_combination_eval
# LANG: _00Jm, _00Jq --> _00Js
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01205__00Js = (v01204__00Jm**1)*(v01207__00Jq**1)
v01205__00Js = (v01205__00Js*_00Jr_coeff).reshape((1, 40, 100))

# op _00Ko_power_combination_eval
# LANG: _radius --> _00Kp
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01247__00Kp = (v01143__radius**1)
v01247__00Kp = (v01247__00Kp*_00Ko_coeff).reshape((1, 40, 100))

# op _00LT_power_combination_eval
# LANG: _00IN, _00LS --> _00LU
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01304__00LU = (v01303__00LS**1)*(v01249__00IN**1)
v01304__00LU = (v01304__00LU*_00LT_coeff).reshape((1, 40, 100))

# op _00M2_linear_combination_eval
# LANG: _00LW, _00M1 --> _00M3
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01307__00M3 = _00M2_constant+1*v01306__00LW+1*v01310__00M1

# op _00Pi_power_combination_eval
# LANG: rotor_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v01405_origin = (v012_rotor_disk_origin**1)
v01405_origin = (v01405_origin*_00Pi_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _00Pl_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _00Pm
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v01424__00Pm = (v010_rotor_disk_in_plane_2**1)
v01424__00Pm = (v01424__00Pm*_00Pl_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _00S4 expand_array_eval
# LANG: aircraft_location --> _00S5
# SHAPES: (3, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01484__00S5 = np.einsum('bc,a->abc', v01483_aircraft_location.reshape((3, 2)) ,np.ones((1,))).reshape((1, 3, 2))

# op _00Sb_decompose_eval
# LANG: _00S2 --> _00Sc, _00Sk, _00Sr
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01490__00Sc = ((v01489__00S2.flatten())[src_indices__00Sc__00Sb]).reshape((1, 1, 2))
v01491__00Sk = ((v01489__00S2.flatten())[src_indices__00Sk__00Sb]).reshape((1, 1, 2))
v01492__00Sr = ((v01489__00S2.flatten())[src_indices__00Sr__00Sb]).reshape((1, 1, 2))

# op _00Sd_decompose_eval
# LANG: _00S8 --> _00Se, _00Sl, _00Ss
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01496__00Se = ((v01495__00S8.flatten())[src_indices__00Se__00Sd]).reshape((1, 1, 2))
v01497__00Sl = ((v01495__00S8.flatten())[src_indices__00Sl__00Sd]).reshape((1, 1, 2))
v01498__00Ss = ((v01495__00S8.flatten())[src_indices__00Ss__00Sd]).reshape((1, 1, 2))

# op _00UE expand_scalar_eval
# LANG: density --> _00UF
# SHAPES: (1,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01628__00UF = np.empty((1, 2, 3, 40, 11))
v01628__00UF.fill(v01470_density.item())

# op _00VG_power_combination_eval
# LANG: _00VB, _00VF --> _00VH
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01577__00VH = (v01576__00VB**1)*(v01579__00VF**1)
v01577__00VH = (v01577__00VH*_00VG_coeff).reshape((1, 2, 3, 40, 10))

# op _00VO_power_combination_eval
# LANG: _00VL, _00VN --> _00VP
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01583__00VP = (v01582__00VL**1)*(v01584__00VN**1)
v01583__00VP = (v01583__00VP*_00VO_coeff).reshape((1, 2, 3, 40, 10))

# op _00VW_power_combination_eval
# LANG: _00VT, _00VV --> _00VX
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01587__00VX = (v01586__00VT**1)*(v01588__00VV**1)
v01587__00VX = (v01587__00VX*_00VW_coeff).reshape((1, 2, 3, 40, 10))

# op _00VY_bessel_eval
# LANG: _00Vz --> _00VZ
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01590__00VZ=_00VY_bessel_eval(0,v01569__00Vz)

# op _00W3_bessel_eval
# LANG: _00Vz --> _00W4
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01592__00W4=_00W3_bessel_eval(1,v01569__00Vz)

# op _00W5_bessel_eval
# LANG: _00Vz --> _00W6
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01594__00W6=_00W5_bessel_eval(0,v01569__00Vz)

# op _00WB_bessel_eval
# LANG: _00Vz --> _00WC
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01611__00WC=_00WB_bessel_eval(1,v01569__00Vz)

# op _00WJ_bessel_eval
# LANG: _00Vz --> _00WK
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01615__00WK=_00WJ_bessel_eval(1,v01569__00Vz)

# op _00Wl_power_combination_eval
# LANG: _00Wg, _00Wk --> _00Wm
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01599__00Wm = (v01598__00Wg**1)*(v01601__00Wk**1)
v01599__00Wm = (v01599__00Wm*_00Wl_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wt_power_combination_eval
# LANG: _00Wq, _00Ws --> _00Wu
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01605__00Wu = (v01604__00Wq**1)*(v01606__00Ws**1)
v01605__00Wu = (v01605__00Wu*_00Wt_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wz_power_combination_eval
# LANG: _00Wy --> _00WA
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01609__00WA = (v01608__00Wy**2)
v01609__00WA = (v01609__00WA*_00Wz_coeff).reshape((1, 2, 3, 40, 10))

# op _00XW_linear_combination_eval
# LANG: _00XN, _00XV --> _00XX
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01671__00XX = _00XW_constant+1*v01665__00XN+1*v01674__00XV

# op _00Y5_power_combination_eval
# LANG: _00Y2, _00Y4 --> _00Y6
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01680__00Y6 = (v01678__00Y2**1)*(v01681__00Y4**1)
v01680__00Y6 = (v01680__00Y6*_00Y5_coeff).reshape((1, 2, 3, 40, 10))

# op _00YT_power_combination_eval
# LANG: _00UN, _00YS --> _00YU
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01638__00YU = (v01637__00YS**1)*(v01574__00UN**1)
v01638__00YU = (v01638__00YU*_00YT_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yd_power_combination_eval
# LANG: _00Ya, _00Yc --> _00Ye
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01684__00Ye = (v01683__00Ya**1)*(v01685__00Yc**1)
v01684__00Ye = (v01684__00Ye*_00Yd_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yf_bessel_eval
# LANG: _00Vz --> _00Yg
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01687__00Yg=_00Yf_bessel_eval(1,v01569__00Vz)

# op _00Yn_bessel_eval
# LANG: _00Vz --> _00Yo
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01691__00Yo=_00Yn_bessel_eval(1,v01569__00Vz)

# op _00Z2_power_combination_eval
# LANG: _00UN, _00Z1 --> _00Z3
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01632__00Z3 = (v01631__00Z1**1)*(v01574__00UN**1)
v01632__00Z3 = (v01632__00Z3*_00Z2_coeff).reshape((1, 2, 3, 40, 10))

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

# op _005Y_power_combination_eval
# LANG: propeller_radius --> _005Z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0195__005Z = (v0128_propeller_radius**1)
v0195__005Z = (v0195__005Z*_005Y_coeff).reshape((1,))

# op _00Df_power_combination_eval
# LANG: _00De --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v01122_dr = (v01120__00De**1)
v01122_dr = (v01122_dr*_00Df_coeff).reshape((1,))

# op _00JH_power_combination_eval
# LANG: _00Js, _00JG --> _ux
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01208__ux = (v01205__00Js**1)*(v01214__00JG**-1)
v01208__ux = (v01208__ux*_00JH_coeff).reshape((1, 40, 100))

# op _00Kq_power_combination_eval
# LANG: _00Kp, _00IN --> _00Kr
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01248__00Kr = (v01247__00Kp**1)*(v01249__00IN**1)
v01248__00Kr = (v01248__00Kr*_00Kq_coeff).reshape((1, 40, 100))

# op _00M4_power_combination_eval
# LANG: _00LU, _00M3 --> _00M5
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01305__00M5 = (v01304__00LU**1)*(v01307__00M3**1)
v01305__00M5 = (v01305__00M5*_00M4_coeff).reshape((1, 40, 100))

# op _00PV cross_product_eval
# LANG: _00Pg, _00Pm --> _00PW
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01425__00PW = np.cross(v01424__00Pm, v01406__00Pg, axisa = 0, axisb = 0, axisc = 0)

# op _00Qb_power_combination_eval
# LANG: propeller_radius --> _00Qc
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01429__00Qc = (v01408_propeller_radius**1)
v01429__00Qc = (v01429__00Qc*_00Qb_coeff).reshape((1,))

# op _00S9_decompose_eval
# LANG: _00S5 --> _00Sa, _00Sj, _00Sq
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01485__00Sa = ((v01484__00S5.flatten())[src_indices__00Sa__00S9]).reshape((1, 1, 2))
v01486__00Sj = ((v01484__00S5.flatten())[src_indices__00Sj__00S9]).reshape((1, 1, 2))
v01487__00Sq = ((v01484__00S5.flatten())[src_indices__00Sq__00S9]).reshape((1, 1, 2))

# op _00SE expand_array_eval
# LANG: origin --> _00SF
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01507__00SF = np.einsum('b,ac->abc', v01405_origin.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00Sf_power_combination_eval
# LANG: _00Sc, _00Se --> _00Sg
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01493__00Sg = (v01490__00Sc**1)*(v01496__00Se**1)
v01493__00Sg = (v01493__00Sg*_00Sf_coeff).reshape((1, 1, 2))

# op _00Sm_power_combination_eval
# LANG: _00Sk, _00Sl --> _00Sn
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01500__00Sn = (v01491__00Sk**1)*(v01497__00Sl**1)
v01500__00Sn = (v01500__00Sn*_00Sm_coeff).reshape((1, 1, 2))

# op _00US_decompose_eval
# LANG: _00UF --> _00UT
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01629__00UT = ((v01628__00UF.flatten())[src_indices__00UT__00US]).reshape((1, 2, 3, 40, 10))

# op _00VQ_linear_combination_eval
# LANG: _00VH, _00VP --> _00VR
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01580__00VR = _00VQ_constant+1*v01577__00VH+-1*v01583__00VP

# op _00V__power_combination_eval
# LANG: _00VX, _00VZ --> _00W0
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01589__00W0 = (v01587__00VX**1)*(v01590__00VZ**1)
v01589__00W0 = (v01589__00W0*_00V__coeff).reshape((1, 2, 3, 40, 10))

# op _00W7_power_combination_eval
# LANG: _00W4, _00W6 --> _00W8
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01593__00W8 = (v01592__00W4**1)*(v01594__00W6**1)
v01593__00W8 = (v01593__00W8*_00W7_coeff).reshape((1, 2, 3, 40, 10))

# op _00W9_bessel_eval
# LANG: _00Vz --> _00Wa
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01596__00Wa=_00W9_bessel_eval(1,v01569__00Vz)

# op _00WD_power_combination_eval
# LANG: _00WA, _00WC --> _00WE
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01610__00WE = (v01609__00WA**1)*(v01611__00WC**1)
v01610__00WE = (v01610__00WE*_00WD_coeff).reshape((1, 2, 3, 40, 10))

# op _00WH_bessel_eval
# LANG: _00Vz --> _00WI
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01613__00WI=_00WH_bessel_eval(0,v01569__00Vz)

# op _00WL_power_combination_eval
# LANG: _00WK --> _00WM
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01616__00WM = (v01615__00WK**2)
v01616__00WM = (v01616__00WM*_00WL_coeff).reshape((1, 2, 3, 40, 10))

# op _00WT_bessel_eval
# LANG: _00Vz --> _00WU
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01618__00WU=_00WT_bessel_eval(1,v01569__00Vz)

# op _00WV_bessel_eval
# LANG: _00Vz --> _00WW
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01620__00WW=_00WV_bessel_eval(0,v01569__00Vz)

# op _00Wv_linear_combination_eval
# LANG: _00Wm, _00Wu --> _00Ww
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01602__00Ww = _00Wv_constant+1*v01599__00Wm+1*v01605__00Wu

# op _00X0_bessel_eval
# LANG: _00Vz --> _00X1
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01623__00X1=_00X0_bessel_eval(0,v01569__00Vz)

# op _00X2_bessel_eval
# LANG: _00Vz --> _00X3
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01625__00X3=_00X2_bessel_eval(1,v01569__00Vz)

# op _00Y7_linear_combination_eval
# LANG: _00XX, _00Y6 --> _00Y8
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01676__00Y8 = _00Y7_constant+1*v01671__00XX+-1*v01680__00Y6

# op _00YF_bessel_eval
# LANG: _00Vz --> _00YG
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01700__00YG=_00YF_bessel_eval(0,v01569__00Vz)

# op _00YH_bessel_eval
# LANG: _00Vz --> _00YI
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01702__00YI=_00YH_bessel_eval(1,v01569__00Vz)

# op _00YV_power_combination_eval
# LANG: _00Vn, _00YU --> _00YW
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01639__00YW = (v01638__00YU**1)*(v01559__00Vn**-1)
v01639__00YW = (v01639__00YW*_00YV_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yh_power_combination_eval
# LANG: _00Ye, _00Yg --> _00Yi
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01686__00Yi = (v01684__00Ye**1)*(v01687__00Yg**1)
v01686__00Yi = (v01686__00Yi*_00Yh_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yl_bessel_eval
# LANG: _00Vz --> _00Ym
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01689__00Ym=_00Yl_bessel_eval(1,v01569__00Vz)

# op _00Yp_power_combination_eval
# LANG: _00Yo --> _00Yq
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01692__00Yq = (v01691__00Yo**2)
v01692__00Yq = (v01692__00Yq*_00Yp_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yx_bessel_eval
# LANG: _00Vz --> _00Yy
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01695__00Yy=_00Yx_bessel_eval(1,v01569__00Vz)

# op _00Yz_bessel_eval
# LANG: _00Vz --> _00YA
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01697__00YA=_00Yz_bessel_eval(0,v01569__00Vz)

# op _00Z4_linear_combination_eval
# LANG: _00Z3 --> _00Z5
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01633__00Z5 = _00Z4_constant+1*v01632__00Z3

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

# op _005__linear_combination_eval
# LANG: _005Z, propeller_radius --> _0060
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0194__0060 = _005__constant+1*v0128_propeller_radius+-1*v0195__005Z

# op _00En expand_scalar_eval
# LANG: dr --> _dr
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_core_inputs_model
v01131__dr = np.empty((1, 40, 100))
v01131__dr.fill(v01122_dr.item())

# op _00Ks_power_combination_eval
# LANG: _ux, _00Kr --> _00Kt
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01250__00Kt = (v01248__00Kr**1)*(v01208__ux**1)
v01250__00Kt = (v01250__00Kt*_00Ks_coeff).reshape((1, 40, 100))

# op _00Ku_linear_combination_eval
# LANG: _ux, _axial_inflow_velocity --> _00Kv
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01252__00Kv = _00Ku_constant+1*v01208__ux+-1*v01150__axial_inflow_velocity

# op _00M6_power_combination_eval
# LANG: _00M5, _chord --> _00M7
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01311__00M7 = (v01305__00M5**1)*(v01138__chord**1)
v01311__00M7 = (v01311__00M7*_00M6_coeff).reshape((1, 40, 100))

# op _00PA_linear_combination_eval
# LANG: theta --> _00PB
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0970_theta = v0970_theta.reshape((1, 1))
v01412__00PB = _00PA_constant+1*v0970_theta
v0970_theta = v0970_theta.reshape((1,))

# op _00PC_linear_combination_eval
# LANG: theta --> _00PD
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0970_theta = v0970_theta.reshape((1, 1))
v01414__00PD = _00PC_constant+1*v0970_theta
v0970_theta = v0970_theta.reshape((1,))

# op _00PJ_sin_eval
# LANG: theta --> _00PK
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0970_theta = v0970_theta.reshape((1, 1))
v01417__00PK = np.sin(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _00PN_sin_eval
# LANG: theta --> _00PO
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0970_theta = v0970_theta.reshape((1, 1))
v01419__00PO = np.sin(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _00PR_cos_eval
# LANG: theta --> _00PS
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0970_theta = v0970_theta.reshape((1, 1))
v01421__00PS = np.cos(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _00PX pnorm_eval
# LANG: _00PW --> _00PY
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01427__00PY = np.linalg.norm(v01425__00PW.flatten(), ord=2)

# op _00Qd_power_combination_eval
# LANG: _00Qc --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01430_dr = (v01429__00Qc**1)
v01430_dr = (v01430_dr*_00Qd_coeff).reshape((1,))

# op _00SG_decompose_eval
# LANG: _00SF --> _00SH, _00SM, _00SR
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01508__00SH = ((v01507__00SF.flatten())[src_indices__00SH__00SG]).reshape((1, 1, 2))
v01509__00SM = ((v01507__00SF.flatten())[src_indices__00SM__00SG]).reshape((1, 1, 2))
v01510__00SR = ((v01507__00SF.flatten())[src_indices__00SR__00SG]).reshape((1, 1, 2))

# op _00Sh_linear_combination_eval
# LANG: _00Sa, _00Sg --> aircraft_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01488_aircraft_x_pos = _00Sh_constant+1*v01485__00Sa+1*v01493__00Sg

# op _00So_linear_combination_eval
# LANG: _00Sj, _00Sn --> aircraft_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01499_aircraft_y_pos = _00So_constant+1*v01486__00Sj+1*v01500__00Sn

# op _00St_power_combination_eval
# LANG: _00Sr, _00Ss --> _00Su
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01502__00Su = (v01492__00Sr**1)*(v01498__00Ss**1)
v01502__00Su = (v01502__00Su*_00St_coeff).reshape((1, 1, 2))

# op _00W1_linear_combination_eval
# LANG: _00VR, _00W0 --> _00W2
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01585__00W2 = _00W1_constant+1*v01580__00VR+1*v01589__00W0

# op _00WF_linear_combination_eval
# LANG: _00Ww, _00WE --> _00WG
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01607__00WG = _00WF_constant+1*v01602__00Ww+-1*v01610__00WE

# op _00WN_power_combination_eval
# LANG: _00WI, _00WM --> _00WO
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01614__00WO = (v01613__00WI**1)*(v01616__00WM**1)
v01614__00WO = (v01614__00WO*_00WN_coeff).reshape((1, 2, 3, 40, 10))

# op _00WX_linear_combination_eval
# LANG: _00WU, _00WW --> _00WY
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01619__00WY = _00WX_constant+1*v01618__00WU+1*v01620__00WW

# op _00Wb_power_combination_eval
# LANG: _00W8, _00Wa --> _00Wc
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01595__00Wc = (v01593__00W8**1)*(v01596__00Wa**1)
v01595__00Wc = (v01595__00Wc*_00Wb_coeff).reshape((1, 2, 3, 40, 10))

# op _00X4_linear_combination_eval
# LANG: _00X1, _00X3 --> _00X5
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01624__00X5 = _00X4_constant+1*v01623__00X1+-1*v01625__00X3

# op _00YB_linear_combination_eval
# LANG: _00Yy, _00YA --> _00YC
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01696__00YC = _00YB_constant+1*v01695__00Yy+1*v01697__00YA

# op _00YJ_linear_combination_eval
# LANG: _00YG, _00YI --> _00YK
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01701__00YK = _00YJ_constant+1*v01700__00YG+-1*v01702__00YI

# op _00YX_power_combination_eval
# LANG: _00YW --> _00YY
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01640__00YY = (v01639__00YW**1)
v01640__00YY = (v01640__00YY*_00YX_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yj_linear_combination_eval
# LANG: _00Y8, _00Yi --> _00Yk
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01682__00Yk = _00Yj_constant+1*v01676__00Y8+-1*v01686__00Yi

# op _00Yr_power_combination_eval
# LANG: _00Ym, _00Yq --> _00Ys
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01690__00Ys = (v01689__00Ym**1)*(v01692__00Yq**1)
v01690__00Ys = (v01690__00Ys*_00Yr_coeff).reshape((1, 2, 3, 40, 10))

# op _00Z6_power_combination_eval
# LANG: _00UT, _00Z5 --> _00Z7
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01630__00Z7 = (v01629__00UT**1)*(v01633__00Z5**1)
v01630__00Z7 = (v01630__00Z7*_00Z6_coeff).reshape((1, 2, 3, 40, 10))

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

# op _0061_power_combination_eval
# LANG: _0060 --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_external_inputs_model
v0196_dr = (v0194__0060**1)
v0196_dr = (v0196_dr*_0061_coeff).reshape((1,))

# op _00Kw_power_combination_eval
# LANG: _00Kt, _00Kv --> _00Kx
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01251__00Kx = (v01250__00Kt**1)*(v01252__00Kv**1)
v01251__00Kx = (v01251__00Kx*_00Kw_coeff).reshape((1, 40, 100))

# op _00M8_power_combination_eval
# LANG: _00M7, _dr --> _dD
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01312__dD = (v01311__00M7**1)*(v01131__dr**1)
v01312__dD = (v01312__dD*_00M8_coeff).reshape((1, 40, 100))

# op _00PE_power_combination_eval
# LANG: _00PB, _00PD --> _00PF
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01413__00PF = (v01412__00PB**1)*(v01414__00PD**-1)
v01413__00PF = (v01413__00PF*_00PE_coeff).reshape((1, 1))

# op _00PH_cos_eval
# LANG: theta --> _00PI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v0970_theta = v0970_theta.reshape((1, 1))
v01416__00PI = np.cos(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _00PL_power_combination_eval
# LANG: _00PK --> _00PM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01418__00PM = (v01417__00PK**1)
v01418__00PM = (v01418__00PM*_00PL_coeff).reshape((1, 1))

# op _00PP_power_combination_eval
# LANG: _00PO --> _00PQ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01420__00PQ = (v01419__00PO**1)
v01420__00PQ = (v01420__00PQ*_00PP_coeff).reshape((1, 1))

# op _00PT_power_combination_eval
# LANG: _00PS --> _00PU
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01422__00PU = (v01421__00PS**1)
v01422__00PU = (v01422__00PU*_00PT_coeff).reshape((1, 1))

# op _00PZ expand_scalar_eval
# LANG: _00PY --> _00P_
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01428__00P_ = np.empty((3,))
v01428__00P_.fill(v01427__00PY.item())

# op _00SI_linear_combination_eval
# LANG: aircraft_x_pos, _00SH --> _00SJ
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01506__00SJ = _00SI_constant+1*v01488_aircraft_x_pos+1*v01508__00SH

# op _00SN_linear_combination_eval
# LANG: aircraft_y_pos, _00SM --> _00SO
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01514__00SO = _00SN_constant+1*v01499_aircraft_y_pos+1*v01509__00SM

# op _00Sv_linear_combination_eval
# LANG: _00Sq, _00Su --> aircraft_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01501_aircraft_z_pos = _00Sv_constant+1*v01487__00Sq+1*v01502__00Su

# op _00Sx expand_array_eval
# LANG: init_obs_x_loc --> _00Sy
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01504__00Sy = np.einsum('c,ab->abc', v01503_init_obs_x_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00Sz expand_array_eval
# LANG: init_obs_y_loc --> _00SA
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01512__00SA = np.einsum('c,ab->abc', v01511_init_obs_y_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00Ug expand_scalar_eval
# LANG: dr --> _00Uh
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01547__00Uh = np.empty((1, 40, 100))
v01547__00Uh.fill(v01430_dr.item())

# op _00WP_linear_combination_eval
# LANG: _00WG, _00WO --> _00WQ
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01612__00WQ = _00WP_constant+1*v01607__00WG+-1*v01614__00WO

# op _00WZ_power_combination_eval
# LANG: _00WY --> _00W_
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01621__00W_ = (v01619__00WY**2)
v01621__00W_ = (v01621__00W_*_00WZ_coeff).reshape((1, 2, 3, 40, 10))

# op _00Wd_linear_combination_eval
# LANG: _00W2, _00Wc --> _00We
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01591__00We = _00Wd_constant+1*v01585__00W2+-1*v01595__00Wc

# op _00X6_power_combination_eval
# LANG: _00X5 --> _00X7
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01626__00X7 = (v01624__00X5**2)
v01626__00X7 = (v01626__00X7*_00X6_coeff).reshape((1, 2, 3, 40, 10))

# op _00YD_power_combination_eval
# LANG: _00YC --> _00YE
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01698__00YE = (v01696__00YC**2)
v01698__00YE = (v01698__00YE*_00YD_coeff).reshape((1, 2, 3, 40, 10))

# op _00YL_power_combination_eval
# LANG: _00YK --> _00YM
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01703__00YM = (v01701__00YK**2)
v01703__00YM = (v01703__00YM*_00YL_coeff).reshape((1, 2, 3, 40, 10))

# op _00YZ_power_combination_eval
# LANG: _00YY --> _00Y_
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01641__00Y_ = (v01640__00YY**1)
v01641__00Y_ = (v01641__00Y_*_00YZ_coeff).reshape((1, 2, 3, 40, 10))

# op _00Yt_linear_combination_eval
# LANG: _00Yk, _00Ys --> _00Yu
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01688__00Yu = _00Yt_constant+1*v01682__00Yk+1*v01690__00Ys

# op _00Z8_power_combination_eval
# LANG: _00UR, _00Z7 --> _00Z9
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01634__00Z9 = (v01630__00Z7**1)*(v01568__00UR**1)
v01634__00Z9 = (v01634__00Z9*_00Z8_coeff).reshape((1, 2, 3, 40, 10))

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

# op _0079 expand_scalar_eval
# LANG: dr --> _dr
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.BEM_core_inputs_model
v0205__dr = np.empty((1, 40, 30))
v0205__dr.fill(v0196_dr.item())

# op _00Ky_power_combination_eval
# LANG: _00Kx, prandtl_loss_factor --> _00Kz
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01253__00Kz = (v01251__00Kx**1)*(v01193_prandtl_loss_factor**1)
v01253__00Kz = (v01253__00Kz*_00Ky_coeff).reshape((1, 40, 100))

# op _00PG_indexed_passthrough_eval
# LANG: _00PF, _00PI, _00PM, _00PQ, _00PU --> rot_mat
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01415_rot_mat__temp[i_v01413__00PF__00PG_indexed_passthrough_eval] = v01413__00PF.flatten()
v01415_rot_mat = v01415_rot_mat__temp.copy()
v01415_rot_mat__temp[i_v01416__00PI__00PG_indexed_passthrough_eval] = v01416__00PI.flatten()
v01415_rot_mat = v01415_rot_mat__temp.copy()
v01415_rot_mat__temp[i_v01418__00PM__00PG_indexed_passthrough_eval] = v01418__00PM.flatten()
v01415_rot_mat = v01415_rot_mat__temp.copy()
v01415_rot_mat__temp[i_v01420__00PQ__00PG_indexed_passthrough_eval] = v01420__00PQ.flatten()
v01415_rot_mat = v01415_rot_mat__temp.copy()
v01415_rot_mat__temp[i_v01422__00PU__00PG_indexed_passthrough_eval] = v01422__00PU.flatten()
v01415_rot_mat = v01415_rot_mat__temp.copy()

# op _00Q0_power_combination_eval
# LANG: _00PW, _00P_ --> _00Q1
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01426__00Q1 = (v01425__00PW**1)*(v01428__00P_**-1)
v01426__00Q1 = (v01426__00Q1*_00Q0_coeff).reshape((3,))

# op _00SB expand_array_eval
# LANG: init_obs_z_loc --> _00SC
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01516__00SC = np.einsum('c,ab->abc', v01515_init_obs_z_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00SK_linear_combination_eval
# LANG: _00Sy, _00SJ --> rel_obs_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01505_rel_obs_x_pos = _00SK_constant+1*v01504__00Sy+-1*v01506__00SJ

# op _00SP_linear_combination_eval
# LANG: _00SA, _00SO --> rel_obs_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01513_rel_obs_y_pos = _00SP_constant+1*v01512__00SA+-1*v01514__00SO

# op _00SS_linear_combination_eval
# LANG: aircraft_z_pos, _00SR --> _00ST
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01518__00ST = _00SS_constant+1*v01501_aircraft_z_pos+1*v01510__00SR

# op _00Ui_power_combination_eval
# LANG: _00Uh, _dD --> bbb
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01546_bbb = (v01312__dD**1)*(v01547__00Uh**-1)
v01546_bbb = (v01546_bbb*_00Ui_coeff).reshape((1, 40, 100))

# op _00WR_linear_combination_eval
# LANG: _00We, _00WQ --> _00WS
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01597__00WS = _00WR_constant+1*v01591__00We+-1*v01612__00WQ

# op _00X8_linear_combination_eval
# LANG: _00W_, _00X7 --> _00X9
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01622__00X9 = _00X8_constant+1*v01621__00W_+1*v01626__00X7

# op _00YN_linear_combination_eval
# LANG: _00YE, _00YM --> _00YO
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01699__00YO = _00YN_constant+1*v01698__00YE+1*v01703__00YM

# op _00Yv_linear_combination_eval
# LANG: _00Yu --> _00Yw
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01693__00Yw = _00Yv_constant+-1*v01688__00Yu

# op _00Za_power_combination_eval
# LANG: _00Z9, _00Y_ --> _00Zb
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01635__00Zb = (v01634__00Z9**1)*(v01641__00Y_**1)
v01635__00Zb = (v01635__00Zb*_00Za_coeff).reshape((1, 2, 3, 40, 10))

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

# op _00KA_power_combination_eval
# LANG: _00Kz, _dr --> _local_thrust
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01254__local_thrust = (v01253__00Kz**1)*(v01131__dr**1)
v01254__local_thrust = (v01254__local_thrust*_00KA_coeff).reshape((1, 40, 100))

# op _00Q2_matvec_eval
# LANG: rot_mat, _00Q1 --> thrust_dir
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01423_thrust_dir = v01415_rot_mat@v01426__00Q1

# op _00SU_linear_combination_eval
# LANG: _00SC, _00ST --> rel_obs_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01517_rel_obs_z_pos = _00SU_constant+1*v01516__00SC+-1*v01518__00ST

# op _00SY_power_combination_eval
# LANG: rel_obs_x_pos --> _00SZ
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01520__00SZ = (v01505_rel_obs_x_pos**2)
v01520__00SZ = (v01520__00SZ*_00SY_coeff).reshape((1, 1, 2))

# op _00S__power_combination_eval
# LANG: rel_obs_y_pos --> _00T0
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01522__00T0 = (v01513_rel_obs_y_pos**2)
v01522__00T0 = (v01522__00T0*_00S__coeff).reshape((1, 1, 2))

# op _00Uo_decompose_eval
# LANG: bbb --> _00Up
# SHAPES: (1, 40, 100) --> (1, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01646__00Up = ((v01546_bbb.flatten())[src_indices__00Up__00Uo]).reshape((1, 40, 1))

# op _00V2_decompose_eval
# LANG: _00U_ --> _00V3
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01644__00V3 = ((v01550__00U_.flatten())[src_indices__00V3__00V2]).reshape((1, 2, 3, 40, 10))

# op _00Xa_power_combination_eval
# LANG: _00WS, _00X9 --> _00Xb
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01617__00Xb = (v01597__00WS**1)*(v01622__00X9**-1)
v01617__00Xb = (v01617__00Xb*_00Xa_coeff).reshape((1, 2, 3, 40, 10))

# op _00YP_power_combination_eval
# LANG: _00Yw, _00YO --> _00YQ
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01694__00YQ = (v01693__00Yw**1)*(v01699__00YO**-1)
v01694__00YQ = (v01694__00YQ*_00YP_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zc_power_combination_eval
# LANG: _00Zb --> _00Zd
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01642__00Zd = (v01635__00Zb**1)
v01642__00Zd = (v01642__00Zd*_00Zc_coeff).reshape((1, 2, 3, 40, 10))

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
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0597__00lZ = _00lY_constant+1*v0596__00lV+1*v0598__00lX

# op _00l__power_combination_eval
# LANG: rel_obs_z_pos --> _00m0
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0600__00m0 = (v0593_rel_obs_z_pos**2)
v0600__00m0 = (v0600__00m0*_00l__coeff).reshape((1, 1, 2))

# op _00os expand_scalar_eval
# LANG: Vx --> _00ot
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0656__00ot = np.empty((1, 2))
v0656__00ot.fill(v030_u.item())

# op _00ov expand_scalar_eval
# LANG: Vy --> _00ow
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0659__00ow = np.empty((1, 2))
v0659__00ow.fill(v035_v.item())

# op _00oy expand_scalar_eval
# LANG: Vz --> _00oz
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0661__00oz = np.empty((1, 2))
v0661__00oz.fill(v039_w.item())

# op _00P7_power_combination_eval
# LANG: _local_thrust --> _dT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01255__dT = (v01254__local_thrust**1)
v01255__dT = (v01255__dT*_00P7_coeff).reshape((1, 40, 100))

# op _00SX_indexed_passthrough_eval
# LANG: rel_obs_x_pos, rel_obs_y_pos, rel_obs_z_pos --> rel_obs_position
# SHAPES: (1, 1, 2), (1, 1, 2), (1, 1, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01519_rel_obs_position__temp[i_v01505_rel_obs_x_pos__00SX_indexed_passthrough_eval] = v01505_rel_obs_x_pos.flatten()
v01519_rel_obs_position = v01519_rel_obs_position__temp.copy()
v01519_rel_obs_position__temp[i_v01513_rel_obs_y_pos__00SX_indexed_passthrough_eval] = v01513_rel_obs_y_pos.flatten()
v01519_rel_obs_position = v01519_rel_obs_position__temp.copy()
v01519_rel_obs_position__temp[i_v01517_rel_obs_z_pos__00SX_indexed_passthrough_eval] = v01517_rel_obs_z_pos.flatten()
v01519_rel_obs_position = v01519_rel_obs_position__temp.copy()

# op _00T1_linear_combination_eval
# LANG: _00SZ, _00T0 --> _00T2
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01521__00T2 = _00T1_constant+1*v01520__00SZ+1*v01522__00T0

# op _00T3_power_combination_eval
# LANG: rel_obs_z_pos --> _00T4
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01524__00T4 = (v01517_rel_obs_z_pos**2)
v01524__00T4 = (v01524__00T4*_00T3_coeff).reshape((1, 1, 2))

# op _00Ta expand_array_eval
# LANG: thrust_dir --> _00Tb
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01527__00Tb = np.einsum('b,ac->abc', v01423_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00Uc expand_scalar_eval
# LANG: dr --> _00Ud
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01545__00Ud = np.empty((1, 40, 100))
v01545__00Ud.fill(v01430_dr.item())

# op _00Uq reshape_eval
# LANG: _00Up --> _00Ur
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01647__00Ur = v01646__00Up.reshape((1, 40))

# op _00Ze_power_combination_eval
# LANG: _00Xb, _00Zd --> _00Zf
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01627__00Zf = (v01617__00Xb**1)*(v01642__00Zd**1)
v01627__00Zf = (v01627__00Zf*_00Ze_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zg_power_combination_eval
# LANG: _00Zd, _00YQ --> _00Zh
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01704__00Zh = (v01694__00YQ**1)*(v01642__00Zd**1)
v01704__00Zh = (v01704__00Zh*_00Zg_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zm_sin_eval
# LANG: _00V3 --> _00Zn
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01651__00Zn = np.sin(v01644__00V3)

# op _00Zv_sin_eval
# LANG: _00V3 --> _00Zw
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01709__00Zw = np.sin(v01644__00V3)

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
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0599__00m2 = _00m1_constant+1*v0597__00lZ+1*v0600__00m0

# op _00oC reshape_eval
# LANG: _00ot --> _00oD
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0657__00oD = v0656__00ot.reshape((1, 1, 2))

# op _00oF reshape_eval
# LANG: _00ow --> _00oG
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0660__00oG = v0659__00ow.reshape((1, 1, 2))

# op _00oH reshape_eval
# LANG: _00oz --> _00oI
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0662__00oI = v0661__00oz.reshape((1, 1, 2))

# op _00T5_linear_combination_eval
# LANG: _00T2, _00T4 --> _00T6
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01523__00T6 = _00T5_constant+1*v01521__00T2+1*v01524__00T4

# op _00Tc_tensor_dot_product_eval
# LANG: rel_obs_position, _00Tb --> normal_proj
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01526_normal_proj = np.sum(v01519_rel_obs_position * v01527__00Tb, axis=1)

# op _00Ue_power_combination_eval
# LANG: _00Ud, _dT --> aaa
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01544_aaa = (v01255__dT**1)*(v01545__00Ud**-1)
v01544_aaa = (v01544_aaa*_00Ue_coeff).reshape((1, 40, 100))

# op _00Vj expand_array_eval
# LANG: _00Ur --> _00Vk
# SHAPES: (1, 40) --> (1, 2, 3, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01648__00Vk = np.einsum('ad,bce->abcde', v01647__00Ur.reshape((1, 40)) ,np.ones((2, 3, 1))).reshape((1, 2, 3, 40, 1))

# op _00Zo_power_combination_eval
# LANG: _00Zf, _00Zn --> _00Zp
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01650__00Zp = (v01627__00Zf**1)*(v01651__00Zn**1)
v01650__00Zp = (v01650__00Zp*_00Zo_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zx_power_combination_eval
# LANG: _00Zh, _00Zw --> _00Zy
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01708__00Zy = (v01704__00Zh**1)*(v01709__00Zw**1)
v01708__00Zy = (v01708__00Zy*_00Zx_coeff).reshape((1, 2, 3, 40, 10))

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
# SHAPES: (1, 1, 2), (1, 1, 2), (1, 1, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0658_aircraft_vel__temp[i_v0657__00oD__00oE_indexed_passthrough_eval] = v0657__00oD.flatten()
v0658_aircraft_vel = v0658_aircraft_vel__temp.copy()
v0658_aircraft_vel__temp[i_v0660__00oG__00oE_indexed_passthrough_eval] = v0660__00oG.flatten()
v0658_aircraft_vel = v0658_aircraft_vel__temp.copy()
v0658_aircraft_vel__temp[i_v0662__00oI__00oE_indexed_passthrough_eval] = v0662__00oI.flatten()
v0658_aircraft_vel = v0658_aircraft_vel__temp.copy()

# op _00T7_power_combination_eval
# LANG: _00T6 --> rel_obs_dist
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01525_rel_obs_dist = (v01523__00T6**0.5)
v01525_rel_obs_dist = (v01525_rel_obs_dist*_00T7_coeff).reshape((1, 1, 2))

# op _00To expand_array_eval
# LANG: normal_proj --> _00Tp
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01532__00Tp = np.einsum('ac,b->abc', v01526_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00Uk_decompose_eval
# LANG: aaa --> _00Ul
# SHAPES: (1, 40, 100) --> (1, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01554__00Ul = ((v01544_aaa.flatten())[src_indices__00Ul__00Uk]).reshape((1, 40, 1))

# op _00Vl_indexed_passthrough_eval
# LANG: _00Vk, _00Zp --> dDdR_real_exp
# SHAPES: (1, 2, 3, 40, 1), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01649_dDdR_real_exp__temp[i_v01648__00Vk__00Vl_indexed_passthrough_eval] = v01648__00Vk.flatten()
v01649_dDdR_real_exp = v01649_dDdR_real_exp__temp.copy()
v01649_dDdR_real_exp__temp[i_v01650__00Zp__00Vl_indexed_passthrough_eval] = v01650__00Zp.flatten()
v01649_dDdR_real_exp = v01649_dDdR_real_exp__temp.copy()

# op _00Zz_indexed_passthrough_eval
# LANG: _00Zy --> dDdR_imag_exp
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01710_dDdR_imag_exp__temp[i_v01708__00Zy__00Zz_indexed_passthrough_eval] = v01708__00Zy.flatten()
v01710_dDdR_imag_exp = v01710_dDdR_imag_exp__temp.copy()

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
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0681__00oK = np.sum(v0658_aircraft_vel * v0595_rel_obs_position, axis=1)

# op _00op reshape_eval
# LANG: rel_obs_dist --> _00oq
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0679__00oq = v0601_rel_obs_dist.reshape((1, 2))

# op _00Tq_power_combination_eval
# LANG: rel_obs_dist, _00Tp --> _00Tr
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01533__00Tr = (v01532__00Tp**1)*(v01525_rel_obs_dist**-1)
v01533__00Tr = (v01533__00Tr*_00Tq_coeff).reshape((1, 1, 2))

# op _00Um reshape_eval
# LANG: _00Ul --> _00Un
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01555__00Un = v01554__00Ul.reshape((1, 40))

# op _00ZG_power_combination_eval
# LANG: dDdR_real_exp, real_weighting --> _00ZH
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01722__00ZH = (v01713_real_weighting**1)*(v01649_dDdR_real_exp**1)
v01722__00ZH = (v01722__00ZH*_00ZG_coeff).reshape((1, 2, 3, 40, 11))

# op _00ZI_power_combination_eval
# LANG: dDdR_imag_exp, imag_weighting --> _00ZJ
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01724__00ZJ = (v01716_imag_weighting**1)*(v01710_dDdR_imag_exp**1)
v01724__00ZJ = (v01724__00ZJ*_00ZI_coeff).reshape((1, 2, 3, 40, 11))

# op _00ZS_power_combination_eval
# LANG: dDdR_imag_exp, real_weighting --> _00ZT
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01754__00ZT = (v01713_real_weighting**1)*(v01710_dDdR_imag_exp**1)
v01754__00ZT = (v01754__00ZT*_00ZS_coeff).reshape((1, 2, 3, 40, 11))

# op _00ZU_power_combination_eval
# LANG: dDdR_real_exp, imag_weighting --> _00ZV
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01756__00ZV = (v01716_imag_weighting**1)*(v01649_dDdR_real_exp**1)
v01756__00ZV = (v01756__00ZV*_00ZU_coeff).reshape((1, 2, 3, 40, 11))

# op _00Zi_cos_eval
# LANG: _00V3 --> _00Zj
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01645__00Zj = np.cos(v01644__00V3)

# op _00Zq_cos_eval
# LANG: _00V3 --> _00Zr
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01706__00Zr = np.cos(v01644__00V3)

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
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0682__00oM = (v0681__00oK**1)*(v0679__00oq**-1)
v0682__00oM = (v0682__00oM*_00oL_coeff).reshape((1, 2))

# op _00oN expand_scalar_eval
# LANG: speed_of_sound --> _00oO
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0684__00oO = np.empty((1, 2))
v0684__00oO.fill(v0554_speed_of_sound.item())

# op _00ob_power_combination_eval
# LANG: _00oa --> _00oc
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0669__00oc = (v0668__00oa**1)
v0669__00oc = (v0669__00oc*_00ob_coeff).reshape((1,))

# op _00RK_power_combination_eval
# LANG: temperature --> _00RL
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01477__00RL = (v01465_temperature**1)
v01477__00RL = (v01477__00RL*_00RK_coeff).reshape((1,))

# op _00Ts arccos_eval
# LANG: _00Tr --> _00Tt
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01534__00Tt = np.arccos(v01533__00Tr)

# op _00Vg expand_array_eval
# LANG: _00Un --> _00Vh
# SHAPES: (1, 40) --> (1, 2, 3, 40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01556__00Vh = np.einsum('ad,bce->abcde', v01555__00Un.reshape((1, 40)) ,np.ones((2, 3, 1))).reshape((1, 2, 3, 40, 1))

# op _00ZK_linear_combination_eval
# LANG: _00ZH, _00ZJ --> _00ZL
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01723__00ZL = _00ZK_constant+1*v01722__00ZH+1*v01724__00ZJ

# op _00ZW_linear_combination_eval
# LANG: _00ZT, _00ZV --> _00ZX
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01755__00ZX = _00ZW_constant+1*v01754__00ZT+1*v01756__00ZV

# op _00ZY_power_combination_eval
# LANG: n_var --> _00ZZ
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01737__00ZZ = (v01726_n_var**1)
v01737__00ZZ = (v01737__00ZZ*_00ZY_coeff).reshape((1, 2, 3, 40, 11))

# op _00Zk_power_combination_eval
# LANG: _00Zf, _00Zj --> _00Zl
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01643__00Zl = (v01627__00Zf**1)*(v01645__00Zj**1)
v01643__00Zl = (v01643__00Zl*_00Zk_coeff).reshape((1, 2, 3, 40, 10))

# op _00Zs_power_combination_eval
# LANG: _00Zh, _00Zr --> _00Zt
# SHAPES: (1, 2, 3, 40, 10), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 10)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01705__00Zt = (v01704__00Zh**1)*(v01706__00Zr**1)
v01705__00Zt = (v01705__00Zt*_00Zs_coeff).reshape((1, 2, 3, 40, 10))

# op _00_J_linear_combination_eval
# LANG: lam_var, n_var --> _00_K
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01758__00_K = _00_J_constant+1*v01726_n_var+-1*v01558_lam_var

# op _00_R_power_combination_eval
# LANG: n_var --> _00_S
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01762__00_S = (v01726_n_var**1)
v01762__00_S = (v01762__00_S*_00_R_coeff).reshape((1, 2, 3, 40, 11))

# op _00_f_linear_combination_eval
# LANG: lam_var, n_var --> _00_g
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01727__00_g = _00_f_constant+1*v01726_n_var+-1*v01558_lam_var

# op _00_n_power_combination_eval
# LANG: n_var --> _00_o
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01732__00_o = (v01726_n_var**1)
v01732__00_o = (v01732__00_o*_00_n_coeff).reshape((1, 2, 3, 40, 11))

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
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0683__00oQ = (v0682__00oM**1)*(v0684__00oO**-1)
v0683__00oQ = (v0683__00oQ*_00oP_coeff).reshape((1, 2))

# op _00od_power_combination_eval
# LANG: _00oc --> _00oe
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0670__00oe = (v0669__00oc**1)
v0670__00oe = (v0670__00oe*_00od_coeff).reshape((1,))

# op _00RM_power_combination_eval
# LANG: _00RL --> speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01478_speed_of_sound = (v01477__00RL**0.5)
v01478_speed_of_sound = (v01478_speed_of_sound*_00RM_coeff).reshape((1,))

# op _00Tw reshape_eval
# LANG: _00Tt --> rel_angle_normal
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01535_rel_angle_normal = v01534__00Tt.reshape((1, 2))

# op _00Vi_indexed_passthrough_eval
# LANG: _00Vh, _00Zl --> dTdR_real_exp
# SHAPES: (1, 2, 3, 40, 1), (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01557_dTdR_real_exp__temp[i_v01556__00Vh__00Vi_indexed_passthrough_eval] = v01556__00Vh.flatten()
v01557_dTdR_real_exp = v01557_dTdR_real_exp__temp.copy()
v01557_dTdR_real_exp__temp[i_v01643__00Zl__00Vi_indexed_passthrough_eval] = v01643__00Zl.flatten()
v01557_dTdR_real_exp = v01557_dTdR_real_exp__temp.copy()

# op _00Z__power_combination_eval
# LANG: _00Ux, _00ZZ --> _00_0
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01738__00_0 = (v01737__00ZZ**1)*(v01564__00Ux**1)
v01738__00_0 = (v01738__00_0*_00Z__coeff).reshape((1, 2, 3, 40, 11))

# op _00Zu_indexed_passthrough_eval
# LANG: _00Zt --> dTdR_imag_exp
# SHAPES: (1, 2, 3, 40, 10) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01707_dTdR_imag_exp__temp[i_v01705__00Zt__00Zu_indexed_passthrough_eval] = v01705__00Zt.flatten()
v01707_dTdR_imag_exp = v01707_dTdR_imag_exp__temp.copy()

# op _00_L_power_combination_eval
# LANG: _00ZX, _00_K --> _00_M
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01757__00_M = (v01755__00ZX**1)*(v01758__00_K**1)
v01757__00_M = (v01757__00_M*_00_L_coeff).reshape((1, 2, 3, 40, 11))

# op _00_T_power_combination_eval
# LANG: _00Ux, _00_S --> _00_U
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01763__00_U = (v01762__00_S**1)*(v01564__00Ux**1)
v01763__00_U = (v01763__00_U*_00_T_coeff).reshape((1, 2, 3, 40, 11))

# op _00_h_power_combination_eval
# LANG: _00ZL, _00_g --> _00_i
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01725__00_i = (v01723__00ZL**1)*(v01727__00_g**1)
v01725__00_i = (v01725__00_i*_00_h_coeff).reshape((1, 2, 3, 40, 11))

# op _00_p_power_combination_eval
# LANG: _00Ux, _00_o --> _00_q
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01733__00_q = (v01732__00_o**1)*(v01564__00Ux**1)
v01733__00_q = (v01733__00_q*_00_p_coeff).reshape((1, 2, 3, 40, 11))

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
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0685__00oS = _00oR_constant+-1*v0683__00oQ

# op _00o_ expand_array_eval
# LANG: in_plane_ex --> _00p0
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0702__00p0 = np.einsum('ab,c->abc', v0181_in_plane_ex.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _00p9 expand_scalar_eval
# LANG: _00oe --> _00pa
# SHAPES: (1,) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0671__00pa = np.empty((1, 2, 3, 2, 11))
v0671__00pa.fill(v0670__00oe.item())

# op _013C expand_scalar_eval
# LANG: Vy --> _013D
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01866__013D = np.empty((1, 1))
v01866__013D.fill(v0962_v.item())

# op _013E expand_scalar_eval
# LANG: Vz --> _013F
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01867__013F = np.empty((1, 1))
v01867__013F.fill(v0963_w.item())

# op _013z expand_scalar_eval
# LANG: Vx --> _013A
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01864__013A = np.empty((1, 1))
v01864__013A.fill(v0961_u.item())

# op _00UA expand_scalar_eval
# LANG: speed_of_sound --> _00UB
# SHAPES: (1,) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01730__00UB = np.empty((1, 2, 3, 40, 11))
v01730__00UB.fill(v01478_speed_of_sound.item())

# op _00Us expand_array_eval
# LANG: rel_angle_normal --> _00Ut
# SHAPES: (1, 2) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01719__00Ut = np.einsum('ab,cde->abcde', v01535_rel_angle_normal.reshape((1, 2)) ,np.ones((3, 40, 11))).reshape((1, 2, 3, 40, 11))

# op _00ZA_power_combination_eval
# LANG: dTdR_real_exp, real_weighting --> _00ZB
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01714__00ZB = (v01713_real_weighting**1)*(v01557_dTdR_real_exp**1)
v01714__00ZB = (v01714__00ZB*_00ZA_coeff).reshape((1, 2, 3, 40, 11))

# op _00ZC_power_combination_eval
# LANG: dTdR_imag_exp, imag_weighting --> _00ZD
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01717__00ZD = (v01716_imag_weighting**1)*(v01707_dTdR_imag_exp**1)
v01717__00ZD = (v01717__00ZD*_00ZC_coeff).reshape((1, 2, 3, 40, 11))

# op _00ZM_power_combination_eval
# LANG: dTdR_imag_exp, real_weighting --> _00ZN
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01748__00ZN = (v01713_real_weighting**1)*(v01707_dTdR_imag_exp**1)
v01748__00ZN = (v01748__00ZN*_00ZM_coeff).reshape((1, 2, 3, 40, 11))

# op _00ZO_power_combination_eval
# LANG: dTdR_real_exp, imag_weighting --> _00ZP
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01750__00ZP = (v01716_imag_weighting**1)*(v01557_dTdR_real_exp**1)
v01750__00ZP = (v01750__00ZP*_00ZO_coeff).reshape((1, 2, 3, 40, 11))

# op _00_1_power_combination_eval
# LANG: _00Uv, _00_0 --> _00_2
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01739__00_2 = (v01738__00_0**1)*(v01553__00Uv**1)
v01739__00_2 = (v01739__00_2*_00_1_coeff).reshape((1, 2, 3, 40, 11))

# op _00_N_power_combination_eval
# LANG: _00_M --> _00_O
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01759__00_O = (v01757__00_M**1)
v01759__00_O = (v01759__00_O*_00_N_coeff).reshape((1, 2, 3, 40, 11))

# op _00_V_power_combination_eval
# LANG: _00Uv, _00_U --> _00_W
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01764__00_W = (v01763__00_U**1)*(v01553__00Uv**1)
v01764__00_W = (v01764__00_W*_00_V_coeff).reshape((1, 2, 3, 40, 11))

# op _00_j_power_combination_eval
# LANG: _00_i --> _00_k
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01728__00_k = (v01725__00_i**1)
v01728__00_k = (v01728__00_k*_00_j_coeff).reshape((1, 2, 3, 40, 11))

# op _00_r_power_combination_eval
# LANG: _00Uv, _00_q --> _00_s
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01734__00_s = (v01733__00_q**1)*(v01553__00Uv**1)
v01734__00_s = (v01734__00_s*_00_r_coeff).reshape((1, 2, 3, 40, 11))

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
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0680__00oU = (v0679__00oq**1)*(v0685__00oS**1)
v0680__00oU = (v0680__00oU*_00oT_coeff).reshape((1, 2))

# op _00p1_tensor_dot_product_eval
# LANG: _00p0, rel_obs_position --> _00p2
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0701__00p2 = np.sum(v0595_rel_obs_position * v0702__00p0, axis=1)

# op _00pR_power_combination_eval
# LANG: n_var, _00pa --> _00pS
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0697__00pS = (v0665_n_var**1)*(v0671__00pa**1)
v0697__00pS = (v0697__00pS*_00pR_coeff).reshape((1, 2, 3, 2, 11))

# op _00pj expand_scalar_eval
# LANG: propeller_radius --> _00pk
# SHAPES: (1,) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0699__00pk = np.empty((1, 2, 3, 2, 11))
v0699__00pk.fill(v0482_propeller_radius.item())

# op _013B_indexed_passthrough_eval
# LANG: _013A, _013D, _013F --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01865_V_aircraft__temp[i_v01864__013A__013B_indexed_passthrough_eval] = v01864__013A.flatten()
v01865_V_aircraft = v01865_V_aircraft__temp.copy()
v01865_V_aircraft__temp[i_v01866__013D__013B_indexed_passthrough_eval] = v01866__013D.flatten()
v01865_V_aircraft = v01865_V_aircraft__temp.copy()
v01865_V_aircraft__temp[i_v01867__013F__013B_indexed_passthrough_eval] = v01867__013F.flatten()
v01865_V_aircraft = v01865_V_aircraft__temp.copy()

# op _00ZE_linear_combination_eval
# LANG: _00ZB, _00ZD --> _00ZF
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01715__00ZF = _00ZE_constant+1*v01714__00ZB+1*v01717__00ZD

# op _00ZQ_linear_combination_eval
# LANG: _00ZN, _00ZP --> _00ZR
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01749__00ZR = _00ZQ_constant+1*v01748__00ZN+1*v01750__00ZP

# op _00_3_power_combination_eval
# LANG: _00Uz, _00_2 --> _00_4
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01740__00_4 = (v01739__00_2**1)*(v01573__00Uz**1)
v01740__00_4 = (v01740__00_4*_00_3_coeff).reshape((1, 2, 3, 40, 11))

# op _00_F_cos_eval
# LANG: _00Ut --> _00_G
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01752__00_G = np.cos(v01719__00Ut)

# op _00_P_power_combination_eval
# LANG: _00UB, _00_O --> _00_Q
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01760__00_Q = (v01759__00_O**1)*(v01730__00UB**1)
v01760__00_Q = (v01760__00_Q*_00_P_coeff).reshape((1, 2, 3, 40, 11))

# op _00_X_power_combination_eval
# LANG: _00Uz, _00_W --> _00_Y
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01765__00_Y = (v01764__00_W**1)*(v01573__00Uz**1)
v01765__00_Y = (v01765__00_Y*_00_X_coeff).reshape((1, 2, 3, 40, 11))

# op _00_b_cos_eval
# LANG: _00Ut --> _00_c
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01720__00_c = np.cos(v01719__00Ut)

# op _00_l_power_combination_eval
# LANG: _00_k, _00UB --> _00_m
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01729__00_m = (v01728__00_k**1)*(v01730__00UB**1)
v01729__00_m = (v01729__00_m*_00_l_coeff).reshape((1, 2, 3, 40, 11))

# op _00_t_power_combination_eval
# LANG: _00Uz, _00_s --> _00_u
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01735__00_u = (v01734__00_s**1)*(v01573__00Uz**1)
v01735__00_u = (v01735__00_u*_00_t_coeff).reshape((1, 2, 3, 40, 11))

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
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0674__00oY = np.einsum('b,ac->abc', v0494_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00pT_power_combination_eval
# LANG: _00pS, _00pk --> _00pU
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0698__00pU = (v0697__00pS**1)*(v0699__00pk**1)
v0698__00pU = (v0698__00pU*_00pT_coeff).reshape((1, 2, 3, 2, 11))

# op _00pd expand_array_eval
# LANG: _00p2 --> _00pe
# SHAPES: (1, 2) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0703__00pe = np.einsum('ab,cde->abcde', v0701__00p2.reshape((1, 2)) ,np.ones((3, 2, 11))).reshape((1, 2, 3, 2, 11))

# op _00pf expand_scalar_eval
# LANG: speed_of_sound --> _00pg
# SHAPES: (1,) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0677__00pg = np.empty((1, 2, 3, 2, 11))
v0677__00pg.fill(v0554_speed_of_sound.item())

# op _00ph expand_array_eval
# LANG: _00oU --> _00pi
# SHAPES: (1, 2) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0686__00pi = np.einsum('ab,cde->abcde', v0680__00oU.reshape((1, 2)) ,np.ones((3, 2, 11))).reshape((1, 2, 3, 2, 11))

# op _013G expand_array_eval
# LANG: V_aircraft --> _013H
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01874__013H = np.einsum('ab,c->abc', v01865_V_aircraft.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _013M expand_array_eval
# LANG: time_vectors --> _013N
# SHAPES: (2,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01880__013N = np.einsum('c,ab->abc', v01879_time_vectors.reshape((2,)) ,np.ones((1, 3))).reshape((1, 3, 2))

# op _00_5_power_combination_eval
# LANG: _00UB, _00_4 --> _00_6
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01741__00_6 = (v01740__00_4**1)*(v01730__00UB**-1)
v01741__00_6 = (v01741__00_6*_00_5_coeff).reshape((1, 2, 3, 40, 11))

# op _00_7_sin_eval
# LANG: _00Ut --> _00_8
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01743__00_8 = np.sin(v01719__00Ut)

# op _00_H_power_combination_eval
# LANG: _00ZR, _00_G --> _00_I
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01751__00_I = (v01749__00ZR**1)*(v01752__00_G**1)
v01751__00_I = (v01751__00_I*_00_H_coeff).reshape((1, 2, 3, 40, 11))

# op _00_Z_power_combination_eval
# LANG: _00_Q, _00_Y --> _00__
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01761__00__ = (v01760__00_Q**1)*(v01765__00_Y**-1)
v01761__00__ = (v01761__00__*_00_Z_coeff).reshape((1, 2, 3, 40, 11))

# op _00_d_power_combination_eval
# LANG: _00ZF, _00_c --> _00_e
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01718__00_e = (v01715__00ZF**1)*(v01720__00_c**1)
v01718__00_e = (v01718__00_e*_00_d_coeff).reshape((1, 2, 3, 40, 11))

# op _00_v_power_combination_eval
# LANG: _00_m, _00_u --> _00_w
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01731__00_w = (v01729__00_m**1)*(v01735__00_u**-1)
v01731__00_w = (v01731__00_w*_00_v_coeff).reshape((1, 2, 3, 40, 11))

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
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0673__00p4 = np.sum(v0595_rel_obs_position * v0674__00oY, axis=1)

# op _00pV_power_combination_eval
# LANG: _00pU, _00pe --> _00pW
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0700__00pW = (v0698__00pU**1)*(v0703__00pe**1)
v0700__00pW = (v0700__00pW*_00pV_coeff).reshape((1, 2, 3, 2, 11))

# op _00pX_power_combination_eval
# LANG: _00pg, _00pi --> _00pY
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0705__00pY = (v0677__00pg**1)*(v0686__00pi**1)
v0705__00pY = (v0705__00pY*_00pX_coeff).reshape((1, 2, 3, 2, 11))

# op _00qA_exp_a_eval
# LANG: lam_var --> _00qB
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0731__00qB = _00qA_exp_a_eval_a**v0710_lam_var

# op _00rx_exp_a_eval
# LANG: lam_var --> _00ry
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0764__00ry = _00rx_exp_a_eval_a**v0710_lam_var

# op _011A_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _011B
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v01808__011B = (v08_rotor_disk_in_plane_1**1)
v01808__011B = (v01808__011B*_011A_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _011D_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _011E
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v01826__011E = (v010_rotor_disk_in_plane_2**1)
v01826__011E = (v01826__011E*_011D_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _011x_power_combination_eval
# LANG: rotor_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v01807_origin = (v012_rotor_disk_origin**1)
v01807_origin = (v01807_origin*_011x_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _013J expand_array_eval
# LANG: aircraft_location --> _013K
# SHAPES: (3, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01869__013K = np.einsum('bc,a->abc', v01868_aircraft_location.reshape((3, 2)) ,np.ones((1,))).reshape((1, 3, 2))

# op _013Q_decompose_eval
# LANG: _013H --> _013R, _013Z, _0145
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01875__013R = ((v01874__013H.flatten())[src_indices__013R__013Q]).reshape((1, 1, 2))
v01876__013Z = ((v01874__013H.flatten())[src_indices__013Z__013Q]).reshape((1, 1, 2))
v01877__0145 = ((v01874__013H.flatten())[src_indices__0145__013Q]).reshape((1, 1, 2))

# op _013S_decompose_eval
# LANG: _013N --> _013T, _013_, _0146
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01881__013T = ((v01880__013N.flatten())[src_indices__013T__013S]).reshape((1, 1, 2))
v01882__013_ = ((v01880__013N.flatten())[src_indices__013___013S]).reshape((1, 1, 2))
v01883__0146 = ((v01880__013N.flatten())[src_indices__0146__013S]).reshape((1, 1, 2))

# op _00IC_power_combination_eval
# LANG: _angular_speed --> _00ID
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01368__00ID = (v01142__angular_speed**1)
v01368__00ID = (v01368__00ID*_00IC_coeff).reshape((1, 40, 100))

# op _00_9_power_combination_eval
# LANG: _00_6, _00_8 --> _00_a
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01742__00_a = (v01741__00_6**1)*(v01743__00_8**1)
v01742__00_a = (v01742__00_a*_00_9_coeff).reshape((1, 2, 3, 40, 11))

# op _00_x_linear_combination_eval
# LANG: _00_e, _00_w --> _00_y
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01721__00_y = _00_x_constant+1*v01718__00_e+-1*v01731__00_w

# op _00pD_power_combination_eval
# LANG: n_var, _00pa --> _00pE
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0666__00pE = (v0665_n_var**1)*(v0671__00pa**1)
v0666__00pE = (v0666__00pE*_00pD_coeff).reshape((1, 2, 3, 2, 11))

# op _00pH_power_combination_eval
# LANG: _00pi --> _00pI
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0687__00pI = (v0686__00pi**2)
v0687__00pI = (v0687__00pI*_00pH_coeff).reshape((1, 2, 3, 2, 11))

# op _00pZ_power_combination_eval
# LANG: _00pW, _00pY --> _00p_
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0704__00p_ = (v0700__00pW**1)*(v0705__00pY**-1)
v0704__00p_ = (v0704__00p_*_00pZ_coeff).reshape((1, 2, 3, 2, 11))

# op _00pb expand_array_eval
# LANG: _00p4 --> _00pc
# SHAPES: (1, 2) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0675__00pc = np.einsum('ab,cde->abcde', v0673__00p4.reshape((1, 2)) ,np.ones((3, 2, 11))).reshape((1, 2, 3, 2, 11))

# op _00pl expand_array_eval
# LANG: aT --> _00pm
# SHAPES: (1, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0695__00pm = np.einsum('ade,bc->abcde', v0641_aT.reshape((1, 2, 11)) ,np.ones((2, 3))).reshape((1, 2, 3, 2, 11))

# op _00pn expand_array_eval
# LANG: bT --> _00po
# SHAPES: (1, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0691__00po = np.einsum('ade,bc->abcde', v0650_bT.reshape((1, 2, 11)) ,np.ones((2, 3))).reshape((1, 2, 3, 2, 11))

# op _00pp expand_array_eval
# LANG: aD --> _00pq
# SHAPES: (1, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0724__00pq = np.einsum('ade,bc->abcde', v0646_aD.reshape((1, 2, 11)) ,np.ones((2, 3))).reshape((1, 2, 3, 2, 11))

# op _00pr expand_array_eval
# LANG: bD --> _00ps
# SHAPES: (1, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0721__00ps = np.einsum('ade,bc->abcde', v0654_bD.reshape((1, 2, 11)) ,np.ones((2, 3))).reshape((1, 2, 3, 2, 11))

# op _00qC_power_combination_eval
# LANG: A_lin_comb_sign_matrix, _00qB --> _00qD
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0730__00qD = (v0708_A_lin_comb_sign_matrix**1)*(v0731__00qB**1)
v0730__00qD = (v0730__00qD*_00qC_coeff).reshape((1, 2, 3, 2, 11))

# op _00qE_linear_combination_eval
# LANG: n_var, lam_var --> _00qF
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0733__00qF = _00qE_constant+1*v0665_n_var+1*v0710_lam_var

# op _00qg_exp_a_eval
# LANG: lam_var --> _00qh
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0711__00qh = _00qg_exp_a_eval_a**v0710_lam_var

# op _00rB_linear_combination_eval
# LANG: n_var, lam_var --> _00rC
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0766__00rC = _00rB_constant+1*v0665_n_var+1*v0710_lam_var

# op _00rd_exp_a_eval
# LANG: lam_var --> _00re
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0748__00re = _00rd_exp_a_eval_a**v0710_lam_var

# op _00rz_power_combination_eval
# LANG: B_lin_comb_sign_matrix, _00ry --> _00rA
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0763__00rA = (v0746_B_lin_comb_sign_matrix**1)*(v0764__00ry**1)
v0763__00rA = (v0763__00rA*_00rz_coeff).reshape((1, 2, 3, 2, 11))

# op _0100_linear_combination_eval
# LANG: _00_I, _00__ --> _0101
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01753__0101 = _0100_constant+1*v01751__00_I+-1*v01761__00__

# op _012c cross_product_eval
# LANG: _011B, _011E --> _012d
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01827__012d = np.cross(v01826__011E, v01808__011B, axisa = 0, axisb = 0, axisc = 0)

# op _013O_decompose_eval
# LANG: _013K --> _013P, _013Y, _0144
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01870__013P = ((v01869__013K.flatten())[src_indices__013P__013O]).reshape((1, 1, 2))
v01871__013Y = ((v01869__013K.flatten())[src_indices__013Y__013O]).reshape((1, 1, 2))
v01872__0144 = ((v01869__013K.flatten())[src_indices__0144__013O]).reshape((1, 1, 2))

# op _013U_power_combination_eval
# LANG: _013R, _013T --> _013V
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01878__013V = (v01875__013R**1)*(v01881__013T**1)
v01878__013V = (v01878__013V*_013U_coeff).reshape((1, 1, 2))

# op _0140_power_combination_eval
# LANG: _013Z, _013_ --> _0141
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01885__0141 = (v01876__013Z**1)*(v01882__013_**1)
v01885__0141 = (v01885__0141*_0140_coeff).reshape((1, 1, 2))

# op _014i expand_array_eval
# LANG: origin --> _014j
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01892__014j = np.einsum('b,ac->abc', v01807_origin.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00IE_power_combination_eval
# LANG: _00ID --> _00IF
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01369__00IF = (v01368__00ID**1)
v01369__00IF = (v01369__00IF*_00IE_coeff).reshape((1, 40, 100))

# op _00_B_bessel_eval
# LANG: _00_a --> _00_C
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01744__00_C=_00_B_bessel_eval(_00_B_bessel_eval_order,v01742__00_a)

# op _00_z_power_combination_eval
# LANG: coeff_matrix_A, _00_y --> _00_A
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01712__00_A = (v01711_coeff_matrix_A**1)*(v01721__00_y**1)
v01712__00_A = (v01712__00_A*_00_z_coeff).reshape((1, 2, 3, 40, 11))

# op _00pF_power_combination_eval
# LANG: _00pE, _00pc --> _00pG
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0672__00pG = (v0666__00pE**1)*(v0675__00pc**1)
v0672__00pG = (v0672__00pG*_00pF_coeff).reshape((1, 2, 3, 2, 11))

# op _00pJ_power_combination_eval
# LANG: _00pg, _00pI --> _00pK
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0678__00pK = (v0677__00pg**1)*(v0687__00pI**1)
v0678__00pK = (v0678__00pK*_00pJ_coeff).reshape((1, 2, 3, 2, 11))

# op _00pN_power_combination_eval
# LANG: _00pi, _00pk --> _00pO
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0717__00pO = (v0699__00pk**1)*(v0686__00pi**1)
v0717__00pO = (v0717__00pO*_00pN_coeff).reshape((1, 2, 3, 2, 11))

# op _00q0_power_combination_eval
# LANG: coeff_sign_matrix_even, _00po --> _00q1
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0690__00q1 = (v0689_coeff_sign_matrix_even**1)*(v0691__00po**1)
v0690__00q1 = (v0690__00q1*_00q0_coeff).reshape((1, 2, 3, 2, 11))

# op _00q2_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00pm --> _00q3
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0694__00q3 = (v0693_coeff_sign_matrix_odd**1)*(v0695__00pm**1)
v0694__00q3 = (v0694__00q3*_00q2_coeff).reshape((1, 2, 3, 2, 11))

# op _00q6_power_combination_eval
# LANG: coeff_sign_matrix_even, _00ps --> _00q7
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0720__00q7 = (v0689_coeff_sign_matrix_even**1)*(v0721__00ps**1)
v0720__00q7 = (v0720__00q7*_00q6_coeff).reshape((1, 2, 3, 2, 11))

# op _00q8_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00pq --> _00q9
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0723__00q9 = (v0693_coeff_sign_matrix_odd**1)*(v0724__00pq**1)
v0723__00q9 = (v0723__00q9*_00q8_coeff).reshape((1, 2, 3, 2, 11))

# op _00qG_power_combination_eval
# LANG: _00qD, _00qF --> _00qH
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0732__00qH = (v0730__00qD**1)*(v0733__00qF**1)
v0732__00qH = (v0732__00qH*_00qG_coeff).reshape((1, 2, 3, 2, 11))

# op _00qI_bessel_eval
# LANG: _00p_ --> _00qJ
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0735__00qJ=_00qI_bessel_eval(_00qI_bessel_eval_order,v0704__00p_)

# op _00qY_power_combination_eval
# LANG: coeff_sign_matrix_even, _00pm --> _00qZ
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0740__00qZ = (v0689_coeff_sign_matrix_even**1)*(v0695__00pm**1)
v0740__00qZ = (v0740__00qZ*_00qY_coeff).reshape((1, 2, 3, 2, 11))

# op _00q__power_combination_eval
# LANG: _00po, coeff_sign_matrix_odd --> _00r0
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0742__00r0 = (v0693_coeff_sign_matrix_odd**1)*(v0691__00po**1)
v0742__00r0 = (v0742__00r0*_00q__coeff).reshape((1, 2, 3, 2, 11))

# op _00qi_power_combination_eval
# LANG: A_lin_comb_sign_matrix, _00qh --> _00qj
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0709__00qj = (v0708_A_lin_comb_sign_matrix**1)*(v0711__00qh**1)
v0709__00qj = (v0709__00qj*_00qi_coeff).reshape((1, 2, 3, 2, 11))

# op _00qk_bessel_eval
# LANG: _00p_ --> _00ql
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0713__00ql=_00qk_bessel_eval(_00qk_bessel_eval_order,v0704__00p_)

# op _00qu_linear_combination_eval
# LANG: n_var, lam_var --> _00qv
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0726__00qv = _00qu_constant+1*v0665_n_var+-1*v0710_lam_var

# op _00qw_bessel_eval
# LANG: _00p_ --> _00qx
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0728__00qx=_00qw_bessel_eval(_00qw_bessel_eval_order,v0704__00p_)

# op _00r3_power_combination_eval
# LANG: coeff_sign_matrix_even, _00pq --> _00r4
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0755__00r4 = (v0689_coeff_sign_matrix_even**1)*(v0724__00pq**1)
v0755__00r4 = (v0755__00r4*_00r3_coeff).reshape((1, 2, 3, 2, 11))

# op _00r5_power_combination_eval
# LANG: coeff_sign_matrix_odd, _00ps --> _00r6
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0757__00r6 = (v0693_coeff_sign_matrix_odd**1)*(v0721__00ps**1)
v0757__00r6 = (v0757__00r6*_00r5_coeff).reshape((1, 2, 3, 2, 11))

# op _00rD_power_combination_eval
# LANG: _00rA, _00rC --> _00rE
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0765__00rE = (v0763__00rA**1)*(v0766__00rC**1)
v0765__00rE = (v0765__00rE*_00rD_coeff).reshape((1, 2, 3, 2, 11))

# op _00rF_bessel_eval
# LANG: _00p_ --> _00rG
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0768__00rG=_00rF_bessel_eval(_00rF_bessel_eval_order,v0704__00p_)

# op _00rf_power_combination_eval
# LANG: B_lin_comb_sign_matrix, _00re --> _00rg
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0747__00rg = (v0746_B_lin_comb_sign_matrix**1)*(v0748__00re**1)
v0747__00rg = (v0747__00rg*_00rf_coeff).reshape((1, 2, 3, 2, 11))

# op _00rh_bessel_eval
# LANG: _00p_ --> _00ri
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0750__00ri=_00rh_bessel_eval(_00rh_bessel_eval_order,v0704__00p_)

# op _00rr_linear_combination_eval
# LANG: n_var, lam_var --> _00rs
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0759__00rs = _00rr_constant+1*v0665_n_var+-1*v0710_lam_var

# op _00rt_bessel_eval
# LANG: _00p_ --> _00ru
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0761__00ru=_00rt_bessel_eval(_00rt_bessel_eval_order,v0704__00p_)

# op _00uC expand_scalar_eval
# LANG: Vx --> _00uD
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0845__00uD = np.empty((1, 1))
v0845__00uD.fill(v030_u.item())

# op _00uF expand_scalar_eval
# LANG: Vy --> _00uG
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0847__00uG = np.empty((1, 1))
v0847__00uG.fill(v035_v.item())

# op _00uH expand_scalar_eval
# LANG: Vz --> _00uI
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0848__00uI = np.empty((1, 1))
v0848__00uI.fill(v039_w.item())

# op _0102_power_combination_eval
# LANG: coeff_matrix_B, _0101 --> _0103
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01747__0103 = (v01746_coeff_matrix_B**1)*(v01753__0101**1)
v01747__0103 = (v01747__0103*_0102_coeff).reshape((1, 2, 3, 40, 11))

# op _0104_bessel_eval
# LANG: _00_a --> _0105
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01767__0105=_0104_bessel_eval(_0104_bessel_eval_order,v01742__00_a)

# op _011F pnorm_eval
# LANG: _011B --> _011G
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01809__011G = np.linalg.norm(v01808__011B.flatten(), ord=2)

# op _011K pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _011L
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01811__011L = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _011S_linear_combination_eval
# LANG: theta --> _011T
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0970_theta = v0970_theta.reshape((1, 1))
v01814__011T = _011S_constant+1*v0970_theta
v0970_theta = v0970_theta.reshape((1,))

# op _011U_linear_combination_eval
# LANG: theta --> _011V
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0970_theta = v0970_theta.reshape((1, 1))
v01816__011V = _011U_constant+1*v0970_theta
v0970_theta = v0970_theta.reshape((1,))

# op _0120_sin_eval
# LANG: theta --> _0121
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0970_theta = v0970_theta.reshape((1, 1))
v01819__0121 = np.sin(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _0124_sin_eval
# LANG: theta --> _0125
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0970_theta = v0970_theta.reshape((1, 1))
v01821__0125 = np.sin(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _0128_cos_eval
# LANG: theta --> _0129
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0970_theta = v0970_theta.reshape((1, 1))
v01823__0129 = np.cos(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _012e pnorm_eval
# LANG: _012d --> _012f
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01829__012f = np.linalg.norm(v01827__012d.flatten(), ord=2)

# op _013W_linear_combination_eval
# LANG: _013P, _013V --> aircraft_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01873_aircraft_x_pos = _013W_constant+1*v01870__013P+1*v01878__013V

# op _0142_linear_combination_eval
# LANG: _013Y, _0141 --> aircraft_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01884_aircraft_y_pos = _0142_constant+1*v01871__013Y+1*v01885__0141

# op _0147_power_combination_eval
# LANG: _0145, _0146 --> _0148
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01887__0148 = (v01877__0145**1)*(v01883__0146**1)
v01887__0148 = (v01887__0148*_0147_coeff).reshape((1, 1, 2))

# op _014k_decompose_eval
# LANG: _014j --> _014l, _014q, _014v
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01893__014l = ((v01892__014j.flatten())[src_indices__014l__014k]).reshape((1, 1, 2))
v01894__014q = ((v01892__014j.flatten())[src_indices__014q__014k]).reshape((1, 1, 2))
v01895__014v = ((v01892__014j.flatten())[src_indices__014v__014k]).reshape((1, 1, 2))

# op _00NX_single_tensor_sum_with_axis_eval
# LANG: _00IF --> _00NY
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01370__00NY = np.sum(v01369__00IF, axis = (1, 2)).reshape((1,))

# op _00O6_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00O7
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01375__00O7 = np.sum(v01130__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00TW reshape_eval
# LANG: rel_obs_dist --> _00TX
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01775__00TX = v01525_rel_obs_dist.reshape((1, 2))

# op _00_D_power_combination_eval
# LANG: _00_A, _00_C --> _00_E
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01736__00_E = (v01712__00_A**1)*(v01744__00_C**1)
v01736__00_E = (v01736__00_E*_00_D_coeff).reshape((1, 2, 3, 40, 11))

# op _00pL_power_combination_eval
# LANG: _00pG, _00pK --> _00pM
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0676__00pM = (v0672__00pG**1)*(v0678__00pK**-1)
v0676__00pM = (v0676__00pM*_00pL_coeff).reshape((1, 2, 3, 2, 11))

# op _00pP_power_combination_eval
# LANG: _00pO --> _00pQ
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0718__00pQ = (v0717__00pO**-1)
v0718__00pQ = (v0718__00pQ*_00pP_coeff).reshape((1, 2, 3, 2, 11))

# op _00q4_linear_combination_eval
# LANG: _00q1, _00q3 --> _00q5
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0692__00q5 = _00q4_constant+1*v0690__00q1+1*v0694__00q3

# op _00qK_power_combination_eval
# LANG: _00qH, _00qJ --> _00qL
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0734__00qL = (v0732__00qH**1)*(v0735__00qJ**1)
v0734__00qL = (v0734__00qL*_00qK_coeff).reshape((1, 2, 3, 2, 11))

# op _00qa_linear_combination_eval
# LANG: _00q7, _00q9 --> _00qb
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0722__00qb = _00qa_constant+1*v0720__00q7+1*v0723__00q9

# op _00qe_bessel_eval
# LANG: _00p_ --> _00qf
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0706__00qf=_00qe_bessel_eval(_00qe_bessel_eval_order,v0704__00p_)

# op _00qm_power_combination_eval
# LANG: _00qj, _00ql --> _00qn
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0712__00qn = (v0709__00qj**1)*(v0713__00ql**1)
v0712__00qn = (v0712__00qn*_00qm_coeff).reshape((1, 2, 3, 2, 11))

# op _00qy_power_combination_eval
# LANG: _00qv, _00qx --> _00qz
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0727__00qz = (v0726__00qv**1)*(v0728__00qx**1)
v0727__00qz = (v0727__00qz*_00qy_coeff).reshape((1, 2, 3, 2, 11))

# op _00r1_linear_combination_eval
# LANG: _00qZ, _00r0 --> _00r2
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0741__00r2 = _00r1_constant+1*v0740__00qZ+1*v0742__00r0

# op _00r7_linear_combination_eval
# LANG: _00r4, _00r6 --> _00r8
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0756__00r8 = _00r7_constant+1*v0755__00r4+1*v0757__00r6

# op _00rH_power_combination_eval
# LANG: _00rE, _00rG --> _00rI
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0767__00rI = (v0765__00rE**1)*(v0768__00rG**1)
v0767__00rI = (v0767__00rI*_00rH_coeff).reshape((1, 2, 3, 2, 11))

# op _00rb_bessel_eval
# LANG: _00p_ --> _00rc
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0744__00rc=_00rb_bessel_eval(_00rb_bessel_eval_order,v0704__00p_)

# op _00rj_power_combination_eval
# LANG: _00rg, _00ri --> _00rk
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0749__00rk = (v0747__00rg**1)*(v0750__00ri**1)
v0749__00rk = (v0749__00rk*_00rj_coeff).reshape((1, 2, 3, 2, 11))

# op _00rv_power_combination_eval
# LANG: _00rs, _00ru --> _00rw
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0760__00rw = (v0759__00rs**1)*(v0761__00ru**1)
v0760__00rw = (v0760__00rw*_00rv_coeff).reshape((1, 2, 3, 2, 11))

# op _00uE_indexed_passthrough_eval
# LANG: _00uD, _00uG, _00uI --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0846_V_aircraft__temp[i_v0845__00uD__00uE_indexed_passthrough_eval] = v0845__00uD.flatten()
v0846_V_aircraft = v0846_V_aircraft__temp.copy()
v0846_V_aircraft__temp[i_v0847__00uG__00uE_indexed_passthrough_eval] = v0847__00uG.flatten()
v0846_V_aircraft = v0846_V_aircraft__temp.copy()
v0846_V_aircraft__temp[i_v0848__00uI__00uE_indexed_passthrough_eval] = v0848__00uI.flatten()
v0846_V_aircraft = v0846_V_aircraft__temp.copy()

# op _0106_power_combination_eval
# LANG: _0103, _0105 --> _0107
# SHAPES: (1, 2, 3, 40, 11), (1, 2, 3, 40, 11) --> (1, 2, 3, 40, 11)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01766__0107 = (v01747__0103**1)*(v01767__0105**1)
v01766__0107 = (v01766__0107*_0106_coeff).reshape((1, 2, 3, 40, 11))

# op _010g_decompose_eval
# LANG: n_var --> _010h
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01769__010h = ((v01726_n_var.flatten())[src_indices__010h__010g]).reshape((1, 2, 3, 1, 1))

# op _011H_power_combination_eval
# LANG: _011G --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01810_propeller_radius = (v01809__011G**1)
v01810_propeller_radius = (v01810_propeller_radius*_011H_coeff).reshape((1,))

# op _011M reshape_eval
# LANG: _011L --> _011N
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01812__011N = v01811__011L.reshape((40, 1))

# op _011W_power_combination_eval
# LANG: _011T, _011V --> _011X
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01815__011X = (v01814__011T**1)*(v01816__011V**-1)
v01815__011X = (v01815__011X*_011W_coeff).reshape((1, 1))

# op _011Z_cos_eval
# LANG: theta --> _011_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v0970_theta = v0970_theta.reshape((1, 1))
v01818__011_ = np.cos(v0970_theta)
v0970_theta = v0970_theta.reshape((1,))

# op _0122_power_combination_eval
# LANG: _0121 --> _0123
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01820__0123 = (v01819__0121**1)
v01820__0123 = (v01820__0123*_0122_coeff).reshape((1, 1))

# op _0126_power_combination_eval
# LANG: _0125 --> _0127
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01822__0127 = (v01821__0125**1)
v01822__0127 = (v01822__0127*_0126_coeff).reshape((1, 1))

# op _012a_power_combination_eval
# LANG: _0129 --> _012b
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01824__012b = (v01823__0129**1)
v01824__012b = (v01824__012b*_012a_coeff).reshape((1, 1))

# op _012g expand_scalar_eval
# LANG: _012f --> _012h
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01830__012h = np.empty((3,))
v01830__012h.fill(v01829__012f.item())

# op _0149_linear_combination_eval
# LANG: _0144, _0148 --> aircraft_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01886_aircraft_z_pos = _0149_constant+1*v01872__0144+1*v01887__0148

# op _014b expand_array_eval
# LANG: init_obs_x_loc --> _014c
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01889__014c = np.einsum('c,ab->abc', v01888_init_obs_x_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _014d expand_array_eval
# LANG: init_obs_y_loc --> _014e
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01897__014e = np.einsum('c,ab->abc', v01896_init_obs_y_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _014m_linear_combination_eval
# LANG: aircraft_x_pos, _014l --> _014n
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01891__014n = _014m_constant+1*v01873_aircraft_x_pos+1*v01893__014l

# op _014r_linear_combination_eval
# LANG: aircraft_y_pos, _014q --> _014s
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01899__014s = _014r_constant+1*v01884_aircraft_y_pos+1*v01894__014q

# op _00M__single_tensor_sum_with_axis_eval
# LANG: _local_thrust --> _00N0
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01269__00N0 = np.sum(v01254__local_thrust, axis = (1, 2)).reshape((1,))

# op _00NZ_power_combination_eval
# LANG: _00NY --> _00N_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01371__00N_ = (v01370__00NY**1)
v01371__00N_ = (v01371__00N_*_00NZ_coeff).reshape((1,))

# op _00O8_power_combination_eval
# LANG: _00O7 --> _00O9
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01376__00O9 = (v01375__00O7**1)
v01376__00O9 = (v01376__00O9*_00O8_coeff).reshape((1,))

# op _00qM_linear_combination_eval
# LANG: _00qz, _00qL --> _00qN
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0729__00qN = _00qM_constant+1*v0727__00qz+1*v0734__00qL

# op _00qc_power_combination_eval
# LANG: _00pM, _00q5 --> _00qd
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0688__00qd = (v0676__00pM**1)*(v0692__00q5**1)
v0688__00qd = (v0688__00qd*_00qc_coeff).reshape((1, 2, 3, 2, 11))

# op _00qo_linear_combination_eval
# LANG: _00qf, _00qn --> _00qp
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0707__00qp = _00qo_constant+1*v0706__00qf+1*v0712__00qn

# op _00qs_power_combination_eval
# LANG: _00pQ, _00qb --> _00qt
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0719__00qt = (v0718__00pQ**1)*(v0722__00qb**1)
v0719__00qt = (v0719__00qt*_00qs_coeff).reshape((1, 2, 3, 2, 11))

# op _00r9_power_combination_eval
# LANG: _00pM, _00r2 --> _00ra
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0739__00ra = (v0676__00pM**1)*(v0741__00r2**1)
v0739__00ra = (v0739__00ra*_00r9_coeff).reshape((1, 2, 3, 2, 11))

# op _00rJ_linear_combination_eval
# LANG: _00rw, _00rI --> _00rK
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0762__00rK = _00rJ_constant+1*v0760__00rw+1*v0767__00rI

# op _00rl_linear_combination_eval
# LANG: _00rc, _00rk --> _00rm
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0745__00rm = _00rl_constant+1*v0744__00rc+1*v0749__00rk

# op _00rp_power_combination_eval
# LANG: _00pQ, _00r8 --> _00rq
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0754__00rq = (v0718__00pQ**1)*(v0756__00r8**1)
v0754__00rq = (v0754__00rq*_00rp_coeff).reshape((1, 2, 3, 2, 11))

# op _00uJ expand_array_eval
# LANG: V_aircraft --> _00uK
# SHAPES: (1, 3) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0855__00uK = np.einsum('ab,c->abc', v0846_V_aircraft.reshape((1, 3)) ,np.ones((2,))).reshape((1, 3, 2))

# op _00uP expand_array_eval
# LANG: time_vectors --> _00uQ
# SHAPES: (2,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0861__00uQ = np.einsum('c,ab->abc', v0860_time_vectors.reshape((2,)) ,np.ones((1, 3))).reshape((1, 3, 2))

# op _0108_single_tensor_sum_with_axis_eval
# LANG: _00_E --> An
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01745_An = np.sum(v01736__00_E, axis = (4,)).reshape((1, 2, 3, 40))

# op _010a_single_tensor_sum_with_axis_eval
# LANG: _0107 --> Bn
# SHAPES: (1, 2, 3, 40, 11) --> (1, 2, 3, 40)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01768_Bn = np.sum(v01766__0107, axis = (4,)).reshape((1, 2, 3, 40))

# op _010i reshape_eval
# LANG: _010h --> _010j
# SHAPES: (1, 2, 3, 1, 1) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01770__010j = v01769__010h.reshape((1, 2, 3))

# op _010m expand_array_eval
# LANG: _00TX --> _010n
# SHAPES: (1, 2) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01776__010n = np.einsum('ab,c->abc', v01775__00TX.reshape((1, 2)) ,np.ones((3,))).reshape((1, 2, 3))

# op _011O_power_combination_eval
# LANG: _011N --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01813_chord_profile = (v01812__011N**1)
v01813_chord_profile = (v01813_chord_profile*_011O_coeff).reshape((40, 1))

# op _011Y_indexed_passthrough_eval
# LANG: _011X, _011_, _0123, _0127, _012b --> rot_mat
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01817_rot_mat__temp[i_v01815__011X__011Y_indexed_passthrough_eval] = v01815__011X.flatten()
v01817_rot_mat = v01817_rot_mat__temp.copy()
v01817_rot_mat__temp[i_v01818__011___011Y_indexed_passthrough_eval] = v01818__011_.flatten()
v01817_rot_mat = v01817_rot_mat__temp.copy()
v01817_rot_mat__temp[i_v01820__0123__011Y_indexed_passthrough_eval] = v01820__0123.flatten()
v01817_rot_mat = v01817_rot_mat__temp.copy()
v01817_rot_mat__temp[i_v01822__0127__011Y_indexed_passthrough_eval] = v01822__0127.flatten()
v01817_rot_mat = v01817_rot_mat__temp.copy()
v01817_rot_mat__temp[i_v01824__012b__011Y_indexed_passthrough_eval] = v01824__012b.flatten()
v01817_rot_mat = v01817_rot_mat__temp.copy()

# op _012i_power_combination_eval
# LANG: _012d, _012h --> _012j
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01828__012j = (v01827__012d**1)*(v01830__012h**-1)
v01828__012j = (v01828__012j*_012i_coeff).reshape((3,))

# op _012o_power_combination_eval
# LANG: propeller_radius --> _012p
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01831__012p = (v01810_propeller_radius**1)
v01831__012p = (v01831__012p*_012o_coeff).reshape((1,))

# op _014f expand_array_eval
# LANG: init_obs_z_loc --> _014g
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01901__014g = np.einsum('c,ab->abc', v01900_init_obs_z_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _014o_linear_combination_eval
# LANG: _014c, _014n --> rel_obs_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01890_rel_obs_x_pos = _014o_constant+1*v01889__014c+-1*v01891__014n

# op _014t_linear_combination_eval
# LANG: _014e, _014s --> rel_obs_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01898_rel_obs_y_pos = _014t_constant+1*v01897__014e+-1*v01899__014s

# op _014w_linear_combination_eval
# LANG: aircraft_z_pos, _014v --> _014x
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01903__014x = _014w_constant+1*v01886_aircraft_z_pos+1*v01895__014v

# op _00N1_power_combination_eval
# LANG: _00N0 --> T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01270_T = (v01269__00N0**1)
v01270_T = (v01270_T*_00N1_coeff).reshape((1,))

# op _00O0_power_combination_eval
# LANG: _00N_ --> _00O1
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01372__00O1 = (v01371__00N_**1)
v01372__00O1 = (v01372__00O1*_00O0_coeff).reshape((1,))

# op _00Oa_power_combination_eval
# LANG: _00O9 --> _00Ob
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01377__00Ob = (v01376__00O9**1)
v01377__00Ob = (v01377__00Ob*_00Oa_coeff).reshape((1,))

# op _00Qh_power_combination_eval
# LANG: rpm --> _00Qi
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01432__00Qi = (v01090_rpm**1)
v01432__00Qi = (v01432__00Qi*_00Qh_coeff).reshape((1, 1))

# op _00qO_power_combination_eval
# LANG: _00qt, _00qN --> _00qP
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0725__00qP = (v0719__00qt**1)*(v0729__00qN**1)
v0725__00qP = (v0725__00qP*_00qO_coeff).reshape((1, 2, 3, 2, 11))

# op _00qq_power_combination_eval
# LANG: _00qd, _00qp --> _00qr
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0696__00qr = (v0688__00qd**1)*(v0707__00qp**1)
v0696__00qr = (v0696__00qr*_00qq_coeff).reshape((1, 2, 3, 2, 11))

# op _00rL_power_combination_eval
# LANG: _00rq, _00rK --> _00rM
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0758__00rM = (v0754__00rq**1)*(v0762__00rK**1)
v0758__00rM = (v0758__00rM*_00rL_coeff).reshape((1, 2, 3, 2, 11))

# op _00rn_power_combination_eval
# LANG: _00ra, _00rm --> _00ro
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0743__00ro = (v0739__00ra**1)*(v0745__00rm**1)
v0743__00ro = (v0743__00ro*_00rn_coeff).reshape((1, 2, 3, 2, 11))

# op _00sA_power_combination_eval
# LANG: rotor_disk_in_plane_1 --> _00sB
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((3,))
v0789__00sB = (v08_rotor_disk_in_plane_1**1)
v0789__00sB = (v0789__00sB*_00sA_coeff).reshape((3,))
v08_rotor_disk_in_plane_1 = v08_rotor_disk_in_plane_1.reshape((1, 3))

# op _00sD_power_combination_eval
# LANG: rotor_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v0788_origin = (v012_rotor_disk_origin**1)
v0788_origin = (v0788_origin*_00sD_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _00sG_power_combination_eval
# LANG: rotor_disk_in_plane_2 --> _00sH
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((3,))
v0807__00sH = (v010_rotor_disk_in_plane_2**1)
v0807__00sH = (v0807__00sH*_00sG_coeff).reshape((3,))
v010_rotor_disk_in_plane_2 = v010_rotor_disk_in_plane_2.reshape((1, 3))

# op _00uM expand_array_eval
# LANG: aircraft_location --> _00uN
# SHAPES: (3, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0850__00uN = np.einsum('bc,a->abc', v0849_aircraft_location.reshape((3, 2)) ,np.ones((1,))).reshape((1, 3, 2))

# op _00uT_decompose_eval
# LANG: _00uK --> _00uU, _00v1, _00v8
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0856__00uU = ((v0855__00uK.flatten())[src_indices__00uU__00uT]).reshape((1, 1, 2))
v0857__00v1 = ((v0855__00uK.flatten())[src_indices__00v1__00uT]).reshape((1, 1, 2))
v0858__00v8 = ((v0855__00uK.flatten())[src_indices__00v8__00uT]).reshape((1, 1, 2))

# op _00uV_decompose_eval
# LANG: _00uQ --> _00uW, _00v2, _00v9
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0862__00uW = ((v0861__00uQ.flatten())[src_indices__00uW__00uV]).reshape((1, 1, 2))
v0863__00v2 = ((v0861__00uQ.flatten())[src_indices__00v2__00uV]).reshape((1, 1, 2))
v0864__00v9 = ((v0861__00uQ.flatten())[src_indices__00v9__00uV]).reshape((1, 1, 2))

# op _010C_power_combination_eval
# LANG: _010j --> _010D
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01783__010D = (v01770__010j**1)
v01783__010D = (v01783__010D*_010C_coeff).reshape((1, 2, 3))

# op _010G_power_combination_eval
# LANG: _010n --> _010H
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01786__010H = (v01776__010n**1)
v01786__010H = (v01786__010H*_010G_coeff).reshape((1, 2, 3))

# op _010k expand_scalar_eval
# LANG: _00U4 --> _010l
# SHAPES: (1,) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01773__010l = np.empty((1, 2, 3))
v01773__010l.fill(v01563__00U4.item())

# op _010o expand_scalar_eval
# LANG: speed_of_sound --> _010p
# SHAPES: (1,) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01779__010p = np.empty((1, 2, 3))
v01779__010p.fill(v01478_speed_of_sound.item())

# op _010q_power_combination_eval
# LANG: _010j --> _010r
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01771__010r = (v01770__010j**1)
v01771__010r = (v01771__010r*_010q_coeff).reshape((1, 2, 3))

# op _010u_power_combination_eval
# LANG: _010n --> _010v
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01777__010v = (v01776__010n**1)
v01777__010v = (v01777__010v*_010u_coeff).reshape((1, 2, 3))

# op _011d_single_tensor_sum_with_axis_eval
# LANG: An --> _011e
# SHAPES: (1, 2, 3, 40) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01799__011e = np.sum(v01745_An, axis = (3,)).reshape((1, 2, 3))

# op _011n_single_tensor_sum_with_axis_eval
# LANG: Bn --> _011o
# SHAPES: (1, 2, 3, 40) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01803__011o = np.sum(v01768_Bn, axis = (3,)).reshape((1, 2, 3))

# op _012k_matvec_eval
# LANG: rot_mat, _012j --> thrust_dir
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01825_thrust_dir = v01817_rot_mat@v01828__012j

# op _012q_power_combination_eval
# LANG: _012p --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01832_dr = (v01831__012p**1)
v01832_dr = (v01832_dr*_012q_coeff).reshape((1,))

# op _012u_power_combination_eval
# LANG: rpm --> _012v
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01834__012v = (v01090_rpm**1)
v01834__012v = (v01834__012v*_012u_coeff).reshape((1, 1))

# op _014C_power_combination_eval
# LANG: rel_obs_x_pos --> _014D
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01905__014D = (v01890_rel_obs_x_pos**2)
v01905__014D = (v01905__014D*_014C_coeff).reshape((1, 1, 2))

# op _014E_power_combination_eval
# LANG: rel_obs_y_pos --> _014F
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01907__014F = (v01898_rel_obs_y_pos**2)
v01907__014F = (v01907__014F*_014E_coeff).reshape((1, 1, 2))

# op _014y_linear_combination_eval
# LANG: _014g, _014x --> rel_obs_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01902_rel_obs_z_pos = _014y_constant+1*v01901__014g+-1*v01903__014x

# op _015L single_tensor_sum_no_axis_eval
# LANG: chord_profile --> _015M
# SHAPES: (40, 1) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01929__015M = np.sum(v01813_chord_profile).reshape((1,))

# op _015u_power_combination_eval
# LANG: rpm --> _015v
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01090_rpm = v01090_rpm.reshape((1,))
v01937__015v = (v01090_rpm**1)
v01937__015v = (v01937__015v*_015u_coeff).reshape((1,))
v01090_rpm = v01090_rpm.reshape((1, 1))

# op _00NV_power_combination_eval
# LANG: T, density --> _00NW
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01171_density = v01171_density.reshape((1,))
v01366__00NW = (v01270_T**1)*(v01171_density**-1)
v01366__00NW = (v01366__00NW*_00NV_coeff).reshape((1,))
v01171_density = v01171_density.reshape((1, 1))

# op _00O2_power_combination_eval
# LANG: _00O1 --> _00O3
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01373__00O3 = (v01372__00O1**2)
v01373__00O3 = (v01373__00O3*_00O2_coeff).reshape((1,))

# op _00Oc_power_combination_eval
# LANG: _00Ob --> _00Od
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01378__00Od = (v01377__00Ob**1)
v01378__00Od = (v01378__00Od*_00Oc_coeff).reshape((1,))

# op _00Qj_power_combination_eval
# LANG: _00Qi --> _00Qk
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01433__00Qk = (v01432__00Qi**1)
v01433__00Qk = (v01433__00Qk*_00Qj_coeff).reshape((1, 1))

# op _00qQ_power_combination_eval
# LANG: term_1_coeff_A, _00qr --> _00qR
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0664__00qR = (v0663_term_1_coeff_A**1)*(v0696__00qr**1)
v0664__00qR = (v0664__00qR*_00qQ_coeff).reshape((1, 2, 3, 2, 11))

# op _00qS_power_combination_eval
# LANG: term_2_coeff_A, _00qP --> _00qT
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0716__00qT = (v0715_term_2_coeff_A**1)*(v0725__00qP**1)
v0716__00qT = (v0716__00qT*_00qS_coeff).reshape((1, 2, 3, 2, 11))

# op _00rN_power_combination_eval
# LANG: term_1_coeff_B, _00ro --> _00rO
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0738__00rO = (v0737_term_1_coeff_B**1)*(v0743__00ro**1)
v0738__00rO = (v0738__00rO*_00rN_coeff).reshape((1, 2, 3, 2, 11))

# op _00rP_power_combination_eval
# LANG: term_2_coeff_B, _00rM --> _00rQ
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0753__00rQ = (v0752_term_2_coeff_B**1)*(v0758__00rM**1)
v0753__00rQ = (v0753__00rQ*_00rP_coeff).reshape((1, 2, 3, 2, 11))

# op _00sI pnorm_eval
# LANG: _00sB --> _00sJ
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0790__00sJ = np.linalg.norm(v0789__00sB.flatten(), ord=2)

# op _00tf cross_product_eval
# LANG: _00sB, _00sH --> _00tg
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0808__00tg = np.cross(v0807__00sH, v0789__00sB, axisa = 0, axisb = 0, axisc = 0)

# op _00uR_decompose_eval
# LANG: _00uN --> _00uS, _00v0, _00v7
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0851__00uS = ((v0850__00uN.flatten())[src_indices__00uS__00uR]).reshape((1, 1, 2))
v0852__00v0 = ((v0850__00uN.flatten())[src_indices__00v0__00uR]).reshape((1, 1, 2))
v0853__00v7 = ((v0850__00uN.flatten())[src_indices__00v7__00uR]).reshape((1, 1, 2))

# op _00uX_power_combination_eval
# LANG: _00uU, _00uW --> _00uY
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0859__00uY = (v0856__00uU**1)*(v0862__00uW**1)
v0859__00uY = (v0859__00uY*_00uX_coeff).reshape((1, 1, 2))

# op _00v3_power_combination_eval
# LANG: _00v1, _00v2 --> _00v4
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0866__00v4 = (v0857__00v1**1)*(v0863__00v2**1)
v0866__00v4 = (v0866__00v4*_00v3_coeff).reshape((1, 1, 2))

# op _00vl expand_array_eval
# LANG: origin --> _00vm
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0873__00vm = np.einsum('b,ac->abc', v0788_origin.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _010E_power_combination_eval
# LANG: _010l, _010D --> _010F
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01784__010F = (v01783__010D**1)*(v01773__010l**1)
v01784__010F = (v01784__010F*_010E_coeff).reshape((1, 2, 3))

# op _010I_power_combination_eval
# LANG: _010p, _010H --> _010J
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01787__010J = (v01786__010H**1)*(v01779__010p**1)
v01787__010J = (v01787__010J*_010I_coeff).reshape((1, 2, 3))

# op _010s_power_combination_eval
# LANG: _010r, _010l --> _010t
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01772__010t = (v01771__010r**1)*(v01773__010l**1)
v01772__010t = (v01772__010t*_010s_coeff).reshape((1, 2, 3))

# op _010w_power_combination_eval
# LANG: _010v, _010p --> _010x
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01778__010x = (v01777__010v**1)*(v01779__010p**1)
v01778__010x = (v01778__010x*_010w_coeff).reshape((1, 2, 3))

# op _011f_power_combination_eval
# LANG: _011e --> _011g
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01800__011g = (v01799__011e**1)
v01800__011g = (v01800__011g*_011f_coeff).reshape((1, 2, 3))

# op _011h expand_scalar_eval
# LANG: dr --> _011i
# SHAPES: (1,) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01802__011i = np.empty((1, 2, 3))
v01802__011i.fill(v01430_dr.item())

# op _011p_power_combination_eval
# LANG: _011o --> _011q
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01804__011q = (v01803__011o**1)
v01804__011q = (v01804__011q*_011p_coeff).reshape((1, 2, 3))

# op _011r expand_scalar_eval
# LANG: dr --> _011s
# SHAPES: (1,) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01806__011s = np.empty((1, 2, 3))
v01806__011s.fill(v01430_dr.item())

# op _012w_power_combination_eval
# LANG: _012v --> _012x
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01835__012x = (v01834__012v**1)
v01835__012x = (v01835__012x*_012w_coeff).reshape((1, 1))

# op _014B_indexed_passthrough_eval
# LANG: rel_obs_x_pos, rel_obs_y_pos, rel_obs_z_pos --> rel_obs_position
# SHAPES: (1, 1, 2), (1, 1, 2), (1, 1, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01904_rel_obs_position__temp[i_v01890_rel_obs_x_pos__014B_indexed_passthrough_eval] = v01890_rel_obs_x_pos.flatten()
v01904_rel_obs_position = v01904_rel_obs_position__temp.copy()
v01904_rel_obs_position__temp[i_v01898_rel_obs_y_pos__014B_indexed_passthrough_eval] = v01898_rel_obs_y_pos.flatten()
v01904_rel_obs_position = v01904_rel_obs_position__temp.copy()
v01904_rel_obs_position__temp[i_v01902_rel_obs_z_pos__014B_indexed_passthrough_eval] = v01902_rel_obs_z_pos.flatten()
v01904_rel_obs_position = v01904_rel_obs_position__temp.copy()

# op _014G_linear_combination_eval
# LANG: _014D, _014F --> _014H
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01906__014H = _014G_constant+1*v01905__014D+1*v01907__014F

# op _014I_power_combination_eval
# LANG: rel_obs_z_pos --> _014J
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01909__014J = (v01902_rel_obs_z_pos**2)
v01909__014J = (v01909__014J*_014I_coeff).reshape((1, 1, 2))

# op _014P expand_array_eval
# LANG: thrust_dir --> _014Q
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01912__014Q = np.einsum('b,ac->abc', v01825_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _015N_power_combination_eval
# LANG: _015M, dr --> _015O
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01930__015O = (v01929__015M**1)*(v01832_dr**1)
v01930__015O = (v01930__015O*_015N_coeff).reshape((1,))

# op _015T expand_scalar_eval
# LANG: propeller_radius --> _015U
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01934__015U = np.empty((1, 2))
v01934__015U.fill(v01810_propeller_radius.item())

# op _015w_power_combination_eval
# LANG: _015v --> _015x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01938__015x = (v01937__015v**1)
v01938__015x = (v01938__015x*_015w_coeff).reshape((1,))

# op _00O4_power_combination_eval
# LANG: _00NW, _00O3 --> _00O5
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01367__00O5 = (v01366__00NW**1)*(v01373__00O3**-1)
v01367__00O5 = (v01367__00O5*_00O4_coeff).reshape((1,))

# op _00Oe_power_combination_eval
# LANG: _00Od --> _00Of
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01379__00Of = (v01378__00Od**4)
v01379__00Of = (v01379__00Of*_00Oe_coeff).reshape((1,))

# op _00Ql_power_combination_eval
# LANG: _00Qk --> _00Qm
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01434__00Qm = (v01433__00Qk**1)
v01434__00Qm = (v01434__00Qm*_00Ql_coeff).reshape((1, 1))

# op _00qU_linear_combination_eval
# LANG: _00qR, _00qT --> _00qV
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0714__00qV = _00qU_constant+1*v0664__00qR+1*v0716__00qT

# op _00rR_linear_combination_eval
# LANG: _00rO, _00rQ --> _00rS
# SHAPES: (1, 2, 3, 2, 11), (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0751__00rS = _00rR_constant+1*v0738__00rO+1*v0753__00rQ

# op _00sK_power_combination_eval
# LANG: _00sJ --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0791_propeller_radius = (v0790__00sJ**1)
v0791_propeller_radius = (v0791_propeller_radius*_00sK_coeff).reshape((1,))

# op _00sV_linear_combination_eval
# LANG: theta --> _00sW
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0795__00sW = _00sV_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _00sX_linear_combination_eval
# LANG: theta --> _00sY
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0797__00sY = _00sX_constant+1*v048_theta
v048_theta = v048_theta.reshape((1,))

# op _00t3_sin_eval
# LANG: theta --> _00t4
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0800__00t4 = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00t7_sin_eval
# LANG: theta --> _00t8
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0802__00t8 = np.sin(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00tb_cos_eval
# LANG: theta --> _00tc
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0804__00tc = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00th pnorm_eval
# LANG: _00tg --> _00ti
# SHAPES: (3,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0810__00ti = np.linalg.norm(v0808__00tg.flatten(), ord=2)

# op _00uZ_linear_combination_eval
# LANG: _00uS, _00uY --> aircraft_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0854_aircraft_x_pos = _00uZ_constant+1*v0851__00uS+1*v0859__00uY

# op _00v5_linear_combination_eval
# LANG: _00v0, _00v4 --> aircraft_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0865_aircraft_y_pos = _00v5_constant+1*v0852__00v0+1*v0866__00v4

# op _00va_power_combination_eval
# LANG: _00v8, _00v9 --> _00vb
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0868__00vb = (v0858__00v8**1)*(v0864__00v9**1)
v0868__00vb = (v0868__00vb*_00va_coeff).reshape((1, 1, 2))

# op _00vn_decompose_eval
# LANG: _00vm --> _00vo, _00vt, _00vy
# SHAPES: (1, 3, 2) --> (1, 1, 2), (1, 1, 2), (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0874__00vo = ((v0873__00vm.flatten())[src_indices__00vo__00vn]).reshape((1, 1, 2))
v0875__00vt = ((v0873__00vm.flatten())[src_indices__00vt__00vn]).reshape((1, 1, 2))
v0876__00vy = ((v0873__00vm.flatten())[src_indices__00vy__00vn]).reshape((1, 1, 2))

# op _010K_power_combination_eval
# LANG: _010F, _010J --> _010L
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01785__010L = (v01784__010F**1)*(v01787__010J**-1)
v01785__010L = (v01785__010L*_010K_coeff).reshape((1, 2, 3))

# op _010y_power_combination_eval
# LANG: _010t, _010x --> _010z
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01774__010z = (v01772__010t**1)*(v01778__010x**-1)
v01774__010z = (v01774__010z*_010y_coeff).reshape((1, 2, 3))

# op _011j_power_combination_eval
# LANG: _011g, _011i --> C_real_integrand
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01801_C_real_integrand = (v01800__011g**1)*(v01802__011i**1)
v01801_C_real_integrand = (v01801_C_real_integrand*_011j_coeff).reshape((1, 2, 3))

# op _011t_power_combination_eval
# LANG: _011q, _011s --> C_imag_integrand
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01805_C_imag_integrand = (v01804__011q**1)*(v01806__011s**1)
v01805_C_imag_integrand = (v01805_C_imag_integrand*_011t_coeff).reshape((1, 2, 3))

# op _012y_power_combination_eval
# LANG: _012x --> _012z
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01836__012z = (v01835__012x**1)
v01836__012z = (v01836__012z*_012y_coeff).reshape((1, 1))

# op _014K_linear_combination_eval
# LANG: _014H, _014J --> _014L
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01908__014L = _014K_constant+1*v01906__014H+1*v01909__014J

# op _014R_tensor_dot_product_eval
# LANG: rel_obs_position, _014Q --> normal_proj
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01911_normal_proj = np.sum(v01904_rel_obs_position * v01912__014Q, axis=1)

# op _015A expand_scalar_eval
# LANG: propeller_radius --> _015B
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01941__015B = np.empty((1,))
v01941__015B.fill(v01810_propeller_radius.item())

# op _015P expand_scalar_eval
# LANG: _015O --> _015Q
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01931__015Q = np.empty((1, 2))
v01931__015Q.fill(v01930__015O.item())

# op _015V_power_combination_eval
# LANG: _015U --> _015W
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01935__015W = (v01934__015U**2)
v01935__015W = (v01935__015W*_015V_coeff).reshape((1, 2))

# op _015y_power_combination_eval
# LANG: _015x --> _015z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01939__015z = (v01938__015x**1)
v01939__015z = (v01939__015z*_015y_coeff).reshape((1,))

# op _00Og_power_combination_eval
# LANG: _00O5, _00Of --> C_T
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01374_C_T = (v01367__00O5**1)*(v01379__00Of**-1)
v01374_C_T = (v01374_C_T*_00Og_coeff).reshape((1,))

# op _00QA_power_combination_eval
# LANG: _00Qm --> _00QB
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01444__00QB = (v01434__00Qm**2)
v01444__00QB = (v01444__00QB*_00QA_coeff).reshape((1, 1))

# op _00Qw_power_combination_eval
# LANG: _00Qm --> _00Qx
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01441__00Qx = (v01434__00Qm**2)
v01441__00Qx = (v01441__00Qx*_00Qw_coeff).reshape((1, 1))

# op _00bo_power_combination_eval
# LANG: _angular_speed --> _00bp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0442__00bp = (v0216__angular_speed**1)
v0442__00bp = (v0442__00bp*_00bo_coeff).reshape((1, 40, 30))

# op _00qW_power_combination_eval
# LANG: _00qV --> An
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0736_An = (v0714__00qV**1)
v0736_An = (v0736_An*_00qW_coeff).reshape((1, 2, 3, 2, 11))

# op _00rT_power_combination_eval
# LANG: _00rS --> Bn
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2, 11)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0769_Bn = (v0751__00rS**1)
v0769_Bn = (v0769_Bn*_00rT_coeff).reshape((1, 2, 3, 2, 11))

# op _00sN pnorm_axis_eval
# LANG: rotor_blade_chord_length --> _00sO
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0792__00sO = np.sum(v014_rotor_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00sZ_power_combination_eval
# LANG: _00sW, _00sY --> _00s_
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0796__00s_ = (v0795__00sW**1)*(v0797__00sY**-1)
v0796__00s_ = (v0796__00s_*_00sZ_coeff).reshape((1, 1))

# op _00t1_cos_eval
# LANG: theta --> _00t2
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v048_theta = v048_theta.reshape((1, 1))
v0799__00t2 = np.cos(v048_theta)
v048_theta = v048_theta.reshape((1,))

# op _00t5_power_combination_eval
# LANG: _00t4 --> _00t6
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0801__00t6 = (v0800__00t4**1)
v0801__00t6 = (v0801__00t6*_00t5_coeff).reshape((1, 1))

# op _00t9_power_combination_eval
# LANG: _00t8 --> _00ta
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0803__00ta = (v0802__00t8**1)
v0803__00ta = (v0803__00ta*_00t9_coeff).reshape((1, 1))

# op _00td_power_combination_eval
# LANG: _00tc --> _00te
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0805__00te = (v0804__00tc**1)
v0805__00te = (v0805__00te*_00td_coeff).reshape((1, 1))

# op _00tj expand_scalar_eval
# LANG: _00ti --> _00tk
# SHAPES: (1,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0811__00tk = np.empty((3,))
v0811__00tk.fill(v0810__00ti.item())

# op _00tq_power_combination_eval
# LANG: propeller_radius --> _00tr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0812__00tr = (v0791_propeller_radius**1)
v0812__00tr = (v0812__00tr*_00tq_coeff).reshape((1,))

# op _00vc_linear_combination_eval
# LANG: _00v7, _00vb --> aircraft_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0867_aircraft_z_pos = _00vc_constant+1*v0853__00v7+1*v0868__00vb

# op _00ve expand_array_eval
# LANG: init_obs_x_loc --> _00vf
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0870__00vf = np.einsum('c,ab->abc', v0869_init_obs_x_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00vg expand_array_eval
# LANG: init_obs_y_loc --> _00vh
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0878__00vh = np.einsum('c,ab->abc', v0877_init_obs_y_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00vp_linear_combination_eval
# LANG: aircraft_x_pos, _00vo --> _00vq
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0872__00vq = _00vp_constant+1*v0854_aircraft_x_pos+1*v0874__00vo

# op _00vu_linear_combination_eval
# LANG: aircraft_y_pos, _00vt --> _00vv
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0880__00vv = _00vu_constant+1*v0865_aircraft_y_pos+1*v0875__00vt

# op _010A_power_combination_eval
# LANG: _010z, C_real_integrand --> _010B
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01780__010B = (v01774__010z**1)*(v01801_C_real_integrand**1)
v01780__010B = (v01780__010B*_010A_coeff).reshape((1, 2, 3))

# op _010M_power_combination_eval
# LANG: _010L, C_imag_integrand --> _010N
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01788__010N = (v01785__010L**1)*(v01805_C_imag_integrand**1)
v01788__010N = (v01788__010N*_010M_coeff).reshape((1, 2, 3))

# op _012J_power_combination_eval
# LANG: _012z --> _012K
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01843__012K = (v01836__012z**2)
v01843__012K = (v01843__012K*_012J_coeff).reshape((1, 1))

# op _012N_power_combination_eval
# LANG: _012z --> _012O
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01846__012O = (v01836__012z**2)
v01846__012O = (v01846__012O*_012N_coeff).reshape((1, 1))

# op _014M_power_combination_eval
# LANG: _014L --> rel_obs_dist
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01910_rel_obs_dist = (v01908__014L**0.5)
v01910_rel_obs_dist = (v01910_rel_obs_dist*_014M_coeff).reshape((1, 1, 2))

# op _014X expand_array_eval
# LANG: normal_proj --> _014Y
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01913__014Y = np.einsum('ac,b->abc', v01911_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _015C_power_combination_eval
# LANG: _015z, _015B --> _015D
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01940__015D = (v01939__015z**1)*(v01941__015B**1)
v01940__015D = (v01940__015D*_015C_coeff).reshape((1,))

# op _015R_power_combination_eval
# LANG: _015Q --> Ab
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01932_Ab = (v01931__015Q**1)
v01932_Ab = (v01932_Ab*_015R_coeff).reshape((1, 2))

# op _015X_power_combination_eval
# LANG: _015W --> _015Y
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01936__015Y = (v01935__015W**1)
v01936__015Y = (v01936__015Y*_015X_coeff).reshape((1, 2))

# op _00QC_linear_combination_eval
# LANG: _00QB --> _00QD
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01445__00QD = _00QC_constant+1*v01444__00QB

# op _00Qy_linear_combination_eval
# LANG: _00Qx --> _00Qz
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01442__00Qz = _00Qy_constant+1*v01441__00Qx

# op _00bq_power_combination_eval
# LANG: _00bp --> _00br
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model.induced_velocity_model
v0443__00br = (v0442__00bp**1)
v0443__00br = (v0443__00br*_00bq_coeff).reshape((1, 40, 30))

# op _00rV_single_tensor_sum_with_axis_eval
# LANG: An --> _00rW
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0770__00rW = np.sum(v0736_An, axis = (4,)).reshape((1, 2, 3, 2))

# op _00rX_single_tensor_sum_with_axis_eval
# LANG: Bn --> _00rY
# SHAPES: (1, 2, 3, 2, 11) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0773__00rY = np.sum(v0769_Bn, axis = (4,)).reshape((1, 2, 3, 2))

# op _00sP reshape_eval
# LANG: _00sO --> _00sQ
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0793__00sQ = v0792__00sO.reshape((40, 1))

# op _00t0_indexed_passthrough_eval
# LANG: _00s_, _00t2, _00t6, _00ta, _00te --> rot_mat
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0798_rot_mat__temp[i_v0796__00s___00t0_indexed_passthrough_eval] = v0796__00s_.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()
v0798_rot_mat__temp[i_v0799__00t2__00t0_indexed_passthrough_eval] = v0799__00t2.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()
v0798_rot_mat__temp[i_v0801__00t6__00t0_indexed_passthrough_eval] = v0801__00t6.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()
v0798_rot_mat__temp[i_v0803__00ta__00t0_indexed_passthrough_eval] = v0803__00ta.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()
v0798_rot_mat__temp[i_v0805__00te__00t0_indexed_passthrough_eval] = v0805__00te.flatten()
v0798_rot_mat = v0798_rot_mat__temp.copy()

# op _00tl_power_combination_eval
# LANG: _00tg, _00tk --> _00tm
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0809__00tm = (v0808__00tg**1)*(v0811__00tk**-1)
v0809__00tm = (v0809__00tm*_00tl_coeff).reshape((3,))

# op _00ts_power_combination_eval
# LANG: _00tr --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0813_dr = (v0812__00tr**1)
v0813_dr = (v0813_dr*_00ts_coeff).reshape((1,))

# op _00vi expand_array_eval
# LANG: init_obs_z_loc --> _00vj
# SHAPES: (2,) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0882__00vj = np.einsum('c,ab->abc', v0881_init_obs_z_loc.reshape((2,)) ,np.ones((1, 1))).reshape((1, 1, 2))

# op _00vr_linear_combination_eval
# LANG: _00vf, _00vq --> rel_obs_x_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0871_rel_obs_x_pos = _00vr_constant+1*v0870__00vf+-1*v0872__00vq

# op _00vw_linear_combination_eval
# LANG: _00vh, _00vv --> rel_obs_y_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0879_rel_obs_y_pos = _00vw_constant+1*v0878__00vh+-1*v0880__00vv

# op _00vz_linear_combination_eval
# LANG: aircraft_z_pos, _00vy --> _00vA
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0884__00vA = _00vz_constant+1*v0867_aircraft_z_pos+1*v0876__00vy

# op _00ww reshape_eval
# LANG: rpm --> _00wx
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0915__00wx = v0164_rpm.reshape((1,))

# op _010O_power_combination_eval
# LANG: _010B --> _010P
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01781__010P = (v01780__010B**2)
v01781__010P = (v01781__010P*_010O_coeff).reshape((1, 2, 3))

# op _010Q_power_combination_eval
# LANG: _010N --> _010R
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01789__010R = (v01788__010N**2)
v01789__010R = (v01789__010R*_010Q_coeff).reshape((1, 2, 3))

# op _012L_linear_combination_eval
# LANG: _012K --> _012M
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01844__012M = _012L_constant+1*v01843__012K

# op _012P_linear_combination_eval
# LANG: _012O --> _012Q
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01847__012Q = _012P_constant+1*v01846__012O

# op _014Z_power_combination_eval
# LANG: rel_obs_dist, _014Y --> _014_
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01914__014_ = (v01913__014Y**1)*(v01910_rel_obs_dist**-1)
v01914__014_ = (v01914__014_*_014Z_coeff).reshape((1, 1, 2))

# op _015E expand_scalar_eval
# LANG: _015D --> _015F
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01942__015F = np.empty((1, 2))
v01942__015F.fill(v01940__015D.item())

# op _015H expand_scalar_eval
# LANG: CT --> _015I
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01947__015I = np.empty((1, 2))
v01947__015I.fill(v01374_C_T.item())

# op _015Z_power_combination_eval
# LANG: Ab, _015Y --> sigma
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01933_sigma = (v01932_Ab**1)*(v01936__015Y**-1)
v01933_sigma = (v01933_sigma*_015Z_coeff).reshape((1, 2))

# op _00QE_power_combination_eval
# LANG: _00Qz, _00QD --> _00QF
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01443__00QF = (v01442__00Qz**1)*(v01445__00QD**1)
v01443__00QF = (v01443__00QF*_00QE_coeff).reshape((1, 1))

# op _00Qs_power_combination_eval
# LANG: _00Qm --> _00Qt
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01438__00Qt = (v01434__00Qm**2)
v01438__00Qt = (v01438__00Qt*_00Qs_coeff).reshape((1, 1))

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

# op _00rZ_power_combination_eval
# LANG: _00rW --> _00r_
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0771__00r_ = (v0770__00rW**2)
v0771__00r_ = (v0771__00r_*_00rZ_coeff).reshape((1, 2, 3, 2))

# op _00s0_power_combination_eval
# LANG: _00rY --> _00s1
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0774__00s1 = (v0773__00rY**2)
v0774__00s1 = (v0774__00s1*_00s0_coeff).reshape((1, 2, 3, 2))

# op _00sR_power_combination_eval
# LANG: _00sQ --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0794_chord_profile = (v0793__00sQ**1)
v0794_chord_profile = (v0794_chord_profile*_00sR_coeff).reshape((40, 1))

# op _00tn_matvec_eval
# LANG: rot_mat, _00tm --> thrust_dir
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0806_thrust_dir = v0798_rot_mat@v0809__00tm

# op _00vB_linear_combination_eval
# LANG: _00vj, _00vA --> rel_obs_z_pos
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0883_rel_obs_z_pos = _00vB_constant+1*v0882__00vj+-1*v0884__00vA

# op _00vF_power_combination_eval
# LANG: rel_obs_x_pos --> _00vG
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0886__00vG = (v0871_rel_obs_x_pos**2)
v0886__00vG = (v0886__00vG*_00vF_coeff).reshape((1, 1, 2))

# op _00vH_power_combination_eval
# LANG: rel_obs_y_pos --> _00vI
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0888__00vI = (v0879_rel_obs_y_pos**2)
v0888__00vI = (v0888__00vI*_00vH_coeff).reshape((1, 1, 2))

# op _00wW expand_scalar_eval
# LANG: dr --> _00wX
# SHAPES: (1,) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0911__00wX = np.empty((40, 1))
v0911__00wX.fill(v0813_dr.item())

# op _00wy_power_combination_eval
# LANG: _00wx --> _00wz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0916__00wz = (v0915__00wx**1)
v0916__00wz = (v0916__00wz*_00wy_coeff).reshape((1,))

# op _010S_linear_combination_eval
# LANG: _010P, _010R --> _010T
# SHAPES: (1, 2, 3), (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01782__010T = _010S_constant+1*v01781__010P+1*v01789__010R

# op _012F_power_combination_eval
# LANG: _012z --> _012G
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01840__012G = (v01836__012z**2)
v01840__012G = (v01840__012G*_012F_coeff).reshape((1, 1))

# op _012R_power_combination_eval
# LANG: _012M, _012Q --> _012S
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01845__012S = (v01844__012M**1)*(v01847__012Q**1)
v01845__012S = (v01845__012S*_012R_coeff).reshape((1, 1))

# op _0150_arcsin_eval
# LANG: _014_ --> _0151
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01915__0151 = np.arcsin(v01914__014_)

# op _0160_power_combination_eval
# LANG: _015F --> _0161
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01943__0161 = (v01942__015F**3.68)
v01943__0161 = (v01943__0161*_0160_coeff).reshape((1, 2))

# op _0162_power_combination_eval
# LANG: Ab --> _0163
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01945__0163 = (v01932_Ab**0.9)
v01945__0163 = (v01945__0163*_0162_coeff).reshape((1, 2))

# op _0166_power_combination_eval
# LANG: sigma, _015I --> _0167
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01948__0167 = (v01947__015I**1)*(v01933_sigma**-1)
v01948__0167 = (v01948__0167*_0166_coeff).reshape((1, 2))

# op _016i_power_combination_eval
# LANG: _015F --> _016j
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01960__016j = (v01942__015F**7.44)
v01960__016j = (v01960__016j*_016i_coeff).reshape((1, 2))

# op _016k_power_combination_eval
# LANG: Ab --> _016l
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01962__016l = (v01932_Ab**0.9)
v01962__016l = (v01962__016l*_016k_coeff).reshape((1, 2))

# op _016o_power_combination_eval
# LANG: sigma, _015I --> _016p
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01964__016p = (v01947__015I**1)*(v01933_sigma**-1)
v01964__016p = (v01964__016p*_016o_coeff).reshape((1, 2))

# op _00QG_power_combination_eval
# LANG: _00QF --> _00QH
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01446__00QH = (v01443__00QF**0.5)
v01446__00QH = (v01446__00QH*_00QG_coeff).reshape((1, 1))

# op _00QK_power_combination_eval
# LANG: _00Qm --> _00QL
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01448__00QL = (v01434__00Qm**2)
v01448__00QL = (v01448__00QL*_00QK_coeff).reshape((1, 1))

# op _00Qu_linear_combination_eval
# LANG: _00Qt --> _00Qv
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01439__00Qv = _00Qu_constant+1*v01438__00Qt

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

# op _00s2_linear_combination_eval
# LANG: _00r_, _00s1 --> _00s3
# SHAPES: (1, 2, 3, 2), (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0772__00s3 = _00s2_constant+1*v0771__00r_+1*v0774__00s1

# op _00vE_indexed_passthrough_eval
# LANG: rel_obs_x_pos, rel_obs_y_pos, rel_obs_z_pos --> rel_obs_position
# SHAPES: (1, 1, 2), (1, 1, 2), (1, 1, 2) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0885_rel_obs_position__temp[i_v0871_rel_obs_x_pos__00vE_indexed_passthrough_eval] = v0871_rel_obs_x_pos.flatten()
v0885_rel_obs_position = v0885_rel_obs_position__temp.copy()
v0885_rel_obs_position__temp[i_v0879_rel_obs_y_pos__00vE_indexed_passthrough_eval] = v0879_rel_obs_y_pos.flatten()
v0885_rel_obs_position = v0885_rel_obs_position__temp.copy()
v0885_rel_obs_position__temp[i_v0883_rel_obs_z_pos__00vE_indexed_passthrough_eval] = v0883_rel_obs_z_pos.flatten()
v0885_rel_obs_position = v0885_rel_obs_position__temp.copy()

# op _00vJ_linear_combination_eval
# LANG: _00vG, _00vI --> _00vK
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0887__00vK = _00vJ_constant+1*v0886__00vG+1*v0888__00vI

# op _00vL_power_combination_eval
# LANG: rel_obs_z_pos --> _00vM
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0890__00vM = (v0883_rel_obs_z_pos**2)
v0890__00vM = (v0890__00vM*_00vL_coeff).reshape((1, 1, 2))

# op _00vS expand_array_eval
# LANG: thrust_dir --> _00vT
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0893__00vT = np.einsum('b,ac->abc', v0806_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00wA_power_combination_eval
# LANG: _00wz --> _00wB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0917__00wB = (v0916__00wz**1)
v0917__00wB = (v0917__00wB*_00wA_coeff).reshape((1,))

# op _00wY_power_combination_eval
# LANG: _00wX, chord_profile --> _00wZ
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0910__00wZ = (v0794_chord_profile**1)*(v0911__00wX**1)
v0910__00wZ = (v0910__00wZ*_00wY_coeff).reshape((40, 1))

# op _010U_power_combination_eval
# LANG: _010T --> _010V
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01790__010V = (v01782__010T**1)
v01790__010V = (v01790__010V*_010U_coeff).reshape((1, 2, 3))

# op _012H_linear_combination_eval
# LANG: _012G --> _012I
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01841__012I = _012H_constant+1*v01840__012G

# op _012T_power_combination_eval
# LANG: _012S --> _012U
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01848__012U = (v01845__012S**0.5)
v01848__012U = (v01848__012U*_012T_coeff).reshape((1, 1))

# op _012X_power_combination_eval
# LANG: _012z --> _012Y
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01850__012Y = (v01836__012z**2)
v01850__012Y = (v01850__012Y*_012X_coeff).reshape((1, 1))

# op _0158 reshape_eval
# LANG: _0151 --> rel_angle_plane
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01916_rel_angle_plane = v01915__0151.reshape((1, 2))

# op _0164_power_combination_eval
# LANG: _0161, _0163 --> _0165
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01944__0165 = (v01943__0161**1)*(v01945__0163**1)
v01944__0165 = (v01944__0165*_0164_coeff).reshape((1, 2))

# op _0168_power_combination_eval
# LANG: _0167 --> _0169
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01949__0169 = (v01948__0167**1.6)
v01949__0169 = (v01949__0169*_0168_coeff).reshape((1, 2))

# op _016A_linear_combination_eval
# LANG: Ab --> _016B
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01954__016B = _016A_constant+-1*v01932_Ab

# op _016M_linear_combination_eval
# LANG: Ab --> _016N
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01970__016N = _016M_constant+1*v01932_Ab

# op _016m_power_combination_eval
# LANG: _016j, _016l --> _016n
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01961__016n = (v01960__016j**1)*(v01962__016l**1)
v01961__016n = (v01961__016n*_016m_coeff).reshape((1, 2))

# op _016q_power_combination_eval
# LANG: _016p --> _016r
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01965__016r = (v01964__016p**1.6)
v01965__016r = (v01965__016r*_016q_coeff).reshape((1, 2))

# op _00QI_power_combination_eval
# LANG: _00Qv, _00QH --> _00QJ
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01440__00QJ = (v01439__00Qv**1)*(v01446__00QH**1)
v01440__00QJ = (v01440__00QJ*_00QI_coeff).reshape((1, 1))

# op _00QM_linear_combination_eval
# LANG: _00QL --> _00QN
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01449__00QN = _00QM_constant+1*v01448__00QL

# op _00Qo_power_combination_eval
# LANG: _00Qm --> _00Qp
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01435__00Qp = (v01434__00Qm**4)
v01435__00Qp = (v01435__00Qp*_00Qo_coeff).reshape((1, 1))

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

# op _00s4_power_combination_eval
# LANG: _00s3 --> _00s5
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0775__00s5 = (v0772__00s3**1)
v0775__00s5 = (v0775__00s5*_00s4_coeff).reshape((1, 2, 3, 2))

# op _00tx_power_combination_eval
# LANG: rpm --> _00ty
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0815__00ty = (v0164_rpm**1)
v0815__00ty = (v0815__00ty*_00tx_coeff).reshape((1, 1))

# op _00vN_linear_combination_eval
# LANG: _00vK, _00vM --> _00vO
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0889__00vO = _00vN_constant+1*v0887__00vK+1*v0890__00vM

# op _00vU_tensor_dot_product_eval
# LANG: rel_obs_position, _00vT --> normal_proj
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0892_normal_proj = np.sum(v0885_rel_obs_position * v0893__00vT, axis=1)

# op _00wC_power_combination_eval
# LANG: _00wB --> _00wD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0918__00wD = (v0917__00wB**1)
v0918__00wD = (v0918__00wD*_00wC_coeff).reshape((1,))

# op _00w__single_tensor_sum_with_axis_eval
# LANG: _00wZ --> _00x0
# SHAPES: (40, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0912__00x0 = np.sum(v0910__00wZ, axis = (0,)).reshape((1,))

# op _010W_power_combination_eval
# LANG: _010V --> _010X
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01791__010X = (v01790__010V**1)
v01791__010X = (v01791__010X*_010W_coeff).reshape((1, 2, 3))

# op _012B_power_combination_eval
# LANG: _012z --> _012C
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01837__012C = (v01836__012z**4)
v01837__012C = (v01837__012C*_012B_coeff).reshape((1, 1))

# op _012V_power_combination_eval
# LANG: _012I, _012U --> _012W
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01842__012W = (v01841__012I**1)*(v01848__012U**1)
v01842__012W = (v01842__012W*_012V_coeff).reshape((1, 1))

# op _012Z_linear_combination_eval
# LANG: _012Y --> _012_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01851__012_ = _012Z_constant+1*v01850__012Y

# op _016C_power_combination_eval
# LANG: _016B --> _016D
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01955__016D = (v01954__016B**1)
v01955__016D = (v01955__016D*_016C_coeff).reshape((1, 2))

# op _016O_power_combination_eval
# LANG: _016N --> _016P
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01971__016P = (v01970__016N**1)
v01971__016P = (v01971__016P*_016O_coeff).reshape((1, 2))

# op _016a_power_combination_eval
# LANG: _0165, _0169 --> _016b
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01946__016b = (v01944__0165**1)*(v01949__0169**1)
v01946__016b = (v01946__016b*_016a_coeff).reshape((1, 2))

# op _016s_power_combination_eval
# LANG: _016n, _016r --> _016t
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01963__016t = (v01961__016n**1)*(v01965__016r**1)
v01963__016t = (v01963__016t*_016s_coeff).reshape((1, 2))

# op _017o_power_combination_eval
# LANG: rel_angle_plane --> _017p
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01987__017p = (v01916_rel_angle_plane**2)
v01987__017p = (v01987__017p*_017o_coeff).reshape((1, 2))

# op _00QO_power_combination_eval
# LANG: _00QJ, _00QN --> _00QP
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01447__00QP = (v01440__00QJ**1)*(v01449__00QN**1)
v01447__00QP = (v01447__00QP*_00QO_coeff).reshape((1, 1))

# op _00Qq_power_combination_eval
# LANG: _00Qp --> _00Qr
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01436__00Qr = (v01435__00Qp**1)
v01436__00Qr = (v01436__00Qr*_00Qq_coeff).reshape((1, 1))

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

# op _00s6_log10_eval
# LANG: _00s5 --> _00s7
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0776__00s7 = np.log10(v0775__00s5)

# op _00tz_power_combination_eval
# LANG: _00ty --> _00tA
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0816__00tA = (v0815__00ty**1)
v0816__00tA = (v0816__00tA*_00tz_coeff).reshape((1, 1))

# op _00vP_power_combination_eval
# LANG: _00vO --> rel_obs_dist
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0891_rel_obs_dist = (v0889__00vO**0.5)
v0891_rel_obs_dist = (v0891_rel_obs_dist*_00vP_coeff).reshape((1, 1, 2))

# op _00v_ expand_array_eval
# LANG: normal_proj --> _00w0
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0894__00w0 = np.einsum('ac,b->abc', v0892_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00wE_linear_combination_eval
# LANG: _00wD --> _00wF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0919__00wF = _00wE_constant+1*v0918__00wD

# op _00x1_power_combination_eval
# LANG: _00x0 --> _00x2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0913__00x2 = (v0912__00x0**1)
v0913__00x2 = (v0913__00x2*_00x1_coeff).reshape((1,))

# op _010Y_log10_eval
# LANG: _010X --> _010Z
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01792__010Z = np.log10(v01791__010X)

# op _012D_power_combination_eval
# LANG: _012C --> _012E
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01838__012E = (v01837__012C**1)
v01838__012E = (v01838__012E*_012D_coeff).reshape((1, 1))

# op _0130_power_combination_eval
# LANG: _012W, _012_ --> _0131
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01849__0131 = (v01842__012W**1)*(v01851__012_**1)
v01849__0131 = (v01849__0131*_0130_coeff).reshape((1, 1))

# op _016E_tanh_eval
# LANG: _016D --> _016F
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01956__016F = np.tanh(v01955__016D)

# op _016Q_tanh_eval
# LANG: _016P --> _016R
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01972__016R = np.tanh(v01971__016P)

# op _016c_log10_eval
# LANG: _016b --> _016d
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01950__016d = np.log10(v01946__016b)

# op _016u_log10_eval
# LANG: _016t --> _016v
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01966__016v = np.log10(v01963__016t)

# op _017q_power_combination_eval
# LANG: _017p --> _017r
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01988__017r = (v01987__017p**0.5)
v01988__017r = (v01988__017r*_017q_coeff).reshape((1, 2))

# op _00QQ_power_combination_eval
# LANG: _00Qr, _00QP --> _00QR
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01437__00QR = (v01436__00Qr**1)*(v01447__00QP**-1)
v01437__00QR = (v01437__00QR*_00QQ_coeff).reshape((1, 1))

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

# op _00s8_power_combination_eval
# LANG: _00s7 --> bladeSPL
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0777_bladeSPL = (v0776__00s7**1)
v0777_bladeSPL = (v0777_bladeSPL*_00s8_coeff).reshape((1, 2, 3, 2))

# op _00tB_power_combination_eval
# LANG: _00tA --> _00tC
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0817__00tC = (v0816__00tA**1)
v0817__00tC = (v0817__00tC*_00tB_coeff).reshape((1, 1))

# op _00w1_power_combination_eval
# LANG: rel_obs_dist, _00w0 --> _00w2
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0895__00w2 = (v0894__00w0**1)*(v0891_rel_obs_dist**-1)
v0895__00w2 = (v0895__00w2*_00w1_coeff).reshape((1, 1, 2))

# op _00wG expand_scalar_eval
# LANG: _00wF --> _00wH
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0920__00wH = np.empty((1, 2))
v0920__00wH.fill(v0919__00wF.item())

# op _00wJ expand_scalar_eval
# LANG: propeller_radius --> _00wK
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0923__00wK = np.empty((1, 2))
v0923__00wK.fill(v0791_propeller_radius.item())

# op _00x3 expand_scalar_eval
# LANG: _00x2 --> Ab
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0914_Ab = np.empty((1, 2))
v0914_Ab.fill(v0913__00x2.item())

# op _010__power_combination_eval
# LANG: _010Z --> _0110
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01793__0110 = (v01792__010Z**1)
v01793__0110 = (v01793__0110*_010__coeff).reshape((1, 2, 3))

# op _0132_power_combination_eval
# LANG: _012E, _0131 --> _0133
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01839__0133 = (v01838__012E**1)*(v01849__0131**-1)
v01839__0133 = (v01839__0133*_0132_coeff).reshape((1, 1))

# op _016G_power_combination_eval
# LANG: _016F --> _016H
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01957__016H = (v01956__016F**1)
v01957__016H = (v01957__016H*_016G_coeff).reshape((1, 2))

# op _016S_power_combination_eval
# LANG: _016R --> _016T
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01973__016T = (v01972__016R**1)
v01973__016T = (v01973__016T*_016S_coeff).reshape((1, 2))

# op _016__power_combination_eval
# LANG: propeller_radius --> _0170
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01983__0170 = (v01810_propeller_radius**1)
v01983__0170 = (v01983__0170*_016__coeff).reshape((1,))

# op _016e_power_combination_eval
# LANG: _016d --> _016f
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01951__016f = (v01950__016d**1)
v01951__016f = (v01951__016f*_016e_coeff).reshape((1, 2))

# op _016w_power_combination_eval
# LANG: _016v --> _016x
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01967__016x = (v01966__016v**1)
v01967__016x = (v01967__016x*_016w_coeff).reshape((1, 2))

# op _017a_power_combination_eval
# LANG: rel_angle_plane --> _017b
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01976__017b = (v01916_rel_angle_plane**2.0)
v01976__017b = (v01976__017b*_017a_coeff).reshape((1, 2))

# op _017s_sin_eval
# LANG: _017r --> _017t
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01989__017t = np.sin(v01988__017r)

# op _00QS_log10_eval
# LANG: _00QR --> _00QT
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01450__00QT = np.log10(v01437__00QR)

# op _00QW_log10_eval
# LANG: RA_1000 --> _00QX
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01454__00QX = np.log10(v01453_RA_1000)

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

# op _00sa_power_combination_eval
# LANG: bladeSPL --> _00sb
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0778__00sb = (v0777_bladeSPL**1)
v0778__00sb = (v0778__00sb*_00sa_coeff).reshape((1, 2, 3, 2))

# op _00tM_power_combination_eval
# LANG: _00tC --> _00tN
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0824__00tN = (v0817__00tC**2)
v0824__00tN = (v0824__00tN*_00tM_coeff).reshape((1, 1))

# op _00tQ_power_combination_eval
# LANG: _00tC --> _00tR
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0827__00tR = (v0817__00tC**2)
v0827__00tR = (v0827__00tR*_00tQ_coeff).reshape((1, 1))

# op _00w3_arcsin_eval
# LANG: _00w2 --> _00w4
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0896__00w4 = np.arcsin(v0895__00w2)

# op _00wS_linear_combination_eval
# LANG: _00wH --> _00wT
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0921__00wT = _00wS_constant+1*v0920__00wH

# op _00x5_power_combination_eval
# LANG: Ab --> _00x6
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0929__00x6 = (v0914_Ab**1)
v0929__00x6 = (v0929__00x6*_00x5_coeff).reshape((1, 2))

# op _00x7_power_combination_eval
# LANG: _00wK --> _00x8
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0931__00x8 = (v0923__00wK**2)
v0931__00x8 = (v0931__00x8*_00x7_coeff).reshape((1, 2))

# op _0111_power_combination_eval
# LANG: _0110 --> _0112
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01794__0112 = (v01793__0110**1)
v01794__0112 = (v01794__0112*_0111_coeff).reshape((1, 2, 3))

# op _0134_log10_eval
# LANG: _0133 --> _0135
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01852__0135 = np.log10(v01839__0133)

# op _0138_log10_eval
# LANG: RA_1000 --> _0139
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01856__0139 = np.log10(v01855_RA_1000)

# op _016I_linear_combination_eval
# LANG: _016H --> _016J
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01958__016J = _016I_constant+1*v01957__016H

# op _016U_linear_combination_eval
# LANG: _016T --> _016V
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01974__016V = _016U_constant+1*v01973__016T

# op _016g_linear_combination_eval
# LANG: _016f --> _016h
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01952__016h = _016g_constant+1*v01951__016f

# op _016y_linear_combination_eval
# LANG: _016x --> _016z
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01968__016z = _016y_constant+1*v01967__016x

# op _0171 expand_scalar_eval
# LANG: _0170 --> _0172
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01984__0172 = np.empty((1, 2))
v01984__0172.fill(v01983__0170.item())

# op _0174 reshape_eval
# LANG: rel_obs_dist --> _0175
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01981__0175 = v01910_rel_obs_dist.reshape((1, 2))

# op _017c_power_combination_eval
# LANG: _017b --> _017d
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01977__017d = (v01976__017b**0.5)
v01977__017d = (v01977__017d*_017c_coeff).reshape((1, 2))

# op _017u_linear_combination_eval
# LANG: _017t --> _017v
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01990__017v = _017u_constant+-1*v01989__017t

# op _00QU_power_combination_eval
# LANG: _00QT --> _00QV
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01451__00QV = (v01450__00QT**1)
v01451__00QV = (v01451__00QV*_00QU_coeff).reshape((1, 1))

# op _00QY_power_combination_eval
# LANG: _00QX --> _00QZ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01455__00QZ = (v01454__00QX**1)
v01455__00QZ = (v01455__00QZ*_00QY_coeff).reshape((1, 1))

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
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0779__00sd = _00sc_exp_a_eval_a**v0778__00sb

# op _00tO_linear_combination_eval
# LANG: _00tN --> _00tP
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0825__00tP = _00tO_constant+1*v0824__00tN

# op _00tS_linear_combination_eval
# LANG: _00tR --> _00tT
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0828__00tT = _00tS_constant+1*v0827__00tR

# op _00wb reshape_eval
# LANG: _00w4 --> rel_angle_plane
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0897_rel_angle_plane = v0896__00w4.reshape((1, 2))

# op _00x9_power_combination_eval
# LANG: _00x6, _00x8 --> _00xa
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0930__00xa = (v0929__00x6**1)*(v0931__00x8**-1)
v0930__00xa = (v0930__00xa*_00x9_coeff).reshape((1, 2))

# op _00xc expand_scalar_eval
# LANG: CT --> _00xd
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0927__00xd = np.empty((1, 2))
v0927__00xd.fill(v0448_C_T.item())

# op _00xe_power_combination_eval
# LANG: _00wT, _00wK --> _00xf
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0922__00xf = (v0921__00wT**1)*(v0923__00wK**1)
v0922__00xf = (v0922__00xf*_00xe_coeff).reshape((1, 2))

# op _0113_exp_a_eval
# LANG: _0112 --> _0114
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01795__0114 = _0113_exp_a_eval_a**v01794__0112

# op _0136_power_combination_eval
# LANG: _0135 --> _0137
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01853__0137 = (v01852__0135**1)
v01853__0137 = (v01853__0137*_0136_coeff).reshape((1, 1))

# op _013a_power_combination_eval
# LANG: _0139 --> _013b
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01857__013b = (v01856__0139**1)
v01857__013b = (v01857__013b*_013a_coeff).reshape((1, 1))

# op _016K_power_combination_eval
# LANG: _016h, _016J --> _016L
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01953__016L = (v01952__016h**1)*(v01958__016J**1)
v01953__016L = (v01953__016L*_016K_coeff).reshape((1, 2))

# op _016W_power_combination_eval
# LANG: _016z, _016V --> _016X
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01969__016X = (v01968__016z**1)*(v01974__016V**1)
v01969__016X = (v01969__016X*_016W_coeff).reshape((1, 2))

# op _017e_sin_eval
# LANG: _017d --> _017f
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01978__017f = np.sin(v01977__017d)

# op _017k_power_combination_eval
# LANG: _0175, _0172 --> _017l
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01982__017l = (v01981__0175**1)*(v01984__0172**-1)
v01982__017l = (v01982__017l*_017k_coeff).reshape((1, 2))

# op _017w_power_combination_eval
# LANG: _017v --> _017x
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01991__017x = (v01990__017v**1)
v01991__017x = (v01991__017x*_017w_coeff).reshape((1, 2))

# op _00Q__linear_combination_eval
# LANG: _00QV, _00QZ --> _00R0
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01452__00R0 = _00Q__constant+1*v01451__00QV+-1*v01455__00QZ

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
# SHAPES: (1, 2, 3, 2) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0780__00sf = np.sum(v0779__00sd, axis = (3,)).reshape((1, 2, 3))

# op _00tI_power_combination_eval
# LANG: _00tC --> _00tJ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0821__00tJ = (v0817__00tC**2)
v0821__00tJ = (v0821__00tJ*_00tI_coeff).reshape((1, 1))

# op _00tU_power_combination_eval
# LANG: _00tP, _00tT --> _00tV
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0826__00tV = (v0825__00tP**1)*(v0828__00tT**1)
v0826__00tV = (v0826__00tV*_00tU_coeff).reshape((1, 1))

# op _00xg_power_combination_eval
# LANG: _00xf --> _00xh
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0924__00xh = (v0922__00xf**6)
v0924__00xh = (v0924__00xh*_00xg_coeff).reshape((1, 2))

# op _00xk_power_combination_eval
# LANG: _00xd, _00xa --> _00xl
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0928__00xl = (v0927__00xd**1)*(v0930__00xa**-1)
v0928__00xl = (v0928__00xl*_00xk_coeff).reshape((1, 2))

# op _00xy_power_combination_eval
# LANG: rel_angle_plane --> _00xz
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0938__00xz = (v0897_rel_angle_plane**2)
v0938__00xz = (v0938__00xz*_00xy_coeff).reshape((1, 2))

# op _0115_single_tensor_sum_with_axis_eval
# LANG: _0114 --> _0116
# SHAPES: (1, 2, 3) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01796__0116 = np.sum(v01795__0114, axis = (2,)).reshape((1, 2))

# op _013c_linear_combination_eval
# LANG: _0137, _013b --> _013d
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01854__013d = _013c_constant+1*v01853__0137+-1*v01857__013b

# op _016Y_linear_combination_eval
# LANG: _016L, _016X --> _016Z
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01959__016Z = _016Y_constant+1*v01953__016L+1*v01969__016X

# op _017g_power_combination_eval
# LANG: _017f --> _017h
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01979__017h = (v01978__017f**0.031)
v01979__017h = (v01979__017h*_017g_coeff).reshape((1, 2))

# op _017m_log10_eval
# LANG: _017l --> _017n
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01985__017n = np.log10(v01982__017l)

# op _017y_linear_combination_eval
# LANG: _017x --> _017z
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01992__017z = _017y_constant+1*v01991__017x

# op _00KS_power_combination_eval
# LANG: _radius --> _00KT
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01271__00KT = (v01143__radius**2)
v01271__00KT = (v01271__00KT*_00KS_coeff).reshape((1, 40, 100))

# op _00R1 reshape_eval
# LANG: _00R0 --> _00R2
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01456__00R2 = v01452__00R0.reshape((1,))

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
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0781__00sh = np.log10(v0780__00sf)

# op _00tK_linear_combination_eval
# LANG: _00tJ --> _00tL
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0822__00tL = _00tK_constant+1*v0821__00tJ

# op _00tW_power_combination_eval
# LANG: _00tV --> _00tX
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0829__00tX = (v0826__00tV**0.5)
v0829__00tX = (v0829__00tX*_00tW_coeff).reshape((1, 1))

# op _00t__power_combination_eval
# LANG: _00tC --> _00u0
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0831__00u0 = (v0817__00tC**2)
v0831__00u0 = (v0831__00u0*_00t__coeff).reshape((1, 1))

# op _00wM reshape_eval
# LANG: rel_obs_dist --> _00wN
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0942__00wN = v0891_rel_obs_dist.reshape((1, 2))

# op _00xA_power_combination_eval
# LANG: _00xz --> _00xB
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0939__00xB = (v0938__00xz**0.5)
v0939__00xB = (v0939__00xB*_00xA_coeff).reshape((1, 2))

# op _00xi_power_combination_eval
# LANG: Ab, _00xh --> _00xj
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0925__00xj = (v0924__00xh**1)*(v0914_Ab**1)
v0925__00xj = (v0925__00xj*_00xi_coeff).reshape((1, 2))

# op _00xm_power_combination_eval
# LANG: _00xl --> _00xn
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0932__00xn = (v0928__00xl**2)
v0932__00xn = (v0932__00xn*_00xm_coeff).reshape((1, 2))

# op _0117_log10_eval
# LANG: _0116 --> _0118
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01797__0118 = np.log10(v01796__0116)

# op _013e reshape_eval
# LANG: _013d --> _013f
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01858__013f = v01854__013d.reshape((1,))

# op _017A_power_combination_eval
# LANG: _017n, _017z --> _017B
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01986__017B = (v01985__017n**1)*(v01992__017z**1)
v01986__017B = (v01986__017B*_017A_coeff).reshape((1, 2))

# op _017i_power_combination_eval
# LANG: _016Z, _017h --> _017j
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01975__017j = (v01959__016Z**1)*(v01979__017h**1)
v01975__017j = (v01975__017j*_017i_coeff).reshape((1, 2))

# op _00KU_power_combination_eval
# LANG: _00KT --> _00KV
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01272__00KV = (v01271__00KT**1)
v01272__00KV = (v01272__00KV*_00KU_coeff).reshape((1, 40, 100))

# op _00R3 expand_scalar_eval
# LANG: _00R2 --> _00R4
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01457__00R4 = np.empty((1, 2))
v01457__00R4.fill(v01456__00R2.item())

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
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0782__00sj = (v0781__00sh**1)
v0782__00sj = (v0782__00sj*_00si_coeff).reshape((1, 2, 3))

# op _00tE_power_combination_eval
# LANG: _00tC --> _00tF
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0818__00tF = (v0817__00tC**4)
v0818__00tF = (v0818__00tF*_00tE_coeff).reshape((1, 1))

# op _00tY_power_combination_eval
# LANG: _00tL, _00tX --> _00tZ
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0823__00tZ = (v0822__00tL**1)*(v0829__00tX**1)
v0823__00tZ = (v0823__00tZ*_00tY_coeff).reshape((1, 1))

# op _00u1_linear_combination_eval
# LANG: _00u0 --> _00u2
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0832__00u2 = _00u1_constant+1*v0831__00u0

# op _00xC_sin_eval
# LANG: _00xB --> _00xD
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0940__00xD = np.sin(v0939__00xB)

# op _00xE_power_combination_eval
# LANG: _00wN --> _00xF
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0943__00xF = (v0942__00wN**1)
v0943__00xF = (v0943__00xF*_00xE_coeff).reshape((1, 2))

# op _00xo_power_combination_eval
# LANG: _00xj, _00xn --> _00xp
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0926__00xp = (v0925__00xj**1)*(v0932__00xn**1)
v0926__00xp = (v0926__00xp*_00xo_coeff).reshape((1, 2))

# op _0119_power_combination_eval
# LANG: _0118 --> rotor_disk_tonal_spl
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.ks_spl_model
v01798_rotor_disk_tonal_spl = (v01797__0118**1)
v01798_rotor_disk_tonal_spl = (v01798_rotor_disk_tonal_spl*_0119_coeff).reshape((1, 2))

# op _013g expand_scalar_eval
# LANG: _013f --> _013h
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01859__013h = np.empty((1, 2))
v01859__013h.fill(v01858__013f.item())

# op _017C_linear_combination_eval
# LANG: _017j, _017B --> rotor_disk_broadband_spl
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.gl_spl_model
v01980_rotor_disk_broadband_spl = _017C_constant+1*v01975__017j+-1*v01986__017B

# op _00KW_power_combination_eval
# LANG: _00IN, _00KV --> _00KX
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01273__00KX = (v01272__00KV**1)*(v01249__00IN**1)
v01273__00KX = (v01273__00KX*_00KW_coeff).reshape((1, 40, 100))

# op _00R5_linear_combination_eval
# LANG: _00R4, rotor_disk_tonal_spl --> _00R6
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01431__00R6 = _00R5_constant+1*v01798_rotor_disk_tonal_spl+1*v01457__00R4

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
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0783__00sl = (v0782__00sj**1)
v0783__00sl = (v0783__00sl*_00sk_coeff).reshape((1, 2, 3))

# op _00tG_power_combination_eval
# LANG: _00tF --> _00tH
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0819__00tH = (v0818__00tF**1)
v0819__00tH = (v0819__00tH*_00tG_coeff).reshape((1, 1))

# op _00u3_power_combination_eval
# LANG: _00tZ, _00u2 --> _00u4
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0830__00u4 = (v0823__00tZ**1)*(v0832__00u2**1)
v0830__00u4 = (v0830__00u4*_00u3_coeff).reshape((1, 1))

# op _00xG_power_combination_eval
# LANG: _00xD, _00xF --> _00xH
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0941__00xH = (v0940__00xD**1)*(v0943__00xF**-1)
v0941__00xH = (v0941__00xH*_00xG_coeff).reshape((1, 2))

# op _00xq_linear_combination_eval
# LANG: _00xp --> _00xr
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0933__00xr = _00xq_constant+1*v0926__00xp

# op _013i_linear_combination_eval
# LANG: _013h, rotor_disk_broadband_spl --> _013j
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01833__013j = _013i_constant+1*v01980_rotor_disk_broadband_spl+1*v01859__013h

# op _00KY_power_combination_eval
# LANG: _ux, _00KX --> _00KZ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01274__00KZ = (v01273__00KX**1)*(v01208__ux**1)
v01274__00KZ = (v01274__00KZ*_00KY_coeff).reshape((1, 40, 100))

# op _00R7_power_combination_eval
# LANG: _00R6 --> _00R8
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01458__00R8 = (v01431__00R6**1)
v01458__00R8 = (v01458__00R8*_00R7_coeff).reshape((1, 2))

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
# SHAPES: (1, 2, 3) --> (1, 2, 3)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0784__00sn = _00sm_exp_a_eval_a**v0783__00sl

# op _00u5_power_combination_eval
# LANG: _00tH, _00u4 --> _00u6
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0820__00u6 = (v0819__00tH**1)*(v0830__00u4**-1)
v0820__00u6 = (v0820__00u6*_00u5_coeff).reshape((1, 1))

# op _00xI_linear_combination_eval
# LANG: _00xH --> _00xJ
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0944__00xJ = _00xI_constant+1*v0941__00xH

# op _00xs_log10_eval
# LANG: _00xr --> _00xt
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0934__00xt = np.log10(v0933__00xr)

# op _013k_power_combination_eval
# LANG: _013j --> _013l
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01860__013l = (v01833__013j**1)
v01860__013l = (v01860__013l*_013k_coeff).reshape((1, 2))

# op _00K__power_combination_eval
# LANG: _ut, _00KZ --> _00L0
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01275__00L0 = (v01274__00KZ**1)*(v01240__ut**1)
v01275__00L0 = (v01275__00L0*_00K__coeff).reshape((1, 40, 100))

# op _00Lz_power_combination_eval
# LANG: _ut --> _00LA
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01343__00LA = (v01240__ut**1)
v01343__00LA = (v01343__00LA*_00Lz_coeff).reshape((1, 40, 100))

# op _00R9_exp_a_eval
# LANG: _00R8 --> _00Ra
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01459__00Ra = _00R9_exp_a_eval_a**v01458__00R8

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
# SHAPES: (1, 2, 3) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0785__00sp = np.sum(v0784__00sn, axis = (2,)).reshape((1, 2))

# op _00u7_log10_eval
# LANG: _00u6 --> _00u8
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0833__00u8 = np.log10(v0820__00u6)

# op _00ub_log10_eval
# LANG: RA_1000 --> _00uc
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0837__00uc = np.log10(v0836_RA_1000)

# op _00xK_log10_eval
# LANG: _00xJ --> _00xL
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0945__00xL = np.log10(v0944__00xJ)

# op _00xu_power_combination_eval
# LANG: _00xt --> _00xv
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0935__00xv = (v0934__00xt**1)
v0935__00xv = (v0935__00xv*_00xu_coeff).reshape((1, 2))

# op _013m_exp_a_eval
# LANG: _013l --> _013n
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01861__013n = _013m_exp_a_eval_a**v01860__013l

# op _00L1_power_combination_eval
# LANG: _00L0, prandtl_loss_factor --> _00L2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01276__00L2 = (v01275__00L0**1)*(v01193_prandtl_loss_factor**1)
v01276__00L2 = (v01276__00L2*_00L1_coeff).reshape((1, 40, 100))

# op _00LB_linear_combination_eval
# LANG: _00LA, _tangential_inflow_velocity --> _00LC
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01342__00LC = _00LB_constant+1*v01160__tangential_inflow_velocity+-1*v01343__00LA

# op _00Ld_power_combination_eval
# LANG: _ut --> _00Le
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01296__00Le = (v01240__ut**1)
v01296__00Le = (v01296__00Le*_00Ld_coeff).reshape((1, 40, 100))

# op _00Lr_power_combination_eval
# LANG: _00Ja --> _00Ls
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01336__00Ls = (v01218__00Ja**1)
v01336__00Ls = (v01336__00Ls*_00Lr_coeff).reshape((1, 40, 100))

# op _00Rb_log10_eval
# LANG: _00Ra --> _00Rc
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01460__00Rc = np.log10(v01459__00Ra)

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
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0786__00sr = np.log10(v0785__00sp)

# op _00u9_power_combination_eval
# LANG: _00u8 --> _00ua
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0834__00ua = (v0833__00u8**1)
v0834__00ua = (v0834__00ua*_00u9_coeff).reshape((1, 1))

# op _00ud_power_combination_eval
# LANG: _00uc --> _00ue
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0838__00ue = (v0837__00uc**1)
v0838__00ue = (v0838__00ue*_00ud_coeff).reshape((1, 1))

# op _00xM_power_combination_eval
# LANG: _00xL --> _00xN
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0946__00xN = (v0945__00xL**1)
v0946__00xN = (v0946__00xN*_00xM_coeff).reshape((1, 2))

# op _00xw_linear_combination_eval
# LANG: _00xv --> _00xx
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0936__00xx = _00xw_constant+1*v0935__00xv

# op _00yH_power_combination_eval
# LANG: hover_altitude --> _00yI
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01008__00yI = (v0974_hover_altitude**5)
v01008__00yI = (v01008__00yI*_00yH_coeff).reshape((1,))

# op _00yT_power_combination_eval
# LANG: hover_altitude --> _00yU
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01010__00yU = (v0974_hover_altitude**4)
v01010__00yU = (v01010__00yU*_00yT_coeff).reshape((1,))

# op _00yu_power_combination_eval
# LANG: hover_altitude --> _00yv
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01005__00yv = (v0974_hover_altitude**6)
v01005__00yv = (v01005__00yv*_00yu_coeff).reshape((1,))

# op _00z4_power_combination_eval
# LANG: hover_altitude --> _00z5
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01012__00z5 = (v0974_hover_altitude**3)
v01012__00z5 = (v01012__00z5*_00z4_coeff).reshape((1,))

# op _00zE_power_combination_eval
# LANG: hover_altitude --> _00zF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01018__00zF = (v0974_hover_altitude**0)
v01018__00zF = (v01018__00zF*_00zE_coeff).reshape((1,))

# op _00zg_power_combination_eval
# LANG: hover_altitude --> _00zh
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01014__00zh = (v0974_hover_altitude**2)
v01014__00zh = (v01014__00zh*_00zg_coeff).reshape((1,))

# op _00zs_power_combination_eval
# LANG: hover_altitude --> _00zt
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01016__00zt = (v0974_hover_altitude**1)
v01016__00zt = (v01016__00zt*_00zs_coeff).reshape((1,))

# op _013o_log10_eval
# LANG: _013n --> _013p
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01862__013p = np.log10(v01861__013n)

# op _00Jb_cos_eval
# LANG: phi_distribution --> _00Jc
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01257__00Jc = np.cos(v01180_phi_distribution)

# op _00Jf_sin_eval
# LANG: phi_distribution --> _00Jg
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01324__00Jg = np.sin(v01180_phi_distribution)

# op _00L3_power_combination_eval
# LANG: _00L2, _dr --> _local_torque
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01277__local_torque = (v01276__00L2**1)*(v01131__dr**1)
v01277__local_torque = (v01277__local_torque*_00L3_coeff).reshape((1, 40, 100))

# op _00L5_power_combination_eval
# LANG: _00J0 --> _00L6
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01289__00L6 = (v01225__00J0**1)
v01289__00L6 = (v01289__00L6*_00L5_coeff).reshape((1, 40, 100))

# op _00LD_power_combination_eval
# LANG: _00LC --> _00LE
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01344__00LE = (v01342__00LC**2)
v01344__00LE = (v01344__00LE*_00LD_coeff).reshape((1, 40, 100))

# op _00Lf_linear_combination_eval
# LANG: _00Le, _tangential_inflow_velocity --> _00Lg
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01295__00Lg = _00Lf_constant+1*v01160__tangential_inflow_velocity+-1*v01296__00Le

# op _00Lt_power_combination_eval
# LANG: _00Ls --> _00Lu
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01337__00Lu = (v01336__00Ls**1)
v01337__00Lu = (v01337__00Lu*_00Lt_coeff).reshape((1, 40, 100))

# op _00Lx_power_combination_eval
# LANG: _ux_2 --> _00Ly
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01340__00Ly = (v01221__ux_2**2)
v01340__00Ly = (v01340__00Ly*_00Lx_coeff).reshape((1, 40, 100))

# op _00N9_power_combination_eval
# LANG: _ut --> _00Na
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01316__00Na = (v01240__ut**1)
v01316__00Na = (v01316__00Na*_00N9_coeff).reshape((1, 40, 100))

# op _00NF_power_combination_eval
# LANG: _axial_inflow_velocity --> _00NG
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01360__00NG = (v01150__axial_inflow_velocity**2)
v01360__00NG = (v01360__00NG*_00NF_coeff).reshape((1, 40, 100))

# op _00Nt_power_combination_eval
# LANG: _ux, _tangential_inflow_velocity --> _00Nu
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01353__00Nu = (v01160__tangential_inflow_velocity**1)*(v01208__ux**1)
v01353__00Nu = (v01353__00Nu*_00Nt_coeff).reshape((1, 40, 100))

# op _00Nx_power_combination_eval
# LANG: _axial_inflow_velocity --> _00Ny
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01356__00Ny = (v01150__axial_inflow_velocity**1)
v01356__00Ny = (v01356__00Ny*_00Nx_coeff).reshape((1, 40, 100))

# op _00Nz_power_combination_eval
# LANG: _ux --> _00NA
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01358__00NA = (v01208__ux**2)
v01358__00NA = (v01358__00NA*_00Nz_coeff).reshape((1, 40, 100))

# op _00Om_single_tensor_sum_with_axis_eval
# LANG: _00IF --> _00On
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01382__00On = np.sum(v01369__00IF, axis = (1, 2)).reshape((1,))

# op _00Ow_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00Ox
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01387__00Ox = np.sum(v01130__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00Rd_power_combination_eval
# LANG: _00Rc --> rotor_disk_tonal_spl_A_weighted
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model
v01461_rotor_disk_tonal_spl_A_weighted = (v01460__00Rc**1)
v01461_rotor_disk_tonal_spl_A_weighted = (v01461_rotor_disk_tonal_spl_A_weighted*_00Rd_coeff).reshape((1, 2))

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
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.lowson_spl_model
v0787_rotor_disk_tonal_spl = (v0786__00sr**1)
v0787_rotor_disk_tonal_spl = (v0787_rotor_disk_tonal_spl*_00ss_coeff).reshape((1, 2))

# op _00uf_linear_combination_eval
# LANG: _00ua, _00ue --> _00ug
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0835__00ug = _00uf_constant+1*v0834__00ua+-1*v0838__00ue

# op _00xO_linear_combination_eval
# LANG: _00xx, _00xN --> rotor_disk_broadband_spl
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.skm_spl_model
v0937_rotor_disk_broadband_spl = _00xO_constant+1*v0936__00xx+1*v0946__00xN

# op _00yJ_power_combination_eval
# LANG: _00yI --> _00yK
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01009__00yK = (v01008__00yI**1)
v01009__00yK = (v01009__00yK*_00yJ_coeff).reshape((1,))

# op _00yV_power_combination_eval
# LANG: _00yU --> _00yW
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01011__00yW = (v01010__00yU**1)
v01011__00yW = (v01011__00yW*_00yV_coeff).reshape((1,))

# op _00yw_power_combination_eval
# LANG: _00yv --> _00yx
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01006__00yx = (v01005__00yv**1)
v01006__00yx = (v01006__00yx*_00yw_coeff).reshape((1,))

# op _00z6_power_combination_eval
# LANG: _00z5 --> _00z7
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01013__00z7 = (v01012__00z5**1)
v01013__00z7 = (v01013__00z7*_00z6_coeff).reshape((1,))

# op _00zG_power_combination_eval
# LANG: _00zF --> _00zH
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01019__00zH = (v01018__00zF**1)
v01019__00zH = (v01019__00zH*_00zG_coeff).reshape((1,))

# op _00zi_power_combination_eval
# LANG: _00zh --> _00zj
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01015__00zj = (v01014__00zh**1)
v01015__00zj = (v01015__00zj*_00zi_coeff).reshape((1,))

# op _00zu_power_combination_eval
# LANG: _00zt --> _00zv
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01017__00zv = (v01016__00zt**1)
v01017__00zv = (v01017__00zv*_00zu_coeff).reshape((1,))

# op _013q_power_combination_eval
# LANG: _013p --> rotor_disk_broadband_spl_A_weighted
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model
v01863_rotor_disk_broadband_spl_A_weighted = (v01862__013p**1)
v01863_rotor_disk_broadband_spl_A_weighted = (v01863_rotor_disk_broadband_spl_A_weighted*_013q_coeff).reshape((1, 2))

# op _00Jd_power_combination_eval
# LANG: _00Jc, Cl --> _00Je
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01256__00Je = (v01182_Cl**1)*(v01257__00Jc**1)
v01256__00Je = (v01256__00Je*_00Jd_coeff).reshape((1, 40, 100))

# op _00Jh_power_combination_eval
# LANG: _00Jg, Cl --> _00Ji
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01323__00Ji = (v01182_Cl**1)*(v01324__00Jg**1)
v01323__00Ji = (v01323__00Ji*_00Jh_coeff).reshape((1, 40, 100))

# op _00L7_power_combination_eval
# LANG: _00L6 --> _00L8
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01290__00L8 = (v01289__00L6**1)
v01290__00L8 = (v01290__00L8*_00L7_coeff).reshape((1, 40, 100))

# op _00LF_linear_combination_eval
# LANG: _00Ly, _00LE --> _00LG
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01341__00LG = _00LF_constant+1*v01340__00Ly+1*v01344__00LE

# op _00Lb_power_combination_eval
# LANG: _ux_2 --> _00Lc
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01293__00Lc = (v01221__ux_2**2)
v01293__00Lc = (v01293__00Lc*_00Lb_coeff).reshape((1, 40, 100))

# op _00Lh_power_combination_eval
# LANG: _00Lg --> _00Li
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01297__00Li = (v01295__00Lg**2)
v01297__00Li = (v01297__00Li*_00Lh_coeff).reshape((1, 40, 100))

# op _00Lv_power_combination_eval
# LANG: _00IN, _00Lu --> _00Lw
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01338__00Lw = (v01337__00Lu**1)*(v01249__00IN**1)
v01338__00Lw = (v01338__00Lw*_00Lv_coeff).reshape((1, 40, 100))

# op _00ME_power_combination_eval
# LANG: _ut --> _00MF
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01332__00MF = (v01240__ut**1)
v01332__00MF = (v01332__00MF*_00ME_coeff).reshape((1, 40, 100))

# op _00Mi_power_combination_eval
# LANG: _ut --> _00Mj
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01265__00Mj = (v01240__ut**1)
v01265__00Mj = (v01265__00Mj*_00Mi_coeff).reshape((1, 40, 100))

# op _00N3_single_tensor_sum_with_axis_eval
# LANG: _local_torque --> _00N4
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01278__00N4 = np.sum(v01277__local_torque, axis = (1, 2)).reshape((1,))

# op _00N7_power_combination_eval
# LANG: _00IN --> _00N8
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01313__00N8 = (v01249__00IN**1)
v01313__00N8 = (v01313__00N8*_00N7_coeff).reshape((1, 40, 100))

# op _00NB_power_combination_eval
# LANG: _00Ny, _00NA --> _00NC
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01357__00NC = (v01356__00Ny**1)*(v01358__00NA**1)
v01357__00NC = (v01357__00NC*_00NB_coeff).reshape((1, 40, 100))

# op _00NH_power_combination_eval
# LANG: _00NG --> _00NI
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01361__00NI = (v01360__00NG**1)
v01361__00NI = (v01361__00NI*_00NH_coeff).reshape((1, 40, 100))

# op _00Nb_linear_combination_eval
# LANG: _00Na, _tangential_inflow_velocity --> _00Nc
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01315__00Nc = _00Nb_constant+1*v01160__tangential_inflow_velocity+-1*v01316__00Na

# op _00Nv_power_combination_eval
# LANG: _ut, _00Nu --> _00Nw
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01354__00Nw = (v01353__00Nu**1)*(v01240__ut**1)
v01354__00Nw = (v01354__00Nw*_00Nv_coeff).reshape((1, 40, 100))

# op _00OK_power_combination_eval
# LANG: _00IF, _axial_inflow_velocity --> _00OL
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01394__00OL = (v01150__axial_inflow_velocity**1)*(v01369__00IF**-1)
v01394__00OL = (v01394__00OL*_00OK_coeff).reshape((1, 40, 100))

# op _00OM_power_combination_eval
# LANG: _rotor_radius --> _00ON
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01396__00ON = (v01130__rotor_radius**1)
v01396__00ON = (v01396__00ON*_00OM_coeff).reshape((1, 40, 100))

# op _00Oo_power_combination_eval
# LANG: _00On --> _00Op
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01383__00Op = (v01382__00On**1)
v01383__00Op = (v01383__00Op*_00Oo_coeff).reshape((1,))

# op _00Oy_power_combination_eval
# LANG: _00Ox --> _00Oz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01388__00Oz = (v01387__00Ox**1)
v01388__00Oz = (v01388__00Oz*_00Oy_coeff).reshape((1,))

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

# op _00uh reshape_eval
# LANG: _00ug --> _00ui
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0839__00ui = v0835__00ug.reshape((1,))

# op _00xT expand_array_eval
# LANG: rotor_disk_tonal_spl --> _00xU
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0947__00xU = np.einsum('bc,a->abc', v0787_rotor_disk_tonal_spl.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00xX expand_array_eval
# LANG: rotor_disk_broadband_spl --> _00xY
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0949__00xY = np.einsum('bc,a->abc', v0937_rotor_disk_broadband_spl.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00yy_indexed_passthrough_eval
# LANG: _00yx, _00yK, _00yW, _00z7, _00zj, _00zv, _00zH --> temp_temperature
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01007_temp_temperature__temp[i_v01006__00yx__00yy_indexed_passthrough_eval] = v01006__00yx.flatten()
v01007_temp_temperature = v01007_temp_temperature__temp.copy()
v01007_temp_temperature__temp[i_v01009__00yK__00yy_indexed_passthrough_eval] = v01009__00yK.flatten()
v01007_temp_temperature = v01007_temp_temperature__temp.copy()
v01007_temp_temperature__temp[i_v01011__00yW__00yy_indexed_passthrough_eval] = v01011__00yW.flatten()
v01007_temp_temperature = v01007_temp_temperature__temp.copy()
v01007_temp_temperature__temp[i_v01013__00z7__00yy_indexed_passthrough_eval] = v01013__00z7.flatten()
v01007_temp_temperature = v01007_temp_temperature__temp.copy()
v01007_temp_temperature__temp[i_v01015__00zj__00yy_indexed_passthrough_eval] = v01015__00zj.flatten()
v01007_temp_temperature = v01007_temp_temperature__temp.copy()
v01007_temp_temperature__temp[i_v01017__00zv__00yy_indexed_passthrough_eval] = v01017__00zv.flatten()
v01007_temp_temperature = v01007_temp_temperature__temp.copy()
v01007_temp_temperature__temp[i_v01019__00zH__00yy_indexed_passthrough_eval] = v01019__00zH.flatten()
v01007_temp_temperature = v01007_temp_temperature__temp.copy()

# op _017H expand_array_eval
# LANG: rotor_disk_tonal_spl --> _017I
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01993__017I = np.einsum('bc,a->abc', v01798_rotor_disk_tonal_spl.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _017L expand_array_eval
# LANG: rotor_disk_broadband_spl --> _017M
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01995__017M = np.einsum('bc,a->abc', v01980_rotor_disk_broadband_spl.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _017Z expand_array_eval
# LANG: rotor_disk_tonal_spl_A_weighted --> _017_
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02001__017_ = np.einsum('bc,a->abc', v01461_rotor_disk_tonal_spl_A_weighted.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _0182 expand_array_eval
# LANG: rotor_disk_broadband_spl_A_weighted --> _0183
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02003__0183 = np.einsum('bc,a->abc', v01863_rotor_disk_broadband_spl_A_weighted.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _005e_decompose_eval
# LANG: T --> _005f
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_bem_model
v0149__005f = ((v0344_T.flatten())[src_indices__005f__005e]).reshape((1,))

# op _00Cs_decompose_eval
# LANG: T --> _00Ct
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01075__00Ct = ((v01270_T.flatten())[src_indices__00Ct__00Cs]).reshape((1,))

# op _00L9_power_combination_eval
# LANG: _00IN, _00L8 --> _00La
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01291__00La = (v01290__00L8**1)*(v01249__00IN**1)
v01291__00La = (v01291__00La*_00L9_coeff).reshape((1, 40, 100))

# op _00LH_power_combination_eval
# LANG: _00Lw, _00LG --> _00LI
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01339__00LI = (v01338__00Lw**1)*(v01341__00LG**1)
v01339__00LI = (v01339__00LI*_00LH_coeff).reshape((1, 40, 100))

# op _00Lj_linear_combination_eval
# LANG: _00Lc, _00Li --> _00Lk
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01294__00Lk = _00Lj_constant+1*v01293__00Lc+1*v01297__00Li

# op _00MG_linear_combination_eval
# LANG: _00MF, _tangential_inflow_velocity --> _00MH
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01331__00MH = _00MG_constant+1*v01160__tangential_inflow_velocity+-1*v01332__00MF

# op _00Ma_power_combination_eval
# LANG: _00Je --> _00Mb
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01258__00Mb = (v01256__00Je**1)
v01258__00Mb = (v01258__00Mb*_00Ma_coeff).reshape((1, 40, 100))

# op _00Mk_linear_combination_eval
# LANG: _00Mj, _tangential_inflow_velocity --> _00Ml
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01264__00Ml = _00Mk_constant+1*v01160__tangential_inflow_velocity+-1*v01265__00Mj

# op _00Mw_power_combination_eval
# LANG: _00Ji --> _00Mx
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01325__00Mx = (v01323__00Ji**1)
v01325__00Mx = (v01325__00Mx*_00Mw_coeff).reshape((1, 40, 100))

# op _00N5_power_combination_eval
# LANG: _00N4 --> total_torque
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01279_total_torque = (v01278__00N4**1)
v01279_total_torque = (v01279_total_torque*_00N5_coeff).reshape((1,))

# op _00ND_linear_combination_eval
# LANG: _00Nw, _00NC --> _00NE
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01355__00NE = _00ND_constant+1*v01354__00Nw+-1*v01357__00NC

# op _00NJ_power_combination_eval
# LANG: _ux, _00NI --> _00NK
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01362__00NK = (v01361__00NI**1)*(v01208__ux**1)
v01362__00NK = (v01362__00NK*_00NJ_coeff).reshape((1, 40, 100))

# op _00Nd_power_combination_eval
# LANG: _00N8, _00Nc --> _00Ne
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01314__00Ne = (v01313__00N8**1)*(v01315__00Nc**1)
v01314__00Ne = (v01314__00Ne*_00Nd_coeff).reshape((1, 40, 100))

# op _00Np_power_combination_eval
# LANG: _radius --> _00Nq
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01350__00Nq = (v01143__radius**1)
v01350__00Nq = (v01350__00Nq*_00Np_coeff).reshape((1, 40, 100))

# op _00OA_power_combination_eval
# LANG: _00Oz --> _00OB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01389__00OB = (v01388__00Oz**1)
v01389__00OB = (v01389__00OB*_00OA_coeff).reshape((1,))

# op _00OO_power_combination_eval
# LANG: _00OL, _00ON --> _00OP
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01395__00OP = (v01394__00OL**1)*(v01396__00ON**-1)
v01395__00OP = (v01395__00OP*_00OO_coeff).reshape((1, 40, 100))

# op _00Oq_power_combination_eval
# LANG: _00Op --> _00Or
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01384__00Or = (v01383__00Op**1)
v01384__00Or = (v01384__00Or*_00Oq_coeff).reshape((1,))

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
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model
v0533__00k0 = np.empty((1, 2))
v0533__00k0.fill(v0532__00jZ.item())

# op _00m6 expand_array_eval
# LANG: thrust_dir --> _00m7
# SHAPES: (3,) --> (1, 3, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0603__00m7 = np.einsum('b,ac->abc', v0494_thrust_dir.reshape((3,)) ,np.ones((1, 2))).reshape((1, 3, 2))

# op _00uj expand_scalar_eval
# LANG: _00ui --> _00uk
# SHAPES: (1,) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0840__00uk = np.empty((1, 2))
v0840__00uk.fill(v0839__00ui.item())

# op _00xV_indexed_passthrough_eval
# LANG: _00xU, _00xY --> noise_components
# SHAPES: (1, 1, 2), (1, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0948_noise_components__temp[i_v0947__00xU__00xV_indexed_passthrough_eval] = v0947__00xU.flatten()
v0948_noise_components = v0948_noise_components__temp.copy()
v0948_noise_components__temp[i_v0949__00xY__00xV_indexed_passthrough_eval] = v0949__00xY.flatten()
v0948_noise_components = v0948_noise_components__temp.copy()

# op _00zM single_tensor_sum_no_axis_eval
# LANG: temp_temperature --> hover_temperature
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01020_hover_temperature = np.sum(v01007_temp_temperature).reshape((1,))

# op _017J_indexed_passthrough_eval
# LANG: _017I, _017M --> noise_components
# SHAPES: (1, 1, 2), (1, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01994_noise_components__temp[i_v01993__017I__017J_indexed_passthrough_eval] = v01993__017I.flatten()
v01994_noise_components = v01994_noise_components__temp.copy()
v01994_noise_components__temp[i_v01995__017M__017J_indexed_passthrough_eval] = v01995__017M.flatten()
v01994_noise_components = v01994_noise_components__temp.copy()

# op _0180_indexed_passthrough_eval
# LANG: _017_, _0183 --> A_weighted_noise_components
# SHAPES: (1, 1, 2), (1, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02002_A_weighted_noise_components__temp[i_v02001__017___0180_indexed_passthrough_eval] = v02001__017_.flatten()
v02002_A_weighted_noise_components = v02002_A_weighted_noise_components__temp.copy()
v02002_A_weighted_noise_components__temp[i_v02003__0183__0180_indexed_passthrough_eval] = v02003__0183.flatten()
v02002_A_weighted_noise_components = v02002_A_weighted_noise_components__temp.copy()

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

# op _00Br_power_combination_eval
# LANG: rotor_disk_origin --> _00Bs
# SHAPES: (3,) --> (3,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((3,))
v01060__00Bs = (v012_rotor_disk_origin**1)
v01060__00Bs = (v01060__00Bs*_00Br_coeff).reshape((3,))
v012_rotor_disk_origin = v012_rotor_disk_origin.reshape((1, 3))

# op _00CB reshape_eval
# LANG: _00Ct --> _00CC
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01082__00CC = v01075__00Ct.reshape((1, 1))

# op _00CG reshape_eval
# LANG: _00Ct --> _00CH
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01084__00CH = v01075__00Ct.reshape((1, 1))

# op _00Cu reshape_eval
# LANG: _00Ct --> _00Cv
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01076__00Cv = v01075__00Ct.reshape((1, 1))

# op _00Cw_decompose_eval
# LANG: thrust_vector --> _00Cx, _00CD, _00CI
# SHAPES: (1, 3) --> (1, 1), (1, 1), (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01078__00Cx = ((v01059_thrust_vector.flatten())[src_indices__00Cx__00Cw]).reshape((1, 1))
v01079__00CD = ((v01059_thrust_vector.flatten())[src_indices__00CD__00Cw]).reshape((1, 1))
v01080__00CI = ((v01059_thrust_vector.flatten())[src_indices__00CI__00Cw]).reshape((1, 1))

# op _00FX_power_combination_eval
# LANG: temperature --> _00FY
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01178__00FY = (v01166_temperature**1)
v01178__00FY = (v01178__00FY*_00FX_coeff).reshape((1, 1))

# op _00KE_power_combination_eval
# LANG: _angular_speed --> _00KF
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01283__00KF = (v01142__angular_speed**1)
v01283__00KF = (v01283__00KF*_00KE_coeff).reshape((1, 40, 100))

# op _00LJ_power_combination_eval
# LANG: _00LI, _chord --> _00LK
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01345__00LK = (v01339__00LI**1)*(v01138__chord**1)
v01345__00LK = (v01345__00LK*_00LJ_coeff).reshape((1, 40, 100))

# op _00Ll_power_combination_eval
# LANG: _00La, _00Lk --> _00Lm
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01292__00Lm = (v01291__00La**1)*(v01294__00Lk**1)
v01292__00Lm = (v01292__00Lm*_00Ll_coeff).reshape((1, 40, 100))

# op _00MC_power_combination_eval
# LANG: _ux_2 --> _00MD
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01329__00MD = (v01221__ux_2**2)
v01329__00MD = (v01329__00MD*_00MC_coeff).reshape((1, 40, 100))

# op _00MI_power_combination_eval
# LANG: _00MH --> _00MJ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01333__00MJ = (v01331__00MH**2)
v01333__00MJ = (v01333__00MJ*_00MI_coeff).reshape((1, 40, 100))

# op _00Mc_power_combination_eval
# LANG: _00Mb --> _00Md
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01259__00Md = (v01258__00Mb**1)
v01259__00Md = (v01259__00Md*_00Mc_coeff).reshape((1, 40, 100))

# op _00Mg_power_combination_eval
# LANG: _ux_2 --> _00Mh
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01262__00Mh = (v01221__ux_2**2)
v01262__00Mh = (v01262__00Mh*_00Mg_coeff).reshape((1, 40, 100))

# op _00Mm_power_combination_eval
# LANG: _00Ml --> _00Mn
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01266__00Mn = (v01264__00Ml**2)
v01266__00Mn = (v01266__00Mn*_00Mm_coeff).reshape((1, 40, 100))

# op _00My_power_combination_eval
# LANG: _00Mx --> _00Mz
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01326__00Mz = (v01325__00Mx**1)
v01326__00Mz = (v01326__00Mz*_00My_coeff).reshape((1, 40, 100))

# op _00NL_linear_combination_eval
# LANG: _00NE, _00NK --> _00NM
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01359__00NM = _00NL_constant+1*v01355__00NE+1*v01362__00NK

# op _00Nf_power_combination_eval
# LANG: _ut, _00Ne --> _00Ng
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01317__00Ng = (v01314__00Ne**1)*(v01240__ut**1)
v01317__00Ng = (v01317__00Ng*_00Nf_coeff).reshape((1, 40, 100))

# op _00Nr_power_combination_eval
# LANG: _00Nq --> _00Ns
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01351__00Ns = (v01350__00Nq**1)
v01351__00Ns = (v01351__00Ns*_00Nr_coeff).reshape((1, 40, 100))

# op _00OC_power_combination_eval
# LANG: _00OB --> _00OD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01390__00OD = (v01389__00OB**1)
v01390__00OD = (v01390__00OD*_00OC_coeff).reshape((1,))

# op _00OQ_single_tensor_sum_with_axis_eval
# LANG: _00OP --> _00OR
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01397__00OR = np.sum(v01395__00OP, axis = (1, 2)).reshape((1,))

# op _00Ok_power_combination_eval
# LANG: total_torque, density --> _00Ol
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01171_density = v01171_density.reshape((1,))
v01380__00Ol = (v01279_total_torque**1)*(v01171_density**-1)
v01380__00Ol = (v01380__00Ol*_00Ok_coeff).reshape((1,))
v01171_density = v01171_density.reshape((1, 1))

# op _00Os_power_combination_eval
# LANG: _00Or --> _00Ot
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01385__00Ot = (v01384__00Or**2)
v01385__00Ot = (v01385__00Ot*_00Os_coeff).reshape((1,))

# op _00Ry_power_combination_eval
# LANG: temperature --> _00Rz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01471__00Rz = (v01465_temperature**1)
v01471__00Rz = (v01471__00Rz*_00Ry_coeff).reshape((1,))

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
# SHAPES: (1, 2), (1, 2) --> (1, 2)
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
# SHAPES: (1, 3, 2), (1, 3, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_Lowson_tonal_model.observer_location_model
v0602_normal_proj = np.sum(v0595_rel_obs_position * v0603__00m7, axis=1)

# op _00ul_linear_combination_eval
# LANG: _00uk, rotor_disk_broadband_spl --> _00um
# SHAPES: (1, 2), (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0814__00um = _00ul_constant+1*v0937_rotor_disk_broadband_spl+1*v0840__00uk

# op _00xZ_power_combination_eval
# LANG: noise_components --> _00x_
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0950__00x_ = (v0948_noise_components**1)
v0950__00x_ = (v0950__00x_*_00xZ_coeff).reshape((2, 1, 2))

# op _00zO_power_combination_eval
# LANG: hover_temperature --> _00zP
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01023__00zP = (v01020_hover_temperature**1)
v01023__00zP = (v01023__00zP*_00zO_coeff).reshape((1,))

# op _017N_power_combination_eval
# LANG: noise_components --> _017O
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01996__017O = (v01994_noise_components**1)
v01996__017O = (v01996__017O*_017N_coeff).reshape((2, 1, 2))

# op _0184_power_combination_eval
# LANG: A_weighted_noise_components --> _0185
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02004__0185 = (v02002_A_weighted_noise_components**1)
v02004__0185 = (v02004__0185*_0184_coeff).reshape((2, 1, 2))

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

# op _00BJ expand_array_eval
# LANG: _00Bs --> thrust_origin
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01061_thrust_origin = np.einsum('b,a->ab', v01060__00Bs.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

# op _00CE_power_combination_eval
# LANG: _00CD, _00CC --> _00CF
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01083__00CF = (v01082__00CC**1)*(v01079__00CD**1)
v01083__00CF = (v01083__00CF*_00CE_coeff).reshape((1, 1))

# op _00CJ_power_combination_eval
# LANG: _00CI, _00CH --> _00CK
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01085__00CK = (v01084__00CH**1)*(v01080__00CI**1)
v01085__00CK = (v01085__00CK*_00CJ_coeff).reshape((1, 1))

# op _00Cy_power_combination_eval
# LANG: _00Cv, _00Cx --> _00Cz
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01077__00Cz = (v01076__00Cv**1)*(v01078__00Cx**1)
v01077__00Cz = (v01077__00Cz*_00Cy_coeff).reshape((1, 1))

# op _00FZ_power_combination_eval
# LANG: _00FY --> speed_of_sound
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.atmosphere_model
v01179_speed_of_sound = (v01178__00FY**0.5)
v01179_speed_of_sound = (v01179_speed_of_sound*_00FZ_coeff).reshape((1, 1))

# op _00KG_power_combination_eval
# LANG: _00KF --> _00KH
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01284__00KH = (v01283__00KF**1)
v01284__00KH = (v01284__00KH*_00KG_coeff).reshape((1, 40, 100))

# op _00LL_power_combination_eval
# LANG: _00LK, _dr --> _00LM
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01346__00LM = (v01345__00LK**1)*(v01131__dr**1)
v01346__00LM = (v01346__00LM*_00LL_coeff).reshape((1, 40, 100))

# op _00Ln_power_combination_eval
# LANG: _00Lm, _chord --> _00Lo
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01298__00Lo = (v01292__00Lm**1)*(v01138__chord**1)
v01298__00Lo = (v01298__00Lo*_00Ln_coeff).reshape((1, 40, 100))

# op _00MA_power_combination_eval
# LANG: _00IN, _00Mz --> _00MB
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01327__00MB = (v01326__00Mz**1)*(v01249__00IN**1)
v01327__00MB = (v01327__00MB*_00MA_coeff).reshape((1, 40, 100))

# op _00MK_linear_combination_eval
# LANG: _00MD, _00MJ --> _00ML
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01330__00ML = _00MK_constant+1*v01329__00MD+1*v01333__00MJ

# op _00Me_power_combination_eval
# LANG: _00IN, _00Md --> _00Mf
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01260__00Mf = (v01259__00Md**1)*(v01249__00IN**1)
v01260__00Mf = (v01260__00Mf*_00Me_coeff).reshape((1, 40, 100))

# op _00Mo_linear_combination_eval
# LANG: _00Mh, _00Mn --> _00Mp
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01263__00Mp = _00Mo_constant+1*v01262__00Mh+1*v01266__00Mn

# op _00NN_power_combination_eval
# LANG: _00Ns, _00NM --> _00NO
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01352__00NO = (v01351__00Ns**1)*(v01359__00NM**1)
v01352__00NO = (v01352__00NO*_00NN_coeff).reshape((1, 40, 100))

# op _00Nh_power_combination_eval
# LANG: _00Ng, _radius --> _00Ni
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01318__00Ni = (v01317__00Ng**1)*(v01143__radius**1)
v01318__00Ni = (v01318__00Ni*_00Nh_coeff).reshape((1, 40, 100))

# op _00OE_power_combination_eval
# LANG: _00OD --> _00OF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01391__00OF = (v01390__00OD**5)
v01391__00OF = (v01391__00OF*_00OE_coeff).reshape((1,))

# op _00OS_power_combination_eval
# LANG: _00OR --> _00OT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01398__00OT = (v01397__00OR**1)
v01398__00OT = (v01398__00OT*_00OS_coeff).reshape((1,))

# op _00O__power_combination_eval
# LANG: C_T --> _00P0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01402__00P0 = (v01374_C_T**1)
v01402__00P0 = (v01402__00P0*_00O__coeff).reshape((1,))

# op _00Ou_power_combination_eval
# LANG: _00Ol, _00Ot --> _00Ov
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01381__00Ov = (v01380__00Ol**1)*(v01385__00Ot**-1)
v01381__00Ov = (v01381__00Ov*_00Ou_coeff).reshape((1,))

# op _00RA_power_combination_eval
# LANG: _00Rz --> _00RB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01472__00RB = (v01471__00Rz**1.5)
v01472__00RB = (v01472__00RB*_00RA_coeff).reshape((1,))

# op _00TG_linear_combination_eval
# LANG: rel_obs_z_pos --> _00TH
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01541__00TH = _00TG_constant+1*v01517_rel_obs_z_pos

# op _00Ti expand_array_eval
# LANG: normal_proj --> _00Tj
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01528__00Tj = np.einsum('ac,b->abc', v01526_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00Ty_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00Tz
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01536__00Tz = (v01517_rel_obs_z_pos**1)*(v01525_rel_obs_dist**-1)
v01536__00Tz = (v01536__00Tz*_00Ty_coeff).reshape((1, 1, 2))

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

# op _00un_power_combination_eval
# LANG: _00um --> _00uo
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0841__00uo = (v0814__00um**1)
v0841__00uo = (v0841__00uo*_00un_coeff).reshape((1, 2))

# op _00w5 expand_array_eval
# LANG: normal_proj --> _00w6
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0898__00w6 = np.einsum('ac,b->abc', v0892_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _00wf_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00wg
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0902__00wg = (v0883_rel_obs_z_pos**1)*(v0891_rel_obs_dist**-1)
v0902__00wg = (v0902__00wg*_00wf_coeff).reshape((1, 1, 2))

# op _00wn_linear_combination_eval
# LANG: rel_obs_z_pos --> _00wo
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0907__00wo = _00wn_constant+1*v0883_rel_obs_z_pos

# op _00y0_exp_a_eval
# LANG: _00x_ --> _00y1
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0951__00y1 = _00y0_exp_a_eval_a**v0950__00x_

# op _00yD_power_combination_eval
# LANG: hover_altitude --> _00yE
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0993__00yE = (v0974_hover_altitude**5)
v0993__00yE = (v0993__00yE*_00yD_coeff).reshape((1,))

# op _00yL_power_combination_eval
# LANG: hover_altitude --> _00yM
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0980__00yM = (v0974_hover_altitude**4)
v0980__00yM = (v0980__00yM*_00yL_coeff).reshape((1,))

# op _00yP_power_combination_eval
# LANG: hover_altitude --> _00yQ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0995__00yQ = (v0974_hover_altitude**4)
v0995__00yQ = (v0995__00yQ*_00yP_coeff).reshape((1,))

# op _00yX_power_combination_eval
# LANG: hover_altitude --> _00yY
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0982__00yY = (v0974_hover_altitude**3)
v0982__00yY = (v0982__00yY*_00yX_coeff).reshape((1,))

# op _00yk_power_combination_eval
# LANG: hover_altitude --> _00yl
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0975__00yl = (v0974_hover_altitude**6)
v0975__00yl = (v0975__00yl*_00yk_coeff).reshape((1,))

# op _00yp_power_combination_eval
# LANG: hover_altitude --> _00yq
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0990__00yq = (v0974_hover_altitude**6)
v0990__00yq = (v0990__00yq*_00yp_coeff).reshape((1,))

# op _00yz_power_combination_eval
# LANG: hover_altitude --> _00yA
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0978__00yA = (v0974_hover_altitude**5)
v0978__00yA = (v0978__00yA*_00yz_coeff).reshape((1,))

# op _00z0_power_combination_eval
# LANG: hover_altitude --> _00z1
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0997__00z1 = (v0974_hover_altitude**3)
v0997__00z1 = (v0997__00z1*_00z0_coeff).reshape((1,))

# op _00z8_power_combination_eval
# LANG: hover_altitude --> _00z9
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0984__00z9 = (v0974_hover_altitude**2)
v0984__00z9 = (v0984__00z9*_00z8_coeff).reshape((1,))

# op _00zA_power_combination_eval
# LANG: hover_altitude --> _00zB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01003__00zB = (v0974_hover_altitude**0)
v01003__00zB = (v01003__00zB*_00zA_coeff).reshape((1,))

# op _00zQ_power_combination_eval
# LANG: _00zP --> _00zR
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01024__00zR = (v01023__00zP**1.5)
v01024__00zR = (v01024__00zR*_00zQ_coeff).reshape((1,))

# op _00zc_power_combination_eval
# LANG: hover_altitude --> _00zd
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0999__00zd = (v0974_hover_altitude**2)
v0999__00zd = (v0999__00zd*_00zc_coeff).reshape((1,))

# op _00zk_power_combination_eval
# LANG: hover_altitude --> _00zl
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0986__00zl = (v0974_hover_altitude**1)
v0986__00zl = (v0986__00zl*_00zk_coeff).reshape((1,))

# op _00zo_power_combination_eval
# LANG: hover_altitude --> _00zp
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01001__00zp = (v0974_hover_altitude**1)
v01001__00zp = (v01001__00zp*_00zo_coeff).reshape((1,))

# op _00zw_power_combination_eval
# LANG: hover_altitude --> _00zx
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0988__00zx = (v0974_hover_altitude**0)
v0988__00zx = (v0988__00zx*_00zw_coeff).reshape((1,))

# op _0152 expand_array_eval
# LANG: normal_proj --> _0153
# SHAPES: (1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01917__0153 = np.einsum('ac,b->abc', v01911_normal_proj.reshape((1, 2)) ,np.ones((1,))).reshape((1, 1, 2))

# op _015c_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _015d
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01921__015d = (v01902_rel_obs_z_pos**1)*(v01910_rel_obs_dist**-1)
v01921__015d = (v01921__015d*_015c_coeff).reshape((1, 1, 2))

# op _015k_linear_combination_eval
# LANG: rel_obs_z_pos --> _015l
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01926__015l = _015k_constant+1*v01902_rel_obs_z_pos

# op _017P_exp_a_eval
# LANG: _017O --> _017Q
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01997__017Q = _017P_exp_a_eval_a**v01996__017O

# op _0186_exp_a_eval
# LANG: _0185 --> _0187
# SHAPES: (2, 1, 2) --> (2, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02005__0187 = _0186_exp_a_eval_a**v02004__0185

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

# op _00C6 expand_scalar_eval
# LANG: speed_of_sound --> _00C7
# SHAPES: (1,) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01179_speed_of_sound = v01179_speed_of_sound.reshape((1,))
v01072__00C7 = np.empty((1, 40, 100))
v01072__00C7.fill(v01179_speed_of_sound.item())
v01179_speed_of_sound = v01179_speed_of_sound.reshape((1, 1))

# op _00CA_indexed_passthrough_eval
# LANG: _00Cz, _00CF, _00CK --> F
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01081_F__temp[i_v01077__00Cz__00CA_indexed_passthrough_eval] = v01077__00Cz.flatten()
v01081_F = v01081_F__temp.copy()
v01081_F__temp[i_v01083__00CF__00CA_indexed_passthrough_eval] = v01083__00CF.flatten()
v01081_F = v01081_F__temp.copy()
v01081_F__temp[i_v01085__00CK__00CA_indexed_passthrough_eval] = v01085__00CK.flatten()
v01081_F = v01081_F__temp.copy()

# op _00CL_linear_combination_eval
# LANG: thrust_origin, reference_point --> _00CM
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01086__00CM = _00CL_constant+1*v01061_thrust_origin+-1*v01087_reference_point

# op _00KC_power_combination_eval
# LANG: _00IN, _local_thrust --> _00KD
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01281__00KD = (v01254__local_thrust**1)*(v01249__00IN**-1)
v01281__00KD = (v01281__00KD*_00KC_coeff).reshape((1, 40, 100))

# op _00KI_power_combination_eval
# LANG: _00KH --> _00KJ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01285__00KJ = (v01284__00KH**2)
v01285__00KJ = (v01285__00KJ*_00KI_coeff).reshape((1, 40, 100))

# op _00KM_power_combination_eval
# LANG: _rotor_radius --> _00KN
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01287__00KN = (v01130__rotor_radius**1)
v01287__00KN = (v01287__00KN*_00KM_coeff).reshape((1, 40, 100))

# op _00LN_power_combination_eval
# LANG: _00LM, _radius --> _local_torque_2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01347__local_torque_2 = (v01346__00LM**1)*(v01143__radius**1)
v01347__local_torque_2 = (v01347__local_torque_2*_00LN_coeff).reshape((1, 40, 100))

# op _00Lp_power_combination_eval
# LANG: _00Lo, _dr --> _local_thrust_2
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01299__local_thrust_2 = (v01298__00Lo**1)*(v01131__dr**1)
v01299__local_thrust_2 = (v01299__local_thrust_2*_00Lp_coeff).reshape((1, 40, 100))

# op _00MM_power_combination_eval
# LANG: _00MB, _00ML --> _00MN
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01328__00MN = (v01327__00MB**1)*(v01330__00ML**1)
v01328__00MN = (v01328__00MN*_00MM_coeff).reshape((1, 40, 100))

# op _00Mq_power_combination_eval
# LANG: _00Mf, _00Mp --> _00Mr
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01261__00Mr = (v01260__00Mf**1)*(v01263__00Mp**1)
v01261__00Mr = (v01261__00Mr*_00Mq_coeff).reshape((1, 40, 100))

# op _00NP_power_combination_eval
# LANG: _00NO, prandtl_loss_factor --> _00NQ
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01363__00NQ = (v01352__00NO**1)*(v01193_prandtl_loss_factor**1)
v01363__00NQ = (v01363__00NQ*_00NP_coeff).reshape((1, 40, 100))

# op _00Nj_power_combination_eval
# LANG: _00Ni, _dr --> _local_thrust_star
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01319__local_thrust_star = (v01318__00Ni**1)*(v01131__dr**1)
v01319__local_thrust_star = (v01319__local_thrust_star*_00Nj_coeff).reshape((1, 40, 100))

# op _00OG_power_combination_eval
# LANG: _00Ov, _00OF --> C_Q
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01386_C_Q = (v01381__00Ov**1)*(v01391__00OF**-1)
v01386_C_Q = (v01386_C_Q*_00OG_coeff).reshape((1,))

# op _00OU_power_combination_eval
# LANG: _00OT --> J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01399_J = (v01398__00OT**1)
v01399_J = (v01399_J*_00OU_coeff).reshape((1,))

# op _00P1_power_combination_eval
# LANG: _00P0 --> _00P2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01403__00P2 = (v01402__00P0**0.5)
v01403__00P2 = (v01403__00P2*_00P1_coeff).reshape((1,))

# op _00RC_power_combination_eval
# LANG: _00RB --> _00RD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01473__00RD = (v01472__00RB**1)
v01473__00RD = (v01473__00RD*_00RC_coeff).reshape((1,))

# op _00TA arccos_eval
# LANG: _00Tz --> _00TB
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01537__00TB = np.arccos(v01536__00Tz)

# op _00TC_linear_combination_eval
# LANG: rel_obs_z_pos --> _00TD
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01539__00TD = _00TC_constant+1*v01517_rel_obs_z_pos

# op _00TI_power_combination_eval
# LANG: _00TH --> _00TJ
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01542__00TJ = (v01541__00TH**2)
v01542__00TJ = (v01542__00TJ*_00TI_coeff).reshape((1, 1, 2))

# op _00Tk_power_combination_eval
# LANG: rel_obs_dist, _00Tj --> _00Tl
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01529__00Tl = (v01528__00Tj**1)*(v01525_rel_obs_dist**-1)
v01529__00Tl = (v01529__00Tl*_00Tk_coeff).reshape((1, 1, 2))

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

# op _00up_exp_a_eval
# LANG: _00uo --> _00uq
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0842__00uq = _00up_exp_a_eval_a**v0841__00uo

# op _00w7_power_combination_eval
# LANG: rel_obs_dist, _00w6 --> _00w8
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0899__00w8 = (v0898__00w6**1)*(v0891_rel_obs_dist**-1)
v0899__00w8 = (v0899__00w8*_00w7_coeff).reshape((1, 1, 2))

# op _00wh arccos_eval
# LANG: _00wg --> _00wi
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0903__00wi = np.arccos(v0902__00wg)

# op _00wj_linear_combination_eval
# LANG: rel_obs_z_pos --> _00wk
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0905__00wk = _00wj_constant+1*v0883_rel_obs_z_pos

# op _00wp_power_combination_eval
# LANG: _00wo --> _00wq
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0908__00wq = (v0907__00wo**2)
v0908__00wq = (v0908__00wq*_00wp_coeff).reshape((1, 1, 2))

# op _00y2_single_tensor_sum_with_axis_eval
# LANG: _00y1 --> _00y3
# SHAPES: (2, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0952__00y3 = np.sum(v0951__00y1, axis = (0,)).reshape((1, 2))

# op _00yB_power_combination_eval
# LANG: _00yA --> _00yC
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0979__00yC = (v0978__00yA**1)
v0979__00yC = (v0979__00yC*_00yB_coeff).reshape((1,))

# op _00yF_power_combination_eval
# LANG: _00yE --> _00yG
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0994__00yG = (v0993__00yE**1)
v0994__00yG = (v0994__00yG*_00yF_coeff).reshape((1,))

# op _00yN_power_combination_eval
# LANG: _00yM --> _00yO
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0981__00yO = (v0980__00yM**1)
v0981__00yO = (v0981__00yO*_00yN_coeff).reshape((1,))

# op _00yR_power_combination_eval
# LANG: _00yQ --> _00yS
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0996__00yS = (v0995__00yQ**1)
v0996__00yS = (v0996__00yS*_00yR_coeff).reshape((1,))

# op _00yZ_power_combination_eval
# LANG: _00yY --> _00y_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0983__00y_ = (v0982__00yY**1)
v0983__00y_ = (v0983__00y_*_00yZ_coeff).reshape((1,))

# op _00ym_power_combination_eval
# LANG: _00yl --> _00yn
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0976__00yn = (v0975__00yl**1)
v0976__00yn = (v0976__00yn*_00ym_coeff).reshape((1,))

# op _00yr_power_combination_eval
# LANG: _00yq --> _00ys
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0991__00ys = (v0990__00yq**1)
v0991__00ys = (v0991__00ys*_00yr_coeff).reshape((1,))

# op _00z2_power_combination_eval
# LANG: _00z1 --> _00z3
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0998__00z3 = (v0997__00z1**1)
v0998__00z3 = (v0998__00z3*_00z2_coeff).reshape((1,))

# op _00zC_power_combination_eval
# LANG: _00zB --> _00zD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01004__00zD = (v01003__00zB**1)
v01004__00zD = (v01004__00zD*_00zC_coeff).reshape((1,))

# op _00zS_power_combination_eval
# LANG: _00zR --> _00zT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01025__00zT = (v01024__00zR**1)
v01025__00zT = (v01025__00zT*_00zS_coeff).reshape((1,))

# op _00za_power_combination_eval
# LANG: _00z9 --> _00zb
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0985__00zb = (v0984__00z9**1)
v0985__00zb = (v0985__00zb*_00za_coeff).reshape((1,))

# op _00ze_power_combination_eval
# LANG: _00zd --> _00zf
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01000__00zf = (v0999__00zd**1)
v01000__00zf = (v01000__00zf*_00ze_coeff).reshape((1,))

# op _00zm_power_combination_eval
# LANG: _00zl --> _00zn
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0987__00zn = (v0986__00zl**1)
v0987__00zn = (v0987__00zn*_00zm_coeff).reshape((1,))

# op _00zq_power_combination_eval
# LANG: _00zp --> _00zr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01002__00zr = (v01001__00zp**1)
v01002__00zr = (v01002__00zr*_00zq_coeff).reshape((1,))

# op _00zy_power_combination_eval
# LANG: _00zx --> _00zz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0989__00zz = (v0988__00zx**1)
v0989__00zz = (v0989__00zz*_00zy_coeff).reshape((1,))

# op _0154_power_combination_eval
# LANG: rel_obs_dist, _0153 --> _0155
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01918__0155 = (v01917__0153**1)*(v01910_rel_obs_dist**-1)
v01918__0155 = (v01918__0155*_0154_coeff).reshape((1, 1, 2))

# op _015e arccos_eval
# LANG: _015d --> _015f
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01922__015f = np.arccos(v01921__015d)

# op _015g_linear_combination_eval
# LANG: rel_obs_z_pos --> _015h
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01924__015h = _015g_constant+1*v01902_rel_obs_z_pos

# op _015m_power_combination_eval
# LANG: _015l --> _015n
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01927__015n = (v01926__015l**2)
v01927__015n = (v01927__015n*_015m_coeff).reshape((1, 1, 2))

# op _017R_single_tensor_sum_with_axis_eval
# LANG: _017Q --> _017S
# SHAPES: (2, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01998__017S = np.sum(v01997__017Q, axis = (0,)).reshape((1, 2))

# op _0188_single_tensor_sum_with_axis_eval
# LANG: _0187 --> _0189
# SHAPES: (2, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02006__0189 = np.sum(v02005__0187, axis = (0,)).reshape((1, 2))

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

# op _00Ae_power_combination_eval
# LANG: _00A5 --> p
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0964_p = (v0958__00A5**1)
v0964_p = (v0964_p*_00Ae_coeff).reshape((1,))

# op _00Ag_power_combination_eval
# LANG: _00A5 --> q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0965_q = (v0958__00A5**1)
v0965_q = (v0965_q*_00Ag_coeff).reshape((1,))

# op _00Ai_power_combination_eval
# LANG: _00A5 --> r
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0966_r = (v0958__00A5**1)
v0966_r = (v0966_r*_00Ai_coeff).reshape((1,))

# op _00CN cross_product_eval
# LANG: F, _00CM --> _00CO
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01088__00CO = np.cross(v01086__00CM, v01081_F, axisa = 1, axisb = 1, axisc = 1)

# op _00Ce_power_combination_eval
# LANG: _00BZ, _00C7 --> mach_number
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01071_mach_number = (v01067__00BZ**1)*(v01072__00C7**-1)
v01071_mach_number = (v01071_mach_number*_00Ce_coeff).reshape((1, 40, 100))

# op _00KK_power_combination_eval
# LANG: _00KD, _00KJ --> _00KL
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01282__00KL = (v01281__00KD**1)*(v01285__00KJ**-1)
v01282__00KL = (v01282__00KL*_00KK_coeff).reshape((1, 40, 100))

# op _00KO_power_combination_eval
# LANG: _00KN --> _00KP
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01288__00KP = (v01287__00KN**4)
v01288__00KP = (v01288__00KP*_00KO_coeff).reshape((1, 40, 100))

# op _00MO_power_combination_eval
# LANG: _00MN, _chord --> _00MP
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01334__00MP = (v01328__00MN**1)*(v01138__chord**1)
v01334__00MP = (v01334__00MP*_00MO_coeff).reshape((1, 40, 100))

# op _00MS_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_2 --> _00MT
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01300__00MT = np.sum(v01299__local_thrust_2, axis = (1, 2)).reshape((1,))

# op _00MW_single_tensor_sum_with_axis_eval
# LANG: _local_torque_2 --> _00MX
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01348__00MX = np.sum(v01347__local_torque_2, axis = (1, 2)).reshape((1,))

# op _00Ms_power_combination_eval
# LANG: _00Mr, _chord --> _00Mt
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01267__00Mt = (v01261__00Mr**1)*(v01138__chord**1)
v01267__00Mt = (v01267__00Mt*_00Ms_coeff).reshape((1, 40, 100))

# op _00NR_power_combination_eval
# LANG: _00NQ, _dr --> _local_energy_loss
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01364__local_energy_loss = (v01363__00NQ**1)*(v01131__dr**1)
v01364__local_energy_loss = (v01364__local_energy_loss*_00NR_coeff).reshape((1, 40, 100))

# op _00Nl_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_star --> _00Nm
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01320__00Nm = np.sum(v01319__local_thrust_star, axis = (1, 2)).reshape((1,))

# op _00OI_power_combination_eval
# LANG: C_Q --> C_P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01392_C_P = (v01386_C_Q**1)
v01392_C_P = (v01392_C_P*_00OI_coeff).reshape((1,))

# op _00OW_power_combination_eval
# LANG: C_T, J --> _00OX
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01393__00OX = (v01374_C_T**1)*(v01399_J**1)
v01393__00OX = (v01393__00OX*_00OW_coeff).reshape((1,))

# op _00P3_power_combination_eval
# LANG: C_T, _00P2 --> _00P4
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01401__00P4 = (v01374_C_T**1)*(v01403__00P2**1)
v01401__00P4 = (v01401__00P4*_00P3_coeff).reshape((1,))

# op _00RE_power_combination_eval
# LANG: _00RD --> _00RF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01474__00RF = (v01473__00RD**1)
v01474__00RF = (v01474__00RF*_00RE_coeff).reshape((1,))

# op _00RG_linear_combination_eval
# LANG: temperature --> _00RH
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01476__00RH = _00RG_constant+1*v01465_temperature

# op _00TE_power_combination_eval
# LANG: _00TB, _00TD --> _00TF
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01538__00TF = (v01537__00TB**1)*(v01539__00TD**1)
v01538__00TF = (v01538__00TF*_00TE_coeff).reshape((1, 1, 2))

# op _00TK_power_combination_eval
# LANG: _00TJ --> _00TL
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01543__00TL = (v01542__00TJ**0.5)
v01543__00TL = (v01543__00TL*_00TK_coeff).reshape((1, 1, 2))

# op _00Tm_arcsin_eval
# LANG: _00Tl --> _00Tn
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01530__00Tn = np.arcsin(v01529__00Tl)

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

# op _00ur_log10_eval
# LANG: _00uq --> _00us
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0843__00us = np.log10(v0842__00uq)

# op _00w9 arccos_eval
# LANG: _00w8 --> _00wa
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0900__00wa = np.arccos(v0899__00w8)

# op _00wl_power_combination_eval
# LANG: _00wi, _00wk --> _00wm
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0904__00wm = (v0903__00wi**1)*(v0905__00wk**1)
v0904__00wm = (v0904__00wm*_00wl_coeff).reshape((1, 1, 2))

# op _00wr_power_combination_eval
# LANG: _00wq --> _00ws
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0909__00ws = (v0908__00wq**0.5)
v0909__00ws = (v0909__00ws*_00wr_coeff).reshape((1, 1, 2))

# op _00y4_log10_eval
# LANG: _00y3 --> _00y5
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0953__00y5 = np.log10(v0952__00y3)

# op _00yo_indexed_passthrough_eval
# LANG: _00yn, _00yC, _00yO, _00y_, _00zb, _00zn, _00zz --> temp_density
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0977_temp_density__temp[i_v0976__00yn__00yo_indexed_passthrough_eval] = v0976__00yn.flatten()
v0977_temp_density = v0977_temp_density__temp.copy()
v0977_temp_density__temp[i_v0979__00yC__00yo_indexed_passthrough_eval] = v0979__00yC.flatten()
v0977_temp_density = v0977_temp_density__temp.copy()
v0977_temp_density__temp[i_v0981__00yO__00yo_indexed_passthrough_eval] = v0981__00yO.flatten()
v0977_temp_density = v0977_temp_density__temp.copy()
v0977_temp_density__temp[i_v0983__00y___00yo_indexed_passthrough_eval] = v0983__00y_.flatten()
v0977_temp_density = v0977_temp_density__temp.copy()
v0977_temp_density__temp[i_v0985__00zb__00yo_indexed_passthrough_eval] = v0985__00zb.flatten()
v0977_temp_density = v0977_temp_density__temp.copy()
v0977_temp_density__temp[i_v0987__00zn__00yo_indexed_passthrough_eval] = v0987__00zn.flatten()
v0977_temp_density = v0977_temp_density__temp.copy()
v0977_temp_density__temp[i_v0989__00zz__00yo_indexed_passthrough_eval] = v0989__00zz.flatten()
v0977_temp_density = v0977_temp_density__temp.copy()

# op _00yt_indexed_passthrough_eval
# LANG: _00ys, _00yG, _00yS, _00z3, _00zf, _00zr, _00zD --> temp_pressure
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0992_temp_pressure__temp[i_v0991__00ys__00yt_indexed_passthrough_eval] = v0991__00ys.flatten()
v0992_temp_pressure = v0992_temp_pressure__temp.copy()
v0992_temp_pressure__temp[i_v0994__00yG__00yt_indexed_passthrough_eval] = v0994__00yG.flatten()
v0992_temp_pressure = v0992_temp_pressure__temp.copy()
v0992_temp_pressure__temp[i_v0996__00yS__00yt_indexed_passthrough_eval] = v0996__00yS.flatten()
v0992_temp_pressure = v0992_temp_pressure__temp.copy()
v0992_temp_pressure__temp[i_v0998__00z3__00yt_indexed_passthrough_eval] = v0998__00z3.flatten()
v0992_temp_pressure = v0992_temp_pressure__temp.copy()
v0992_temp_pressure__temp[i_v01000__00zf__00yt_indexed_passthrough_eval] = v01000__00zf.flatten()
v0992_temp_pressure = v0992_temp_pressure__temp.copy()
v0992_temp_pressure__temp[i_v01002__00zr__00yt_indexed_passthrough_eval] = v01002__00zr.flatten()
v0992_temp_pressure = v0992_temp_pressure__temp.copy()
v0992_temp_pressure__temp[i_v01004__00zD__00yt_indexed_passthrough_eval] = v01004__00zD.flatten()
v0992_temp_pressure = v0992_temp_pressure__temp.copy()

# op _00zU_power_combination_eval
# LANG: _00zT --> _00zV
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01026__00zV = (v01025__00zT**1)
v01026__00zV = (v01026__00zV*_00zU_coeff).reshape((1,))

# op _00zW_linear_combination_eval
# LANG: hover_temperature --> _00zX
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01028__00zX = _00zW_constant+1*v01020_hover_temperature

# op _00z__power_combination_eval
# LANG: hover_temperature --> _00A0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01029__00A0 = (v01020_hover_temperature**1)
v01029__00A0 = (v01029__00A0*_00z__coeff).reshape((1,))

# op _0156 arccos_eval
# LANG: _0155 --> _0157
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01919__0157 = np.arccos(v01918__0155)

# op _015i_power_combination_eval
# LANG: _015f, _015h --> _015j
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01923__015j = (v01922__015f**1)*(v01924__015h**1)
v01923__015j = (v01923__015j*_015i_coeff).reshape((1, 1, 2))

# op _015o_power_combination_eval
# LANG: _015n --> _015p
# SHAPES: (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01928__015p = (v01927__015n**0.5)
v01928__015p = (v01928__015p*_015o_coeff).reshape((1, 1, 2))

# op _017T_log10_eval
# LANG: _017S --> _017U
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v01999__017U = np.log10(v01998__017S)

# op _018a_log10_eval
# LANG: _0189 --> _018b
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02007__018b = np.log10(v02006__0189)

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

# op _00A1_power_combination_eval
# LANG: _00A0 --> hover_speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01030_hover_speed_of_sound = (v01029__00A0**0.5)
v01030_hover_speed_of_sound = (v01030_hover_speed_of_sound*_00A1_coeff).reshape((1,))

# op _00Ak_power_combination_eval
# LANG: _00A5 --> phi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0967_phi = (v0958__00A5**1)
v0967_phi = (v0967_phi*_00Ak_coeff).reshape((1,))

# op _00Am_power_combination_eval
# LANG: _00A5 --> gamma
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0968_gamma = (v0958__00A5**1)
v0968_gamma = (v0968_gamma*_00Am_coeff).reshape((1,))

# op _00Ao_power_combination_eval
# LANG: _00A5 --> psi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0969_psi = (v0958__00A5**1)
v0969_psi = (v0969_psi*_00Ao_coeff).reshape((1,))

# op _00As_power_combination_eval
# LANG: _00A5 --> x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0971_x = (v0958__00A5**1)
v0971_x = (v0971_x*_00As_coeff).reshape((1,))

# op _00Au_power_combination_eval
# LANG: _00A6 --> y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0972_y = (v0959__00A6**1)
v0972_y = (v0972_y*_00Au_coeff).reshape((1,))

# op _00Aw_power_combination_eval
# LANG: _00A7 --> z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0973_z = (v0960__00A7**1)
v0973_z = (v0973_z*_00Aw_coeff).reshape((1,))

# op _00CP_transpose_eval
# LANG: _00CO --> M
# SHAPES: (1, 3) --> (3, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01089_M = np.transpose(v01088__00CO)

# op _00Cg reshape_eval
# LANG: Re --> Re_ml_input
# SHAPES: (1, 40, 100) --> (4000, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01073_Re_ml_input = v01069_Re.reshape((4000, 1))

# op _00Ci reshape_eval
# LANG: mach_number --> mach_number_ml_input
# SHAPES: (1, 40, 100) --> (4000, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model
v01074_mach_number_ml_input = v01071_mach_number.reshape((4000, 1))

# op _00D0_power_combination_eval
# LANG: p --> p1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0964_p = v0964_p.reshape((1, 1))
v01097_p1 = (v0964_p**1)
v01097_p1 = (v01097_p1*_00D0_coeff).reshape((1, 1))
v0964_p = v0964_p.reshape((1,))

# op _00D3_power_combination_eval
# LANG: q --> q1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0965_q = v0965_q.reshape((1, 1))
v01098_q1 = (v0965_q**1)
v01098_q1 = (v01098_q1*_00D3_coeff).reshape((1, 1))
v0965_q = v0965_q.reshape((1,))

# op _00D6_power_combination_eval
# LANG: r --> r1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.BEM_external_inputs_model
v0966_r = v0966_r.reshape((1, 1))
v01099_r1 = (v0966_r**1)
v01099_r1 = (v01099_r1*_00D6_coeff).reshape((1, 1))
v0966_r = v0966_r.reshape((1,))

# op _00KQ_power_combination_eval
# LANG: _00KL, _00KP --> dC_T
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01286_dC_T = (v01282__00KL**1)*(v01288__00KP**-1)
v01286_dC_T = (v01286_dC_T*_00KQ_coeff).reshape((1, 40, 100))

# op _00MQ_power_combination_eval
# LANG: _00MP, _dr --> _local_torque_induced
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01335__local_torque_induced = (v01334__00MP**1)*(v01131__dr**1)
v01335__local_torque_induced = (v01335__local_torque_induced*_00MQ_coeff).reshape((1, 40, 100))

# op _00MU_power_combination_eval
# LANG: _00MT --> total_thrust_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01301_total_thrust_2 = (v01300__00MT**1)
v01301_total_thrust_2 = (v01301_total_thrust_2*_00MU_coeff).reshape((1,))

# op _00MY_power_combination_eval
# LANG: _00MX --> total_torque_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01349_total_torque_2 = (v01348__00MX**1)
v01349_total_torque_2 = (v01349_total_torque_2*_00MY_coeff).reshape((1,))

# op _00Mu_power_combination_eval
# LANG: _00Mt, _dr --> _local_thrust_induced
# SHAPES: (1, 40, 100), (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01268__local_thrust_induced = (v01267__00Mt**1)*(v01131__dr**1)
v01268__local_thrust_induced = (v01268__local_thrust_induced*_00Mu_coeff).reshape((1, 40, 100))

# op _00NT_single_tensor_sum_with_axis_eval
# LANG: _local_energy_loss --> total_energy_loss
# SHAPES: (1, 40, 100) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01365_total_energy_loss = np.sum(v01364__local_energy_loss, axis = (1, 2)).reshape((1,))

# op _00Nn_power_combination_eval
# LANG: _00Nm --> total_thrust_star
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01321_total_thrust_star = (v01320__00Nm**1)
v01321_total_thrust_star = (v01321_total_thrust_star*_00Nn_coeff).reshape((1,))

# op _00OY_power_combination_eval
# LANG: C_P, _00OX --> eta
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01400_eta = (v01393__00OX**1)*(v01392_C_P**-1)
v01400_eta = (v01400_eta*_00OY_coeff).reshape((1,))

# op _00P5_power_combination_eval
# LANG: C_P, _00P4 --> FOM
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01404_FOM = (v01401__00P4**1)*(v01392_C_P**-1)
v01404_FOM = (v01404_FOM*_00P5_coeff).reshape((1,))

# op _00P9_power_combination_eval
# LANG: total_torque --> Q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01280_Q = (v01279_total_torque**1)
v01280_Q = (v01280_Q*_00P9_coeff).reshape((1,))

# op _00Pb_power_combination_eval
# LANG: _local_torque --> _dQ
# SHAPES: (1, 40, 100) --> (1, 40, 100)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_bem_model.induced_velocity_model
v01322__dQ = (v01277__local_torque**1)
v01322__dQ = (v01322__dQ*_00Pb_coeff).reshape((1, 40, 100))

# op _00RI_power_combination_eval
# LANG: _00RF, _00RH --> dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.atmosphere_model
v01475_dynamic_viscosity = (v01474__00RF**1)*(v01476__00RH**-1)
v01475_dynamic_viscosity = (v01475_dynamic_viscosity*_00RI_coeff).reshape((1,))

# op _00TM_power_combination_eval
# LANG: _00TF, _00TL --> rel_obs_angle
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01540_rel_obs_angle = (v01538__00TF**1)*(v01543__00TL**-1)
v01540_rel_obs_angle = (v01540_rel_obs_angle*_00TM_coeff).reshape((1, 1, 2))

# op _00Tu reshape_eval
# LANG: _00Tn --> rel_angle_plane
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_KS_tonal_model.steady_observer_location_model
v01531_rel_angle_plane = v01530__00Tn.reshape((1, 2))

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

# op _00ut_power_combination_eval
# LANG: _00us --> rotor_disk_broadband_spl_A_weighted
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model
v0844_rotor_disk_broadband_spl_A_weighted = (v0843__00us**1)
v0844_rotor_disk_broadband_spl_A_weighted = (v0844_rotor_disk_broadband_spl_A_weighted*_00ut_coeff).reshape((1, 2))

# op _00wd reshape_eval
# LANG: _00wa --> rel_angle_normal
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0901_rel_angle_normal = v0900__00wa.reshape((1, 2))

# op _00wt_power_combination_eval
# LANG: _00wm, _00ws --> rel_obs_angle
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.rotor_disk_SKM_broadband_model.steady_observer_location_model
v0906_rel_obs_angle = (v0904__00wm**1)*(v0909__00ws**-1)
v0906_rel_obs_angle = (v0906_rel_obs_angle*_00wt_coeff).reshape((1, 1, 2))

# op _00y6_power_combination_eval
# LANG: _00y5 --> total_spl
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.cruise.cruise.total_noise_model
v0954_total_spl = (v0953__00y5**1)
v0954_total_spl = (v0954_total_spl*_00y6_coeff).reshape((1, 2))

# op _00ye_power_combination_eval
# LANG: hover_hover_time --> hover_time
# SHAPES: (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation
v0957_hover_time = (v0955_hover_hover_time**1)
v0957_hover_time = (v0957_hover_time*_00ye_coeff).reshape((1,))

# op _00zI single_tensor_sum_no_axis_eval
# LANG: temp_density --> hover_density
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01022_hover_density = np.sum(v0977_temp_density).reshape((1,))

# op _00zK single_tensor_sum_no_axis_eval
# LANG: temp_pressure --> hover_pressure
# SHAPES: (7,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01021_hover_pressure = np.sum(v0992_temp_pressure).reshape((1,))

# op _00zY_power_combination_eval
# LANG: _00zV, _00zX --> hover_dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.single_rotor_test.hover.hover.hover_ac_states_operation.atmosphere_model
v01027_hover_dynamic_viscosity = (v01026__00zV**1)*(v01028__00zX**-1)
v01027_hover_dynamic_viscosity = (v01027_hover_dynamic_viscosity*_00zY_coeff).reshape((1,))

# op _015a reshape_eval
# LANG: _0157 --> rel_angle_normal
# SHAPES: (1, 1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01920_rel_angle_normal = v01919__0157.reshape((1, 2))

# op _015q_power_combination_eval
# LANG: _015j, _015p --> rel_obs_angle
# SHAPES: (1, 1, 2), (1, 1, 2) --> (1, 1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.rotor_disk_GL_broadband_model.steady_observer_location_model
v01925_rel_obs_angle = (v01923__015j**1)*(v01928__015p**-1)
v01925_rel_obs_angle = (v01925_rel_obs_angle*_015q_coeff).reshape((1, 1, 2))

# op _017V_power_combination_eval
# LANG: _017U --> total_spl
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02000_total_spl = (v01999__017U**1)
v02000_total_spl = (v02000_total_spl*_017V_coeff).reshape((1, 2))

# op _018c_power_combination_eval
# LANG: _018b --> A_weighted_total_spl
# SHAPES: (1, 2) --> (1, 2)
# full namespace: system_model.single_rotor_test.hover.hover.total_noise_model
v02008_A_weighted_total_spl = (v02007__018b**1)
v02008_A_weighted_total_spl = (v02008_A_weighted_total_spl*_018c_coeff).reshape((1, 2))