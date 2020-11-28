#!/usr/bin/env micropython

from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, Motor, MoveTank, OUTPUT_B, OUTPUT_C, SpeedRPM, SpeedPercent, SpeedNativeUnits, follow_for_ms, follow_for_forever
import time


# Connect two large motors on output ports B and C:
#motors = [LargeMotor(address) for address in (OUTPUT_B, OUTPUT_C)]

bot = MoveTank(OUTPUT_B,OUTPUT_C)
spkr = Sound()
l_color = ColorSensor(INPUT_1)
r_color = ColorSensor(INPUT_4)
gyro = GyroSensor(INPUT_2)
bot.gyro = GyroSensor(INPUT_2)


bot.gyro.calibrate()
bot.cs = ColorSensor(INPUT_4)
spkr.beep()
bot.turn_right(SpeedRPM(30),75)
spkr.beep()
bot.on(SpeedRPM(30), SpeedRPM(30))
while r_color.reflected_light_intensity > 10:
    time.sleep(1)
    

bot.stop()

bot.follow_line(
    kp=11.3, ki=0.05, kd=3.2,
    speed=SpeedRPM(20),
    follow_for=follow_for_forever
)




# bot.stop()

#bot.follow_gyro_angle(11.3, 0.05, 3.2,SpeedPercent(10),45)

# bot.on_for_seconds(SpeedPercent(10),SpeedPercent(10),2)

# bot.turn_right(SpeedPercent(15),45,True)

# time.sleep(2)
# bot.turn_left(SpeedPercent(15),45,True)
# time.sleep(2)
# bot.on_for_seconds(SpeedPercent(-10),SpeedPercent(-10),2)


