# Motivation

The need for a simple 'template like' app to create various simple applications, a framework maybe?

##  Temperature and Humidity monitoring at several locations in my house

- track solar power yield from the balcony power station
- timelapse photography


All those apps follow the same pattern:

- read input, such as sensor data and photos as they come or on demand
- process them
- send them somewhere else
- run forever
- as no software is perfect: 
    - monitor resource usage
    - watch for errors

This combination tends to get complex already:

- how to guarantee timely calls
- how to prevent blocking behaviour
- how to do things 'at the same time'


Didn't like 'threading' to much (because of many reasons, but that's a different story), so went for 'asyncio'.
