#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver
from pybricks.parameters import Port, Direction, Color, Button
from pybricks.tools import wait
from pybricks.robotics import DriveBase
#from pybricks.media.ev3dev import SoundFile
from r3_Mal import run3 
from r2_nico import run2
from r5_step import run4
#######################
## Main Program      ##
#######################

ev3.speaker.set_volume(100)
ev3.speaker.set_speech_options(language='el',voice='f3',speed=60)
ev3.speaker.say("lets go athenas  we got this")

while True: #basicly a forever loop
    while not any(ev3.buttons.pressed()): #if no buttons are being pressed wait
        wait(10)

    if Button.LEFT in ev3.buttons.pressed(): #if the left buttion is pressed run run1
        ev3.speaker.beep() #beeping to let us know it started
        wait(20) #wait to give us time to move finger up
        run1()
        driver.stop 
        ev3.speaker.beep()#beeping to let us know it stoped

    if Button.DOWN in ev3.buttons.pressed(): #if the down button is pressed run run 4
        ev3.speaker.beep()
        wait(20)
        run4()
        driver.stop()
        ev3.speaker.beep()

    if Button.UP in ev3.buttons.pressed(): #if up button is pressed run run 2
        ev3.speaker.beep()
        wait(20)
        run2()
        driver.stop()
        ev3.speaker.beep()

    if Button.RIGHT in ev3.buttons.pressed():#if the right button is pressed run run 3
        ev3.speaker.beep()
        wait(20)
        run3()
        driver.stop()
        ev3.speaker.beep()

    if Button.CENTER in ev3.buttons.pressed():#if the center button is pressed run run 5
        ev3.speaker.beep()
        wait(20)
        run5()
        driver.stop()
        ev3.speaker.beep()


#its the final countdown 
#dododoododududodododododudodododoodoooooooooooooo

