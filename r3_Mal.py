#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, door, r_color, l_color
from turning import gyroRight, gyroLeft

def run3():
    driver.settings(straight_speed=200) #setting the speed when you go straight to always be 200
    driver.straight(445) #goes straight to bench driving health units and innovation challenge
    driver.stop() #stops
    driver.straight(-20)
    driver.stop()
    door.up(200,10)
    driver.stop()
    gyroRight(15)
    driver.straight(-450)
    door.down(200,10)
    driver.stop()
