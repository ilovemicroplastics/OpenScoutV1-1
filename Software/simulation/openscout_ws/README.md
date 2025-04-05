This is a ROS2 package for virtually simulating the OpenScoutV2 robot.

## Environment
[Ubuntu Noble 24.04.1](https://releases.ubuntu.com/noble/) 

[ROS2 Jazzy](https://docs.ros.org/en/jazzy/Installation.html)

[Gazebo Harmonic](https://gazebosim.org/docs/harmonic/ros_installation/)
 
### Further info
During the time of writing (2025), Gazebo Harmonic does not tolerate running in a virtual machine very well. It is recommended to run it on a computer with Ubuntu Noble installed natively. 

Additionally, when installing Gazebo Harmonic ensure that you do not install the standalone version. Instead first install ROS2 Jazzy, and then opt for [the version of Gazebo integrated into ROS2 Jazzy.](https://docs.ros.org/en/jazzy/Installation.html)

![alt text](https://github.com/ilovemicroplastics/OpenScout/blob/main/Software/simulation/openscout_ws/openscout_sim.png)

## Guide to running the package (On the default Ubuntu system)

First prepare the environment, as listed above.

Then make sure you have teleop twist keyboard installed.
````
sudo apt-get install ros-jazzy-teleop-twist-keyboard
````

Download or clone the repository openscout_ws, and put it in the **home** folder.

Open the Terminal and enter the following commands.

````
source /opt/ros/jazzy/setup.bash
cd ~/openscout_ws
colcon build
source install/setup.bash
ros2 launch openscout openscout.launch.py
````

This should open the simulation.

From there you can try moving the openscout with teleop keyboard.
In a new terminal enter the following:
````
source /opt/ros/jazzy/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
````

## Once in the simulation

Try driving over the slope with one side. This showcases the joint in the middle of the robot.

Feel free to make edits to the SDF to test whatever you like.

Its possible to make a python file to control the openscout using ROS2 topics.

## Example video of simulation running once set up

https://github.com/user-attachments/assets/db36529f-7577-4ad0-a52f-730f6c3506c2

## Statement on simulation accuracy

**Most Recent Performance Analysis of real OpenScoutV2**

| **Parameter**            | **No Load** | **3kg Load** | **6kg Load** | **Units**   |
|--------------------------|-------------|--------------|--------------|------------|
| Distance Tested          | 5.0         | 5.0          | 5.0          | meters     |
| Time Taken               | 9.0         | 10.0         | 11.0         | seconds    |
| Linear Velocity          | 0.60        | 0.50         | 0.45         | m/s        |
| Performance Reduction    | 0%          | 16.7%        | 25.0%        | percentage |
| Angular Velocity         | $\pi/7 \approx 0.45$ |  |  | rad/s      |
| Full Rotation Time       | 14.0        |          |          | seconds    |

**Performance Analysis of virtual OpenScoutV2**

| **Parameter**   | **Value** | **Unit** |
|-|-|-|
| Distance Tested | 5.0       | m        |
| Time Taken      | 10.0      | s        |
| Linear Velocity | 0.5       | m/s      |
| Angular Veloctiy| $\pi/9 \approx 0.35$ | rad/s |
| Full Rotation Time | 18     | s        |

As can be seen, the simulated OpenScoutV2 is a close approximation. Unfortunately due to Gazebo Harmonic (01/04/25) physics limitations, modelling the interaction between wheels and the ground realistically is difficult. An idea being floated is to try to port the [Gazebo Classic wheel slip plugin](https://github.com/gazebosim/gazebo-classic/blob/gazebo11/plugins/WheelSlipPlugin.hh) to Gazebo Harmonic. In theory this would resolve the software bottleneck, but it would require extensive development and testing.

- Further testing and refinement will be conducted when newly released software that may yield improvement is released.
