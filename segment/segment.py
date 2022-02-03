# Modules
## External
from __future__ import annotations
from typing import List
import numpy as np

from bone.bone import BoneBase
from neuron.neuron import NeuronBase

# Parameters

# Methods

# Classes
## Segment Base
class SegmentBase:
    # Constructor
    def __init__(self, bone: BoneBase, neurons: List[NeuronBase]) -> SegmentBase:
        # Parameters
        self.bone = bone
        self.neurons = neurons
        #
        return
    # Step
    def step( self, dt: float ):
        self.bone.step(dt)
        [ neuron.step(dt) for neuron in self.neurons ]
        #
        return
    # Neurons Absolute Pos
    @property
    def neurons_abs_pos( self ) -> List[np.ndarray]:
        bone_matrix_rotation = self.bone.matrix_rotation
        bone_rotation_angles = self.bone.rotation_angles
        bone_base_pos = self.bone.base_pos
        rotate = lambda arr: np.matmul(
            bone_rotation_angles,
            np.matmul(
                bone_matrix_rotation,
                arr
            )
        )
        return [
            bone_base_pos + rotate(neuron.pos_relative) for neuron in self.neurons
        ]