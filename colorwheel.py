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
import time

def run_color():
    found_color = False

    while found_color == False:
        isee = l_color.color()
        if isee == Color.RED:
            print ("I see red")
            return "Red"

        if isee == Color.BROWN:
            print ("I see brown")
            return "Brown"
 

        if isee == Color.BLUE:
            print ("I see blue")
            return "Blue"
 

        if isee == Color.GREEN:
            print ("I see green") 
            return "Green"
    

        if isee == Color.YELLOW:
            print ("I see yellow")
            return "Yellow"


    # if isee == Color.WHITE:
    #     print ("I see white")

    # if isee == Color.BLACK:
    #     print ("I see black")

    # time.sleep(3)

# "Red"
# "Brown"
# "Blue"
# "Yellow"
# "White"
# "Black"