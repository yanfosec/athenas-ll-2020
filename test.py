#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from robotsetup import ev3, driver, d_motor, door, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor, dumper
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
import time
from turning import gyroRight,gyroLeft
from dump import Dump

#tup = d_motor.control.stall_tolerances()
#print(tup)

door.up(300,90)
while True:
    a=1