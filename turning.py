#!/usr/bin/env pybricks-micropython

from robotsetup import ev3, driver, door, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor, dumper
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
import time

#######################################################################
## Run Code Starts Here                                              ##
#######################################################################

def gyroRight (degrees):
    turnSpeed = 60
    gyro.reset_angle(0)
    while gyro.angle() <= degrees:
            r_DriveMotor.run(-1 * turnSpeed)
            l_DriveMotor.run(turnSpeed)

def gyroLeft (degrees):
    turnSpeed = 60
    gyro.reset_angle(0)
    while gyro.angle() >= -1 * degrees:
            r_DriveMotor.run(turnSpeed)
            l_DriveMotor.run(-1 * turnSpeed)
    


