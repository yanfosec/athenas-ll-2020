#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, fork, r_color, l_color, gyro
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
from turning import calcOffset, turnBot

#######################################################################
## Run Code Starts Here                                              ##
#######################################################################

#print(str(calcOffset(gyro)))

turnBot(gyro,'R', 89)
turnBot(gyro,'L', 89)

