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
import time

#######################################################################
## Run Code Starts Here                                              ##
#######################################################################

#print(str(calcOffset(gyro)))
print("Gyro Turns")
for x in range(10):
    turnBot(gyro,'R', 89)
    turnBot(gyro,'L', 89)

# time.sleep(1)
# print("Driver Turns")
# for y in range(10):
#     gyro.reset_angle(0)
#     driver.turn(90)
#     print(str(gyro.angle()))
#     driver.stop()
#     time.sleep(1)
#     gyro.reset_angle(0)
#     driver.turn(-90)
#     print(str(gyro.angle()))
#     driver.stop()
#     time.sleep(1)
