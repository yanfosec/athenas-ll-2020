#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor
from turning import gyroLeft, gyroRight, gyroRightTo
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
import time
from turning import gyroRight,gyroLeft


#######################################################################
## Run Code Starts Here                                              ##
#######################################################################

def run1():
    driver.settings(straight_speed=450)
    ev3.speaker.beep() # notify done
    # drive until black
    gyro.reset_angle(0)
    driver.stop()
    driver.straight(75)
    driver.stop()
    gyroRight(79)
    driver.stop()
    driver.straight(1450)
    driver.stop()
    gyroRight(80)
    driver.straight(250)
    driver.straight(-150)
    driver.stop()
    gyroRight(85)
    driver.straight(-250)
    driver.stop()
    driver.settings(straight_speed=500)
    l_DriveMotor.run_time(-500,4300)
    driver.stop()
    driver.straight(260)
    driver.stop()
    gyroLeft(50)
    driver.straight(200)
    driver.straight(-160)
    driver.stop()
    gyroRight(88)
    driver.straight(2000)

    

    


    







    # while r_color.reflection() >10:
        # when robot finds black line, it follows the black line to the bridge
        #driver.drive(125, 0)
        #wait(10)
    #driver.stop()

    #ev3.speaker.beep() 
    #while l_color.reflection() >9:
        # Start following the line endlessly.
        #followBlack(r_color, 150)
    #driver.stop()
    #driver.straight(-10)
    #driver.stop()
    # robot turns to go under the bridge
    #gyroLeft(80)

    #driver.straight(400)
    #driver.stop()
    #driver.straight(-420)
    #driver.stop()

    # turns left and goes backwards at the speed of 350 to the treadmill
    #gyroLeft(82)
    #gyro.reset_angle(0)

    #driver.settings(straight_speed=350)
    #driver.straight(-900)
    #driver.stop()
    #r_DriveMotor.run_time(100,2000)

    # turns left wheel backwards for 3550 millaseconds to turn the treadmill 
    #ev3.speaker.beep()
    #l_DriveMotor.run_time(-500,4000)
    #ev3.speaker.beep()
    # goes forwards off of the treadmill
    #driver.straight(300)
    #driver.stop()

    #ev3.speaker.beep() 
    # corrects itself  to go back to the start
    #if gyro.angle()<0:
        #gyroRight(-1 * gyro.angle()+10)
    #else:
        #gyroLeft(gyro.angle()+10)

    #ev3.speaker.beep() 
    #while l_color.reflection() >10:
        #driver.drive(125, 0)
        #wait(10)
    #driver.stop()

    #ev3.speaker.beep() 
    #while True:
        # Start following the line endlessly.
        #followBlack(l_color, 150)
