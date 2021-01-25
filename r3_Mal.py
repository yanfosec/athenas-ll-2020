#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, door, r_color, l_color
from turning import gyroRight, gyroLeft

def run3(): #making run three a function for main to cut down on start up time
    driver.settings(straight_speed=200) #setting the speed when you go straight to always be 200
    driver.straight(445) #goes straight to bench driving health units and innovation challenge
    driver.stop() #stops
    driver.straight(-20) #goes backward to stop door from catching
    driver.stop() #stops
    door.up(200,10) #brings door up to flick bench back off 
    driver.stop() #stops for gyro
    gyroRight(15) #turns right so we can still get in home
    driver.straight(-450) #drives backwards to home
    door.down(200,10) #brings door down so it isnt over the edge
    driver.stop() #stops to end program
