#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from forklift import Forklift

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


## SET UP THE DRIVE CHASIS ##
ev3 = EV3Brick()
l_DriveMotor = Motor(Port.B)
r_DriveMotor = Motor(Port.C)
driver = DriveBase(l_DriveMotor,r_DriveMotor,68.8,111)

## CREATE THE FORKLIFT ##
f_motor = Motor(Port.A)
myFork = Forklift(f_motor, 650)


## SET UP THE SENSORS ##
#gyro = GyroSensor(Port.S1)

#######################
## Main Program      ##
#######################

ev3.speaker.beep() # notify done
#driver.straight(1440)
myFork.up(100,50)
myFork.down(100,50)
#driver.straight(-1440)
ev3.speaker.beep() # notify done