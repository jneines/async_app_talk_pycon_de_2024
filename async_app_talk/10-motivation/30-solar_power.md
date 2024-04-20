# Solar Power yield of the balcony power plant

Power inverter offers data via proprietary wireless interface, which can be read by a Raspberry Pi with a matching receiver attached.

:::{image} images/solar_power_reading.png
:::

- Read data via matching receiver.
- decode and wrap into a usable format
- send to **fastapi** based webservice for relaying and storage
- use **pyscript** engine to diplay data in webbrowser
