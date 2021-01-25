#!/usr/bin/env pybricks-micropython

from robotsetup import ev3, driver, r_color, l_color, gyro, l_DriveMotor, r_DriveMotor
from turning import gyroLeft, gyroRight, gyroTurnTo
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack



#reset gyro
gyro.reset_angle(0)
driver.settings(straight_speed=300)
#positioned the robot for the run
driver.straight(100)
driver.stop()
gyroRight(50)
driver.stop()

# find the black line and turns to go straight back
while l_color.reflection() >10:
   driver.drive(135, 0)
driver.stop()
gyroLeft(50)
driver.stop()
driver.straight(320)#drives straight to be parrallle to bball hoop
driver.stop()
gyroLeft(35) #trun to bball hoop
driver.stop()
driver.straight(155) #goes to bball hoop
driver.stop()
gyroRight(gyro.angle()*-0.96)
ev3.speaker.beep()
driver.stop()
driver.straight(75)
driver.stop()
driver.straight(-75)
driver.stop()
gyroRight(90)
driver.stop()
driver.straight(320)
driver.stop()
gyroLeft(90)
driver.straight(70)
while True: #basicly a forever loop
   driver.straight(20)
   driver.stop()
   gyroRight(180)
   driver.stop()
   driver.straight(-20)
   driver.straight(10)
   driver.stop()
   gyroLeft(140)
   driver.stop()
   gyroRight(100)
   driver.stop()
   gyroLeft(90)
   driver.straight(10)
   ev3.speaker.set_volume(100) #telling the speker to talk at volume 100 aka 100%
   ev3.speaker.set_speech_options(language='el',voice='f3',speed=60) #settieng the accent to greek the
   #voice to female and the speed 100 wpm
   ev3.speaker.say("YAAAAAAAAAAAAAAYYYYYYYYYYYYY") #telling it to say whatever we want


        











# # goes back until it sees the second black line 
# counter = 0
# ev3.speaker.beep()
# while counter < 2:
#     while l_color.reflection() >9:
#         driver.drive(125, 0)
#         #followBlack(r_color, 150)
#     counter = counter + 1
#     ev3.speaker.beep() 
# driver.stop()
# driver.straight(10)
# driver.stop()
# driver.straight(30)
# driver.stop()

# turns toward the basketball hoop 
# gyroLeft(40)
# driver.stop()

# goes straight until the cube is dumped
# driver.straight(210)
# driver.stop()
 #gyroRight(85)
# driver.straight(255)
# driver.stop()
# for x in range (5):
#     gyroRight(50)
#     gyroLeft(50)