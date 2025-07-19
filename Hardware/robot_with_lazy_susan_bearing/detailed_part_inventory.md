# Wheel (and Hex coupler, Hex wheel driver)
<p float="center">
  <img src="../../Documentation/Images/wheels_1.jpeg" title="wheels with hex adaptors on them" width="300"/>
  <img src="../../Documentation/Images/wheel.PNG" title="wheels without hex adaptor" width="256"/>
</p>

**Priority:** Very High

**Description:** The 112x46mm wheel, 6mm hex coupler and 12mm to 17mm hex wheel driver are the parts which contact the ground. The other two are supposed to firmly attach the wheel to the motor axle. The wheel has an almost flat rubber tread, which is important because this is a skid-steer robot.

**Availability:** The wheel is no longer being produced. The traditional hex wheel driver amazon link is dead. The hex coupler is currently sourced from an alternative amazon store page which is produced by a 3rd party (The original manufacturer was KingVal).

**Additional notes:** This is a critical shortage which prevents anyone who doesn't already own these parts from building the OpenScoutV1.1. As such, they have to be replaced one way or another. Rather than finding a new commercial part, it is highly recommended to find a design or to design a wheel which can be produced locally with low or little skill. 3D printing comes to mind as it's a good way to make a part which can be reproduced forever, but if a better wheel solution is found so be it. Maybe it's easier to make the wheel out of cut acrylic and rubber tape? Ultimately it comes down to what works in practice and that's hard to predict.

#### Segment last reviewed by: B.K. on 19/07/25

# Din rail with terminal blocks

(Picture needed)

**Priority:** Medium

**Description:**

**Availability:** The amazon storefront used to buy these goes out of stock very often, making it difficult to aquire new terminal blocks.

**Additional notes:** There are quite a few other options to consider, they essentially just serve the purpsoe of wire connectors.

#### Segment last reviewed by: B.K. on 19/07/25

# Hinge
<p float="left">
  <img src="../../Documentation/Images/hinge.PNG" title="hinge" width="300"/>
</p>

**Priority:** Low-Mid

**Description:** The 5.5in metal hinge is the mobile part which connects the "front" and "back" frames to each other. It can do a full rotation. This particular hinge comes in multiple size variants, although 5.5in is used for the OpenScoutV1.1. Occasionally stores will refer to it as a "Lazy Susan".

**Availability:** The hinge isn't technically out of stock, but it's availablity has been spotty. It seems to be available on aliexpress but western online stores can be hit or miss.

**Additional notes:** If this particular design does come out of production it should be easy to replace it as there are many similar hinges online, its just that the CAD files for the plastic plates where the hinge meets would need to be redesigned to fit the new screw locations. This would work, but once again it's not a permanent solution. The ideal solution would be reproducible locally forever, admittedly that's difficult with a hinge but maybe there is a solution. 

#### Segment last reviewed by: B.K. on 19/07/25

# ESP32
<p float="left">
  <img src="../../Documentation/Images/esp32.jpg" title="ESP32" width="300"/>
</p>

**Priority:** Low

**Description:** ESP32 refers to a variety of different chips which do almost the same thing, but not quite. The particular ESP32 which the OpenScoutV1.1 was designed with can be called the "[ESP32-CH340C Type-C](https://amz.run/9w90)", which means that it's a generic ESP32 with a CH340C chip and a Type-C connector. The manufacturer is [ESPRESSIF website](https://www.espressif.com/en/products/socs/esp32)), however there are many third-party produced variants on the market. They generally work the same but have some small differences; for example some of the pin locations/functions are different to the ESP32s produced directly be ESPRESSIF.

The "ESP32-CH340C Type-C" wasn't chosen out of any technical reason, other than the fact that an ESP32 was needed quickly and amazon had 1 day shipping as opposed to the month+ wait from AliExpress. 

**Availability:** Good.

**Additional notes:** If you happen to have one of these third-party ESP32s you are better off finding out which pin does what by comparing it to the core designs, looking at the labels, and trial and error. Ultimately it shouldn't make much of a difference as all these ESP32s generally do almost the same thing, just they might have slightly different dimensions or pin configurations. In the future it may be worth switching the OpenScout design to a ESP32 model actually produced by ESPRESSIF as opposed to the current third-party one, especially if its a newer model which is planned for long term production (you can check this on the ESPRESSIF website).

MCUs are almost impossible to produce locally, I suppose this part might be an exception where its acceptable to update it as an OpenScout version ages, since it shouldn't change the properties aside from having better compute. Alternatively, the OpenScout definition could be flexible with the MCU. For example something like "An MCU which fulfills these requirements... ", but then there would be a recommended chip with available firmware. The only problem with this approach is that quirks of certain chips might alter experiment results, but that seems unlikely.

#### Segment last reviewed by: B.K. on 19/07/25

# Velcro

(Picture needed)

**Priority:** Low

**Description:**

**Availability:** Bad, dead amazon link. New source is needed.

**Additional notes:** Until the above mentioned wheel issue is resolved, whether the battery is loose or not doesn't matter. Although the velcro availability issue is trivial to fix.

#### Segment last reviewed by: B.K. on 19/07/25

# 20x20 aluminium extrusion

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# 20x20 Angle Joint Brace Brackets

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# 90 Degree Cast Corner

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# 3mm acrylic sheet

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# 90:1 12V motor with encoders

(Picture needed)

**Priority:** Low

**Description:** This CQRobot motor has a helpful [wiki page](http://www.cqrobot.wiki/index.php/DC_Gearmotor_SKU:_CQR37D).

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# 12V Lead Acid battery

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# 10A circuit breaker

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# 5V Buck converter

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# L298N Motor drivers

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# Breadboard

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# Wires

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# M2/3/4/5 Hex Key

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25

# Small Flathead and Head Screwdriver

(Picture needed)

**Priority:** Low

**Description:**

**Availability:**

**Additional notes:**

#### Segment last reviewed by: B.K. on 19/07/25


#### Page last reviewed by: B.K. on 19/07/25

Notes - I can't do this fully due to practical limitations, but I recommend this page be used to detail what each part is exactly with pictures, blueprints, and specification; just in case links to buy them go offline. This could also be a place to store notes about plans of how each part is going to be replaced to increase the ability to build the robot locally, or whatever else it may be useful for.
