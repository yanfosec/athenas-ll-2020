#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, fork, r_color, l_color
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#######################################################################
## Run Code Starts Here                                              ##
#######################################################################
ev3.speaker.beep() # notify done
# drive until black
while r_color.reflection() >10:
    driver.drive(125, 0)
    wait(10)
driver.stop()
# push the step counter
driver.straight(40)
while r_color.reflection() <95:
    driver.drive(20, 0)
    wait(10)
driver.stop()
driver.settings(straight_speed=30)
driver.straight(110)
# turn to the bridge
driver.straight(-140)
driver.turn(90)
ev3.speaker.beep() # notify done