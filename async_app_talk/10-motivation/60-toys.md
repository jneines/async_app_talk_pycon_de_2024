# Driving little toys

These little cars are fun to play with. Equipped with all sorts of sensors they are meant to drive as autonomous as possible and teach you how things work.

I do have fun with remote controlling already

:::{image} images/rover.jpg
:height: 480px
:align: center
:::

- car platform is equipped with 4 motors and all sorts of sensors, camera and stepper motor to adjust viewing angle
- Raspberry Pi is used to control everything
- All motors have a Python app for steering waiting for commands via redis
- camera is operated by the great [camera-streamer](https://github.com/ayufan/camera-streamer) app
- steering events are generated using gamepad
- Python based joystick controller app is bridging events to steering commands
