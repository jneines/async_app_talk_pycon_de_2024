#  Track overall power usage at the main power meter


Power meter offers a serial interface via infrared diode, which is read by a Raspberry Pi.

:::::{grid}
::::{grid-item}
:::{image} images/power_meter.jpg
:width: 90%
:align: center
:::
::::

::::{grid-item}
:::{image} images/power_meter_reading.png
:width: 90%
:align: center
:::
::::
:::::


- Read data stream from the power meter using **serial interface**.
- parse data for a pattern matching the latest power draw.
- publish data to a central **fastapi** service for display and storage.
- display again using **pyscript** engine in web browser.

