#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, fork, r_color, l_color
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack

driver.straight(500)
while l_color.reflection() > 12:
    driver.drive(150,0)
driver.straight(30)
while l_color.reflection() > 12:
    driver.drive(25,0)
    wait(1000)
    driver.stop()
    driver.straight(-10)
    driver.stop()
driver.reset()
while driver.distance() < 100:
    driver.drive(25,0)
    wait(1000)
    driver.stop()
    driver.straight(-10)
    driver.stop()

