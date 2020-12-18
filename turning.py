#!/usr/bin/env pybricks-micropython

from robotsetup import ev3, driver, fork, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
import time

#######################################################################
## Run Code Starts Here                                              ##
#######################################################################

def gyroRight (degrees):
    startingAngle = gyro.angle()
    finishAngle = startingAngle + degrees
    print("Right --> Starting at: " + str(startingAngle) + " need to turn " + str(degrees) + " Will stop at: " + str(finishAngle))

    turnSpeed = 150
    while gyro.angle() <= finishAngle:
            r_DriveMotor.run(-1 * turnSpeed)
            l_DriveMotor.run(turnSpeed)
    driver.stop()


def gyroLeft (degrees):
    startingAngle = gyro.angle()
    finishAngle = startingAngle - degrees

    print("Left --> Starting at: " + str(startingAngle) + " need to turn " + str(degrees) + " Will stop at: " + str(finishAngle))

    turnSpeed = 150
    while gyro.angle() >= finishAngle:
            r_DriveMotor.run(turnSpeed)
            l_DriveMotor.run(-1 * turnSpeed)
    
    driver.stop()

def trimExtraDegrees ():
        currentAngle = gyro.angle()
        print("Starting Trim at: " + str(currentAngle))
        while currentAngle > 360:
                currentAngle -= 360
        
        while currentAngle < -360:
                currentAngle += 360
        
        gyro.reset_angle(currentAngle)
        print("Returning angle: " + str(gyro.angle()))
        return gyro.angle()

def gyroTurnTo (degree):
        currentAngle = trimExtraDegrees()
        
        while gyro.angle() != degree:
                currentAngle = gyro.angle()
                if currentAngle < degree:
                        if (degree-currentAngle) <= 180:
                                gyroRight(degree-currentAngle)
                        else:
                                gyroLeft((degree-180)+currentAngle)
                else:
                        if (currentAngle-degree) <= 180:
                                gyroLeft(currentAngle-degree)
                        else:
                                gyroRight((360-currentAngle)+degree)
                time.sleep(1)

def gyroRightTo (degree):
        currentAngle = trimExtraDegrees()

        if degree > currentAngle:
                gyroRight(degree-currentAngle)
        else:
                gyroRight(degree+currentAngle)

def gyroLeftTo (degree):
        currentAngle = trimExtraDegrees()

        if currentAngle > degree:
                gyroLeft(currentAngle-degree)
        else:
                gyroLeft(currentAngle-degree)