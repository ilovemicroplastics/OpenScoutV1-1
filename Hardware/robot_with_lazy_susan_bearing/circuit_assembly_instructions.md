# Electronics layout

## Build time = 75 minutes

### Bill of materials:

| Material                         | Quantity | Reference | UK link |
| ---------------------------------|---------:|:---------:|:-------:|
| 12V Lead Acid battery | 1 | E1 | [Link](https://uk.rs-online.com/web/p/lead-acid-batteries/0597835) |
| 10A circuit breaker | 1 | E2 | [Link](https://amz.run/5TFI) |
| Buck converter | 1 | E3 | [Link](https://amz.run/5TFJ) |
| ESP32 | 1 | E4 | [Link](https://amz.run/9w90) |
| L298N Motor drivers | 2 | E5 | [Link](https://amz.run/5TFN) |
| 90:1 12V motor with encoders | 4 | M1 | [Link](https://amz.run/5TFQ) |
| Din rail with terminal blocks | 1 | DT | [Link](https://amz.run/5TFF) |
| Velcro 50mmx1m | 1 | Q | [Link](https://amz.run/5TFP) |
| Breadboards | - | - | - |
| Wires | - | - | - |


CQrobot Motor (M1) pinout:
| Motor (M1) | wire |
| -----------|-----:|
| ENC_A  | yellow |
| ENC_B  | white |
| VCC    | blue |
| GND    | gray |
| MOTOR+ | red |
| MOTOR- | black |

## Introduction

This tutorial provides instructions for wiring together the electronic components. Example photos are provided and can be used as reference, however some of the components are optional (e.g. the terminal blocks (DT) on the din rail, and the breadboards) but you are free to replace them with other components such as veroboards, depending on your soldering experience. The schematics provided in `.pdf` format show in-detail how the different components are connected together. (**WARNING**: Please handle the Lead Acid battery (E1) with care.)

## Wiring Diagram

<p float="center">
  <img src="../../Documentation/Images/wire_diagram_2.png" title="Wiring diagram." width="100%"/>
</p>


## Step-by-step instructions

### 1. Connecting the ESP32

1. Attach a strap of velcro (Q) either on the back or the front of the robot (depending on where you'd like to place the battery), and on the bottom of the battery (E1) so you can secure it on the robot. You can use the terminal blocks on the din rail (DT) to prepare some 12V and 5V (using the step down converter (E3)) power lines to power the components.

<p float="center">
  <img src="../../Documentation/Images/esp_pinout.PNG" width="500"/>
</p>

2. Attach the ESP32 on a breadboard.

### 2. Connecting the front motors with the front motor driver

1. Connect the L298N front motor driver (E5) on 12V and the enable/input pins on the ESP32 (E4)

<p float="center">
  <img src="../../Documentation/Images/electronics_0.jpeg" title="Attaching the motor brackets on the bottom of the chassis." width="500"/>
</p>

| L298N front motor driver (E5) | Pin on ESP32 |
| -----------------|---------------:|
| ENA | D13 |
| IN1 | D17 |
| IN2 | D16 |
| IN3 | D4 |
| IN4 | D16 |
| ENB | D14 |

2. Connect the output pins of the L298N (E5) on the LF and RF motors (M1) (see the motor color table on the top of the page).

| L298N front motor driver (E5) | RF Motor (M1)|
| -----|----:|
| OUT1 | red |
| OUT2 | black |

| L298N front motor driver (E5) | LF Motor (M1)|
| -----|----:|
| OUT3 | black |
| OUT4 | red |

3. Connect the encoder VCC and GND on the LF and RF motors (M1) on the 3.3V output of the ESP32 (E4).
   
4. See the [front side motors layout](../../Documentation/Schematics/front_side_motors.pdf) schematic for reference.


### 3. Connecting the back motors with the back motor driver

1. Connect the L298N back motor driver (E5) on 12V and the enable/input pins on the arduino (E4)

| L298N back motor driver (E5) | Pin on ESP32 |
| -----------------|---------------:|
| ENA | D9 |
| IN1 | D25 |
| IN2 | D24 |
| IN3 | D23 |
| IN4 | D22 |
| ENB | D8 |

2. Connect the output pins of the L298N (E5) on the LB and RB motors (M1) (see the motor color table on the top of the page).

| L298N back motor driver (E5) | LB Motor (M1)|
| -----|----:|
| OUT1 | red |
| OUT2 | black |

| L298N back motor driver (E5) | RB Motor (M1)|
| -----|----:|
| OUT3 | black |
| OUT4 | red |

<p float="center">
  <img src="../../Documentation/Images/final_circuit.jpg" title="Example wiring of the robot." width="500"/>
</p>

## What's next?
Congratulations! The robot wiring is complete. Follow the last part of the tutorial series to [flash the software](../../Software/README.md).
