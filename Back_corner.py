#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, door, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor, dumper
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
import time
from turning import gyroRight,gyroLeft
from dump import Dump


driver.settings(straight_speed=450)
driver.stop()
driver.straight(-10)
ev3.speaker.beep() # notify done
gyro.reset_angle(0)
driver.stop()
driver.straight(80)
driver.stop()
gyroRight(79)
driver.stop()#turrning out to face challange zone
driver.straight(1380)#getting out to zone
driver.stop()
gyroLeft(80)
driver.straight(300)
driver.stop()
while r_color.reflection()<85:#sensing white by weight machine 
    driver.drive(200,0)
driver.stop()
driver.straight(30)
driver.stop()
driver.straight(80)
driver.stop()
gyroRight(80)
#door.run_until_stalled(400)
while l_color.reflection()>12:#
    driver.drive(200,0)
driver.stop()
door.run_until_stalled(-400)#door up
gyroLeft(77)#turn so door is over weight machine
door.run_until_stalled(400)#door down to get machine
driver.stop()
gyroRight(93)
driver.stop()
driver.straight(500)#wall square
while l_color.reflection()<85:#goes back to white line
    driver.drive(-200,0)
driver.stop()
gyroRight(52)#turns to row machine
door.up(300,30)
driver.straight(200)#does row
driver.stop()
door.down(300,26)
driver.stop()
gyroRight(55)
driver.stop()
driver.straight(-40)#pulls circle into small space
door.run_until_stalled(-300)
driver.straight(-40)
driver.stop()
gyroRight(30)
driver.stop()
driver.straight(250)
driver.stop()
gyroLeft(63)
door.run_until_stalled(300)
while l_color.reflection()<85:
    driver.drive(300,0)
driver.stop()
gyroLeft(35)
driver.stop()
driver.straight(50)
driver.stop()
gyroRight(25)
driver.straight(200)
driver.stop()








