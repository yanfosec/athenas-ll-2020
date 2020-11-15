#!/usr/bin/env pybricks-micropython
from robotsetup import ev3, driver, fork, r_color, l_color, gyro
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from linefollow import followBlack
from turning import gyroRightTo, gyroLeftTo, gyroTurnTo
import time

#######################################################################
## Run Code Starts Here                                              ##
#######################################################################



gyroTurnTo(45)
time.sleep(5)
# print("Currently at: " + str(gyro.angle()))
# gyroTurnTo(90)
# time.sleep(5)
# print("Currently at: " + str(gyro.angle()))
# gyroTurnTo(45)
# time.sleep(5)
# print("Currently at: " + str(gyro.angle()))
# gyroTurnTo(0)
# print("Currently at: " + str(gyro.angle()))


# gyro.reset_angle(0)

# print("Start at " + str(gyro.angle()))
# gyroRight(90)
# print("End at " + str(gyro.angle()))
# gyroLeft(gyro.angle())
# while gyro.angle() != 0:
#     if gyro.angle()>1:
#         gyroLeft(-1*gyro.angle())
#     else:
#         gyroRight(gyro.angle())

# print("End at " + str(gyro.angle()))

# # print("Gyro Turns")
# # for x in range(5):
# #     gyroRight(89)
# #     print(str(gyro.angle()))
# #     time.sleep(2)
#     gyroLeft(89)
#     print(str(gyro.angle()))
#     time.sleep(2)
=======
#print(str(calcOffset(gyro)))

# time.sleep(1)
# print("Driver Turns")
# for y in range(10):
#     gyro.reset_angle(0)
#     driver.turn(90)
#     print(str(gyro.angle()))
#     driver.stop()
#     time.sleep(1)
#     gyro.reset_angle(0)
#     driver.turn(-90)
#     print(str(gyro.angle()))
#     driver.stop()
#     time.sleep(1)
