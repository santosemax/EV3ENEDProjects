#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# INPUTS
laps = 3
angle = 180

# CONSTANTS
x = 0
y = 120
lengths = laps * 2

# Adjustments
if angle > 0:
    angle -= 5 # Account for motor difference for turning

# FUNCTIONS
def ConvertMM(num):
    return num * 10

# Create your objects here.
ev3 = EV3Brick()

# random stuff
ev3.speaker.say("I'm an elephant")
ev3.speaker.play_file(SoundFile.ELEPHANT_CALL)
ev3.screen.load_image(ImageFile.DIZZY)

# Initialize the motors.
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

# Intialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=68.8, axle_track=126)

# Run the laps
flip = False
for i in range(lengths):
    flip = not flip
    if angle == 0:
        robot.straight(ConvertMM(y) if flip else -ConvertMM(y))
    else:
        robot.straight(ConvertMM(y))
        robot.turn(angle) if flip else robot.turn(-angle)

        # DEBUG
        #ev3.screen.draw_text(50, 50, robot.angle())

    wait(1000)


ev3.speaker.beep()