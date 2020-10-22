#!/usr/bin/env pybricks-micropython
#import codes
from robotsetup import ev3, driver, fork, r_color, l_color
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack

#start following black line with right sensor
while r_color.reflection() >30:
    driver.drive(125,10)
    wait(10)
driver.stop()
ev3.speaker.beep() 
#turn to follow black line
while l_color.reflection() >15:
    followBlack(r_color,DRIVE_SPEED=100)
    wait(10)
driver.stop()
while r_color.reflection() >10:
    driver.turn(10)