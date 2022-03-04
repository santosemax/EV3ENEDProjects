#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# *** INPUTS ***
laps = 0.5     # 0.5 for straight line and 1 for turning
angle = 90

# *** CONSTANTS ***
x = 12
y = 12

lengths = laps * 2

# Adjustments to variables
if angle > 0:
    angle -= 5 # Account for motor difference for turning


# *** FUNCTIONS ***

# Convert mm to centimeters
def ConvertToCM(num):
    return num * 10

# Convert mm to inches
def ConvertToInches(num):
    return num / 25.4

# Create your objects here.
ev3 = EV3Brick()

# random stuff
#ev3.speaker.say("I'm an elephant")
#ev3.speaker.play_file(SoundFile.ELEPHANT_CALL)
#ev3.screen.load_image(ImageFile.DIZZY)

# Initialize the motors.
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

# Intialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=68.8, axle_track=126)

# Go in straight line and output current distance traveled (in) to screen
for i in range(y):
    if angle == 0:
        robot.straight(ConvertToInches(i))
        ev3.screen.draw_text(50, 50, i)
        wait(250)
        ev3.screen.clear()
    else:
        robot.straight(ConvertToInches(y))
        # Turn at end of y
        if i == y:
            robot.turn(angle)
            ev3.screen.draw_text(30, 50)
            wait(250)
            # Go straight for second distance, x
            for k in range(x):
                robot.straight(ConvertToInches(x))
                ev3.screen.draw_text(20, 50, k)
                wait(1000)
                ev3.screen.clear()




ev3.speaker.beep()