#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, door, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor, Dump
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
import time
from turning import gyroRight,gyroLeft
from dump import Dump

def run2():
    driver.settings(straight_speed=300)
    #drive to the dance floor
    door.up(150,50)#lifts door uo 50%
    gyroRight(28)#turns right to face dance floor health
    driver.straight(935) #drives to dance floor
    driver.stop()
    door.down(150,50)
    driver.stop() #stops for gyro
    gyroRight(65) #turns to face black line
    driver.settings(straight_speed=125) #set straight speed
    while r_color.reflection() >12: #goes to black line 
        driver.drive(125, 0)
    driver.stop() #stops
    driver.straight(145) #moves stright to get around target
    driver.stop()#stops for gyro
    gyroRight(65)#turns to get dump facting target
    driver.stop() #stops
    driver.straight(-25) #moves backwards to get dumper over target
    driver.stop()
    dumper.down(350,95) #moves dumper down 90% to dump blocks
    driver.straight(10) #move forward to not catch on target
    driver.stop()
    dumper.up(300,30) #dumper moves up 30% to get lined up with flip
    driver.straight(125) #moves forward to be at right distance to flip
    driver.stop() #stops for gyro
    gyroRight(40) #turns to line up wiht flip
    driver.straight(-55) #backward so flip is in dump and turn flip
    driver.straight(10) #forward for +special effects+ (also so we knock flip sligly)
    dumper.up(150,10) #dump moves up to flip
    driver.straight(10) #forward to not catch
    dumper.up(150,10) #moves up to finish fliping the flip
    driver.straight(50) #goes forward to 
    driver.stop()#
    driver.settings(straight_speed=300)
    driver.stop() 
    gyroRight(20)
    driver.stop()
    driver.straight(50)
    door.up(125,45)
    driver.stop()
    driver.settings(straight_speed=300)
    driver.straight(70)
    driver.stop()
    driver.straight(-72)
    driver.stop()
    door.down(100,45)
    dumper.up(300,40)
    gyroRight(41)
    driver.straight(400)
    driver.stop()
    gyroLeft(95)
    door.up(100,80)
    driver.straight (496)
    driver.stop()
    door.down(100,75)
    gyroRight(90)
    driver.straight(803)
