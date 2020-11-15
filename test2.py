#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, fork, r_color, l_color, dumper,dumpMotor
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack

dumpMotor.run_until_stalled(100, then=Stop.COAST, duty_limit=None)
dumper.down(300,100)
wait(200)
dumper.up(300,100)
#driver.settings(straight_speed=200)
#driver.straight(200)

#dump.up()


