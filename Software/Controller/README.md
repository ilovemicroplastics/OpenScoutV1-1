# Flashing Controller Software to the OpenScout Robot

## Install time = 20 minutes

### Setup
1. Start by downloading [ArduinoIDE 2.X](https://www.arduino.cc/en/Main/Software).
2. In Arduino IDE, in board manager downlaod "esp32 by Espressif Systems"
3. Download this [driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads).
4. If using some variant of ESP32 Ch340c, you might need this [driver](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all) (skip, and go back to this step if your board isn't being recognised.)
5. Connect the ESP32 via USB to the computer and set the port it is attached to
- `Tools -> Board -> Arduino AVR Boards -> *Select the ESP32 board, if you're not sure pick ESP32 Dev Module*`
- `Tools -> Port -> *Select the USB port*`

### Option A: Flash BlueTooth controller
1. Open the Arduino IDE and load in the `OpenScout_control_BT.ino` file (`File -> Open -> select_file`).
2. Upload the sketch by pressing the upload button.
3. Download an app like `Serial Bluetooth Terminal` on your phone (or use any other serial BT terminal of your choice, OpenScoutV2 isn't affiliated)
4. Connect to the OpenScout via bluetooth.
5. Connect the phone serial terminal to the OpenScoutV2.
6. Try sending single characters "w", "a", "s", "d" to move, and "x" to stop.

### Option B: Flash MQTT controller
1. Open the Arduino IDE and load in the `OpenScout_control_MQTT.ino` file (`File -> Open -> select_file`).
2. Upload the sketch by pressing the upload button.
3. Download [ros2_ws](./ros2_ws) into the home folder, on a (likely ubuntu noble) machine running ROS2 Jazzy. (If you know what you are doing, feel free to deviate at this point.)
4. Open a bash terminal.
5. `cd ~/ros2_ws/`
6. `colcon build --symlink-install`
7. `ros2 run esp32_mqtt_interface mqtt_publisher`
8. Open a new bash terminal.
9. `ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0}, angular: {z: 0.0}}"`
