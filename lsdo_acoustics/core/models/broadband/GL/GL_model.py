import numpy as np
import csdl_alpha as csdl
from dataclasses import dataclass
from csdl_alpha.utils.typing import VariableLike, Variable
from typing import Union, Optional

from lsdo_acoustics.core.models.broadband.GL.gl_spl_model import GL_spl_model
from lsdo_acoustics.core.models.observer_location_model import steady_observer_location_model
from lsdo_acoustics.utils.a_weighting import A_weighting_function

@dataclass
class GLVariableGroup(csdl.VariableGroup):
    thrust_vector: VariableLike
    thrust_origin: VariableLike
    CT: VariableLike
    rotor_radius: VariableLike
    
    rpm: VariableLike
    speed_of_sound: VariableLike
    mesh: VariableLike = None

    num_radial: int = None
    num_tangential: int = None
    
    chord_length: Optional[VariableLike] = None
    chord_profile: Optional[VariableLike] = None
    theta: Optional[VariableLike] = None
    mach_number: Optional[VariableLike] = None
    Vx: Optional[VariableLike] = None
    Vy: Optional[VariableLike] = None
    Vz: Optional[VariableLike] = None
    

    # def define_checks(self):
    #     self.add_check('thrust_vector', type=Union(Variable, np.ndarray))
    #     self.add_check('thrust_origin', type=Union(Variable, np.ndarray))

def GL_model(GLVariableGroup, observer_data, num_blades, num_nodes, debug=False, use_geometry=False, A_weighting=False):
    freq_band = np.array(
            [12.5, 16, 20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 
             500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000,
             10000, 12500, 16000, 20000,
             25000, 31500, 40000, 50000, 63000 # additional frequencies used by Hyunjune
             ])
    
    num_radial = GLVariableGroup.num_radial

    a = GLVariableGroup.speed_of_sound

    if debug or not use_geometry:
        propeller_radius = GLVariableGroup.rotor_radius
        chord_profile = GLVariableGroup.chord_profile
        thrust_dir = GLVariableGroup.thrust_vector
        thrust_origin = GLVariableGroup.thrust_origin

        M = GLVariableGroup.mach_number
        Vx = csdl.expand(M, (num_nodes,)) * a
        Vy = csdl.Variable(value=np.zeros(shape=Vx.shape))
        Vz = csdl.Variable(value=np.zeros(shape=Vx.shape))
    else:
        Vx = GLVariableGroup.Vx
        Vy = GLVariableGroup.Vy
        Vz = GLVariableGroup.Vz
        M = (Vx**2 + Vy**2 + Vz**2 + 1.e-12)**0.5 / a

        r = GLVariableGroup.rotor_radius
        propeller_radius = r
        thrust_origin = GLVariableGroup.thrust_origin
        chord_length = GLVariableGroup.chord_length
        chord_profile = chord_length

        # FINDING THRUST VECTOR DIRECTION
        theta = GLVariableGroup.theta
        rot_mat = csdl.Variable(shape=(3,3), value=0.)
        # ONLY CONSIDERING PITCH CHANGES (X-Z), NO YAW OR ROLL FOR NOW
        rot_mat = rot_mat.set(csdl.slice[1,1], value=1.)
        rot_mat = rot_mat.set(csdl.slice[0,0], value=csdl.cos(theta))
        rot_mat = rot_mat.set(csdl.slice[2,2], value=-1 * csdl.cos(theta))
        rot_mat = rot_mat.set(csdl.slice[0,2], value=-1 * csdl.sin(theta))
        rot_mat = rot_mat.set(csdl.slice[2,0], value=-1 * csdl.sin(theta))

        thrust_vec = GLVariableGroup.thrust_vector
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

    num_observers = observer_data['num_observers']

    rpm = GLVariableGroup.rpm
    CT = GLVariableGroup.CT

    inputs_dict = {
        'CT': CT,
        'chord_profile': chord_profile,
        'rel_obs_dist': rel_obs_dist,
        'rel_angle_plane': rel_angle_plane,
        'propeller_radius': propeller_radius,
        'dr': dr,
        'rpm': rpm,
        'speed_of_sound': a,
        'velocity': velocity

    }
    GL_spl = GL_spl_model(num_nodes, num_observers, num_blades, inputs_dict, frequency_band=freq_band)

    if A_weighting:
        BPF = 1. * rpm * num_blades/ 60.
        GL_spl_A_weighted = A_weighting_function(SPL=GL_spl, f=BPF)
        
        return GL_spl, GL_spl_A_weighted

    else:
        return GL_spl