# Flashing Controller Software to the OpenScout Robot

## Install time = 20 minutes

### Setup

Start by downloading [ArduinoIDE 2.X](https://www.arduino.cc/en/Main/Software).

In Arduino IDE, in board manager downlaod "esp32 by Espressif Systems"

### Download this driver.
https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads

### If using some variant of ESP32 Ch340c, you might need this driver (likely optional)
https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all

### Connect the ESP32 via USB to the computer and set the port it is attached to
  
- `Tools -> Board -> Arduino AVR Boards -> *Select the ESP32 board, if you're not sure pick ESP32 Dev Module*`
- `Tools -> Port -> *Select the USB port*`

### Option A: Flash BlueTooth controller
1. Open the Arduino IDE and load in the `OpenScout_control_BT.ino` file (`File -> Open -> select_file`).
2. Upload the sketch by pressing the upload button.
3. Download an app like `Serial Bluetooth Terminal` on your phone (or use any other serial BT terminal of your choice, OpenScoutV2 isn't affiliated)
4. Connect to the OpenScout via bluetooth.
5. Connect to the serial terminal.
6. Try sending single characters "w", "a", "s", "d" to move, and "x" to stop.

### Option B: Flash MQTT controller
1. Open the Arduino IDE and load in the `OpenScout_control_MQTT.ino` file (`File -> Open -> select_file`).
2. Upload the sketch by pressing the upload button.
3. Download ros2_ws into the home folder, on a (likely ubuntu noble) machine running ROS2 Jazzy.
4. 
