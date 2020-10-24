#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, fork, r_color, l_color
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack

## Main Program      ##

ev3.speaker.beep() # notify done
driver.straight(50)
fork.up(100,50)
fork.down(100,50)
driver.straight(-50)
ev3.speaker.beep() # notify done
ev3.speaker.say("Hello World")
ev3.screen.print("Hello")
ev3.screen.print("World")
wait(10000)