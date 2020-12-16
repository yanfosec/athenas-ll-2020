#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver
from pybricks.parameters import Port, Direction, Color, Button
from pybricks.tools import wait
from pybricks.robotics import DriveBase
#from pybricks.media.ev3dev import SoundFile
from r3_Mal import run3 
from r2_nico import run2
#######################
## Main Program      ##
#######################

while True:
    while not any(ev3.buttons.pressed()):
        wait(10)

    if Button.LEFT in ev3.buttons.pressed():
        ev3.speaker.beep()
        wait(20)

    if Button.UP in ev3.buttons.pressed():
        ev3.speaker.beep()
        wait(20)
        run2()
        driver.stop()
        ev3.speaker.beep()

    if Button.RIGHT in ev3.buttons.pressed():
        ev3.speaker.beep()
        wait(20)
        run3()
        driver.stop()
        ev3.speaker.beep()

#its the final countdown 
#dododoododududodododododudodododoodoooooooooooooo

