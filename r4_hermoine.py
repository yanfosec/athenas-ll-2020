#!/usr/bin/env pybricks-micropython

from robotsetup import ev3, driver, fork, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor
from turning import gyroLeft, gyroRight, gyroRightTo
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
from colorwheel import run_color

#start following black line with right sensor

while run_color() != "Yellow":
    wait(10)

driver.straight(100)
driver.stop()
gyroRight(50)
driver.stop()
while r_color.reflection() >10:
   driver.drive(130, 0)
driver.stop()
gyroLeft(25)
driver.stop()
counter = 0
while counter < 3:
    while l_color.reflection() >9:
        followBlack(r_color, 150)
    counter = counter + 1
    ev3.speaker.beep() 
driver.stop()
gyroRight(90)
driver.straight(255)
driver.stop()
for x in range (5):
    gyroRight(50)
    gyroLeft(50)