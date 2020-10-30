#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, gyro, l_DriveMotor, r_DriveMotor
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

GYRO_CALIBRATION_LOOP_COUNT = 200
GYRO_OFFSET_FACTOR = 0.0005

def calcOffset(thisSensor):
    # Calibrate the gyro offset. This makes sure that the robot is perfectly
    # still by making sure that the measured rate does not fluctuate more than
    # 2 deg/s. Gyro drift can cause the rate to be non-zero even when the robot
    # is not moving, so we save that value for use later.
    while True:
        gyro_minimum_rate, gyro_maximum_rate = 440, -440
        gyro_sum = 0
        for _ in range(GYRO_CALIBRATION_LOOP_COUNT):
            gyro_sensor_value = thisSensor.angle()
            gyro_sum += gyro_sensor_value
            if gyro_sensor_value > gyro_maximum_rate:
                gyro_maximum_rate = gyro_sensor_value
            if gyro_sensor_value < gyro_minimum_rate:
                gyro_minimum_rate = gyro_sensor_value
            wait(5)
        if gyro_maximum_rate - gyro_minimum_rate < 2:
            break
    gyro_offset = gyro_sum / GYRO_CALIBRATION_LOOP_COUNT

    return gyro_offset

def turnBot(thisSensor, direction = 'R', degrees = 90):
    # directions R or L
    turnSpeed = 160
    thisSensor.reset_angle(0)

    if direction == 'R':
        while thisSensor.angle() <= degrees:
            r_DriveMotor.run(-1 * turnSpeed)
            l_DriveMotor.run(turnSpeed)
    else:
        while thisSensor.angle() >= -1 * degrees:
            r_DriveMotor.run(turnSpeed)
            l_DriveMotor.run(-1 * turnSpeed)
            

    print(str(thisSensor.angle()))