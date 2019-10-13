#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, SpeedPercent, MoveSteering, MoveTank
from MVInfrared import *
from MVFollowLine import *
from time import time

class FifthStage:
    def __init__(self):
        self.mvFollowLine = MVFollowLine()
        self.steeringDrive = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.moveTank = MoveTank(OUTPUT_B, OUTPUT_C)
        self.mvInfrared = MVInfraredSensor()

    def start(self):
        timer = time()
        while time() - timer < 5:
            self.mvFollowLine._followLine(0)

        self.moveTank.on_for_rotations(SpeedPercent(-40), SpeedPercent(40), -0.3)

        self.moveTank.on_for_rotations(SpeedPercent(-100), SpeedPercent(-100), 3)

        sleep(6.5)

        self.moveTank.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 5)

        sleep(6)
        #self.moveTank.on_for_rotations(SpeedPercent(-40), SpeedPercent(40), -1)
        #sleep(3)

        self.moveTank.on_for_rotations(SpeedPercent(-100), SpeedPercent(-100), 10)

        self.moveTank.on_for_rotations(SpeedPercent(-40), SpeedPercent(40), -1)

        self.mvFollowLine.lookForLine()

        timer = time()
        while time() - timer < 2:
            self.mvFollowLine._followLine(0)

        self.moveTank.on_for_rotations(SpeedPercent(-100), SpeedPercent(-100), 3)

fifth = FifthStage()
fifth.start()