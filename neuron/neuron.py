# Modules
## External
from __future__ import annotations
from typing import List
import numpy as np

# Parameters

# Methods

# Classes
class NeuronBase:
    # Constructor
    def __init__(self, color: str) -> NeuronBase:
        # Color
        self.color = color
        # Glow
        self.glow_magnitude = 0.0
        self.glow_phase = 0.0
        self.glow_omega = 0.0
        #
        return
    # Step
    def step( self, dt: float ):
        self.glow_phase += dt * self.glow_omega
        #
        return
    # Glow
    @property
    def glow(self):
        return self.glow_magnitude * ( 1.0 + np.math.sin(self.glow_phase) )/2