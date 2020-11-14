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

driver.settings(straight_speed=200) #setting the speed when you go straight to always be 200

#drive to bench
driver.straight(450) #goes straight to bench driving health units and innovation challenge
driver.stop() #stops 
fork.down (160,25) #forklift moves down
driver.straight(-20) #driver moves back slightly back as to not hit innovation challenge and health
driver.stop() #stops
driver.turn(-25) #turn and knock the bench down
driver.straight(-230)#backup and turn to face bench
driver.stop()#stops
driver.turn(-80) #turns to be almost parallel to the bench
driver.straight(270) #moves to be around bench
driver.stop() #stops
driver.turn(90) #turns to face bench
fork.down (200,40) #forklift moves to be under the height of the bench handle
driver.straight(300) #drives straight to bench. use bench to square up with handle
driver.stop() #stops
fork.up(160,60) #forklift moves up to grab handle
driver.straight(-500) #drive backwards towards home
driver.stop() #Stops

####YAYAYAYAYAYAY####
