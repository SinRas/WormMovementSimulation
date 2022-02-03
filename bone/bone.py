# Modules
## External
from __future__ import annotations
from typing import List
import numpy as np

# Parameters
sin = np.math.sin
cos = np.math.cos

# Methods
## 3D Spatial Rotations
def general_rotation( a: float, b: float, g: float ) -> np.ndarray:
    return np.array([
        [ cos(a)*cos(b) , cos(a)*sin(b)*sin(g) - sin(a)*cos(g) , cos(a)*sin(b)*cos(g) + sin(a)*sin(g) ],
        [ sin(a)*cos(b) , sin(a)*sin(b)*sin(g) + cos(a)*cos(g) , sin(a)*sin(b)*cos(g) - cos(a)*sin(g) ],
        [ -sin(b)       , cos(b)*sin(g)                        , cos(b)*cos(g)                        ],
    ])

# Classes
## Bone Base
class BoneBase:
    # Constructor
    def __init__( self, bone_previous: BoneBase, bones_next: List[BoneBase], bone_width: float = 1.0 ) -> BoneBase:
        # Bones
        self.bone_width = bone_width
        self.bone_previous = bone_previous
        self.bones_next = bones_next
        # Positions
        self.angles = np.zeros(2)
        self.rotation = 0.0
        # Velocities
        self.velocity_angles = np.zeros(2)
        self.velocity_rotation = 0.0
        # Accelartions
        self.accelaration_angles = np.zeros(2)
        self.accelaration_rotation = 0.0
        #
        return
    # Step
    def step( self, dt: float ):
        # Apply Acceleration
        self.velocity_angles += dt * self.accelaration_angles
        self.velocity_rotation += dt * self.accelaration_rotation
        # Apply Velocities
        self.angles += dt * self.velocity_angles
        self.rotation += dt * self.velocity_rotation
        #
        return
    # Bone Tip
    @property
    def tip_pos( self ) -> np.ndarray:
        pos = self.base_pos + np.matmul(
            self.rotation_angles,
            np.array([ self.bone_width, 0, 0 ])
        )
        #
        return pos
    # Bone Tip
    @property
    def base_pos( self ) -> np.ndarray:
        return self.bone_previous.tip_pos if self.bone_previous else np.zeros(3)

    # Rotation Angles
    @property
    def rotation_angles( self ) -> np.ndarray:
        phi, theta = self.angles
        return general_rotation( phi, theta, 0.0 )
    @property
    def rotation_angles_inv( self ) -> np.ndarray:
        phi, theta = self.angles
        return general_rotation( -phi, -theta, 0.0 )
    # Matrix Rotation
    @property
    def matrix_rotation( self ) -> np.ndarray:
        gamma = self.rotation
        return general_rotation( 0.0, 0.0, gamma )