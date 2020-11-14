#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, fork, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor, dumper
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
import time
from turning import gyroRight,gyroLeft
from dump import Dump

driver.settings(straight_speed=250)

#drive to the dance floor
gyroRight(28)
driver.straight(935)
driver.stop()
gyroRight(65)
driver.settings(straight_speed=125)
while r_color.reflection() >12:
    driver.drive(125, 0)
driver.stop()
driver.straight(20)
driver.stop()
#while r_color.reflection() >12:
 #   driver.drive(125, 0)
driver.straight(125)
driver.stop()
gyroRight(65)
driver.stop()
driver.straight(-50)
dumper.down(300,90)
driver.straight(10)
dumper.up(300,30)
driver.straight(125)
driver.stop()
gyroRight(40)
driver.straight(-55)
driver.straight(10)
dumper.up(150,10)
driver.straight(10)
dumper.up(150,10)
driver.straight(50)
driver.stop()
driver.settings(straight_speed=300)
driver.stop()
gyroRight(55)
driver.straight(500)
driver.stop()
gyroLeft(65)
driver.straight (800)
dumper.up(300,40)

