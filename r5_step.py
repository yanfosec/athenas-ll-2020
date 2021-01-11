#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor
from turning import gyroLeft, gyroRight
from pybricks.hubs import EV3Brick
#from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from linefollow import followBlack

def run4():
    driver.stop() #stops for membory problem
    driver.settings(straight_speed=450) #definig straight speed
    driver.straight(600) #going straight to get out near sc
    driver.stop() #stoping to try and drop
    driver.straight(150)
    driver.stop()
    driver.straight(600)
    driver.stop()
    driver.straight(-1300)


