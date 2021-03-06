#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor
from turning import gyroLeft, gyroRight
from pybricks.hubs import EV3Brick
#from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from linefollow import followBlack
#INSPIRED BY: the wordy nerd
# https://docs.google.com/document/d/1-XtIKJ9Rxke5ZgvPM95F9kQTXDrwLeiBTXmjrIRSvHE/edit?usp=sharing

def run4():#creats a function for run 4
    driver.stop() #stops for membory problem
    driver.settings(straight_speed=500) #definig straight speed
    driver.straight(600) #going straight to get out near sc
    driver.stop() #stoping to try and drop
    driver.straight(150) #goes forward more; closer to the step counter
    driver.stop()#trys to drop again just incase
    driver.straight(600) #dives all the way back to push back the stepcounter
    driver.stop() #stops
    driver.straight(-1300) #drives back to hime


