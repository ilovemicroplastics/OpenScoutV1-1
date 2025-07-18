### build
cd ~/ros2_ws/

colcon build --symlink-install

ros2 run esp32_mqtt_interface mqtt_publisher

### use
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0}, angular: {z: 1.0}}"

### example output
publishing #1: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.5))

publishing #2: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.5))

publishing #3: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=1.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.5))

### clarification

This has been made primarily to serve as a demo for further refinement. These commands have been used in Ubuntu Noble. There must be a ESP32 loaded with the MQTT program turned on within the same WiFi network for this to work. Be aware of the fact that there is no timeout or off switch, so be ready to send a stop command or to pick the robot up if it may hit a wall.

Page last reviewed by: B.K. on 18/07/25
