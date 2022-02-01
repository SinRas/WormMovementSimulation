# Modules
## External
from __future__ import annotations
from typing import List
import numpy as np

# Parameters

# Methods

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
    def tip_pos( self ) -> np.np.ndarray:
        phi, theta = self.angles
        gamma = self.rotation
        # Angles
        pos = self.bone_width * np.array([
            np.math.cos(phi) * np.math.cos(theta),
            np.math.sin(phi) * np.math.cos(theta),
            np.math.sin(theta),
        ])
        # Rotation
        mat_rot = np.array([
            [ 1, 0, 0 ],
            [ 0, np.math.cos(gamma), -np.math.sin(gamma) ],
            [ 0, np.math.sin(gamma), np.math.cos(gamma) ],
        ])
        pos = np.matmul( mat_rot, pos )
        #
        return pos