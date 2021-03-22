#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Door: #creacting the class

    CURRENT_ANGLE = 0 
    global ONE_PERCENT #making these words global
    global DOORA

    def __init__ (self, motorobject, maxangle): #creating a function to set up the thing
        global DOORA
        global ONE_PERCENT
        DOORA = motorobject
        DOORA.reset_angle(0)
        ONE_PERCENT = maxangle/100
        #DOORA.control.stall_tolerances(7,1000)
    
    def up (self, speed, pct): #creating a function for up
        global ONE_PERCENT
        DOORA.run_angle(speed, pct * ONE_PERCENT * -1, then=Stop.HOLD, wait=False)
        print("Status: " + str(DOORA.control.done()))
        while not DOORA.control.done():
            if DOORA.control.stalled():
                print("Status up = stalled ")              
                DOORA.hold()
                break
        return DOORA.angle()/ONE_PERCENT*-1


    def down (self, speed, pct): #creating a function for down
        DOORA.run_angle(speed, pct * ONE_PERCENT, then=Stop.HOLD, wait=False)
        while not DOORA.control.done():
            if DOORA.control.stalled():
                print("Status down = stalled") 
                DOORA.hold()
                break
        return DOORA.angle()/ONE_PERCENT*-1



    def run_until_stalled(self, speed):
        DOORA.run_until_stalled(speed)
        return DOORA.angle()/ONE_PERCENT*-1


    