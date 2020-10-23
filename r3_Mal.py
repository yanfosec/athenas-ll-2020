#!/usr/bin/env pybricks-micropython
#import codes
from robotsetup import ev3, driver, fork, r_color, l_color
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack

driver.settings(straight_speed=200)

#drive to bench
driver.straight(450)
driver.stop()
fork.down (160,25)
driver.straight(-20)
driver.stop()
#turn and knock the bench down
driver.turn(10)
#backup and turn to face bench
driver.straight(-230)
driver.stop()
driver.turn(80)
driver.straight(220)
driver.stop()
driver.turn(-90)
#get bench top and backup to base
fork.down (160,55)
driver.straight(300)
driver.stop()
fork.up(160,60)
driver.straight(-500)
driver.stop()
