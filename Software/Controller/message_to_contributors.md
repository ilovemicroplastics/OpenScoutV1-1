### Hello

This is a message to anyone attempting to modify the ESP32 program, its very much doable! but it will take some determination.

This MQTT script might be a little confusing.

It's essentially a normal MCU robot controller, which has a MQTT broker built in.

The MQTT broker receives certain preprogramed ROS2 topics, and parses them to calculate the movement command.

Therefore this isn't a direct ROS2 implementation, but more like a ROS2 implementation from first principles, or a ROS2 interface without true ROS2.

This was done as a workaround to the 1.3MB of memory contained, and the program maxes it out.

Believe me, this ESP32 script seems intimidating, and it genuinely is if you aren't primed properly.

I would recommend going in this order.
- First have a basic understanding of C++ (Chose someone who knows already ideally)
- Also, ideally you would have a basic understanding of how electronic circuits work
- Then understand that the ESP32 has certain built in commands which aren't native to C++, such as timers or input/output pin settings
- Then understand that the ESP32 has libraries which are developed specifically for it, and they have their own syntax (although its similar to C++). The MQTT broker used is a library for example.
- Be careful with library versions, because some of them have minor syntax changes between versions which can be a frustrating source of errors when trying to find the correct syntax
- After all that, try understand the program by running through it line by line and making notes
- If you don't understand why certain pins are set to high, and others set to low (etc), you have to read the specification sheet of every part you want to interact with. It's not that complicated, manufacturers literally just write how the part works and what input/outputs it needs.
- It does a lot of maths regarding the Hall effect, and technically its only at half efficiency as these motors can give twice as many readings.
- But you don't really need to know that to modify the code, just know that it works and that it modulates the motor speed.
- If you really want to know about how the Hall sensing works then read the wiki of the [motor](http://www.cqrobot.wiki/index.php/DC_Gearmotor_SKU:_CQR37D) 
- Without the Hall effect maths the motors will work FAR worse, try it if you wish.
- On top of all this the MQTT  interface is used to send ROS2 command strings across networks which are parsed into real low level commands.
- The Bluetooth variant is simpler, it uses simple CLI to control the robot. Bluetooth is a seperate program because the MQTT and Bluetooth library together take up too much space on the ESP32
- When in doubt use trail and error or LLMs, but ideally only for explanation purposes because I've found LLMs (in 2025) to be mediocre for low-level C++ like this.
- If it doesn't make sense read all this again, and or take a break.
- Make the changes you need to.

If you can understand all this you earned your low-level programming wizard hat, congratulations.

Good luck.

B.K. - 19/07/2025
