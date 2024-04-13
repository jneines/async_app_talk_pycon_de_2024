# The motor driven telescope

Yes, there are star trackers available already. I wanted to know what it takes to build one myself.

:::{image} ./images/telescope.gif
:height: 480px
:align: center
:::

- Have stepper motor attached to telescope axis
- Atache a stepper motor controller to a Raspberry Pi
- Use Python app to drive stepper motor based on commands received via redis
- Use gamepad to steer motor using buttons for 'on', 'off' and 'start tracking' actions, and axis events for fast moves.
- Have Rasperry Pi HD camera attached to the telescope to provide video stream via the astounding [camera-streamer](https://github.com/ayufan/camera-streamer) app
