#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, fork, r_color, l_color
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack

#######################################################################
## Run Code Starts Here                                              ##
#######################################################################
ev3.speaker.beep() # notify done
# drive until black


while l_color.reflection() >10:
    # Start following the line endlessly.
    
    followBlack(r_color, 150)


driver.stop()
driver.turn(110)
driver.stop()
driver.straight(400)
driver.stop()
driver.straight(-408)
driver.stop()
driver.turn(110)
driver.stop()

while r_color.reflection() >10:
    # Start following the line endlessly.
    
    followBlack(l_color, -150)

while r_color.reflection() >10:
    # Start following the line endlessly.
    
    followBlack(l_color, -150)
#
# while r_color.reflection() <95:
#     driver.drive(20, 0)
#     wait(10)
# driver.stop()
# driver.settings(straight_speed=30)
# driver.straight(110)
# # turn to the bridge
# driver.straight(-140)
# driver.turn(90)
# ev3.speaker.beep() # notify done
