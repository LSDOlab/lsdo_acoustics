import numpy as np
import csdl_alpha as csdl
from dataclasses import dataclass
from csdl_alpha.utils.typing import VariableLike, Variable
from typing import Union, Optional

from lsdo_acoustics.core.models.observer_location_model import steady_observer_location_model
from lsdo_acoustics.core.models.tonal.Lowson.load_integration_model import load_integration_model
from lsdo_acoustics.core.models.tonal.Lowson.lowson_spl_model import Lowson_spl_model
from lsdo_acoustics.core.models.tonal.Lowson.sears_function_model import Sears_function_model
from lsdo_acoustics.core.models.tonal.Barry_Magliozzi.thickness.BM_thickness_model import BM_thickness_model

from lsdo_acoustics.utils.a_weighting import A_weighting_function, A_weighting_function_new
from lsdo_acoustics.utils.csdl_switch import switch_func

@dataclass
class LowsonVariableGroup(csdl.VariableGroup):
    thrust_vector: VariableLike
    thrust_origin: VariableLike
    RPM: VariableLike
    speed_of_sound: VariableLike
    rotor_radius: VariableLike
    density: VariableLike
    
    num_radial: int
    num_tangential: int
    
    dD: Optional[VariableLike] = None
    dT: Optional[VariableLike] = None

    dDdR: Optional[VariableLike] = None
    dTdR: Optional[VariableLike] = None

    phi: Optional[VariableLike] = None
    lambda_i: Optional[VariableLike] = None

    chord_length: Optional[VariableLike] = None
    chord_profile: Optional[VariableLike] = None
    theta: Optional[VariableLike] = None # pitch angle

    mach_number: Optional[VariableLike] = None
    Vx: Optional[VariableLike] = None
    Vy: Optional[VariableLike] = None
    Vz: Optional[VariableLike] = None

    thickness_to_chord_ratio: Optional[VariableLike] = None
    nondim_sectional_radius: Optional[VariableLike] = None
    

    # def define_checks(self):
    #     self.add_check('thrust_vector', type=Union(Variable, np.ndarray))
    #     self.add_check('thrust_origin', type=Union(Variable, np.ndarray))

def Lowson_model(LowsonVariableGroup, observer_data, num_blades, num_nodes, modes=[1,2,3], A_weighting=False, toggle_thickness_noise=False, debug=False, use_geometry=False):

    num_observers = observer_data['num_observers']

    num_radial = LowsonVariableGroup.num_radial
    num_azim = LowsonVariableGroup.num_tangential

    test = debug

    rpm = LowsonVariableGroup.RPM

    a = LowsonVariableGroup.speed_of_sound
    if test or not use_geometry:
        propeller_radius = LowsonVariableGroup.rotor_radius
        chord_profile = LowsonVariableGroup.chord_profile
        thrust_dir = LowsonVariableGroup.thrust_vector
        thrust_origin = LowsonVariableGroup.thrust_origin

        M = LowsonVariableGroup.mach_number
        Vx = csdl.expand(M, (num_nodes,)) * a
        Vy = csdl.Variable(value=np.zeros(shape=Vx.shape))
        Vz = csdl.Variable(value=np.zeros(shape=Vx.shape))
    else:
        Vx = LowsonVariableGroup.Vx
        Vy = LowsonVariableGroup.Vy
        Vz = LowsonVariableGroup.Vz
        M = (Vx**2 + Vy**2 + Vz**2 + 1.e-12)**0.5 / a

        r = LowsonVariableGroup.rotor_radius
        propeller_radius = r
        thrust_origin = LowsonVariableGroup.thrust_origin
        chord_length = LowsonVariableGroup.chord_length
        chord_profile = chord_length

        # FINDING THRUST VECTOR DIRECTION
        theta = LowsonVariableGroup.theta
        rot_mat = csdl.Variable(shape=(3,3), value=0.)
        # ONLY CONSIDERING PITCH CHANGES (X-Z), NO YAW OR ROLL FOR NOW
        rot_mat = rot_mat.set(csdl.slice[1,1], value=1.)
        rot_mat = rot_mat.set(csdl.slice[0,0], value=csdl.cos(theta))
        rot_mat = rot_mat.set(csdl.slice[2,2], value=-1 * csdl.cos(theta))
        rot_mat = rot_mat.set(csdl.slice[0,2], value=-1 * csdl.sin(theta))
        rot_mat = rot_mat.set(csdl.slice[2,0], value=-1 * csdl.sin(theta))

        thrust_vec = LowsonVariableGroup.thrust_vector
        thrust_dir = csdl.matvec(rot_mat, thrust_vec/csdl.expand(csdl.norm(thrust_vec), shape=(3,)))

    velocity = csdl.Variable(shape=(num_nodes, 3), value=0.)
    velocity = velocity.set(csdl.slice[:,0], value=Vx)
    velocity = velocity.set(csdl.slice[:,1], value=Vy)
    velocity = velocity.set(csdl.slice[:,2], value=Vz)
    
    rel_obs_position, rel_obs_dist, rel_angle_plane, rel_angle_normal = steady_observer_location_model(
        num_nodes=num_nodes,
        observer_data=observer_data,
        rotor_origin=thrust_origin,
        thrust_vector=thrust_dir,
        velocity=velocity
    )

    norm_hub_rad = 0.2
    dr = (1 - norm_hub_rad) * propeller_radius / (num_radial-1)
    if LowsonVariableGroup.nondim_sectional_radius is None:
        nondim_sectional_radius = np.linspace(0.2, 1., num_radial)
    else:
        nondim_sectional_radius = LowsonVariableGroup.nondim_sectional_radius

    num_observers = observer_data['num_observers']

    # region Load integration
    if LowsonVariableGroup.dD is None:
        dD = np.ones((num_nodes, num_radial, num_azim))
        dT = np.ones((num_nodes, num_radial, num_azim))
    else:
        dD = LowsonVariableGroup.dD
        dT = LowsonVariableGroup.dT
    load_integration_inputs = {
        'dD': dD,
        'dT': dT,
    }
    aT, aD, bT, bD = load_integration_model(
        load_integration_inputs=load_integration_inputs,
        num_nodes=num_nodes,
        num_blades=num_blades,
        num_radial=num_radial,
        num_azim=num_azim
    )
    # endregion

    # region Sears function
    Sears_inputs = {
        'density': LowsonVariableGroup.density,
        'RPM': rpm,
        'propeller_radius': propeller_radius,
        'speed_of_sound': a,
        'chord_profile': chord_profile,
        'nondim_sectional_radius': nondim_sectional_radius,
    }  

    if test:
        Sears_inputs['_dTdR'] = LowsonVariableGroup.dTdR
        Sears_inputs['_dDdR'] = LowsonVariableGroup.dDdR
        Sears_inputs['lambda_i'] = LowsonVariableGroup.lambda_i
    else:
        Sears_inputs['dT'] = dT
        Sears_inputs['dD'] = dD
        Sears_inputs['phi'] = LowsonVariableGroup.phi
        Sears_inputs['dr'] = dr


    aT_Sears, aD_Sears, bT_Sears, bD_Sears = Sears_function_model(
        input_dict=Sears_inputs,
        num_nodes=num_nodes,
        num_blades=num_blades,
        num_radial=num_radial,
        num_azim=num_azim,
        modes=modes,
        test=test
    )
    # endregion

    # region SPL model
    unsteady_Lowson_inputs = {
        'a': a,
        'propeller_radius': propeller_radius,
        'nondim_sectional_radius': nondim_sectional_radius,
        'dr': dr,
        'rpm': rpm,
        'rel_obs_dist': rel_obs_dist,
        'rel_obs_position': rel_obs_position,
        'rel_obs_dist': rel_obs_dist,
        'thrust_dir': thrust_dir,
        'Vx': Vx,
        'Vy': Vy,
        'Vz': Vz,
        'aT_uns': aT,
        'aD_uns': aD,
        'bT_uns': bT,
        'bD_uns': bD,
        'aT_Sears': aT_Sears,
        'aD_Sears': aD_Sears,
        'bT_Sears': bT_Sears,
        'bD_Sears': bD_Sears,
    }
    spl_unsteady, spl_Sears, P_uns, P_Sears_s, P_Sears_uns = Lowson_spl_model(
        Lowson_inputs=unsteady_Lowson_inputs,
        num_nodes=num_nodes,
        num_observers=num_observers,
        B=num_blades,
        num_radial=num_radial,
        modes=modes,
    )
    # endregion

    # print(spl_unsteady.value)
    # print(spl_Sears.value)

    # region SPL smoothing
    V_inf = csdl.norm(velocity + 1.e-12, axes=(1,))

    if num_nodes == 1:
        V_inf_exp = csdl.expand(V_inf, (num_nodes, 3))
    else:
        V_inf_exp = csdl.expand(V_inf, (num_nodes, 3), 'i->ia')
    
    # V_dir = velocity / V_inf_exp # normalized flight direction vector
    V_dir = velocity

    thrust_dir_exp = csdl.expand(thrust_dir, (num_nodes, 3), 'i->ai')
    td_cross_V = csdl.cross(thrust_dir_exp, V_dir, axis=1) # should have max norm 1
    # print(V_dir.value)
    # print(thrust_dir_exp.value)
    # print(td_cross_V.value)
    # exit()
    td_cross_V_norm = csdl.norm(td_cross_V + 1.e-12, axes=(1,))
    target_shape = (num_nodes, num_observers)
    if num_nodes == 1:
        td_cross_V_norm_exp = csdl.expand(td_cross_V_norm, target_shape)
    else:
        td_cross_V_norm_exp = csdl.expand(td_cross_V_norm, target_shape, 'i->ia')

    # print(td_cross_V_norm_exp.value)
    funcs_list = [spl_Sears, spl_unsteady]
    bounds_list = [1.e-1]
    loading_noise = switch_func(
        x=td_cross_V_norm_exp,
        funcs_list=funcs_list,
        bounds_list=bounds_list,
        scale=100.
    )
    # print(loading_noise.value)
    # exit()
    # endregion

    if toggle_thickness_noise:
        # region BM thickness noise
        BM_inputs = {
            'rho': LowsonVariableGroup.density,
            'mach_number': M,
            'speed_of_sound': a,
            'rpm': rpm,
            'rel_obs_position': rel_obs_position,
            'thrust_dir': thrust_dir,
            'rel_obs_dist': rel_obs_dist,
            'thickness_to_chord_ratio': LowsonVariableGroup.thickness_to_chord_ratio,
            'chord_profile': chord_profile,
            'propeller_radius': propeller_radius,
            'dr': dr,
            'nondim_sectional_radius': nondim_sectional_radius,

        }
        thickness_noise, PmT_per_mode = BM_thickness_model(
            BM_inputs=BM_inputs,
            num_nodes=num_nodes,
            num_blades=num_blades,
            num_observers=num_observers,
            num_radial=num_radial
        )
        # endregion

        Lowson_spl = 10*csdl.log(
            csdl.power(10., loading_noise/10.) + csdl.power(10., thickness_noise/10.),
            base=10.
        )
    else:
        Lowson_spl = loading_noise

    # region A_weighting
    if A_weighting:
        BPF = 1. * rpm * num_blades/ 60.
        # Lowson_spl_dBA = A_weighting_function(SPL=Lowson_spl, f=BPF)

        dBA_unsteady = A_weighting_function_new(P_mag=P_uns, fm=BPF)

        ex = csdl.power(10., dBA_unsteady/10.)
        ex_sum = csdl.sum(ex, axes=(3,))
        SPL_m = 10.*csdl.log(ex_sum, base=10.)
        spl_unsteady_dBA = 10*csdl.log(csdl.sum(csdl.power(10.,SPL_m/10.), axes=(2,)), base=10.) # SHAPE IS (num_nodes, num_observers)

        dBA_Sears_s = A_weighting_function_new(P_mag=P_Sears_s, fm=BPF)
        dBA_Sears_uns = A_weighting_function_new(P_mag=P_Sears_uns, fm=BPF)

        SPL_per_mode_per_blade = 10*csdl.log(
            csdl.power(10., dBA_Sears_s/10.) + csdl.power(10., dBA_Sears_uns/10.),
            base=10.
        )
        SPL_m = csdl.reshape(SPL_per_mode_per_blade[:,:,:,0], (num_nodes, num_observers, len(modes)))
        spl_Sears_dBA = 10*csdl.log(csdl.sum(csdl.power(10.,SPL_m/10.), axes=(2,)), base=10.) # SHAPE IS (num_nodes, num_observers)

        funcs_list = [spl_Sears_dBA, spl_unsteady_dBA]
        bounds_list = [1.e-1]
        loading_noise_dBA = switch_func(
            x=td_cross_V_norm_exp,
            funcs_list=funcs_list,
            bounds_list=bounds_list,
            scale=100.
        )

        if toggle_thickness_noise:
            dBA_thickness = A_weighting_function_new(P_mag=PmT_per_mode, fm=BPF)
            thickness_noise_dBA  = 10.*csdl.log(
                csdl.sum(
                    csdl.power(
                        10., 
                        dBA_thickness/10. + 1.e-6
                    ),
                    axes=(2,)
                ),
                base=10.
            )

            Lowson_spl_dBA = 10*csdl.log(
                csdl.power(10., loading_noise_dBA/10.) + csdl.power(10., thickness_noise_dBA/10.),
                base=10.
            )
            
        else:
            Lowson_spl_dBA = loading_noise

    # endregion

    if A_weighting:
        return Lowson_spl, Lowson_spl_dBA
    else:
        return Lowson_spl
        


'''
NOTES:
================ 01/30/2024: ================
The structure of the Lowson model will look as such:
- observer model
- Load integration model (with dT, dD)
- Sears function model (with dTdr, dDdr)
- SPL model for unsteady loads
- SPL model for steady loads
- Cross-product weighting between unsteady and steady loads

As discussed with Hyunjune, the unsteady and steady models use different inputs
There is also a different way to calculate SPL for the two.

'''