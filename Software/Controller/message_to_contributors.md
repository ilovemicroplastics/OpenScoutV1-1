### Hello

This MQTT script might be a little confusing.

It's essentially a normal MCU robot controller, which has a MQTT broker built in.

The MQTT broker receives certain preprogramed ROS2 topics, and parses them to calcualte the movement command.

Therefore this isn't a direct ROS2 implemention, but more like a ROS2 implemention from first principles, or a ROS2 interface without true ROS2.

This was done as a workaround to the 1.3MB of memory contained, and the program maxes it out.
