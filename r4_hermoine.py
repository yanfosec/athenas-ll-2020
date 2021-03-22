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

def run5():
   #reset gyro
   gyro.reset_angle(0)
   driver.settings(straight_speed=350)
   driver.straight(-10)
   #positioned the robot for the run
   driver.straight(100)
   driver.stop()
   gyroRight(53)
   driver.stop()
   # find the black line and turns to go straight back
   driver.straight(410)
   driver.stop()
   gyroLeft(53)
   driver.stop()
   driver.straight(325)#drives straight to be parrallle to bball hoop
   driver.stop()
   gyroLeft(28) #turn to bball hoop
   driver.stop()
   driver.settings(straight_speed=100)
   driver.straight(187) #goes to bball hoop
   driver.straight(-50)
   driver.stop()#stop because its important
   gyroRight(gyro.angle()*-0.91) #turns over to botci
   driver.stop()
   driver.settings(straight_speed=150)
   driver.straight(70) #goes to botchi tipping red cube out
   driver.stop()
   driver.straight(-75) #backs up from botchi
   driver.stop()
   driver.settings(straight_speed=350)
   gyroRight(90)#turns to be paralelle to dance floor
   driver.stop()
   driver.straight(320) #goes to be next to dance floor
   driver.stop()
   gyroLeft(90)#turns to dance floor
   driver.straight(150)#
   while True: #basicly a forever loop
      driver.straight(20)#danceeeee like theres no tommorow 
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
      ev3.speaker.say("bootsandcatsaandbootsandcats") #telling it to say whatever we want
