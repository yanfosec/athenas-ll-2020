#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, fork, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor, dumper
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
import time
from turning import gyroRight,gyroLeft
from dump import Dump

#drive to the dance floor
gyroRight(30)
driver.straight(935)
driver.stop()
gyroRight(65)
while r_color.reflection() >12:
    driver.drive(125, 0)
driver.stop()
driver.straight(20)
driver.stop()
while r_color.reflection() >12:
    driver.drive(125, 0)
driver.stop()
gyroRight(60)
driver.stop()
dumper.down(100,100)



