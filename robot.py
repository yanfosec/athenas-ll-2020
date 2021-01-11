#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

## SET UP THE DRIVE CHASIS ##
class Robot(DriveBase):
    def __init__(self,l_motor,r_motor,diameter,distance,gyro_sensor):
        super().__init__(l_motor.r_motor,diameter,distance)
        gyro = gyro_sensor
        speed = 150

    def turnRight(degree)
        return True

    def turnLeft(degree)
        return True

    def goForward(cm)
        return True

    def goBackword(cm)
        return True

