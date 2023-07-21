

# RUN_MODEL

# system evaluation block

# op _0009_power_combination_eval
# LANG: system_representation_geometry --> design_geometry
# SHAPES: (32500, 3) --> (32500, 3)
# full namespace: system_representation.system_configurations_model
v05_design_geometry = (v04_system_representation_geometry**1)
v05_design_geometry = (v05_design_geometry*_0009_coeff).reshape((32500, 3))

# op _000A_sparsematmat_eval
# LANG: design_geometry --> _000B
# SHAPES: (32500, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v017__000B = _000A_sparsematmat_eval_mat@v05_design_geometry

# op _000E_sparsematmat_eval
# LANG: design_geometry --> _000F
# SHAPES: (32500, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v019__000F = _000E_sparsematmat_eval_mat@v05_design_geometry

# op _000g_sparsematmat_eval
# LANG: design_geometry --> _000h
# SHAPES: (32500, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v07__000h = _000g_sparsematmat_eval_mat@v05_design_geometry

# op _000k_sparsematmat_eval
# LANG: design_geometry --> _000l
# SHAPES: (32500, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v09__000l = _000k_sparsematmat_eval_mat@v05_design_geometry

# op _000C reshape_eval
# LANG: _000B --> rotor_2_disk_in_plane_1
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v018_rotor_2_disk_in_plane_1 = v017__000B.reshape((1, 3))

# op _000G reshape_eval
# LANG: _000F --> rotor_2_disk_in_plane_2
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v020_rotor_2_disk_in_plane_2 = v019__000F.reshape((1, 3))

# op _000i reshape_eval
# LANG: _000h --> rotor_1_disk_in_plane_1
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v08_rotor_1_disk_in_plane_1 = v07__000h.reshape((1, 3))

# op _000m reshape_eval
# LANG: _000l --> rotor_1_disk_in_plane_2
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v010_rotor_1_disk_in_plane_2 = v09__000l.reshape((1, 3))

# op _002O_decompose_eval
# LANG: hover_observer_location --> _002P, _002Q, _002R
# SHAPES: (3,) --> (1,), (1,), (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v030__002P = ((v028_hover_observer_location.flatten())[src_indices__002P__002O]).reshape((1,))
v031__002Q = ((v028_hover_observer_location.flatten())[src_indices__002Q__002O]).reshape((1,))
v032__002R = ((v028_hover_observer_location.flatten())[src_indices__002R__002O]).reshape((1,))

# op _0039_power_combination_eval
# LANG: _002P --> theta
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v042_theta = (v030__002P**1)
v042_theta = (v042_theta*_0039_coeff).reshape((1,))

# op _004b cross_product_eval
# LANG: rotor_2_disk_in_plane_1, rotor_2_disk_in_plane_2 --> _004c
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v018_rotor_2_disk_in_plane_1 = v018_rotor_2_disk_in_plane_1.reshape((3,))
v020_rotor_2_disk_in_plane_2 = v020_rotor_2_disk_in_plane_2.reshape((3,))
v0124__004c = np.cross(v020_rotor_2_disk_in_plane_2, v018_rotor_2_disk_in_plane_1, axisa = 0, axisb = 0, axisc = 0)
v018_rotor_2_disk_in_plane_1 = v018_rotor_2_disk_in_plane_1.reshape((1, 3))
v020_rotor_2_disk_in_plane_2 = v020_rotor_2_disk_in_plane_2.reshape((1, 3))

# op _00je cross_product_eval
# LANG: rotor_1_disk_in_plane_1, rotor_1_disk_in_plane_2 --> _00jf
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v08_rotor_1_disk_in_plane_1 = v08_rotor_1_disk_in_plane_1.reshape((3,))
v010_rotor_1_disk_in_plane_2 = v010_rotor_1_disk_in_plane_2.reshape((3,))
v0497__00jf = np.cross(v010_rotor_1_disk_in_plane_2, v08_rotor_1_disk_in_plane_1, axisa = 0, axisb = 0, axisc = 0)
v08_rotor_1_disk_in_plane_1 = v08_rotor_1_disk_in_plane_1.reshape((1, 3))
v010_rotor_1_disk_in_plane_2 = v010_rotor_1_disk_in_plane_2.reshape((1, 3))

# op _003A_linear_combination_eval
# LANG: theta --> _003B
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0109__003B = _003A_constant+1*v042_theta
v042_theta = v042_theta.reshape((1,))

# op _003E_sin_eval
# LANG: theta --> _003F
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0110__003F = np.sin(v042_theta)
v042_theta = v042_theta.reshape((1,))

# op _003I_cos_eval
# LANG: theta --> _003J
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0112__003J = np.cos(v042_theta)
v042_theta = v042_theta.reshape((1,))

# op _003u_sin_eval
# LANG: theta --> _003v
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0105__003v = np.sin(v042_theta)
v042_theta = v042_theta.reshape((1,))

# op _003y_linear_combination_eval
# LANG: theta --> _003z
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0107__003z = _003y_constant+1*v042_theta
v042_theta = v042_theta.reshape((1,))

# op _004d pnorm_eval
# LANG: _004c --> _004e
# SHAPES: (3,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0126__004e = np.linalg.norm(v0124__004c.flatten(), ord=2)

# op _00iB_linear_combination_eval
# LANG: theta --> _00iC
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0480__00iC = _00iB_constant+1*v042_theta
v042_theta = v042_theta.reshape((1,))

# op _00iD_linear_combination_eval
# LANG: theta --> _00iE
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0482__00iE = _00iD_constant+1*v042_theta
v042_theta = v042_theta.reshape((1,))

# op _00iH_sin_eval
# LANG: theta --> _00iI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0483__00iI = np.sin(v042_theta)
v042_theta = v042_theta.reshape((1,))

# op _00iL_cos_eval
# LANG: theta --> _00iM
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0485__00iM = np.cos(v042_theta)
v042_theta = v042_theta.reshape((1,))

# op _00ix_sin_eval
# LANG: theta --> _00iy
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0478__00iy = np.sin(v042_theta)
v042_theta = v042_theta.reshape((1,))

# op _00jg pnorm_eval
# LANG: _00jf --> _00jh
# SHAPES: (3,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0499__00jh = np.linalg.norm(v0497__00jf.flatten(), ord=2)

# op _003C_power_combination_eval
# LANG: _003z, _003B --> _003D
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0108__003D = (v0107__003z**1)*(v0109__003B**-1)
v0108__003D = (v0108__003D*_003C_coeff).reshape((1, 1))

# op _003G_power_combination_eval
# LANG: _003F --> _003H
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0111__003H = (v0110__003F**1)
v0111__003H = (v0111__003H*_003G_coeff).reshape((1, 1))

# op _003K_power_combination_eval
# LANG: _003J --> _003L
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0113__003L = (v0112__003J**1)
v0113__003L = (v0113__003L*_003K_coeff).reshape((1, 1))

# op _003r_cos_eval
# LANG: theta --> _003s
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0103__003s = np.cos(v042_theta)
v042_theta = v042_theta.reshape((1,))

# op _003w_power_combination_eval
# LANG: _003v --> _003x
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0106__003x = (v0105__003v**1)
v0106__003x = (v0106__003x*_003w_coeff).reshape((1, 1))

# op _004f expand_scalar_eval
# LANG: _004e --> _004g
# SHAPES: (1,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0127__004g = np.empty((3,))
v0127__004g.fill(v0126__004e.item())

# op _00iF_power_combination_eval
# LANG: _00iC, _00iE --> _00iG
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0481__00iG = (v0480__00iC**1)*(v0482__00iE**-1)
v0481__00iG = (v0481__00iG*_00iF_coeff).reshape((1, 1))

# op _00iJ_power_combination_eval
# LANG: _00iI --> _00iK
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0484__00iK = (v0483__00iI**1)
v0484__00iK = (v0484__00iK*_00iJ_coeff).reshape((1, 1))

# op _00iN_power_combination_eval
# LANG: _00iM --> _00iO
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0486__00iO = (v0485__00iM**1)
v0486__00iO = (v0486__00iO*_00iN_coeff).reshape((1, 1))

# op _00iu_cos_eval
# LANG: theta --> _00iv
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v042_theta = v042_theta.reshape((1, 1))
v0476__00iv = np.cos(v042_theta)
v042_theta = v042_theta.reshape((1,))

# op _00iz_power_combination_eval
# LANG: _00iy --> _00iA
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0479__00iA = (v0478__00iy**1)
v0479__00iA = (v0479__00iA*_00iz_coeff).reshape((1, 1))

# op _00ji expand_scalar_eval
# LANG: _00jh --> _00jj
# SHAPES: (1,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0500__00jj = np.empty((3,))
v0500__00jj.fill(v0499__00jh.item())

# op _003t_indexed_passthrough_eval
# LANG: _003s, _003x, _003D, _003H, _003L --> rotation_matrix
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0104_rotation_matrix__temp[i_v0103__003s__003t_indexed_passthrough_eval] = v0103__003s.flatten()
v0104_rotation_matrix = v0104_rotation_matrix__temp.copy()
v0104_rotation_matrix__temp[i_v0106__003x__003t_indexed_passthrough_eval] = v0106__003x.flatten()
v0104_rotation_matrix = v0104_rotation_matrix__temp.copy()
v0104_rotation_matrix__temp[i_v0108__003D__003t_indexed_passthrough_eval] = v0108__003D.flatten()
v0104_rotation_matrix = v0104_rotation_matrix__temp.copy()
v0104_rotation_matrix__temp[i_v0111__003H__003t_indexed_passthrough_eval] = v0111__003H.flatten()
v0104_rotation_matrix = v0104_rotation_matrix__temp.copy()
v0104_rotation_matrix__temp[i_v0113__003L__003t_indexed_passthrough_eval] = v0113__003L.flatten()
v0104_rotation_matrix = v0104_rotation_matrix__temp.copy()

# op _004h_power_combination_eval
# LANG: _004c, _004g --> _004i
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0125__004i = (v0124__004c**1)*(v0127__004g**-1)
v0125__004i = (v0125__004i*_004h_coeff).reshape((3,))

# op _00iw_indexed_passthrough_eval
# LANG: _00iv, _00iA, _00iG, _00iK, _00iO --> rotation_matrix
# SHAPES: (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) --> (3, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0477_rotation_matrix__temp[i_v0476__00iv__00iw_indexed_passthrough_eval] = v0476__00iv.flatten()
v0477_rotation_matrix = v0477_rotation_matrix__temp.copy()
v0477_rotation_matrix__temp[i_v0479__00iA__00iw_indexed_passthrough_eval] = v0479__00iA.flatten()
v0477_rotation_matrix = v0477_rotation_matrix__temp.copy()
v0477_rotation_matrix__temp[i_v0481__00iG__00iw_indexed_passthrough_eval] = v0481__00iG.flatten()
v0477_rotation_matrix = v0477_rotation_matrix__temp.copy()
v0477_rotation_matrix__temp[i_v0484__00iK__00iw_indexed_passthrough_eval] = v0484__00iK.flatten()
v0477_rotation_matrix = v0477_rotation_matrix__temp.copy()
v0477_rotation_matrix__temp[i_v0486__00iO__00iw_indexed_passthrough_eval] = v0486__00iO.flatten()
v0477_rotation_matrix = v0477_rotation_matrix__temp.copy()

# op _00jk_power_combination_eval
# LANG: _00jf, _00jj --> _00jl
# SHAPES: (3,), (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0498__00jl = (v0497__00jf**1)*(v0500__00jj**-1)
v0498__00jl = (v0498__00jl*_00jk_coeff).reshape((3,))

# op _004j_matvec_eval
# LANG: rotation_matrix, _004i --> _004k
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0123__004k = v0104_rotation_matrix@v0125__004i

# op _00jm_matvec_eval
# LANG: rotation_matrix, _00jl --> _00jn
# SHAPES: (3, 3), (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0496__00jn = v0477_rotation_matrix@v0498__00jl

# op _004l expand_array_eval
# LANG: _004k --> thrust_vector
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0128_thrust_vector = np.einsum('b,a->ab', v0123__004k.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

# op _00jo expand_array_eval
# LANG: _00jn --> thrust_vector
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0501_thrust_vector = np.einsum('b,a->ab', v0496__00jn.reshape((3,)) ,np.ones((1,))).reshape((1, 3))

# op _005Y_decompose_eval
# LANG: thrust_vector --> _005Z
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0173__005Z = ((v0128_thrust_vector.flatten())[src_indices__005Z__005Y]).reshape((1, 3))

# op _00l0_decompose_eval
# LANG: thrust_vector --> _00l1
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0546__00l1 = ((v0501_thrust_vector.flatten())[src_indices__00l1__00l0]).reshape((1, 3))

# op _0061_tensor_dot_product_eval
# LANG: projection_vector, _005Z --> _0062
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0180__0062 = np.sum(v0162_projection_vector * v0173__005Z, axis=1)

# op _00l4_tensor_dot_product_eval
# LANG: projection_vector, _00l1 --> _00l5
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0553__00l5 = np.sum(v0535_projection_vector * v0546__00l1, axis=1)

# op _0063 expand_scalar_eval
# LANG: _0062 --> _0064
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0181__0064 = np.empty((1, 3))
v0181__0064.fill(v0180__0062.item())

# op _00l6 expand_scalar_eval
# LANG: _00l5 --> _00l7
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0554__00l7 = np.empty((1, 3))
v0554__00l7.fill(v0553__00l5.item())

# op _0065_power_combination_eval
# LANG: _005Z, _0064 --> _0066
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0182__0066 = (v0181__0064**1)*(v0173__005Z**1)
v0182__0066 = (v0182__0066*_0065_coeff).reshape((1, 3))

# op _00l8_power_combination_eval
# LANG: _00l1, _00l7 --> _00l9
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0555__00l9 = (v0554__00l7**1)*(v0546__00l1**1)
v0555__00l9 = (v0555__00l9*_00l8_coeff).reshape((1, 3))

# op _002S_power_combination_eval
# LANG: _002P --> u
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v033_u = (v030__002P**1)
v033_u = (v033_u*_002S_coeff).reshape((1,))

# op _0067_linear_combination_eval
# LANG: projection_vector, _0066 --> _0068
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0179__0068 = _0067_constant+1*v0162_projection_vector+-1*v0182__0066

# op _00la_linear_combination_eval
# LANG: projection_vector, _00l9 --> _00lb
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0552__00lb = _00la_constant+1*v0535_projection_vector+-1*v0555__00l9

# op _002U_power_combination_eval
# LANG: _002P --> v
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v034_v = (v030__002P**1)
v034_v = (v034_v*_002U_coeff).reshape((1,))

# op _002W_power_combination_eval
# LANG: _002P --> w
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v035_w = (v030__002P**1)
v035_w = (v035_w*_002W_coeff).reshape((1,))

# op _005z_power_combination_eval
# LANG: u --> _005A
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v033_u = v033_u.reshape((1, 1))
v0163__005A = (v033_u**1)
v0163__005A = (v0163__005A*_005z_coeff).reshape((1, 1))
v033_u = v033_u.reshape((1,))

# op _0069 pnorm_eval
# LANG: _0068 --> _006a
# SHAPES: (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0184__006a = np.linalg.norm(v0179__0068.flatten(), ord=2)

# op _00kC_power_combination_eval
# LANG: u --> _00kD
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v033_u = v033_u.reshape((1, 1))
v0536__00kD = (v033_u**1)
v0536__00kD = (v0536__00kD*_00kC_coeff).reshape((1, 1))
v033_u = v033_u.reshape((1,))

# op _00lc pnorm_eval
# LANG: _00lb --> _00ld
# SHAPES: (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0557__00ld = np.linalg.norm(v0552__00lb.flatten(), ord=2)

# op _006b expand_scalar_eval
# LANG: _006a --> _006c
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0185__006c = np.empty((1, 3))
v0185__006c.fill(v0184__006a.item())

# op _006m_decompose_eval
# LANG: _005A --> _006n
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0164__006n = ((v0163__005A.flatten())[src_indices__006n__006m]).reshape((1, 1))

# op _006p_decompose_eval
# LANG: v --> _006q
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v034_v = v034_v.reshape((1, 1))
v0166__006q = ((v034_v.flatten())[src_indices__006q__006p]).reshape((1, 1))
v034_v = v034_v.reshape((1,))

# op _006r_decompose_eval
# LANG: w --> _006s
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v035_w = v035_w.reshape((1, 1))
v0167__006s = ((v035_w.flatten())[src_indices__006s__006r]).reshape((1, 1))
v035_w = v035_w.reshape((1,))

# op _00le expand_scalar_eval
# LANG: _00ld --> _00lf
# SHAPES: (1,) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0558__00lf = np.empty((1, 3))
v0558__00lf.fill(v0557__00ld.item())

# op _00lp_decompose_eval
# LANG: _00kD --> _00lq
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0537__00lq = ((v0536__00kD.flatten())[src_indices__00lq__00lp]).reshape((1, 1))

# op _00ls_decompose_eval
# LANG: v --> _00lt
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v034_v = v034_v.reshape((1, 1))
v0539__00lt = ((v034_v.flatten())[src_indices__00lt__00ls]).reshape((1, 1))
v034_v = v034_v.reshape((1,))

# op _00lu_decompose_eval
# LANG: w --> _00lv
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v035_w = v035_w.reshape((1, 1))
v0540__00lv = ((v035_w.flatten())[src_indices__00lv__00lu]).reshape((1, 1))
v035_w = v035_w.reshape((1,))

# op _006d_power_combination_eval
# LANG: _0068, _006c --> in_plane_ey
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0183_in_plane_ey = (v0179__0068**1)*(v0185__006c**-1)
v0183_in_plane_ey = (v0183_in_plane_ey*_006d_coeff).reshape((1, 3))

# op _006o_indexed_passthrough_eval
# LANG: _006n, _006q, _006s --> velocity_vector
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0165_velocity_vector__temp[i_v0164__006n__006o_indexed_passthrough_eval] = v0164__006n.flatten()
v0165_velocity_vector = v0165_velocity_vector__temp.copy()
v0165_velocity_vector__temp[i_v0166__006q__006o_indexed_passthrough_eval] = v0166__006q.flatten()
v0165_velocity_vector = v0165_velocity_vector__temp.copy()
v0165_velocity_vector__temp[i_v0167__006s__006o_indexed_passthrough_eval] = v0167__006s.flatten()
v0165_velocity_vector = v0165_velocity_vector__temp.copy()

# op _00lg_power_combination_eval
# LANG: _00lb, _00lf --> in_plane_ey
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0556_in_plane_ey = (v0552__00lb**1)*(v0558__00lf**-1)
v0556_in_plane_ey = (v0556_in_plane_ey*_00lg_coeff).reshape((1, 3))

# op _00lr_indexed_passthrough_eval
# LANG: _00lq, _00lt, _00lv --> velocity_vector
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0538_velocity_vector__temp[i_v0537__00lq__00lr_indexed_passthrough_eval] = v0537__00lq.flatten()
v0538_velocity_vector = v0538_velocity_vector__temp.copy()
v0538_velocity_vector__temp[i_v0539__00lt__00lr_indexed_passthrough_eval] = v0539__00lt.flatten()
v0538_velocity_vector = v0538_velocity_vector__temp.copy()
v0538_velocity_vector__temp[i_v0540__00lv__00lr_indexed_passthrough_eval] = v0540__00lv.flatten()
v0538_velocity_vector = v0538_velocity_vector__temp.copy()

# op _006f cross_product_eval
# LANG: _005Z, in_plane_ey --> in_plane_ex
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0178_in_plane_ex = np.cross(v0173__005Z, v0183_in_plane_ey, axisa = 1, axisb = 1, axisc = 1)

# op _006t_decompose_eval
# LANG: velocity_vector --> _006u
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0171__006u = ((v0165_velocity_vector.flatten())[src_indices__006u__006t]).reshape((1, 3))

# op _00li cross_product_eval
# LANG: _00l1, in_plane_ey --> in_plane_ex
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0551_in_plane_ex = np.cross(v0546__00l1, v0556_in_plane_ey, axisa = 1, axisb = 1, axisc = 1)

# op _00lw_decompose_eval
# LANG: velocity_vector --> _00lx
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0544__00lx = ((v0538_velocity_vector.flatten())[src_indices__00lx__00lw]).reshape((1, 3))

# op _005__power_combination_eval
# LANG: _005Z --> _0060
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0174__0060 = (v0173__005Z**1)
v0174__0060 = (v0174__0060*_005__coeff).reshape((1, 3))

# op _006v_tensor_dot_product_eval
# LANG: _006u, in_plane_ex --> _006w
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0177__006w = np.sum(v0171__006u * v0178_in_plane_ex, axis=1)

# op _00l2_power_combination_eval
# LANG: _00l1 --> _00l3
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0547__00l3 = (v0546__00l1**1)
v0547__00l3 = (v0547__00l3*_00l2_coeff).reshape((1, 3))

# op _00ly_tensor_dot_product_eval
# LANG: _00lx, in_plane_ex --> _00lz
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0550__00lz = np.sum(v0544__00lx * v0551_in_plane_ex, axis=1)

# op _0047 pnorm_eval
# LANG: rotor_2_disk_in_plane_1 --> _0048
# SHAPES: (3,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v018_rotor_2_disk_in_plane_1 = v018_rotor_2_disk_in_plane_1.reshape((3,))
v0121__0048 = np.linalg.norm(v018_rotor_2_disk_in_plane_1.flatten(), ord=2)
v018_rotor_2_disk_in_plane_1 = v018_rotor_2_disk_in_plane_1.reshape((1, 3))

# op _006E_linear_combination_eval
# LANG: _006w --> _006F
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0186__006F = _006E_constant+-1*v0177__006w

# op _006x_tensor_dot_product_eval
# LANG: _006u, in_plane_ey --> _006y
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0188__006y = np.sum(v0171__006u * v0183_in_plane_ey, axis=1)

# op _006z_tensor_dot_product_eval
# LANG: _006u, _0060 --> _006A
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0172__006A = np.sum(v0171__006u * v0174__0060, axis=1)

# op _00ja pnorm_eval
# LANG: rotor_1_disk_in_plane_1 --> _00jb
# SHAPES: (3,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v08_rotor_1_disk_in_plane_1 = v08_rotor_1_disk_in_plane_1.reshape((3,))
v0494__00jb = np.linalg.norm(v08_rotor_1_disk_in_plane_1.flatten(), ord=2)
v08_rotor_1_disk_in_plane_1 = v08_rotor_1_disk_in_plane_1.reshape((1, 3))

# op _00lA_tensor_dot_product_eval
# LANG: _00lx, in_plane_ey --> _00lB
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0561__00lB = np.sum(v0544__00lx * v0556_in_plane_ey, axis=1)

# op _00lC_tensor_dot_product_eval
# LANG: _00lx, _00l3 --> _00lD
# SHAPES: (1, 3), (1, 3) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0545__00lD = np.sum(v0544__00lx * v0547__00l3, axis=1)

# op _00lH_linear_combination_eval
# LANG: _00lz --> _00lI
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0559__00lI = _00lH_constant+-1*v0550__00lz

# op _0049_power_combination_eval
# LANG: _0048 --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0122_propeller_radius = (v0121__0048**1)
v0122_propeller_radius = (v0122_propeller_radius*_0049_coeff).reshape((1,))

# op _006B expand_scalar_eval
# LANG: _006A --> _006C
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0175__006C = np.empty((1, 40, 30, 1))
v0175__006C.fill(v0172__006A.item())

# op _006G expand_scalar_eval
# LANG: _006F --> _006H
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0187__006H = np.empty((1, 40, 30, 1))
v0187__006H.fill(v0186__006F.item())

# op _006I expand_scalar_eval
# LANG: _006y --> _006J
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0189__006J = np.empty((1, 40, 30, 1))
v0189__006J.fill(v0188__006y.item())

# op _00jc_power_combination_eval
# LANG: _00jb --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0495_propeller_radius = (v0494__00jb**1)
v0495_propeller_radius = (v0495_propeller_radius*_00jc_coeff).reshape((1,))

# op _00lE expand_scalar_eval
# LANG: _00lD --> _00lF
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0548__00lF = np.empty((1, 40, 30, 1))
v0548__00lF.fill(v0545__00lD.item())

# op _00lJ expand_scalar_eval
# LANG: _00lI --> _00lK
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0560__00lK = np.empty((1, 40, 30, 1))
v0560__00lK.fill(v0559__00lI.item())

# op _00lL expand_scalar_eval
# LANG: _00lB --> _00lM
# SHAPES: (1,) --> (1, 40, 30, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0562__00lM = np.empty((1, 40, 30, 1))
v0562__00lM.fill(v0561__00lB.item())

# op _005O_power_combination_eval
# LANG: propeller_radius --> hub_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0190_hub_radius = (v0122_propeller_radius**1)
v0190_hub_radius = (v0190_hub_radius*_005O_coeff).reshape((1,))

# op _006D_indexed_passthrough_eval
# LANG: _006C, _006H, _006J --> inflow_velocity
# SHAPES: (1, 40, 30, 1), (1, 40, 30, 1), (1, 40, 30, 1) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0176_inflow_velocity__temp[i_v0175__006C__006D_indexed_passthrough_eval] = v0175__006C.flatten()
v0176_inflow_velocity = v0176_inflow_velocity__temp.copy()
v0176_inflow_velocity__temp[i_v0187__006H__006D_indexed_passthrough_eval] = v0187__006H.flatten()
v0176_inflow_velocity = v0176_inflow_velocity__temp.copy()
v0176_inflow_velocity__temp[i_v0189__006J__006D_indexed_passthrough_eval] = v0189__006J.flatten()
v0176_inflow_velocity = v0176_inflow_velocity__temp.copy()

# op _006h_decompose_eval
# LANG: rpm --> _006i
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0194__006i = ((v0158_rpm.flatten())[src_indices__006i__006h]).reshape((1, 1))

# op _0087_power_combination_eval
# LANG: z --> _0088
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0234__0088 = (v0233_z**1)
v0234__0088 = (v0234__0088*_0087_coeff).reshape((1, 1))

# op _00kR_power_combination_eval
# LANG: propeller_radius --> hub_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0563_hub_radius = (v0495_propeller_radius**1)
v0563_hub_radius = (v0563_hub_radius*_00kR_coeff).reshape((1,))

# op _00lG_indexed_passthrough_eval
# LANG: _00lF, _00lK, _00lM --> inflow_velocity
# SHAPES: (1, 40, 30, 1), (1, 40, 30, 1), (1, 40, 30, 1) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0549_inflow_velocity__temp[i_v0548__00lF__00lG_indexed_passthrough_eval] = v0548__00lF.flatten()
v0549_inflow_velocity = v0549_inflow_velocity__temp.copy()
v0549_inflow_velocity__temp[i_v0560__00lK__00lG_indexed_passthrough_eval] = v0560__00lK.flatten()
v0549_inflow_velocity = v0549_inflow_velocity__temp.copy()
v0549_inflow_velocity__temp[i_v0562__00lM__00lG_indexed_passthrough_eval] = v0562__00lM.flatten()
v0549_inflow_velocity = v0549_inflow_velocity__temp.copy()

# op _00lk_decompose_eval
# LANG: rpm --> _00ll
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0567__00ll = ((v0531_rpm.flatten())[src_indices__00ll__00lk]).reshape((1, 1))

# op _00na_power_combination_eval
# LANG: z --> _00nb
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0607__00nb = (v0606_z**1)
v0607__00nb = (v0607__00nb*_00na_coeff).reshape((1, 1))

# op _006Y expand_scalar_eval
# LANG: hub_radius --> _hub_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0200__hub_radius = np.empty((1, 40, 30))
v0200__hub_radius.fill(v0190_hub_radius.item())

# op _006_ expand_scalar_eval
# LANG: propeller_radius --> _rotor_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0201__rotor_radius = np.empty((1, 40, 30))
v0201__rotor_radius.fill(v0122_propeller_radius.item())

# op _006j_power_combination_eval
# LANG: _006i --> _006k
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0195__006k = (v0194__006i**1)
v0195__006k = (v0195__006k*_006j_coeff).reshape((1, 1))

# op _0077 expand_array_eval
# LANG: y_dir --> _y_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0205__y_dir = np.einsum('ad,bc->abcd', v0198_y_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _0079 expand_array_eval
# LANG: z_dir --> _z_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0206__z_dir = np.einsum('ad,bc->abcd', v0199_z_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _007b_power_combination_eval
# LANG: inflow_velocity --> _inflow_velocity
# SHAPES: (1, 40, 30, 3) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0207__inflow_velocity = (v0176_inflow_velocity**1)
v0207__inflow_velocity = (v0207__inflow_velocity*_007b_coeff).reshape((1, 40, 30, 3))

# op _0089_linear_combination_eval
# LANG: _0088 --> _008a
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0235__008a = _0089_constant+-1*v0234__0088

# op _00lm_power_combination_eval
# LANG: _00ll --> _00ln
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0568__00ln = (v0567__00ll**1)
v0568__00ln = (v0568__00ln*_00lm_coeff).reshape((1, 1))

# op _00m0 expand_scalar_eval
# LANG: hub_radius --> _hub_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0573__hub_radius = np.empty((1, 40, 30))
v0573__hub_radius.fill(v0563_hub_radius.item())

# op _00m2 expand_scalar_eval
# LANG: propeller_radius --> _rotor_radius
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0574__rotor_radius = np.empty((1, 40, 30))
v0574__rotor_radius.fill(v0495_propeller_radius.item())

# op _00ma expand_array_eval
# LANG: y_dir --> _y_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0578__y_dir = np.einsum('ad,bc->abcd', v0571_y_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _00mc expand_array_eval
# LANG: z_dir --> _z_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0579__z_dir = np.einsum('ad,bc->abcd', v0572_z_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _00me_power_combination_eval
# LANG: inflow_velocity --> _inflow_velocity
# SHAPES: (1, 40, 30, 3) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0580__inflow_velocity = (v0549_inflow_velocity**1)
v0580__inflow_velocity = (v0580__inflow_velocity*_00me_coeff).reshape((1, 40, 30, 3))

# op _00nc_linear_combination_eval
# LANG: _00nb --> _00nd
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0608__00nd = _00nc_constant+-1*v0607__00nb

# op _006l_indexed_passthrough_eval
# LANG: _006k --> rotational_speed
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0196_rotational_speed__temp[i_v0195__006k__006l_indexed_passthrough_eval] = v0195__006k.flatten()
v0196_rotational_speed = v0196_rotational_speed__temp.copy()

# op _007L_tensor_dot_product_eval
# LANG: _y_dir, _inflow_velocity --> _in_plane_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0222__in_plane_inflow_velocity = np.sum(v0207__inflow_velocity * v0205__y_dir, axis=3)

# op _007N_tensor_dot_product_eval
# LANG: _z_dir, _inflow_velocity --> inflow_z
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0223_inflow_z = np.sum(v0207__inflow_velocity * v0206__z_dir, axis=3)

# op _007v_linear_combination_eval
# LANG: _hub_radius, _rotor_radius --> _007w
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0215__007w = _007v_constant+1*v0201__rotor_radius+-1*v0200__hub_radius

# op _008b_power_combination_eval
# LANG: _008a --> _008c
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0236__008c = (v0235__008a**1)
v0236__008c = (v0236__008c*_008b_coeff).reshape((1, 1))

# op _00lo_indexed_passthrough_eval
# LANG: _00ln --> rotational_speed
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0569_rotational_speed__temp[i_v0568__00ln__00lo_indexed_passthrough_eval] = v0568__00ln.flatten()
v0569_rotational_speed = v0569_rotational_speed__temp.copy()

# op _00mO_tensor_dot_product_eval
# LANG: _y_dir, _inflow_velocity --> _in_plane_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0595__in_plane_inflow_velocity = np.sum(v0580__inflow_velocity * v0578__y_dir, axis=3)

# op _00mQ_tensor_dot_product_eval
# LANG: _z_dir, _inflow_velocity --> inflow_z
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0596_inflow_z = np.sum(v0580__inflow_velocity * v0579__z_dir, axis=3)

# op _00my_linear_combination_eval
# LANG: _hub_radius, _rotor_radius --> _00mz
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0588__00mz = _00my_constant+1*v0574__rotor_radius+-1*v0573__hub_radius

# op _00ne_power_combination_eval
# LANG: _00nd --> _00nf
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0609__00nf = (v0608__00nd**1)
v0609__00nf = (v0609__00nf*_00ne_coeff).reshape((1, 1))

# op _0073 expand_scalar_eval
# LANG: rotational_speed --> _rotational_speed
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0196_rotational_speed = v0196_rotational_speed.reshape((1,))
v0203__rotational_speed = np.empty((1, 40, 30))
v0203__rotational_speed.fill(v0196_rotational_speed.item())
v0196_rotational_speed = v0196_rotational_speed.reshape((1, 1))

# op _007P_power_combination_eval
# LANG: inflow_z --> _007Q
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0224__007Q = (v0223_inflow_z**1)
v0224__007Q = (v0224__007Q*_007P_coeff).reshape((1, 40, 30))

# op _007R_cos_eval
# LANG: _theta --> _007S
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0226__007S = np.cos(v0211__theta)

# op _007V_power_combination_eval
# LANG: _in_plane_inflow_velocity --> _007W
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0228__007W = (v0222__in_plane_inflow_velocity**1)
v0228__007W = (v0228__007W*_007V_coeff).reshape((1, 40, 30))

# op _007X_sin_eval
# LANG: _theta --> _007Y
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0230__007Y = np.sin(v0211__theta)

# op _007x_power_combination_eval
# LANG: _007w, _normalized_radius --> _007y
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0216__007y = (v0215__007w**1)*(v0212__normalized_radius**1)
v0216__007y = (v0216__007y*_007x_coeff).reshape((1, 40, 30))

# op _008d_linear_combination_eval
# LANG: _008c --> temperature
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0237_temperature = _008d_constant+1*v0236__008c

# op _00m6 expand_scalar_eval
# LANG: rotational_speed --> _rotational_speed
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0569_rotational_speed = v0569_rotational_speed.reshape((1,))
v0576__rotational_speed = np.empty((1, 40, 30))
v0576__rotational_speed.fill(v0569_rotational_speed.item())
v0569_rotational_speed = v0569_rotational_speed.reshape((1, 1))

# op _00mA_power_combination_eval
# LANG: _00mz, _normalized_radius --> _00mB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0589__00mB = (v0588__00mz**1)*(v0585__normalized_radius**1)
v0589__00mB = (v0589__00mB*_00mA_coeff).reshape((1, 40, 30))

# op _00mS_power_combination_eval
# LANG: inflow_z --> _00mT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0597__00mT = (v0596_inflow_z**1)
v0597__00mT = (v0597__00mT*_00mS_coeff).reshape((1, 40, 30))

# op _00mU_cos_eval
# LANG: _theta --> _00mV
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0599__00mV = np.cos(v0584__theta)

# op _00mY_power_combination_eval
# LANG: _in_plane_inflow_velocity --> _00mZ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0601__00mZ = (v0595__in_plane_inflow_velocity**1)
v0601__00mZ = (v0601__00mZ*_00mY_coeff).reshape((1, 40, 30))

# op _00m__sin_eval
# LANG: _theta --> _00n0
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0603__00n0 = np.sin(v0584__theta)

# op _00ng_linear_combination_eval
# LANG: _00nf --> temperature
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0610_temperature = _00ng_constant+1*v0609__00nf

# op _007T_power_combination_eval
# LANG: _007Q, _007S --> _007U
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0225__007U = (v0224__007Q**1)*(v0226__007S**1)
v0225__007U = (v0225__007U*_007T_coeff).reshape((1, 40, 30))

# op _007Z_power_combination_eval
# LANG: _007W, _007Y --> _007_
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0229__007_ = (v0228__007W**1)*(v0230__007Y**1)
v0229__007_ = (v0229__007_*_007Z_coeff).reshape((1, 40, 30))

# op _007t_power_combination_eval
# LANG: _rotational_speed --> _angular_speed
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0213__angular_speed = (v0203__rotational_speed**1)
v0213__angular_speed = (v0213__angular_speed*_007t_coeff).reshape((1, 40, 30))

# op _007z_linear_combination_eval
# LANG: _007y, _hub_radius --> _radius
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0214__radius = _007z_constant+1*v0200__hub_radius+1*v0216__007y

# op _008f_power_combination_eval
# LANG: temperature --> _008g
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0238__008g = (v0237_temperature**1)
v0238__008g = (v0238__008g*_008f_coeff).reshape((1, 1))

# op _00mC_linear_combination_eval
# LANG: _00mB, _hub_radius --> _radius
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0587__radius = _00mC_constant+1*v0573__hub_radius+1*v0589__00mB

# op _00mW_power_combination_eval
# LANG: _00mT, _00mV --> _00mX
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0598__00mX = (v0597__00mT**1)*(v0599__00mV**1)
v0598__00mX = (v0598__00mX*_00mW_coeff).reshape((1, 40, 30))

# op _00mw_power_combination_eval
# LANG: _rotational_speed --> _angular_speed
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0586__angular_speed = (v0576__rotational_speed**1)
v0586__angular_speed = (v0586__angular_speed*_00mw_coeff).reshape((1, 40, 30))

# op _00n1_power_combination_eval
# LANG: _00mZ, _00n0 --> _00n2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0602__00n2 = (v0601__00mZ**1)*(v0603__00n0**1)
v0602__00n2 = (v0602__00n2*_00n1_coeff).reshape((1, 40, 30))

# op _00ni_power_combination_eval
# LANG: temperature --> _00nj
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0611__00nj = (v0610_temperature**1)
v0611__00nj = (v0611__00nj*_00ni_coeff).reshape((1, 1))

# op _000M_sparsematmat_eval
# LANG: design_geometry --> _000N
# SHAPES: (32500, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v023__000N = _000M_sparsematmat_eval_mat@v05_design_geometry

# op _000s_sparsematmat_eval
# LANG: design_geometry --> _000t
# SHAPES: (32500, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v013__000t = _000s_sparsematmat_eval_mat@v05_design_geometry

# op _0075 expand_array_eval
# LANG: x_dir --> _x_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0204__x_dir = np.einsum('ad,bc->abcd', v0197_x_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _0080_linear_combination_eval
# LANG: _007U, _007_ --> _0081
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0227__0081 = _0080_constant+1*v0225__007U+1*v0229__007_

# op _0082_power_combination_eval
# LANG: _angular_speed, _radius --> _0083
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0232__0083 = (v0214__radius**1)*(v0213__angular_speed**1)
v0232__0083 = (v0232__0083*_0082_coeff).reshape((1, 40, 30))

# op _008h_power_combination_eval
# LANG: _008g --> _008i
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0239__008i = (v0238__008g**5.258643795229161)
v0239__008i = (v0239__008i*_008h_coeff).reshape((1, 1))

# op _00m8 expand_array_eval
# LANG: x_dir --> _x_dir
# SHAPES: (1, 3) --> (1, 40, 30, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0577__x_dir = np.einsum('ad,bc->abcd', v0570_x_dir.reshape((1, 3)) ,np.ones((40, 30))).reshape((1, 40, 30, 3))

# op _00n3_linear_combination_eval
# LANG: _00mX, _00n2 --> _00n4
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0600__00n4 = _00n3_constant+1*v0598__00mX+1*v0602__00n2

# op _00n5_power_combination_eval
# LANG: _angular_speed, _radius --> _00n6
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0605__00n6 = (v0587__radius**1)*(v0586__angular_speed**1)
v0605__00n6 = (v0605__00n6*_00n5_coeff).reshape((1, 40, 30))

# op _00nk_power_combination_eval
# LANG: _00nj --> _00nl
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0612__00nl = (v0611__00nj**5.258643795229161)
v0612__00nl = (v0612__00nl*_00nk_coeff).reshape((1, 1))

# op _000O reshape_eval
# LANG: _000N --> rotor_2_blade_chord_length
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v024_rotor_2_blade_chord_length = v023__000N.reshape((40, 3))

# op _000Q_sparsematmat_eval
# LANG: design_geometry --> _000R
# SHAPES: (32500, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v025__000R = _000Q_sparsematmat_eval_mat@v05_design_geometry

# op _000u reshape_eval
# LANG: _000t --> rotor_1_blade_chord_length
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v014_rotor_1_blade_chord_length = v013__000t.reshape((40, 3))

# op _000w_sparsematmat_eval
# LANG: design_geometry --> _000x
# SHAPES: (32500, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v015__000x = _000w_sparsematmat_eval_mat@v05_design_geometry

# op _007J_tensor_dot_product_eval
# LANG: _x_dir, _inflow_velocity --> _axial_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0221__axial_inflow_velocity = np.sum(v0207__inflow_velocity * v0204__x_dir, axis=3)

# op _0084_linear_combination_eval
# LANG: _0081, _0083 --> _tangential_inflow_velocity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0231__tangential_inflow_velocity = _0084_constant+1*v0227__0081+1*v0232__0083

# op _008j_power_combination_eval
# LANG: _008i --> pressure
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0240_pressure = (v0239__008i**1)
v0240_pressure = (v0240_pressure*_008j_coeff).reshape((1, 1))

# op _008p_power_combination_eval
# LANG: temperature --> _008q
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0243__008q = (v0237_temperature**1)
v0243__008q = (v0243__008q*_008p_coeff).reshape((1, 1))

# op _00mM_tensor_dot_product_eval
# LANG: _x_dir, _inflow_velocity --> _axial_inflow_velocity
# SHAPES: (1, 40, 30, 3), (1, 40, 30, 3) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0594__axial_inflow_velocity = np.sum(v0580__inflow_velocity * v0577__x_dir, axis=3)

# op _00n7_linear_combination_eval
# LANG: _00n4, _00n6 --> _tangential_inflow_velocity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0604__tangential_inflow_velocity = _00n7_constant+1*v0600__00n4+1*v0605__00n6

# op _00nm_power_combination_eval
# LANG: _00nl --> pressure
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0613_pressure = (v0612__00nl**1)
v0613_pressure = (v0613_pressure*_00nm_coeff).reshape((1, 1))

# op _00ns_power_combination_eval
# LANG: temperature --> _00nt
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0616__00nt = (v0610_temperature**1)
v0616__00nt = (v0616__00nt*_00ns_coeff).reshape((1, 1))

# op _000S reshape_eval
# LANG: _000R --> rotor_2_blade_twist
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v026_rotor_2_blade_twist = v025__000R.reshape((40, 3))

# op _000y reshape_eval
# LANG: _000x --> rotor_1_blade_twist
# SHAPES: (40, 3) --> (40, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v016_rotor_1_blade_twist = v015__000x.reshape((40, 3))

# op _003Q pnorm_axis_eval
# LANG: rotor_2_blade_chord_length --> _003R
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0114__003R = np.sum(v024_rotor_2_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _004w_power_combination_eval
# LANG: _axial_inflow_velocity --> _004x
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0132__004x = (v0221__axial_inflow_velocity**2)
v0132__004x = (v0132__004x*_004w_coeff).reshape((1, 40, 30))

# op _004y_power_combination_eval
# LANG: _tangential_inflow_velocity --> _004z
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0134__004z = (v0231__tangential_inflow_velocity**2)
v0134__004z = (v0134__004z*_004y_coeff).reshape((1, 40, 30))

# op _008l_power_combination_eval
# LANG: pressure --> _008m
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0241__008m = (v0240_pressure**1)
v0241__008m = (v0241__008m*_008l_coeff).reshape((1, 1))

# op _008r_power_combination_eval
# LANG: _008q --> _008s
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0244__008s = (v0243__008q**1.5)
v0244__008s = (v0244__008s*_008r_coeff).reshape((1, 1))

# op _00iT pnorm_axis_eval
# LANG: rotor_1_blade_chord_length --> _00iU
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0487__00iU = np.sum(v014_rotor_1_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00jB_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00jC
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0507__00jC = (v0604__tangential_inflow_velocity**2)
v0507__00jC = (v0507__00jC*_00jB_coeff).reshape((1, 40, 30))

# op _00jz_power_combination_eval
# LANG: _axial_inflow_velocity --> _00jA
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0505__00jA = (v0594__axial_inflow_velocity**2)
v0505__00jA = (v0505__00jA*_00jz_coeff).reshape((1, 40, 30))

# op _00no_power_combination_eval
# LANG: pressure --> _00np
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0614__00np = (v0613_pressure**1)
v0614__00np = (v0614__00np*_00no_coeff).reshape((1, 1))

# op _00nu_power_combination_eval
# LANG: _00nt --> _00nv
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0617__00nv = (v0616__00nt**1.5)
v0617__00nv = (v0617__00nv*_00nu_coeff).reshape((1, 1))

# op _003S reshape_eval
# LANG: _003R --> chord_profile
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0115_chord_profile = v0114__003R.reshape((40, 1))

# op _003V_single_tensor_sum_with_axis_eval
# LANG: rotor_2_blade_twist --> _003W
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0116__003W = np.sum(v026_rotor_2_blade_twist, axis = (1,)).reshape((40,))

# op _004A_linear_combination_eval
# LANG: _004x, _004z --> _004B
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0133__004B = _004A_constant+1*v0132__004x+1*v0134__004z

# op _008n_power_combination_eval
# LANG: temperature, _008m --> density
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0242_density = (v0241__008m**1)*(v0237_temperature**-1)
v0242_density = (v0242_density*_008n_coeff).reshape((1, 1))

# op _008t_power_combination_eval
# LANG: _008s --> _008u
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0245__008u = (v0244__008s**1)
v0245__008u = (v0245__008u*_008t_coeff).reshape((1, 1))

# op _00iV reshape_eval
# LANG: _00iU --> chord_profile
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0488_chord_profile = v0487__00iU.reshape((40, 1))

# op _00iY_single_tensor_sum_with_axis_eval
# LANG: rotor_1_blade_twist --> _00iZ
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0489__00iZ = np.sum(v016_rotor_1_blade_twist, axis = (1,)).reshape((40,))

# op _00jD_linear_combination_eval
# LANG: _00jA, _00jC --> _00jE
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0506__00jE = _00jD_constant+1*v0505__00jA+1*v0507__00jC

# op _00nq_power_combination_eval
# LANG: temperature, _00np --> density
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0615_density = (v0614__00np**1)*(v0610_temperature**-1)
v0615_density = (v0615_density*_00nq_coeff).reshape((1, 1))

# op _00nw_power_combination_eval
# LANG: _00nv --> _00nx
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0618__00nx = (v0617__00nv**1)
v0618__00nx = (v0618__00nx*_00nw_coeff).reshape((1, 1))

# op _003X reshape_eval
# LANG: _003W --> _003Y
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0117__003Y = v0116__003W.reshape((40, 1))

# op _004C_power_combination_eval
# LANG: _004B --> _004D
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0135__004D = (v0133__004B**0.5)
v0135__004D = (v0135__004D*_004C_coeff).reshape((1, 40, 30))

# op _004F expand_scalar_eval
# LANG: density --> _004G
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0242_density = v0242_density.reshape((1,))
v0130__004G = np.empty((1, 40, 30))
v0130__004G.fill(v0242_density.item())
v0242_density = v0242_density.reshape((1, 1))

# op _007f expand_array_eval
# LANG: chord_profile --> _chord
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0115_chord_profile = v0115_chord_profile.reshape((40,))
v0209__chord = np.einsum('b,ac->abc', v0115_chord_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v0115_chord_profile = v0115_chord_profile.reshape((40, 1))

# op _008B_power_combination_eval
# LANG: temperature --> _008C
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0249__008C = (v0237_temperature**1)
v0249__008C = (v0249__008C*_008B_coeff).reshape((1, 1))

# op _008v_power_combination_eval
# LANG: _008u --> _008w
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0246__008w = (v0245__008u**1)
v0246__008w = (v0246__008w*_008v_coeff).reshape((1, 1))

# op _008x_linear_combination_eval
# LANG: temperature --> _008y
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0248__008y = _008x_constant+1*v0237_temperature

# op _00i_ reshape_eval
# LANG: _00iZ --> _00j0
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0490__00j0 = v0489__00iZ.reshape((40, 1))

# op _00jF_power_combination_eval
# LANG: _00jE --> _00jG
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0508__00jG = (v0506__00jE**0.5)
v0508__00jG = (v0508__00jG*_00jF_coeff).reshape((1, 40, 30))

# op _00jI expand_scalar_eval
# LANG: density --> _00jJ
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0615_density = v0615_density.reshape((1,))
v0503__00jJ = np.empty((1, 40, 30))
v0503__00jJ.fill(v0615_density.item())
v0615_density = v0615_density.reshape((1, 1))

# op _00mi expand_array_eval
# LANG: chord_profile --> _chord
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0488_chord_profile = v0488_chord_profile.reshape((40,))
v0582__chord = np.einsum('b,ac->abc', v0488_chord_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v0488_chord_profile = v0488_chord_profile.reshape((40, 1))

# op _00nA_linear_combination_eval
# LANG: temperature --> _00nB
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0621__00nB = _00nA_constant+1*v0610_temperature

# op _00nE_power_combination_eval
# LANG: temperature --> _00nF
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0622__00nF = (v0610_temperature**1)
v0622__00nF = (v0622__00nF*_00nE_coeff).reshape((1, 1))

# op _00ny_power_combination_eval
# LANG: _00nx --> _00nz
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0619__00nz = (v0618__00nx**1)
v0619__00nz = (v0619__00nz*_00ny_coeff).reshape((1, 1))

# op _003Z_power_combination_eval
# LANG: chord_profile, _003Y --> _003_
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0118__003_ = (v0117__003Y**1)*(v0115_chord_profile**-1)
v0118__003_ = (v0118__003_*_003Z_coeff).reshape((40, 1))

# op _004N_power_combination_eval
# LANG: _004G, _004D --> _004O
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0131__004O = (v0130__004G**1)*(v0135__004D**1)
v0131__004O = (v0131__004O*_004N_coeff).reshape((1, 40, 30))

# op _007B_power_combination_eval
# LANG: _chord --> _007C
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0217__007C = (v0209__chord**1)
v0217__007C = (v0217__007C*_007B_coeff).reshape((1, 40, 30))

# op _008D_power_combination_eval
# LANG: _008C --> speed_of_sound
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0250_speed_of_sound = (v0249__008C**0.5)
v0250_speed_of_sound = (v0250_speed_of_sound*_008D_coeff).reshape((1, 1))

# op _008z_power_combination_eval
# LANG: _008w, _008y --> dynamic_viscosity
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.atmosphere_model
v0247_dynamic_viscosity = (v0246__008w**1)*(v0248__008y**-1)
v0247_dynamic_viscosity = (v0247_dynamic_viscosity*_008z_coeff).reshape((1, 1))

# op _00j1_power_combination_eval
# LANG: chord_profile, _00j0 --> _00j2
# SHAPES: (40, 1), (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0491__00j2 = (v0490__00j0**1)*(v0488_chord_profile**-1)
v0491__00j2 = (v0491__00j2*_00j1_coeff).reshape((40, 1))

# op _00jQ_power_combination_eval
# LANG: _00jJ, _00jG --> _00jR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0504__00jR = (v0503__00jJ**1)*(v0508__00jG**1)
v0504__00jR = (v0504__00jR*_00jQ_coeff).reshape((1, 40, 30))

# op _00mE_power_combination_eval
# LANG: _chord --> _00mF
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0590__00mF = (v0582__chord**1)
v0590__00mF = (v0590__00mF*_00mE_coeff).reshape((1, 40, 30))

# op _00nC_power_combination_eval
# LANG: _00nz, _00nB --> dynamic_viscosity
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0620_dynamic_viscosity = (v0619__00nz**1)*(v0621__00nB**-1)
v0620_dynamic_viscosity = (v0620_dynamic_viscosity*_00nC_coeff).reshape((1, 1))

# op _00nG_power_combination_eval
# LANG: _00nF --> speed_of_sound
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.atmosphere_model
v0623_speed_of_sound = (v0622__00nF**0.5)
v0623_speed_of_sound = (v0623_speed_of_sound*_00nG_coeff).reshape((1, 1))

# op _0040_arcsin_eval
# LANG: _003_ --> _0041
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0119__0041 = np.arcsin(v0118__003_)

# op _004I expand_scalar_eval
# LANG: dynamic_viscosity --> _004J
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0247_dynamic_viscosity = v0247_dynamic_viscosity.reshape((1,))
v0138__004J = np.empty((1, 40, 30))
v0138__004J.fill(v0247_dynamic_viscosity.item())
v0247_dynamic_viscosity = v0247_dynamic_viscosity.reshape((1, 1))

# op _004L expand_scalar_eval
# LANG: speed_of_sound --> _004M
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0250_speed_of_sound = v0250_speed_of_sound.reshape((1,))
v0140__004M = np.empty((1, 40, 30))
v0140__004M.fill(v0250_speed_of_sound.item())
v0250_speed_of_sound = v0250_speed_of_sound.reshape((1, 1))

# op _004P_power_combination_eval
# LANG: _004O, _chord --> _004Q
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0136__004Q = (v0131__004O**1)*(v0209__chord**1)
v0136__004Q = (v0136__004Q*_004P_coeff).reshape((1, 40, 30))

# op _007D_power_combination_eval
# LANG: _007C --> _007E
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0218__007E = (v0217__007C**1)
v0218__007E = (v0218__007E*_007D_coeff).reshape((1, 40, 30))

# op _00j3_arcsin_eval
# LANG: _00j2 --> _00j4
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0492__00j4 = np.arcsin(v0491__00j2)

# op _00jL expand_scalar_eval
# LANG: dynamic_viscosity --> _00jM
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0620_dynamic_viscosity = v0620_dynamic_viscosity.reshape((1,))
v0511__00jM = np.empty((1, 40, 30))
v0511__00jM.fill(v0620_dynamic_viscosity.item())
v0620_dynamic_viscosity = v0620_dynamic_viscosity.reshape((1, 1))

# op _00jO expand_scalar_eval
# LANG: speed_of_sound --> _00jP
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0623_speed_of_sound = v0623_speed_of_sound.reshape((1,))
v0513__00jP = np.empty((1, 40, 30))
v0513__00jP.fill(v0623_speed_of_sound.item())
v0623_speed_of_sound = v0623_speed_of_sound.reshape((1, 1))

# op _00jS_power_combination_eval
# LANG: _00jR, _chord --> _00jT
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0509__00jT = (v0504__00jR**1)*(v0582__chord**1)
v0509__00jT = (v0509__00jT*_00jS_coeff).reshape((1, 40, 30))

# op _00mG_power_combination_eval
# LANG: _00mF --> _00mH
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0591__00mH = (v0590__00mF**1)
v0591__00mH = (v0591__00mH*_00mG_coeff).reshape((1, 40, 30))

# op _0042_linear_combination_eval
# LANG: _0041 --> twist_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0120_twist_profile = _0042_constant+1*v0119__0041

# op _004R_power_combination_eval
# LANG: _004Q, _004J --> Re
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0137_Re = (v0136__004Q**1)*(v0138__004J**-1)
v0137_Re = (v0137_Re*_004R_coeff).reshape((1, 40, 30))

# op _004T_power_combination_eval
# LANG: _004D, _004M --> mach_number
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0139_mach_number = (v0135__004D**1)*(v0140__004M**-1)
v0139_mach_number = (v0139_mach_number*_004T_coeff).reshape((1, 40, 30))

# op _007F_power_combination_eval
# LANG: _007E --> _007G
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0219__007G = (v0218__007E**1)
v0219__007G = (v0219__007G*_007F_coeff).reshape((1, 40, 30))

# op _00j5_linear_combination_eval
# LANG: _00j4 --> twist_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0493_twist_profile = _00j5_constant+1*v0492__00j4

# op _00jU_power_combination_eval
# LANG: _00jT, _00jM --> Re
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0510_Re = (v0509__00jT**1)*(v0511__00jM**-1)
v0510_Re = (v0510_Re*_00jU_coeff).reshape((1, 40, 30))

# op _00jW_power_combination_eval
# LANG: _00jG, _00jP --> mach_number
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0512_mach_number = (v0508__00jG**1)*(v0513__00jP**-1)
v0512_mach_number = (v0512_mach_number*_00jW_coeff).reshape((1, 40, 30))

# op _00mI_power_combination_eval
# LANG: _00mH --> _00mJ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0592__00mJ = (v0591__00mH**1)
v0592__00mJ = (v0592__00mJ*_00mI_coeff).reshape((1, 40, 30))

# op _004V reshape_eval
# LANG: Re --> Re_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0141_Re_ml_input = v0137_Re.reshape((1200, 1))

# op _004X reshape_eval
# LANG: mach_number --> mach_number_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0142_mach_number_ml_input = v0139_mach_number.reshape((1200, 1))

# op _007H_power_combination_eval
# LANG: _radius, _007G --> _blade_solidity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_pre_process_model
v0220__blade_solidity = (v0219__007G**1)*(v0214__radius**-1)
v0220__blade_solidity = (v0220__blade_solidity*_007H_coeff).reshape((1, 40, 30))

# op _007d expand_array_eval
# LANG: twist_profile --> _pitch
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0120_twist_profile = v0120_twist_profile.reshape((40,))
v0208__pitch = np.einsum('b,ac->abc', v0120_twist_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v0120_twist_profile = v0120_twist_profile.reshape((40, 1))

# op _00jY reshape_eval
# LANG: Re --> Re_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0514_Re_ml_input = v0510_Re.reshape((1200, 1))

# op _00j_ reshape_eval
# LANG: mach_number --> mach_number_ml_input
# SHAPES: (1, 40, 30) --> (1200, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0515_mach_number_ml_input = v0512_mach_number.reshape((1200, 1))

# op _00mK_power_combination_eval
# LANG: _radius, _00mJ --> _blade_solidity
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_pre_process_model
v0593__blade_solidity = (v0592__00mJ**1)*(v0587__radius**-1)
v0593__blade_solidity = (v0593__blade_solidity*_00mK_coeff).reshape((1, 40, 30))

# op _00mg expand_array_eval
# LANG: twist_profile --> _pitch
# SHAPES: (40,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0493_twist_profile = v0493_twist_profile.reshape((40,))
v0581__pitch = np.einsum('b,ac->abc', v0493_twist_profile.reshape((40,)) ,np.ones((1, 30))).reshape((1, 40, 30))
v0493_twist_profile = v0493_twist_profile.reshape((40, 1))

# op _00aU_bracketed_implict_eval
# LANG: Re_ml_input, mach_number_ml_input, X_min, X_max, control_points, _hub_radius, _rotor_radius, _pitch, _radius, _blade_solidity, _axial_inflow_velocity, _tangential_inflow_velocity --> phi_distribution, alpha_ml_input, Cd, Cl
# SHAPES: (1200, 1), (1200, 1), (1200, 35), (1200, 35), (1200, 32), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30) --> (1, 40, 30), (1200, 1), (1200,), (1200,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.phi_bracketed_search_group
_00aU_bracketed.set_guess(initial_guess_v0251_phi_distribution)
_00aU_bracketed_out = _00aU_bracketed.solve(v0220__blade_solidity, v0221__axial_inflow_velocity, v0231__tangential_inflow_velocity, v0214__radius, v0201__rotor_radius, v0200__hub_radius, v0208__pitch, v0141_Re_ml_input, v0142_mach_number_ml_input, v0160_X_max, v0159_X_min, v0161_control_points)
v0251_phi_distribution = _00aU_bracketed_out[0]
v0252_alpha_ml_input = _00aU_bracketed_out[1]
v0253_Cd = _00aU_bracketed_out[2]
v0254_Cl = _00aU_bracketed_out[3]

# op _00pX_bracketed_implict_eval
# LANG: Re_ml_input, mach_number_ml_input, X_min, X_max, control_points, _hub_radius, _rotor_radius, _pitch, _radius, _blade_solidity, _axial_inflow_velocity, _tangential_inflow_velocity --> phi_distribution, alpha_ml_input, Cd, Cl
# SHAPES: (1200, 1), (1200, 1), (1200, 35), (1200, 35), (1200, 32), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30), (1, 40, 30) --> (1, 40, 30), (1200, 1), (1200,), (1200,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.phi_bracketed_search_group
_00pX_bracketed.set_guess(initial_guess_v0624_phi_distribution)
_00pX_bracketed_out = _00pX_bracketed.solve(v0593__blade_solidity, v0594__axial_inflow_velocity, v0604__tangential_inflow_velocity, v0587__radius, v0574__rotor_radius, v0573__hub_radius, v0581__pitch, v0514_Re_ml_input, v0515_mach_number_ml_input, v0533_X_max, v0532_X_min, v0534_control_points)
v0624_phi_distribution = _00pX_bracketed_out[0]
v0625_alpha_ml_input = _00pX_bracketed_out[1]
v0626_Cd = _00pX_bracketed_out[2]
v0627_Cl = _00pX_bracketed_out[3]

# op _00b2_linear_combination_eval
# LANG: _rotor_radius, _radius --> _00b3
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0255__00b3 = _00b2_constant+1*v0201__rotor_radius+-1*v0214__radius

# op _00bc_linear_combination_eval
# LANG: _hub_radius, _radius --> _00bd
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0265__00bd = _00bc_constant+1*v0214__radius+-1*v0200__hub_radius

# op _00q5_linear_combination_eval
# LANG: _rotor_radius, _radius --> _00q6
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0628__00q6 = _00q5_constant+1*v0574__rotor_radius+-1*v0587__radius

# op _00qf_linear_combination_eval
# LANG: _hub_radius, _radius --> _00qg
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0638__00qg = _00qf_constant+1*v0587__radius+-1*v0573__hub_radius

# op _00B9_power_combination_eval
# LANG: rpm --> _00Ba
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0531_rpm = v0531_rpm.reshape((1,))
v0982__00Ba = (v0531_rpm**1)
v0982__00Ba = (v0982__00Ba*_00B9_coeff).reshape((1,))
v0531_rpm = v0531_rpm.reshape((1, 1))

# op _00SP_power_combination_eval
# LANG: rpm --> _00SQ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v0158_rpm = v0158_rpm.reshape((1,))
v01528__00SQ = (v0158_rpm**1)
v01528__00SQ = (v01528__00SQ*_00SP_coeff).reshape((1,))
v0158_rpm = v0158_rpm.reshape((1, 1))

# op _00b4_power_combination_eval
# LANG: _00b3 --> _00b5
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0256__00b5 = (v0255__00b3**1)
v0256__00b5 = (v0256__00b5*_00b4_coeff).reshape((1, 40, 30))

# op _00be_power_combination_eval
# LANG: _00bd --> _00bf
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0266__00bf = (v0265__00bd**1)
v0266__00bf = (v0266__00bf*_00be_coeff).reshape((1, 40, 30))

# op _00q7_power_combination_eval
# LANG: _00q6 --> _00q8
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0629__00q8 = (v0628__00q6**1)
v0629__00q8 = (v0629__00q8*_00q7_coeff).reshape((1, 40, 30))

# op _00qh_power_combination_eval
# LANG: _00qg --> _00qi
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0639__00qi = (v0638__00qg**1)
v0639__00qi = (v0639__00qi*_00qh_coeff).reshape((1, 40, 30))

# op _00Bb_power_combination_eval
# LANG: _00Ba --> _00Bc
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0983__00Bc = (v0982__00Ba**1)
v0983__00Bc = (v0983__00Bc*_00Bb_coeff).reshape((1,))

# op _00P4_power_combination_eval
# LANG: rotor_2_disk_in_plane_1 --> _00P5
# SHAPES: (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v018_rotor_2_disk_in_plane_1 = v018_rotor_2_disk_in_plane_1.reshape((3,))
v01396__00P5 = (v018_rotor_2_disk_in_plane_1**1)
v01396__00P5 = (v01396__00P5*_00P4_coeff).reshape((3,))
v018_rotor_2_disk_in_plane_1 = v018_rotor_2_disk_in_plane_1.reshape((1, 3))

# op _00SR_power_combination_eval
# LANG: _00SQ --> _00SS
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01529__00SS = (v01528__00SQ**1)
v01529__00SS = (v01529__00SS*_00SR_coeff).reshape((1,))

# op _00b6_power_combination_eval
# LANG: _00b5, _radius --> _00b7
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0257__00b7 = (v0256__00b5**1)*(v0214__radius**-1)
v0257__00b7 = (v0257__00b7*_00b6_coeff).reshape((1, 40, 30))

# op _00b8_sin_eval
# LANG: phi_distribution --> _00b9
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0259__00b9 = np.sin(v0251_phi_distribution)

# op _00bg_power_combination_eval
# LANG: _00bf, _hub_radius --> _00bh
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0267__00bh = (v0266__00bf**1)*(v0200__hub_radius**-1)
v0267__00bh = (v0267__00bh*_00bg_coeff).reshape((1, 40, 30))

# op _00bi_sin_eval
# LANG: phi_distribution --> _00bj
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0269__00bj = np.sin(v0251_phi_distribution)

# op _00q9_power_combination_eval
# LANG: _00q8, _radius --> _00qa
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0630__00qa = (v0629__00q8**1)*(v0587__radius**-1)
v0630__00qa = (v0630__00qa*_00q9_coeff).reshape((1, 40, 30))

# op _00qb_sin_eval
# LANG: phi_distribution --> _00qc
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0632__00qc = np.sin(v0624_phi_distribution)

# op _00qj_power_combination_eval
# LANG: _00qi, _hub_radius --> _00qk
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0640__00qk = (v0639__00qi**1)*(v0573__hub_radius**-1)
v0640__00qk = (v0640__00qk*_00qj_coeff).reshape((1, 40, 30))

# op _00ql_sin_eval
# LANG: phi_distribution --> _00qm
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0642__00qm = np.sin(v0624_phi_distribution)

# op _00xp_power_combination_eval
# LANG: rotor_1_disk_in_plane_1 --> _00xq
# SHAPES: (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v08_rotor_1_disk_in_plane_1 = v08_rotor_1_disk_in_plane_1.reshape((3,))
v0850__00xq = (v08_rotor_1_disk_in_plane_1**1)
v0850__00xq = (v0850__00xq*_00xp_coeff).reshape((3,))
v08_rotor_1_disk_in_plane_1 = v08_rotor_1_disk_in_plane_1.reshape((1, 3))

# op _00Bd_power_combination_eval
# LANG: _00Bc --> _00Be
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0984__00Be = (v0983__00Bc**1)
v0984__00Be = (v0984__00Be*_00Bd_coeff).reshape((1,))

# op _00P9 pnorm_eval
# LANG: _00P5 --> _00Pa
# SHAPES: (3,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01397__00Pa = np.linalg.norm(v01396__00P5.flatten(), ord=2)

# op _00Pe pnorm_axis_eval
# LANG: rotor_2_blade_chord_length --> _00Pf
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01399__00Pf = np.sum(v024_rotor_2_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00ST_power_combination_eval
# LANG: _00SS --> _00SU
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01530__00SU = (v01529__00SS**1)
v01530__00SU = (v01530__00SU*_00ST_coeff).reshape((1,))

# op _00ba_power_combination_eval
# LANG: _00b7, _00b9 --> _00bb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0258__00bb = (v0257__00b7**1)*(v0259__00b9**-1)
v0258__00bb = (v0258__00bb*_00ba_coeff).reshape((1, 40, 30))

# op _00bk_power_combination_eval
# LANG: _00bh, _00bj --> _00bl
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0268__00bl = (v0267__00bh**1)*(v0269__00bj**-1)
v0268__00bl = (v0268__00bl*_00bk_coeff).reshape((1, 40, 30))

# op _00qd_power_combination_eval
# LANG: _00qa, _00qc --> _00qe
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0631__00qe = (v0630__00qa**1)*(v0632__00qc**-1)
v0631__00qe = (v0631__00qe*_00qd_coeff).reshape((1, 40, 30))

# op _00qn_power_combination_eval
# LANG: _00qk, _00qm --> _00qo
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0641__00qo = (v0640__00qk**1)*(v0642__00qm**-1)
v0641__00qo = (v0641__00qo*_00qn_coeff).reshape((1, 40, 30))

# op _00xu pnorm_eval
# LANG: _00xq --> _00xv
# SHAPES: (3,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0851__00xv = np.linalg.norm(v0850__00xq.flatten(), ord=2)

# op _00xz pnorm_axis_eval
# LANG: rotor_1_blade_chord_length --> _00xA
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0853__00xA = np.sum(v014_rotor_1_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00BE expand_array_eval
# LANG: nondim_sectional_radius --> _00BF
# SHAPES: (40,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0974__00BF = np.einsum('d,abce->abcde', v0973_nondim_sectional_radius.reshape((40,)) ,np.ones((1, 27, 3, 11))).reshape((1, 27, 3, 40, 11))

# op _00BG expand_scalar_eval
# LANG: _00Be --> _00BH
# SHAPES: (1,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0985__00BH = np.empty((1, 27, 3, 40, 11))
v0985__00BH.fill(v0984__00Be.item())

# op _00Pb_power_combination_eval
# LANG: _00Pa --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01398_propeller_radius = (v01397__00Pa**1)
v01398_propeller_radius = (v01398_propeller_radius*_00Pb_coeff).reshape((1,))

# op _00Pg reshape_eval
# LANG: _00Pf --> _00Ph
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01400__00Ph = v01399__00Pf.reshape((40, 1))

# op _00Tj expand_array_eval
# LANG: nondim_sectional_radius --> _00Tk
# SHAPES: (40,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01520__00Tk = np.einsum('d,abce->abcde', v01519_nondim_sectional_radius.reshape((40,)) ,np.ones((1, 27, 3, 11))).reshape((1, 27, 3, 40, 11))

# op _00Tl expand_scalar_eval
# LANG: _00SU --> _00Tm
# SHAPES: (1,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01531__00Tm = np.empty((1, 27, 3, 40, 11))
v01531__00Tm.fill(v01530__00SU.item())

# op _00bm_linear_combination_eval
# LANG: _00bb --> _00bn
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0260__00bn = _00bm_constant+-1*v0258__00bb

# op _00bu_linear_combination_eval
# LANG: _00bl --> _00bv
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0270__00bv = _00bu_constant+-1*v0268__00bl

# op _00qp_linear_combination_eval
# LANG: _00qe --> _00qq
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0633__00qq = _00qp_constant+-1*v0631__00qe

# op _00qx_linear_combination_eval
# LANG: _00qo --> _00qy
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0643__00qy = _00qx_constant+-1*v0641__00qo

# op _00xB reshape_eval
# LANG: _00xA --> _00xC
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0854__00xC = v0853__00xA.reshape((40, 1))

# op _00xw_power_combination_eval
# LANG: _00xv --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0852_propeller_radius = (v0851__00xv**1)
v0852_propeller_radius = (v0852_propeller_radius*_00xw_coeff).reshape((1,))

# op _00BI expand_scalar_eval
# LANG: propeller_radius --> _00BJ
# SHAPES: (1,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0994__00BJ = np.empty((1, 27, 3, 40, 11))
v0994__00BJ.fill(v0852_propeller_radius.item())

# op _00BS_decompose_eval
# LANG: _00BF --> _00BT
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0992__00BT = ((v0974__00BF.flatten())[src_indices__00BT__00BS]).reshape((1, 27, 3, 40, 10))

# op _00BU_decompose_eval
# LANG: _00BH --> _00BV
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0986__00BV = ((v0985__00BH.flatten())[src_indices__00BV__00BU]).reshape((1, 27, 3, 40, 10))

# op _00Pi_power_combination_eval
# LANG: _00Ph --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01401_chord_profile = (v01400__00Ph**1)
v01401_chord_profile = (v01401_chord_profile*_00Pi_coeff).reshape((40, 1))

# op _00Tn expand_scalar_eval
# LANG: propeller_radius --> _00To
# SHAPES: (1,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01540__00To = np.empty((1, 27, 3, 40, 11))
v01540__00To.fill(v01398_propeller_radius.item())

# op _00Tx_decompose_eval
# LANG: _00Tk --> _00Ty
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01538__00Ty = ((v01520__00Tk.flatten())[src_indices__00Ty__00Tx]).reshape((1, 27, 3, 40, 10))

# op _00Tz_decompose_eval
# LANG: _00Tm --> _00TA
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01532__00TA = ((v01531__00Tm.flatten())[src_indices__00TA__00Tz]).reshape((1, 27, 3, 40, 10))

# op _00bo exp_eval
# LANG: _00bn --> _00bp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0261__00bp = np.exp(v0260__00bn)

# op _00bw exp_eval
# LANG: _00bv --> _00bx
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0271__00bx = np.exp(v0270__00bv)

# op _00qr exp_eval
# LANG: _00qq --> _00qs
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0634__00qs = np.exp(v0633__00qq)

# op _00qz exp_eval
# LANG: _00qy --> _00qA
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0644__00qA = np.exp(v0643__00qy)

# op _00xD_power_combination_eval
# LANG: _00xC --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0855_chord_profile = (v0854__00xC**1)
v0855_chord_profile = (v0855_chord_profile*_00xD_coeff).reshape((40, 1))

# op _00BM expand_array_eval
# LANG: chord_profile --> _00BN
# SHAPES: (40,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0855_chord_profile = v0855_chord_profile.reshape((40,))
v0988__00BN = np.einsum('d,abce->abcde', v0855_chord_profile.reshape((40,)) ,np.ones((1, 27, 3, 11))).reshape((1, 27, 3, 40, 11))
v0855_chord_profile = v0855_chord_profile.reshape((40, 1))

# op _00BW_decompose_eval
# LANG: _00BJ --> _00BX
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0995__00BX = ((v0994__00BJ.flatten())[src_indices__00BX__00BW]).reshape((1, 27, 3, 40, 10))

# op _00Cw_decompose_eval
# LANG: lam_var --> _00Cx
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0980__00Cx = ((v0979_lam_var.flatten())[src_indices__00Cx__00Cw]).reshape((1, 27, 3, 40, 10))

# op _00Cy_power_combination_eval
# LANG: _00BV, _00BT --> _00Cz
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0991__00Cz = (v0986__00BV**1)*(v0992__00BT**1)
v0991__00Cz = (v0991__00Cz*_00Cy_coeff).reshape((1, 27, 3, 40, 10))

# op _00TB_decompose_eval
# LANG: _00To --> _00TC
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01541__00TC = ((v01540__00To.flatten())[src_indices__00TC__00TB]).reshape((1, 27, 3, 40, 10))

# op _00Tr expand_array_eval
# LANG: chord_profile --> _00Ts
# SHAPES: (40,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01401_chord_profile = v01401_chord_profile.reshape((40,))
v01534__00Ts = np.einsum('d,abce->abcde', v01401_chord_profile.reshape((40,)) ,np.ones((1, 27, 3, 11))).reshape((1, 27, 3, 40, 11))
v01401_chord_profile = v01401_chord_profile.reshape((40, 1))

# op _00Ub_decompose_eval
# LANG: lam_var --> _00Uc
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01526__00Uc = ((v01525_lam_var.flatten())[src_indices__00Uc__00Ub]).reshape((1, 27, 3, 40, 10))

# op _00Ud_power_combination_eval
# LANG: _00TA, _00Ty --> _00Ue
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01537__00Ue = (v01532__00TA**1)*(v01538__00Ty**1)
v01537__00Ue = (v01537__00Ue*_00Ud_coeff).reshape((1, 27, 3, 40, 10))

# op _00bq arccos_eval
# LANG: _00bp --> _00br
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0262__00br = np.arccos(v0261__00bp)

# op _00by arccos_eval
# LANG: _00bx --> _00bz
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0272__00bz = np.arccos(v0271__00bx)

# op _00qB arccos_eval
# LANG: _00qA --> _00qC
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0645__00qC = np.arccos(v0644__00qA)

# op _00qt arccos_eval
# LANG: _00qs --> _00qu
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0635__00qu = np.arccos(v0634__00qs)

# op _00B__decompose_eval
# LANG: _00BN --> _00C0
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0989__00C0 = ((v0988__00BN.flatten())[src_indices__00C0__00B_]).reshape((1, 27, 3, 40, 10))

# op _00CA_power_combination_eval
# LANG: _00Cz, _00BX --> _00CB
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0993__00CB = (v0991__00Cz**1)*(v0995__00BX**1)
v0993__00CB = (v0993__00CB*_00CA_coeff).reshape((1, 27, 3, 40, 10))

# op _00CC_power_combination_eval
# LANG: _00Cx, _00BV --> _00CD
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0981__00CD = (v0980__00Cx**1)*(v0986__00BV**1)
v0981__00CD = (v0981__00CD*_00CC_coeff).reshape((1, 27, 3, 40, 10))

# op _00Qw_power_combination_eval
# LANG: altitude --> _00Qx
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01436__00Qx = (v01435_altitude**1)
v01436__00Qx = (v01436__00Qx*_00Qw_coeff).reshape((1,))

# op _00TF_decompose_eval
# LANG: _00Ts --> _00TG
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01535__00TG = ((v01534__00Ts.flatten())[src_indices__00TG__00TF]).reshape((1, 27, 3, 40, 10))

# op _00Uf_power_combination_eval
# LANG: _00Ue, _00TC --> _00Ug
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01539__00Ug = (v01537__00Ue**1)*(v01541__00TC**1)
v01539__00Ug = (v01539__00Ug*_00Uf_coeff).reshape((1, 27, 3, 40, 10))

# op _00Uh_power_combination_eval
# LANG: _00Uc, _00TA --> _00Ui
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01527__00Ui = (v01526__00Uc**1)*(v01532__00TA**1)
v01527__00Ui = (v01527__00Ui*_00Uh_coeff).reshape((1, 27, 3, 40, 10))

# op _00bA_power_combination_eval
# LANG: _00bz --> _00bB
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0273__00bB = (v0272__00bz**1)
v0273__00bB = (v0273__00bB*_00bA_coeff).reshape((1, 40, 30))

# op _00bs_power_combination_eval
# LANG: _00br --> _00bt
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0263__00bt = (v0262__00br**1)
v0263__00bt = (v0263__00bt*_00bs_coeff).reshape((1, 40, 30))

# op _00c8_sin_eval
# LANG: phi_distribution --> _00c9
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0288__00c9 = np.sin(v0251_phi_distribution)

# op _00cc_cos_eval
# LANG: phi_distribution --> _00cd
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0291__00cd = np.cos(v0251_phi_distribution)

# op _00qD_power_combination_eval
# LANG: _00qC --> _00qE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0646__00qE = (v0645__00qC**1)
v0646__00qE = (v0646__00qE*_00qD_coeff).reshape((1, 40, 30))

# op _00qv_power_combination_eval
# LANG: _00qu --> _00qw
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0636__00qw = (v0635__00qu**1)
v0636__00qw = (v0636__00qw*_00qv_coeff).reshape((1, 40, 30))

# op _00rb_sin_eval
# LANG: phi_distribution --> _00rc
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0661__00rc = np.sin(v0624_phi_distribution)

# op _00rf_cos_eval
# LANG: phi_distribution --> _00rg
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0664__00rg = np.cos(v0624_phi_distribution)

# op _00yR_power_combination_eval
# LANG: altitude --> _00yS
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0890__00yS = (v0889_altitude**1)
v0890__00yS = (v0890__00yS*_00yR_coeff).reshape((1,))

# op _00CE_power_combination_eval
# LANG: _00CD, _00C0 --> _00CF
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0987__00CF = (v0981__00CD**1)*(v0989__00C0**1)
v0987__00CF = (v0987__00CF*_00CE_coeff).reshape((1, 27, 3, 40, 10))

# op _00CG_power_combination_eval
# LANG: _00CB --> _00CH
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0996__00CH = (v0993__00CB**1)
v0996__00CH = (v0996__00CH*_00CG_coeff).reshape((1, 27, 3, 40, 10))

# op _00Qy_linear_combination_eval
# LANG: _00Qx --> _00Qz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01437__00Qz = _00Qy_constant+-1*v01436__00Qx

# op _00Uj_power_combination_eval
# LANG: _00Ui, _00TG --> _00Uk
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01533__00Uk = (v01527__00Ui**1)*(v01535__00TG**1)
v01533__00Uk = (v01533__00Uk*_00Uj_coeff).reshape((1, 27, 3, 40, 10))

# op _00Ul_power_combination_eval
# LANG: _00Ug --> _00Um
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01542__00Um = (v01539__00Ug**1)
v01542__00Um = (v01542__00Um*_00Ul_coeff).reshape((1, 27, 3, 40, 10))

# op _00bC_power_combination_eval
# LANG: _00bt, _00bB --> prandtl_loss_factor
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.prandtl_loss_factor_model
v0264_prandtl_loss_factor = (v0263__00bt**1)*(v0273__00bB**1)
v0264_prandtl_loss_factor = (v0264_prandtl_loss_factor*_00bC_coeff).reshape((1, 40, 30))

# op _00bZ_cos_eval
# LANG: phi_distribution --> _00b_
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0295__00b_ = np.cos(v0251_phi_distribution)

# op _00c2_sin_eval
# LANG: phi_distribution --> _00c3
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0298__00c3 = np.sin(v0251_phi_distribution)

# op _00ca_power_combination_eval
# LANG: _00c9, Cl --> _00cb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0254_Cl = v0254_Cl.reshape((1, 40, 30))
v0287__00cb = (v0254_Cl**1)*(v0288__00c9**1)
v0287__00cb = (v0287__00cb*_00ca_coeff).reshape((1, 40, 30))
v0254_Cl = v0254_Cl.reshape((1200,))

# op _00ce_power_combination_eval
# LANG: _00cd, Cd --> _00cf
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0253_Cd = v0253_Cd.reshape((1, 40, 30))
v0290__00cf = (v0253_Cd**1)*(v0291__00cd**1)
v0290__00cf = (v0290__00cf*_00ce_coeff).reshape((1, 40, 30))
v0253_Cd = v0253_Cd.reshape((1200,))

# op _00dj_power_combination_eval
# LANG: phi_distribution --> _00dk
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0314__00dk = (v0251_phi_distribution**1)
v0314__00dk = (v0314__00dk*_00dj_coeff).reshape((1, 40, 30))

# op _00qF_power_combination_eval
# LANG: _00qw, _00qE --> prandtl_loss_factor
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.prandtl_loss_factor_model
v0637_prandtl_loss_factor = (v0636__00qw**1)*(v0646__00qE**1)
v0637_prandtl_loss_factor = (v0637_prandtl_loss_factor*_00qF_coeff).reshape((1, 40, 30))

# op _00r1_cos_eval
# LANG: phi_distribution --> _00r2
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0668__00r2 = np.cos(v0624_phi_distribution)

# op _00r5_sin_eval
# LANG: phi_distribution --> _00r6
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0671__00r6 = np.sin(v0624_phi_distribution)

# op _00rd_power_combination_eval
# LANG: _00rc, Cl --> _00re
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0627_Cl = v0627_Cl.reshape((1, 40, 30))
v0660__00re = (v0627_Cl**1)*(v0661__00rc**1)
v0660__00re = (v0660__00re*_00rd_coeff).reshape((1, 40, 30))
v0627_Cl = v0627_Cl.reshape((1200,))

# op _00rh_power_combination_eval
# LANG: _00rg, Cd --> _00ri
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0626_Cd = v0626_Cd.reshape((1, 40, 30))
v0663__00ri = (v0626_Cd**1)*(v0664__00rg**1)
v0663__00ri = (v0663__00ri*_00rh_coeff).reshape((1, 40, 30))
v0626_Cd = v0626_Cd.reshape((1200,))

# op _00sm_power_combination_eval
# LANG: phi_distribution --> _00sn
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0687__00sn = (v0624_phi_distribution**1)
v0687__00sn = (v0687__00sn*_00sm_coeff).reshape((1, 40, 30))

# op _00yT_linear_combination_eval
# LANG: _00yS --> _00yU
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0891__00yU = _00yT_constant+-1*v0890__00yS

# op _00CI_power_combination_eval
# LANG: _00CF, _00CH --> _00CJ
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0990__00CJ = (v0987__00CF**1)*(v0996__00CH**-1)
v0990__00CJ = (v0990__00CJ*_00CI_coeff).reshape((1, 27, 3, 40, 10))

# op _00QA_power_combination_eval
# LANG: _00Qz --> _00QB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01438__00QB = (v01437__00Qz**1)
v01438__00QB = (v01438__00QB*_00QA_coeff).reshape((1,))

# op _00Un_power_combination_eval
# LANG: _00Uk, _00Um --> _00Uo
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01536__00Uo = (v01533__00Uk**1)*(v01542__00Um**-1)
v01536__00Uo = (v01536__00Uo*_00Un_coeff).reshape((1, 27, 3, 40, 10))

# op _00c0_power_combination_eval
# LANG: _00b_, Cl --> _00c1
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0254_Cl = v0254_Cl.reshape((1, 40, 30))
v0294__00c1 = (v0254_Cl**1)*(v0295__00b_**1)
v0294__00c1 = (v0294__00c1*_00c0_coeff).reshape((1, 40, 30))
v0254_Cl = v0254_Cl.reshape((1200,))

# op _00c4_power_combination_eval
# LANG: _00c3, Cd --> _00c5
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0253_Cd = v0253_Cd.reshape((1, 40, 30))
v0297__00c5 = (v0253_Cd**1)*(v0298__00c3**1)
v0297__00c5 = (v0297__00c5*_00c4_coeff).reshape((1, 40, 30))
v0253_Cd = v0253_Cd.reshape((1200,))

# op _00cU_power_combination_eval
# LANG: prandtl_loss_factor --> _00cV
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0301__00cV = (v0264_prandtl_loss_factor**1)
v0301__00cV = (v0301__00cV*_00cU_coeff).reshape((1, 40, 30))

# op _00cW_sin_eval
# LANG: phi_distribution --> _00cX
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0303__00cX = np.sin(v0251_phi_distribution)

# op _00cg_linear_combination_eval
# LANG: _00cb, _00cf --> _00ch
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0289__00ch = _00cg_constant+1*v0287__00cb+1*v0290__00cf

# op _00db_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00dc
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0308__00dc = (v0231__tangential_inflow_velocity**1)
v0308__00dc = (v0308__00dc*_00db_coeff).reshape((1, 40, 30))

# op _00dh_power_combination_eval
# LANG: prandtl_loss_factor --> _00di
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0312__00di = (v0264_prandtl_loss_factor**1)
v0312__00di = (v0312__00di*_00dh_coeff).reshape((1, 40, 30))

# op _00dl_sin_eval
# LANG: _00dk --> _00dm
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0315__00dm = np.sin(v0314__00dk)

# op _00r3_power_combination_eval
# LANG: _00r2, Cl --> _00r4
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0627_Cl = v0627_Cl.reshape((1, 40, 30))
v0667__00r4 = (v0627_Cl**1)*(v0668__00r2**1)
v0667__00r4 = (v0667__00r4*_00r3_coeff).reshape((1, 40, 30))
v0627_Cl = v0627_Cl.reshape((1200,))

# op _00r7_power_combination_eval
# LANG: _00r6, Cd --> _00r8
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0626_Cd = v0626_Cd.reshape((1, 40, 30))
v0670__00r8 = (v0626_Cd**1)*(v0671__00r6**1)
v0670__00r8 = (v0670__00r8*_00r7_coeff).reshape((1, 40, 30))
v0626_Cd = v0626_Cd.reshape((1200,))

# op _00rX_power_combination_eval
# LANG: prandtl_loss_factor --> _00rY
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0674__00rY = (v0637_prandtl_loss_factor**1)
v0674__00rY = (v0674__00rY*_00rX_coeff).reshape((1, 40, 30))

# op _00rZ_sin_eval
# LANG: phi_distribution --> _00r_
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0676__00r_ = np.sin(v0624_phi_distribution)

# op _00rj_linear_combination_eval
# LANG: _00re, _00ri --> _00rk
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0662__00rk = _00rj_constant+1*v0660__00re+1*v0663__00ri

# op _00se_power_combination_eval
# LANG: _tangential_inflow_velocity --> _00sf
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0681__00sf = (v0604__tangential_inflow_velocity**1)
v0681__00sf = (v0681__00sf*_00se_coeff).reshape((1, 40, 30))

# op _00sk_power_combination_eval
# LANG: prandtl_loss_factor --> _00sl
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0685__00sl = (v0637_prandtl_loss_factor**1)
v0685__00sl = (v0685__00sl*_00sk_coeff).reshape((1, 40, 30))

# op _00so_sin_eval
# LANG: _00sn --> _00sp
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0688__00sp = np.sin(v0687__00sn)

# op _00yV_power_combination_eval
# LANG: _00yU --> _00yW
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0892__00yW = (v0891__00yU**1)
v0892__00yW = (v0892__00yW*_00yV_coeff).reshape((1,))

# op _00C4_decompose_eval
# LANG: phi --> _00C5
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0969__00C5 = ((v0624_phi_distribution.flatten())[src_indices__00C5__00C4]).reshape((1, 40, 1))

# op _00Eq_bessel_eval
# LANG: _00CJ --> _00Er
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01076__00Er=_00Eq_bessel_eval(0,v0990__00CJ)

# op _00Es_bessel_eval
# LANG: _00CJ --> _00Et
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01078__00Et=_00Es_bessel_eval(1,v0990__00CJ)

# op _00QC_linear_combination_eval
# LANG: _00QB --> temperature
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01439_temperature = _00QC_constant+1*v01438__00QB

# op _00TK_decompose_eval
# LANG: phi --> _00TL
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01515__00TL = ((v0251_phi_distribution.flatten())[src_indices__00TL__00TK]).reshape((1, 40, 1))

# op _00W5_bessel_eval
# LANG: _00Uo --> _00W6
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01622__00W6=_00W5_bessel_eval(0,v01536__00Uo)

# op _00W7_bessel_eval
# LANG: _00Uo --> _00W8
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01624__00W8=_00W7_bessel_eval(1,v01536__00Uo)

# op _00c6_linear_combination_eval
# LANG: _00c1, _00c5 --> _00c7
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0296__00c7 = _00c6_constant+1*v0294__00c1+-1*v0297__00c5

# op _00cY_power_combination_eval
# LANG: _00cV, _00cX --> _00cZ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0302__00cZ = (v0301__00cV**1)*(v0303__00cX**1)
v0302__00cZ = (v0302__00cZ*_00cY_coeff).reshape((1, 40, 30))

# op _00c__cos_eval
# LANG: phi_distribution --> _00d0
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0305__00d0 = np.cos(v0251_phi_distribution)

# op _00dd_power_combination_eval
# LANG: _00dc, _blade_solidity --> _00de
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0309__00de = (v0308__00dc**1)*(v0220__blade_solidity**1)
v0309__00de = (v0309__00de*_00dd_coeff).reshape((1, 40, 30))

# op _00dn_power_combination_eval
# LANG: _00di, _00dm --> _00do
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0313__00do = (v0312__00di**1)*(v0315__00dm**1)
v0313__00do = (v0313__00do*_00dn_coeff).reshape((1, 40, 30))

# op _00dp_power_combination_eval
# LANG: _00ch, _blade_solidity --> _00dq
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0317__00dq = (v0220__blade_solidity**1)*(v0289__00ch**1)
v0317__00dq = (v0317__00dq*_00dp_coeff).reshape((1, 40, 30))

# op _00r9_linear_combination_eval
# LANG: _00r4, _00r8 --> _00ra
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0669__00ra = _00r9_constant+1*v0667__00r4+-1*v0670__00r8

# op _00s0_power_combination_eval
# LANG: _00rY, _00r_ --> _00s1
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0675__00s1 = (v0674__00rY**1)*(v0676__00r_**1)
v0675__00s1 = (v0675__00s1*_00s0_coeff).reshape((1, 40, 30))

# op _00s2_cos_eval
# LANG: phi_distribution --> _00s3
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0678__00s3 = np.cos(v0624_phi_distribution)

# op _00sg_power_combination_eval
# LANG: _00sf, _blade_solidity --> _00sh
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0682__00sh = (v0681__00sf**1)*(v0593__blade_solidity**1)
v0682__00sh = (v0682__00sh*_00sg_coeff).reshape((1, 40, 30))

# op _00sq_power_combination_eval
# LANG: _00sl, _00sp --> _00sr
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0686__00sr = (v0685__00sl**1)*(v0688__00sp**1)
v0686__00sr = (v0686__00sr*_00sq_coeff).reshape((1, 40, 30))

# op _00ss_power_combination_eval
# LANG: _00rk, _blade_solidity --> _00st
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0690__00st = (v0593__blade_solidity**1)*(v0662__00rk**1)
v0690__00st = (v0690__00st*_00ss_coeff).reshape((1, 40, 30))

# op _00yX_linear_combination_eval
# LANG: _00yW --> temperature
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0893_temperature = _00yX_constant+1*v0892__00yW

# op _00C6 reshape_eval
# LANG: _00C5 --> _00C7
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0970__00C7 = v0969__00C5.reshape((1, 40))

# op _00EC_bessel_eval
# LANG: _00CJ --> _00ED
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01082__00ED=_00EC_bessel_eval(1,v0990__00CJ)

# op _00Em_bessel_eval
# LANG: _00CJ --> _00En
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01073__00En=_00Em_bessel_eval(1,v0990__00CJ)

# op _00Eu_power_combination_eval
# LANG: _00Er, _00Et --> _00Ev
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01077__00Ev = (v01076__00Er**1)*(v01078__00Et**1)
v01077__00Ev = (v01077__00Ev*_00Eu_coeff).reshape((1, 27, 3, 40, 10))

# op _00Ew_bessel_eval
# LANG: _00CJ --> _00Ex
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01080__00Ex=_00Ew_bessel_eval(1,v0990__00CJ)

# op _00QE_power_combination_eval
# LANG: temperature --> _00QF
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01440__00QF = (v01439_temperature**1)
v01440__00QF = (v01440__00QF*_00QE_coeff).reshape((1,))

# op _00TM reshape_eval
# LANG: _00TL --> _00TN
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01516__00TN = v01515__00TL.reshape((1, 40))

# op _00W1_bessel_eval
# LANG: _00Uo --> _00W2
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01619__00W2=_00W1_bessel_eval(1,v01536__00Uo)

# op _00W9_power_combination_eval
# LANG: _00W6, _00W8 --> _00Wa
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01623__00Wa = (v01622__00W6**1)*(v01624__00W8**1)
v01623__00Wa = (v01623__00Wa*_00W9_coeff).reshape((1, 27, 3, 40, 10))

# op _00Wb_bessel_eval
# LANG: _00Uo --> _00Wc
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01626__00Wc=_00Wb_bessel_eval(1,v01536__00Uo)

# op _00Wh_bessel_eval
# LANG: _00Uo --> _00Wi
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01628__00Wi=_00Wh_bessel_eval(1,v01536__00Uo)

# op _00cQ_power_combination_eval
# LANG: _00c7, _blade_solidity --> _00cR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0293__00cR = (v0220__blade_solidity**1)*(v0296__00c7**1)
v0293__00cR = (v0293__00cR*_00cQ_coeff).reshape((1, 40, 30))

# op _00d1_power_combination_eval
# LANG: _00cZ, _00d0 --> _00d2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0304__00d2 = (v0302__00cZ**1)*(v0305__00d0**1)
v0304__00d2 = (v0304__00d2*_00d1_coeff).reshape((1, 40, 30))

# op _00d3_power_combination_eval
# LANG: _00ch, _blade_solidity --> _00d4
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0307__00d4 = (v0220__blade_solidity**1)*(v0289__00ch**1)
v0307__00d4 = (v0307__00d4*_00d3_coeff).reshape((1, 40, 30))

# op _00df_power_combination_eval
# LANG: _00ch, _00de --> _00dg
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0310__00dg = (v0309__00de**1)*(v0289__00ch**1)
v0310__00dg = (v0310__00dg*_00df_coeff).reshape((1, 40, 30))

# op _00dr_linear_combination_eval
# LANG: _00do, _00dq --> _00ds
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0316__00ds = _00dr_constant+1*v0313__00do+1*v0317__00dq

# op _00rT_power_combination_eval
# LANG: _00ra, _blade_solidity --> _00rU
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0666__00rU = (v0593__blade_solidity**1)*(v0669__00ra**1)
v0666__00rU = (v0666__00rU*_00rT_coeff).reshape((1, 40, 30))

# op _00s4_power_combination_eval
# LANG: _00s1, _00s3 --> _00s5
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0677__00s5 = (v0675__00s1**1)*(v0678__00s3**1)
v0677__00s5 = (v0677__00s5*_00s4_coeff).reshape((1, 40, 30))

# op _00s6_power_combination_eval
# LANG: _00rk, _blade_solidity --> _00s7
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0680__00s7 = (v0593__blade_solidity**1)*(v0662__00rk**1)
v0680__00s7 = (v0680__00s7*_00s6_coeff).reshape((1, 40, 30))

# op _00si_power_combination_eval
# LANG: _00rk, _00sh --> _00sj
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0683__00sj = (v0682__00sh**1)*(v0662__00rk**1)
v0683__00sj = (v0683__00sj*_00si_coeff).reshape((1, 40, 30))

# op _00su_linear_combination_eval
# LANG: _00sr, _00st --> _00sv
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0689__00sv = _00su_constant+1*v0686__00sr+1*v0690__00st

# op _00yZ_power_combination_eval
# LANG: temperature --> _00y_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0894__00y_ = (v0893_temperature**1)
v0894__00y_ = (v0894__00y_*_00yZ_coeff).reshape((1,))

# op _00C8 expand_array_eval
# LANG: _00C7 --> _00C9
# SHAPES: (1, 40) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0971__00C9 = np.einsum('ad,bce->abcde', v0970__00C7.reshape((1, 40)) ,np.ones((27, 3, 11))).reshape((1, 27, 3, 40, 11))

# op _00EE_power_combination_eval
# LANG: _00ED --> _00EF
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01083__00EF = (v01082__00ED**2)
v01083__00EF = (v01083__00EF*_00EE_coeff).reshape((1, 27, 3, 40, 10))

# op _00EG_bessel_eval
# LANG: _00CJ --> _00EH
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01085__00EH=_00EG_bessel_eval(0,v0990__00CJ)

# op _00EM_bessel_eval
# LANG: _00CJ --> _00EN
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01087__00EN=_00EM_bessel_eval(0,v0990__00CJ)

# op _00EO_bessel_eval
# LANG: _00CJ --> _00EP
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01089__00EP=_00EO_bessel_eval(0,v0990__00CJ)

# op _00Eo_power_combination_eval
# LANG: _00En --> _00Ep
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01074__00Ep = (v01073__00En**3)
v01074__00Ep = (v01074__00Ep*_00Eo_coeff).reshape((1, 27, 3, 40, 10))

# op _00Ey_power_combination_eval
# LANG: _00Ev, _00Ex --> _00Ez
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01079__00Ez = (v01077__00Ev**1)*(v01080__00Ex**1)
v01079__00Ez = (v01079__00Ez*_00Ey_coeff).reshape((1, 27, 3, 40, 10))

# op _00QG_power_combination_eval
# LANG: _00QF --> _00QH
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01441__00QH = (v01440__00QF**5.258643795229161)
v01441__00QH = (v01441__00QH*_00QG_coeff).reshape((1,))

# op _00TO expand_array_eval
# LANG: _00TN --> _00TP
# SHAPES: (1, 40) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01517__00TP = np.einsum('ad,bce->abcde', v01516__00TN.reshape((1, 40)) ,np.ones((27, 3, 11))).reshape((1, 27, 3, 40, 11))

# op _00W3_power_combination_eval
# LANG: _00W2 --> _00W4
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01620__00W4 = (v01619__00W2**3)
v01620__00W4 = (v01620__00W4*_00W3_coeff).reshape((1, 27, 3, 40, 10))

# op _00Wd_power_combination_eval
# LANG: _00Wa, _00Wc --> _00We
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01625__00We = (v01623__00Wa**1)*(v01626__00Wc**1)
v01625__00We = (v01625__00We*_00Wd_coeff).reshape((1, 27, 3, 40, 10))

# op _00Wj_power_combination_eval
# LANG: _00Wi --> _00Wk
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01629__00Wk = (v01628__00Wi**2)
v01629__00Wk = (v01629__00Wk*_00Wj_coeff).reshape((1, 27, 3, 40, 10))

# op _00Wl_bessel_eval
# LANG: _00Uo --> _00Wm
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01631__00Wm=_00Wl_bessel_eval(0,v01536__00Uo)

# op _00Wr_bessel_eval
# LANG: _00Uo --> _00Ws
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01633__00Ws=_00Wr_bessel_eval(0,v01536__00Uo)

# op _00Wt_bessel_eval
# LANG: _00Uo --> _00Wu
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01635__00Wu=_00Wt_bessel_eval(0,v01536__00Uo)

# op _00cS_power_combination_eval
# LANG: _00cR, _tangential_inflow_velocity --> _00cT
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0299__00cT = (v0293__00cR**1)*(v0231__tangential_inflow_velocity**1)
v0299__00cT = (v0299__00cT*_00cS_coeff).reshape((1, 40, 30))

# op _00d5_linear_combination_eval
# LANG: _00d2, _00d4 --> _00d6
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0306__00d6 = _00d5_constant+1*v0304__00d2+1*v0307__00d4

# op _00dt_power_combination_eval
# LANG: _00dg, _00ds --> _ut
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0311__ut = (v0310__00dg**1)*(v0316__00ds**-1)
v0311__ut = (v0311__ut*_00dt_coeff).reshape((1, 40, 30))

# op _00rV_power_combination_eval
# LANG: _00rU, _tangential_inflow_velocity --> _00rW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0672__00rW = (v0666__00rU**1)*(v0604__tangential_inflow_velocity**1)
v0672__00rW = (v0672__00rW*_00rV_coeff).reshape((1, 40, 30))

# op _00s8_linear_combination_eval
# LANG: _00s5, _00s7 --> _00s9
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0679__00s9 = _00s8_constant+1*v0677__00s5+1*v0680__00s7

# op _00sw_power_combination_eval
# LANG: _00sj, _00sv --> _ut
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0684__ut = (v0683__00sj**1)*(v0689__00sv**-1)
v0684__ut = (v0684__ut*_00sw_coeff).reshape((1, 40, 30))

# op _00z0_power_combination_eval
# LANG: _00y_ --> _00z1
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0895__00z1 = (v0894__00y_**5.258643795229161)
v0895__00z1 = (v0895__00z1*_00z0_coeff).reshape((1,))

# op _00Ca_power_combination_eval
# LANG: _00C9, _00BF --> lambda_test
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0972_lambda_test = (v0971__00C9**1)*(v0974__00BF**1)
v0972_lambda_test = (v0972_lambda_test*_00Ca_coeff).reshape((1, 27, 3, 40, 11))

# op _00EA_linear_combination_eval
# LANG: _00Ep, _00Ez --> _00EB
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01075__00EB = _00EA_constant+1*v01074__00Ep+1*v01079__00Ez

# op _00EI_power_combination_eval
# LANG: _00EF, _00EH --> _00EJ
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01084__00EJ = (v01083__00EF**1)*(v01085__00EH**1)
v01084__00EJ = (v01084__00EJ*_00EI_coeff).reshape((1, 27, 3, 40, 10))

# op _00EQ_power_combination_eval
# LANG: _00EN, _00EP --> _00ER
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01088__00ER = (v01087__00EN**1)*(v01089__00EP**1)
v01088__00ER = (v01088__00ER*_00EQ_coeff).reshape((1, 27, 3, 40, 10))

# op _00ES_bessel_eval
# LANG: _00CJ --> _00ET
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01091__00ET=_00ES_bessel_eval(1,v0990__00CJ)

# op _00EY_bessel_eval
# LANG: _00CJ --> _00EZ
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01093__00EZ=_00EY_bessel_eval(0,v0990__00CJ)

# op _00QI_power_combination_eval
# LANG: _00QH --> pressure
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01442_pressure = (v01441__00QH**1)
v01442_pressure = (v01442_pressure*_00QI_coeff).reshape((1,))

# op _00Ra expand_scalar_eval
# LANG: Vx --> _00Rb
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01453__00Rb = np.empty((1, 1))
v01453__00Rb.fill(v033_u.item())

# op _00Rd expand_scalar_eval
# LANG: Vy --> _00Re
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01455__00Re = np.empty((1, 1))
v01455__00Re.fill(v034_v.item())

# op _00Rf expand_scalar_eval
# LANG: Vz --> _00Rg
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01456__00Rg = np.empty((1, 1))
v01456__00Rg.fill(v035_w.item())

# op _00TQ_power_combination_eval
# LANG: _00TP, _00Tk --> lambda_test
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01518_lambda_test = (v01517__00TP**1)*(v01520__00Tk**1)
v01518_lambda_test = (v01518_lambda_test*_00TQ_coeff).reshape((1, 27, 3, 40, 11))

# op _00WD_bessel_eval
# LANG: _00Uo --> _00WE
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01639__00WE=_00WD_bessel_eval(0,v01536__00Uo)

# op _00Wf_linear_combination_eval
# LANG: _00W4, _00We --> _00Wg
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01621__00Wg = _00Wf_constant+1*v01620__00W4+1*v01625__00We

# op _00Wn_power_combination_eval
# LANG: _00Wk, _00Wm --> _00Wo
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01630__00Wo = (v01629__00Wk**1)*(v01631__00Wm**1)
v01630__00Wo = (v01630__00Wo*_00Wn_coeff).reshape((1, 27, 3, 40, 10))

# op _00Wv_power_combination_eval
# LANG: _00Ws, _00Wu --> _00Ww
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01634__00Ww = (v01633__00Ws**1)*(v01635__00Wu**1)
v01634__00Ww = (v01634__00Ww*_00Wv_coeff).reshape((1, 27, 3, 40, 10))

# op _00Wx_bessel_eval
# LANG: _00Uo --> _00Wy
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01637__00Wy=_00Wx_bessel_eval(1,v01536__00Uo)

# op _00cA_power_combination_eval
# LANG: prandtl_loss_factor --> _00cB
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0280__00cB = (v0264_prandtl_loss_factor**1)
v0280__00cB = (v0280__00cB*_00cA_coeff).reshape((1, 40, 30))

# op _00cC_sin_eval
# LANG: phi_distribution --> _00cD
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0282__00cD = np.sin(v0251_phi_distribution)

# op _00d7_power_combination_eval
# LANG: _00cT, _00d6 --> _00d8
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0300__00d8 = (v0299__00cT**1)*(v0306__00d6**-1)
v0300__00d8 = (v0300__00d8*_00d7_coeff).reshape((1, 40, 30))

# op _00f3_power_combination_eval
# LANG: _ut --> _00f4
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0380__00f4 = (v0311__ut**1)
v0380__00f4 = (v0380__00f4*_00f3_coeff).reshape((1, 40, 30))

# op _00rD_power_combination_eval
# LANG: prandtl_loss_factor --> _00rE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0653__00rE = (v0637_prandtl_loss_factor**1)
v0653__00rE = (v0653__00rE*_00rD_coeff).reshape((1, 40, 30))

# op _00rF_sin_eval
# LANG: phi_distribution --> _00rG
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0655__00rG = np.sin(v0624_phi_distribution)

# op _00sa_power_combination_eval
# LANG: _00rW, _00s9 --> _00sb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0673__00sb = (v0672__00rW**1)*(v0679__00s9**-1)
v0673__00sb = (v0673__00sb*_00sa_coeff).reshape((1, 40, 30))

# op _00u6_power_combination_eval
# LANG: _ut --> _00u7
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0753__00u7 = (v0684__ut**1)
v0753__00u7 = (v0753__00u7*_00u6_coeff).reshape((1, 40, 30))

# op _00z2_power_combination_eval
# LANG: _00z1 --> pressure
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0896_pressure = (v0895__00z1**1)
v0896_pressure = (v0896_pressure*_00z2_coeff).reshape((1,))

# op _00zA expand_scalar_eval
# LANG: Vz --> _00zB
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0910__00zB = np.empty((1, 1))
v0910__00zB.fill(v035_w.item())

# op _00zv expand_scalar_eval
# LANG: Vx --> _00zw
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0907__00zw = np.empty((1, 1))
v0907__00zw.fill(v033_u.item())

# op _00zy expand_scalar_eval
# LANG: Vy --> _00zz
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0909__00zz = np.empty((1, 1))
v0909__00zz.fill(v034_v.item())

# op _000I_sparsematmat_eval
# LANG: design_geometry --> _000J
# SHAPES: (32500, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v021__000J = _000I_sparsematmat_eval_mat@v05_design_geometry

# op _000o_sparsematmat_eval
# LANG: design_geometry --> _000p
# SHAPES: (32500, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v011__000p = _000o_sparsematmat_eval_mat@v05_design_geometry

# op _00CM_bessel_eval
# LANG: _00CJ --> _00CN
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0999__00CN=_00CM_bessel_eval(1,v0990__00CJ)

# op _00CS_bessel_eval
# LANG: _00CJ --> _00CT
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01002__00CT=_00CS_bessel_eval(1,v0990__00CJ)

# op _00Ce_decompose_eval
# LANG: lambda_test --> _00Cf
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01057__00Cf = ((v0972_lambda_test.flatten())[src_indices__00Cf__00Ce]).reshape((1, 27, 3, 40, 10))

# op _00Dr_bessel_eval
# LANG: _00CJ --> _00Ds
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01021__00Ds=_00Dr_bessel_eval(1,v0990__00CJ)

# op _00Dx_bessel_eval
# LANG: _00CJ --> _00Dy
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01024__00Dy=_00Dx_bessel_eval(0,v0990__00CJ)

# op _00EK_linear_combination_eval
# LANG: _00EB, _00EJ --> _00EL
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01081__00EL = _00EK_constant+1*v01075__00EB+1*v01084__00EJ

# op _00EU_power_combination_eval
# LANG: _00ER, _00ET --> _00EV
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01090__00EV = (v01088__00ER**1)*(v01091__00ET**1)
v01090__00EV = (v01090__00EV*_00EU_coeff).reshape((1, 27, 3, 40, 10))

# op _00E__power_combination_eval
# LANG: _00EZ --> _00F0
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01094__00F0 = (v01093__00EZ**2)
v01094__00F0 = (v01094__00F0*_00E__coeff).reshape((1, 27, 3, 40, 10))

# op _00F1_bessel_eval
# LANG: _00CJ --> _00F2
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01096__00F2=_00F1_bessel_eval(1,v0990__00CJ)

# op _00F7_bessel_eval
# LANG: _00CJ --> _00F8
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01098__00F8=_00F7_bessel_eval(0,v0990__00CJ)

# op _00F9_bessel_eval
# LANG: _00CJ --> _00Fa
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01100__00Fa=_00F9_bessel_eval(1,v0990__00CJ)

# op _00QK_power_combination_eval
# LANG: pressure --> _00QL
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01443__00QL = (v01442_pressure**1)
v01443__00QL = (v01443__00QL*_00QK_coeff).reshape((1,))

# op _00Rc_indexed_passthrough_eval
# LANG: _00Rb, _00Re, _00Rg --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01454_V_aircraft__temp[i_v01453__00Rb__00Rc_indexed_passthrough_eval] = v01453__00Rb.flatten()
v01454_V_aircraft = v01454_V_aircraft__temp.copy()
v01454_V_aircraft__temp[i_v01455__00Re__00Rc_indexed_passthrough_eval] = v01455__00Re.flatten()
v01454_V_aircraft = v01454_V_aircraft__temp.copy()
v01454_V_aircraft__temp[i_v01456__00Rg__00Rc_indexed_passthrough_eval] = v01456__00Rg.flatten()
v01454_V_aircraft = v01454_V_aircraft__temp.copy()

# op _00TU_decompose_eval
# LANG: lambda_test --> _00TV
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01603__00TV = ((v01518_lambda_test.flatten())[src_indices__00TV__00TU]).reshape((1, 27, 3, 40, 10))

# op _00Ur_bessel_eval
# LANG: _00Uo --> _00Us
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01545__00Us=_00Ur_bessel_eval(1,v01536__00Uo)

# op _00Ux_bessel_eval
# LANG: _00Uo --> _00Uy
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01548__00Uy=_00Ux_bessel_eval(1,v01536__00Uo)

# op _00V6_bessel_eval
# LANG: _00Uo --> _00V7
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01567__00V7=_00V6_bessel_eval(1,v01536__00Uo)

# op _00Vc_bessel_eval
# LANG: _00Uo --> _00Vd
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01570__00Vd=_00Vc_bessel_eval(0,v01536__00Uo)

# op _00WF_power_combination_eval
# LANG: _00WE --> _00WG
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01640__00WG = (v01639__00WE**2)
v01640__00WG = (v01640__00WG*_00WF_coeff).reshape((1, 27, 3, 40, 10))

# op _00WH_bessel_eval
# LANG: _00Uo --> _00WI
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01642__00WI=_00WH_bessel_eval(1,v01536__00Uo)

# op _00WN_bessel_eval
# LANG: _00Uo --> _00WO
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01644__00WO=_00WN_bessel_eval(0,v01536__00Uo)

# op _00WP_bessel_eval
# LANG: _00Uo --> _00WQ
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01646__00WQ=_00WP_bessel_eval(1,v01536__00Uo)

# op _00Wp_linear_combination_eval
# LANG: _00Wg, _00Wo --> _00Wq
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01627__00Wq = _00Wp_constant+1*v01621__00Wg+1*v01630__00Wo

# op _00Wz_power_combination_eval
# LANG: _00Ww, _00Wy --> _00WA
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01636__00WA = (v01634__00Ww**1)*(v01637__00Wy**1)
v01636__00WA = (v01636__00WA*_00Wz_coeff).reshape((1, 27, 3, 40, 10))

# op _00cE_power_combination_eval
# LANG: _00cB, _00cD --> _00cF
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0281__00cF = (v0280__00cB**1)*(v0282__00cD**1)
v0281__00cF = (v0281__00cF*_00cE_coeff).reshape((1, 40, 30))

# op _00cG_cos_eval
# LANG: phi_distribution --> _00cH
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0284__00cH = np.cos(v0251_phi_distribution)

# op _00cq_power_combination_eval
# LANG: prandtl_loss_factor --> _00cr
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0274__00cr = (v0264_prandtl_loss_factor**1)
v0274__00cr = (v0274__00cr*_00cq_coeff).reshape((1, 40, 30))

# op _00cu_sin_eval
# LANG: phi_distribution --> _00cv
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0277__00cv = np.sin(v0251_phi_distribution)

# op _00d9_linear_combination_eval
# LANG: _00d8, _axial_inflow_velocity --> _ux_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0292__ux_2 = _00d9_constant+1*v0221__axial_inflow_velocity+1*v0300__00d8

# op _00eW_power_combination_eval
# LANG: Cd --> _00eX
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0253_Cd = v0253_Cd.reshape((1, 40, 30))
v0373__00eX = (v0253_Cd**1)
v0373__00eX = (v0373__00eX*_00eW_coeff).reshape((1, 40, 30))
v0253_Cd = v0253_Cd.reshape((1200,))

# op _00f5_linear_combination_eval
# LANG: _00f4, _tangential_inflow_velocity --> _00f6
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0379__00f6 = _00f5_constant+1*v0231__tangential_inflow_velocity+-1*v0380__00f4

# op _00rH_power_combination_eval
# LANG: _00rE, _00rG --> _00rI
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0654__00rI = (v0653__00rE**1)*(v0655__00rG**1)
v0654__00rI = (v0654__00rI*_00rH_coeff).reshape((1, 40, 30))

# op _00rJ_cos_eval
# LANG: phi_distribution --> _00rK
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0657__00rK = np.cos(v0624_phi_distribution)

# op _00rt_power_combination_eval
# LANG: prandtl_loss_factor --> _00ru
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0647__00ru = (v0637_prandtl_loss_factor**1)
v0647__00ru = (v0647__00ru*_00rt_coeff).reshape((1, 40, 30))

# op _00rx_sin_eval
# LANG: phi_distribution --> _00ry
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0650__00ry = np.sin(v0624_phi_distribution)

# op _00sc_linear_combination_eval
# LANG: _00sb, _axial_inflow_velocity --> _ux_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0665__ux_2 = _00sc_constant+1*v0594__axial_inflow_velocity+1*v0673__00sb

# op _00tZ_power_combination_eval
# LANG: Cd --> _00t_
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0626_Cd = v0626_Cd.reshape((1, 40, 30))
v0746__00t_ = (v0626_Cd**1)
v0746__00t_ = (v0746__00t_*_00tZ_coeff).reshape((1, 40, 30))
v0626_Cd = v0626_Cd.reshape((1200,))

# op _00u8_linear_combination_eval
# LANG: _00u7, _tangential_inflow_velocity --> _00u9
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0752__00u9 = _00u8_constant+1*v0604__tangential_inflow_velocity+-1*v0753__00u7

# op _00z4_power_combination_eval
# LANG: pressure --> _00z5
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0897__00z5 = (v0896_pressure**1)
v0897__00z5 = (v0897__00z5*_00z4_coeff).reshape((1,))

# op _00zx_indexed_passthrough_eval
# LANG: _00zw, _00zz, _00zB --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0908_V_aircraft__temp[i_v0907__00zw__00zx_indexed_passthrough_eval] = v0907__00zw.flatten()
v0908_V_aircraft = v0908_V_aircraft__temp.copy()
v0908_V_aircraft__temp[i_v0909__00zz__00zx_indexed_passthrough_eval] = v0909__00zz.flatten()
v0908_V_aircraft = v0908_V_aircraft__temp.copy()
v0908_V_aircraft__temp[i_v0910__00zB__00zx_indexed_passthrough_eval] = v0910__00zB.flatten()
v0908_V_aircraft = v0908_V_aircraft__temp.copy()

# op _000K reshape_eval
# LANG: _000J --> rotor_2_disk_origin
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v022_rotor_2_disk_origin = v021__000J.reshape((1, 3))

# op _000q reshape_eval
# LANG: _000p --> rotor_1_disk_origin
# SHAPES: (1, 3) --> (1, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v012_rotor_1_disk_origin = v011__000p.reshape((1, 3))

# op _005Q_power_combination_eval
# LANG: propeller_radius --> _005R
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0192__005R = (v0122_propeller_radius**1)
v0192__005R = (v0192__005R*_005Q_coeff).reshape((1,))

# op _00CK_bessel_eval
# LANG: _00CJ --> _00CL
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0997__00CL=_00CK_bessel_eval(0,v0990__00CJ)

# op _00CO_power_combination_eval
# LANG: _00CN --> _00CP
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01000__00CP = (v0999__00CN**2)
v01000__00CP = (v01000__00CP*_00CO_coeff).reshape((1, 27, 3, 40, 10))

# op _00CU_power_combination_eval
# LANG: _00CT --> _00CV
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01003__00CV = (v01002__00CT**2)
v01003__00CV = (v01003__00CV*_00CU_coeff).reshape((1, 27, 3, 40, 10))

# op _00CW_bessel_eval
# LANG: _00CJ --> _00CX
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01005__00CX=_00CW_bessel_eval(1,v0990__00CJ)

# op _00D1_bessel_eval
# LANG: _00CJ --> _00D2
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01007__00D2=_00D1_bessel_eval(0,v0990__00CJ)

# op _00D3_bessel_eval
# LANG: _00CJ --> _00D4
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01009__00D4=_00D3_bessel_eval(1,v0990__00CJ)

# op _00DB_bessel_eval
# LANG: _00CJ --> _00DC
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01027__00DC=_00DB_bessel_eval(1,v0990__00CJ)

# op _00DH_bessel_eval
# LANG: _00CJ --> _00DI
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01029__00DI=_00DH_bessel_eval(1,v0990__00CJ)

# op _00Dp_bessel_eval
# LANG: _00CJ --> _00Dq
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01019__00Dq=_00Dp_bessel_eval(0,v0990__00CJ)

# op _00Dt_power_combination_eval
# LANG: _00Ds --> _00Du
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01022__00Du = (v01021__00Ds**2)
v01022__00Du = (v01022__00Du*_00Dt_coeff).reshape((1, 27, 3, 40, 10))

# op _00Dz_power_combination_eval
# LANG: _00Dy --> _00DA
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01025__00DA = (v01024__00Dy**2)
v01025__00DA = (v01025__00DA*_00Dz_coeff).reshape((1, 27, 3, 40, 10))

# op _00EW_linear_combination_eval
# LANG: _00EL, _00EV --> _00EX
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01086__00EX = _00EW_constant+1*v01081__00EL+1*v01090__00EV

# op _00F3_power_combination_eval
# LANG: _00F0, _00F2 --> _00F4
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01095__00F4 = (v01094__00F0**1)*(v01096__00F2**1)
v01095__00F4 = (v01095__00F4*_00F3_coeff).reshape((1, 27, 3, 40, 10))

# op _00Fb_power_combination_eval
# LANG: _00F8, _00Fa --> _00Fc
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01099__00Fc = (v01098__00F8**1)*(v01100__00Fa**1)
v01099__00Fc = (v01099__00Fc*_00Fb_coeff).reshape((1, 27, 3, 40, 10))

# op _00Fd_bessel_eval
# LANG: _00CJ --> _00Fe
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01102__00Fe=_00Fd_bessel_eval(1,v0990__00CJ)

# op _00Fj_bessel_eval
# LANG: _00CJ --> _00Fk
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01104__00Fk=_00Fj_bessel_eval(0,v0990__00CJ)

# op _00Fl_bessel_eval
# LANG: _00CJ --> _00Fm
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01106__00Fm=_00Fl_bessel_eval(1,v0990__00CJ)

# op _00G0_power_combination_eval
# LANG: _00BV, _00Cf --> _00G1
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01058__00G1 = (v01057__00Cf**1)*(v0986__00BV**1)
v01058__00G1 = (v01058__00G1*_00G0_coeff).reshape((1, 27, 3, 40, 10))

# op _00Ga_power_combination_eval
# LANG: _00BV, _00BT --> _00Gb
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01052__00Gb = (v0986__00BV**1)*(v0992__00BT**1)
v01052__00Gb = (v01052__00Gb*_00Ga_coeff).reshape((1, 27, 3, 40, 10))

# op _00QM_power_combination_eval
# LANG: temperature, _00QL --> density
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01444_density = (v01443__00QL**1)*(v01439_temperature**-1)
v01444_density = (v01444_density*_00QM_coeff).reshape((1,))

# op _00Rh expand_array_eval
# LANG: V_aircraft --> _00Ri
# SHAPES: (1, 3) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01463__00Ri = np.einsum('ab,c->abc', v01454_V_aircraft.reshape((1, 3)) ,np.ones((27,))).reshape((1, 3, 27))

# op _00Rn expand_array_eval
# LANG: time_vectors --> _00Ro
# SHAPES: (27,) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01469__00Ro = np.einsum('c,ab->abc', v01468_time_vectors.reshape((27,)) ,np.ones((1, 3))).reshape((1, 3, 27))

# op _00UB_bessel_eval
# LANG: _00Uo --> _00UC
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01551__00UC=_00UB_bessel_eval(1,v01536__00Uo)

# op _00UH_bessel_eval
# LANG: _00Uo --> _00UI
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01553__00UI=_00UH_bessel_eval(0,v01536__00Uo)

# op _00UJ_bessel_eval
# LANG: _00Uo --> _00UK
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01555__00UK=_00UJ_bessel_eval(1,v01536__00Uo)

# op _00Up_bessel_eval
# LANG: _00Uo --> _00Uq
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01543__00Uq=_00Up_bessel_eval(0,v01536__00Uo)

# op _00Ut_power_combination_eval
# LANG: _00Us --> _00Uu
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01546__00Uu = (v01545__00Us**2)
v01546__00Uu = (v01546__00Uu*_00Ut_coeff).reshape((1, 27, 3, 40, 10))

# op _00Uz_power_combination_eval
# LANG: _00Uy --> _00UA
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01549__00UA = (v01548__00Uy**2)
v01549__00UA = (v01549__00UA*_00Uz_coeff).reshape((1, 27, 3, 40, 10))

# op _00V4_bessel_eval
# LANG: _00Uo --> _00V5
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01565__00V5=_00V4_bessel_eval(0,v01536__00Uo)

# op _00V8_power_combination_eval
# LANG: _00V7 --> _00V9
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01568__00V9 = (v01567__00V7**2)
v01568__00V9 = (v01568__00V9*_00V8_coeff).reshape((1, 27, 3, 40, 10))

# op _00Ve_power_combination_eval
# LANG: _00Vd --> _00Vf
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01571__00Vf = (v01570__00Vd**2)
v01571__00Vf = (v01571__00Vf*_00Ve_coeff).reshape((1, 27, 3, 40, 10))

# op _00Vg_bessel_eval
# LANG: _00Uo --> _00Vh
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01573__00Vh=_00Vg_bessel_eval(1,v01536__00Uo)

# op _00Vm_bessel_eval
# LANG: _00Uo --> _00Vn
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01575__00Vn=_00Vm_bessel_eval(1,v01536__00Uo)

# op _00WB_linear_combination_eval
# LANG: _00Wq, _00WA --> _00WC
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01632__00WC = _00WB_constant+1*v01627__00Wq+1*v01636__00WA

# op _00WJ_power_combination_eval
# LANG: _00WG, _00WI --> _00WK
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01641__00WK = (v01640__00WG**1)*(v01642__00WI**1)
v01641__00WK = (v01641__00WK*_00WJ_coeff).reshape((1, 27, 3, 40, 10))

# op _00WR_power_combination_eval
# LANG: _00WO, _00WQ --> _00WS
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01645__00WS = (v01644__00WO**1)*(v01646__00WQ**1)
v01645__00WS = (v01645__00WS*_00WR_coeff).reshape((1, 27, 3, 40, 10))

# op _00WT_bessel_eval
# LANG: _00Uo --> _00WU
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01648__00WU=_00WT_bessel_eval(1,v01536__00Uo)

# op _00WZ_bessel_eval
# LANG: _00Uo --> _00W_
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01650__00W_=_00WZ_bessel_eval(0,v01536__00Uo)

# op _00X0_bessel_eval
# LANG: _00Uo --> _00X1
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01652__00X1=_00X0_bessel_eval(1,v01536__00Uo)

# op _00XG_power_combination_eval
# LANG: _00TA, _00TV --> _00XH
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01604__00XH = (v01603__00TV**1)*(v01532__00TA**1)
v01604__00XH = (v01604__00XH*_00XG_coeff).reshape((1, 27, 3, 40, 10))

# op _00XQ_power_combination_eval
# LANG: _00TA, _00Ty --> _00XR
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01598__00XR = (v01532__00TA**1)*(v01538__00Ty**1)
v01598__00XR = (v01598__00XR*_00XQ_coeff).reshape((1, 27, 3, 40, 10))

# op _00bT expand_scalar_eval
# LANG: density --> _00bU
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0242_density = v0242_density.reshape((1,))
v0320__00bU = np.empty((1, 40, 30))
v0320__00bU.fill(v0242_density.item())
v0242_density = v0242_density.reshape((1, 1))

# op _00cI_power_combination_eval
# LANG: _00cF, _00cH --> _00cJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0283__00cJ = (v0281__00cF**1)*(v0284__00cH**1)
v0283__00cJ = (v0283__00cJ*_00cI_coeff).reshape((1, 40, 30))

# op _00cK_power_combination_eval
# LANG: _00ch, _blade_solidity --> _00cL
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0286__00cL = (v0220__blade_solidity**1)*(v0289__00ch**1)
v0286__00cL = (v0286__00cL*_00cK_coeff).reshape((1, 40, 30))

# op _00cs_power_combination_eval
# LANG: _00cr, _tangential_inflow_velocity --> _00ct
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0275__00ct = (v0274__00cr**1)*(v0231__tangential_inflow_velocity**1)
v0275__00ct = (v0275__00ct*_00cs_coeff).reshape((1, 40, 30))

# op _00cw_power_combination_eval
# LANG: _00cv --> _00cx
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0278__00cx = (v0277__00cv**2)
v0278__00cx = (v0278__00cx*_00cw_coeff).reshape((1, 40, 30))

# op _00eY_power_combination_eval
# LANG: _00eX --> _00eZ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0374__00eZ = (v0373__00eX**1)
v0374__00eZ = (v0374__00eZ*_00eY_coeff).reshape((1, 40, 30))

# op _00f1_power_combination_eval
# LANG: _ux_2 --> _00f2
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0377__00f2 = (v0292__ux_2**2)
v0377__00f2 = (v0377__00f2*_00f1_coeff).reshape((1, 40, 30))

# op _00f7_power_combination_eval
# LANG: _00f6 --> _00f8
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0381__00f8 = (v0379__00f6**2)
v0381__00f8 = (v0381__00f8*_00f7_coeff).reshape((1, 40, 30))

# op _00kT_power_combination_eval
# LANG: propeller_radius --> _00kU
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0565__00kU = (v0495_propeller_radius**1)
v0565__00kU = (v0565__00kU*_00kT_coeff).reshape((1,))

# op _00qW expand_scalar_eval
# LANG: density --> _00qX
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0615_density = v0615_density.reshape((1,))
v0693__00qX = np.empty((1, 40, 30))
v0693__00qX.fill(v0615_density.item())
v0615_density = v0615_density.reshape((1, 1))

# op _00rL_power_combination_eval
# LANG: _00rI, _00rK --> _00rM
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0656__00rM = (v0654__00rI**1)*(v0657__00rK**1)
v0656__00rM = (v0656__00rM*_00rL_coeff).reshape((1, 40, 30))

# op _00rN_power_combination_eval
# LANG: _00rk, _blade_solidity --> _00rO
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0659__00rO = (v0593__blade_solidity**1)*(v0662__00rk**1)
v0659__00rO = (v0659__00rO*_00rN_coeff).reshape((1, 40, 30))

# op _00rv_power_combination_eval
# LANG: _00ru, _tangential_inflow_velocity --> _00rw
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0648__00rw = (v0647__00ru**1)*(v0604__tangential_inflow_velocity**1)
v0648__00rw = (v0648__00rw*_00rv_coeff).reshape((1, 40, 30))

# op _00rz_power_combination_eval
# LANG: _00ry --> _00rA
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0651__00rA = (v0650__00ry**2)
v0651__00rA = (v0651__00rA*_00rz_coeff).reshape((1, 40, 30))

# op _00u0_power_combination_eval
# LANG: _00t_ --> _00u1
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0747__00u1 = (v0746__00t_**1)
v0747__00u1 = (v0747__00u1*_00u0_coeff).reshape((1, 40, 30))

# op _00u4_power_combination_eval
# LANG: _ux_2 --> _00u5
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0750__00u5 = (v0665__ux_2**2)
v0750__00u5 = (v0750__00u5*_00u4_coeff).reshape((1, 40, 30))

# op _00ua_power_combination_eval
# LANG: _00u9 --> _00ub
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0754__00ub = (v0752__00u9**2)
v0754__00ub = (v0754__00ub*_00ua_coeff).reshape((1, 40, 30))

# op _00z6_power_combination_eval
# LANG: temperature, _00z5 --> density
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0898_density = (v0897__00z5**1)*(v0893_temperature**-1)
v0898_density = (v0898_density*_00z6_coeff).reshape((1,))

# op _00zC expand_array_eval
# LANG: V_aircraft --> _00zD
# SHAPES: (1, 3) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0917__00zD = np.einsum('ab,c->abc', v0908_V_aircraft.reshape((1, 3)) ,np.ones((27,))).reshape((1, 3, 27))

# op _00zI expand_array_eval
# LANG: time_vectors --> _00zJ
# SHAPES: (27,) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0923__00zJ = np.einsum('c,ab->abc', v0922_time_vectors.reshape((27,)) ,np.ones((1, 3))).reshape((1, 3, 27))

# op _005S_linear_combination_eval
# LANG: _005R, propeller_radius --> _005T
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0191__005T = _005S_constant+1*v0122_propeller_radius+-1*v0192__005R

# op _00BO expand_scalar_eval
# LANG: density --> _00BP
# SHAPES: (1,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01049__00BP = np.empty((1, 27, 3, 40, 11))
v01049__00BP.fill(v0898_density.item())

# op _00CQ_power_combination_eval
# LANG: _00CL, _00CP --> _00CR
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0998__00CR = (v0997__00CL**1)*(v01000__00CP**1)
v0998__00CR = (v0998__00CR*_00CQ_coeff).reshape((1, 27, 3, 40, 10))

# op _00CY_power_combination_eval
# LANG: _00CV, _00CX --> _00CZ
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01004__00CZ = (v01003__00CV**1)*(v01005__00CX**1)
v01004__00CZ = (v01004__00CZ*_00CY_coeff).reshape((1, 27, 3, 40, 10))

# op _00D5_power_combination_eval
# LANG: _00D2, _00D4 --> _00D6
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01008__00D6 = (v01007__00D2**1)*(v01009__00D4**1)
v01008__00D6 = (v01008__00D6*_00D5_coeff).reshape((1, 27, 3, 40, 10))

# op _00D7_bessel_eval
# LANG: _00CJ --> _00D8
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01011__00D8=_00D7_bessel_eval(0,v0990__00CJ)

# op _00DD_power_combination_eval
# LANG: _00DA, _00DC --> _00DE
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01026__00DE = (v01025__00DA**1)*(v01027__00DC**1)
v01026__00DE = (v01026__00DE*_00DD_coeff).reshape((1, 27, 3, 40, 10))

# op _00DJ_power_combination_eval
# LANG: _00DI --> _00DK
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01030__00DK = (v01029__00DI**2)
v01030__00DK = (v01030__00DK*_00DJ_coeff).reshape((1, 27, 3, 40, 10))

# op _00DL_bessel_eval
# LANG: _00CJ --> _00DM
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01032__00DM=_00DL_bessel_eval(1,v0990__00CJ)

# op _00DT_bessel_eval
# LANG: _00CJ --> _00DU
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01036__00DU=_00DT_bessel_eval(1,v0990__00CJ)

# op _00Dd_bessel_eval
# LANG: _00CJ --> _00De
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01013__00De=_00Dd_bessel_eval(1,v0990__00CJ)

# op _00Df_bessel_eval
# LANG: _00CJ --> _00Dg
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01015__00Dg=_00Df_bessel_eval(0,v0990__00CJ)

# op _00Dv_power_combination_eval
# LANG: _00Dq, _00Du --> _00Dw
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01020__00Dw = (v01019__00Dq**1)*(v01022__00Du**1)
v01020__00Dw = (v01020__00Dw*_00Dv_coeff).reshape((1, 27, 3, 40, 10))

# op _00F5_linear_combination_eval
# LANG: _00EX, _00F4 --> _00F6
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01092__00F6 = _00F5_constant+1*v01086__00EX+1*v01095__00F4

# op _00Ff_power_combination_eval
# LANG: _00Fc, _00Fe --> _00Fg
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01101__00Fg = (v01099__00Fc**1)*(v01102__00Fe**1)
v01101__00Fg = (v01101__00Fg*_00Ff_coeff).reshape((1, 27, 3, 40, 10))

# op _00Fn_power_combination_eval
# LANG: _00Fk, _00Fm --> _00Fo
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01105__00Fo = (v01104__00Fk**1)*(v01106__00Fm**1)
v01105__00Fo = (v01105__00Fo*_00Fn_coeff).reshape((1, 27, 3, 40, 10))

# op _00Fp_bessel_eval
# LANG: _00CJ --> _00Fq
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01108__00Fq=_00Fp_bessel_eval(1,v0990__00CJ)

# op _00Fx_bessel_eval
# LANG: _00CJ --> _00Fy
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01112__00Fy=_00Fx_bessel_eval(1,v0990__00CJ)

# op _00G2_power_combination_eval
# LANG: _00BX, _00G1 --> _00G3
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01059__00G3 = (v01058__00G1**1)*(v0995__00BX**1)
v01059__00G3 = (v01059__00G3*_00G2_coeff).reshape((1, 27, 3, 40, 10))

# op _00Gc_power_combination_eval
# LANG: _00BX, _00Gb --> _00Gd
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01053__00Gd = (v01052__00Gb**1)*(v0995__00BX**1)
v01053__00Gd = (v01053__00Gd*_00Gc_coeff).reshape((1, 27, 3, 40, 10))

# op _00P7_power_combination_eval
# LANG: rotor_2_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v022_rotor_2_disk_origin = v022_rotor_2_disk_origin.reshape((3,))
v01395_origin = (v022_rotor_2_disk_origin**1)
v01395_origin = (v01395_origin*_00P7_coeff).reshape((3,))
v022_rotor_2_disk_origin = v022_rotor_2_disk_origin.reshape((1, 3))

# op _00Rk expand_array_eval
# LANG: aircraft_location --> _00Rl
# SHAPES: (3, 27) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01458__00Rl = np.einsum('bc,a->abc', v01457_aircraft_location.reshape((3, 27)) ,np.ones((1,))).reshape((1, 3, 27))

# op _00Rr_decompose_eval
# LANG: _00Ri --> _00Rs, _00RA, _00RH
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01464__00Rs = ((v01463__00Ri.flatten())[src_indices__00Rs__00Rr]).reshape((1, 1, 27))
v01465__00RA = ((v01463__00Ri.flatten())[src_indices__00RA__00Rr]).reshape((1, 1, 27))
v01466__00RH = ((v01463__00Ri.flatten())[src_indices__00RH__00Rr]).reshape((1, 1, 27))

# op _00Rt_decompose_eval
# LANG: _00Ro --> _00Ru, _00RB, _00RI
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01470__00Ru = ((v01469__00Ro.flatten())[src_indices__00Ru__00Rt]).reshape((1, 1, 27))
v01471__00RB = ((v01469__00Ro.flatten())[src_indices__00RB__00Rt]).reshape((1, 1, 27))
v01472__00RI = ((v01469__00Ro.flatten())[src_indices__00RI__00Rt]).reshape((1, 1, 27))

# op _00Tt expand_scalar_eval
# LANG: density --> _00Tu
# SHAPES: (1,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01595__00Tu = np.empty((1, 27, 3, 40, 11))
v01595__00Tu.fill(v01444_density.item())

# op _00UD_power_combination_eval
# LANG: _00UA, _00UC --> _00UE
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01550__00UE = (v01549__00UA**1)*(v01551__00UC**1)
v01550__00UE = (v01550__00UE*_00UD_coeff).reshape((1, 27, 3, 40, 10))

# op _00UL_power_combination_eval
# LANG: _00UI, _00UK --> _00UM
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01554__00UM = (v01553__00UI**1)*(v01555__00UK**1)
v01554__00UM = (v01554__00UM*_00UL_coeff).reshape((1, 27, 3, 40, 10))

# op _00UN_bessel_eval
# LANG: _00Uo --> _00UO
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01557__00UO=_00UN_bessel_eval(0,v01536__00Uo)

# op _00UT_bessel_eval
# LANG: _00Uo --> _00UU
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01559__00UU=_00UT_bessel_eval(1,v01536__00Uo)

# op _00UV_bessel_eval
# LANG: _00Uo --> _00UW
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01561__00UW=_00UV_bessel_eval(0,v01536__00Uo)

# op _00Uv_power_combination_eval
# LANG: _00Uq, _00Uu --> _00Uw
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01544__00Uw = (v01543__00Uq**1)*(v01546__00Uu**1)
v01544__00Uw = (v01544__00Uw*_00Uv_coeff).reshape((1, 27, 3, 40, 10))

# op _00Va_power_combination_eval
# LANG: _00V5, _00V9 --> _00Vb
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01566__00Vb = (v01565__00V5**1)*(v01568__00V9**1)
v01566__00Vb = (v01566__00Vb*_00Va_coeff).reshape((1, 27, 3, 40, 10))

# op _00Vi_power_combination_eval
# LANG: _00Vf, _00Vh --> _00Vj
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01572__00Vj = (v01571__00Vf**1)*(v01573__00Vh**1)
v01572__00Vj = (v01572__00Vj*_00Vi_coeff).reshape((1, 27, 3, 40, 10))

# op _00Vo_power_combination_eval
# LANG: _00Vn --> _00Vp
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01576__00Vp = (v01575__00Vn**2)
v01576__00Vp = (v01576__00Vp*_00Vo_coeff).reshape((1, 27, 3, 40, 10))

# op _00Vq_bessel_eval
# LANG: _00Uo --> _00Vr
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01578__00Vr=_00Vq_bessel_eval(1,v01536__00Uo)

# op _00Vy_bessel_eval
# LANG: _00Uo --> _00Vz
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01582__00Vz=_00Vy_bessel_eval(1,v01536__00Uo)

# op _00WL_linear_combination_eval
# LANG: _00WC, _00WK --> _00WM
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01638__00WM = _00WL_constant+1*v01632__00WC+1*v01641__00WK

# op _00WV_power_combination_eval
# LANG: _00WS, _00WU --> _00WW
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01647__00WW = (v01645__00WS**1)*(v01648__00WU**1)
v01647__00WW = (v01647__00WW*_00WV_coeff).reshape((1, 27, 3, 40, 10))

# op _00X2_power_combination_eval
# LANG: _00W_, _00X1 --> _00X3
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01651__00X3 = (v01650__00W_**1)*(v01652__00X1**1)
v01651__00X3 = (v01651__00X3*_00X2_coeff).reshape((1, 27, 3, 40, 10))

# op _00X4_bessel_eval
# LANG: _00Uo --> _00X5
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01654__00X5=_00X4_bessel_eval(1,v01536__00Uo)

# op _00XI_power_combination_eval
# LANG: _00TC, _00XH --> _00XJ
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01605__00XJ = (v01604__00XH**1)*(v01541__00TC**1)
v01605__00XJ = (v01605__00XJ*_00XI_coeff).reshape((1, 27, 3, 40, 10))

# op _00XS_power_combination_eval
# LANG: _00TC, _00XR --> _00XT
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01599__00XT = (v01598__00XR**1)*(v01541__00TC**1)
v01599__00XT = (v01599__00XT*_00XS_coeff).reshape((1, 27, 3, 40, 10))

# op _00Xc_bessel_eval
# LANG: _00Uo --> _00Xd
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01658__00Xd=_00Xc_bessel_eval(1,v01536__00Uo)

# op _00cM_linear_combination_eval
# LANG: _00cJ, _00cL --> _00cN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0285__00cN = _00cM_constant+1*v0283__00cJ+1*v0286__00cL

# op _00cy_power_combination_eval
# LANG: _00ct, _00cx --> _00cz
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0276__00cz = (v0275__00ct**1)*(v0278__00cx**1)
v0276__00cz = (v0276__00cz*_00cy_coeff).reshape((1, 40, 30))

# op _00dv_power_combination_eval
# LANG: _radius --> _00dw
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0318__00dw = (v0214__radius**1)
v0318__00dw = (v0318__00dw*_00dv_coeff).reshape((1, 40, 30))

# op _00e__power_combination_eval
# LANG: _00bU, _00eZ --> _00f0
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0375__00f0 = (v0374__00eZ**1)*(v0320__00bU**1)
v0375__00f0 = (v0375__00f0*_00e__coeff).reshape((1, 40, 30))

# op _00f9_linear_combination_eval
# LANG: _00f2, _00f8 --> _00fa
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0378__00fa = _00f9_constant+1*v0377__00f2+1*v0381__00f8

# op _00kV_linear_combination_eval
# LANG: _00kU, propeller_radius --> _00kW
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0564__00kW = _00kV_constant+1*v0495_propeller_radius+-1*v0565__00kU

# op _00rB_power_combination_eval
# LANG: _00rw, _00rA --> _00rC
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0649__00rC = (v0648__00rw**1)*(v0651__00rA**1)
v0649__00rC = (v0649__00rC*_00rB_coeff).reshape((1, 40, 30))

# op _00rP_linear_combination_eval
# LANG: _00rM, _00rO --> _00rQ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0658__00rQ = _00rP_constant+1*v0656__00rM+1*v0659__00rO

# op _00sy_power_combination_eval
# LANG: _radius --> _00sz
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0691__00sz = (v0587__radius**1)
v0691__00sz = (v0691__00sz*_00sy_coeff).reshape((1, 40, 30))

# op _00u2_power_combination_eval
# LANG: _00qX, _00u1 --> _00u3
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0748__00u3 = (v0747__00u1**1)*(v0693__00qX**1)
v0748__00u3 = (v0748__00u3*_00u2_coeff).reshape((1, 40, 30))

# op _00uc_linear_combination_eval
# LANG: _00u5, _00ub --> _00ud
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0751__00ud = _00uc_constant+1*v0750__00u5+1*v0754__00ub

# op _00xs_power_combination_eval
# LANG: rotor_1_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v012_rotor_1_disk_origin = v012_rotor_1_disk_origin.reshape((3,))
v0849_origin = (v012_rotor_1_disk_origin**1)
v0849_origin = (v0849_origin*_00xs_coeff).reshape((3,))
v012_rotor_1_disk_origin = v012_rotor_1_disk_origin.reshape((1, 3))

# op _00zF expand_array_eval
# LANG: aircraft_location --> _00zG
# SHAPES: (3, 27) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0912__00zG = np.einsum('bc,a->abc', v0911_aircraft_location.reshape((3, 27)) ,np.ones((1,))).reshape((1, 3, 27))

# op _00zM_decompose_eval
# LANG: _00zD --> _00zN, _00zV, _00A1
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0918__00zN = ((v0917__00zD.flatten())[src_indices__00zN__00zM]).reshape((1, 1, 27))
v0919__00zV = ((v0917__00zD.flatten())[src_indices__00zV__00zM]).reshape((1, 1, 27))
v0920__00A1 = ((v0917__00zD.flatten())[src_indices__00A1__00zM]).reshape((1, 1, 27))

# op _00zO_decompose_eval
# LANG: _00zJ --> _00zP, _00zW, _00A2
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0924__00zP = ((v0923__00zJ.flatten())[src_indices__00zP__00zO]).reshape((1, 1, 27))
v0925__00zW = ((v0923__00zJ.flatten())[src_indices__00zW__00zO]).reshape((1, 1, 27))
v0926__00A2 = ((v0923__00zJ.flatten())[src_indices__00A2__00zO]).reshape((1, 1, 27))

# op _005U_power_combination_eval
# LANG: _005T --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v0193_dr = (v0191__005T**1)
v0193_dr = (v0193_dr*_005U_coeff).reshape((1,))

# op _00Ae expand_array_eval
# LANG: origin --> _00Af
# SHAPES: (3,) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0935__00Af = np.einsum('b,ac->abc', v0849_origin.reshape((3,)) ,np.ones((1, 27))).reshape((1, 3, 27))

# op _00C1_decompose_eval
# LANG: _00BP --> _00C2
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01050__00C2 = ((v01049__00BP.flatten())[src_indices__00C2__00C1]).reshape((1, 27, 3, 40, 10))

# op _00C__linear_combination_eval
# LANG: _00CR, _00CZ --> _00D0
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01001__00D0 = _00C__constant+1*v0998__00CR+-1*v01004__00CZ

# op _00D9_power_combination_eval
# LANG: _00D6, _00D8 --> _00Da
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01010__00Da = (v01008__00D6**1)*(v01011__00D8**1)
v01010__00Da = (v01010__00Da*_00D9_coeff).reshape((1, 27, 3, 40, 10))

# op _00DF_linear_combination_eval
# LANG: _00Dw, _00DE --> _00DG
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01023__00DG = _00DF_constant+1*v01020__00Dw+1*v01026__00DE

# op _00DN_power_combination_eval
# LANG: _00DK, _00DM --> _00DO
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01031__00DO = (v01030__00DK**1)*(v01032__00DM**1)
v01031__00DO = (v01031__00DO*_00DN_coeff).reshape((1, 27, 3, 40, 10))

# op _00DR_bessel_eval
# LANG: _00CJ --> _00DS
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01034__00DS=_00DR_bessel_eval(0,v0990__00CJ)

# op _00DV_power_combination_eval
# LANG: _00DU --> _00DW
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01037__00DW = (v01036__00DU**2)
v01037__00DW = (v01037__00DW*_00DV_coeff).reshape((1, 27, 3, 40, 10))

# op _00Dh_power_combination_eval
# LANG: _00De, _00Dg --> _00Di
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01014__00Di = (v01013__00De**1)*(v01015__00Dg**1)
v01014__00Di = (v01014__00Di*_00Dh_coeff).reshape((1, 27, 3, 40, 10))

# op _00Dj_bessel_eval
# LANG: _00CJ --> _00Dk
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01017__00Dk=_00Dj_bessel_eval(1,v0990__00CJ)

# op _00E2_bessel_eval
# LANG: _00CJ --> _00E3
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01039__00E3=_00E2_bessel_eval(1,v0990__00CJ)

# op _00E4_bessel_eval
# LANG: _00CJ --> _00E5
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01041__00E5=_00E4_bessel_eval(0,v0990__00CJ)

# op _00Ea_bessel_eval
# LANG: _00CJ --> _00Eb
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01044__00Eb=_00Ea_bessel_eval(0,v0990__00CJ)

# op _00Ec_bessel_eval
# LANG: _00CJ --> _00Ed
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01046__00Ed=_00Ec_bessel_eval(1,v0990__00CJ)

# op _00FH_bessel_eval
# LANG: _00CJ --> _00FI
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01116__00FI=_00FH_bessel_eval(1,v0990__00CJ)

# op _00FJ_bessel_eval
# LANG: _00CJ --> _00FK
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01118__00FK=_00FJ_bessel_eval(0,v0990__00CJ)

# op _00FP_bessel_eval
# LANG: _00CJ --> _00FQ
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01121__00FQ=_00FP_bessel_eval(0,v0990__00CJ)

# op _00FR_bessel_eval
# LANG: _00CJ --> _00FS
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01123__00FS=_00FR_bessel_eval(1,v0990__00CJ)

# op _00Fh_linear_combination_eval
# LANG: _00F6, _00Fg --> _00Fi
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01097__00Fi = _00Fh_constant+1*v01092__00F6+-1*v01101__00Fg

# op _00Fr_power_combination_eval
# LANG: _00Fo, _00Fq --> _00Fs
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01107__00Fs = (v01105__00Fo**1)*(v01108__00Fq**1)
v01107__00Fs = (v01107__00Fs*_00Fr_coeff).reshape((1, 27, 3, 40, 10))

# op _00Fv_bessel_eval
# LANG: _00CJ --> _00Fw
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01110__00Fw=_00Fv_bessel_eval(1,v0990__00CJ)

# op _00Fz_power_combination_eval
# LANG: _00Fy --> _00FA
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01113__00FA = (v01112__00Fy**2)
v01113__00FA = (v01113__00FA*_00Fz_coeff).reshape((1, 27, 3, 40, 10))

# op _00G4_power_combination_eval
# LANG: _00Cx, _00G3 --> _00G5
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01060__00G5 = (v01059__00G3**1)*(v0980__00Cx**-1)
v01060__00G5 = (v01060__00G5*_00G4_coeff).reshape((1, 27, 3, 40, 10))

# op _00Ge_linear_combination_eval
# LANG: _00Gd --> _00Gf
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01054__00Gf = _00Ge_constant+1*v01053__00Gd

# op _00Pr_power_combination_eval
# LANG: propeller_radius --> _00Ps
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01402__00Ps = (v01398_propeller_radius**1)
v01402__00Ps = (v01402__00Ps*_00Pr_coeff).reshape((1,))

# op _00RC_power_combination_eval
# LANG: _00RA, _00RB --> _00RD
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01474__00RD = (v01465__00RA**1)*(v01471__00RB**1)
v01474__00RD = (v01474__00RD*_00RC_coeff).reshape((1, 1, 27))

# op _00RU expand_array_eval
# LANG: origin --> _00RV
# SHAPES: (3,) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01481__00RV = np.einsum('b,ac->abc', v01395_origin.reshape((3,)) ,np.ones((1, 27))).reshape((1, 3, 27))

# op _00Rp_decompose_eval
# LANG: _00Rl --> _00Rq, _00Rz, _00RG
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01459__00Rq = ((v01458__00Rl.flatten())[src_indices__00Rq__00Rp]).reshape((1, 1, 27))
v01460__00Rz = ((v01458__00Rl.flatten())[src_indices__00Rz__00Rp]).reshape((1, 1, 27))
v01461__00RG = ((v01458__00Rl.flatten())[src_indices__00RG__00Rp]).reshape((1, 1, 27))

# op _00Rv_power_combination_eval
# LANG: _00Rs, _00Ru --> _00Rw
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01467__00Rw = (v01464__00Rs**1)*(v01470__00Ru**1)
v01467__00Rw = (v01467__00Rw*_00Rv_coeff).reshape((1, 1, 27))

# op _00TH_decompose_eval
# LANG: _00Tu --> _00TI
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01596__00TI = ((v01595__00Tu.flatten())[src_indices__00TI__00TH]).reshape((1, 27, 3, 40, 10))

# op _00UF_linear_combination_eval
# LANG: _00Uw, _00UE --> _00UG
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01547__00UG = _00UF_constant+1*v01544__00Uw+-1*v01550__00UE

# op _00UP_power_combination_eval
# LANG: _00UM, _00UO --> _00UQ
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01556__00UQ = (v01554__00UM**1)*(v01557__00UO**1)
v01556__00UQ = (v01556__00UQ*_00UP_coeff).reshape((1, 27, 3, 40, 10))

# op _00UX_power_combination_eval
# LANG: _00UU, _00UW --> _00UY
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01560__00UY = (v01559__00UU**1)*(v01561__00UW**1)
v01560__00UY = (v01560__00UY*_00UX_coeff).reshape((1, 27, 3, 40, 10))

# op _00UZ_bessel_eval
# LANG: _00Uo --> _00U_
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01563__00U_=_00UZ_bessel_eval(1,v01536__00Uo)

# op _00VA_power_combination_eval
# LANG: _00Vz --> _00VB
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01583__00VB = (v01582__00Vz**2)
v01583__00VB = (v01583__00VB*_00VA_coeff).reshape((1, 27, 3, 40, 10))

# op _00VI_bessel_eval
# LANG: _00Uo --> _00VJ
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01585__00VJ=_00VI_bessel_eval(1,v01536__00Uo)

# op _00VK_bessel_eval
# LANG: _00Uo --> _00VL
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01587__00VL=_00VK_bessel_eval(0,v01536__00Uo)

# op _00VQ_bessel_eval
# LANG: _00Uo --> _00VR
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01590__00VR=_00VQ_bessel_eval(0,v01536__00Uo)

# op _00VS_bessel_eval
# LANG: _00Uo --> _00VT
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01592__00VT=_00VS_bessel_eval(1,v01536__00Uo)

# op _00Vk_linear_combination_eval
# LANG: _00Vb, _00Vj --> _00Vl
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01569__00Vl = _00Vk_constant+1*v01566__00Vb+1*v01572__00Vj

# op _00Vs_power_combination_eval
# LANG: _00Vp, _00Vr --> _00Vt
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01577__00Vt = (v01576__00Vp**1)*(v01578__00Vr**1)
v01577__00Vt = (v01577__00Vt*_00Vs_coeff).reshape((1, 27, 3, 40, 10))

# op _00Vw_bessel_eval
# LANG: _00Uo --> _00Vx
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01580__00Vx=_00Vw_bessel_eval(0,v01536__00Uo)

# op _00WX_linear_combination_eval
# LANG: _00WM, _00WW --> _00WY
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01643__00WY = _00WX_constant+1*v01638__00WM+-1*v01647__00WW

# op _00X6_power_combination_eval
# LANG: _00X3, _00X5 --> _00X7
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01653__00X7 = (v01651__00X3**1)*(v01654__00X5**1)
v01653__00X7 = (v01653__00X7*_00X6_coeff).reshape((1, 27, 3, 40, 10))

# op _00XK_power_combination_eval
# LANG: _00Uc, _00XJ --> _00XL
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01606__00XL = (v01605__00XJ**1)*(v01526__00Uc**-1)
v01606__00XL = (v01606__00XL*_00XK_coeff).reshape((1, 27, 3, 40, 10))

# op _00XU_linear_combination_eval
# LANG: _00XT --> _00XV
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01600__00XV = _00XU_constant+1*v01599__00XT

# op _00Xa_bessel_eval
# LANG: _00Uo --> _00Xb
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01656__00Xb=_00Xa_bessel_eval(1,v01536__00Uo)

# op _00Xe_power_combination_eval
# LANG: _00Xd --> _00Xf
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01659__00Xf = (v01658__00Xd**2)
v01659__00Xf = (v01659__00Xf*_00Xe_coeff).reshape((1, 27, 3, 40, 10))

# op _00Xm_bessel_eval
# LANG: _00Uo --> _00Xn
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01662__00Xn=_00Xm_bessel_eval(1,v01536__00Uo)

# op _00Xo_bessel_eval
# LANG: _00Uo --> _00Xp
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01664__00Xp=_00Xo_bessel_eval(0,v01536__00Uo)

# op _00Xu_bessel_eval
# LANG: _00Uo --> _00Xv
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01667__00Xv=_00Xu_bessel_eval(0,v01536__00Uo)

# op _00Xw_bessel_eval
# LANG: _00Uo --> _00Xx
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01669__00Xx=_00Xw_bessel_eval(1,v01536__00Uo)

# op _00cO_power_combination_eval
# LANG: _00cz, _00cN --> _ux
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0279__ux = (v0276__00cz**1)*(v0285__00cN**-1)
v0279__ux = (v0279__ux*_00cO_coeff).reshape((1, 40, 30))

# op _00dx_power_combination_eval
# LANG: _00dw, _00bU --> _00dy
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0319__00dy = (v0318__00dw**1)*(v0320__00bU**1)
v0319__00dy = (v0319__00dy*_00dx_coeff).reshape((1, 40, 30))

# op _00fb_power_combination_eval
# LANG: _00f0, _00fa --> _00fc
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0376__00fc = (v0375__00f0**1)*(v0378__00fa**1)
v0376__00fc = (v0376__00fc*_00fb_coeff).reshape((1, 40, 30))

# op _00kX_power_combination_eval
# LANG: _00kW --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v0566_dr = (v0564__00kW**1)
v0566_dr = (v0566_dr*_00kX_coeff).reshape((1,))

# op _00rR_power_combination_eval
# LANG: _00rC, _00rQ --> _ux
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0652__ux = (v0649__00rC**1)*(v0658__00rQ**-1)
v0652__ux = (v0652__ux*_00rR_coeff).reshape((1, 40, 30))

# op _00sA_power_combination_eval
# LANG: _00sz, _00qX --> _00sB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0692__00sB = (v0691__00sz**1)*(v0693__00qX**1)
v0692__00sB = (v0692__00sB*_00sA_coeff).reshape((1, 40, 30))

# op _00ue_power_combination_eval
# LANG: _00u3, _00ud --> _00uf
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0749__00uf = (v0748__00u3**1)*(v0751__00ud**1)
v0749__00uf = (v0749__00uf*_00ue_coeff).reshape((1, 40, 30))

# op _00xM_power_combination_eval
# LANG: propeller_radius --> _00xN
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0856__00xN = (v0852_propeller_radius**1)
v0856__00xN = (v0856__00xN*_00xM_coeff).reshape((1,))

# op _00zK_decompose_eval
# LANG: _00zG --> _00zL, _00zU, _00A0
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0913__00zL = ((v0912__00zG.flatten())[src_indices__00zL__00zK]).reshape((1, 1, 27))
v0914__00zU = ((v0912__00zG.flatten())[src_indices__00zU__00zK]).reshape((1, 1, 27))
v0915__00A0 = ((v0912__00zG.flatten())[src_indices__00A0__00zK]).reshape((1, 1, 27))

# op _00zQ_power_combination_eval
# LANG: _00zN, _00zP --> _00zR
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0921__00zR = (v0918__00zN**1)*(v0924__00zP**1)
v0921__00zR = (v0921__00zR*_00zQ_coeff).reshape((1, 1, 27))

# op _00zX_power_combination_eval
# LANG: _00zV, _00zW --> _00zY
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0928__00zY = (v0919__00zV**1)*(v0925__00zW**1)
v0928__00zY = (v0928__00zY*_00zX_coeff).reshape((1, 1, 27))

# op _0071 expand_scalar_eval
# LANG: dr --> _dr
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_core_inputs_model
v0202__dr = np.empty((1, 40, 30))
v0202__dr.fill(v0193_dr.item())

# op _00A3_power_combination_eval
# LANG: _00A1, _00A2 --> _00A4
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0930__00A4 = (v0920__00A1**1)*(v0926__00A2**1)
v0930__00A4 = (v0930__00A4*_00A3_coeff).reshape((1, 1, 27))

# op _00Ag_decompose_eval
# LANG: _00Af --> _00Ah, _00Am, _00Ar
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0936__00Ah = ((v0935__00Af.flatten())[src_indices__00Ah__00Ag]).reshape((1, 1, 27))
v0937__00Am = ((v0935__00Af.flatten())[src_indices__00Am__00Ag]).reshape((1, 1, 27))
v0938__00Ar = ((v0935__00Af.flatten())[src_indices__00Ar__00Ag]).reshape((1, 1, 27))

# op _00DP_linear_combination_eval
# LANG: _00DG, _00DO --> _00DQ
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01028__00DQ = _00DP_constant+1*v01023__00DG+-1*v01031__00DO

# op _00DX_power_combination_eval
# LANG: _00DS, _00DW --> _00DY
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01035__00DY = (v01034__00DS**1)*(v01037__00DW**1)
v01035__00DY = (v01035__00DY*_00DX_coeff).reshape((1, 27, 3, 40, 10))

# op _00Db_linear_combination_eval
# LANG: _00D0, _00Da --> _00Dc
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01006__00Dc = _00Db_constant+1*v01001__00D0+1*v01010__00Da

# op _00Dl_power_combination_eval
# LANG: _00Di, _00Dk --> _00Dm
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01016__00Dm = (v01014__00Di**1)*(v01017__00Dk**1)
v01016__00Dm = (v01016__00Dm*_00Dl_coeff).reshape((1, 27, 3, 40, 10))

# op _00E6_linear_combination_eval
# LANG: _00E3, _00E5 --> _00E7
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01040__00E7 = _00E6_constant+1*v01039__00E3+1*v01041__00E5

# op _00Ee_linear_combination_eval
# LANG: _00Eb, _00Ed --> _00Ef
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01045__00Ef = _00Ee_constant+1*v01044__00Eb+-1*v01046__00Ed

# op _00FB_power_combination_eval
# LANG: _00Fw, _00FA --> _00FC
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01111__00FC = (v01110__00Fw**1)*(v01113__00FA**1)
v01111__00FC = (v01111__00FC*_00FB_coeff).reshape((1, 27, 3, 40, 10))

# op _00FL_linear_combination_eval
# LANG: _00FI, _00FK --> _00FM
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01117__00FM = _00FL_constant+1*v01116__00FI+1*v01118__00FK

# op _00FT_linear_combination_eval
# LANG: _00FQ, _00FS --> _00FU
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01122__00FU = _00FT_constant+1*v01121__00FQ+-1*v01123__00FS

# op _00Ft_linear_combination_eval
# LANG: _00Fi, _00Fs --> _00Fu
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01103__00Fu = _00Ft_constant+1*v01097__00Fi+-1*v01107__00Fs

# op _00G6_power_combination_eval
# LANG: _00G5 --> _00G7
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01061__00G7 = (v01060__00G5**1)
v01061__00G7 = (v01061__00G7*_00G6_coeff).reshape((1, 27, 3, 40, 10))

# op _00Gg_power_combination_eval
# LANG: _00C2, _00Gf --> _00Gh
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01051__00Gh = (v01050__00C2**1)*(v01054__00Gf**1)
v01051__00Gh = (v01051__00Gh*_00Gg_coeff).reshape((1, 27, 3, 40, 10))

# op _00Pt_power_combination_eval
# LANG: _00Ps --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01403_dr = (v01402__00Ps**1)
v01403_dr = (v01403_dr*_00Pt_coeff).reshape((1,))

# op _00RE_linear_combination_eval
# LANG: _00Rz, _00RD --> aircraft_y_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01473_aircraft_y_pos = _00RE_constant+1*v01460__00Rz+1*v01474__00RD

# op _00RJ_power_combination_eval
# LANG: _00RH, _00RI --> _00RK
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01476__00RK = (v01466__00RH**1)*(v01472__00RI**1)
v01476__00RK = (v01476__00RK*_00RJ_coeff).reshape((1, 1, 27))

# op _00RW_decompose_eval
# LANG: _00RV --> _00RX, _00S1, _00S6
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01482__00RX = ((v01481__00RV.flatten())[src_indices__00RX__00RW]).reshape((1, 1, 27))
v01483__00S1 = ((v01481__00RV.flatten())[src_indices__00S1__00RW]).reshape((1, 1, 27))
v01484__00S6 = ((v01481__00RV.flatten())[src_indices__00S6__00RW]).reshape((1, 1, 27))

# op _00Rx_linear_combination_eval
# LANG: _00Rq, _00Rw --> aircraft_x_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01462_aircraft_x_pos = _00Rx_constant+1*v01459__00Rq+1*v01467__00Rw

# op _00UR_linear_combination_eval
# LANG: _00UG, _00UQ --> _00US
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01552__00US = _00UR_constant+1*v01547__00UG+1*v01556__00UQ

# op _00V0_power_combination_eval
# LANG: _00UY, _00U_ --> _00V1
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01562__00V1 = (v01560__00UY**1)*(v01563__00U_**1)
v01562__00V1 = (v01562__00V1*_00V0_coeff).reshape((1, 27, 3, 40, 10))

# op _00VC_power_combination_eval
# LANG: _00Vx, _00VB --> _00VD
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01581__00VD = (v01580__00Vx**1)*(v01583__00VB**1)
v01581__00VD = (v01581__00VD*_00VC_coeff).reshape((1, 27, 3, 40, 10))

# op _00VM_linear_combination_eval
# LANG: _00VJ, _00VL --> _00VN
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01586__00VN = _00VM_constant+1*v01585__00VJ+1*v01587__00VL

# op _00VU_linear_combination_eval
# LANG: _00VR, _00VT --> _00VV
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01591__00VV = _00VU_constant+1*v01590__00VR+-1*v01592__00VT

# op _00Vu_linear_combination_eval
# LANG: _00Vl, _00Vt --> _00Vv
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01574__00Vv = _00Vu_constant+1*v01569__00Vl+-1*v01577__00Vt

# op _00X8_linear_combination_eval
# LANG: _00WY, _00X7 --> _00X9
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01649__00X9 = _00X8_constant+1*v01643__00WY+-1*v01653__00X7

# op _00XM_power_combination_eval
# LANG: _00XL --> _00XN
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01607__00XN = (v01606__00XL**1)
v01607__00XN = (v01607__00XN*_00XM_coeff).reshape((1, 27, 3, 40, 10))

# op _00XW_power_combination_eval
# LANG: _00TI, _00XV --> _00XX
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01597__00XX = (v01596__00TI**1)*(v01600__00XV**1)
v01597__00XX = (v01597__00XX*_00XW_coeff).reshape((1, 27, 3, 40, 10))

# op _00Xg_power_combination_eval
# LANG: _00Xb, _00Xf --> _00Xh
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01657__00Xh = (v01656__00Xb**1)*(v01659__00Xf**1)
v01657__00Xh = (v01657__00Xh*_00Xg_coeff).reshape((1, 27, 3, 40, 10))

# op _00Xq_linear_combination_eval
# LANG: _00Xn, _00Xp --> _00Xr
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01663__00Xr = _00Xq_constant+1*v01662__00Xn+1*v01664__00Xp

# op _00Xy_linear_combination_eval
# LANG: _00Xv, _00Xx --> _00Xz
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01668__00Xz = _00Xy_constant+1*v01667__00Xv+-1*v01669__00Xx

# op _00dB_linear_combination_eval
# LANG: _ux, _axial_inflow_velocity --> _00dC
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0323__00dC = _00dB_constant+1*v0279__ux+-1*v0221__axial_inflow_velocity

# op _00dz_power_combination_eval
# LANG: _ux, _00dy --> _00dA
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0321__00dA = (v0319__00dy**1)*(v0279__ux**1)
v0321__00dA = (v0321__00dA*_00dz_coeff).reshape((1, 40, 30))

# op _00fd_power_combination_eval
# LANG: _00fc, _chord --> _00fe
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0382__00fe = (v0376__00fc**1)*(v0209__chord**1)
v0382__00fe = (v0382__00fe*_00fd_coeff).reshape((1, 40, 30))

# op _00m4 expand_scalar_eval
# LANG: dr --> _dr
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_core_inputs_model
v0575__dr = np.empty((1, 40, 30))
v0575__dr.fill(v0566_dr.item())

# op _00sC_power_combination_eval
# LANG: _ux, _00sB --> _00sD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0694__00sD = (v0692__00sB**1)*(v0652__ux**1)
v0694__00sD = (v0694__00sD*_00sC_coeff).reshape((1, 40, 30))

# op _00sE_linear_combination_eval
# LANG: _ux, _axial_inflow_velocity --> _00sF
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0696__00sF = _00sE_constant+1*v0652__ux+-1*v0594__axial_inflow_velocity

# op _00ug_power_combination_eval
# LANG: _00uf, _chord --> _00uh
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0755__00uh = (v0749__00uf**1)*(v0582__chord**1)
v0755__00uh = (v0755__00uh*_00ug_coeff).reshape((1, 40, 30))

# op _00xO_power_combination_eval
# LANG: _00xN --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0857_dr = (v0856__00xN**1)
v0857_dr = (v0857_dr*_00xO_coeff).reshape((1,))

# op _00zS_linear_combination_eval
# LANG: _00zL, _00zR --> aircraft_x_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0916_aircraft_x_pos = _00zS_constant+1*v0913__00zL+1*v0921__00zR

# op _00zZ_linear_combination_eval
# LANG: _00zU, _00zY --> aircraft_y_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0927_aircraft_y_pos = _00zZ_constant+1*v0914__00zU+1*v0928__00zY

# op _00A5_linear_combination_eval
# LANG: _00A0, _00A4 --> aircraft_z_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0929_aircraft_z_pos = _00A5_constant+1*v0915__00A0+1*v0930__00A4

# op _00A7 expand_array_eval
# LANG: init_obs_x_loc --> _00A8
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0932__00A8 = np.einsum('c,ab->abc', v0931_init_obs_x_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _00A9 expand_array_eval
# LANG: init_obs_y_loc --> _00Aa
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0940__00Aa = np.einsum('c,ab->abc', v0939_init_obs_y_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _00Ai_linear_combination_eval
# LANG: aircraft_x_pos, _00Ah --> _00Aj
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0934__00Aj = _00Ai_constant+1*v0916_aircraft_x_pos+1*v0936__00Ah

# op _00An_linear_combination_eval
# LANG: aircraft_y_pos, _00Am --> _00Ao
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0942__00Ao = _00An_constant+1*v0927_aircraft_y_pos+1*v0937__00Am

# op _00Bq expand_scalar_eval
# LANG: dr --> _00Br
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0968__00Br = np.empty((1, 40, 30))
v0968__00Br.fill(v0857_dr.item())

# op _00DZ_linear_combination_eval
# LANG: _00DQ, _00DY --> _00D_
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01033__00D_ = _00DZ_constant+1*v01028__00DQ+-1*v01035__00DY

# op _00Dn_linear_combination_eval
# LANG: _00Dc, _00Dm --> _00Do
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01012__00Do = _00Dn_constant+1*v01006__00Dc+-1*v01016__00Dm

# op _00E8_power_combination_eval
# LANG: _00E7 --> _00E9
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01042__00E9 = (v01040__00E7**2)
v01042__00E9 = (v01042__00E9*_00E8_coeff).reshape((1, 27, 3, 40, 10))

# op _00Eg_power_combination_eval
# LANG: _00Ef --> _00Eh
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01047__00Eh = (v01045__00Ef**2)
v01047__00Eh = (v01047__00Eh*_00Eg_coeff).reshape((1, 27, 3, 40, 10))

# op _00FD_linear_combination_eval
# LANG: _00Fu, _00FC --> _00FE
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01109__00FE = _00FD_constant+1*v01103__00Fu+1*v01111__00FC

# op _00FN_power_combination_eval
# LANG: _00FM --> _00FO
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01119__00FO = (v01117__00FM**2)
v01119__00FO = (v01119__00FO*_00FN_coeff).reshape((1, 27, 3, 40, 10))

# op _00FV_power_combination_eval
# LANG: _00FU --> _00FW
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01124__00FW = (v01122__00FU**2)
v01124__00FW = (v01124__00FW*_00FV_coeff).reshape((1, 27, 3, 40, 10))

# op _00G8_power_combination_eval
# LANG: _00G7 --> _00G9
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01062__00G9 = (v01061__00G7**1)
v01062__00G9 = (v01062__00G9*_00G8_coeff).reshape((1, 27, 3, 40, 10))

# op _00Gi_power_combination_eval
# LANG: _00C0, _00Gh --> _00Gj
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01055__00Gj = (v01051__00Gh**1)*(v0989__00C0**1)
v01055__00Gj = (v01055__00Gj*_00Gi_coeff).reshape((1, 27, 3, 40, 10))

# op _00RL_linear_combination_eval
# LANG: _00RG, _00RK --> aircraft_z_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01475_aircraft_z_pos = _00RL_constant+1*v01461__00RG+1*v01476__00RK

# op _00RN expand_array_eval
# LANG: init_obs_x_loc --> _00RO
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01478__00RO = np.einsum('c,ab->abc', v01477_init_obs_x_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _00RP expand_array_eval
# LANG: init_obs_y_loc --> _00RQ
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01486__00RQ = np.einsum('c,ab->abc', v01485_init_obs_y_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _00RY_linear_combination_eval
# LANG: aircraft_x_pos, _00RX --> _00RZ
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01480__00RZ = _00RY_constant+1*v01462_aircraft_x_pos+1*v01482__00RX

# op _00S2_linear_combination_eval
# LANG: aircraft_y_pos, _00S1 --> _00S3
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01488__00S3 = _00S2_constant+1*v01473_aircraft_y_pos+1*v01483__00S1

# op _00T5 expand_scalar_eval
# LANG: dr --> _00T6
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01514__00T6 = np.empty((1, 40, 30))
v01514__00T6.fill(v01403_dr.item())

# op _00V2_linear_combination_eval
# LANG: _00US, _00V1 --> _00V3
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01558__00V3 = _00V2_constant+1*v01552__00US+-1*v01562__00V1

# op _00VE_linear_combination_eval
# LANG: _00Vv, _00VD --> _00VF
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01579__00VF = _00VE_constant+1*v01574__00Vv+-1*v01581__00VD

# op _00VO_power_combination_eval
# LANG: _00VN --> _00VP
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01588__00VP = (v01586__00VN**2)
v01588__00VP = (v01588__00VP*_00VO_coeff).reshape((1, 27, 3, 40, 10))

# op _00VW_power_combination_eval
# LANG: _00VV --> _00VX
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01593__00VX = (v01591__00VV**2)
v01593__00VX = (v01593__00VX*_00VW_coeff).reshape((1, 27, 3, 40, 10))

# op _00XA_power_combination_eval
# LANG: _00Xz --> _00XB
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01670__00XB = (v01668__00Xz**2)
v01670__00XB = (v01670__00XB*_00XA_coeff).reshape((1, 27, 3, 40, 10))

# op _00XO_power_combination_eval
# LANG: _00XN --> _00XP
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01608__00XP = (v01607__00XN**1)
v01608__00XP = (v01608__00XP*_00XO_coeff).reshape((1, 27, 3, 40, 10))

# op _00XY_power_combination_eval
# LANG: _00TG, _00XX --> _00XZ
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01601__00XZ = (v01597__00XX**1)*(v01535__00TG**1)
v01601__00XZ = (v01601__00XZ*_00XY_coeff).reshape((1, 27, 3, 40, 10))

# op _00Xi_linear_combination_eval
# LANG: _00X9, _00Xh --> _00Xj
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01655__00Xj = _00Xi_constant+1*v01649__00X9+1*v01657__00Xh

# op _00Xs_power_combination_eval
# LANG: _00Xr --> _00Xt
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01665__00Xt = (v01663__00Xr**2)
v01665__00Xt = (v01665__00Xt*_00Xs_coeff).reshape((1, 27, 3, 40, 10))

# op _00dD_power_combination_eval
# LANG: _00dA, _00dC --> _00dE
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0322__00dE = (v0321__00dA**1)*(v0323__00dC**1)
v0322__00dE = (v0322__00dE*_00dD_coeff).reshape((1, 40, 30))

# op _00ff_power_combination_eval
# LANG: _00fe, _dr --> _dD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0383__dD = (v0382__00fe**1)*(v0202__dr**1)
v0383__dD = (v0383__dD*_00ff_coeff).reshape((1, 40, 30))

# op _00sG_power_combination_eval
# LANG: _00sD, _00sF --> _00sH
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0695__00sH = (v0694__00sD**1)*(v0696__00sF**1)
v0695__00sH = (v0695__00sH*_00sG_coeff).reshape((1, 40, 30))

# op _00ui_power_combination_eval
# LANG: _00uh, _dr --> _dD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0756__dD = (v0755__00uh**1)*(v0575__dr**1)
v0756__dD = (v0756__dD*_00ui_coeff).reshape((1, 40, 30))

# op _00Ab expand_array_eval
# LANG: init_obs_z_loc --> _00Ac
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0944__00Ac = np.einsum('c,ab->abc', v0943_init_obs_z_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _00Ak_linear_combination_eval
# LANG: _00A8, _00Aj --> rel_obs_x_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0933_rel_obs_x_pos = _00Ak_constant+1*v0932__00A8+-1*v0934__00Aj

# op _00Ap_linear_combination_eval
# LANG: _00Aa, _00Ao --> rel_obs_y_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0941_rel_obs_y_pos = _00Ap_constant+1*v0940__00Aa+-1*v0942__00Ao

# op _00As_linear_combination_eval
# LANG: aircraft_z_pos, _00Ar --> _00At
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0946__00At = _00As_constant+1*v0929_aircraft_z_pos+1*v0938__00Ar

# op _00Bs_power_combination_eval
# LANG: _00Br, _dD --> bbb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0967_bbb = (v0756__dD**1)*(v0968__00Br**-1)
v0967_bbb = (v0967_bbb*_00Bs_coeff).reshape((1, 40, 30))

# op _00E0_linear_combination_eval
# LANG: _00Do, _00D_ --> _00E1
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01018__00E1 = _00E0_constant+1*v01012__00Do+-1*v01033__00D_

# op _00Ei_linear_combination_eval
# LANG: _00E9, _00Eh --> _00Ej
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01043__00Ej = _00Ei_constant+1*v01042__00E9+1*v01047__00Eh

# op _00FF_linear_combination_eval
# LANG: _00FE --> _00FG
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01114__00FG = _00FF_constant+-1*v01109__00FE

# op _00FX_linear_combination_eval
# LANG: _00FO, _00FW --> _00FY
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01120__00FY = _00FX_constant+1*v01119__00FO+1*v01124__00FW

# op _00Gk_power_combination_eval
# LANG: _00Gj, _00G9 --> _00Gl
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01056__00Gl = (v01055__00Gj**1)*(v01062__00G9**1)
v01056__00Gl = (v01056__00Gl*_00Gk_coeff).reshape((1, 27, 3, 40, 10))

# op _00RR expand_array_eval
# LANG: init_obs_z_loc --> _00RS
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01490__00RS = np.einsum('c,ab->abc', v01489_init_obs_z_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _00R__linear_combination_eval
# LANG: _00RO, _00RZ --> rel_obs_x_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01479_rel_obs_x_pos = _00R__constant+1*v01478__00RO+-1*v01480__00RZ

# op _00S4_linear_combination_eval
# LANG: _00RQ, _00S3 --> rel_obs_y_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01487_rel_obs_y_pos = _00S4_constant+1*v01486__00RQ+-1*v01488__00S3

# op _00S7_linear_combination_eval
# LANG: aircraft_z_pos, _00S6 --> _00S8
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01492__00S8 = _00S7_constant+1*v01475_aircraft_z_pos+1*v01484__00S6

# op _00T7_power_combination_eval
# LANG: _00T6, _dD --> bbb
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01513_bbb = (v0383__dD**1)*(v01514__00T6**-1)
v01513_bbb = (v01513_bbb*_00T7_coeff).reshape((1, 40, 30))

# op _00VG_linear_combination_eval
# LANG: _00V3, _00VF --> _00VH
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01564__00VH = _00VG_constant+1*v01558__00V3+-1*v01579__00VF

# op _00VY_linear_combination_eval
# LANG: _00VP, _00VX --> _00VZ
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01589__00VZ = _00VY_constant+1*v01588__00VP+1*v01593__00VX

# op _00XC_linear_combination_eval
# LANG: _00Xt, _00XB --> _00XD
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01666__00XD = _00XC_constant+1*v01665__00Xt+1*v01670__00XB

# op _00X__power_combination_eval
# LANG: _00XZ, _00XP --> _00Y0
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01602__00Y0 = (v01601__00XZ**1)*(v01608__00XP**1)
v01602__00Y0 = (v01602__00Y0*_00X__coeff).reshape((1, 27, 3, 40, 10))

# op _00Xk_linear_combination_eval
# LANG: _00Xj --> _00Xl
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01660__00Xl = _00Xk_constant+-1*v01655__00Xj

# op _00dF_power_combination_eval
# LANG: _00dE, prandtl_loss_factor --> _00dG
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0324__00dG = (v0322__00dE**1)*(v0264_prandtl_loss_factor**1)
v0324__00dG = (v0324__00dG*_00dF_coeff).reshape((1, 40, 30))

# op _00sI_power_combination_eval
# LANG: _00sH, prandtl_loss_factor --> _00sJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0697__00sJ = (v0695__00sH**1)*(v0637_prandtl_loss_factor**1)
v0697__00sJ = (v0697__00sJ*_00sI_coeff).reshape((1, 40, 30))

# op _00Au_linear_combination_eval
# LANG: _00Ac, _00At --> rel_obs_z_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0945_rel_obs_z_pos = _00Au_constant+1*v0944__00Ac+-1*v0946__00At

# op _00Aw_power_combination_eval
# LANG: rel_obs_x_pos --> _00Ax
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0947__00Ax = (v0933_rel_obs_x_pos**2)
v0947__00Ax = (v0947__00Ax*_00Aw_coeff).reshape((1, 1, 27))

# op _00Ay_power_combination_eval
# LANG: rel_obs_y_pos --> _00Az
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0949__00Az = (v0941_rel_obs_y_pos**2)
v0949__00Az = (v0949__00Az*_00Ay_coeff).reshape((1, 1, 27))

# op _00By_decompose_eval
# LANG: bbb --> _00Bz
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01067__00Bz = ((v0967_bbb.flatten())[src_indices__00Bz__00By]).reshape((1, 40, 1))

# op _00Cc_decompose_eval
# LANG: _00C9 --> _00Cd
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01065__00Cd = ((v0971__00C9.flatten())[src_indices__00Cd__00Cc]).reshape((1, 27, 3, 40, 10))

# op _00Ek_power_combination_eval
# LANG: _00E1, _00Ej --> _00El
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01038__00El = (v01018__00E1**1)*(v01043__00Ej**-1)
v01038__00El = (v01038__00El*_00Ek_coeff).reshape((1, 27, 3, 40, 10))

# op _00FZ_power_combination_eval
# LANG: _00FG, _00FY --> _00F_
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01115__00F_ = (v01114__00FG**1)*(v01120__00FY**-1)
v01115__00F_ = (v01115__00F_*_00FZ_coeff).reshape((1, 27, 3, 40, 10))

# op _00Gm_power_combination_eval
# LANG: _00Gl --> _00Gn
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01063__00Gn = (v01056__00Gl**1)
v01063__00Gn = (v01063__00Gn*_00Gm_coeff).reshape((1, 27, 3, 40, 10))

# op _00S9_linear_combination_eval
# LANG: _00RS, _00S8 --> rel_obs_z_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01491_rel_obs_z_pos = _00S9_constant+1*v01490__00RS+-1*v01492__00S8

# op _00Sb_power_combination_eval
# LANG: rel_obs_x_pos --> _00Sc
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01493__00Sc = (v01479_rel_obs_x_pos**2)
v01493__00Sc = (v01493__00Sc*_00Sb_coeff).reshape((1, 1, 27))

# op _00Sd_power_combination_eval
# LANG: rel_obs_y_pos --> _00Se
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01495__00Se = (v01487_rel_obs_y_pos**2)
v01495__00Se = (v01495__00Se*_00Sd_coeff).reshape((1, 1, 27))

# op _00TS_decompose_eval
# LANG: _00TP --> _00TT
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01611__00TT = ((v01517__00TP.flatten())[src_indices__00TT__00TS]).reshape((1, 27, 3, 40, 10))

# op _00Td_decompose_eval
# LANG: bbb --> _00Te
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01613__00Te = ((v01513_bbb.flatten())[src_indices__00Te__00Td]).reshape((1, 40, 1))

# op _00V__power_combination_eval
# LANG: _00VH, _00VZ --> _00W0
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01584__00W0 = (v01564__00VH**1)*(v01589__00VZ**-1)
v01584__00W0 = (v01584__00W0*_00V__coeff).reshape((1, 27, 3, 40, 10))

# op _00XE_power_combination_eval
# LANG: _00Xl, _00XD --> _00XF
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01661__00XF = (v01660__00Xl**1)*(v01666__00XD**-1)
v01661__00XF = (v01661__00XF*_00XE_coeff).reshape((1, 27, 3, 40, 10))

# op _00Y1_power_combination_eval
# LANG: _00Y0 --> _00Y2
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01609__00Y2 = (v01602__00Y0**1)
v01609__00Y2 = (v01609__00Y2*_00Y1_coeff).reshape((1, 27, 3, 40, 10))

# op _00dH_power_combination_eval
# LANG: _00dG, _dr --> _local_thrust
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0325__local_thrust = (v0324__00dG**1)*(v0202__dr**1)
v0325__local_thrust = (v0325__local_thrust*_00dH_coeff).reshape((1, 40, 30))

# op _00sK_power_combination_eval
# LANG: _00sJ, _dr --> _local_thrust
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0698__local_thrust = (v0697__00sJ**1)*(v0575__dr**1)
v0698__local_thrust = (v0698__local_thrust*_00sK_coeff).reshape((1, 40, 30))

# op _00AA_linear_combination_eval
# LANG: _00Ax, _00Az --> _00AB
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0948__00AB = _00AA_constant+1*v0947__00Ax+1*v0949__00Az

# op _00AC_power_combination_eval
# LANG: rel_obs_z_pos --> _00AD
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0951__00AD = (v0945_rel_obs_z_pos**2)
v0951__00AD = (v0951__00AD*_00AC_coeff).reshape((1, 1, 27))

# op _00BA reshape_eval
# LANG: _00Bz --> _00BB
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01068__00BB = v01067__00Bz.reshape((1, 40))

# op _00Bm expand_scalar_eval
# LANG: dr --> _00Bn
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0966__00Bn = np.empty((1, 40, 30))
v0966__00Bn.fill(v0857_dr.item())

# op _00GF_sin_eval
# LANG: _00Cd --> _00GG
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01130__00GG = np.sin(v01065__00Cd)

# op _00Go_power_combination_eval
# LANG: _00El, _00Gn --> _00Gp
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01048__00Gp = (v01038__00El**1)*(v01063__00Gn**1)
v01048__00Gp = (v01048__00Gp*_00Go_coeff).reshape((1, 27, 3, 40, 10))

# op _00Gq_power_combination_eval
# LANG: _00Gn, _00F_ --> _00Gr
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01125__00Gr = (v01115__00F_**1)*(v01063__00Gn**1)
v01125__00Gr = (v01125__00Gr*_00Gq_coeff).reshape((1, 27, 3, 40, 10))

# op _00Gw_sin_eval
# LANG: _00Cd --> _00Gx
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01072__00Gx = np.sin(v01065__00Cd)

# op _00Sf_linear_combination_eval
# LANG: _00Sc, _00Se --> _00Sg
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01494__00Sg = _00Sf_constant+1*v01493__00Sc+1*v01495__00Se

# op _00Sh_power_combination_eval
# LANG: rel_obs_z_pos --> _00Si
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01497__00Si = (v01491_rel_obs_z_pos**2)
v01497__00Si = (v01497__00Si*_00Sh_coeff).reshape((1, 1, 27))

# op _00T1 expand_scalar_eval
# LANG: dr --> _00T2
# SHAPES: (1,) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01512__00T2 = np.empty((1, 40, 30))
v01512__00T2.fill(v01403_dr.item())

# op _00Tf reshape_eval
# LANG: _00Te --> _00Tg
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01614__00Tg = v01613__00Te.reshape((1, 40))

# op _00Y3_power_combination_eval
# LANG: _00W0, _00Y2 --> _00Y4
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01594__00Y4 = (v01584__00W0**1)*(v01609__00Y2**1)
v01594__00Y4 = (v01594__00Y4*_00Y3_coeff).reshape((1, 27, 3, 40, 10))

# op _00Y5_power_combination_eval
# LANG: _00Y2, _00XF --> _00Y6
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01671__00Y6 = (v01661__00XF**1)*(v01609__00Y2**1)
v01671__00Y6 = (v01671__00Y6*_00Y5_coeff).reshape((1, 27, 3, 40, 10))

# op _00Yb_sin_eval
# LANG: _00TT --> _00Yc
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01618__00Yc = np.sin(v01611__00TT)

# op _00Yk_sin_eval
# LANG: _00TT --> _00Yl
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01676__00Yl = np.sin(v01611__00TT)

# op _00ie_power_combination_eval
# LANG: _local_thrust --> _dT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0326__dT = (v0325__local_thrust**1)
v0326__dT = (v0326__dT*_00ie_coeff).reshape((1, 40, 30))

# op _00xh_power_combination_eval
# LANG: _local_thrust --> _dT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0699__dT = (v0698__local_thrust**1)
v0699__dT = (v0699__dT*_00xh_coeff).reshape((1, 40, 30))

# op _00AE_linear_combination_eval
# LANG: _00AB, _00AD --> _00AF
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0950__00AF = _00AE_constant+1*v0948__00AB+1*v0951__00AD

# op _00Bo_power_combination_eval
# LANG: _00Bn, _dT --> aaa
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0965_aaa = (v0699__dT**1)*(v0966__00Bn**-1)
v0965_aaa = (v0965_aaa*_00Bo_coeff).reshape((1, 40, 30))

# op _00Ct expand_array_eval
# LANG: _00BB --> _00Cu
# SHAPES: (1, 40) --> (1, 27, 3, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01069__00Cu = np.einsum('ad,bce->abcde', v01068__00BB.reshape((1, 40)) ,np.ones((27, 3, 1))).reshape((1, 27, 3, 40, 1))

# op _00GH_power_combination_eval
# LANG: _00Gr, _00GG --> _00GI
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01129__00GI = (v01125__00Gr**1)*(v01130__00GG**1)
v01129__00GI = (v01129__00GI*_00GH_coeff).reshape((1, 27, 3, 40, 10))

# op _00Gy_power_combination_eval
# LANG: _00Gp, _00Gx --> _00Gz
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01071__00Gz = (v01048__00Gp**1)*(v01072__00Gx**1)
v01071__00Gz = (v01071__00Gz*_00Gy_coeff).reshape((1, 27, 3, 40, 10))

# op _00Sj_linear_combination_eval
# LANG: _00Sg, _00Si --> _00Sk
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01496__00Sk = _00Sj_constant+1*v01494__00Sg+1*v01497__00Si

# op _00T3_power_combination_eval
# LANG: _00T2, _dT --> aaa
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01511_aaa = (v0326__dT**1)*(v01512__00T2**-1)
v01511_aaa = (v01511_aaa*_00T3_coeff).reshape((1, 40, 30))

# op _00U8 expand_array_eval
# LANG: _00Tg --> _00U9
# SHAPES: (1, 40) --> (1, 27, 3, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01615__00U9 = np.einsum('ad,bce->abcde', v01614__00Tg.reshape((1, 40)) ,np.ones((27, 3, 1))).reshape((1, 27, 3, 40, 1))

# op _00Yd_power_combination_eval
# LANG: _00Y4, _00Yc --> _00Ye
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01617__00Ye = (v01594__00Y4**1)*(v01618__00Yc**1)
v01617__00Ye = (v01617__00Ye*_00Yd_coeff).reshape((1, 27, 3, 40, 10))

# op _00Ym_power_combination_eval
# LANG: _00Y6, _00Yl --> _00Yn
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01675__00Yn = (v01671__00Y6**1)*(v01676__00Yl**1)
v01675__00Yn = (v01675__00Yn*_00Ym_coeff).reshape((1, 27, 3, 40, 10))

# op _00AG_power_combination_eval
# LANG: _00AF --> rel_obs_dist
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0952_rel_obs_dist = (v0950__00AF**0.5)
v0952_rel_obs_dist = (v0952_rel_obs_dist*_00AG_coeff).reshape((1, 1, 27))

# op _00Bu_decompose_eval
# LANG: aaa --> _00Bv
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0975__00Bv = ((v0965_aaa.flatten())[src_indices__00Bv__00Bu]).reshape((1, 40, 1))

# op _00Cv_indexed_passthrough_eval
# LANG: _00Cu, _00Gz --> dDdR_real_exp
# SHAPES: (1, 27, 3, 40, 1), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01070_dDdR_real_exp__temp[i_v01069__00Cu__00Cv_indexed_passthrough_eval] = v01069__00Cu.flatten()
v01070_dDdR_real_exp = v01070_dDdR_real_exp__temp.copy()
v01070_dDdR_real_exp__temp[i_v01071__00Gz__00Cv_indexed_passthrough_eval] = v01071__00Gz.flatten()
v01070_dDdR_real_exp = v01070_dDdR_real_exp__temp.copy()

# op _00GJ_indexed_passthrough_eval
# LANG: _00GI --> dDdR_imag_exp
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01131_dDdR_imag_exp__temp[i_v01129__00GI__00GJ_indexed_passthrough_eval] = v01129__00GI.flatten()
v01131_dDdR_imag_exp = v01131_dDdR_imag_exp__temp.copy()

# op _00Sl_power_combination_eval
# LANG: _00Sk --> rel_obs_dist
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01498_rel_obs_dist = (v01496__00Sk**0.5)
v01498_rel_obs_dist = (v01498_rel_obs_dist*_00Sl_coeff).reshape((1, 1, 27))

# op _00T9_decompose_eval
# LANG: aaa --> _00Ta
# SHAPES: (1, 40, 30) --> (1, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01521__00Ta = ((v01511_aaa.flatten())[src_indices__00Ta__00T9]).reshape((1, 40, 1))

# op _00Ua_indexed_passthrough_eval
# LANG: _00U9, _00Ye --> dDdR_real_exp
# SHAPES: (1, 27, 3, 40, 1), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01616_dDdR_real_exp__temp[i_v01615__00U9__00Ua_indexed_passthrough_eval] = v01615__00U9.flatten()
v01616_dDdR_real_exp = v01616_dDdR_real_exp__temp.copy()
v01616_dDdR_real_exp__temp[i_v01617__00Ye__00Ua_indexed_passthrough_eval] = v01617__00Ye.flatten()
v01616_dDdR_real_exp = v01616_dDdR_real_exp__temp.copy()

# op _00Yo_indexed_passthrough_eval
# LANG: _00Yn --> dDdR_imag_exp
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01677_dDdR_imag_exp__temp[i_v01675__00Yn__00Yo_indexed_passthrough_eval] = v01675__00Yn.flatten()
v01677_dDdR_imag_exp = v01677_dDdR_imag_exp__temp.copy()

# op _00A_ reshape_eval
# LANG: rel_obs_x_pos --> _00B0
# SHAPES: (1, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0961__00B0 = v0933_rel_obs_x_pos.reshape((1, 27))

# op _00B2 reshape_eval
# LANG: rel_obs_dist --> _00B3
# SHAPES: (1, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0963__00B3 = v0952_rel_obs_dist.reshape((1, 27))

# op _00Bw reshape_eval
# LANG: _00Bv --> _00Bx
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0976__00Bx = v0975__00Bv.reshape((1, 40))

# op _00GA_cos_eval
# LANG: _00Cd --> _00GB
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01127__00GB = np.cos(v01065__00Cd)

# op _00GQ_power_combination_eval
# LANG: dDdR_real_exp, real_weighting --> _00GR
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01143__00GR = (v01134_real_weighting**1)*(v01070_dDdR_real_exp**1)
v01143__00GR = (v01143__00GR*_00GQ_coeff).reshape((1, 27, 3, 40, 11))

# op _00GS_power_combination_eval
# LANG: dDdR_imag_exp, imag_weighting --> _00GT
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01145__00GT = (v01137_imag_weighting**1)*(v01131_dDdR_imag_exp**1)
v01145__00GT = (v01145__00GT*_00GS_coeff).reshape((1, 27, 3, 40, 11))

# op _00Gs_cos_eval
# LANG: _00Cd --> _00Gt
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01066__00Gt = np.cos(v01065__00Cd)

# op _00H1_power_combination_eval
# LANG: dDdR_imag_exp, real_weighting --> _00H2
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01175__00H2 = (v01134_real_weighting**1)*(v01131_dDdR_imag_exp**1)
v01175__00H2 = (v01175__00H2*_00H1_coeff).reshape((1, 27, 3, 40, 11))

# op _00H3_power_combination_eval
# LANG: dDdR_real_exp, imag_weighting --> _00H4
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01177__00H4 = (v01137_imag_weighting**1)*(v01070_dDdR_real_exp**1)
v01177__00H4 = (v01177__00H4*_00H3_coeff).reshape((1, 27, 3, 40, 11))

# op _00SF reshape_eval
# LANG: rel_obs_x_pos --> _00SG
# SHAPES: (1, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01507__00SG = v01479_rel_obs_x_pos.reshape((1, 27))

# op _00SI reshape_eval
# LANG: rel_obs_dist --> _00SJ
# SHAPES: (1, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01509__00SJ = v01498_rel_obs_dist.reshape((1, 27))

# op _00Tb reshape_eval
# LANG: _00Ta --> _00Tc
# SHAPES: (1, 40, 1) --> (1, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01522__00Tc = v01521__00Ta.reshape((1, 40))

# op _00Y7_cos_eval
# LANG: _00TT --> _00Y8
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01612__00Y8 = np.cos(v01611__00TT)

# op _00YH_power_combination_eval
# LANG: dDdR_imag_exp, real_weighting --> _00YI
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01721__00YI = (v01680_real_weighting**1)*(v01677_dDdR_imag_exp**1)
v01721__00YI = (v01721__00YI*_00YH_coeff).reshape((1, 27, 3, 40, 11))

# op _00YJ_power_combination_eval
# LANG: dDdR_real_exp, imag_weighting --> _00YK
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01723__00YK = (v01683_imag_weighting**1)*(v01616_dDdR_real_exp**1)
v01723__00YK = (v01723__00YK*_00YJ_coeff).reshape((1, 27, 3, 40, 11))

# op _00Yf_cos_eval
# LANG: _00TT --> _00Yg
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01673__00Yg = np.cos(v01611__00TT)

# op _00Yv_power_combination_eval
# LANG: dDdR_real_exp, real_weighting --> _00Yw
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01689__00Yw = (v01680_real_weighting**1)*(v01616_dDdR_real_exp**1)
v01689__00Yw = (v01689__00Yw*_00Yv_coeff).reshape((1, 27, 3, 40, 11))

# op _00Yx_power_combination_eval
# LANG: dDdR_imag_exp, imag_weighting --> _00Yy
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01691__00Yy = (v01683_imag_weighting**1)*(v01677_dDdR_imag_exp**1)
v01691__00Yy = (v01691__00Yy*_00Yx_coeff).reshape((1, 27, 3, 40, 11))

# op _00B5_power_combination_eval
# LANG: _00B0, _00B3 --> _00B6
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0962__00B6 = (v0961__00B0**1)*(v0963__00B3**-1)
v0962__00B6 = (v0962__00B6*_00B5_coeff).reshape((1, 27))

# op _00Cq expand_array_eval
# LANG: _00Bx --> _00Cr
# SHAPES: (1, 40) --> (1, 27, 3, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0977__00Cr = np.einsum('ad,bce->abcde', v0976__00Bx.reshape((1, 40)) ,np.ones((27, 3, 1))).reshape((1, 27, 3, 40, 1))

# op _00GC_power_combination_eval
# LANG: _00Gr, _00GB --> _00GD
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01126__00GD = (v01125__00Gr**1)*(v01127__00GB**1)
v01126__00GD = (v01126__00GD*_00GC_coeff).reshape((1, 27, 3, 40, 10))

# op _00GU_linear_combination_eval
# LANG: _00GR, _00GT --> _00GV
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01144__00GV = _00GU_constant+1*v01143__00GR+1*v01145__00GT

# op _00Gu_power_combination_eval
# LANG: _00Gp, _00Gt --> _00Gv
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01064__00Gv = (v01048__00Gp**1)*(v01066__00Gt**1)
v01064__00Gv = (v01064__00Gv*_00Gu_coeff).reshape((1, 27, 3, 40, 10))

# op _00H5_linear_combination_eval
# LANG: _00H2, _00H4 --> _00H6
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01176__00H6 = _00H5_constant+1*v01175__00H2+1*v01177__00H4

# op _00H7_power_combination_eval
# LANG: n_var --> _00H8
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01158__00H8 = (v01147_n_var**1)
v01158__00H8 = (v01158__00H8*_00H7_coeff).reshape((1, 27, 3, 40, 11))

# op _00HT_linear_combination_eval
# LANG: lam_var, n_var --> _00HU
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01179__00HU = _00HT_constant+1*v01147_n_var+-1*v0979_lam_var

# op _00Hp_linear_combination_eval
# LANG: lam_var, n_var --> _00Hq
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01148__00Hq = _00Hp_constant+1*v01147_n_var+-1*v0979_lam_var

# op _00Hx_power_combination_eval
# LANG: n_var --> _00Hy
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01153__00Hy = (v01147_n_var**1)
v01153__00Hy = (v01153__00Hy*_00Hx_coeff).reshape((1, 27, 3, 40, 11))

# op _00I0_power_combination_eval
# LANG: n_var --> _00I1
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01183__00I1 = (v01147_n_var**1)
v01183__00I1 = (v01183__00I1*_00I0_coeff).reshape((1, 27, 3, 40, 11))

# op _00Q__power_combination_eval
# LANG: temperature --> _00R0
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01451__00R0 = (v01439_temperature**1)
v01451__00R0 = (v01451__00R0*_00Q__coeff).reshape((1,))

# op _00SL_power_combination_eval
# LANG: _00SG, _00SJ --> _00SM
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01508__00SM = (v01507__00SG**1)*(v01509__00SJ**-1)
v01508__00SM = (v01508__00SM*_00SL_coeff).reshape((1, 27))

# op _00U5 expand_array_eval
# LANG: _00Tc --> _00U6
# SHAPES: (1, 40) --> (1, 27, 3, 40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01523__00U6 = np.einsum('ad,bce->abcde', v01522__00Tc.reshape((1, 40)) ,np.ones((27, 3, 1))).reshape((1, 27, 3, 40, 1))

# op _00Y9_power_combination_eval
# LANG: _00Y4, _00Y8 --> _00Ya
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01610__00Ya = (v01594__00Y4**1)*(v01612__00Y8**1)
v01610__00Ya = (v01610__00Ya*_00Y9_coeff).reshape((1, 27, 3, 40, 10))

# op _00YL_linear_combination_eval
# LANG: _00YI, _00YK --> _00YM
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01722__00YM = _00YL_constant+1*v01721__00YI+1*v01723__00YK

# op _00YN_power_combination_eval
# LANG: n_var --> _00YO
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01704__00YO = (v01693_n_var**1)
v01704__00YO = (v01704__00YO*_00YN_coeff).reshape((1, 27, 3, 40, 11))

# op _00Yh_power_combination_eval
# LANG: _00Y6, _00Yg --> _00Yi
# SHAPES: (1, 27, 3, 40, 10), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 10)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01672__00Yi = (v01671__00Y6**1)*(v01673__00Yg**1)
v01672__00Yi = (v01672__00Yi*_00Yh_coeff).reshape((1, 27, 3, 40, 10))

# op _00Yz_linear_combination_eval
# LANG: _00Yw, _00Yy --> _00YA
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01690__00YA = _00Yz_constant+1*v01689__00Yw+1*v01691__00Yy

# op _00Z4_linear_combination_eval
# LANG: lam_var, n_var --> _00Z5
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01694__00Z5 = _00Z4_constant+1*v01693_n_var+-1*v01525_lam_var

# op _00ZG_power_combination_eval
# LANG: n_var --> _00ZH
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01729__00ZH = (v01693_n_var**1)
v01729__00ZH = (v01729__00ZH*_00ZG_coeff).reshape((1, 27, 3, 40, 11))

# op _00Zc_power_combination_eval
# LANG: n_var --> _00Zd
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01699__00Zd = (v01693_n_var**1)
v01699__00Zd = (v01699__00Zd*_00Zc_coeff).reshape((1, 27, 3, 40, 11))

# op _00Zy_linear_combination_eval
# LANG: lam_var, n_var --> _00Zz
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01725__00Zz = _00Zy_constant+1*v01693_n_var+-1*v01525_lam_var

# op _00zk_power_combination_eval
# LANG: temperature --> _00zl
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0905__00zl = (v0893_temperature**1)
v0905__00zl = (v0905__00zl*_00zk_coeff).reshape((1,))

# op _00B7 arccos_eval
# LANG: _00B6 --> theta_dummy
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0964_theta_dummy = np.arccos(v0962__00B6)

# op _00Cs_indexed_passthrough_eval
# LANG: _00Cr, _00Gv --> dTdR_real_exp
# SHAPES: (1, 27, 3, 40, 1), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v0978_dTdR_real_exp__temp[i_v0977__00Cr__00Cs_indexed_passthrough_eval] = v0977__00Cr.flatten()
v0978_dTdR_real_exp = v0978_dTdR_real_exp__temp.copy()
v0978_dTdR_real_exp__temp[i_v01064__00Gv__00Cs_indexed_passthrough_eval] = v01064__00Gv.flatten()
v0978_dTdR_real_exp = v0978_dTdR_real_exp__temp.copy()

# op _00GE_indexed_passthrough_eval
# LANG: _00GD --> dTdR_imag_exp
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01128_dTdR_imag_exp__temp[i_v01126__00GD__00GE_indexed_passthrough_eval] = v01126__00GD.flatten()
v01128_dTdR_imag_exp = v01128_dTdR_imag_exp__temp.copy()

# op _00H9_power_combination_eval
# LANG: _00BH, _00H8 --> _00Ha
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01159__00Ha = (v01158__00H8**1)*(v0985__00BH**1)
v01159__00Ha = (v01159__00Ha*_00H9_coeff).reshape((1, 27, 3, 40, 11))

# op _00HV_power_combination_eval
# LANG: _00H6, _00HU --> _00HW
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01178__00HW = (v01176__00H6**1)*(v01179__00HU**1)
v01178__00HW = (v01178__00HW*_00HV_coeff).reshape((1, 27, 3, 40, 11))

# op _00Hr_power_combination_eval
# LANG: _00GV, _00Hq --> _00Hs
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01146__00Hs = (v01144__00GV**1)*(v01148__00Hq**1)
v01146__00Hs = (v01146__00Hs*_00Hr_coeff).reshape((1, 27, 3, 40, 11))

# op _00Hz_power_combination_eval
# LANG: _00BH, _00Hy --> _00HA
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01154__00HA = (v01153__00Hy**1)*(v0985__00BH**1)
v01154__00HA = (v01154__00HA*_00Hz_coeff).reshape((1, 27, 3, 40, 11))

# op _00I2_power_combination_eval
# LANG: _00BH, _00I1 --> _00I3
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01184__00I3 = (v01183__00I1**1)*(v0985__00BH**1)
v01184__00I3 = (v01184__00I3*_00I2_coeff).reshape((1, 27, 3, 40, 11))

# op _00R1_power_combination_eval
# LANG: _00R0 --> speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01452_speed_of_sound = (v01451__00R0**0.5)
v01452_speed_of_sound = (v01452_speed_of_sound*_00R1_coeff).reshape((1,))

# op _00SN arccos_eval
# LANG: _00SM --> theta_dummy
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01510_theta_dummy = np.arccos(v01508__00SM)

# op _00U7_indexed_passthrough_eval
# LANG: _00U6, _00Ya --> dTdR_real_exp
# SHAPES: (1, 27, 3, 40, 1), (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01524_dTdR_real_exp__temp[i_v01523__00U6__00U7_indexed_passthrough_eval] = v01523__00U6.flatten()
v01524_dTdR_real_exp = v01524_dTdR_real_exp__temp.copy()
v01524_dTdR_real_exp__temp[i_v01610__00Ya__00U7_indexed_passthrough_eval] = v01610__00Ya.flatten()
v01524_dTdR_real_exp = v01524_dTdR_real_exp__temp.copy()

# op _00YP_power_combination_eval
# LANG: _00Tm, _00YO --> _00YQ
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01705__00YQ = (v01704__00YO**1)*(v01531__00Tm**1)
v01705__00YQ = (v01705__00YQ*_00YP_coeff).reshape((1, 27, 3, 40, 11))

# op _00Yj_indexed_passthrough_eval
# LANG: _00Yi --> dTdR_imag_exp
# SHAPES: (1, 27, 3, 40, 10) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01674_dTdR_imag_exp__temp[i_v01672__00Yi__00Yj_indexed_passthrough_eval] = v01672__00Yi.flatten()
v01674_dTdR_imag_exp = v01674_dTdR_imag_exp__temp.copy()

# op _00Z6_power_combination_eval
# LANG: _00YA, _00Z5 --> _00Z7
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01692__00Z7 = (v01690__00YA**1)*(v01694__00Z5**1)
v01692__00Z7 = (v01692__00Z7*_00Z6_coeff).reshape((1, 27, 3, 40, 11))

# op _00ZA_power_combination_eval
# LANG: _00YM, _00Zz --> _00ZB
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01724__00ZB = (v01722__00YM**1)*(v01725__00Zz**1)
v01724__00ZB = (v01724__00ZB*_00ZA_coeff).reshape((1, 27, 3, 40, 11))

# op _00ZI_power_combination_eval
# LANG: _00Tm, _00ZH --> _00ZJ
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01730__00ZJ = (v01729__00ZH**1)*(v01531__00Tm**1)
v01730__00ZJ = (v01730__00ZJ*_00ZI_coeff).reshape((1, 27, 3, 40, 11))

# op _00Ze_power_combination_eval
# LANG: _00Tm, _00Zd --> _00Zf
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01700__00Zf = (v01699__00Zd**1)*(v01531__00Tm**1)
v01700__00Zf = (v01700__00Zf*_00Ze_coeff).reshape((1, 27, 3, 40, 11))

# op _00zm_power_combination_eval
# LANG: _00zl --> speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0906_speed_of_sound = (v0905__00zl**0.5)
v0906_speed_of_sound = (v0906_speed_of_sound*_00zm_coeff).reshape((1,))

# op _00BC expand_array_eval
# LANG: theta_dummy --> _00BD
# SHAPES: (1, 27) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01140__00BD = np.einsum('ab,cde->abcde', v0964_theta_dummy.reshape((1, 27)) ,np.ones((3, 40, 11))).reshape((1, 27, 3, 40, 11))

# op _00BK expand_scalar_eval
# LANG: speed_of_sound --> _00BL
# SHAPES: (1,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01151__00BL = np.empty((1, 27, 3, 40, 11))
v01151__00BL.fill(v0906_speed_of_sound.item())

# op _00GK_power_combination_eval
# LANG: dTdR_real_exp, real_weighting --> _00GL
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01135__00GL = (v01134_real_weighting**1)*(v0978_dTdR_real_exp**1)
v01135__00GL = (v01135__00GL*_00GK_coeff).reshape((1, 27, 3, 40, 11))

# op _00GM_power_combination_eval
# LANG: dTdR_imag_exp, imag_weighting --> _00GN
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01138__00GN = (v01137_imag_weighting**1)*(v01128_dTdR_imag_exp**1)
v01138__00GN = (v01138__00GN*_00GM_coeff).reshape((1, 27, 3, 40, 11))

# op _00GW_power_combination_eval
# LANG: dTdR_imag_exp, real_weighting --> _00GX
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01169__00GX = (v01134_real_weighting**1)*(v01128_dTdR_imag_exp**1)
v01169__00GX = (v01169__00GX*_00GW_coeff).reshape((1, 27, 3, 40, 11))

# op _00GY_power_combination_eval
# LANG: dTdR_real_exp, imag_weighting --> _00GZ
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01171__00GZ = (v01137_imag_weighting**1)*(v0978_dTdR_real_exp**1)
v01171__00GZ = (v01171__00GZ*_00GY_coeff).reshape((1, 27, 3, 40, 11))

# op _00HB_power_combination_eval
# LANG: _00BF, _00HA --> _00HC
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01155__00HC = (v01154__00HA**1)*(v0974__00BF**1)
v01155__00HC = (v01155__00HC*_00HB_coeff).reshape((1, 27, 3, 40, 11))

# op _00HX_power_combination_eval
# LANG: _00HW --> _00HY
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01180__00HY = (v01178__00HW**1)
v01180__00HY = (v01180__00HY*_00HX_coeff).reshape((1, 27, 3, 40, 11))

# op _00Hb_power_combination_eval
# LANG: _00BF, _00Ha --> _00Hc
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01160__00Hc = (v01159__00Ha**1)*(v0974__00BF**1)
v01160__00Hc = (v01160__00Hc*_00Hb_coeff).reshape((1, 27, 3, 40, 11))

# op _00Ht_power_combination_eval
# LANG: _00Hs --> _00Hu
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01149__00Hu = (v01146__00Hs**1)
v01149__00Hu = (v01149__00Hu*_00Ht_coeff).reshape((1, 27, 3, 40, 11))

# op _00I4_power_combination_eval
# LANG: _00BF, _00I3 --> _00I5
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01185__00I5 = (v01184__00I3**1)*(v0974__00BF**1)
v01185__00I5 = (v01185__00I5*_00I4_coeff).reshape((1, 27, 3, 40, 11))

# op _00Lj expand_scalar_eval
# LANG: Vx --> _00Lk
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01273__00Lk = np.empty((1, 1))
v01273__00Lk.fill(v033_u.item())

# op _00Lm expand_scalar_eval
# LANG: Vy --> _00Ln
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01275__00Ln = np.empty((1, 1))
v01275__00Ln.fill(v034_v.item())

# op _00Lo expand_scalar_eval
# LANG: Vz --> _00Lp
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01276__00Lp = np.empty((1, 1))
v01276__00Lp.fill(v035_w.item())

# op _00Th expand_array_eval
# LANG: theta_dummy --> _00Ti
# SHAPES: (1, 27) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01686__00Ti = np.einsum('ab,cde->abcde', v01510_theta_dummy.reshape((1, 27)) ,np.ones((3, 40, 11))).reshape((1, 27, 3, 40, 11))

# op _00Tp expand_scalar_eval
# LANG: speed_of_sound --> _00Tq
# SHAPES: (1,) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01697__00Tq = np.empty((1, 27, 3, 40, 11))
v01697__00Tq.fill(v01452_speed_of_sound.item())

# op _00YB_power_combination_eval
# LANG: dTdR_imag_exp, real_weighting --> _00YC
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01715__00YC = (v01680_real_weighting**1)*(v01674_dTdR_imag_exp**1)
v01715__00YC = (v01715__00YC*_00YB_coeff).reshape((1, 27, 3, 40, 11))

# op _00YD_power_combination_eval
# LANG: dTdR_real_exp, imag_weighting --> _00YE
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01717__00YE = (v01683_imag_weighting**1)*(v01524_dTdR_real_exp**1)
v01717__00YE = (v01717__00YE*_00YD_coeff).reshape((1, 27, 3, 40, 11))

# op _00YR_power_combination_eval
# LANG: _00Tk, _00YQ --> _00YS
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01706__00YS = (v01705__00YQ**1)*(v01520__00Tk**1)
v01706__00YS = (v01706__00YS*_00YR_coeff).reshape((1, 27, 3, 40, 11))

# op _00Yp_power_combination_eval
# LANG: dTdR_real_exp, real_weighting --> _00Yq
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01681__00Yq = (v01680_real_weighting**1)*(v01524_dTdR_real_exp**1)
v01681__00Yq = (v01681__00Yq*_00Yp_coeff).reshape((1, 27, 3, 40, 11))

# op _00Yr_power_combination_eval
# LANG: dTdR_imag_exp, imag_weighting --> _00Ys
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01684__00Ys = (v01683_imag_weighting**1)*(v01674_dTdR_imag_exp**1)
v01684__00Ys = (v01684__00Ys*_00Yr_coeff).reshape((1, 27, 3, 40, 11))

# op _00Z8_power_combination_eval
# LANG: _00Z7 --> _00Z9
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01695__00Z9 = (v01692__00Z7**1)
v01695__00Z9 = (v01695__00Z9*_00Z8_coeff).reshape((1, 27, 3, 40, 11))

# op _00ZC_power_combination_eval
# LANG: _00ZB --> _00ZD
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01726__00ZD = (v01724__00ZB**1)
v01726__00ZD = (v01726__00ZD*_00ZC_coeff).reshape((1, 27, 3, 40, 11))

# op _00ZK_power_combination_eval
# LANG: _00Tk, _00ZJ --> _00ZL
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01731__00ZL = (v01730__00ZJ**1)*(v01520__00Tk**1)
v01731__00ZL = (v01731__00ZL*_00ZK_coeff).reshape((1, 27, 3, 40, 11))

# op _00Zg_power_combination_eval
# LANG: _00Tk, _00Zf --> _00Zh
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01701__00Zh = (v01700__00Zf**1)*(v01520__00Tk**1)
v01701__00Zh = (v01701__00Zh*_00Zg_coeff).reshape((1, 27, 3, 40, 11))

# op _011Z expand_scalar_eval
# LANG: Vx --> _011_
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01819__011_ = np.empty((1, 1))
v01819__011_.fill(v033_u.item())

# op _0121 expand_scalar_eval
# LANG: Vy --> _0122
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01821__0122 = np.empty((1, 1))
v01821__0122.fill(v034_v.item())

# op _0123 expand_scalar_eval
# LANG: Vz --> _0124
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01822__0124 = np.empty((1, 1))
v01822__0124.fill(v035_w.item())

# op _00GO_linear_combination_eval
# LANG: _00GL, _00GN --> _00GP
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01136__00GP = _00GO_constant+1*v01135__00GL+1*v01138__00GN

# op _00G__linear_combination_eval
# LANG: _00GX, _00GZ --> _00H0
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01170__00H0 = _00G__constant+1*v01169__00GX+1*v01171__00GZ

# op _00HD_power_combination_eval
# LANG: _00BJ, _00HC --> _00HE
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01156__00HE = (v01155__00HC**1)*(v0994__00BJ**1)
v01156__00HE = (v01156__00HE*_00HD_coeff).reshape((1, 27, 3, 40, 11))

# op _00HP_cos_eval
# LANG: _00BD --> _00HQ
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01173__00HQ = np.cos(v01140__00BD)

# op _00HZ_power_combination_eval
# LANG: _00BL, _00HY --> _00H_
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01181__00H_ = (v01180__00HY**1)*(v01151__00BL**1)
v01181__00H_ = (v01181__00H_*_00HZ_coeff).reshape((1, 27, 3, 40, 11))

# op _00Hd_power_combination_eval
# LANG: _00BJ, _00Hc --> _00He
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01161__00He = (v01160__00Hc**1)*(v0994__00BJ**1)
v01161__00He = (v01161__00He*_00Hd_coeff).reshape((1, 27, 3, 40, 11))

# op _00Hl_cos_eval
# LANG: _00BD --> _00Hm
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01141__00Hm = np.cos(v01140__00BD)

# op _00Hv_power_combination_eval
# LANG: _00Hu, _00BL --> _00Hw
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01150__00Hw = (v01149__00Hu**1)*(v01151__00BL**1)
v01150__00Hw = (v01150__00Hw*_00Hv_coeff).reshape((1, 27, 3, 40, 11))

# op _00I6_power_combination_eval
# LANG: _00BJ, _00I5 --> _00I7
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01186__00I7 = (v01185__00I5**1)*(v0994__00BJ**1)
v01186__00I7 = (v01186__00I7*_00I6_coeff).reshape((1, 27, 3, 40, 11))

# op _00Ll_indexed_passthrough_eval
# LANG: _00Lk, _00Ln, _00Lp --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01274_V_aircraft__temp[i_v01273__00Lk__00Ll_indexed_passthrough_eval] = v01273__00Lk.flatten()
v01274_V_aircraft = v01274_V_aircraft__temp.copy()
v01274_V_aircraft__temp[i_v01275__00Ln__00Ll_indexed_passthrough_eval] = v01275__00Ln.flatten()
v01274_V_aircraft = v01274_V_aircraft__temp.copy()
v01274_V_aircraft__temp[i_v01276__00Lp__00Ll_indexed_passthrough_eval] = v01276__00Lp.flatten()
v01274_V_aircraft = v01274_V_aircraft__temp.copy()

# op _00YF_linear_combination_eval
# LANG: _00YC, _00YE --> _00YG
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01716__00YG = _00YF_constant+1*v01715__00YC+1*v01717__00YE

# op _00YT_power_combination_eval
# LANG: _00To, _00YS --> _00YU
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01707__00YU = (v01706__00YS**1)*(v01540__00To**1)
v01707__00YU = (v01707__00YU*_00YT_coeff).reshape((1, 27, 3, 40, 11))

# op _00Yt_linear_combination_eval
# LANG: _00Yq, _00Ys --> _00Yu
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01682__00Yu = _00Yt_constant+1*v01681__00Yq+1*v01684__00Ys

# op _00Z0_cos_eval
# LANG: _00Ti --> _00Z1
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01687__00Z1 = np.cos(v01686__00Ti)

# op _00ZE_power_combination_eval
# LANG: _00Tq, _00ZD --> _00ZF
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01727__00ZF = (v01726__00ZD**1)*(v01697__00Tq**1)
v01727__00ZF = (v01727__00ZF*_00ZE_coeff).reshape((1, 27, 3, 40, 11))

# op _00ZM_power_combination_eval
# LANG: _00To, _00ZL --> _00ZN
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01732__00ZN = (v01731__00ZL**1)*(v01540__00To**1)
v01732__00ZN = (v01732__00ZN*_00ZM_coeff).reshape((1, 27, 3, 40, 11))

# op _00Za_power_combination_eval
# LANG: _00Z9, _00Tq --> _00Zb
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01696__00Zb = (v01695__00Z9**1)*(v01697__00Tq**1)
v01696__00Zb = (v01696__00Zb*_00Za_coeff).reshape((1, 27, 3, 40, 11))

# op _00Zi_power_combination_eval
# LANG: _00To, _00Zh --> _00Zj
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01702__00Zj = (v01701__00Zh**1)*(v01540__00To**1)
v01702__00Zj = (v01702__00Zj*_00Zi_coeff).reshape((1, 27, 3, 40, 11))

# op _00Zu_cos_eval
# LANG: _00Ti --> _00Zv
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01719__00Zv = np.cos(v01686__00Ti)

# op _0120_indexed_passthrough_eval
# LANG: _011_, _0122, _0124 --> V_aircraft
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01820_V_aircraft__temp[i_v01819__011___0120_indexed_passthrough_eval] = v01819__011_.flatten()
v01820_V_aircraft = v01820_V_aircraft__temp.copy()
v01820_V_aircraft__temp[i_v01821__0122__0120_indexed_passthrough_eval] = v01821__0122.flatten()
v01820_V_aircraft = v01820_V_aircraft__temp.copy()
v01820_V_aircraft__temp[i_v01822__0124__0120_indexed_passthrough_eval] = v01822__0124.flatten()
v01820_V_aircraft = v01820_V_aircraft__temp.copy()

# op _00HF_power_combination_eval
# LANG: _00Hw, _00HE --> _00HG
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01152__00HG = (v01150__00Hw**1)*(v01156__00HE**-1)
v01152__00HG = (v01152__00HG*_00HF_coeff).reshape((1, 27, 3, 40, 11))

# op _00HR_power_combination_eval
# LANG: _00H0, _00HQ --> _00HS
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01172__00HS = (v01170__00H0**1)*(v01173__00HQ**1)
v01172__00HS = (v01172__00HS*_00HR_coeff).reshape((1, 27, 3, 40, 11))

# op _00Hf_power_combination_eval
# LANG: _00BL, _00He --> _00Hg
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01162__00Hg = (v01161__00He**1)*(v01151__00BL**-1)
v01162__00Hg = (v01162__00Hg*_00Hf_coeff).reshape((1, 27, 3, 40, 11))

# op _00Hh_sin_eval
# LANG: _00BD --> _00Hi
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01164__00Hi = np.sin(v01140__00BD)

# op _00Hn_power_combination_eval
# LANG: _00GP, _00Hm --> _00Ho
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01139__00Ho = (v01136__00GP**1)*(v01141__00Hm**1)
v01139__00Ho = (v01139__00Ho*_00Hn_coeff).reshape((1, 27, 3, 40, 11))

# op _00I8_power_combination_eval
# LANG: _00H_, _00I7 --> _00I9
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01182__00I9 = (v01181__00H_**1)*(v01186__00I7**-1)
v01182__00I9 = (v01182__00I9*_00I8_coeff).reshape((1, 27, 3, 40, 11))

# op _00Lq expand_array_eval
# LANG: V_aircraft --> _00Lr
# SHAPES: (1, 3) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01283__00Lr = np.einsum('ab,c->abc', v01274_V_aircraft.reshape((1, 3)) ,np.ones((27,))).reshape((1, 3, 27))

# op _00Lw expand_array_eval
# LANG: time_vectors --> _00Lx
# SHAPES: (27,) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01289__00Lx = np.einsum('c,ab->abc', v01288_time_vectors.reshape((27,)) ,np.ones((1, 3))).reshape((1, 3, 27))

# op _00YV_power_combination_eval
# LANG: _00Tq, _00YU --> _00YW
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01708__00YW = (v01707__00YU**1)*(v01697__00Tq**-1)
v01708__00YW = (v01708__00YW*_00YV_coeff).reshape((1, 27, 3, 40, 11))

# op _00YX_sin_eval
# LANG: _00Ti --> _00YY
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01710__00YY = np.sin(v01686__00Ti)

# op _00Z2_power_combination_eval
# LANG: _00Yu, _00Z1 --> _00Z3
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01685__00Z3 = (v01682__00Yu**1)*(v01687__00Z1**1)
v01685__00Z3 = (v01685__00Z3*_00Z2_coeff).reshape((1, 27, 3, 40, 11))

# op _00ZO_power_combination_eval
# LANG: _00ZF, _00ZN --> _00ZP
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01728__00ZP = (v01727__00ZF**1)*(v01732__00ZN**-1)
v01728__00ZP = (v01728__00ZP*_00ZO_coeff).reshape((1, 27, 3, 40, 11))

# op _00Zk_power_combination_eval
# LANG: _00Zb, _00Zj --> _00Zl
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01698__00Zl = (v01696__00Zb**1)*(v01702__00Zj**-1)
v01698__00Zl = (v01698__00Zl*_00Zk_coeff).reshape((1, 27, 3, 40, 11))

# op _00Zw_power_combination_eval
# LANG: _00YG, _00Zv --> _00Zx
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01718__00Zx = (v01716__00YG**1)*(v01719__00Zv**1)
v01718__00Zx = (v01718__00Zx*_00Zw_coeff).reshape((1, 27, 3, 40, 11))

# op _0125 expand_array_eval
# LANG: V_aircraft --> _0126
# SHAPES: (1, 3) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01829__0126 = np.einsum('ab,c->abc', v01820_V_aircraft.reshape((1, 3)) ,np.ones((27,))).reshape((1, 3, 27))

# op _012b expand_array_eval
# LANG: time_vectors --> _012c
# SHAPES: (27,) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01835__012c = np.einsum('c,ab->abc', v01834_time_vectors.reshape((27,)) ,np.ones((1, 3))).reshape((1, 3, 27))

# op _00HH_linear_combination_eval
# LANG: _00Ho, _00HG --> _00HI
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01142__00HI = _00HH_constant+1*v01139__00Ho+-1*v01152__00HG

# op _00Hj_power_combination_eval
# LANG: _00Hg, _00Hi --> _00Hk
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01163__00Hk = (v01162__00Hg**1)*(v01164__00Hi**1)
v01163__00Hk = (v01163__00Hk*_00Hj_coeff).reshape((1, 27, 3, 40, 11))

# op _00Ia_linear_combination_eval
# LANG: _00HS, _00I9 --> _00Ib
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01174__00Ib = _00Ia_constant+1*v01172__00HS+-1*v01182__00I9

# op _00JR_power_combination_eval
# LANG: rotor_1_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v012_rotor_1_disk_origin = v012_rotor_1_disk_origin.reshape((3,))
v01233_origin = (v012_rotor_1_disk_origin**1)
v01233_origin = (v01233_origin*_00JR_coeff).reshape((3,))
v012_rotor_1_disk_origin = v012_rotor_1_disk_origin.reshape((1, 3))

# op _00LA_decompose_eval
# LANG: _00Lr --> _00LB, _00LJ, _00LQ
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01284__00LB = ((v01283__00Lr.flatten())[src_indices__00LB__00LA]).reshape((1, 1, 27))
v01285__00LJ = ((v01283__00Lr.flatten())[src_indices__00LJ__00LA]).reshape((1, 1, 27))
v01286__00LQ = ((v01283__00Lr.flatten())[src_indices__00LQ__00LA]).reshape((1, 1, 27))

# op _00LC_decompose_eval
# LANG: _00Lx --> _00LD, _00LK, _00LR
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01290__00LD = ((v01289__00Lx.flatten())[src_indices__00LD__00LC]).reshape((1, 1, 27))
v01291__00LK = ((v01289__00Lx.flatten())[src_indices__00LK__00LC]).reshape((1, 1, 27))
v01292__00LR = ((v01289__00Lx.flatten())[src_indices__00LR__00LC]).reshape((1, 1, 27))

# op _00Lt expand_array_eval
# LANG: aircraft_location --> _00Lu
# SHAPES: (3, 27) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01278__00Lu = np.einsum('bc,a->abc', v01277_aircraft_location.reshape((3, 27)) ,np.ones((1,))).reshape((1, 3, 27))

# op _00YZ_power_combination_eval
# LANG: _00YW, _00YY --> _00Y_
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01709__00Y_ = (v01708__00YW**1)*(v01710__00YY**1)
v01709__00Y_ = (v01709__00Y_*_00YZ_coeff).reshape((1, 27, 3, 40, 11))

# op _00ZQ_linear_combination_eval
# LANG: _00Zx, _00ZP --> _00ZR
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01720__00ZR = _00ZQ_constant+1*v01718__00Zx+-1*v01728__00ZP

# op _00Zm_linear_combination_eval
# LANG: _00Z3, _00Zl --> _00Zn
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01688__00Zn = _00Zm_constant+1*v01685__00Z3+-1*v01698__00Zl

# op _010w_power_combination_eval
# LANG: rotor_2_disk_origin --> origin
# SHAPES: (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v022_rotor_2_disk_origin = v022_rotor_2_disk_origin.reshape((3,))
v01779_origin = (v022_rotor_2_disk_origin**1)
v01779_origin = (v01779_origin*_010w_coeff).reshape((3,))
v022_rotor_2_disk_origin = v022_rotor_2_disk_origin.reshape((1, 3))

# op _0128 expand_array_eval
# LANG: aircraft_location --> _0129
# SHAPES: (3, 27) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01824__0129 = np.einsum('bc,a->abc', v01823_aircraft_location.reshape((3, 27)) ,np.ones((1,))).reshape((1, 3, 27))

# op _012f_decompose_eval
# LANG: _0126 --> _012g, _012o, _012v
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01830__012g = ((v01829__0126.flatten())[src_indices__012g__012f]).reshape((1, 1, 27))
v01831__012o = ((v01829__0126.flatten())[src_indices__012o__012f]).reshape((1, 1, 27))
v01832__012v = ((v01829__0126.flatten())[src_indices__012v__012f]).reshape((1, 1, 27))

# op _012h_decompose_eval
# LANG: _012c --> _012i, _012p, _012w
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01836__012i = ((v01835__012c.flatten())[src_indices__012i__012h]).reshape((1, 1, 27))
v01837__012p = ((v01835__012c.flatten())[src_indices__012p__012h]).reshape((1, 1, 27))
v01838__012w = ((v01835__012c.flatten())[src_indices__012w__012h]).reshape((1, 1, 27))

# op _00HJ_power_combination_eval
# LANG: coeff_matrix_A, _00HI --> _00HK
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01133__00HK = (v01132_coeff_matrix_A**1)*(v01142__00HI**1)
v01133__00HK = (v01133__00HK*_00HJ_coeff).reshape((1, 27, 3, 40, 11))

# op _00HL_bessel_eval
# LANG: _00Hk --> _00HM
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01165__00HM=_00HL_bessel_eval(_00HL_bessel_eval_order,v01163__00Hk)

# op _00Ic_power_combination_eval
# LANG: coeff_matrix_B, _00Ib --> _00Id
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01168__00Id = (v01167_coeff_matrix_B**1)*(v01174__00Ib**1)
v01168__00Id = (v01168__00Id*_00Ic_coeff).reshape((1, 27, 3, 40, 11))

# op _00Ie_bessel_eval
# LANG: _00Hk --> _00If
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01188__00If=_00Ie_bessel_eval(_00Ie_bessel_eval_order,v01163__00Hk)

# op _00LE_power_combination_eval
# LANG: _00LB, _00LD --> _00LF
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01287__00LF = (v01284__00LB**1)*(v01290__00LD**1)
v01287__00LF = (v01287__00LF*_00LE_coeff).reshape((1, 1, 27))

# op _00LL_power_combination_eval
# LANG: _00LJ, _00LK --> _00LM
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01294__00LM = (v01285__00LJ**1)*(v01291__00LK**1)
v01294__00LM = (v01294__00LM*_00LL_coeff).reshape((1, 1, 27))

# op _00Ly_decompose_eval
# LANG: _00Lu --> _00Lz, _00LI, _00LP
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01279__00Lz = ((v01278__00Lu.flatten())[src_indices__00Lz__00Ly]).reshape((1, 1, 27))
v01280__00LI = ((v01278__00Lu.flatten())[src_indices__00LI__00Ly]).reshape((1, 1, 27))
v01281__00LP = ((v01278__00Lu.flatten())[src_indices__00LP__00Ly]).reshape((1, 1, 27))

# op _00M2 expand_array_eval
# LANG: origin --> _00M3
# SHAPES: (3,) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01301__00M3 = np.einsum('b,ac->abc', v01233_origin.reshape((3,)) ,np.ones((1, 27))).reshape((1, 3, 27))

# op _00ZS_power_combination_eval
# LANG: coeff_matrix_B, _00ZR --> _00ZT
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01714__00ZT = (v01713_coeff_matrix_B**1)*(v01720__00ZR**1)
v01714__00ZT = (v01714__00ZT*_00ZS_coeff).reshape((1, 27, 3, 40, 11))

# op _00ZU_bessel_eval
# LANG: _00Y_ --> _00ZV
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01734__00ZV=_00ZU_bessel_eval(_00ZU_bessel_eval_order,v01709__00Y_)

# op _00Zo_power_combination_eval
# LANG: coeff_matrix_A, _00Zn --> _00Zp
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01679__00Zp = (v01678_coeff_matrix_A**1)*(v01688__00Zn**1)
v01679__00Zp = (v01679__00Zp*_00Zo_coeff).reshape((1, 27, 3, 40, 11))

# op _00Zq_bessel_eval
# LANG: _00Y_ --> _00Zr
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01711__00Zr=_00Zq_bessel_eval(_00Zq_bessel_eval_order,v01709__00Y_)

# op _012I expand_array_eval
# LANG: origin --> _012J
# SHAPES: (3,) --> (1, 3, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01847__012J = np.einsum('b,ac->abc', v01779_origin.reshape((3,)) ,np.ones((1, 27))).reshape((1, 3, 27))

# op _012d_decompose_eval
# LANG: _0129 --> _012e, _012n, _012u
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01825__012e = ((v01824__0129.flatten())[src_indices__012e__012d]).reshape((1, 1, 27))
v01826__012n = ((v01824__0129.flatten())[src_indices__012n__012d]).reshape((1, 1, 27))
v01827__012u = ((v01824__0129.flatten())[src_indices__012u__012d]).reshape((1, 1, 27))

# op _012j_power_combination_eval
# LANG: _012g, _012i --> _012k
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01833__012k = (v01830__012g**1)*(v01836__012i**1)
v01833__012k = (v01833__012k*_012j_coeff).reshape((1, 1, 27))

# op _012q_power_combination_eval
# LANG: _012o, _012p --> _012r
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01840__012r = (v01831__012o**1)*(v01837__012p**1)
v01840__012r = (v01840__012r*_012q_coeff).reshape((1, 1, 27))

# op _00HN_power_combination_eval
# LANG: _00HK, _00HM --> _00HO
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01157__00HO = (v01133__00HK**1)*(v01165__00HM**1)
v01157__00HO = (v01157__00HO*_00HN_coeff).reshape((1, 27, 3, 40, 11))

# op _00Ig_power_combination_eval
# LANG: _00Id, _00If --> _00Ih
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01187__00Ih = (v01168__00Id**1)*(v01188__00If**1)
v01187__00Ih = (v01187__00Ih*_00Ig_coeff).reshape((1, 27, 3, 40, 11))

# op _00JU_power_combination_eval
# LANG: rotor_1_disk_in_plane_1 --> _00JV
# SHAPES: (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v08_rotor_1_disk_in_plane_1 = v08_rotor_1_disk_in_plane_1.reshape((3,))
v01234__00JV = (v08_rotor_1_disk_in_plane_1**1)
v01234__00JV = (v01234__00JV*_00JU_coeff).reshape((3,))
v08_rotor_1_disk_in_plane_1 = v08_rotor_1_disk_in_plane_1.reshape((1, 3))

# op _00LG_linear_combination_eval
# LANG: _00Lz, _00LF --> aircraft_x_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01282_aircraft_x_pos = _00LG_constant+1*v01279__00Lz+1*v01287__00LF

# op _00LN_linear_combination_eval
# LANG: _00LI, _00LM --> aircraft_y_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01293_aircraft_y_pos = _00LN_constant+1*v01280__00LI+1*v01294__00LM

# op _00LS_power_combination_eval
# LANG: _00LQ, _00LR --> _00LT
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01296__00LT = (v01286__00LQ**1)*(v01292__00LR**1)
v01296__00LT = (v01296__00LT*_00LS_coeff).reshape((1, 1, 27))

# op _00M4_decompose_eval
# LANG: _00M3 --> _00M5, _00Ma, _00Mf
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01302__00M5 = ((v01301__00M3.flatten())[src_indices__00M5__00M4]).reshape((1, 1, 27))
v01303__00Ma = ((v01301__00M3.flatten())[src_indices__00Ma__00M4]).reshape((1, 1, 27))
v01304__00Mf = ((v01301__00M3.flatten())[src_indices__00Mf__00M4]).reshape((1, 1, 27))

# op _00ZW_power_combination_eval
# LANG: _00ZT, _00ZV --> _00ZX
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01733__00ZX = (v01714__00ZT**1)*(v01734__00ZV**1)
v01733__00ZX = (v01733__00ZX*_00ZW_coeff).reshape((1, 27, 3, 40, 11))

# op _00Zs_power_combination_eval
# LANG: _00Zp, _00Zr --> _00Zt
# SHAPES: (1, 27, 3, 40, 11), (1, 27, 3, 40, 11) --> (1, 27, 3, 40, 11)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01703__00Zt = (v01679__00Zp**1)*(v01711__00Zr**1)
v01703__00Zt = (v01703__00Zt*_00Zs_coeff).reshape((1, 27, 3, 40, 11))

# op _00bJ_power_combination_eval
# LANG: _angular_speed --> _00bK
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0439__00bK = (v0213__angular_speed**1)
v0439__00bK = (v0439__00bK*_00bJ_coeff).reshape((1, 40, 30))

# op _00qM_power_combination_eval
# LANG: _angular_speed --> _00qN
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0812__00qN = (v0586__angular_speed**1)
v0812__00qN = (v0812__00qN*_00qM_coeff).reshape((1, 40, 30))

# op _010z_power_combination_eval
# LANG: rotor_2_disk_in_plane_1 --> _010A
# SHAPES: (3,) --> (3,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v018_rotor_2_disk_in_plane_1 = v018_rotor_2_disk_in_plane_1.reshape((3,))
v01780__010A = (v018_rotor_2_disk_in_plane_1**1)
v01780__010A = (v01780__010A*_010z_coeff).reshape((3,))
v018_rotor_2_disk_in_plane_1 = v018_rotor_2_disk_in_plane_1.reshape((1, 3))

# op _012K_decompose_eval
# LANG: _012J --> _012L, _012Q, _012V
# SHAPES: (1, 3, 27) --> (1, 1, 27), (1, 1, 27), (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01848__012L = ((v01847__012J.flatten())[src_indices__012L__012K]).reshape((1, 1, 27))
v01849__012Q = ((v01847__012J.flatten())[src_indices__012Q__012K]).reshape((1, 1, 27))
v01850__012V = ((v01847__012J.flatten())[src_indices__012V__012K]).reshape((1, 1, 27))

# op _012l_linear_combination_eval
# LANG: _012e, _012k --> aircraft_x_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01828_aircraft_x_pos = _012l_constant+1*v01825__012e+1*v01833__012k

# op _012s_linear_combination_eval
# LANG: _012n, _012r --> aircraft_y_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01839_aircraft_y_pos = _012s_constant+1*v01826__012n+1*v01840__012r

# op _012x_power_combination_eval
# LANG: _012v, _012w --> _012y
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01842__012y = (v01832__012v**1)*(v01838__012w**1)
v01842__012y = (v01842__012y*_012x_coeff).reshape((1, 1, 27))

# op _00Ii_single_tensor_sum_with_axis_eval
# LANG: _00HO --> An
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01166_An = np.sum(v01157__00HO, axis = (4,)).reshape((1, 27, 3, 40))

# op _00Ik_single_tensor_sum_with_axis_eval
# LANG: _00Ih --> Bn
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01189_Bn = np.sum(v01187__00Ih, axis = (4,)).reshape((1, 27, 3, 40))

# op _00JW pnorm_eval
# LANG: _00JV --> _00JX
# SHAPES: (3,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01235__00JX = np.linalg.norm(v01234__00JV.flatten(), ord=2)

# op _00K0 pnorm_axis_eval
# LANG: rotor_1_blade_chord_length --> _00K1
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01237__00K1 = np.sum(v014_rotor_1_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _00LU_linear_combination_eval
# LANG: _00LP, _00LT --> aircraft_z_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01295_aircraft_z_pos = _00LU_constant+1*v01281__00LP+1*v01296__00LT

# op _00LW expand_array_eval
# LANG: init_obs_x_loc --> _00LX
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01298__00LX = np.einsum('c,ab->abc', v01297_init_obs_x_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _00LY expand_array_eval
# LANG: init_obs_y_loc --> _00LZ
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01306__00LZ = np.einsum('c,ab->abc', v01305_init_obs_y_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _00M6_linear_combination_eval
# LANG: aircraft_x_pos, _00M5 --> _00M7
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01300__00M7 = _00M6_constant+1*v01282_aircraft_x_pos+1*v01302__00M5

# op _00Mb_linear_combination_eval
# LANG: aircraft_y_pos, _00Ma --> _00Mc
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01308__00Mc = _00Mb_constant+1*v01293_aircraft_y_pos+1*v01303__00Ma

# op _00ZY_single_tensor_sum_with_axis_eval
# LANG: _00Zt --> An
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01712_An = np.sum(v01703__00Zt, axis = (4,)).reshape((1, 27, 3, 40))

# op _00Z__single_tensor_sum_with_axis_eval
# LANG: _00ZX --> Bn
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 40)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01735_Bn = np.sum(v01733__00ZX, axis = (4,)).reshape((1, 27, 3, 40))

# op _00bL_power_combination_eval
# LANG: _00bK --> _00bM
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0440__00bM = (v0439__00bK**1)
v0440__00bM = (v0440__00bM*_00bL_coeff).reshape((1, 40, 30))

# op _00qO_power_combination_eval
# LANG: _00qN --> _00qP
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0813__00qP = (v0812__00qN**1)
v0813__00qP = (v0813__00qP*_00qO_coeff).reshape((1, 40, 30))

# op _010B pnorm_eval
# LANG: _010A --> _010C
# SHAPES: (3,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01781__010C = np.linalg.norm(v01780__010A.flatten(), ord=2)

# op _010G pnorm_axis_eval
# LANG: rotor_2_blade_chord_length --> _010H
# SHAPES: (40, 3) --> (40,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01783__010H = np.sum(v024_rotor_2_blade_chord_length**2,axis=(1,))**(1 / 2)

# op _012B expand_array_eval
# LANG: init_obs_x_loc --> _012C
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01844__012C = np.einsum('c,ab->abc', v01843_init_obs_x_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _012D expand_array_eval
# LANG: init_obs_y_loc --> _012E
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01852__012E = np.einsum('c,ab->abc', v01851_init_obs_y_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _012M_linear_combination_eval
# LANG: aircraft_x_pos, _012L --> _012N
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01846__012N = _012M_constant+1*v01828_aircraft_x_pos+1*v01848__012L

# op _012R_linear_combination_eval
# LANG: aircraft_y_pos, _012Q --> _012S
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01854__012S = _012R_constant+1*v01839_aircraft_y_pos+1*v01849__012Q

# op _012z_linear_combination_eval
# LANG: _012u, _012y --> aircraft_z_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01841_aircraft_z_pos = _012z_constant+1*v01827__012u+1*v01842__012y

# op _00Iq_decompose_eval
# LANG: n_var --> _00Ir
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01190__00Ir = ((v01147_n_var.flatten())[src_indices__00Ir__00Iq]).reshape((1, 27, 3, 1, 1))

# op _00JC_decompose_eval
# LANG: Bn --> _00JD, _00JE
# SHAPES: (1, 27, 3, 40) --> (1, 27, 3, 39), (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01226__00JD = ((v01189_Bn.flatten())[src_indices__00JD__00JC]).reshape((1, 27, 3, 39))
v01227__00JE = ((v01189_Bn.flatten())[src_indices__00JE__00JC]).reshape((1, 27, 3, 39))

# op _00JY_power_combination_eval
# LANG: _00JX --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01236_propeller_radius = (v01235__00JX**1)
v01236_propeller_radius = (v01236_propeller_radius*_00JY_coeff).reshape((1,))

# op _00Jn_decompose_eval
# LANG: An --> _00Jo, _00Jp
# SHAPES: (1, 27, 3, 40) --> (1, 27, 3, 39), (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01219__00Jo = ((v01166_An.flatten())[src_indices__00Jo__00Jn]).reshape((1, 27, 3, 39))
v01220__00Jp = ((v01166_An.flatten())[src_indices__00Jp__00Jn]).reshape((1, 27, 3, 39))

# op _00K2 reshape_eval
# LANG: _00K1 --> _00K3
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01238__00K3 = v01237__00K1.reshape((40, 1))

# op _00L_ expand_array_eval
# LANG: init_obs_z_loc --> _00M0
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01310__00M0 = np.einsum('c,ab->abc', v01309_init_obs_z_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _00M8_linear_combination_eval
# LANG: _00LX, _00M7 --> rel_obs_x_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01299_rel_obs_x_pos = _00M8_constant+1*v01298__00LX+-1*v01300__00M7

# op _00Md_linear_combination_eval
# LANG: _00LZ, _00Mc --> rel_obs_y_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01307_rel_obs_y_pos = _00Md_constant+1*v01306__00LZ+-1*v01308__00Mc

# op _00Mg_linear_combination_eval
# LANG: aircraft_z_pos, _00Mf --> _00Mh
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01312__00Mh = _00Mg_constant+1*v01295_aircraft_z_pos+1*v01304__00Mf

# op _00_5_decompose_eval
# LANG: n_var --> _00_6
# SHAPES: (1, 27, 3, 40, 11) --> (1, 27, 3, 1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01736__00_6 = ((v01693_n_var.flatten())[src_indices__00_6__00_5]).reshape((1, 27, 3, 1, 1))

# op _00h3_single_tensor_sum_with_axis_eval
# LANG: _00bM --> _00h4
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0441__00h4 = np.sum(v0440__00bM, axis = (1, 2)).reshape((1,))

# op _00hd_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00he
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0446__00he = np.sum(v0201__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00w6_single_tensor_sum_with_axis_eval
# LANG: _00qP --> _00w7
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0814__00w7 = np.sum(v0813__00qP, axis = (1, 2)).reshape((1,))

# op _00wg_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00wh
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0819__00wh = np.sum(v0574__rotor_radius, axis = (1, 2)).reshape((1,))

# op _0102_decompose_eval
# LANG: An --> _0103, _0104
# SHAPES: (1, 27, 3, 40) --> (1, 27, 3, 39), (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01765__0103 = ((v01712_An.flatten())[src_indices__0103__0102]).reshape((1, 27, 3, 39))
v01766__0104 = ((v01712_An.flatten())[src_indices__0104__0102]).reshape((1, 27, 3, 39))

# op _010D_power_combination_eval
# LANG: _010C --> propeller_radius
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01782_propeller_radius = (v01781__010C**1)
v01782_propeller_radius = (v01782_propeller_radius*_010D_coeff).reshape((1,))

# op _010I reshape_eval
# LANG: _010H --> _010J
# SHAPES: (40,) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01784__010J = v01783__010H.reshape((40, 1))

# op _010h_decompose_eval
# LANG: Bn --> _010i, _010j
# SHAPES: (1, 27, 3, 40) --> (1, 27, 3, 39), (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01772__010i = ((v01735_Bn.flatten())[src_indices__010i__010h]).reshape((1, 27, 3, 39))
v01773__010j = ((v01735_Bn.flatten())[src_indices__010j__010h]).reshape((1, 27, 3, 39))

# op _012F expand_array_eval
# LANG: init_obs_z_loc --> _012G
# SHAPES: (27,) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01856__012G = np.einsum('c,ab->abc', v01855_init_obs_z_loc.reshape((27,)) ,np.ones((1, 1))).reshape((1, 1, 27))

# op _012O_linear_combination_eval
# LANG: _012C, _012N --> rel_obs_x_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01845_rel_obs_x_pos = _012O_constant+1*v01844__012C+-1*v01846__012N

# op _012T_linear_combination_eval
# LANG: _012E, _012S --> rel_obs_y_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01853_rel_obs_y_pos = _012T_constant+1*v01852__012E+-1*v01854__012S

# op _012W_linear_combination_eval
# LANG: aircraft_z_pos, _012V --> _012X
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01858__012X = _012W_constant+1*v01841_aircraft_z_pos+1*v01850__012V

# op _00Is reshape_eval
# LANG: _00Ir --> _00It
# SHAPES: (1, 27, 3, 1, 1) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01191__00It = v01190__00Ir.reshape((1, 27, 3))

# op _00Iw expand_array_eval
# LANG: _00B3 --> _00Ix
# SHAPES: (1, 27) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01196__00Ix = np.einsum('ab,c->abc', v0963__00B3.reshape((1, 27)) ,np.ones((3,))).reshape((1, 27, 3))

# op _00JF_linear_combination_eval
# LANG: _00JD, _00JE --> _00JG
# SHAPES: (1, 27, 3, 39), (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01228__00JG = _00JF_constant+1*v01226__00JD+1*v01227__00JE

# op _00JH expand_scalar_eval
# LANG: dr --> _00JI
# SHAPES: (1,) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01230__00JI = np.empty((1, 27, 3, 39))
v01230__00JI.fill(v0857_dr.item())

# op _00Jq_linear_combination_eval
# LANG: _00Jo, _00Jp --> _00Jr
# SHAPES: (1, 27, 3, 39), (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01221__00Jr = _00Jq_constant+1*v01219__00Jo+1*v01220__00Jp

# op _00Js expand_scalar_eval
# LANG: dr --> _00Jt
# SHAPES: (1,) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01223__00Jt = np.empty((1, 27, 3, 39))
v01223__00Jt.fill(v0857_dr.item())

# op _00K4_power_combination_eval
# LANG: _00K3 --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01239_chord_profile = (v01238__00K3**1)
v01239_chord_profile = (v01239_chord_profile*_00K4_coeff).reshape((40, 1))

# op _00K8_power_combination_eval
# LANG: propeller_radius --> _00K9
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01240__00K9 = (v01236_propeller_radius**1)
v01240__00K9 = (v01240__00K9*_00K8_coeff).reshape((1,))

# op _00Mi_linear_combination_eval
# LANG: _00M0, _00Mh --> rel_obs_z_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01311_rel_obs_z_pos = _00Mi_constant+1*v01310__00M0+-1*v01312__00Mh

# op _00Mk_power_combination_eval
# LANG: rel_obs_x_pos --> _00Ml
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01313__00Ml = (v01299_rel_obs_x_pos**2)
v01313__00Ml = (v01313__00Ml*_00Mk_coeff).reshape((1, 1, 27))

# op _00Mm_power_combination_eval
# LANG: rel_obs_y_pos --> _00Mn
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01315__00Mn = (v01307_rel_obs_y_pos**2)
v01315__00Mn = (v01315__00Mn*_00Mm_coeff).reshape((1, 1, 27))

# op _00_7 reshape_eval
# LANG: _00_6 --> _00_8
# SHAPES: (1, 27, 3, 1, 1) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01737__00_8 = v01736__00_6.reshape((1, 27, 3))

# op _00_b expand_array_eval
# LANG: _00SJ --> _00_c
# SHAPES: (1, 27) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01742__00_c = np.einsum('ab,c->abc', v01509__00SJ.reshape((1, 27)) ,np.ones((3,))).reshape((1, 27, 3))

# op _00g6_single_tensor_sum_with_axis_eval
# LANG: _local_thrust --> _00g7
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0340__00g7 = np.sum(v0325__local_thrust, axis = (1, 2)).reshape((1,))

# op _00h5_power_combination_eval
# LANG: _00h4 --> _00h6
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0442__00h6 = (v0441__00h4**1)
v0442__00h6 = (v0442__00h6*_00h5_coeff).reshape((1,))

# op _00hf_power_combination_eval
# LANG: _00he --> _00hg
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0447__00hg = (v0446__00he**1)
v0447__00hg = (v0447__00hg*_00hf_coeff).reshape((1,))

# op _00v9_single_tensor_sum_with_axis_eval
# LANG: _local_thrust --> _00va
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0713__00va = np.sum(v0698__local_thrust, axis = (1, 2)).reshape((1,))

# op _00w8_power_combination_eval
# LANG: _00w7 --> _00w9
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0815__00w9 = (v0814__00w7**1)
v0815__00w9 = (v0815__00w9*_00w8_coeff).reshape((1,))

# op _00wi_power_combination_eval
# LANG: _00wh --> _00wj
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0820__00wj = (v0819__00wh**1)
v0820__00wj = (v0820__00wj*_00wi_coeff).reshape((1,))

# op _0105_linear_combination_eval
# LANG: _0103, _0104 --> _0106
# SHAPES: (1, 27, 3, 39), (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01767__0106 = _0105_constant+1*v01765__0103+1*v01766__0104

# op _0107 expand_scalar_eval
# LANG: dr --> _0108
# SHAPES: (1,) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01769__0108 = np.empty((1, 27, 3, 39))
v01769__0108.fill(v01403_dr.item())

# op _010K_power_combination_eval
# LANG: _010J --> chord_profile
# SHAPES: (40, 1) --> (40, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01785_chord_profile = (v01784__010J**1)
v01785_chord_profile = (v01785_chord_profile*_010K_coeff).reshape((40, 1))

# op _010O_power_combination_eval
# LANG: propeller_radius --> _010P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01786__010P = (v01782_propeller_radius**1)
v01786__010P = (v01786__010P*_010O_coeff).reshape((1,))

# op _010k_linear_combination_eval
# LANG: _010i, _010j --> _010l
# SHAPES: (1, 27, 3, 39), (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01774__010l = _010k_constant+1*v01772__010i+1*v01773__010j

# op _010m expand_scalar_eval
# LANG: dr --> _010n
# SHAPES: (1,) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01776__010n = np.empty((1, 27, 3, 39))
v01776__010n.fill(v01403_dr.item())

# op _012Y_linear_combination_eval
# LANG: _012G, _012X --> rel_obs_z_pos
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01857_rel_obs_z_pos = _012Y_constant+1*v01856__012G+-1*v01858__012X

# op _012__power_combination_eval
# LANG: rel_obs_x_pos --> _0130
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01859__0130 = (v01845_rel_obs_x_pos**2)
v01859__0130 = (v01859__0130*_012__coeff).reshape((1, 1, 27))

# op _0131_power_combination_eval
# LANG: rel_obs_y_pos --> _0132
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01861__0132 = (v01853_rel_obs_y_pos**2)
v01861__0132 = (v01861__0132*_0131_coeff).reshape((1, 1, 27))

# op _00IA_power_combination_eval
# LANG: _00It --> _00IB
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01192__00IB = (v01191__00It**1)
v01192__00IB = (v01192__00IB*_00IA_coeff).reshape((1, 27, 3))

# op _00IE_power_combination_eval
# LANG: _00Ix --> _00IF
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01197__00IF = (v01196__00Ix**1)
v01197__00IF = (v01197__00IF*_00IE_coeff).reshape((1, 27, 3))

# op _00IM_power_combination_eval
# LANG: _00It --> _00IN
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01203__00IN = (v01191__00It**1)
v01203__00IN = (v01203__00IN*_00IM_coeff).reshape((1, 27, 3))

# op _00IQ_power_combination_eval
# LANG: _00Ix --> _00IR
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01206__00IR = (v01196__00Ix**1)
v01206__00IR = (v01206__00IR*_00IQ_coeff).reshape((1, 27, 3))

# op _00Iu expand_scalar_eval
# LANG: _00Be --> _00Iv
# SHAPES: (1,) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01194__00Iv = np.empty((1, 27, 3))
v01194__00Iv.fill(v0984__00Be.item())

# op _00Iy expand_scalar_eval
# LANG: speed_of_sound --> _00Iz
# SHAPES: (1,) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01199__00Iz = np.empty((1, 27, 3))
v01199__00Iz.fill(v0906_speed_of_sound.item())

# op _00JJ_power_combination_eval
# LANG: _00JG, _00JI --> _00JK
# SHAPES: (1, 27, 3, 39), (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01229__00JK = (v01228__00JG**1)*(v01230__00JI**1)
v01229__00JK = (v01229__00JK*_00JJ_coeff).reshape((1, 27, 3, 39))

# op _00Ju_power_combination_eval
# LANG: _00Jr, _00Jt --> _00Jv
# SHAPES: (1, 27, 3, 39), (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01222__00Jv = (v01221__00Jr**1)*(v01223__00Jt**1)
v01222__00Jv = (v01222__00Jv*_00Ju_coeff).reshape((1, 27, 3, 39))

# op _00Ka_power_combination_eval
# LANG: _00K9 --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01241_dr = (v01240__00K9**1)
v01241_dr = (v01241_dr*_00Ka_coeff).reshape((1,))

# op _00Ke_power_combination_eval
# LANG: rpm --> _00Kf
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01243__00Kf = (v0531_rpm**1)
v01243__00Kf = (v01243__00Kf*_00Ke_coeff).reshape((1, 1))

# op _00MO_power_combination_eval
# LANG: rpm --> _00MP
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v0531_rpm = v0531_rpm.reshape((1,))
v01335__00MP = (v0531_rpm**1)
v01335__00MP = (v01335__00MP*_00MO_coeff).reshape((1,))
v0531_rpm = v0531_rpm.reshape((1, 1))

# op _00Mo_linear_combination_eval
# LANG: _00Ml, _00Mn --> _00Mp
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01314__00Mp = _00Mo_constant+1*v01313__00Ml+1*v01315__00Mn

# op _00Mq_power_combination_eval
# LANG: rel_obs_z_pos --> _00Mr
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01317__00Mr = (v01311_rel_obs_z_pos**2)
v01317__00Mr = (v01317__00Mr*_00Mq_coeff).reshape((1, 1, 27))

# op _00N4 single_tensor_sum_no_axis_eval
# LANG: chord_profile --> _00N5
# SHAPES: (40, 1) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01327__00N5 = np.sum(v01239_chord_profile).reshape((1,))

# op _00Px_power_combination_eval
# LANG: rpm --> _00Py
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01405__00Py = (v0158_rpm**1)
v01405__00Py = (v01405__00Py*_00Px_coeff).reshape((1, 1))

# op _00_9 expand_scalar_eval
# LANG: _00SU --> _00_a
# SHAPES: (1,) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01740__00_a = np.empty((1, 27, 3))
v01740__00_a.fill(v01530__00SU.item())

# op _00_d expand_scalar_eval
# LANG: speed_of_sound --> _00_e
# SHAPES: (1,) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01745__00_e = np.empty((1, 27, 3))
v01745__00_e.fill(v01452_speed_of_sound.item())

# op _00_f_power_combination_eval
# LANG: _00_8 --> _00_g
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01738__00_g = (v01737__00_8**1)
v01738__00_g = (v01738__00_g*_00_f_coeff).reshape((1, 27, 3))

# op _00_j_power_combination_eval
# LANG: _00_c --> _00_k
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01743__00_k = (v01742__00_c**1)
v01743__00_k = (v01743__00_k*_00_j_coeff).reshape((1, 27, 3))

# op _00_r_power_combination_eval
# LANG: _00_8 --> _00_s
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01749__00_s = (v01737__00_8**1)
v01749__00_s = (v01749__00_s*_00_r_coeff).reshape((1, 27, 3))

# op _00_v_power_combination_eval
# LANG: _00_c --> _00_w
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01752__00_w = (v01742__00_c**1)
v01752__00_w = (v01752__00_w*_00_v_coeff).reshape((1, 27, 3))

# op _00g8_power_combination_eval
# LANG: _00g7 --> T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0341_T = (v0340__00g7**1)
v0341_T = (v0341_T*_00g8_coeff).reshape((1,))

# op _00h7_power_combination_eval
# LANG: _00h6 --> _00h8
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0443__00h8 = (v0442__00h6**1)
v0443__00h8 = (v0443__00h8*_00h7_coeff).reshape((1,))

# op _00hh_power_combination_eval
# LANG: _00hg --> _00hi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0448__00hi = (v0447__00hg**1)
v0448__00hi = (v0448__00hi*_00hh_coeff).reshape((1,))

# op _00vb_power_combination_eval
# LANG: _00va --> T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0714_T = (v0713__00va**1)
v0714_T = (v0714_T*_00vb_coeff).reshape((1,))

# op _00wa_power_combination_eval
# LANG: _00w9 --> _00wb
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0816__00wb = (v0815__00w9**1)
v0816__00wb = (v0816__00wb*_00wa_coeff).reshape((1,))

# op _00wk_power_combination_eval
# LANG: _00wj --> _00wl
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0821__00wl = (v0820__00wj**1)
v0821__00wl = (v0821__00wl*_00wk_coeff).reshape((1,))

# op _00xS_power_combination_eval
# LANG: rpm --> _00xT
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0859__00xT = (v0531_rpm**1)
v0859__00xT = (v0859__00xT*_00xS_coeff).reshape((1, 1))

# op _0109_power_combination_eval
# LANG: _0106, _0108 --> _010a
# SHAPES: (1, 27, 3, 39), (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01768__010a = (v01767__0106**1)*(v01769__0108**1)
v01768__010a = (v01768__010a*_0109_coeff).reshape((1, 27, 3, 39))

# op _010Q_power_combination_eval
# LANG: _010P --> dr
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01787_dr = (v01786__010P**1)
v01787_dr = (v01787_dr*_010Q_coeff).reshape((1,))

# op _010U_power_combination_eval
# LANG: rpm --> _010V
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01789__010V = (v0158_rpm**1)
v01789__010V = (v01789__010V*_010U_coeff).reshape((1, 1))

# op _010o_power_combination_eval
# LANG: _010l, _010n --> _010p
# SHAPES: (1, 27, 3, 39), (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01775__010p = (v01774__010l**1)*(v01776__010n**1)
v01775__010p = (v01775__010p*_010o_coeff).reshape((1, 27, 3, 39))

# op _0133_linear_combination_eval
# LANG: _0130, _0132 --> _0134
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01860__0134 = _0133_constant+1*v01859__0130+1*v01861__0132

# op _0135_power_combination_eval
# LANG: rel_obs_z_pos --> _0136
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01863__0136 = (v01857_rel_obs_z_pos**2)
v01863__0136 = (v01863__0136*_0135_coeff).reshape((1, 1, 27))

# op _013K single_tensor_sum_no_axis_eval
# LANG: chord_profile --> _013L
# SHAPES: (40, 1) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01873__013L = np.sum(v01785_chord_profile).reshape((1,))

# op _013t_power_combination_eval
# LANG: rpm --> _013u
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v0158_rpm = v0158_rpm.reshape((1,))
v01881__013u = (v0158_rpm**1)
v01881__013u = (v01881__013u*_013t_coeff).reshape((1,))
v0158_rpm = v0158_rpm.reshape((1, 1))

# op _00IC_power_combination_eval
# LANG: _00IB, _00Iv --> _00ID
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01193__00ID = (v01192__00IB**1)*(v01194__00Iv**1)
v01193__00ID = (v01193__00ID*_00IC_coeff).reshape((1, 27, 3))

# op _00IG_power_combination_eval
# LANG: _00IF, _00Iz --> _00IH
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01198__00IH = (v01197__00IF**1)*(v01199__00Iz**1)
v01198__00IH = (v01198__00IH*_00IG_coeff).reshape((1, 27, 3))

# op _00IO_power_combination_eval
# LANG: _00Iv, _00IN --> _00IP
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01204__00IP = (v01203__00IN**1)*(v01194__00Iv**1)
v01204__00IP = (v01204__00IP*_00IO_coeff).reshape((1, 27, 3))

# op _00IS_power_combination_eval
# LANG: _00Iz, _00IR --> _00IT
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01207__00IT = (v01206__00IR**1)*(v01199__00Iz**1)
v01207__00IT = (v01207__00IT*_00IS_coeff).reshape((1, 27, 3))

# op _00JL_power_combination_eval
# LANG: _00JK --> _00JM
# SHAPES: (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01231__00JM = (v01229__00JK**1)
v01231__00JM = (v01231__00JM*_00JL_coeff).reshape((1, 27, 3, 39))

# op _00Jw_power_combination_eval
# LANG: _00Jv --> _00Jx
# SHAPES: (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01224__00Jx = (v01222__00Jv**1)
v01224__00Jx = (v01224__00Jx*_00Jw_coeff).reshape((1, 27, 3, 39))

# op _00Kg_power_combination_eval
# LANG: _00Kf --> _00Kh
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01244__00Kh = (v01243__00Kf**1)
v01244__00Kh = (v01244__00Kh*_00Kg_coeff).reshape((1, 1))

# op _00MQ_power_combination_eval
# LANG: _00MP --> _00MR
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01336__00MR = (v01335__00MP**1)
v01336__00MR = (v01336__00MR*_00MQ_coeff).reshape((1,))

# op _00Ms_linear_combination_eval
# LANG: _00Mp, _00Mr --> _00Mt
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01316__00Mt = _00Ms_constant+1*v01314__00Mp+1*v01317__00Mr

# op _00N6_power_combination_eval
# LANG: _00N5, dr --> _00N7
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01328__00N7 = (v01327__00N5**1)*(v01241_dr**1)
v01328__00N7 = (v01328__00N7*_00N6_coeff).reshape((1,))

# op _00Nc expand_scalar_eval
# LANG: propeller_radius --> _00Nd
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01332__00Nd = np.empty((1, 27))
v01332__00Nd.fill(v01236_propeller_radius.item())

# op _00Pz_power_combination_eval
# LANG: _00Py --> _00PA
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01406__00PA = (v01405__00Py**1)
v01406__00PA = (v01406__00PA*_00Pz_coeff).reshape((1, 1))

# op _00_h_power_combination_eval
# LANG: _00_g, _00_a --> _00_i
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01739__00_i = (v01738__00_g**1)*(v01740__00_a**1)
v01739__00_i = (v01739__00_i*_00_h_coeff).reshape((1, 27, 3))

# op _00_l_power_combination_eval
# LANG: _00_k, _00_e --> _00_m
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01744__00_m = (v01743__00_k**1)*(v01745__00_e**1)
v01744__00_m = (v01744__00_m*_00_l_coeff).reshape((1, 27, 3))

# op _00_t_power_combination_eval
# LANG: _00_a, _00_s --> _00_u
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01750__00_u = (v01749__00_s**1)*(v01740__00_a**1)
v01750__00_u = (v01750__00_u*_00_t_coeff).reshape((1, 27, 3))

# op _00_x_power_combination_eval
# LANG: _00_e, _00_w --> _00_y
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01753__00_y = (v01752__00_w**1)*(v01745__00_e**1)
v01753__00_y = (v01753__00_y*_00_x_coeff).reshape((1, 27, 3))

# op _00h1_power_combination_eval
# LANG: T, density --> _00h2
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0242_density = v0242_density.reshape((1,))
v0437__00h2 = (v0341_T**1)*(v0242_density**-1)
v0437__00h2 = (v0437__00h2*_00h1_coeff).reshape((1,))
v0242_density = v0242_density.reshape((1, 1))

# op _00h9_power_combination_eval
# LANG: _00h8 --> _00ha
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0444__00ha = (v0443__00h8**2)
v0444__00ha = (v0444__00ha*_00h9_coeff).reshape((1,))

# op _00hj_power_combination_eval
# LANG: _00hi --> _00hk
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0449__00hk = (v0448__00hi**1)
v0449__00hk = (v0449__00hk*_00hj_coeff).reshape((1,))

# op _00w4_power_combination_eval
# LANG: T, density --> _00w5
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0615_density = v0615_density.reshape((1,))
v0810__00w5 = (v0714_T**1)*(v0615_density**-1)
v0810__00w5 = (v0810__00w5*_00w4_coeff).reshape((1,))
v0615_density = v0615_density.reshape((1, 1))

# op _00wc_power_combination_eval
# LANG: _00wb --> _00wd
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0817__00wd = (v0816__00wb**2)
v0817__00wd = (v0817__00wd*_00wc_coeff).reshape((1,))

# op _00wm_power_combination_eval
# LANG: _00wl --> _00wn
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0822__00wn = (v0821__00wl**1)
v0822__00wn = (v0822__00wn*_00wm_coeff).reshape((1,))

# op _00xU_power_combination_eval
# LANG: _00xT --> _00xV
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0860__00xV = (v0859__00xT**1)
v0860__00xV = (v0860__00xV*_00xU_coeff).reshape((1, 1))

# op _010W_power_combination_eval
# LANG: _010V --> _010X
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01790__010X = (v01789__010V**1)
v01790__010X = (v01790__010X*_010W_coeff).reshape((1, 1))

# op _010b_power_combination_eval
# LANG: _010a --> _010c
# SHAPES: (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01770__010c = (v01768__010a**1)
v01770__010c = (v01770__010c*_010b_coeff).reshape((1, 27, 3, 39))

# op _010q_power_combination_eval
# LANG: _010p --> _010r
# SHAPES: (1, 27, 3, 39) --> (1, 27, 3, 39)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01777__010r = (v01775__010p**1)
v01777__010r = (v01777__010r*_010q_coeff).reshape((1, 27, 3, 39))

# op _0137_linear_combination_eval
# LANG: _0134, _0136 --> _0138
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01862__0138 = _0137_constant+1*v01860__0134+1*v01863__0136

# op _013M_power_combination_eval
# LANG: _013L, dr --> _013N
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01874__013N = (v01873__013L**1)*(v01787_dr**1)
v01874__013N = (v01874__013N*_013M_coeff).reshape((1,))

# op _013S expand_scalar_eval
# LANG: propeller_radius --> _013T
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01878__013T = np.empty((1, 27))
v01878__013T.fill(v01782_propeller_radius.item())

# op _013v_power_combination_eval
# LANG: _013u --> _013w
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01882__013w = (v01881__013u**1)
v01882__013w = (v01882__013w*_013v_coeff).reshape((1,))

# op _00II_power_combination_eval
# LANG: _00ID, _00IH --> _00IJ
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01195__00IJ = (v01193__00ID**1)*(v01198__00IH**-1)
v01195__00IJ = (v01195__00IJ*_00II_coeff).reshape((1, 27, 3))

# op _00IU_power_combination_eval
# LANG: _00IP, _00IT --> _00IV
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01205__00IV = (v01204__00IP**1)*(v01207__00IT**-1)
v01205__00IV = (v01205__00IV*_00IU_coeff).reshape((1, 27, 3))

# op _00JN_single_tensor_sum_with_axis_eval
# LANG: _00JM --> C_imag_integrand
# SHAPES: (1, 27, 3, 39) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01232_C_imag_integrand = np.sum(v01231__00JM, axis = (3,)).reshape((1, 27, 3))

# op _00Jy_single_tensor_sum_with_axis_eval
# LANG: _00Jx --> C_real_integrand
# SHAPES: (1, 27, 3, 39) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01225_C_real_integrand = np.sum(v01224__00Jx, axis = (3,)).reshape((1, 27, 3))

# op _00Ki_power_combination_eval
# LANG: _00Kh --> _00Kj
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01245__00Kj = (v01244__00Kh**1)
v01245__00Kj = (v01245__00Kj*_00Ki_coeff).reshape((1, 1))

# op _00MS_power_combination_eval
# LANG: _00MR --> _00MT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01337__00MT = (v01336__00MR**1)
v01337__00MT = (v01337__00MT*_00MS_coeff).reshape((1,))

# op _00MU expand_scalar_eval
# LANG: propeller_radius --> _00MV
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01339__00MV = np.empty((1,))
v01339__00MV.fill(v01236_propeller_radius.item())

# op _00Mu_power_combination_eval
# LANG: _00Mt --> rel_obs_dist
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01318_rel_obs_dist = (v01316__00Mt**0.5)
v01318_rel_obs_dist = (v01318_rel_obs_dist*_00Mu_coeff).reshape((1, 1, 27))

# op _00N8 expand_scalar_eval
# LANG: _00N7 --> _00N9
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01329__00N9 = np.empty((1, 27))
v01329__00N9.fill(v01328__00N7.item())

# op _00Ne_power_combination_eval
# LANG: _00Nd --> _00Nf
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01333__00Nf = (v01332__00Nd**2)
v01333__00Nf = (v01333__00Nf*_00Ne_coeff).reshape((1, 27))

# op _00PB_power_combination_eval
# LANG: _00PA --> _00PC
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01407__00PC = (v01406__00PA**1)
v01407__00PC = (v01407__00PC*_00PB_coeff).reshape((1, 1))

# op _00_n_power_combination_eval
# LANG: _00_i, _00_m --> _00_o
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01741__00_o = (v01739__00_i**1)*(v01744__00_m**-1)
v01741__00_o = (v01741__00_o*_00_n_coeff).reshape((1, 27, 3))

# op _00_z_power_combination_eval
# LANG: _00_u, _00_y --> _00_A
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01751__00_A = (v01750__00_u**1)*(v01753__00_y**-1)
v01751__00_A = (v01751__00_A*_00_z_coeff).reshape((1, 27, 3))

# op _00hb_power_combination_eval
# LANG: _00h2, _00ha --> _00hc
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0438__00hc = (v0437__00h2**1)*(v0444__00ha**-1)
v0438__00hc = (v0438__00hc*_00hb_coeff).reshape((1,))

# op _00hl_power_combination_eval
# LANG: _00hk --> _00hm
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0450__00hm = (v0449__00hk**4)
v0450__00hm = (v0450__00hm*_00hl_coeff).reshape((1,))

# op _00we_power_combination_eval
# LANG: _00w5, _00wd --> _00wf
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0811__00wf = (v0810__00w5**1)*(v0817__00wd**-1)
v0811__00wf = (v0811__00wf*_00we_coeff).reshape((1,))

# op _00wo_power_combination_eval
# LANG: _00wn --> _00wp
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0823__00wp = (v0822__00wn**4)
v0823__00wp = (v0823__00wp*_00wo_coeff).reshape((1,))

# op _00xW_power_combination_eval
# LANG: _00xV --> _00xX
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0861__00xX = (v0860__00xV**1)
v0861__00xX = (v0861__00xX*_00xW_coeff).reshape((1, 1))

# op _010Y_power_combination_eval
# LANG: _010X --> _010Z
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01791__010Z = (v01790__010X**1)
v01791__010Z = (v01791__010Z*_010Y_coeff).reshape((1, 1))

# op _010d_single_tensor_sum_with_axis_eval
# LANG: _010c --> C_real_integrand
# SHAPES: (1, 27, 3, 39) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.An_integration_model
v01771_C_real_integrand = np.sum(v01770__010c, axis = (3,)).reshape((1, 27, 3))

# op _010s_single_tensor_sum_with_axis_eval
# LANG: _010r --> C_imag_integrand
# SHAPES: (1, 27, 3, 39) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model.Bn_integration_model
v01778_C_imag_integrand = np.sum(v01777__010r, axis = (3,)).reshape((1, 27, 3))

# op _0139_power_combination_eval
# LANG: _0138 --> rel_obs_dist
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01864_rel_obs_dist = (v01862__0138**0.5)
v01864_rel_obs_dist = (v01864_rel_obs_dist*_0139_coeff).reshape((1, 1, 27))

# op _013O expand_scalar_eval
# LANG: _013N --> _013P
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01875__013P = np.empty((1, 27))
v01875__013P.fill(v01874__013N.item())

# op _013U_power_combination_eval
# LANG: _013T --> _013V
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01879__013V = (v01878__013T**2)
v01879__013V = (v01879__013V*_013U_coeff).reshape((1, 27))

# op _013x_power_combination_eval
# LANG: _013w --> _013y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01883__013y = (v01882__013w**1)
v01883__013y = (v01883__013y*_013x_coeff).reshape((1,))

# op _013z expand_scalar_eval
# LANG: propeller_radius --> _013A
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01885__013A = np.empty((1,))
v01885__013A.fill(v01782_propeller_radius.item())

# op _00IK_power_combination_eval
# LANG: _00IJ, C_real_integrand --> _00IL
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01200__00IL = (v01195__00IJ**1)*(v01225_C_real_integrand**1)
v01200__00IL = (v01200__00IL*_00IK_coeff).reshape((1, 27, 3))

# op _00IW_power_combination_eval
# LANG: _00IV, C_imag_integrand --> _00IX
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01208__00IX = (v01205__00IV**1)*(v01232_C_imag_integrand**1)
v01208__00IX = (v01208__00IX*_00IW_coeff).reshape((1, 27, 3))

# op _00Kt_power_combination_eval
# LANG: _00Kj --> _00Ku
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01252__00Ku = (v01245__00Kj**2)
v01252__00Ku = (v01252__00Ku*_00Kt_coeff).reshape((1, 1))

# op _00Kx_power_combination_eval
# LANG: _00Kj --> _00Ky
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01255__00Ky = (v01245__00Kj**2)
v01255__00Ky = (v01255__00Ky*_00Kx_coeff).reshape((1, 1))

# op _00MW_power_combination_eval
# LANG: _00MT, _00MV --> _00MX
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01338__00MX = (v01337__00MT**1)*(v01339__00MV**1)
v01338__00MX = (v01338__00MX*_00MW_coeff).reshape((1,))

# op _00Na_power_combination_eval
# LANG: _00N9 --> Ab
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01330_Ab = (v01329__00N9**1)
v01330_Ab = (v01330_Ab*_00Na_coeff).reshape((1, 27))

# op _00Ng_power_combination_eval
# LANG: _00Nf --> _00Nh
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01334__00Nh = (v01333__00Nf**1)
v01334__00Nh = (v01334__00Nh*_00Ng_coeff).reshape((1, 27))

# op _00Oo reshape_eval
# LANG: rel_obs_dist --> _00Op
# SHAPES: (1, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01376__00Op = v01318_rel_obs_dist.reshape((1, 27))

# op _00Or reshape_eval
# LANG: rel_obs_z_pos --> _00Os
# SHAPES: (1, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01374__00Os = v01311_rel_obs_z_pos.reshape((1, 27))

# op _00PM_power_combination_eval
# LANG: _00PC --> _00PN
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01414__00PN = (v01407__00PC**2)
v01414__00PN = (v01414__00PN*_00PM_coeff).reshape((1, 1))

# op _00PQ_power_combination_eval
# LANG: _00PC --> _00PR
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01417__00PR = (v01407__00PC**2)
v01417__00PR = (v01417__00PR*_00PQ_coeff).reshape((1, 1))

# op _00_B_power_combination_eval
# LANG: _00_A, C_imag_integrand --> _00_C
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01754__00_C = (v01751__00_A**1)*(v01778_C_imag_integrand**1)
v01754__00_C = (v01754__00_C*_00_B_coeff).reshape((1, 27, 3))

# op _00_p_power_combination_eval
# LANG: _00_o, C_real_integrand --> _00_q
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01746__00_q = (v01741__00_o**1)*(v01771_C_real_integrand**1)
v01746__00_q = (v01746__00_q*_00_p_coeff).reshape((1, 27, 3))

# op _00hn_power_combination_eval
# LANG: _00hc, _00hm --> C_T
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0445_C_T = (v0438__00hc**1)*(v0450__00hm**-1)
v0445_C_T = (v0445_C_T*_00hn_coeff).reshape((1,))

# op _00wq_power_combination_eval
# LANG: _00wf, _00wp --> C_T
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0818_C_T = (v0811__00wf**1)*(v0823__00wp**-1)
v0818_C_T = (v0818_C_T*_00wq_coeff).reshape((1,))

# op _00y6_power_combination_eval
# LANG: _00xX --> _00y7
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0868__00y7 = (v0861__00xX**2)
v0868__00y7 = (v0868__00y7*_00y6_coeff).reshape((1, 1))

# op _00ya_power_combination_eval
# LANG: _00xX --> _00yb
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0871__00yb = (v0861__00xX**2)
v0871__00yb = (v0871__00yb*_00ya_coeff).reshape((1, 1))

# op _0118_power_combination_eval
# LANG: _010Z --> _0119
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01798__0119 = (v01791__010Z**2)
v01798__0119 = (v01798__0119*_0118_coeff).reshape((1, 1))

# op _011c_power_combination_eval
# LANG: _010Z --> _011d
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01801__011d = (v01791__010Z**2)
v01801__011d = (v01801__011d*_011c_coeff).reshape((1, 1))

# op _013B_power_combination_eval
# LANG: _013y, _013A --> _013C
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01884__013C = (v01883__013y**1)*(v01885__013A**1)
v01884__013C = (v01884__013C*_013B_coeff).reshape((1,))

# op _013Q_power_combination_eval
# LANG: _013P --> Ab
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01876_Ab = (v01875__013P**1)
v01876_Ab = (v01876_Ab*_013Q_coeff).reshape((1, 27))

# op _013W_power_combination_eval
# LANG: _013V --> _013X
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01880__013X = (v01879__013V**1)
v01880__013X = (v01880__013X*_013W_coeff).reshape((1, 27))

# op _0153 reshape_eval
# LANG: rel_obs_dist --> _0154
# SHAPES: (1, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01922__0154 = v01864_rel_obs_dist.reshape((1, 27))

# op _0156 reshape_eval
# LANG: rel_obs_z_pos --> _0157
# SHAPES: (1, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01920__0157 = v01857_rel_obs_z_pos.reshape((1, 27))

# op _00IY_power_combination_eval
# LANG: _00IL --> _00IZ
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01201__00IZ = (v01200__00IL**2)
v01201__00IZ = (v01201__00IZ*_00IY_coeff).reshape((1, 27, 3))

# op _00I__power_combination_eval
# LANG: _00IX --> _00J0
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01209__00J0 = (v01208__00IX**2)
v01209__00J0 = (v01209__00J0*_00I__coeff).reshape((1, 27, 3))

# op _00Kv_linear_combination_eval
# LANG: _00Ku --> _00Kw
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01253__00Kw = _00Kv_constant+1*v01252__00Ku

# op _00Kz_linear_combination_eval
# LANG: _00Ky --> _00KA
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01256__00KA = _00Kz_constant+1*v01255__00Ky

# op _00MY expand_scalar_eval
# LANG: _00MX --> _00MZ
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01340__00MZ = np.empty((1, 27))
v01340__00MZ.fill(v01338__00MX.item())

# op _00N0 expand_scalar_eval
# LANG: CT --> _00N1
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01345__00N1 = np.empty((1, 27))
v01345__00N1.fill(v0818_C_T.item())

# op _00Ni_power_combination_eval
# LANG: Ab, _00Nh --> sigma
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01331_sigma = (v01330_Ab**1)*(v01334__00Nh**-1)
v01331_sigma = (v01331_sigma*_00Ni_coeff).reshape((1, 27))

# op _00Ot_power_combination_eval
# LANG: _00Os, _00Op --> _00Ou
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01375__00Ou = (v01374__00Os**1)*(v01376__00Op**-1)
v01375__00Ou = (v01375__00Ou*_00Ot_coeff).reshape((1, 27))

# op _00PO_linear_combination_eval
# LANG: _00PN --> _00PP
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01415__00PP = _00PO_constant+1*v01414__00PN

# op _00PS_linear_combination_eval
# LANG: _00PR --> _00PT
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01418__00PT = _00PS_constant+1*v01417__00PR

# op _00_D_power_combination_eval
# LANG: _00_q --> _00_E
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01747__00_E = (v01746__00_q**2)
v01747__00_E = (v01747__00_E*_00_D_coeff).reshape((1, 27, 3))

# op _00_F_power_combination_eval
# LANG: _00_C --> _00_G
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01755__00_G = (v01754__00_C**2)
v01755__00_G = (v01755__00_G*_00_F_coeff).reshape((1, 27, 3))

# op _00y8_linear_combination_eval
# LANG: _00y7 --> _00y9
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0869__00y9 = _00y8_constant+1*v0868__00y7

# op _00yc_linear_combination_eval
# LANG: _00yb --> _00yd
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0872__00yd = _00yc_constant+1*v0871__00yb

# op _011a_linear_combination_eval
# LANG: _0119 --> _011b
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01799__011b = _011a_constant+1*v01798__0119

# op _011e_linear_combination_eval
# LANG: _011d --> _011f
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01802__011f = _011e_constant+1*v01801__011d

# op _013D expand_scalar_eval
# LANG: _013C --> _013E
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01886__013E = np.empty((1, 27))
v01886__013E.fill(v01884__013C.item())

# op _013G expand_scalar_eval
# LANG: CT --> _013H
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01891__013H = np.empty((1, 27))
v01891__013H.fill(v0445_C_T.item())

# op _013Y_power_combination_eval
# LANG: Ab, _013X --> sigma
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01877_sigma = (v01876_Ab**1)*(v01880__013X**-1)
v01877_sigma = (v01877_sigma*_013Y_coeff).reshape((1, 27))

# op _0158_power_combination_eval
# LANG: _0157, _0154 --> _0159
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01921__0159 = (v01920__0157**1)*(v01922__0154**-1)
v01921__0159 = (v01921__0159*_0158_coeff).reshape((1, 27))

# op _00J1_linear_combination_eval
# LANG: _00IZ, _00J0 --> _00J2
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01202__00J2 = _00J1_constant+1*v01201__00IZ+1*v01209__00J0

# op _00KB_power_combination_eval
# LANG: _00Kw, _00KA --> _00KC
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01254__00KC = (v01253__00Kw**1)*(v01256__00KA**1)
v01254__00KC = (v01254__00KC*_00KB_coeff).reshape((1, 1))

# op _00Kp_power_combination_eval
# LANG: _00Kj --> _00Kq
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01249__00Kq = (v01245__00Kj**2)
v01249__00Kq = (v01249__00Kq*_00Kp_coeff).reshape((1, 1))

# op _00NC_power_combination_eval
# LANG: _00MZ --> _00ND
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01358__00ND = (v01340__00MZ**7.44)
v01358__00ND = (v01358__00ND*_00NC_coeff).reshape((1, 27))

# op _00NE_power_combination_eval
# LANG: Ab --> _00NF
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01360__00NF = (v01330_Ab**0.9)
v01360__00NF = (v01360__00NF*_00NE_coeff).reshape((1, 27))

# op _00NI_power_combination_eval
# LANG: sigma, _00N1 --> _00NJ
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01362__00NJ = (v01345__00N1**1)*(v01331_sigma**-1)
v01362__00NJ = (v01362__00NJ*_00NI_coeff).reshape((1, 27))

# op _00Nk_power_combination_eval
# LANG: _00MZ --> _00Nl
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01341__00Nl = (v01340__00MZ**3.68)
v01341__00Nl = (v01341__00Nl*_00Nk_coeff).reshape((1, 27))

# op _00Nm_power_combination_eval
# LANG: Ab --> _00Nn
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01343__00Nn = (v01330_Ab**0.9)
v01343__00Nn = (v01343__00Nn*_00Nm_coeff).reshape((1, 27))

# op _00Nq_power_combination_eval
# LANG: sigma, _00N1 --> _00Nr
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01346__00Nr = (v01345__00N1**1)*(v01331_sigma**-1)
v01346__00Nr = (v01346__00Nr*_00Nq_coeff).reshape((1, 27))

# op _00Ov_arcsin_eval
# LANG: _00Ou --> _00Ow
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01377__00Ow = np.arcsin(v01375__00Ou)

# op _00PI_power_combination_eval
# LANG: _00PC --> _00PJ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01411__00PJ = (v01407__00PC**2)
v01411__00PJ = (v01411__00PJ*_00PI_coeff).reshape((1, 1))

# op _00PU_power_combination_eval
# LANG: _00PP, _00PT --> _00PV
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01416__00PV = (v01415__00PP**1)*(v01418__00PT**1)
v01416__00PV = (v01416__00PV*_00PU_coeff).reshape((1, 1))

# op _00_H_linear_combination_eval
# LANG: _00_E, _00_G --> _00_I
# SHAPES: (1, 27, 3), (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01748__00_I = _00_H_constant+1*v01747__00_E+1*v01755__00_G

# op _00y2_power_combination_eval
# LANG: _00xX --> _00y3
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0865__00y3 = (v0861__00xX**2)
v0865__00y3 = (v0865__00y3*_00y2_coeff).reshape((1, 1))

# op _00ye_power_combination_eval
# LANG: _00y9, _00yd --> _00yf
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0870__00yf = (v0869__00y9**1)*(v0872__00yd**1)
v0870__00yf = (v0870__00yf*_00ye_coeff).reshape((1, 1))

# op _0114_power_combination_eval
# LANG: _010Z --> _0115
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01795__0115 = (v01791__010Z**2)
v01795__0115 = (v01795__0115*_0114_coeff).reshape((1, 1))

# op _011g_power_combination_eval
# LANG: _011b, _011f --> _011h
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01800__011h = (v01799__011b**1)*(v01802__011f**1)
v01800__011h = (v01800__011h*_011g_coeff).reshape((1, 1))

# op _013__power_combination_eval
# LANG: _013E --> _0140
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01887__0140 = (v01886__013E**3.68)
v01887__0140 = (v01887__0140*_013__coeff).reshape((1, 27))

# op _0141_power_combination_eval
# LANG: Ab --> _0142
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01889__0142 = (v01876_Ab**0.9)
v01889__0142 = (v01889__0142*_0141_coeff).reshape((1, 27))

# op _0145_power_combination_eval
# LANG: sigma, _013H --> _0146
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01892__0146 = (v01891__013H**1)*(v01877_sigma**-1)
v01892__0146 = (v01892__0146*_0145_coeff).reshape((1, 27))

# op _014h_power_combination_eval
# LANG: _013E --> _014i
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01904__014i = (v01886__013E**7.44)
v01904__014i = (v01904__014i*_014h_coeff).reshape((1, 27))

# op _014j_power_combination_eval
# LANG: Ab --> _014k
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01906__014k = (v01876_Ab**0.9)
v01906__014k = (v01906__014k*_014j_coeff).reshape((1, 27))

# op _014n_power_combination_eval
# LANG: sigma, _013H --> _014o
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01908__014o = (v01891__013H**1)*(v01877_sigma**-1)
v01908__014o = (v01908__014o*_014n_coeff).reshape((1, 27))

# op _015a_arcsin_eval
# LANG: _0159 --> _015b
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01923__015b = np.arcsin(v01921__0159)

# op _00J3_power_combination_eval
# LANG: _00J2 --> _00J4
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01210__00J4 = (v01202__00J2**1)
v01210__00J4 = (v01210__00J4*_00J3_coeff).reshape((1, 27, 3))

# op _00KD_power_combination_eval
# LANG: _00KC --> _00KE
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01257__00KE = (v01254__00KC**0.5)
v01257__00KE = (v01257__00KE*_00KD_coeff).reshape((1, 1))

# op _00KH_power_combination_eval
# LANG: _00Kj --> _00KI
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01259__00KI = (v01245__00Kj**2)
v01259__00KI = (v01259__00KI*_00KH_coeff).reshape((1, 1))

# op _00Kr_linear_combination_eval
# LANG: _00Kq --> _00Ks
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01250__00Ks = _00Kr_constant+1*v01249__00Kq

# op _00NG_power_combination_eval
# LANG: _00ND, _00NF --> _00NH
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01359__00NH = (v01358__00ND**1)*(v01360__00NF**1)
v01359__00NH = (v01359__00NH*_00NG_coeff).reshape((1, 27))

# op _00NK_power_combination_eval
# LANG: _00NJ --> _00NL
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01363__00NL = (v01362__00NJ**1.6)
v01363__00NL = (v01363__00NL*_00NK_coeff).reshape((1, 27))

# op _00NU_linear_combination_eval
# LANG: Ab --> _00NV
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01352__00NV = _00NU_constant+-1*v01330_Ab

# op _00No_power_combination_eval
# LANG: _00Nl, _00Nn --> _00Np
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01342__00Np = (v01341__00Nl**1)*(v01343__00Nn**1)
v01342__00Np = (v01342__00Np*_00No_coeff).reshape((1, 27))

# op _00Ns_power_combination_eval
# LANG: _00Nr --> _00Nt
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01347__00Nt = (v01346__00Nr**1.6)
v01347__00Nt = (v01347__00Nt*_00Ns_coeff).reshape((1, 27))

# op _00O5_linear_combination_eval
# LANG: Ab --> _00O6
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01368__00O6 = _00O5_constant+1*v01330_Ab

# op _00Ox reshape_eval
# LANG: _00Ow --> _00Oy
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01378__00Oy = v01377__00Ow.reshape((1, 27))

# op _00PK_linear_combination_eval
# LANG: _00PJ --> _00PL
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01412__00PL = _00PK_constant+1*v01411__00PJ

# op _00PW_power_combination_eval
# LANG: _00PV --> _00PX
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01419__00PX = (v01416__00PV**0.5)
v01419__00PX = (v01419__00PX*_00PW_coeff).reshape((1, 1))

# op _00P__power_combination_eval
# LANG: _00PC --> _00Q0
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01421__00Q0 = (v01407__00PC**2)
v01421__00Q0 = (v01421__00Q0*_00P__coeff).reshape((1, 1))

# op _00_J_power_combination_eval
# LANG: _00_I --> _00_K
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01756__00_K = (v01748__00_I**1)
v01756__00_K = (v01756__00_K*_00_J_coeff).reshape((1, 27, 3))

# op _00y4_linear_combination_eval
# LANG: _00y3 --> _00y5
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0866__00y5 = _00y4_constant+1*v0865__00y3

# op _00yg_power_combination_eval
# LANG: _00yf --> _00yh
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0873__00yh = (v0870__00yf**0.5)
v0873__00yh = (v0873__00yh*_00yg_coeff).reshape((1, 1))

# op _00yk_power_combination_eval
# LANG: _00xX --> _00yl
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0875__00yl = (v0861__00xX**2)
v0875__00yl = (v0875__00yl*_00yk_coeff).reshape((1, 1))

# op _0116_linear_combination_eval
# LANG: _0115 --> _0117
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01796__0117 = _0116_constant+1*v01795__0115

# op _011i_power_combination_eval
# LANG: _011h --> _011j
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01803__011j = (v01800__011h**0.5)
v01803__011j = (v01803__011j*_011i_coeff).reshape((1, 1))

# op _011m_power_combination_eval
# LANG: _010Z --> _011n
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01805__011n = (v01791__010Z**2)
v01805__011n = (v01805__011n*_011m_coeff).reshape((1, 1))

# op _0143_power_combination_eval
# LANG: _0140, _0142 --> _0144
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01888__0144 = (v01887__0140**1)*(v01889__0142**1)
v01888__0144 = (v01888__0144*_0143_coeff).reshape((1, 27))

# op _0147_power_combination_eval
# LANG: _0146 --> _0148
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01893__0148 = (v01892__0146**1.6)
v01893__0148 = (v01893__0148*_0147_coeff).reshape((1, 27))

# op _014L_linear_combination_eval
# LANG: Ab --> _014M
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01914__014M = _014L_constant+1*v01876_Ab

# op _014l_power_combination_eval
# LANG: _014i, _014k --> _014m
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01905__014m = (v01904__014i**1)*(v01906__014k**1)
v01905__014m = (v01905__014m*_014l_coeff).reshape((1, 27))

# op _014p_power_combination_eval
# LANG: _014o --> _014q
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01909__014q = (v01908__014o**1.6)
v01909__014q = (v01909__014q*_014p_coeff).reshape((1, 27))

# op _014z_linear_combination_eval
# LANG: Ab --> _014A
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01898__014A = _014z_constant+-1*v01876_Ab

# op _015c reshape_eval
# LANG: _015b --> _015d
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01924__015d = v01923__015b.reshape((1, 27))

# op _00J5_power_combination_eval
# LANG: _00J4 --> _00J6
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01211__00J6 = (v01210__00J4**1)
v01211__00J6 = (v01211__00J6*_00J5_coeff).reshape((1, 27, 3))

# op _00KF_power_combination_eval
# LANG: _00Ks, _00KE --> _00KG
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01251__00KG = (v01250__00Ks**1)*(v01257__00KE**1)
v01251__00KG = (v01251__00KG*_00KF_coeff).reshape((1, 1))

# op _00KJ_linear_combination_eval
# LANG: _00KI --> _00KK
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01260__00KK = _00KJ_constant+1*v01259__00KI

# op _00Kl_power_combination_eval
# LANG: _00Kj --> _00Km
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01246__00Km = (v01245__00Kj**4)
v01246__00Km = (v01246__00Km*_00Kl_coeff).reshape((1, 1))

# op _00NM_power_combination_eval
# LANG: _00NH, _00NL --> _00NN
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01361__00NN = (v01359__00NH**1)*(v01363__00NL**1)
v01361__00NN = (v01361__00NN*_00NM_coeff).reshape((1, 27))

# op _00NW_power_combination_eval
# LANG: _00NV --> _00NX
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01353__00NX = (v01352__00NV**1)
v01353__00NX = (v01353__00NX*_00NW_coeff).reshape((1, 27))

# op _00Nu_power_combination_eval
# LANG: _00Np, _00Nt --> _00Nv
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01344__00Nv = (v01342__00Np**1)*(v01347__00Nt**1)
v01344__00Nv = (v01344__00Nv*_00Nu_coeff).reshape((1, 27))

# op _00O7_power_combination_eval
# LANG: _00O6 --> _00O8
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01369__00O8 = (v01368__00O6**1)
v01369__00O8 = (v01369__00O8*_00O7_coeff).reshape((1, 27))

# op _00ON_power_combination_eval
# LANG: _00Oy --> _00OO
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01389__00OO = (v01378__00Oy**2)
v01389__00OO = (v01389__00OO*_00ON_coeff).reshape((1, 27))

# op _00PE_power_combination_eval
# LANG: _00PC --> _00PF
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01408__00PF = (v01407__00PC**4)
v01408__00PF = (v01408__00PF*_00PE_coeff).reshape((1, 1))

# op _00PY_power_combination_eval
# LANG: _00PL, _00PX --> _00PZ
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01413__00PZ = (v01412__00PL**1)*(v01419__00PX**1)
v01413__00PZ = (v01413__00PZ*_00PY_coeff).reshape((1, 1))

# op _00Q1_linear_combination_eval
# LANG: _00Q0 --> _00Q2
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01422__00Q2 = _00Q1_constant+1*v01421__00Q0

# op _00_L_power_combination_eval
# LANG: _00_K --> _00_M
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01757__00_M = (v01756__00_K**1)
v01757__00_M = (v01757__00_M*_00_L_coeff).reshape((1, 27, 3))

# op _00xZ_power_combination_eval
# LANG: _00xX --> _00x_
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0862__00x_ = (v0861__00xX**4)
v0862__00x_ = (v0862__00x_*_00xZ_coeff).reshape((1, 1))

# op _00yi_power_combination_eval
# LANG: _00y5, _00yh --> _00yj
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0867__00yj = (v0866__00y5**1)*(v0873__00yh**1)
v0867__00yj = (v0867__00yj*_00yi_coeff).reshape((1, 1))

# op _00ym_linear_combination_eval
# LANG: _00yl --> _00yn
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0876__00yn = _00ym_constant+1*v0875__00yl

# op _0110_power_combination_eval
# LANG: _010Z --> _0111
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01792__0111 = (v01791__010Z**4)
v01792__0111 = (v01792__0111*_0110_coeff).reshape((1, 1))

# op _011k_power_combination_eval
# LANG: _0117, _011j --> _011l
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01797__011l = (v01796__0117**1)*(v01803__011j**1)
v01797__011l = (v01797__011l*_011k_coeff).reshape((1, 1))

# op _011o_linear_combination_eval
# LANG: _011n --> _011p
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01806__011p = _011o_constant+1*v01805__011n

# op _0149_power_combination_eval
# LANG: _0144, _0148 --> _014a
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01890__014a = (v01888__0144**1)*(v01893__0148**1)
v01890__014a = (v01890__014a*_0149_coeff).reshape((1, 27))

# op _014B_power_combination_eval
# LANG: _014A --> _014C
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01899__014C = (v01898__014A**1)
v01899__014C = (v01899__014C*_014B_coeff).reshape((1, 27))

# op _014N_power_combination_eval
# LANG: _014M --> _014O
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01915__014O = (v01914__014M**1)
v01915__014O = (v01915__014O*_014N_coeff).reshape((1, 27))

# op _014r_power_combination_eval
# LANG: _014m, _014q --> _014s
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01907__014s = (v01905__014m**1)*(v01909__014q**1)
v01907__014s = (v01907__014s*_014r_coeff).reshape((1, 27))

# op _015s_power_combination_eval
# LANG: _015d --> _015t
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01935__015t = (v01924__015d**2)
v01935__015t = (v01935__015t*_015s_coeff).reshape((1, 27))

# op _00J7_log10_eval
# LANG: _00J6 --> _00J8
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01212__00J8 = np.log10(v01211__00J6)

# op _00KL_power_combination_eval
# LANG: _00KG, _00KK --> _00KM
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01258__00KM = (v01251__00KG**1)*(v01260__00KK**1)
v01258__00KM = (v01258__00KM*_00KL_coeff).reshape((1, 1))

# op _00Kn_power_combination_eval
# LANG: _00Km --> _00Ko
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01247__00Ko = (v01246__00Km**1)
v01247__00Ko = (v01247__00Ko*_00Kn_coeff).reshape((1, 1))

# op _00NO_log10_eval
# LANG: _00NN --> _00NP
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01364__00NP = np.log10(v01361__00NN)

# op _00NY_tanh_eval
# LANG: _00NX --> _00NZ
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01354__00NZ = np.tanh(v01353__00NX)

# op _00Nw_log10_eval
# LANG: _00Nv --> _00Nx
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01348__00Nx = np.log10(v01344__00Nv)

# op _00O9_tanh_eval
# LANG: _00O8 --> _00Oa
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01370__00Oa = np.tanh(v01369__00O8)

# op _00OP_power_combination_eval
# LANG: _00OO --> _00OQ
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01390__00OQ = (v01389__00OO**0.5)
v01390__00OQ = (v01390__00OQ*_00OP_coeff).reshape((1, 27))

# op _00PG_power_combination_eval
# LANG: _00PF --> _00PH
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01409__00PH = (v01408__00PF**1)
v01409__00PH = (v01409__00PH*_00PG_coeff).reshape((1, 1))

# op _00Q3_power_combination_eval
# LANG: _00PZ, _00Q2 --> _00Q4
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01420__00Q4 = (v01413__00PZ**1)*(v01422__00Q2**1)
v01420__00Q4 = (v01420__00Q4*_00Q3_coeff).reshape((1, 1))

# op _00_N_log10_eval
# LANG: _00_M --> _00_O
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01758__00_O = np.log10(v01757__00_M)

# op _00y0_power_combination_eval
# LANG: _00x_ --> _00y1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0863__00y1 = (v0862__00x_**1)
v0863__00y1 = (v0863__00y1*_00y0_coeff).reshape((1, 1))

# op _00yo_power_combination_eval
# LANG: _00yj, _00yn --> _00yp
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0874__00yp = (v0867__00yj**1)*(v0876__00yn**1)
v0874__00yp = (v0874__00yp*_00yo_coeff).reshape((1, 1))

# op _0112_power_combination_eval
# LANG: _0111 --> _0113
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01793__0113 = (v01792__0111**1)
v01793__0113 = (v01793__0113*_0112_coeff).reshape((1, 1))

# op _011q_power_combination_eval
# LANG: _011l, _011p --> _011r
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01804__011r = (v01797__011l**1)*(v01806__011p**1)
v01804__011r = (v01804__011r*_011q_coeff).reshape((1, 1))

# op _014D_tanh_eval
# LANG: _014C --> _014E
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01900__014E = np.tanh(v01899__014C)

# op _014P_tanh_eval
# LANG: _014O --> _014Q
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01916__014Q = np.tanh(v01915__014O)

# op _014b_log10_eval
# LANG: _014a --> _014c
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01894__014c = np.log10(v01890__014a)

# op _014t_log10_eval
# LANG: _014s --> _014u
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01910__014u = np.log10(v01907__014s)

# op _015u_power_combination_eval
# LANG: _015t --> _015v
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01936__015v = (v01935__015t**0.5)
v01936__015v = (v01936__015v*_015u_coeff).reshape((1, 27))

# op _00J9_power_combination_eval
# LANG: _00J8 --> _00Ja
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01213__00Ja = (v01212__00J8**1)
v01213__00Ja = (v01213__00Ja*_00J9_coeff).reshape((1, 27, 3))

# op _00KN_power_combination_eval
# LANG: _00Ko, _00KM --> _00KO
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01248__00KO = (v01247__00Ko**1)*(v01258__00KM**-1)
v01248__00KO = (v01248__00KO*_00KN_coeff).reshape((1, 1))

# op _00NQ_power_combination_eval
# LANG: _00NP --> _00NR
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01365__00NR = (v01364__00NP**1)
v01365__00NR = (v01365__00NR*_00NQ_coeff).reshape((1, 27))

# op _00N__power_combination_eval
# LANG: _00NZ --> _00O0
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01355__00O0 = (v01354__00NZ**1)
v01355__00O0 = (v01355__00O0*_00N__coeff).reshape((1, 27))

# op _00Ny_power_combination_eval
# LANG: _00Nx --> _00Nz
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01349__00Nz = (v01348__00Nx**1)
v01349__00Nz = (v01349__00Nz*_00Ny_coeff).reshape((1, 27))

# op _00OR_sin_eval
# LANG: _00OQ --> _00OS
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01391__00OS = np.sin(v01390__00OQ)

# op _00Ob_power_combination_eval
# LANG: _00Oa --> _00Oc
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01371__00Oc = (v01370__00Oa**1)
v01371__00Oc = (v01371__00Oc*_00Ob_coeff).reshape((1, 27))

# op _00Oj_power_combination_eval
# LANG: propeller_radius --> _00Ok
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01385__00Ok = (v01236_propeller_radius**1)
v01385__00Ok = (v01385__00Ok*_00Oj_coeff).reshape((1,))

# op _00Oz_power_combination_eval
# LANG: _00Oy --> _00OA
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01379__00OA = (v01378__00Oy**2.0)
v01379__00OA = (v01379__00OA*_00Oz_coeff).reshape((1, 27))

# op _00Q5_power_combination_eval
# LANG: _00PH, _00Q4 --> _00Q6
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01410__00Q6 = (v01409__00PH**1)*(v01420__00Q4**-1)
v01410__00Q6 = (v01410__00Q6*_00Q5_coeff).reshape((1, 1))

# op _00_P_power_combination_eval
# LANG: _00_O --> _00_Q
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01759__00_Q = (v01758__00_O**1)
v01759__00_Q = (v01759__00_Q*_00_P_coeff).reshape((1, 27, 3))

# op _00yq_power_combination_eval
# LANG: _00y1, _00yp --> _00yr
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0864__00yr = (v0863__00y1**1)*(v0874__00yp**-1)
v0864__00yr = (v0864__00yr*_00yq_coeff).reshape((1, 1))

# op _011s_power_combination_eval
# LANG: _0113, _011r --> _011t
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01794__011t = (v01793__0113**1)*(v01804__011r**-1)
v01794__011t = (v01794__011t*_011s_coeff).reshape((1, 1))

# op _014F_power_combination_eval
# LANG: _014E --> _014G
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01901__014G = (v01900__014E**1)
v01901__014G = (v01901__014G*_014F_coeff).reshape((1, 27))

# op _014R_power_combination_eval
# LANG: _014Q --> _014S
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01917__014S = (v01916__014Q**1)
v01917__014S = (v01917__014S*_014R_coeff).reshape((1, 27))

# op _014Z_power_combination_eval
# LANG: propeller_radius --> _014_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01931__014_ = (v01782_propeller_radius**1)
v01931__014_ = (v01931__014_*_014Z_coeff).reshape((1,))

# op _014d_power_combination_eval
# LANG: _014c --> _014e
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01895__014e = (v01894__014c**1)
v01895__014e = (v01895__014e*_014d_coeff).reshape((1, 27))

# op _014v_power_combination_eval
# LANG: _014u --> _014w
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01911__014w = (v01910__014u**1)
v01911__014w = (v01911__014w*_014v_coeff).reshape((1, 27))

# op _015e_power_combination_eval
# LANG: _015d --> _015f
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01925__015f = (v01924__015d**2.0)
v01925__015f = (v01925__015f*_015e_coeff).reshape((1, 27))

# op _015w_sin_eval
# LANG: _015v --> _015x
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01937__015x = np.sin(v01936__015v)

# op _00Jb_power_combination_eval
# LANG: _00Ja --> _00Jc
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01214__00Jc = (v01213__00Ja**1)
v01214__00Jc = (v01214__00Jc*_00Jb_coeff).reshape((1, 27, 3))

# op _00KP_log10_eval
# LANG: _00KO --> _00KQ
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01261__00KQ = np.log10(v01248__00KO)

# op _00KT_log10_eval
# LANG: RA_1000 --> _00KU
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01265__00KU = np.log10(v01264_RA_1000)

# op _00NA_linear_combination_eval
# LANG: _00Nz --> _00NB
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01350__00NB = _00NA_constant+1*v01349__00Nz

# op _00NS_linear_combination_eval
# LANG: _00NR --> _00NT
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01366__00NT = _00NS_constant+1*v01365__00NR

# op _00O1_linear_combination_eval
# LANG: _00O0 --> _00O2
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01356__00O2 = _00O1_constant+1*v01355__00O0

# op _00OB_power_combination_eval
# LANG: _00OA --> _00OC
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01380__00OC = (v01379__00OA**0.5)
v01380__00OC = (v01380__00OC*_00OB_coeff).reshape((1, 27))

# op _00OT_linear_combination_eval
# LANG: _00OS --> _00OU
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01392__00OU = _00OT_constant+-1*v01391__00OS

# op _00Od_linear_combination_eval
# LANG: _00Oc --> _00Oe
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01372__00Oe = _00Od_constant+1*v01371__00Oc

# op _00Ol expand_scalar_eval
# LANG: _00Ok --> _00Om
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01386__00Om = np.empty((1, 27))
v01386__00Om.fill(v01385__00Ok.item())

# op _00Q7_log10_eval
# LANG: _00Q6 --> _00Q8
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01423__00Q8 = np.log10(v01410__00Q6)

# op _00Qb_log10_eval
# LANG: RA_1000 --> _00Qc
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01427__00Qc = np.log10(v01426_RA_1000)

# op _00_R_power_combination_eval
# LANG: _00_Q --> _00_S
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01760__00_S = (v01759__00_Q**1)
v01760__00_S = (v01760__00_S*_00_R_coeff).reshape((1, 27, 3))

# op _00ys_log10_eval
# LANG: _00yr --> _00yt
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0877__00yt = np.log10(v0864__00yr)

# op _00yw_log10_eval
# LANG: RA_1000 --> _00yx
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0881__00yx = np.log10(v0880_RA_1000)

# op _011u_log10_eval
# LANG: _011t --> _011v
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01807__011v = np.log10(v01794__011t)

# op _011y_log10_eval
# LANG: RA_1000 --> _011z
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01811__011z = np.log10(v01810_RA_1000)

# op _014H_linear_combination_eval
# LANG: _014G --> _014I
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01902__014I = _014H_constant+1*v01901__014G

# op _014T_linear_combination_eval
# LANG: _014S --> _014U
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01918__014U = _014T_constant+1*v01917__014S

# op _014f_linear_combination_eval
# LANG: _014e --> _014g
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01896__014g = _014f_constant+1*v01895__014e

# op _014x_linear_combination_eval
# LANG: _014w --> _014y
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01912__014y = _014x_constant+1*v01911__014w

# op _0150 expand_scalar_eval
# LANG: _014_ --> _0151
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01932__0151 = np.empty((1, 27))
v01932__0151.fill(v01931__014_.item())

# op _015g_power_combination_eval
# LANG: _015f --> _015h
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01926__015h = (v01925__015f**0.5)
v01926__015h = (v01926__015h*_015g_coeff).reshape((1, 27))

# op _015y_linear_combination_eval
# LANG: _015x --> _015z
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01938__015z = _015y_constant+-1*v01937__015x

# op _00Jd_exp_a_eval
# LANG: _00Jc --> _00Je
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01215__00Je = _00Jd_exp_a_eval_a**v01214__00Jc

# op _00KR_power_combination_eval
# LANG: _00KQ --> _00KS
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01262__00KS = (v01261__00KQ**1)
v01262__00KS = (v01262__00KS*_00KR_coeff).reshape((1, 1))

# op _00KV_power_combination_eval
# LANG: _00KU --> _00KW
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01266__00KW = (v01265__00KU**1)
v01266__00KW = (v01266__00KW*_00KV_coeff).reshape((1, 1))

# op _00O3_power_combination_eval
# LANG: _00NB, _00O2 --> _00O4
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01351__00O4 = (v01350__00NB**1)*(v01356__00O2**1)
v01351__00O4 = (v01351__00O4*_00O3_coeff).reshape((1, 27))

# op _00OD_sin_eval
# LANG: _00OC --> _00OE
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01381__00OE = np.sin(v01380__00OC)

# op _00OJ_power_combination_eval
# LANG: _00Op, _00Om --> _00OK
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01384__00OK = (v01376__00Op**1)*(v01386__00Om**-1)
v01384__00OK = (v01384__00OK*_00OJ_coeff).reshape((1, 27))

# op _00OV_power_combination_eval
# LANG: _00OU --> _00OW
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01393__00OW = (v01392__00OU**1)
v01393__00OW = (v01393__00OW*_00OV_coeff).reshape((1, 27))

# op _00Of_power_combination_eval
# LANG: _00NT, _00Oe --> _00Og
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01367__00Og = (v01366__00NT**1)*(v01372__00Oe**1)
v01367__00Og = (v01367__00Og*_00Of_coeff).reshape((1, 27))

# op _00Q9_power_combination_eval
# LANG: _00Q8 --> _00Qa
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01424__00Qa = (v01423__00Q8**1)
v01424__00Qa = (v01424__00Qa*_00Q9_coeff).reshape((1, 1))

# op _00Qd_power_combination_eval
# LANG: _00Qc --> _00Qe
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01428__00Qe = (v01427__00Qc**1)
v01428__00Qe = (v01428__00Qe*_00Qd_coeff).reshape((1, 1))

# op _00_T_exp_a_eval
# LANG: _00_S --> _00_U
# SHAPES: (1, 27, 3) --> (1, 27, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01761__00_U = _00_T_exp_a_eval_a**v01760__00_S

# op _00yu_power_combination_eval
# LANG: _00yt --> _00yv
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0878__00yv = (v0877__00yt**1)
v0878__00yv = (v0878__00yv*_00yu_coeff).reshape((1, 1))

# op _00yy_power_combination_eval
# LANG: _00yx --> _00yz
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0882__00yz = (v0881__00yx**1)
v0882__00yz = (v0882__00yz*_00yy_coeff).reshape((1, 1))

# op _011A_power_combination_eval
# LANG: _011z --> _011B
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01812__011B = (v01811__011z**1)
v01812__011B = (v01812__011B*_011A_coeff).reshape((1, 1))

# op _011w_power_combination_eval
# LANG: _011v --> _011x
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01808__011x = (v01807__011v**1)
v01808__011x = (v01808__011x*_011w_coeff).reshape((1, 1))

# op _014J_power_combination_eval
# LANG: _014g, _014I --> _014K
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01897__014K = (v01896__014g**1)*(v01902__014I**1)
v01897__014K = (v01897__014K*_014J_coeff).reshape((1, 27))

# op _014V_power_combination_eval
# LANG: _014y, _014U --> _014W
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01913__014W = (v01912__014y**1)*(v01918__014U**1)
v01913__014W = (v01913__014W*_014V_coeff).reshape((1, 27))

# op _015A_power_combination_eval
# LANG: _015z --> _015B
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01939__015B = (v01938__015z**1)
v01939__015B = (v01939__015B*_015A_coeff).reshape((1, 27))

# op _015i_sin_eval
# LANG: _015h --> _015j
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01927__015j = np.sin(v01926__015h)

# op _015o_power_combination_eval
# LANG: _0154, _0151 --> _015p
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01930__015p = (v01922__0154**1)*(v01932__0151**-1)
v01930__015p = (v01930__015p*_015o_coeff).reshape((1, 27))

# op _00Jf_single_tensor_sum_with_axis_eval
# LANG: _00Je --> _00Jg
# SHAPES: (1, 27, 3) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01216__00Jg = np.sum(v01215__00Je, axis = (2,)).reshape((1, 27))

# op _00KX_linear_combination_eval
# LANG: _00KS, _00KW --> _00KY
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01263__00KY = _00KX_constant+1*v01262__00KS+-1*v01266__00KW

# op _00OF_power_combination_eval
# LANG: _00OE --> _00OG
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01382__00OG = (v01381__00OE**0.031)
v01382__00OG = (v01382__00OG*_00OF_coeff).reshape((1, 27))

# op _00OL_log10_eval
# LANG: _00OK --> _00OM
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01387__00OM = np.log10(v01384__00OK)

# op _00OX_linear_combination_eval
# LANG: _00OW --> _00OY
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01394__00OY = _00OX_constant+1*v01393__00OW

# op _00Oh_linear_combination_eval
# LANG: _00O4, _00Og --> _00Oi
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01357__00Oi = _00Oh_constant+1*v01351__00O4+1*v01367__00Og

# op _00Qf_linear_combination_eval
# LANG: _00Qa, _00Qe --> _00Qg
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01425__00Qg = _00Qf_constant+1*v01424__00Qa+-1*v01428__00Qe

# op _00_V_single_tensor_sum_with_axis_eval
# LANG: _00_U --> _00_W
# SHAPES: (1, 27, 3) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01762__00_W = np.sum(v01761__00_U, axis = (2,)).reshape((1, 27))

# op _00yA_linear_combination_eval
# LANG: _00yv, _00yz --> _00yB
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0879__00yB = _00yA_constant+1*v0878__00yv+-1*v0882__00yz

# op _011C_linear_combination_eval
# LANG: _011x, _011B --> _011D
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01809__011D = _011C_constant+1*v01808__011x+-1*v01812__011B

# op _014X_linear_combination_eval
# LANG: _014K, _014W --> _014Y
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01903__014Y = _014X_constant+1*v01897__014K+1*v01913__014W

# op _015C_linear_combination_eval
# LANG: _015B --> _015D
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01940__015D = _015C_constant+1*v01939__015B

# op _015k_power_combination_eval
# LANG: _015j --> _015l
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01928__015l = (v01927__015j**0.031)
v01928__015l = (v01928__015l*_015k_coeff).reshape((1, 27))

# op _015q_log10_eval
# LANG: _015p --> _015r
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01933__015r = np.log10(v01930__015p)

# op _00Jh_log10_eval
# LANG: _00Jg --> _00Ji
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01217__00Ji = np.log10(v01216__00Jg)

# op _00KZ reshape_eval
# LANG: _00KY --> _00K_
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01267__00K_ = v01263__00KY.reshape((1,))

# op _00OH_power_combination_eval
# LANG: _00Oi, _00OG --> _00OI
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01373__00OI = (v01357__00Oi**1)*(v01382__00OG**1)
v01373__00OI = (v01373__00OI*_00OH_coeff).reshape((1, 27))

# op _00OZ_power_combination_eval
# LANG: _00OM, _00OY --> _00O_
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01388__00O_ = (v01387__00OM**1)*(v01394__00OY**1)
v01388__00O_ = (v01388__00O_*_00OZ_coeff).reshape((1, 27))

# op _00Qh reshape_eval
# LANG: _00Qg --> _00Qi
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01429__00Qi = v01425__00Qg.reshape((1,))

# op _00_X_log10_eval
# LANG: _00_W --> _00_Y
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01763__00_Y = np.log10(v01762__00_W)

# op _00dZ_power_combination_eval
# LANG: _radius --> _00d_
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0342__00d_ = (v0214__radius**2)
v0342__00d_ = (v0342__00d_*_00dZ_coeff).reshape((1, 40, 30))

# op _00t1_power_combination_eval
# LANG: _radius --> _00t2
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0715__00t2 = (v0587__radius**2)
v0715__00t2 = (v0715__00t2*_00t1_coeff).reshape((1, 40, 30))

# op _00yC reshape_eval
# LANG: _00yB --> _00yD
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0883__00yD = v0879__00yB.reshape((1,))

# op _011E reshape_eval
# LANG: _011D --> _011F
# SHAPES: (1, 1) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01813__011F = v01809__011D.reshape((1,))

# op _015E_power_combination_eval
# LANG: _015r, _015D --> _015F
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01934__015F = (v01933__015r**1)*(v01940__015D**1)
v01934__015F = (v01934__015F*_015E_coeff).reshape((1, 27))

# op _015m_power_combination_eval
# LANG: _014Y, _015l --> _015n
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01919__015n = (v01903__014Y**1)*(v01928__015l**1)
v01919__015n = (v01919__015n*_015m_coeff).reshape((1, 27))

# op _00Jj_power_combination_eval
# LANG: _00Ji --> rotor_1_disk_tonal_spl
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.ks_spl_model
v01218_rotor_1_disk_tonal_spl = (v01217__00Ji**1)
v01218_rotor_1_disk_tonal_spl = (v01218_rotor_1_disk_tonal_spl*_00Jj_coeff).reshape((1, 27))

# op _00L0 expand_scalar_eval
# LANG: _00K_ --> _00L1
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01268__00L1 = np.empty((1, 27))
v01268__00L1.fill(v01267__00K_.item())

# op _00P0_linear_combination_eval
# LANG: _00OI, _00O_ --> rotor_1_disk_broadband_spl
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.gl_spl_model
v01383_rotor_1_disk_broadband_spl = _00P0_constant+1*v01373__00OI+-1*v01388__00O_

# op _00Qj expand_scalar_eval
# LANG: _00Qi --> _00Qk
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01430__00Qk = np.empty((1, 27))
v01430__00Qk.fill(v01429__00Qi.item())

# op _00_Z_power_combination_eval
# LANG: _00_Y --> rotor_2_disk_tonal_spl
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.ks_spl_model
v01764_rotor_2_disk_tonal_spl = (v01763__00_Y**1)
v01764_rotor_2_disk_tonal_spl = (v01764_rotor_2_disk_tonal_spl*_00_Z_coeff).reshape((1, 27))

# op _00e0_power_combination_eval
# LANG: _00d_ --> _00e1
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0343__00e1 = (v0342__00d_**1)
v0343__00e1 = (v0343__00e1*_00e0_coeff).reshape((1, 40, 30))

# op _00t3_power_combination_eval
# LANG: _00t2 --> _00t4
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0716__00t4 = (v0715__00t2**1)
v0716__00t4 = (v0716__00t4*_00t3_coeff).reshape((1, 40, 30))

# op _00yE expand_scalar_eval
# LANG: _00yD --> _00yF
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0884__00yF = np.empty((1, 27))
v0884__00yF.fill(v0883__00yD.item())

# op _011G expand_scalar_eval
# LANG: _011F --> _011H
# SHAPES: (1,) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01814__011H = np.empty((1, 27))
v01814__011H.fill(v01813__011F.item())

# op _015G_linear_combination_eval
# LANG: _015n, _015F --> rotor_2_disk_broadband_spl
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.gl_spl_model
v01929_rotor_2_disk_broadband_spl = _015G_constant+1*v01919__015n+-1*v01934__015F

# op _00L2_linear_combination_eval
# LANG: _00L1, rotor_1_disk_broadband_spl --> _00L3
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01242__00L3 = _00L2_constant+1*v01383_rotor_1_disk_broadband_spl+1*v01268__00L1

# op _00Ql_linear_combination_eval
# LANG: _00Qk, rotor_2_disk_tonal_spl --> _00Qm
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01404__00Qm = _00Ql_constant+1*v01764_rotor_2_disk_tonal_spl+1*v01430__00Qk

# op _00e2_power_combination_eval
# LANG: _00bU, _00e1 --> _00e3
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0344__00e3 = (v0343__00e1**1)*(v0320__00bU**1)
v0344__00e3 = (v0344__00e3*_00e2_coeff).reshape((1, 40, 30))

# op _00t5_power_combination_eval
# LANG: _00qX, _00t4 --> _00t6
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0717__00t6 = (v0716__00t4**1)*(v0693__00qX**1)
v0717__00t6 = (v0717__00t6*_00t5_coeff).reshape((1, 40, 30))

# op _00yG_linear_combination_eval
# LANG: _00yF, rotor_1_disk_tonal_spl --> _00yH
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0858__00yH = _00yG_constant+1*v01218_rotor_1_disk_tonal_spl+1*v0884__00yF

# op _011I_linear_combination_eval
# LANG: _011H, rotor_2_disk_broadband_spl --> _011J
# SHAPES: (1, 27), (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01788__011J = _011I_constant+1*v01929_rotor_2_disk_broadband_spl+1*v01814__011H

# op _00L4_power_combination_eval
# LANG: _00L3 --> _00L5
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01269__00L5 = (v01242__00L3**1)
v01269__00L5 = (v01269__00L5*_00L4_coeff).reshape((1, 27))

# op _00Qn_power_combination_eval
# LANG: _00Qm --> _00Qo
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01431__00Qo = (v01404__00Qm**1)
v01431__00Qo = (v01431__00Qo*_00Qn_coeff).reshape((1, 27))

# op _00e4_power_combination_eval
# LANG: _ux, _00e3 --> _00e5
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0345__00e5 = (v0344__00e3**1)*(v0279__ux**1)
v0345__00e5 = (v0345__00e5*_00e4_coeff).reshape((1, 40, 30))

# op _00t7_power_combination_eval
# LANG: _ux, _00t6 --> _00t8
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0718__00t8 = (v0717__00t6**1)*(v0652__ux**1)
v0718__00t8 = (v0718__00t8*_00t7_coeff).reshape((1, 40, 30))

# op _00yI_power_combination_eval
# LANG: _00yH --> _00yJ
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0885__00yJ = (v0858__00yH**1)
v0885__00yJ = (v0885__00yJ*_00yI_coeff).reshape((1, 27))

# op _011K_power_combination_eval
# LANG: _011J --> _011L
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01815__011L = (v01788__011J**1)
v01815__011L = (v01815__011L*_011K_coeff).reshape((1, 27))

# op _00L6_exp_a_eval
# LANG: _00L5 --> _00L7
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01270__00L7 = _00L6_exp_a_eval_a**v01269__00L5

# op _00Qp_exp_a_eval
# LANG: _00Qo --> _00Qq
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01432__00Qq = _00Qp_exp_a_eval_a**v01431__00Qo

# op _00e6_power_combination_eval
# LANG: _ut, _00e5 --> _00e7
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0346__00e7 = (v0345__00e5**1)*(v0311__ut**1)
v0346__00e7 = (v0346__00e7*_00e6_coeff).reshape((1, 40, 30))

# op _00eG_power_combination_eval
# LANG: _ut --> _00eH
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0414__00eH = (v0311__ut**1)
v0414__00eH = (v0414__00eH*_00eG_coeff).reshape((1, 40, 30))

# op _00t9_power_combination_eval
# LANG: _ut, _00t8 --> _00ta
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0719__00ta = (v0718__00t8**1)*(v0684__ut**1)
v0719__00ta = (v0719__00ta*_00t9_coeff).reshape((1, 40, 30))

# op _00tJ_power_combination_eval
# LANG: _ut --> _00tK
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0787__00tK = (v0684__ut**1)
v0787__00tK = (v0787__00tK*_00tJ_coeff).reshape((1, 40, 30))

# op _00yK_exp_a_eval
# LANG: _00yJ --> _00yL
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0886__00yL = _00yK_exp_a_eval_a**v0885__00yJ

# op _011M_exp_a_eval
# LANG: _011L --> _011N
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01816__011N = _011M_exp_a_eval_a**v01815__011L

# op _001C_power_combination_eval
# LANG: hover_altitude --> _001D
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v082__001D = (v046_hover_altitude**4)
v082__001D = (v082__001D*_001C_coeff).reshape((1,))

# op _001O_power_combination_eval
# LANG: hover_altitude --> _001P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v084__001P = (v046_hover_altitude**3)
v084__001P = (v084__001P*_001O_coeff).reshape((1,))

# op _001__power_combination_eval
# LANG: hover_altitude --> _0020
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v086__0020 = (v046_hover_altitude**2)
v086__0020 = (v086__0020*_001__coeff).reshape((1,))

# op _001d_power_combination_eval
# LANG: hover_altitude --> _001e
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v077__001e = (v046_hover_altitude**6)
v077__001e = (v077__001e*_001d_coeff).reshape((1,))

# op _001q_power_combination_eval
# LANG: hover_altitude --> _001r
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v080__001r = (v046_hover_altitude**5)
v080__001r = (v080__001r*_001q_coeff).reshape((1,))

# op _002b_power_combination_eval
# LANG: hover_altitude --> _002c
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v088__002c = (v046_hover_altitude**1)
v088__002c = (v088__002c*_002b_coeff).reshape((1,))

# op _002n_power_combination_eval
# LANG: hover_altitude --> _002o
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v090__002o = (v046_hover_altitude**0)
v090__002o = (v090__002o*_002n_coeff).reshape((1,))

# op _00L8_log10_eval
# LANG: _00L7 --> _00L9
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01271__00L9 = np.log10(v01270__00L7)

# op _00Qr_log10_eval
# LANG: _00Qq --> _00Qs
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01433__00Qs = np.log10(v01432__00Qq)

# op _00e8_power_combination_eval
# LANG: _00e7, prandtl_loss_factor --> _00e9
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0347__00e9 = (v0346__00e7**1)*(v0264_prandtl_loss_factor**1)
v0347__00e9 = (v0347__00e9*_00e8_coeff).reshape((1, 40, 30))

# op _00eI_linear_combination_eval
# LANG: _00eH, _tangential_inflow_velocity --> _00eJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0413__00eJ = _00eI_constant+1*v0231__tangential_inflow_velocity+-1*v0414__00eH

# op _00ek_power_combination_eval
# LANG: _ut --> _00el
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0367__00el = (v0311__ut**1)
v0367__00el = (v0367__00el*_00ek_coeff).reshape((1, 40, 30))

# op _00ey_power_combination_eval
# LANG: _00ch --> _00ez
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0407__00ez = (v0289__00ch**1)
v0407__00ez = (v0407__00ez*_00ey_coeff).reshape((1, 40, 30))

# op _00tB_power_combination_eval
# LANG: _00rk --> _00tC
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0780__00tC = (v0662__00rk**1)
v0780__00tC = (v0780__00tC*_00tB_coeff).reshape((1, 40, 30))

# op _00tL_linear_combination_eval
# LANG: _00tK, _tangential_inflow_velocity --> _00tM
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0786__00tM = _00tL_constant+1*v0604__tangential_inflow_velocity+-1*v0787__00tK

# op _00tb_power_combination_eval
# LANG: _00ta, prandtl_loss_factor --> _00tc
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0720__00tc = (v0719__00ta**1)*(v0637_prandtl_loss_factor**1)
v0720__00tc = (v0720__00tc*_00tb_coeff).reshape((1, 40, 30))

# op _00tn_power_combination_eval
# LANG: _ut --> _00to
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0740__00to = (v0684__ut**1)
v0740__00to = (v0740__00to*_00tn_coeff).reshape((1, 40, 30))

# op _00yM_log10_eval
# LANG: _00yL --> _00yN
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0887__00yN = np.log10(v0886__00yL)

# op _011O_log10_eval
# LANG: _011N --> _011P
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01817__011P = np.log10(v01816__011N)

# op _001E_power_combination_eval
# LANG: _001D --> _001F
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v083__001F = (v082__001D**1)
v083__001F = (v083__001F*_001E_coeff).reshape((1,))

# op _001Q_power_combination_eval
# LANG: _001P --> _001R
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v085__001R = (v084__001P**1)
v085__001R = (v085__001R*_001Q_coeff).reshape((1,))

# op _001f_power_combination_eval
# LANG: _001e --> _001g
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v078__001g = (v077__001e**1)
v078__001g = (v078__001g*_001f_coeff).reshape((1,))

# op _001s_power_combination_eval
# LANG: _001r --> _001t
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v081__001t = (v080__001r**1)
v081__001t = (v081__001t*_001s_coeff).reshape((1,))

# op _0021_power_combination_eval
# LANG: _0020 --> _0022
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v087__0022 = (v086__0020**1)
v087__0022 = (v087__0022*_0021_coeff).reshape((1,))

# op _002d_power_combination_eval
# LANG: _002c --> _002e
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v089__002e = (v088__002c**1)
v089__002e = (v089__002e*_002d_coeff).reshape((1,))

# op _002p_power_combination_eval
# LANG: _002o --> _002q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v091__002q = (v090__002o**1)
v091__002q = (v091__002q*_002p_coeff).reshape((1,))

# op _00La_power_combination_eval
# LANG: _00L9 --> rotor_1_disk_broadband_spl_A_weighted
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model
v01272_rotor_1_disk_broadband_spl_A_weighted = (v01271__00L9**1)
v01272_rotor_1_disk_broadband_spl_A_weighted = (v01272_rotor_1_disk_broadband_spl_A_weighted*_00La_coeff).reshape((1, 27))

# op _00Qt_power_combination_eval
# LANG: _00Qs --> rotor_2_disk_tonal_spl_A_weighted
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model
v01434_rotor_2_disk_tonal_spl_A_weighted = (v01433__00Qs**1)
v01434_rotor_2_disk_tonal_spl_A_weighted = (v01434_rotor_2_disk_tonal_spl_A_weighted*_00Qt_coeff).reshape((1, 27))

# op _00ci_cos_eval
# LANG: phi_distribution --> _00cj
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0328__00cj = np.cos(v0251_phi_distribution)

# op _00cm_sin_eval
# LANG: phi_distribution --> _00cn
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0395__00cn = np.sin(v0251_phi_distribution)

# op _00eA_power_combination_eval
# LANG: _00ez --> _00eB
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0408__00eB = (v0407__00ez**1)
v0408__00eB = (v0408__00eB*_00eA_coeff).reshape((1, 40, 30))

# op _00eE_power_combination_eval
# LANG: _ux_2 --> _00eF
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0411__00eF = (v0292__ux_2**2)
v0411__00eF = (v0411__00eF*_00eE_coeff).reshape((1, 40, 30))

# op _00eK_power_combination_eval
# LANG: _00eJ --> _00eL
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0415__00eL = (v0413__00eJ**2)
v0415__00eL = (v0415__00eL*_00eK_coeff).reshape((1, 40, 30))

# op _00ea_power_combination_eval
# LANG: _00e9, _dr --> _local_torque
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0348__local_torque = (v0347__00e9**1)*(v0202__dr**1)
v0348__local_torque = (v0348__local_torque*_00ea_coeff).reshape((1, 40, 30))

# op _00ec_power_combination_eval
# LANG: _00c7 --> _00ed
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0360__00ed = (v0296__00c7**1)
v0360__00ed = (v0360__00ed*_00ec_coeff).reshape((1, 40, 30))

# op _00em_linear_combination_eval
# LANG: _00el, _tangential_inflow_velocity --> _00en
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0366__00en = _00em_constant+1*v0231__tangential_inflow_velocity+-1*v0367__00el

# op _00gA_power_combination_eval
# LANG: _ux, _tangential_inflow_velocity --> _00gB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0424__00gB = (v0231__tangential_inflow_velocity**1)*(v0279__ux**1)
v0424__00gB = (v0424__00gB*_00gA_coeff).reshape((1, 40, 30))

# op _00gE_power_combination_eval
# LANG: _axial_inflow_velocity --> _00gF
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0427__00gF = (v0221__axial_inflow_velocity**1)
v0427__00gF = (v0427__00gF*_00gE_coeff).reshape((1, 40, 30))

# op _00gG_power_combination_eval
# LANG: _ux --> _00gH
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0429__00gH = (v0279__ux**2)
v0429__00gH = (v0429__00gH*_00gG_coeff).reshape((1, 40, 30))

# op _00gM_power_combination_eval
# LANG: _axial_inflow_velocity --> _00gN
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0431__00gN = (v0221__axial_inflow_velocity**2)
v0431__00gN = (v0431__00gN*_00gM_coeff).reshape((1, 40, 30))

# op _00gg_power_combination_eval
# LANG: _ut --> _00gh
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0387__00gh = (v0311__ut**1)
v0387__00gh = (v0387__00gh*_00gg_coeff).reshape((1, 40, 30))

# op _00hD_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00hE
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0458__00hE = np.sum(v0201__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00ht_single_tensor_sum_with_axis_eval
# LANG: _00bM --> _00hu
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0453__00hu = np.sum(v0440__00bM, axis = (1, 2)).reshape((1,))

# op _00rl_cos_eval
# LANG: phi_distribution --> _00rm
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0701__00rm = np.cos(v0624_phi_distribution)

# op _00rp_sin_eval
# LANG: phi_distribution --> _00rq
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0768__00rq = np.sin(v0624_phi_distribution)

# op _00tD_power_combination_eval
# LANG: _00tC --> _00tE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0781__00tE = (v0780__00tC**1)
v0781__00tE = (v0781__00tE*_00tD_coeff).reshape((1, 40, 30))

# op _00tH_power_combination_eval
# LANG: _ux_2 --> _00tI
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0784__00tI = (v0665__ux_2**2)
v0784__00tI = (v0784__00tI*_00tH_coeff).reshape((1, 40, 30))

# op _00tN_power_combination_eval
# LANG: _00tM --> _00tO
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0788__00tO = (v0786__00tM**2)
v0788__00tO = (v0788__00tO*_00tN_coeff).reshape((1, 40, 30))

# op _00td_power_combination_eval
# LANG: _00tc, _dr --> _local_torque
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0721__local_torque = (v0720__00tc**1)*(v0575__dr**1)
v0721__local_torque = (v0721__local_torque*_00td_coeff).reshape((1, 40, 30))

# op _00tf_power_combination_eval
# LANG: _00ra --> _00tg
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0733__00tg = (v0669__00ra**1)
v0733__00tg = (v0733__00tg*_00tf_coeff).reshape((1, 40, 30))

# op _00tp_linear_combination_eval
# LANG: _00to, _tangential_inflow_velocity --> _00tq
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0739__00tq = _00tp_constant+1*v0604__tangential_inflow_velocity+-1*v0740__00to

# op _00vD_power_combination_eval
# LANG: _ux, _tangential_inflow_velocity --> _00vE
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0797__00vE = (v0604__tangential_inflow_velocity**1)*(v0652__ux**1)
v0797__00vE = (v0797__00vE*_00vD_coeff).reshape((1, 40, 30))

# op _00vH_power_combination_eval
# LANG: _axial_inflow_velocity --> _00vI
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0800__00vI = (v0594__axial_inflow_velocity**1)
v0800__00vI = (v0800__00vI*_00vH_coeff).reshape((1, 40, 30))

# op _00vJ_power_combination_eval
# LANG: _ux --> _00vK
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0802__00vK = (v0652__ux**2)
v0802__00vK = (v0802__00vK*_00vJ_coeff).reshape((1, 40, 30))

# op _00vP_power_combination_eval
# LANG: _axial_inflow_velocity --> _00vQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0804__00vQ = (v0594__axial_inflow_velocity**2)
v0804__00vQ = (v0804__00vQ*_00vP_coeff).reshape((1, 40, 30))

# op _00vj_power_combination_eval
# LANG: _ut --> _00vk
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0760__00vk = (v0684__ut**1)
v0760__00vk = (v0760__00vk*_00vj_coeff).reshape((1, 40, 30))

# op _00wG_single_tensor_sum_with_axis_eval
# LANG: _rotor_radius --> _00wH
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0831__00wH = np.sum(v0574__rotor_radius, axis = (1, 2)).reshape((1,))

# op _00ww_single_tensor_sum_with_axis_eval
# LANG: _00qP --> _00wx
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0826__00wx = np.sum(v0813__00qP, axis = (1, 2)).reshape((1,))

# op _00yO_power_combination_eval
# LANG: _00yN --> rotor_1_disk_tonal_spl_A_weighted
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model
v0888_rotor_1_disk_tonal_spl_A_weighted = (v0887__00yN**1)
v0888_rotor_1_disk_tonal_spl_A_weighted = (v0888_rotor_1_disk_tonal_spl_A_weighted*_00yO_coeff).reshape((1, 27))

# op _011Q_power_combination_eval
# LANG: _011P --> rotor_2_disk_broadband_spl_A_weighted
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model
v01818_rotor_2_disk_broadband_spl_A_weighted = (v01817__011P**1)
v01818_rotor_2_disk_broadband_spl_A_weighted = (v01818_rotor_2_disk_broadband_spl_A_weighted*_011Q_coeff).reshape((1, 27))

# op _001h_indexed_passthrough_eval
# LANG: _001g, _001t, _001F, _001R, _0022, _002e, _002q --> temp_temperature
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v079_temp_temperature__temp[i_v078__001g__001h_indexed_passthrough_eval] = v078__001g.flatten()
v079_temp_temperature = v079_temp_temperature__temp.copy()
v079_temp_temperature__temp[i_v081__001t__001h_indexed_passthrough_eval] = v081__001t.flatten()
v079_temp_temperature = v079_temp_temperature__temp.copy()
v079_temp_temperature__temp[i_v083__001F__001h_indexed_passthrough_eval] = v083__001F.flatten()
v079_temp_temperature = v079_temp_temperature__temp.copy()
v079_temp_temperature__temp[i_v085__001R__001h_indexed_passthrough_eval] = v085__001R.flatten()
v079_temp_temperature = v079_temp_temperature__temp.copy()
v079_temp_temperature__temp[i_v087__0022__001h_indexed_passthrough_eval] = v087__0022.flatten()
v079_temp_temperature = v079_temp_temperature__temp.copy()
v079_temp_temperature__temp[i_v089__002e__001h_indexed_passthrough_eval] = v089__002e.flatten()
v079_temp_temperature = v079_temp_temperature__temp.copy()
v079_temp_temperature__temp[i_v091__002q__001h_indexed_passthrough_eval] = v091__002q.flatten()
v079_temp_temperature = v079_temp_temperature__temp.copy()

# op _00ck_power_combination_eval
# LANG: _00cj, Cl --> _00cl
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0254_Cl = v0254_Cl.reshape((1, 40, 30))
v0327__00cl = (v0254_Cl**1)*(v0328__00cj**1)
v0327__00cl = (v0327__00cl*_00ck_coeff).reshape((1, 40, 30))
v0254_Cl = v0254_Cl.reshape((1200,))

# op _00co_power_combination_eval
# LANG: _00cn, Cl --> _00cp
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0254_Cl = v0254_Cl.reshape((1, 40, 30))
v0394__00cp = (v0254_Cl**1)*(v0395__00cn**1)
v0394__00cp = (v0394__00cp*_00co_coeff).reshape((1, 40, 30))
v0254_Cl = v0254_Cl.reshape((1200,))

# op _00eC_power_combination_eval
# LANG: _00bU, _00eB --> _00eD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0409__00eD = (v0408__00eB**1)*(v0320__00bU**1)
v0409__00eD = (v0409__00eD*_00eC_coeff).reshape((1, 40, 30))

# op _00eM_linear_combination_eval
# LANG: _00eF, _00eL --> _00eN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0412__00eN = _00eM_constant+1*v0411__00eF+1*v0415__00eL

# op _00ee_power_combination_eval
# LANG: _00ed --> _00ef
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0361__00ef = (v0360__00ed**1)
v0361__00ef = (v0361__00ef*_00ee_coeff).reshape((1, 40, 30))

# op _00ei_power_combination_eval
# LANG: _ux_2 --> _00ej
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0364__00ej = (v0292__ux_2**2)
v0364__00ej = (v0364__00ej*_00ei_coeff).reshape((1, 40, 30))

# op _00eo_power_combination_eval
# LANG: _00en --> _00ep
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0368__00ep = (v0366__00en**2)
v0368__00ep = (v0368__00ep*_00eo_coeff).reshape((1, 40, 30))

# op _00fL_power_combination_eval
# LANG: _ut --> _00fM
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0403__00fM = (v0311__ut**1)
v0403__00fM = (v0403__00fM*_00fL_coeff).reshape((1, 40, 30))

# op _00fp_power_combination_eval
# LANG: _ut --> _00fq
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0336__00fq = (v0311__ut**1)
v0336__00fq = (v0336__00fq*_00fp_coeff).reshape((1, 40, 30))

# op _00gC_power_combination_eval
# LANG: _ut, _00gB --> _00gD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0425__00gD = (v0424__00gB**1)*(v0311__ut**1)
v0425__00gD = (v0425__00gD*_00gC_coeff).reshape((1, 40, 30))

# op _00gI_power_combination_eval
# LANG: _00gF, _00gH --> _00gJ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0428__00gJ = (v0427__00gF**1)*(v0429__00gH**1)
v0428__00gJ = (v0428__00gJ*_00gI_coeff).reshape((1, 40, 30))

# op _00gO_power_combination_eval
# LANG: _00gN --> _00gP
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0432__00gP = (v0431__00gN**1)
v0432__00gP = (v0432__00gP*_00gO_coeff).reshape((1, 40, 30))

# op _00ga_single_tensor_sum_with_axis_eval
# LANG: _local_torque --> _00gb
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0349__00gb = np.sum(v0348__local_torque, axis = (1, 2)).reshape((1,))

# op _00ge_power_combination_eval
# LANG: _00bU --> _00gf
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0384__00gf = (v0320__00bU**1)
v0384__00gf = (v0384__00gf*_00ge_coeff).reshape((1, 40, 30))

# op _00gi_linear_combination_eval
# LANG: _00gh, _tangential_inflow_velocity --> _00gj
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0386__00gj = _00gi_constant+1*v0231__tangential_inflow_velocity+-1*v0387__00gh

# op _00hF_power_combination_eval
# LANG: _00hE --> _00hG
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0459__00hG = (v0458__00hE**1)
v0459__00hG = (v0459__00hG*_00hF_coeff).reshape((1,))

# op _00hR_power_combination_eval
# LANG: _00bM, _axial_inflow_velocity --> _00hS
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0465__00hS = (v0221__axial_inflow_velocity**1)*(v0440__00bM**-1)
v0465__00hS = (v0465__00hS*_00hR_coeff).reshape((1, 40, 30))

# op _00hT_power_combination_eval
# LANG: _rotor_radius --> _00hU
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0467__00hU = (v0201__rotor_radius**1)
v0467__00hU = (v0467__00hU*_00hT_coeff).reshape((1, 40, 30))

# op _00hv_power_combination_eval
# LANG: _00hu --> _00hw
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0454__00hw = (v0453__00hu**1)
v0454__00hw = (v0454__00hw*_00hv_coeff).reshape((1,))

# op _00rn_power_combination_eval
# LANG: _00rm, Cl --> _00ro
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0627_Cl = v0627_Cl.reshape((1, 40, 30))
v0700__00ro = (v0627_Cl**1)*(v0701__00rm**1)
v0700__00ro = (v0700__00ro*_00rn_coeff).reshape((1, 40, 30))
v0627_Cl = v0627_Cl.reshape((1200,))

# op _00rr_power_combination_eval
# LANG: _00rq, Cl --> _00rs
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0627_Cl = v0627_Cl.reshape((1, 40, 30))
v0767__00rs = (v0627_Cl**1)*(v0768__00rq**1)
v0767__00rs = (v0767__00rs*_00rr_coeff).reshape((1, 40, 30))
v0627_Cl = v0627_Cl.reshape((1200,))

# op _00tF_power_combination_eval
# LANG: _00qX, _00tE --> _00tG
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0782__00tG = (v0781__00tE**1)*(v0693__00qX**1)
v0782__00tG = (v0782__00tG*_00tF_coeff).reshape((1, 40, 30))

# op _00tP_linear_combination_eval
# LANG: _00tI, _00tO --> _00tQ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0785__00tQ = _00tP_constant+1*v0784__00tI+1*v0788__00tO

# op _00th_power_combination_eval
# LANG: _00tg --> _00ti
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0734__00ti = (v0733__00tg**1)
v0734__00ti = (v0734__00ti*_00th_coeff).reshape((1, 40, 30))

# op _00tl_power_combination_eval
# LANG: _ux_2 --> _00tm
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0737__00tm = (v0665__ux_2**2)
v0737__00tm = (v0737__00tm*_00tl_coeff).reshape((1, 40, 30))

# op _00tr_power_combination_eval
# LANG: _00tq --> _00ts
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0741__00ts = (v0739__00tq**2)
v0741__00ts = (v0741__00ts*_00tr_coeff).reshape((1, 40, 30))

# op _00uO_power_combination_eval
# LANG: _ut --> _00uP
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0776__00uP = (v0684__ut**1)
v0776__00uP = (v0776__00uP*_00uO_coeff).reshape((1, 40, 30))

# op _00us_power_combination_eval
# LANG: _ut --> _00ut
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0709__00ut = (v0684__ut**1)
v0709__00ut = (v0709__00ut*_00us_coeff).reshape((1, 40, 30))

# op _00vF_power_combination_eval
# LANG: _ut, _00vE --> _00vG
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0798__00vG = (v0797__00vE**1)*(v0684__ut**1)
v0798__00vG = (v0798__00vG*_00vF_coeff).reshape((1, 40, 30))

# op _00vL_power_combination_eval
# LANG: _00vI, _00vK --> _00vM
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0801__00vM = (v0800__00vI**1)*(v0802__00vK**1)
v0801__00vM = (v0801__00vM*_00vL_coeff).reshape((1, 40, 30))

# op _00vR_power_combination_eval
# LANG: _00vQ --> _00vS
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0805__00vS = (v0804__00vQ**1)
v0805__00vS = (v0805__00vS*_00vR_coeff).reshape((1, 40, 30))

# op _00vd_single_tensor_sum_with_axis_eval
# LANG: _local_torque --> _00ve
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0722__00ve = np.sum(v0721__local_torque, axis = (1, 2)).reshape((1,))

# op _00vh_power_combination_eval
# LANG: _00qX --> _00vi
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0757__00vi = (v0693__00qX**1)
v0757__00vi = (v0757__00vi*_00vh_coeff).reshape((1, 40, 30))

# op _00vl_linear_combination_eval
# LANG: _00vk, _tangential_inflow_velocity --> _00vm
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0759__00vm = _00vl_constant+1*v0604__tangential_inflow_velocity+-1*v0760__00vk

# op _00wI_power_combination_eval
# LANG: _00wH --> _00wJ
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0832__00wJ = (v0831__00wH**1)
v0832__00wJ = (v0832__00wJ*_00wI_coeff).reshape((1,))

# op _00wU_power_combination_eval
# LANG: _00qP, _axial_inflow_velocity --> _00wV
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0838__00wV = (v0594__axial_inflow_velocity**1)*(v0813__00qP**-1)
v0838__00wV = (v0838__00wV*_00wU_coeff).reshape((1, 40, 30))

# op _00wW_power_combination_eval
# LANG: _rotor_radius --> _00wX
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0840__00wX = (v0574__rotor_radius**1)
v0840__00wX = (v0840__00wX*_00wW_coeff).reshape((1, 40, 30))

# op _00wy_power_combination_eval
# LANG: _00wx --> _00wz
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0827__00wz = (v0826__00wx**1)
v0827__00wz = (v0827__00wz*_00wy_coeff).reshape((1,))

# op _015L expand_array_eval
# LANG: rotor_1_disk_tonal_spl --> _015M
# SHAPES: (1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01941__015M = np.einsum('bc,a->abc', v01218_rotor_1_disk_tonal_spl.reshape((1, 27)) ,np.ones((1,))).reshape((1, 1, 27))

# op _015P expand_array_eval
# LANG: rotor_1_disk_broadband_spl --> _015Q
# SHAPES: (1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01943__015Q = np.einsum('bc,a->abc', v01383_rotor_1_disk_broadband_spl.reshape((1, 27)) ,np.ones((1,))).reshape((1, 1, 27))

# op _015S expand_array_eval
# LANG: rotor_2_disk_tonal_spl --> _015T
# SHAPES: (1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01944__015T = np.einsum('bc,a->abc', v01764_rotor_2_disk_tonal_spl.reshape((1, 27)) ,np.ones((1,))).reshape((1, 1, 27))

# op _015V expand_array_eval
# LANG: rotor_2_disk_broadband_spl --> _015W
# SHAPES: (1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01945__015W = np.einsum('bc,a->abc', v01929_rotor_2_disk_broadband_spl.reshape((1, 27)) ,np.ones((1,))).reshape((1, 1, 27))

# op _0168 expand_array_eval
# LANG: rotor_1_disk_tonal_spl_A_weighted --> _0169
# SHAPES: (1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01951__0169 = np.einsum('bc,a->abc', v0888_rotor_1_disk_tonal_spl_A_weighted.reshape((1, 27)) ,np.ones((1,))).reshape((1, 1, 27))

# op _016c expand_array_eval
# LANG: rotor_1_disk_broadband_spl_A_weighted --> _016d
# SHAPES: (1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01953__016d = np.einsum('bc,a->abc', v01272_rotor_1_disk_broadband_spl_A_weighted.reshape((1, 27)) ,np.ones((1,))).reshape((1, 1, 27))

# op _016f expand_array_eval
# LANG: rotor_2_disk_tonal_spl_A_weighted --> _016g
# SHAPES: (1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01954__016g = np.einsum('bc,a->abc', v01434_rotor_2_disk_tonal_spl_A_weighted.reshape((1, 27)) ,np.ones((1,))).reshape((1, 1, 27))

# op _016i expand_array_eval
# LANG: rotor_2_disk_broadband_spl_A_weighted --> _016j
# SHAPES: (1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01955__016j = np.einsum('bc,a->abc', v01818_rotor_2_disk_broadband_spl_A_weighted.reshape((1, 27)) ,np.ones((1,))).reshape((1, 1, 27))

# op _002v single_tensor_sum_no_axis_eval
# LANG: temp_temperature --> hover_temperature
# SHAPES: (7,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v092_hover_temperature = np.sum(v079_temp_temperature).reshape((1,))

# op _0056_decompose_eval
# LANG: T --> _0057
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0143__0057 = ((v0341_T.flatten())[src_indices__0057__0056]).reshape((1,))

# op _00eO_power_combination_eval
# LANG: _00eD, _00eN --> _00eP
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0410__00eP = (v0409__00eD**1)*(v0412__00eN**1)
v0410__00eP = (v0410__00eP*_00eO_coeff).reshape((1, 40, 30))

# op _00eg_power_combination_eval
# LANG: _00bU, _00ef --> _00eh
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0362__00eh = (v0361__00ef**1)*(v0320__00bU**1)
v0362__00eh = (v0362__00eh*_00eg_coeff).reshape((1, 40, 30))

# op _00eq_linear_combination_eval
# LANG: _00ej, _00ep --> _00er
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0365__00er = _00eq_constant+1*v0364__00ej+1*v0368__00ep

# op _00fD_power_combination_eval
# LANG: _00cp --> _00fE
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0396__00fE = (v0394__00cp**1)
v0396__00fE = (v0396__00fE*_00fD_coeff).reshape((1, 40, 30))

# op _00fN_linear_combination_eval
# LANG: _00fM, _tangential_inflow_velocity --> _00fO
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0402__00fO = _00fN_constant+1*v0231__tangential_inflow_velocity+-1*v0403__00fM

# op _00fh_power_combination_eval
# LANG: _00cl --> _00fi
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0329__00fi = (v0327__00cl**1)
v0329__00fi = (v0329__00fi*_00fh_coeff).reshape((1, 40, 30))

# op _00fr_linear_combination_eval
# LANG: _00fq, _tangential_inflow_velocity --> _00fs
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0335__00fs = _00fr_constant+1*v0231__tangential_inflow_velocity+-1*v0336__00fq

# op _00gK_linear_combination_eval
# LANG: _00gD, _00gJ --> _00gL
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0426__00gL = _00gK_constant+1*v0425__00gD+-1*v0428__00gJ

# op _00gQ_power_combination_eval
# LANG: _ux, _00gP --> _00gR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0433__00gR = (v0432__00gP**1)*(v0279__ux**1)
v0433__00gR = (v0433__00gR*_00gQ_coeff).reshape((1, 40, 30))

# op _00gc_power_combination_eval
# LANG: _00gb --> total_torque
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0350_total_torque = (v0349__00gb**1)
v0350_total_torque = (v0350_total_torque*_00gc_coeff).reshape((1,))

# op _00gk_power_combination_eval
# LANG: _00gf, _00gj --> _00gl
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0385__00gl = (v0384__00gf**1)*(v0386__00gj**1)
v0385__00gl = (v0385__00gl*_00gk_coeff).reshape((1, 40, 30))

# op _00gw_power_combination_eval
# LANG: _radius --> _00gx
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0421__00gx = (v0214__radius**1)
v0421__00gx = (v0421__00gx*_00gw_coeff).reshape((1, 40, 30))

# op _00hH_power_combination_eval
# LANG: _00hG --> _00hI
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0460__00hI = (v0459__00hG**1)
v0460__00hI = (v0460__00hI*_00hH_coeff).reshape((1,))

# op _00hV_power_combination_eval
# LANG: _00hS, _00hU --> _00hW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0466__00hW = (v0465__00hS**1)*(v0467__00hU**-1)
v0466__00hW = (v0466__00hW*_00hV_coeff).reshape((1, 40, 30))

# op _00hx_power_combination_eval
# LANG: _00hw --> _00hy
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0455__00hy = (v0454__00hw**1)
v0455__00hy = (v0455__00hy*_00hx_coeff).reshape((1,))

# op _00k9_decompose_eval
# LANG: T --> _00ka
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0516__00ka = ((v0714_T.flatten())[src_indices__00ka__00k9]).reshape((1,))

# op _00tR_power_combination_eval
# LANG: _00tG, _00tQ --> _00tS
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0783__00tS = (v0782__00tG**1)*(v0785__00tQ**1)
v0783__00tS = (v0783__00tS*_00tR_coeff).reshape((1, 40, 30))

# op _00tj_power_combination_eval
# LANG: _00qX, _00ti --> _00tk
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0735__00tk = (v0734__00ti**1)*(v0693__00qX**1)
v0735__00tk = (v0735__00tk*_00tj_coeff).reshape((1, 40, 30))

# op _00tt_linear_combination_eval
# LANG: _00tm, _00ts --> _00tu
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0738__00tu = _00tt_constant+1*v0737__00tm+1*v0741__00ts

# op _00uG_power_combination_eval
# LANG: _00rs --> _00uH
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0769__00uH = (v0767__00rs**1)
v0769__00uH = (v0769__00uH*_00uG_coeff).reshape((1, 40, 30))

# op _00uQ_linear_combination_eval
# LANG: _00uP, _tangential_inflow_velocity --> _00uR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0775__00uR = _00uQ_constant+1*v0604__tangential_inflow_velocity+-1*v0776__00uP

# op _00uk_power_combination_eval
# LANG: _00ro --> _00ul
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0702__00ul = (v0700__00ro**1)
v0702__00ul = (v0702__00ul*_00uk_coeff).reshape((1, 40, 30))

# op _00uu_linear_combination_eval
# LANG: _00ut, _tangential_inflow_velocity --> _00uv
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0708__00uv = _00uu_constant+1*v0604__tangential_inflow_velocity+-1*v0709__00ut

# op _00vN_linear_combination_eval
# LANG: _00vG, _00vM --> _00vO
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0799__00vO = _00vN_constant+1*v0798__00vG+-1*v0801__00vM

# op _00vT_power_combination_eval
# LANG: _ux, _00vS --> _00vU
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0806__00vU = (v0805__00vS**1)*(v0652__ux**1)
v0806__00vU = (v0806__00vU*_00vT_coeff).reshape((1, 40, 30))

# op _00vf_power_combination_eval
# LANG: _00ve --> total_torque
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0723_total_torque = (v0722__00ve**1)
v0723_total_torque = (v0723_total_torque*_00vf_coeff).reshape((1,))

# op _00vn_power_combination_eval
# LANG: _00vi, _00vm --> _00vo
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0758__00vo = (v0757__00vi**1)*(v0759__00vm**1)
v0758__00vo = (v0758__00vo*_00vn_coeff).reshape((1, 40, 30))

# op _00vz_power_combination_eval
# LANG: _radius --> _00vA
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0794__00vA = (v0587__radius**1)
v0794__00vA = (v0794__00vA*_00vz_coeff).reshape((1, 40, 30))

# op _00wA_power_combination_eval
# LANG: _00wz --> _00wB
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0828__00wB = (v0827__00wz**1)
v0828__00wB = (v0828__00wB*_00wA_coeff).reshape((1,))

# op _00wK_power_combination_eval
# LANG: _00wJ --> _00wL
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0833__00wL = (v0832__00wJ**1)
v0833__00wL = (v0833__00wL*_00wK_coeff).reshape((1,))

# op _00wY_power_combination_eval
# LANG: _00wV, _00wX --> _00wZ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0839__00wZ = (v0838__00wV**1)*(v0840__00wX**-1)
v0839__00wZ = (v0839__00wZ*_00wY_coeff).reshape((1, 40, 30))

# op _015N_indexed_passthrough_eval
# LANG: _015M, _015Q, _015T, _015W --> noise_components
# SHAPES: (1, 1, 27), (1, 1, 27), (1, 1, 27), (1, 1, 27) --> (4, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01942_noise_components__temp[i_v01941__015M__015N_indexed_passthrough_eval] = v01941__015M.flatten()
v01942_noise_components = v01942_noise_components__temp.copy()
v01942_noise_components__temp[i_v01943__015Q__015N_indexed_passthrough_eval] = v01943__015Q.flatten()
v01942_noise_components = v01942_noise_components__temp.copy()
v01942_noise_components__temp[i_v01944__015T__015N_indexed_passthrough_eval] = v01944__015T.flatten()
v01942_noise_components = v01942_noise_components__temp.copy()
v01942_noise_components__temp[i_v01945__015W__015N_indexed_passthrough_eval] = v01945__015W.flatten()
v01942_noise_components = v01942_noise_components__temp.copy()

# op _016a_indexed_passthrough_eval
# LANG: _0169, _016d, _016g, _016j --> A_weighted_noise_components
# SHAPES: (1, 1, 27), (1, 1, 27), (1, 1, 27), (1, 1, 27) --> (4, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01952_A_weighted_noise_components__temp[i_v01951__0169__016a_indexed_passthrough_eval] = v01951__0169.flatten()
v01952_A_weighted_noise_components = v01952_A_weighted_noise_components__temp.copy()
v01952_A_weighted_noise_components__temp[i_v01953__016d__016a_indexed_passthrough_eval] = v01953__016d.flatten()
v01952_A_weighted_noise_components = v01952_A_weighted_noise_components__temp.copy()
v01952_A_weighted_noise_components__temp[i_v01954__016g__016a_indexed_passthrough_eval] = v01954__016g.flatten()
v01952_A_weighted_noise_components = v01952_A_weighted_noise_components__temp.copy()
v01952_A_weighted_noise_components__temp[i_v01955__016j__016a_indexed_passthrough_eval] = v01955__016j.flatten()
v01952_A_weighted_noise_components = v01952_A_weighted_noise_components__temp.copy()

# op _002x_power_combination_eval
# LANG: hover_temperature --> _002y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v095__002y = (v092_hover_temperature**1)
v095__002y = (v095__002y*_002x_coeff).reshape((1,))

# op _0058 reshape_eval
# LANG: _0057 --> _0059
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0144__0059 = v0143__0057.reshape((1, 1))

# op _005a_decompose_eval
# LANG: thrust_vector --> _005b, _005h, _005m
# SHAPES: (1, 3) --> (1, 1), (1, 1), (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0146__005b = ((v0128_thrust_vector.flatten())[src_indices__005b__005a]).reshape((1, 1))
v0147__005h = ((v0128_thrust_vector.flatten())[src_indices__005h__005a]).reshape((1, 1))
v0148__005m = ((v0128_thrust_vector.flatten())[src_indices__005m__005a]).reshape((1, 1))

# op _005f reshape_eval
# LANG: _0057 --> _005g
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0150__005g = v0143__0057.reshape((1, 1))

# op _005k reshape_eval
# LANG: _0057 --> _005l
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0152__005l = v0143__0057.reshape((1, 1))

# op _00QO_power_combination_eval
# LANG: temperature --> _00QP
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01445__00QP = (v01439_temperature**1)
v01445__00QP = (v01445__00QP*_00QO_coeff).reshape((1,))

# op _00dL_power_combination_eval
# LANG: _angular_speed --> _00dM
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0354__00dM = (v0213__angular_speed**1)
v0354__00dM = (v0354__00dM*_00dL_coeff).reshape((1, 40, 30))

# op _00eQ_power_combination_eval
# LANG: _00eP, _chord --> _00eR
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0416__00eR = (v0410__00eP**1)*(v0209__chord**1)
v0416__00eR = (v0416__00eR*_00eQ_coeff).reshape((1, 40, 30))

# op _00es_power_combination_eval
# LANG: _00eh, _00er --> _00et
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0363__00et = (v0362__00eh**1)*(v0365__00er**1)
v0363__00et = (v0363__00et*_00es_coeff).reshape((1, 40, 30))

# op _00fF_power_combination_eval
# LANG: _00fE --> _00fG
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0397__00fG = (v0396__00fE**1)
v0397__00fG = (v0397__00fG*_00fF_coeff).reshape((1, 40, 30))

# op _00fJ_power_combination_eval
# LANG: _ux_2 --> _00fK
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0400__00fK = (v0292__ux_2**2)
v0400__00fK = (v0400__00fK*_00fJ_coeff).reshape((1, 40, 30))

# op _00fP_power_combination_eval
# LANG: _00fO --> _00fQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0404__00fQ = (v0402__00fO**2)
v0404__00fQ = (v0404__00fQ*_00fP_coeff).reshape((1, 40, 30))

# op _00fj_power_combination_eval
# LANG: _00fi --> _00fk
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0330__00fk = (v0329__00fi**1)
v0330__00fk = (v0330__00fk*_00fj_coeff).reshape((1, 40, 30))

# op _00fn_power_combination_eval
# LANG: _ux_2 --> _00fo
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0333__00fo = (v0292__ux_2**2)
v0333__00fo = (v0333__00fo*_00fn_coeff).reshape((1, 40, 30))

# op _00ft_power_combination_eval
# LANG: _00fs --> _00fu
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0337__00fu = (v0335__00fs**2)
v0337__00fu = (v0337__00fu*_00ft_coeff).reshape((1, 40, 30))

# op _00gS_linear_combination_eval
# LANG: _00gL, _00gR --> _00gT
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0430__00gT = _00gS_constant+1*v0426__00gL+1*v0433__00gR

# op _00gm_power_combination_eval
# LANG: _ut, _00gl --> _00gn
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0388__00gn = (v0385__00gl**1)*(v0311__ut**1)
v0388__00gn = (v0388__00gn*_00gm_coeff).reshape((1, 40, 30))

# op _00gy_power_combination_eval
# LANG: _00gx --> _00gz
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0422__00gz = (v0421__00gx**1)
v0422__00gz = (v0422__00gz*_00gy_coeff).reshape((1, 40, 30))

# op _00hJ_power_combination_eval
# LANG: _00hI --> _00hK
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0461__00hK = (v0460__00hI**1)
v0461__00hK = (v0461__00hK*_00hJ_coeff).reshape((1,))

# op _00hX_single_tensor_sum_with_axis_eval
# LANG: _00hW --> _00hY
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0468__00hY = np.sum(v0466__00hW, axis = (1, 2)).reshape((1,))

# op _00hr_power_combination_eval
# LANG: total_torque, density --> _00hs
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0242_density = v0242_density.reshape((1,))
v0451__00hs = (v0350_total_torque**1)*(v0242_density**-1)
v0451__00hs = (v0451__00hs*_00hr_coeff).reshape((1,))
v0242_density = v0242_density.reshape((1, 1))

# op _00hz_power_combination_eval
# LANG: _00hy --> _00hA
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0456__00hA = (v0455__00hy**2)
v0456__00hA = (v0456__00hA*_00hz_coeff).reshape((1,))

# op _00kb reshape_eval
# LANG: _00ka --> _00kc
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0517__00kc = v0516__00ka.reshape((1, 1))

# op _00kd_decompose_eval
# LANG: thrust_vector --> _00ke, _00kk, _00kp
# SHAPES: (1, 3) --> (1, 1), (1, 1), (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0519__00ke = ((v0501_thrust_vector.flatten())[src_indices__00ke__00kd]).reshape((1, 1))
v0520__00kk = ((v0501_thrust_vector.flatten())[src_indices__00kk__00kd]).reshape((1, 1))
v0521__00kp = ((v0501_thrust_vector.flatten())[src_indices__00kp__00kd]).reshape((1, 1))

# op _00ki reshape_eval
# LANG: _00ka --> _00kj
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0523__00kj = v0516__00ka.reshape((1, 1))

# op _00kn reshape_eval
# LANG: _00ka --> _00ko
# SHAPES: (1,) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0525__00ko = v0516__00ka.reshape((1, 1))

# op _00sO_power_combination_eval
# LANG: _angular_speed --> _00sP
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0727__00sP = (v0586__angular_speed**1)
v0727__00sP = (v0727__00sP*_00sO_coeff).reshape((1, 40, 30))

# op _00tT_power_combination_eval
# LANG: _00tS, _chord --> _00tU
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0789__00tU = (v0783__00tS**1)*(v0582__chord**1)
v0789__00tU = (v0789__00tU*_00tT_coeff).reshape((1, 40, 30))

# op _00tv_power_combination_eval
# LANG: _00tk, _00tu --> _00tw
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0736__00tw = (v0735__00tk**1)*(v0738__00tu**1)
v0736__00tw = (v0736__00tw*_00tv_coeff).reshape((1, 40, 30))

# op _00uI_power_combination_eval
# LANG: _00uH --> _00uJ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0770__00uJ = (v0769__00uH**1)
v0770__00uJ = (v0770__00uJ*_00uI_coeff).reshape((1, 40, 30))

# op _00uM_power_combination_eval
# LANG: _ux_2 --> _00uN
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0773__00uN = (v0665__ux_2**2)
v0773__00uN = (v0773__00uN*_00uM_coeff).reshape((1, 40, 30))

# op _00uS_power_combination_eval
# LANG: _00uR --> _00uT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0777__00uT = (v0775__00uR**2)
v0777__00uT = (v0777__00uT*_00uS_coeff).reshape((1, 40, 30))

# op _00um_power_combination_eval
# LANG: _00ul --> _00un
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0703__00un = (v0702__00ul**1)
v0703__00un = (v0703__00un*_00um_coeff).reshape((1, 40, 30))

# op _00uq_power_combination_eval
# LANG: _ux_2 --> _00ur
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0706__00ur = (v0665__ux_2**2)
v0706__00ur = (v0706__00ur*_00uq_coeff).reshape((1, 40, 30))

# op _00uw_power_combination_eval
# LANG: _00uv --> _00ux
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0710__00ux = (v0708__00uv**2)
v0710__00ux = (v0710__00ux*_00uw_coeff).reshape((1, 40, 30))

# op _00vB_power_combination_eval
# LANG: _00vA --> _00vC
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0795__00vC = (v0794__00vA**1)
v0795__00vC = (v0795__00vC*_00vB_coeff).reshape((1, 40, 30))

# op _00vV_linear_combination_eval
# LANG: _00vO, _00vU --> _00vW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0803__00vW = _00vV_constant+1*v0799__00vO+1*v0806__00vU

# op _00vp_power_combination_eval
# LANG: _ut, _00vo --> _00vq
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0761__00vq = (v0758__00vo**1)*(v0684__ut**1)
v0761__00vq = (v0761__00vq*_00vp_coeff).reshape((1, 40, 30))

# op _00wC_power_combination_eval
# LANG: _00wB --> _00wD
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0829__00wD = (v0828__00wB**2)
v0829__00wD = (v0829__00wD*_00wC_coeff).reshape((1,))

# op _00wM_power_combination_eval
# LANG: _00wL --> _00wN
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0834__00wN = (v0833__00wL**1)
v0834__00wN = (v0834__00wN*_00wM_coeff).reshape((1,))

# op _00w__single_tensor_sum_with_axis_eval
# LANG: _00wZ --> _00x0
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0841__00x0 = np.sum(v0839__00wZ, axis = (1, 2)).reshape((1,))

# op _00wu_power_combination_eval
# LANG: total_torque, density --> _00wv
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0615_density = v0615_density.reshape((1,))
v0824__00wv = (v0723_total_torque**1)*(v0615_density**-1)
v0824__00wv = (v0824__00wv*_00wu_coeff).reshape((1,))
v0615_density = v0615_density.reshape((1, 1))

# op _00z8_power_combination_eval
# LANG: temperature --> _00z9
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0899__00z9 = (v0893_temperature**1)
v0899__00z9 = (v0899__00z9*_00z8_coeff).reshape((1,))

# op _015X_power_combination_eval
# LANG: noise_components --> _015Y
# SHAPES: (4, 1, 27) --> (4, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01946__015Y = (v01942_noise_components**1)
v01946__015Y = (v01946__015Y*_015X_coeff).reshape((4, 1, 27))

# op _016k_power_combination_eval
# LANG: A_weighted_noise_components --> _016l
# SHAPES: (4, 1, 27) --> (4, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01956__016l = (v01952_A_weighted_noise_components**1)
v01956__016l = (v01956__016l*_016k_coeff).reshape((4, 1, 27))

# op _0013_power_combination_eval
# LANG: hover_altitude --> _0014
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v047__0014 = (v046_hover_altitude**6)
v047__0014 = (v047__0014*_0013_coeff).reshape((1,))

# op _0018_power_combination_eval
# LANG: hover_altitude --> _0019
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v062__0019 = (v046_hover_altitude**6)
v062__0019 = (v062__0019*_0018_coeff).reshape((1,))

# op _001G_power_combination_eval
# LANG: hover_altitude --> _001H
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v054__001H = (v046_hover_altitude**3)
v054__001H = (v054__001H*_001G_coeff).reshape((1,))

# op _001K_power_combination_eval
# LANG: hover_altitude --> _001L
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v069__001L = (v046_hover_altitude**3)
v069__001L = (v069__001L*_001K_coeff).reshape((1,))

# op _001S_power_combination_eval
# LANG: hover_altitude --> _001T
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v056__001T = (v046_hover_altitude**2)
v056__001T = (v056__001T*_001S_coeff).reshape((1,))

# op _001W_power_combination_eval
# LANG: hover_altitude --> _001X
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v071__001X = (v046_hover_altitude**2)
v071__001X = (v071__001X*_001W_coeff).reshape((1,))

# op _001i_power_combination_eval
# LANG: hover_altitude --> _001j
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v050__001j = (v046_hover_altitude**5)
v050__001j = (v050__001j*_001i_coeff).reshape((1,))

# op _001m_power_combination_eval
# LANG: hover_altitude --> _001n
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v065__001n = (v046_hover_altitude**5)
v065__001n = (v065__001n*_001m_coeff).reshape((1,))

# op _001u_power_combination_eval
# LANG: hover_altitude --> _001v
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v052__001v = (v046_hover_altitude**4)
v052__001v = (v052__001v*_001u_coeff).reshape((1,))

# op _001y_power_combination_eval
# LANG: hover_altitude --> _001z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v067__001z = (v046_hover_altitude**4)
v067__001z = (v067__001z*_001y_coeff).reshape((1,))

# op _0023_power_combination_eval
# LANG: hover_altitude --> _0024
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v058__0024 = (v046_hover_altitude**1)
v058__0024 = (v058__0024*_0023_coeff).reshape((1,))

# op _0027_power_combination_eval
# LANG: hover_altitude --> _0028
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v073__0028 = (v046_hover_altitude**1)
v073__0028 = (v073__0028*_0027_coeff).reshape((1,))

# op _002f_power_combination_eval
# LANG: hover_altitude --> _002g
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v060__002g = (v046_hover_altitude**0)
v060__002g = (v060__002g*_002f_coeff).reshape((1,))

# op _002j_power_combination_eval
# LANG: hover_altitude --> _002k
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v075__002k = (v046_hover_altitude**0)
v075__002k = (v075__002k*_002j_coeff).reshape((1,))

# op _002z_power_combination_eval
# LANG: _002y --> _002A
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v096__002A = (v095__002y**1.5)
v096__002A = (v096__002A*_002z_coeff).reshape((1,))

# op _004n expand_array_eval
# LANG: rotor_2_disk_origin --> thrust_origin
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v022_rotor_2_disk_origin = v022_rotor_2_disk_origin.reshape((3,))
v0129_thrust_origin = np.einsum('b,a->ab', v022_rotor_2_disk_origin.reshape((3,)) ,np.ones((1,))).reshape((1, 3))
v022_rotor_2_disk_origin = v022_rotor_2_disk_origin.reshape((1, 3))

# op _005c_power_combination_eval
# LANG: _0059, _005b --> _005d
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0145__005d = (v0144__0059**1)*(v0146__005b**1)
v0145__005d = (v0145__005d*_005c_coeff).reshape((1, 1))

# op _005i_power_combination_eval
# LANG: _005h, _005g --> _005j
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0151__005j = (v0150__005g**1)*(v0147__005h**1)
v0151__005j = (v0151__005j*_005i_coeff).reshape((1, 1))

# op _005n_power_combination_eval
# LANG: _005m, _005l --> _005o
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0153__005o = (v0152__005l**1)*(v0148__005m**1)
v0153__005o = (v0153__005o*_005n_coeff).reshape((1, 1))

# op _00AI_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00AJ
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0953__00AJ = (v0945_rel_obs_z_pos**1)*(v0952_rel_obs_dist**-1)
v0953__00AJ = (v0953__00AJ*_00AI_coeff).reshape((1, 1, 27))

# op _00AQ_linear_combination_eval
# LANG: rel_obs_z_pos --> _00AR
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0958__00AR = _00AQ_constant+1*v0945_rel_obs_z_pos

# op _00ME_linear_combination_eval
# LANG: rel_obs_z_pos --> _00MF
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01324__00MF = _00ME_constant+1*v01311_rel_obs_z_pos

# op _00Mw_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00Mx
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01319__00Mx = (v01311_rel_obs_z_pos**1)*(v01318_rel_obs_dist**-1)
v01319__00Mx = (v01319__00Mx*_00Mw_coeff).reshape((1, 1, 27))

# op _00QQ_power_combination_eval
# LANG: _00QP --> _00QR
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01446__00QR = (v01445__00QP**1.5)
v01446__00QR = (v01446__00QR*_00QQ_coeff).reshape((1,))

# op _00Sn_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _00So
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01499__00So = (v01491_rel_obs_z_pos**1)*(v01498_rel_obs_dist**-1)
v01499__00So = (v01499__00So*_00Sn_coeff).reshape((1, 1, 27))

# op _00Sv_linear_combination_eval
# LANG: rel_obs_z_pos --> _00Sw
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01504__00Sw = _00Sv_constant+1*v01491_rel_obs_z_pos

# op _00dN_power_combination_eval
# LANG: _00dM --> _00dO
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0355__00dO = (v0354__00dM**1)
v0355__00dO = (v0355__00dO*_00dN_coeff).reshape((1, 40, 30))

# op _00eS_power_combination_eval
# LANG: _00eR, _dr --> _00eT
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0417__00eT = (v0416__00eR**1)*(v0202__dr**1)
v0417__00eT = (v0417__00eT*_00eS_coeff).reshape((1, 40, 30))

# op _00eu_power_combination_eval
# LANG: _00et, _chord --> _00ev
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0369__00ev = (v0363__00et**1)*(v0209__chord**1)
v0369__00ev = (v0369__00ev*_00eu_coeff).reshape((1, 40, 30))

# op _00fH_power_combination_eval
# LANG: _00bU, _00fG --> _00fI
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0398__00fI = (v0397__00fG**1)*(v0320__00bU**1)
v0398__00fI = (v0398__00fI*_00fH_coeff).reshape((1, 40, 30))

# op _00fR_linear_combination_eval
# LANG: _00fK, _00fQ --> _00fS
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0401__00fS = _00fR_constant+1*v0400__00fK+1*v0404__00fQ

# op _00fl_power_combination_eval
# LANG: _00bU, _00fk --> _00fm
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0331__00fm = (v0330__00fk**1)*(v0320__00bU**1)
v0331__00fm = (v0331__00fm*_00fl_coeff).reshape((1, 40, 30))

# op _00fv_linear_combination_eval
# LANG: _00fo, _00fu --> _00fw
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0334__00fw = _00fv_constant+1*v0333__00fo+1*v0337__00fu

# op _00gU_power_combination_eval
# LANG: _00gz, _00gT --> _00gV
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0423__00gV = (v0422__00gz**1)*(v0430__00gT**1)
v0423__00gV = (v0423__00gV*_00gU_coeff).reshape((1, 40, 30))

# op _00go_power_combination_eval
# LANG: _00gn, _radius --> _00gp
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0389__00gp = (v0388__00gn**1)*(v0214__radius**1)
v0389__00gp = (v0389__00gp*_00go_coeff).reshape((1, 40, 30))

# op _00hB_power_combination_eval
# LANG: _00hs, _00hA --> _00hC
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0452__00hC = (v0451__00hs**1)*(v0456__00hA**-1)
v0452__00hC = (v0452__00hC*_00hB_coeff).reshape((1,))

# op _00hL_power_combination_eval
# LANG: _00hK --> _00hM
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0462__00hM = (v0461__00hK**5)
v0462__00hM = (v0462__00hM*_00hL_coeff).reshape((1,))

# op _00hZ_power_combination_eval
# LANG: _00hY --> _00h_
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0469__00h_ = (v0468__00hY**1)
v0469__00h_ = (v0469__00h_*_00hZ_coeff).reshape((1,))

# op _00i6_power_combination_eval
# LANG: C_T --> _00i7
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0473__00i7 = (v0445_C_T**1)
v0473__00i7 = (v0473__00i7*_00i6_coeff).reshape((1,))

# op _00jq expand_array_eval
# LANG: rotor_1_disk_origin --> thrust_origin
# SHAPES: (3,) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v012_rotor_1_disk_origin = v012_rotor_1_disk_origin.reshape((3,))
v0502_thrust_origin = np.einsum('b,a->ab', v012_rotor_1_disk_origin.reshape((3,)) ,np.ones((1,))).reshape((1, 3))
v012_rotor_1_disk_origin = v012_rotor_1_disk_origin.reshape((1, 3))

# op _00kf_power_combination_eval
# LANG: _00kc, _00ke --> _00kg
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0518__00kg = (v0517__00kc**1)*(v0519__00ke**1)
v0518__00kg = (v0518__00kg*_00kf_coeff).reshape((1, 1))

# op _00kl_power_combination_eval
# LANG: _00kk, _00kj --> _00km
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0524__00km = (v0523__00kj**1)*(v0520__00kk**1)
v0524__00km = (v0524__00km*_00kl_coeff).reshape((1, 1))

# op _00kq_power_combination_eval
# LANG: _00kp, _00ko --> _00kr
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0526__00kr = (v0525__00ko**1)*(v0521__00kp**1)
v0526__00kr = (v0526__00kr*_00kq_coeff).reshape((1, 1))

# op _00sQ_power_combination_eval
# LANG: _00sP --> _00sR
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0728__00sR = (v0727__00sP**1)
v0728__00sR = (v0728__00sR*_00sQ_coeff).reshape((1, 40, 30))

# op _00tV_power_combination_eval
# LANG: _00tU, _dr --> _00tW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0790__00tW = (v0789__00tU**1)*(v0575__dr**1)
v0790__00tW = (v0790__00tW*_00tV_coeff).reshape((1, 40, 30))

# op _00tx_power_combination_eval
# LANG: _00tw, _chord --> _00ty
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0742__00ty = (v0736__00tw**1)*(v0582__chord**1)
v0742__00ty = (v0742__00ty*_00tx_coeff).reshape((1, 40, 30))

# op _00uK_power_combination_eval
# LANG: _00qX, _00uJ --> _00uL
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0771__00uL = (v0770__00uJ**1)*(v0693__00qX**1)
v0771__00uL = (v0771__00uL*_00uK_coeff).reshape((1, 40, 30))

# op _00uU_linear_combination_eval
# LANG: _00uN, _00uT --> _00uV
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0774__00uV = _00uU_constant+1*v0773__00uN+1*v0777__00uT

# op _00uo_power_combination_eval
# LANG: _00qX, _00un --> _00up
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0704__00up = (v0703__00un**1)*(v0693__00qX**1)
v0704__00up = (v0704__00up*_00uo_coeff).reshape((1, 40, 30))

# op _00uy_linear_combination_eval
# LANG: _00ur, _00ux --> _00uz
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0707__00uz = _00uy_constant+1*v0706__00ur+1*v0710__00ux

# op _00vX_power_combination_eval
# LANG: _00vC, _00vW --> _00vY
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0796__00vY = (v0795__00vC**1)*(v0803__00vW**1)
v0796__00vY = (v0796__00vY*_00vX_coeff).reshape((1, 40, 30))

# op _00vr_power_combination_eval
# LANG: _00vq, _radius --> _00vs
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0762__00vs = (v0761__00vq**1)*(v0587__radius**1)
v0762__00vs = (v0762__00vs*_00vr_coeff).reshape((1, 40, 30))

# op _00wE_power_combination_eval
# LANG: _00wv, _00wD --> _00wF
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0825__00wF = (v0824__00wv**1)*(v0829__00wD**-1)
v0825__00wF = (v0825__00wF*_00wE_coeff).reshape((1,))

# op _00wO_power_combination_eval
# LANG: _00wN --> _00wP
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0835__00wP = (v0834__00wN**5)
v0835__00wP = (v0835__00wP*_00wO_coeff).reshape((1,))

# op _00x1_power_combination_eval
# LANG: _00x0 --> _00x2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0842__00x2 = (v0841__00x0**1)
v0842__00x2 = (v0842__00x2*_00x1_coeff).reshape((1,))

# op _00x9_power_combination_eval
# LANG: C_T --> _00xa
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0846__00xa = (v0818_C_T**1)
v0846__00xa = (v0846__00xa*_00x9_coeff).reshape((1,))

# op _00za_power_combination_eval
# LANG: _00z9 --> _00zb
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0900__00zb = (v0899__00z9**1.5)
v0900__00zb = (v0900__00zb*_00za_coeff).reshape((1,))

# op _013b_power_combination_eval
# LANG: rel_obs_z_pos, rel_obs_dist --> _013c
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01865__013c = (v01857_rel_obs_z_pos**1)*(v01864_rel_obs_dist**-1)
v01865__013c = (v01865__013c*_013b_coeff).reshape((1, 1, 27))

# op _013j_linear_combination_eval
# LANG: rel_obs_z_pos --> _013k
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01870__013k = _013j_constant+1*v01857_rel_obs_z_pos

# op _015Z_exp_a_eval
# LANG: _015Y --> _015_
# SHAPES: (4, 1, 27) --> (4, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01947__015_ = _015Z_exp_a_eval_a**v01946__015Y

# op _016m_exp_a_eval
# LANG: _016l --> _016n
# SHAPES: (4, 1, 27) --> (4, 1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01957__016n = _016m_exp_a_eval_a**v01956__016l

# op _0015_power_combination_eval
# LANG: _0014 --> _0016
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v048__0016 = (v047__0014**1)
v048__0016 = (v048__0016*_0015_coeff).reshape((1,))

# op _001A_power_combination_eval
# LANG: _001z --> _001B
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v068__001B = (v067__001z**1)
v068__001B = (v068__001B*_001A_coeff).reshape((1,))

# op _001I_power_combination_eval
# LANG: _001H --> _001J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v055__001J = (v054__001H**1)
v055__001J = (v055__001J*_001I_coeff).reshape((1,))

# op _001M_power_combination_eval
# LANG: _001L --> _001N
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v070__001N = (v069__001L**1)
v070__001N = (v070__001N*_001M_coeff).reshape((1,))

# op _001U_power_combination_eval
# LANG: _001T --> _001V
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v057__001V = (v056__001T**1)
v057__001V = (v057__001V*_001U_coeff).reshape((1,))

# op _001Y_power_combination_eval
# LANG: _001X --> _001Z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v072__001Z = (v071__001X**1)
v072__001Z = (v072__001Z*_001Y_coeff).reshape((1,))

# op _001a_power_combination_eval
# LANG: _0019 --> _001b
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v063__001b = (v062__0019**1)
v063__001b = (v063__001b*_001a_coeff).reshape((1,))

# op _001k_power_combination_eval
# LANG: _001j --> _001l
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v051__001l = (v050__001j**1)
v051__001l = (v051__001l*_001k_coeff).reshape((1,))

# op _001o_power_combination_eval
# LANG: _001n --> _001p
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v066__001p = (v065__001n**1)
v066__001p = (v066__001p*_001o_coeff).reshape((1,))

# op _001w_power_combination_eval
# LANG: _001v --> _001x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v053__001x = (v052__001v**1)
v053__001x = (v053__001x*_001w_coeff).reshape((1,))

# op _0025_power_combination_eval
# LANG: _0024 --> _0026
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v059__0026 = (v058__0024**1)
v059__0026 = (v059__0026*_0025_coeff).reshape((1,))

# op _0029_power_combination_eval
# LANG: _0028 --> _002a
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v074__002a = (v073__0028**1)
v074__002a = (v074__002a*_0029_coeff).reshape((1,))

# op _002B_power_combination_eval
# LANG: _002A --> _002C
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v097__002C = (v096__002A**1)
v097__002C = (v097__002C*_002B_coeff).reshape((1,))

# op _002h_power_combination_eval
# LANG: _002g --> _002i
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v061__002i = (v060__002g**1)
v061__002i = (v061__002i*_002h_coeff).reshape((1,))

# op _002l_power_combination_eval
# LANG: _002k --> _002m
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v076__002m = (v075__002k**1)
v076__002m = (v076__002m*_002l_coeff).reshape((1,))

# op _005e_indexed_passthrough_eval
# LANG: _005d, _005j, _005o --> F
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0149_F__temp[i_v0145__005d__005e_indexed_passthrough_eval] = v0145__005d.flatten()
v0149_F = v0149_F__temp.copy()
v0149_F__temp[i_v0151__005j__005e_indexed_passthrough_eval] = v0151__005j.flatten()
v0149_F = v0149_F__temp.copy()
v0149_F__temp[i_v0153__005o__005e_indexed_passthrough_eval] = v0153__005o.flatten()
v0149_F = v0149_F__temp.copy()

# op _005p_linear_combination_eval
# LANG: thrust_origin, reference_point --> _005q
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0154__005q = _005p_constant+1*v0129_thrust_origin+-1*v0155_reference_point

# op _00AK arccos_eval
# LANG: _00AJ --> _00AL
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0954__00AL = np.arccos(v0953__00AJ)

# op _00AM_linear_combination_eval
# LANG: rel_obs_z_pos --> _00AN
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0956__00AN = _00AM_constant+1*v0945_rel_obs_z_pos

# op _00AS_power_combination_eval
# LANG: _00AR --> _00AT
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0959__00AT = (v0958__00AR**2)
v0959__00AT = (v0959__00AT*_00AS_coeff).reshape((1, 1, 27))

# op _00MA_linear_combination_eval
# LANG: rel_obs_z_pos --> _00MB
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01322__00MB = _00MA_constant+1*v01311_rel_obs_z_pos

# op _00MG_power_combination_eval
# LANG: _00MF --> _00MH
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01325__00MH = (v01324__00MF**2)
v01325__00MH = (v01325__00MH*_00MG_coeff).reshape((1, 1, 27))

# op _00My arccos_eval
# LANG: _00Mx --> _00Mz
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01320__00Mz = np.arccos(v01319__00Mx)

# op _00QS_power_combination_eval
# LANG: _00QR --> _00QT
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01447__00QT = (v01446__00QR**1)
v01447__00QT = (v01447__00QT*_00QS_coeff).reshape((1,))

# op _00Sp arccos_eval
# LANG: _00So --> _00Sq
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01500__00Sq = np.arccos(v01499__00So)

# op _00Sr_linear_combination_eval
# LANG: rel_obs_z_pos --> _00Ss
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01502__00Ss = _00Sr_constant+1*v01491_rel_obs_z_pos

# op _00Sx_power_combination_eval
# LANG: _00Sw --> _00Sy
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01505__00Sy = (v01504__00Sw**2)
v01505__00Sy = (v01505__00Sy*_00Sx_coeff).reshape((1, 1, 27))

# op _00dJ_power_combination_eval
# LANG: _00bU, _local_thrust --> _00dK
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0352__00dK = (v0325__local_thrust**1)*(v0320__00bU**-1)
v0352__00dK = (v0352__00dK*_00dJ_coeff).reshape((1, 40, 30))

# op _00dP_power_combination_eval
# LANG: _00dO --> _00dQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0356__00dQ = (v0355__00dO**2)
v0356__00dQ = (v0356__00dQ*_00dP_coeff).reshape((1, 40, 30))

# op _00dT_power_combination_eval
# LANG: _rotor_radius --> _00dU
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0358__00dU = (v0201__rotor_radius**1)
v0358__00dU = (v0358__00dU*_00dT_coeff).reshape((1, 40, 30))

# op _00eU_power_combination_eval
# LANG: _00eT, _radius --> _local_torque_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0418__local_torque_2 = (v0417__00eT**1)*(v0214__radius**1)
v0418__local_torque_2 = (v0418__local_torque_2*_00eU_coeff).reshape((1, 40, 30))

# op _00ew_power_combination_eval
# LANG: _00ev, _dr --> _local_thrust_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0370__local_thrust_2 = (v0369__00ev**1)*(v0202__dr**1)
v0370__local_thrust_2 = (v0370__local_thrust_2*_00ew_coeff).reshape((1, 40, 30))

# op _00fT_power_combination_eval
# LANG: _00fI, _00fS --> _00fU
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0399__00fU = (v0398__00fI**1)*(v0401__00fS**1)
v0399__00fU = (v0399__00fU*_00fT_coeff).reshape((1, 40, 30))

# op _00fx_power_combination_eval
# LANG: _00fm, _00fw --> _00fy
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0332__00fy = (v0331__00fm**1)*(v0334__00fw**1)
v0332__00fy = (v0332__00fy*_00fx_coeff).reshape((1, 40, 30))

# op _00gW_power_combination_eval
# LANG: _00gV, prandtl_loss_factor --> _00gX
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0434__00gX = (v0423__00gV**1)*(v0264_prandtl_loss_factor**1)
v0434__00gX = (v0434__00gX*_00gW_coeff).reshape((1, 40, 30))

# op _00gq_power_combination_eval
# LANG: _00gp, _dr --> _local_thrust_star
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0390__local_thrust_star = (v0389__00gp**1)*(v0202__dr**1)
v0390__local_thrust_star = (v0390__local_thrust_star*_00gq_coeff).reshape((1, 40, 30))

# op _00hN_power_combination_eval
# LANG: _00hC, _00hM --> C_Q
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0457_C_Q = (v0452__00hC**1)*(v0462__00hM**-1)
v0457_C_Q = (v0457_C_Q*_00hN_coeff).reshape((1,))

# op _00i0_power_combination_eval
# LANG: _00h_ --> J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0470_J = (v0469__00h_**1)
v0470_J = (v0470_J*_00i0_coeff).reshape((1,))

# op _00i8_power_combination_eval
# LANG: _00i7 --> _00i9
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0474__00i9 = (v0473__00i7**0.5)
v0474__00i9 = (v0474__00i9*_00i8_coeff).reshape((1,))

# op _00kh_indexed_passthrough_eval
# LANG: _00kg, _00km, _00kr --> F
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0522_F__temp[i_v0518__00kg__00kh_indexed_passthrough_eval] = v0518__00kg.flatten()
v0522_F = v0522_F__temp.copy()
v0522_F__temp[i_v0524__00km__00kh_indexed_passthrough_eval] = v0524__00km.flatten()
v0522_F = v0522_F__temp.copy()
v0522_F__temp[i_v0526__00kr__00kh_indexed_passthrough_eval] = v0526__00kr.flatten()
v0522_F = v0522_F__temp.copy()

# op _00ks_linear_combination_eval
# LANG: thrust_origin, reference_point --> _00kt
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0527__00kt = _00ks_constant+1*v0502_thrust_origin+-1*v0528_reference_point

# op _00sM_power_combination_eval
# LANG: _00qX, _local_thrust --> _00sN
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0725__00sN = (v0698__local_thrust**1)*(v0693__00qX**-1)
v0725__00sN = (v0725__00sN*_00sM_coeff).reshape((1, 40, 30))

# op _00sS_power_combination_eval
# LANG: _00sR --> _00sT
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0729__00sT = (v0728__00sR**2)
v0729__00sT = (v0729__00sT*_00sS_coeff).reshape((1, 40, 30))

# op _00sW_power_combination_eval
# LANG: _rotor_radius --> _00sX
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0731__00sX = (v0574__rotor_radius**1)
v0731__00sX = (v0731__00sX*_00sW_coeff).reshape((1, 40, 30))

# op _00tX_power_combination_eval
# LANG: _00tW, _radius --> _local_torque_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0791__local_torque_2 = (v0790__00tW**1)*(v0587__radius**1)
v0791__local_torque_2 = (v0791__local_torque_2*_00tX_coeff).reshape((1, 40, 30))

# op _00tz_power_combination_eval
# LANG: _00ty, _dr --> _local_thrust_2
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0743__local_thrust_2 = (v0742__00ty**1)*(v0575__dr**1)
v0743__local_thrust_2 = (v0743__local_thrust_2*_00tz_coeff).reshape((1, 40, 30))

# op _00uA_power_combination_eval
# LANG: _00up, _00uz --> _00uB
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0705__00uB = (v0704__00up**1)*(v0707__00uz**1)
v0705__00uB = (v0705__00uB*_00uA_coeff).reshape((1, 40, 30))

# op _00uW_power_combination_eval
# LANG: _00uL, _00uV --> _00uX
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0772__00uX = (v0771__00uL**1)*(v0774__00uV**1)
v0772__00uX = (v0772__00uX*_00uW_coeff).reshape((1, 40, 30))

# op _00vZ_power_combination_eval
# LANG: _00vY, prandtl_loss_factor --> _00v_
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0807__00v_ = (v0796__00vY**1)*(v0637_prandtl_loss_factor**1)
v0807__00v_ = (v0807__00v_*_00vZ_coeff).reshape((1, 40, 30))

# op _00vt_power_combination_eval
# LANG: _00vs, _dr --> _local_thrust_star
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0763__local_thrust_star = (v0762__00vs**1)*(v0575__dr**1)
v0763__local_thrust_star = (v0763__local_thrust_star*_00vt_coeff).reshape((1, 40, 30))

# op _00wQ_power_combination_eval
# LANG: _00wF, _00wP --> C_Q
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0830_C_Q = (v0825__00wF**1)*(v0835__00wP**-1)
v0830_C_Q = (v0830_C_Q*_00wQ_coeff).reshape((1,))

# op _00x3_power_combination_eval
# LANG: _00x2 --> J
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0843_J = (v0842__00x2**1)
v0843_J = (v0843_J*_00x3_coeff).reshape((1,))

# op _00xb_power_combination_eval
# LANG: _00xa --> _00xc
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0847__00xc = (v0846__00xa**0.5)
v0847__00xc = (v0847__00xc*_00xb_coeff).reshape((1,))

# op _00zc_power_combination_eval
# LANG: _00zb --> _00zd
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0901__00zd = (v0900__00zb**1)
v0901__00zd = (v0901__00zd*_00zc_coeff).reshape((1,))

# op _013d arccos_eval
# LANG: _013c --> _013e
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01866__013e = np.arccos(v01865__013c)

# op _013f_linear_combination_eval
# LANG: rel_obs_z_pos --> _013g
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01868__013g = _013f_constant+1*v01857_rel_obs_z_pos

# op _013l_power_combination_eval
# LANG: _013k --> _013m
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01871__013m = (v01870__013k**2)
v01871__013m = (v01871__013m*_013l_coeff).reshape((1, 1, 27))

# op _0160_single_tensor_sum_with_axis_eval
# LANG: _015_ --> _0161
# SHAPES: (4, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01948__0161 = np.sum(v01947__015_, axis = (0,)).reshape((1, 27))

# op _016o_single_tensor_sum_with_axis_eval
# LANG: _016n --> _016p
# SHAPES: (4, 1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01958__016p = np.sum(v01957__016n, axis = (0,)).reshape((1, 27))

# op _0017_indexed_passthrough_eval
# LANG: _0016, _001l, _001x, _001J, _001V, _0026, _002i --> temp_density
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v049_temp_density__temp[i_v048__0016__0017_indexed_passthrough_eval] = v048__0016.flatten()
v049_temp_density = v049_temp_density__temp.copy()
v049_temp_density__temp[i_v051__001l__0017_indexed_passthrough_eval] = v051__001l.flatten()
v049_temp_density = v049_temp_density__temp.copy()
v049_temp_density__temp[i_v053__001x__0017_indexed_passthrough_eval] = v053__001x.flatten()
v049_temp_density = v049_temp_density__temp.copy()
v049_temp_density__temp[i_v055__001J__0017_indexed_passthrough_eval] = v055__001J.flatten()
v049_temp_density = v049_temp_density__temp.copy()
v049_temp_density__temp[i_v057__001V__0017_indexed_passthrough_eval] = v057__001V.flatten()
v049_temp_density = v049_temp_density__temp.copy()
v049_temp_density__temp[i_v059__0026__0017_indexed_passthrough_eval] = v059__0026.flatten()
v049_temp_density = v049_temp_density__temp.copy()
v049_temp_density__temp[i_v061__002i__0017_indexed_passthrough_eval] = v061__002i.flatten()
v049_temp_density = v049_temp_density__temp.copy()

# op _001c_indexed_passthrough_eval
# LANG: _001b, _001p, _001B, _001N, _001Z, _002a, _002m --> temp_pressure
# SHAPES: (1,), (1,), (1,), (1,), (1,), (1,), (1,) --> (7,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v064_temp_pressure__temp[i_v063__001b__001c_indexed_passthrough_eval] = v063__001b.flatten()
v064_temp_pressure = v064_temp_pressure__temp.copy()
v064_temp_pressure__temp[i_v066__001p__001c_indexed_passthrough_eval] = v066__001p.flatten()
v064_temp_pressure = v064_temp_pressure__temp.copy()
v064_temp_pressure__temp[i_v068__001B__001c_indexed_passthrough_eval] = v068__001B.flatten()
v064_temp_pressure = v064_temp_pressure__temp.copy()
v064_temp_pressure__temp[i_v070__001N__001c_indexed_passthrough_eval] = v070__001N.flatten()
v064_temp_pressure = v064_temp_pressure__temp.copy()
v064_temp_pressure__temp[i_v072__001Z__001c_indexed_passthrough_eval] = v072__001Z.flatten()
v064_temp_pressure = v064_temp_pressure__temp.copy()
v064_temp_pressure__temp[i_v074__002a__001c_indexed_passthrough_eval] = v074__002a.flatten()
v064_temp_pressure = v064_temp_pressure__temp.copy()
v064_temp_pressure__temp[i_v076__002m__001c_indexed_passthrough_eval] = v076__002m.flatten()
v064_temp_pressure = v064_temp_pressure__temp.copy()

# op _002D_power_combination_eval
# LANG: _002C --> _002E
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v098__002E = (v097__002C**1)
v098__002E = (v098__002E*_002D_coeff).reshape((1,))

# op _002F_linear_combination_eval
# LANG: hover_temperature --> _002G
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0100__002G = _002F_constant+1*v092_hover_temperature

# op _002J_power_combination_eval
# LANG: hover_temperature --> _002K
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0101__002K = (v092_hover_temperature**1)
v0101__002K = (v0101__002K*_002J_coeff).reshape((1,))

# op _002Y_power_combination_eval
# LANG: _002P --> p
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v036_p = (v030__002P**1)
v036_p = (v036_p*_002Y_coeff).reshape((1,))

# op _002__power_combination_eval
# LANG: _002P --> q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v037_q = (v030__002P**1)
v037_q = (v037_q*_002__coeff).reshape((1,))

# op _0031_power_combination_eval
# LANG: _002P --> r
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v038_r = (v030__002P**1)
v038_r = (v038_r*_0031_coeff).reshape((1,))

# op _005r cross_product_eval
# LANG: F, _005q --> _005s
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0156__005s = np.cross(v0154__005q, v0149_F, axisa = 1, axisb = 1, axisc = 1)

# op _00AO_power_combination_eval
# LANG: _00AL, _00AN --> _00AP
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0955__00AP = (v0954__00AL**1)*(v0956__00AN**1)
v0955__00AP = (v0955__00AP*_00AO_coeff).reshape((1, 1, 27))

# op _00AU_power_combination_eval
# LANG: _00AT --> _00AV
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0960__00AV = (v0959__00AT**0.5)
v0960__00AV = (v0960__00AV*_00AU_coeff).reshape((1, 1, 27))

# op _00MC_power_combination_eval
# LANG: _00Mz, _00MB --> _00MD
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01321__00MD = (v01320__00Mz**1)*(v01322__00MB**1)
v01321__00MD = (v01321__00MD*_00MC_coeff).reshape((1, 1, 27))

# op _00MI_power_combination_eval
# LANG: _00MH --> _00MJ
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01326__00MJ = (v01325__00MH**0.5)
v01326__00MJ = (v01326__00MJ*_00MI_coeff).reshape((1, 1, 27))

# op _00QU_power_combination_eval
# LANG: _00QT --> _00QV
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01448__00QV = (v01447__00QT**1)
v01448__00QV = (v01448__00QV*_00QU_coeff).reshape((1,))

# op _00QW_linear_combination_eval
# LANG: temperature --> _00QX
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01450__00QX = _00QW_constant+1*v01439_temperature

# op _00St_power_combination_eval
# LANG: _00Sq, _00Ss --> _00Su
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01501__00Su = (v01500__00Sq**1)*(v01502__00Ss**1)
v01501__00Su = (v01501__00Su*_00St_coeff).reshape((1, 1, 27))

# op _00Sz_power_combination_eval
# LANG: _00Sy --> _00SA
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01506__00SA = (v01505__00Sy**0.5)
v01506__00SA = (v01506__00SA*_00Sz_coeff).reshape((1, 1, 27))

# op _00dR_power_combination_eval
# LANG: _00dK, _00dQ --> _00dS
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0353__00dS = (v0352__00dK**1)*(v0356__00dQ**-1)
v0353__00dS = (v0353__00dS*_00dR_coeff).reshape((1, 40, 30))

# op _00dV_power_combination_eval
# LANG: _00dU --> _00dW
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0359__00dW = (v0358__00dU**4)
v0359__00dW = (v0359__00dW*_00dV_coeff).reshape((1, 40, 30))

# op _00fV_power_combination_eval
# LANG: _00fU, _chord --> _00fW
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0405__00fW = (v0399__00fU**1)*(v0209__chord**1)
v0405__00fW = (v0405__00fW*_00fV_coeff).reshape((1, 40, 30))

# op _00fZ_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_2 --> _00f_
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0371__00f_ = np.sum(v0370__local_thrust_2, axis = (1, 2)).reshape((1,))

# op _00fz_power_combination_eval
# LANG: _00fy, _chord --> _00fA
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0338__00fA = (v0332__00fy**1)*(v0209__chord**1)
v0338__00fA = (v0338__00fA*_00fz_coeff).reshape((1, 40, 30))

# op _00g2_single_tensor_sum_with_axis_eval
# LANG: _local_torque_2 --> _00g3
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0419__00g3 = np.sum(v0418__local_torque_2, axis = (1, 2)).reshape((1,))

# op _00gY_power_combination_eval
# LANG: _00gX, _dr --> _local_energy_loss
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0435__local_energy_loss = (v0434__00gX**1)*(v0202__dr**1)
v0435__local_energy_loss = (v0435__local_energy_loss*_00gY_coeff).reshape((1, 40, 30))

# op _00gs_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_star --> _00gt
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0391__00gt = np.sum(v0390__local_thrust_star, axis = (1, 2)).reshape((1,))

# op _00hP_power_combination_eval
# LANG: C_Q --> C_P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0463_C_P = (v0457_C_Q**1)
v0463_C_P = (v0463_C_P*_00hP_coeff).reshape((1,))

# op _00i2_power_combination_eval
# LANG: C_T, J --> _00i3
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0464__00i3 = (v0445_C_T**1)*(v0470_J**1)
v0464__00i3 = (v0464__00i3*_00i2_coeff).reshape((1,))

# op _00ia_power_combination_eval
# LANG: C_T, _00i9 --> _00ib
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0472__00ib = (v0445_C_T**1)*(v0474__00i9**1)
v0472__00ib = (v0472__00ib*_00ia_coeff).reshape((1,))

# op _00ku cross_product_eval
# LANG: F, _00kt --> _00kv
# SHAPES: (1, 3), (1, 3) --> (1, 3)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0529__00kv = np.cross(v0527__00kt, v0522_F, axisa = 1, axisb = 1, axisc = 1)

# op _00sU_power_combination_eval
# LANG: _00sN, _00sT --> _00sV
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0726__00sV = (v0725__00sN**1)*(v0729__00sT**-1)
v0726__00sV = (v0726__00sV*_00sU_coeff).reshape((1, 40, 30))

# op _00sY_power_combination_eval
# LANG: _00sX --> _00sZ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0732__00sZ = (v0731__00sX**4)
v0732__00sZ = (v0732__00sZ*_00sY_coeff).reshape((1, 40, 30))

# op _00uC_power_combination_eval
# LANG: _00uB, _chord --> _00uD
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0711__00uD = (v0705__00uB**1)*(v0582__chord**1)
v0711__00uD = (v0711__00uD*_00uC_coeff).reshape((1, 40, 30))

# op _00uY_power_combination_eval
# LANG: _00uX, _chord --> _00uZ
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0778__00uZ = (v0772__00uX**1)*(v0582__chord**1)
v0778__00uZ = (v0778__00uZ*_00uY_coeff).reshape((1, 40, 30))

# op _00v1_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_2 --> _00v2
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0744__00v2 = np.sum(v0743__local_thrust_2, axis = (1, 2)).reshape((1,))

# op _00v5_single_tensor_sum_with_axis_eval
# LANG: _local_torque_2 --> _00v6
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0792__00v6 = np.sum(v0791__local_torque_2, axis = (1, 2)).reshape((1,))

# op _00vv_single_tensor_sum_with_axis_eval
# LANG: _local_thrust_star --> _00vw
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0764__00vw = np.sum(v0763__local_thrust_star, axis = (1, 2)).reshape((1,))

# op _00w0_power_combination_eval
# LANG: _00v_, _dr --> _local_energy_loss
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0808__local_energy_loss = (v0807__00v_**1)*(v0575__dr**1)
v0808__local_energy_loss = (v0808__local_energy_loss*_00w0_coeff).reshape((1, 40, 30))

# op _00wS_power_combination_eval
# LANG: C_Q --> C_P
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0836_C_P = (v0830_C_Q**1)
v0836_C_P = (v0836_C_P*_00wS_coeff).reshape((1,))

# op _00x5_power_combination_eval
# LANG: C_T, J --> _00x6
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0837__00x6 = (v0818_C_T**1)*(v0843_J**1)
v0837__00x6 = (v0837__00x6*_00x5_coeff).reshape((1,))

# op _00xd_power_combination_eval
# LANG: C_T, _00xc --> _00xe
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0845__00xe = (v0818_C_T**1)*(v0847__00xc**1)
v0845__00xe = (v0845__00xe*_00xd_coeff).reshape((1,))

# op _00ze_power_combination_eval
# LANG: _00zd --> _00zf
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0902__00zf = (v0901__00zd**1)
v0902__00zf = (v0902__00zf*_00ze_coeff).reshape((1,))

# op _00zg_linear_combination_eval
# LANG: temperature --> _00zh
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0904__00zh = _00zg_constant+1*v0893_temperature

# op _013h_power_combination_eval
# LANG: _013e, _013g --> _013i
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01867__013i = (v01866__013e**1)*(v01868__013g**1)
v01867__013i = (v01867__013i*_013h_coeff).reshape((1, 1, 27))

# op _013n_power_combination_eval
# LANG: _013m --> _013o
# SHAPES: (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01872__013o = (v01871__013m**0.5)
v01872__013o = (v01872__013o*_013n_coeff).reshape((1, 1, 27))

# op _0162_log10_eval
# LANG: _0161 --> _0163
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01949__0163 = np.log10(v01948__0161)

# op _016q_log10_eval
# LANG: _016p --> _016r
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01959__016r = np.log10(v01958__016p)

# op _0001_power_combination_eval
# LANG: caddee_test_input --> caddee_test_output
# SHAPES: (1,) --> (1,)
# full namespace: 
v02_caddee_test_output = (v01_caddee_test_input**1)
v02_caddee_test_output = (v02_caddee_test_output*_0001_coeff).reshape((1,))

# op _000Y_power_combination_eval
# LANG: hover_hover_time --> hover_time
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v029_hover_time = (v027_hover_hover_time**1)
v029_hover_time = (v029_hover_time*_000Y_coeff).reshape((1,))

# op _000d_power_combination_eval
# LANG: design_geometry --> design_geometry_0
# SHAPES: (32500, 3) --> (32500, 3)
# full namespace: system_representation.outputs_model.design_outputs_model
v06_design_geometry_0 = (v05_design_geometry**1)
v06_design_geometry_0 = (v06_design_geometry_0*_000d_coeff).reshape((32500, 3))

# op _002H_power_combination_eval
# LANG: _002E, _002G --> hover_dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v099_hover_dynamic_viscosity = (v098__002E**1)*(v0100__002G**-1)
v099_hover_dynamic_viscosity = (v099_hover_dynamic_viscosity*_002H_coeff).reshape((1,))

# op _002L_power_combination_eval
# LANG: _002K --> hover_speed_of_sound
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v0102_hover_speed_of_sound = (v0101__002K**0.5)
v0102_hover_speed_of_sound = (v0102_hover_speed_of_sound*_002L_coeff).reshape((1,))

# op _002r single_tensor_sum_no_axis_eval
# LANG: temp_density --> hover_density
# SHAPES: (7,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v094_hover_density = np.sum(v049_temp_density).reshape((1,))

# op _002t single_tensor_sum_no_axis_eval
# LANG: temp_pressure --> hover_pressure
# SHAPES: (7,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation.atmosphere_model
v093_hover_pressure = np.sum(v064_temp_pressure).reshape((1,))

# op _0033_power_combination_eval
# LANG: _002P --> phi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v039_phi = (v030__002P**1)
v039_phi = (v039_phi*_0033_coeff).reshape((1,))

# op _0035_power_combination_eval
# LANG: _002P --> gamma
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v040_gamma = (v030__002P**1)
v040_gamma = (v040_gamma*_0035_coeff).reshape((1,))

# op _0037_power_combination_eval
# LANG: _002P --> psi
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v041_psi = (v030__002P**1)
v041_psi = (v041_psi*_0037_coeff).reshape((1,))

# op _003b_power_combination_eval
# LANG: _002P --> x
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v043_x = (v030__002P**1)
v043_x = (v043_x*_003b_coeff).reshape((1,))

# op _003d_power_combination_eval
# LANG: _002Q --> y
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v044_y = (v031__002Q**1)
v044_y = (v044_y*_003d_coeff).reshape((1,))

# op _003f_power_combination_eval
# LANG: _002R --> z
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.hover_ac_states_operation
v045_z = (v032__002R**1)
v045_z = (v045_z*_003f_coeff).reshape((1,))

# op _005F_power_combination_eval
# LANG: p --> p1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v036_p = v036_p.reshape((1, 1))
v0168_p1 = (v036_p**1)
v0168_p1 = (v0168_p1*_005F_coeff).reshape((1, 1))
v036_p = v036_p.reshape((1,))

# op _005I_power_combination_eval
# LANG: q --> q1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v037_q = v037_q.reshape((1, 1))
v0169_q1 = (v037_q**1)
v0169_q1 = (v0169_q1*_005I_coeff).reshape((1, 1))
v037_q = v037_q.reshape((1,))

# op _005L_power_combination_eval
# LANG: r --> r1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.BEM_external_inputs_model
v038_r = v038_r.reshape((1, 1))
v0170_r1 = (v038_r**1)
v0170_r1 = (v0170_r1*_005L_coeff).reshape((1, 1))
v038_r = v038_r.reshape((1,))

# op _005t_transpose_eval
# LANG: _005s --> M
# SHAPES: (1, 3) --> (3, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model
v0157_M = np.transpose(v0156__005s)

# op _00AW_power_combination_eval
# LANG: _00AP, _00AV --> rel_obs_angle
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.steady_observer_location_model
v0957_rel_obs_angle = (v0955__00AP**1)*(v0960__00AV**-1)
v0957_rel_obs_angle = (v0957_rel_obs_angle*_00AW_coeff).reshape((1, 1, 27))

# op _00MK_power_combination_eval
# LANG: _00MD, _00MJ --> rel_obs_angle
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_GL_broadband_model.steady_observer_location_model
v01323_rel_obs_angle = (v01321__00MD**1)*(v01326__00MJ**-1)
v01323_rel_obs_angle = (v01323_rel_obs_angle*_00MK_coeff).reshape((1, 1, 27))

# op _00QY_power_combination_eval
# LANG: _00QV, _00QX --> dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.atmosphere_model
v01449_dynamic_viscosity = (v01448__00QV**1)*(v01450__00QX**-1)
v01449_dynamic_viscosity = (v01449_dynamic_viscosity*_00QY_coeff).reshape((1,))

# op _00SB_power_combination_eval
# LANG: _00Su, _00SA --> rel_obs_angle
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_KS_tonal_model.steady_observer_location_model
v01503_rel_obs_angle = (v01501__00Su**1)*(v01506__00SA**-1)
v01503_rel_obs_angle = (v01503_rel_obs_angle*_00SB_coeff).reshape((1, 1, 27))

# op _00dX_power_combination_eval
# LANG: _00dS, _00dW --> dC_T
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0357_dC_T = (v0353__00dS**1)*(v0359__00dW**-1)
v0357_dC_T = (v0357_dC_T*_00dX_coeff).reshape((1, 40, 30))

# op _00fB_power_combination_eval
# LANG: _00fA, _dr --> _local_thrust_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0339__local_thrust_induced = (v0338__00fA**1)*(v0202__dr**1)
v0339__local_thrust_induced = (v0339__local_thrust_induced*_00fB_coeff).reshape((1, 40, 30))

# op _00fX_power_combination_eval
# LANG: _00fW, _dr --> _local_torque_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0406__local_torque_induced = (v0405__00fW**1)*(v0202__dr**1)
v0406__local_torque_induced = (v0406__local_torque_induced*_00fX_coeff).reshape((1, 40, 30))

# op _00g0_power_combination_eval
# LANG: _00f_ --> total_thrust_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0372_total_thrust_2 = (v0371__00f_**1)
v0372_total_thrust_2 = (v0372_total_thrust_2*_00g0_coeff).reshape((1,))

# op _00g4_power_combination_eval
# LANG: _00g3 --> total_torque_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0420_total_torque_2 = (v0419__00g3**1)
v0420_total_torque_2 = (v0420_total_torque_2*_00g4_coeff).reshape((1,))

# op _00g__single_tensor_sum_with_axis_eval
# LANG: _local_energy_loss --> total_energy_loss
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0436_total_energy_loss = np.sum(v0435__local_energy_loss, axis = (1, 2)).reshape((1,))

# op _00gu_power_combination_eval
# LANG: _00gt --> total_thrust_star
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0392_total_thrust_star = (v0391__00gt**1)
v0392_total_thrust_star = (v0392_total_thrust_star*_00gu_coeff).reshape((1,))

# op _00i4_power_combination_eval
# LANG: C_P, _00i3 --> eta
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0471_eta = (v0464__00i3**1)*(v0463_C_P**-1)
v0471_eta = (v0471_eta*_00i4_coeff).reshape((1,))

# op _00ic_power_combination_eval
# LANG: C_P, _00ib --> FOM
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0475_FOM = (v0472__00ib**1)*(v0463_C_P**-1)
v0475_FOM = (v0475_FOM*_00ic_coeff).reshape((1,))

# op _00ig_power_combination_eval
# LANG: total_torque --> Q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0351_Q = (v0350_total_torque**1)
v0351_Q = (v0351_Q*_00ig_coeff).reshape((1,))

# op _00ii_power_combination_eval
# LANG: _local_torque --> _dQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_bem_model.induced_velocity_model
v0393__dQ = (v0348__local_torque**1)
v0393__dQ = (v0393__dQ*_00ii_coeff).reshape((1, 40, 30))

# op _00kI_power_combination_eval
# LANG: p --> p1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v036_p = v036_p.reshape((1, 1))
v0541_p1 = (v036_p**1)
v0541_p1 = (v0541_p1*_00kI_coeff).reshape((1, 1))
v036_p = v036_p.reshape((1,))

# op _00kL_power_combination_eval
# LANG: q --> q1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v037_q = v037_q.reshape((1, 1))
v0542_q1 = (v037_q**1)
v0542_q1 = (v0542_q1*_00kL_coeff).reshape((1, 1))
v037_q = v037_q.reshape((1,))

# op _00kO_power_combination_eval
# LANG: r --> r1
# SHAPES: (1, 1) --> (1, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.BEM_external_inputs_model
v038_r = v038_r.reshape((1, 1))
v0543_r1 = (v038_r**1)
v0543_r1 = (v0543_r1*_00kO_coeff).reshape((1, 1))
v038_r = v038_r.reshape((1,))

# op _00kw_transpose_eval
# LANG: _00kv --> M
# SHAPES: (1, 3) --> (3, 1)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model
v0530_M = np.transpose(v0529__00kv)

# op _00s__power_combination_eval
# LANG: _00sV, _00sZ --> dC_T
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0730_dC_T = (v0726__00sV**1)*(v0732__00sZ**-1)
v0730_dC_T = (v0730_dC_T*_00s__coeff).reshape((1, 40, 30))

# op _00uE_power_combination_eval
# LANG: _00uD, _dr --> _local_thrust_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0712__local_thrust_induced = (v0711__00uD**1)*(v0575__dr**1)
v0712__local_thrust_induced = (v0712__local_thrust_induced*_00uE_coeff).reshape((1, 40, 30))

# op _00u__power_combination_eval
# LANG: _00uZ, _dr --> _local_torque_induced
# SHAPES: (1, 40, 30), (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0779__local_torque_induced = (v0778__00uZ**1)*(v0575__dr**1)
v0779__local_torque_induced = (v0779__local_torque_induced*_00u__coeff).reshape((1, 40, 30))

# op _00v3_power_combination_eval
# LANG: _00v2 --> total_thrust_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0745_total_thrust_2 = (v0744__00v2**1)
v0745_total_thrust_2 = (v0745_total_thrust_2*_00v3_coeff).reshape((1,))

# op _00v7_power_combination_eval
# LANG: _00v6 --> total_torque_2
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0793_total_torque_2 = (v0792__00v6**1)
v0793_total_torque_2 = (v0793_total_torque_2*_00v7_coeff).reshape((1,))

# op _00vx_power_combination_eval
# LANG: _00vw --> total_thrust_star
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0765_total_thrust_star = (v0764__00vw**1)
v0765_total_thrust_star = (v0765_total_thrust_star*_00vx_coeff).reshape((1,))

# op _00w2_single_tensor_sum_with_axis_eval
# LANG: _local_energy_loss --> total_energy_loss
# SHAPES: (1, 40, 30) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0809_total_energy_loss = np.sum(v0808__local_energy_loss, axis = (1, 2)).reshape((1,))

# op _00x7_power_combination_eval
# LANG: C_P, _00x6 --> eta
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0844_eta = (v0837__00x6**1)*(v0836_C_P**-1)
v0844_eta = (v0844_eta*_00x7_coeff).reshape((1,))

# op _00xf_power_combination_eval
# LANG: C_P, _00xe --> FOM
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0848_FOM = (v0845__00xe**1)*(v0836_C_P**-1)
v0848_FOM = (v0848_FOM*_00xf_coeff).reshape((1,))

# op _00xj_power_combination_eval
# LANG: total_torque --> Q
# SHAPES: (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0724_Q = (v0723_total_torque**1)
v0724_Q = (v0724_Q*_00xj_coeff).reshape((1,))

# op _00xl_power_combination_eval
# LANG: _local_torque --> _dQ
# SHAPES: (1, 40, 30) --> (1, 40, 30)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_bem_model.induced_velocity_model
v0766__dQ = (v0721__local_torque**1)
v0766__dQ = (v0766__dQ*_00xl_coeff).reshape((1, 40, 30))

# op _00zi_power_combination_eval
# LANG: _00zf, _00zh --> dynamic_viscosity
# SHAPES: (1,), (1,) --> (1,)
# full namespace: system_model.hover_test.hover.hover.rotor_1_disk_KS_tonal_model.atmosphere_model
v0903_dynamic_viscosity = (v0902__00zf**1)*(v0904__00zh**-1)
v0903_dynamic_viscosity = (v0903_dynamic_viscosity*_00zi_coeff).reshape((1,))

# op _013p_power_combination_eval
# LANG: _013i, _013o --> rel_obs_angle
# SHAPES: (1, 1, 27), (1, 1, 27) --> (1, 1, 27)
# full namespace: system_model.hover_test.hover.hover.rotor_2_disk_GL_broadband_model.steady_observer_location_model
v01869_rel_obs_angle = (v01867__013i**1)*(v01872__013o**-1)
v01869_rel_obs_angle = (v01869_rel_obs_angle*_013p_coeff).reshape((1, 1, 27))

# op _0164_power_combination_eval
# LANG: _0163 --> total_spl
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01950_total_spl = (v01949__0163**1)
v01950_total_spl = (v01950_total_spl*_0164_coeff).reshape((1, 27))

# op _016s_power_combination_eval
# LANG: _016r --> A_weighted_total_spl
# SHAPES: (1, 27) --> (1, 27)
# full namespace: system_model.hover_test.hover.hover.total_noise_model
v01960_A_weighted_total_spl = (v01959__016r**1)
v01960_A_weighted_total_spl = (v01960_A_weighted_total_spl*_016s_coeff).reshape((1, 27))