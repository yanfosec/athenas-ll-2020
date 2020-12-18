#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Door:

    CURRENT_ANGLE = 0
    global ONE_PERCENT
    global DOORA

    def __init__ (self, motorobject, maxangle):
        global DOORA
        global ONE_PERCENT
        DOORA = motorobject
        DOORA.reset_angle(0)
        ONE_PERCENT = maxangle/100

        return
    
    def up (self, speed, pct):
        DOORA.run_angle(speed, pct * ONE_PERCENT * -1, then=Stop.HOLD, wait=True)

    def down (self, speed, pct):
        DOORA.run_angle(speed, pct * ONE_PERCENT, then=Stop.HOLD, wait=True)