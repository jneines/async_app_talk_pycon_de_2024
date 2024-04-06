#  Track overall power usage at the main power meter

:::{image} images/power_meter.jpg
:::


- Read the infrared sensor, which is a serial interface actually
- parse data for a pattern matching the latest power draw
- publish date to a central fastapi service for display and storage

:::{image} images/power_meter_reading.png
:width: 480px
:::
