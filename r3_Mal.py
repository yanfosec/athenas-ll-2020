#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, door, r_color, l_color
from turning import gyroRight, gyroLeft

def run3():
    driver.straight(-10) #making run three a function for main to cut down on start up time
    driver.stop()
    driver.settings(straight_speed=400) #setting the speed when you go straight to always be 200
    driver.straight(300)
    driver.stop()
    gyroRight(6)
    driver.straight(125) #goes straight to bench driving health units and innovation challenge
    door.run_until_stalled(300)
    driver.stop() #stops
    gyroLeft(130)
    driver.stop() #stops for gyro
    #gyroRight(10)
    #driver.straight(-350) #drives backwards to home
    #driver.stop()
    #gyroLeft(70)
    driver.straight(550)
    driver.stop() #stops to end program
