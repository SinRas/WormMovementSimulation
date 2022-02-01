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
    def __init__( self, bone_previous: BoneBase, bones_next: List[BoneBase] ) -> BoneBase:
        # Bones
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