#!/usr/bin/env micropython

from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_B, OUTPUT_C, SpeedRPM, SpeedPercent, SpeedNativeUnits, follow_for_ms, follow_for_forever
import time



bot = MoveTank(OUTPUT_B,OUTPUT_C)
spkr = Sound()
l_color = ColorSensor(INPUT_1)
r_color = ColorSensor(INPUT_4)
gyro = GyroSensor(INPUT_2)
bot.gyro = GyroSensor(INPUT_2)


bot.gyro.calibrate()
bot.cs = ColorSensor(INPUT_4)
spkr.beep()
bot.turn_right(SpeedNativeUnits(100),75)
spkr.beep()
bot.stop()
while r_color.color != 1:
    # when robot finds black line, it follows the black line to the bridge
    bot.on(SpeedNativeUnits(100),SpeedNativeUnits(100))


bot.stop()
bot.follow_line(
    kp=10, ki=0.01, kd=3.2,
    speed=SpeedNativeUnits(100),
    follow_left_edge=True,
    target_light_intensity=7,
    white=60,
    follow_for=follow_for_forever
)




bot.stop()

#bot.follow_gyro_angle(11.3, 0.05, 3.2,SpeedPercent(10),45)

# bot.on_for_seconds(SpeedPercent(10),SpeedPercent(10),2)

# bot.turn_right(SpeedPercent(15),45,True)

# time.sleep(2)
# bot.turn_left(SpeedPercent(15),45,True)
# time.sleep(2)
# bot.on_for_seconds(SpeedPercent(-10),SpeedPercent(-10),2)


