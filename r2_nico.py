#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, door, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor, dumper
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
import time
from turning import gyroRight,gyroLeft
from dump import Dump


def run2():
    driver.settings(straight_speed=450)
    driver.straight(250)
    driver.straight(-140)
    driver.stop()
    gyroRight(85)
    driver.straight(-250)
    driver.stop()
    driver.settings(straight_speed=500)
    l_DriveMotor.run_time(-600,4000)#runs treadmill
    driver.stop()
    driver.straight(260)#gets off treadmill
    driver.stop()
    gyroLeft(70)#facing wall
    driver.straight(200)
    driver.straight(-160)
    driver.stop()
    gyroRight(87)#facing home
    driver.straight(300)
    driver.stop()
    while r_color.reflection()<90:
        driver.drive(150,0)
    driver.stop()
    driver.straight(150)
    driver.stop()
    #run2 starts
    driver.settings(straight_speed=450)
    gyroLeft(90)
    driver.straight(350)#wall square
    driver.straight(-690)
    driver.stop()
    driver.settings(straight_speed=300)
    dumper.down(350,95) #moves dumper down 90% to dump blocks
    #driver.straight(470) #move forward to GO UNDER BRIDGE
    #driver.straight(-375) #goes backwards go go back to target
    driver.stop()
    driver.straight(100)
    dumper.up(300,30) #dumper moves up 30% to get lined up with flip
     #moves forward to be at right distance to flip
    driver.stop() #stops for gyro
    gyroRight(30) #turns to line up wiht flip
    driver.straight(-55) #backward so flip is in dump and turn flip
    driver.straight(10) #forward for +special effects+ (also so we knock flip sligly)
    dumper.run_until_stalled(100)
    driver.straight(50) #goes forward to finish the dump
    driver.stop()
    driver.settings(straight_speed=500) #changing the speed so its faster to cut down on time 
    #(we get speedy)
    driver.stop() #stops for gyro
    gyroRight(20) #turns overso we are in line with the slide
    driver.stop() #stops because its inportant to do that
    driver.straight(30) #goes forward so we are by the slide 
    driver.stop()
    pct = door.up(300,48)
    print("PCT: " + str(pct))
    while pct <= 47.5:
        driver.straight(-20)
        driver.stop()
        pct = door.up(500, 48 - pct)
        print("PCT: " + str(pct))
    driver.stop()
    driver.straight(95) #goes straight to actually knock them down
    driver.stop()
    driver.straight(-120) #goes backwards so we down hurt our robot by turning them
    driver.stop()
    door.down(100,45) #brings door down so we don't accidently hit something
    dumper.run_until_stalled(300) #brings dump up becuse we don't want to forget and get penilized 
    driver.stop()
    gyroRight(41) #turns so we are facing bench/baskitball area
    driver.straight(440) #drives so we are parallel
    driver.stop() #stops because the gyro dosn't like us when we don't
    gyroLeft(88) #turns so we are facing little dudes
    driver.settings(straight_speed=250)
    door.up(100,80) #brings door up to prepare to trap little dudes
    driver.straight (530) #drives forward to trap little dudes
    driver.stop()
    driver.settings(straight_speed=400)
    door.down(100,80) #now actually finally traps little dudes
    gyroRight(80) #turns right to face home
    driver.straight(803) #drives into home

