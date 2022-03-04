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
angle = 0

# *** CONSTANTS ***
x = 0
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

# Initialize the motors.
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

# Intialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=68.8, axle_track=126)

# Go in straight line
for i in range(y):
    robot.straight(ConvertToInches(i))
    ev3.screen.draw_text(50, 50, i)
    wait(250)

ev3.speaker.beep()