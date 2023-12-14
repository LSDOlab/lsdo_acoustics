from lsdo_acoustics import Acoustics, Lowson, KS, SKM, GL, TotalAircraftNoise
import m3l
from typing import Union, List


def evaluate_multiple_acoustic_models(
    acoustics_data : Acoustics,
    tonal_noise_model : Union[Lowson, KS],
    broadband_noise_model : Union[GL, SKM],
    altitude : m3l.Variable,
    rotor_parameters,
    rotor_meshes : List[m3l.Variable],
    rpm_list: List[m3l.Variable],
    rotor_outputs : List[m3l.Variable],
    ac_states,
    model_name_prefix : str,
    num_nodes : int = 1,
    atmos=None,
    m3l_model : m3l.Model=None

) -> m3l.Variable:
    """
    Helper function to automate the creation of multiple acoustic models
    """

    if tonal_noise_model not in ['KS', 'Lowson']:
        raise ValueError(f"Unknown tonal noise model '{tonal_noise_model}'. Acceptable models are 'KS', 'Lowson'")
    
    if broadband_noise_model not in ['GL', 'SKM']:
        raise ValueError(f"Unknown tonal noise model '{broadband_noise_model}'. Acceptable models are 'GL', 'SKM'")
    
    if not isinstance(rpm_list, list):
        raise TypeError(f"'rpm_list'  and 'rotor_outputs' must be of type {type(list)}. Received '{type(rpm_list)}' and '{type(rotor_outputs)}'")
    else:
        if len(rpm_list) != len(rotor_outputs):
            raise ValueError(f"Number of sepcified rpms not equal to number of rotor_outputs")

    noise_componenents = []
    a_weighted_noise_componenents = []

    if not isinstance(rotor_parameters, list):
        rotor_parameters = [rotor_parameters] * len(rpm_list)

    for i in range(len(rpm_list)):
        # Tonal noise 
        if tonal_noise_model == 'KS':
            ks_model = KS(
                name=f"{model_name_prefix}_KS_{i}",
                num_nodes=num_nodes,
                rotor_parameters=rotor_parameters[i],
                acoustics_data=acoustics_data,
            )

            rotor_output = rotor_outputs[i]
            rpm = rpm_list[i]
            rotor_mesh = rotor_meshes[i]

            dT = rotor_output.dT
            dD = rotor_output.dD
            phi = rotor_output.phi
            thrust_origin = rotor_mesh.thrust_origin
            thrust_vector = rotor_mesh.thrust_vector
            radius = rotor_mesh.radius
            
            if rotor_mesh.chord_profile is None:
                chord_profile = rotor_output._chord_profile
            else:
                chord_profile = rotor_mesh.chord_profile


            ks_tonal_SPL, ks_tonal_SPL_A_weighted = ks_model.evaluate_tonal_noise(dT, dD, ac_states,
                                                                                   rpm=rpm, rotor_origin=thrust_origin,
                                                                                   thrust_vector=thrust_vector, 
                                                                                   rotor_radius=radius, altitude=altitude,
                                                                                   chord_length=chord_profile, phi_profile=phi,)
            
            noise_componenents.append(ks_tonal_SPL)
            a_weighted_noise_componenents.append(ks_tonal_SPL_A_weighted)

            if m3l_model:
                m3l_model.register_output(ks_tonal_SPL)
                m3l_model.register_output(ks_tonal_SPL_A_weighted)

        elif tonal_noise_model == 'Lowson':
            lowson_model = Lowson(
                name=f"{model_name_prefix}_lowson_{i}",
                num_nodes=num_nodes,
                rotor_parameters=rotor_parameters[i],
                acoustics_data=acoustics_data,
            )

            rotor_output = rotor_outputs[i]
            rpm = rpm_list[i]
            rotor_mesh = rotor_meshes[i]

            phi = rotor_output.phi
            dT = rotor_output.dT
            dD = rotor_output.dD
            thrust_origin = rotor_mesh.thrust_origin
            thrust_vector = rotor_mesh.thrust_vector
            radius = rotor_mesh.radius
            in_plane_ex = rotor_mesh.in_plane_2

            if rotor_mesh.chord_profile is None:
                chord_length = rotor_output._chord_profile
            
            else:
                chord_length = rotor_mesh.chord_profile

            lowson_tonal_SPL, lowson_tonal_SPL_A_weighted = lowson_model.evaluate_tonal_noise(dT, dD, ac_states,
                                                                                   rpm=rpm, rotor_origin=thrust_origin,
                                                                                   thrust_vector=thrust_vector, 
                                                                                   rotor_radius=radius, altitude=altitude,
                                                                                   in_plane_ex=in_plane_ex, phi_profile=phi,
                                                                                   chord_length=chord_length)
            
            noise_componenents.append(lowson_tonal_SPL)
            a_weighted_noise_componenents.append(lowson_tonal_SPL_A_weighted)

            if m3l_model:
                m3l_model.register_output(lowson_tonal_SPL)
                m3l_model.register_output(lowson_tonal_SPL_A_weighted)


        if broadband_noise_model == 'GL':
            gl_model = GL(
                name=f"{model_name_prefix}_GL_{i}",
                num_nodes=num_nodes,
                rotor_parameters=rotor_parameters[i],
                acoustics_data=acoustics_data,
            )

            rotor_output = rotor_outputs[i]
            rpm = rpm_list[i]
            rotor_mesh = rotor_meshes[i]

            C_T = rotor_output.C_T
            thrust_origin = rotor_mesh.thrust_origin
            thrust_vector = rotor_mesh.thrust_vector
            radius = rotor_mesh.radius
            # chord_length = rotor_mesh.chord_profile
            
            if rotor_mesh.chord_profile is None:
                chord_length = rotor_output._chord_profile
            
            else:
                chord_length = rotor_mesh.chord_profile

            GL_broadband_SPL, GL_broadband_SPL_A_weighted = gl_model.evaluate_broadband_noise(ac_states, C_T, rpm=rpm,
                                                                                           disk_origin=thrust_origin,
                                                                                           thrust_vector=thrust_vector,
                                                                                           radius=radius, chord_length=chord_length,
                                                                                           speed_of_sound=atmos.speed_of_sound)
    
            noise_componenents.append(GL_broadband_SPL)
            a_weighted_noise_componenents.append(GL_broadband_SPL_A_weighted)

            if m3l_model:
                m3l_model.register_output(GL_broadband_SPL)
                m3l_model.register_output(GL_broadband_SPL_A_weighted)

        elif broadband_noise_model == 'SKM':
            skm_model = SKM(
                name=f"{model_name_prefix}_SKM_{i}",
                num_nodes=num_nodes,
                rotor_parameters=rotor_parameters[i],
                acoustics_data=acoustics_data,
            )

            rotor_output = rotor_outputs[i]
            rpm = rpm_list[i]
            rotor_mesh = rotor_meshes[i]

            C_T = rotor_output.C_T
            thrust_origin = rotor_mesh.thrust_origin
            thrust_vector = rotor_mesh.thrust_vector
            radius = rotor_mesh.radius
            # chord_length = rotor_mesh.chord_profile

            if rotor_mesh.chord_profile is None:
                chord_length = rotor_output._chord_profile
            
            else:
                chord_length = rotor_mesh.chord_profile

            skm_broadband_SPL, skm_broadband_SPL_A_weighted = skm_model.evaluate_broadband_noise(ac_states, C_T, rpm=rpm,
                                                                                           disk_origin=thrust_origin,
                                                                                           thrust_vector=thrust_vector,
                                                                                           radius=radius, chord_length=chord_length)
    
            noise_componenents.append(skm_broadband_SPL)
            a_weighted_noise_componenents.append(skm_broadband_SPL_A_weighted)

            if m3l_model:
                m3l_model.register_output(skm_broadband_SPL)
                m3l_model.register_output(skm_broadband_SPL_A_weighted)

    
    total_noise_model = TotalAircraftNoise(
        name=model_name_prefix,
        acoustics_data=acoustics_data,
    )

    total_SPL, total_SPL_A_weighted = total_noise_model.evaluate(noise_components=noise_componenents, A_weighted_noise_components=a_weighted_noise_componenents)

    if m3l_model:
        m3l_model.register_output(total_SPL)
        m3l_model.register_output(total_SPL_A_weighted)

    return total_SPL, total_SPL_A_weighted