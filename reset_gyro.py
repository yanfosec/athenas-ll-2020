#!/usr/bin/env micropython

from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sensor import INPUT_2


def resetGyro():
    gyro = GyroSensor(INPUT_2)
    gyro.calibrate()

resetGyro()