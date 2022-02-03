# Modules
## Internal
from bone.bone import BoneBase
from neuron.neuron import NeuronBase
from segment.segment import SegmentBase
## External
import numpy as np
import matplotlib.pyplot as plt
from typing import Any




# Parameters

# Methods
def plot_segment( segment: SegmentBase, new_plot: bool = False ) -> Any:
    _s = 50
    # Plot
    if( new_plot ):
        plt.figure(figsize=(8,8))

    # Neurons Back
    for neuron, pos3d in zip(segment.neurons, segment.neurons_abs_pos):
        if( pos3d[2] < 0 ):
            plt.scatter(
                pos3d[0],
                pos3d[1],
                s=_s,
                c=neuron.color,
                alpha=neuron.glow,
                zorder=1
            )
    # Bones
    _base_pos = segment.bone.base_pos
    _tip_pose = segment.bone.tip_pos
    plt.plot(
        [_base_pos[0], _tip_pose[0]], [_base_pos[1], _tip_pose[1]],
        lw=5,
        label = segment.name,
        zorder=2
    )
    # Neurons Front
    for neuron, pos3d in zip(segment.neurons, segment.neurons_abs_pos):
        if( pos3d[2] >= 0 ):
            plt.scatter(
                pos3d[0],
                pos3d[1],
                s=_s*2,
                c=neuron.color,
                alpha=neuron.glow,
                zorder=3
            )
    return

# Classes


# Main
if __name__ == "__main__":
    dt = 0.1
    # Bone
    bone1 = BoneBase(None, [], 1.0)
    bone1.angles = np.zeros(2)
    bone1.velocity_angles = np.array([ np.pi/50, 0 ])
    bone1.velocity_rotation = np.pi/20

    bone2 = BoneBase(bone1, [], 1.0)
    bone2.angles = np.array([ np.pi/4, 0 ])
    bone2.velocity_angles = np.array([ -np.pi/50, 0 ])
    bone2.velocity_rotation = np.pi/5
    
    bone1.bones_next.append(bone2)
    bones = [ bone1, bone2 ]
    # bone1.rotation = np.pi/4
    # bone1.velocity_angles = np.pi * np.ones(2)
    # bone1.velocity_rotation = np.pi

    # Neurons
    neurons1 = [
        NeuronBase(
            np.random.rand(3)-np.array([0.0, 0.5, 0.5]),
            '#FF0000' if i%2 == 0 else '#0000FF'
        ) for i in range(30)
    ]
    neurons2 = [
        NeuronBase(
            np.array([0.25, 0.1, 0.1]),
            '#FF0000'
        ),
        NeuronBase(
            np.array([0.5, -0.1, 0.1]),
            '#00FF00'
        ),
        NeuronBase(
            np.array([0.75, 0.2, -0.2]),
            '#0000FF'
        ),
    ]
    
    # Segment
    segment1 = SegmentBase(name="segment1", bone=bone1, neurons=neurons1)
    segment2 = SegmentBase(name="segment2", bone=bone2, neurons=neurons2)

    N = 300
    for i in range(N):
        if (i+1)%30 == 0:
            bone1.accelaration_angles = (np.random.rand(2)-0.5)/10
            bone2.accelaration_angles = (np.random.rand(2)-0.5)/10
        plt.figure(figsize=(8,8))
        plot_segment( segment1 )
        plot_segment( segment2 )
        plt.legend()
        plt.xlim(-1, 2.5)
        plt.ylim(-1, 2.5)
        plt.savefig(f'data/{str(i).zfill(2)}.png')
        plt.close()
        # Steps
        segment1.step(dt)
        segment2.step(dt)
        