# The motor driven telescope

Yes, there are star trackers available already. I wanted to know what it takes to build one myself.

:::{image} ./images/telescope.gif
:width: 100%
:align: center
:::

- Have **stepper motor** attached to telescope axis.
- Atach a stepper **motor controller** to a **Raspberry Pi**.
- Use Python app to drive stepper motor based on commands received via **redis pubsub**.
- Use **gamepad** to steer motor using buttons for toggling active state, and axis events for for positioning and tracking speed fine tuning.
- Have **Rasperry Pi HD camera** attached to the telescope to provide video stream via the astounding [camera-streamer](https://github.com/ayufan/camera-streamer) app.
