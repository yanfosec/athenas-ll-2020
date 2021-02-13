#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Dump: #creating a class

    CURRENT_ANGLE = 0
    global ONE_PERCENT #making theese words globle globle
    global FLIFT

    def __init__ (self, motorobject, maxangle): #creating a functions to set it up
        global FLIFT
        global ONE_PERCENT
        FLIFT = motorobject
        FLIFT.reset_angle(0)
        ONE_PERCENT = maxangle/100 

        return

    def down(self,speed,pct): #creating a function to go down
        FLIFT.run_angle(speed, pct * ONE_PERCENT * -1, then=Stop.HOLD, wait=True)

    def up(self,speed,pct): #creating a function to go up
        FLIFT.run_angle(speed, pct * ONE_PERCENT, then=Stop.HOLD, wait=True)

    def run_until_stalled(self,speed):
        FLIFT.run_until_stalled(speed)
