#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveSteering, MoveTank, MediumMotor
from MVInfrared import *
from MVFollowLine import *
from time import time

class SecondStage:
    def __init__(self):
        self.mvFollowLine = MVFollowLine()
        self.steeringDrive = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.moveTank = MoveTank(OUTPUT_B, OUTPUT_C)
        self.mediumMotor = MediumMotor(OUTPUT_D)
        self.mvInfrared = MVInfraredSensor()

    def start(self):
        
        # reach line
        #self.goUntilDistanceFromWall(27)
        self.mvFollowLine.lookForLine()
        self.steeringDrive.on_for_seconds(0, SpeedPercent(-40), 0.6)
        # turn left
        self.moveTank.on_for_rotations(SpeedPercent(40), SpeedPercent(-40), 1.4)
        # push button on left
        self.goUntilDistanceFromWall(17)
        # go back wee bit
        self.moveTank.on_for_rotations(SpeedPercent(40), SpeedPercent(40), 2.8)
        # turn left
        self.moveTank.on_for_rotations(SpeedPercent(40), SpeedPercent(-40), 1.33)
        # go to the ramp
        #self.goUntilDistanceFromWall(25)
        self.mvFollowLine.lookForLine()
        self.steeringDrive.on_for_seconds(0, SpeedPercent(-40), 0.4)
        # turn left
        self.moveTank.on_for_rotations(SpeedPercent(40), SpeedPercent(-40), 1.35)
        # go up
        self.mvFollowLine.lookForLine()
        self.moveTank.on_for_rotations(SpeedPercent(-100), SpeedPercent(-100), 10.5)
        
        timer = time()
        while time() - timer < 5:
            self.mvFollowLine._followLine(0)
        
        self.moveTank.on_for_rotations(SpeedPercent(20), SpeedPercent(-20), 0.1)
        self.moveTank.on_for_rotations(SpeedPercent(-100), SpeedPercent(-100), 6)
        self.mvFollowLine.lookForLine()
        self.moveTank.on_for_rotations(SpeedPercent(40), SpeedPercent(-40), 2.5)
        self.moveTank.on_for_rotations(SpeedPercent(40), SpeedPercent(40), 0.7)

        self.mediumMotor.on_to_position(5, -80)
        self.moveTank.on_for_rotations(SpeedPercent(-100), SpeedPercent(-100), 0.9)
        self.moveTank.on_for_rotations(SpeedPercent(40), SpeedPercent(-40), 0.4)
        self.moveTank.on_for_rotations(SpeedPercent(-100), SpeedPercent(-100), 4)
        self.mvFollowLine.lookForLine()
        self.mediumMotor.on_to_position(5, 0)

        timer = time()
        while time() - timer < 3:
            self.mvFollowLine._followLine(0)

        self.moveTank.on_for_rotations(SpeedPercent(-40), SpeedPercent(40), 0.15)
        
        self.moveTank.on_for_rotations(SpeedPercent(-100), SpeedPercent(-100), 11)
        self.goUntilDistanceFromWall(40)
        self.moveTank.on_for_rotations(SpeedPercent(-40), SpeedPercent(40), 1.3)
        self.mvFollowLine.lookForLine()
        self.moveTank.on_for_rotations(SpeedPercent(40), SpeedPercent(40), 1.0)

        self.moveTank.on_for_rotations(SpeedPercent(-100), SpeedPercent(100), 10)
        self.mvFollowLine._followLine(0)



    def goUntilDistanceFromWall(self, distance, speed=-40):
        while True:
            self.steeringDrive.on(0, SpeedPercent(speed))
            print(self.mvInfrared.getDistance())
            if self.mvInfrared.getDistance() < distance:
                self.steeringDrive.off()
                break

        self.steeringDrive.on_for_seconds(0, SpeedPercent(speed/2), 0.5)
        return