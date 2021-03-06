#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, door, r_color, l_color
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Calculate the light threshold. Choose values based on your measurements.

BLACK = 10
WHITE = 95

threshold = (BLACK + WHITE) / 2

PROPORTIONAL_GAIN = 0.7

def followBlack(thisSensor,DRIVE_SPEED=150):
    # Calculate the deviation from the threshold.
    deviation = thisSensor.reflection() - threshold

    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation
    
    # Set the drive base speed and turn rate.
    driver.drive(DRIVE_SPEED, turn_rate)

    # You can wait for a short time or do other things in this loop.
    
    wait(10)
