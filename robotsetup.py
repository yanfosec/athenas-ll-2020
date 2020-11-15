#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from forklift import Forklift
from dump import Dump

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


## SET UP THE DRIVE CHASIS ##
ev3 = EV3Brick()
l_DriveMotor = Motor(Port.C)
r_DriveMotor = Motor(Port.B)
driver = DriveBase(l_DriveMotor,r_DriveMotor,68.8,111)

## CREATE THE FORKLIFT ##
f_motor = Motor(Port.A)
fork = Forklift(f_motor, 650)

#DUMP
dumpMotor = Motor(Port.D)
dumper = Dump(dumpMotor, 165)

## CREATE THE COLOR SENSORS ##
r_color = ColorSensor(Port.S4) 
l_color = ColorSensor(Port.S1)

## SET UP THE SENSORS ##
gyro = GyroSensor(Port.S2)
