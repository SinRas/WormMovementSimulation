# Generate 3D Locomotion Data
This module is intended to create 2D video trajectories of 3D neuron structures, e.g. microscopy images of neuron activations inside a transparent body.

<img src="https://github.com/SinRas/WormMovementSimulation/blob/main/samples/sample_animation.gif?raw=true" alt="samples/sample_animation.gif" width="400" height="400" style="display: block;margin-left: auto;margin-right: auto;width: 50%;" />


# TODO
- [x] add base classes
- [x] add animation samples
- [ ] add exporting as .npz files, e.g. projected 2d image time series and individual neuron traces
- [ ] more realistic exporting, e.g. add noises/blurring to glow, observation and video quality
- [ ] add segment rotation smoothing, e.g. interpolate rotation angles between neighboring segments
- [ ] add realistic dynamics samples, e.g. accelerations that mimic real movements, glow spiking dynamics
- [ ] use real life structural examples, e.g. code to generate real worm neuron positions and mimic worm movements
- [ ] restructure base classes -> move positions/connections to segments rather than bones (or not!?)
