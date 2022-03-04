#!/usr/bin/env python3     
from ev3dev2.motor import LargeMotor   #we're importing the motor function
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM #we're importing other functions related to speed
from time import sleep


lm = LargeMotor()    #defining a large motor
'''
This will run the large motor at 50% of its
rated maximum speed of 1050 deg/s.
50% x 1050 = 525 deg/s     
'''
lm.on_for_seconds(speed = 50, seconds=5)    #speed represents the percentage of the rated maximum speed of the motor. 
sleep(1)