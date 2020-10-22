#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Forklift:

    CURRENT_ANGLE = 0
    global ONE_PERCENT
    global FLIFT

    def __init__ (self, motorobject, maxangle):
        global FLIFT
        global ONE_PERCENT
        FLIFT = motorobject
        #FLIFT.run_time(100,6000, then=Stop.HOLD, wait=True)
        FLIFT.reset_angle(0)
        ONE_PERCENT = maxangle/100 

        #forkmotor = Moftor(Port.A)
        #forkmotor.run_time(500, 20000, then=Stop.HOLD, wait=True)
        return
    
    def up (self, speed, pct):
        FLIFT.run_angle(speed, pct * ONE_PERCENT * -1, then=Stop.HOLD, wait=True)

    def down (self, speed, pct):
        FLIFT.run_angle(speed, pct * ONE_PERCENT, then=Stop.HOLD, wait=True)
