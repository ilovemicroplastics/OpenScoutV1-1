# OpenScout v1.1

## An Improved Open Source Hardware Mobile Robot
OpenScout v1.1 is a low-cost (approx. 350USD) OSH mobile robot that can be used for both indoor and outdoor tasks, tested up to 6kg of mounted payload. This project builds on the original [OpenScout](https://zenodo.org/doi/10.5281/zenodo.10263675) by reducing it's complexity, adding a simulated ROS2 interface, providing a WiFi and BlueTooth interface, as well as introducing a Gazebo simulation for testing. The robot is designed to be simple and easily buildable.

The intended purpose is to function as a reproducible physical platform for robotics research and real-world tasks, replacing existent proprietary options. The OpenScoutV1.1 offers light offroad capabilities (suitable for a farm or similar), and is a blank slate to attach modules to. It is designed so that a non-technician should be able to build it and attach a less than 6kg scientific (or other) instrument. Example applications include; mounting a camera for autonomous site survey, an actuator for agricultural operations like crop inspection, use in robotics experiments, and autonomous local deliveries in areas covered by WiFi (for example a campus).

OpenScout is made from standard sized aluminium extrusions making it modular. That means its chassis design can be varied based on the use case and the needs of the user.

https://github.com/user-attachments/assets/4c83e099-2132-454d-ae23-d050e3298f1a

## Assembly Tutorial:
Assembly tutorial for the OpenScout with a 'Lazy Susan' revolute hinge is available at the following link:
[OpenScoutV1.1 robot with 'Lazy Susan' revolute hinge](Hardware/robot_with_lazy_susan_bearing/README.md)

## Gazebo Harmonic Simulation:
To see the Gazebo Harmonic Simulation, follow this link:
[OpenScoutV1.1 simulation](Software/simulation/openscout_ws/README.md)

## If you encounter any problems or find anything unclear...

Feel free to open an issue. All feedback is valuable and instructions will be updated accordingly. 

Fair warning, this is considered a development version of the OpenScout. Assess everything properly, we do not accept liability.

## How to contribute
While we try to keep this project open source you are free to make your own choice of materials and adapt the robot to your needs. However, we kindly request you to stick to the suggested 200mm & 300mm 20x20 aluminum extrusions, to allow others to disassemble their current configuration and try out yours! If you use OpenScout for your project, please open a PR with your configuration and tutorials. 

The general process of contributing on GitHub is widely documented however the outline process is below:

1. Identify where you want to host the project locally. This could be a OpenScout projects folder for example. 


1. Clone or fork the repository using GitHub desktop or the CLI into this location (CLI is recommended as this helps you become more familiar with Git in general). You can do this with the following command:

    ```bash
    git clone https://github.com/ilovemicroplastics/OpenScoutV1.1
    ```

1. Update the project and then make a pull request.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE) and [CERN-OHL-W](LICENCE) and [CC BY-SA](CC-BY-SA_LICENCE)

<p align="left" width="100%">
    <img src="Documentation/Images/oshw_cert_label.png">
</p>

## Governance

Aside from following the licenses, after every modification sign off every github page as proof of work/and or a means of leaving notes for future contributors. This makes auditing easier and helps clear up confusion so new contributors can get to making changes faster (rather than trying to work out where to start).

**Key principles to follow:** OSH, Extensible, Accessible (both in build difficulty and price), reproducible to a high degree.

#### Page last reviewed by: B.K. on 19/07/25
