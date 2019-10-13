#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, SpeedPercent, MoveSteering
from MVFollowLine import *

class FirstStage:
    def __init__(self):
        self.mvFollowLine = MVFollowLine()
        print("First stage")
    
    def start(self):
        # move over start line
        steeringDrive = MoveSteering(OUTPUT_B, OUTPUT_C)
        steeringDrive.on_for_seconds(0, SpeedPercent(-40), 4)

        # find and follow line
        self.mvFollowLine.lookForLine(-40)
        self.mvFollowLine.followLine()

        steeringDrive.on_for_seconds(0, SpeedPercent(-40), 2)

        print("First over")

first = FirstStage()
first.start()