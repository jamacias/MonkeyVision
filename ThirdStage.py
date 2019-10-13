#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, SpeedPercent, MoveSteering, MoveTank
from MVInfrared import *
from MVFollowLine import *
from time import sleep

class ThirdStage:
    def __init__(self):
        self.steeringDrive = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.moveTank = MoveTank(OUTPUT_B, OUTPUT_C)
        self.mvInfrared = MVInfraredSensor()

    def Start(self):
        # go until wall
        self.goUntilDistanceFromWall(41)

        # turn right
        self.moveTank.on_for_rotations(SpeedPercent(-40), SpeedPercent(40), 1.33)
        #self.steeringDrive.on(100, SpeedPercent(40))

        # go until wall
        self.goUntilDistanceFromWall(36.4)

        # turn right
        self.moveTank.on_for_rotations(SpeedPercent(-40), SpeedPercent(40), 1.33)
        #self.steeringDrive.on(100, SpeedPercent(40))

        sleep(4)
        
        self.steeringDrive.on_for_seconds(0, SpeedPercent(-100), 6)


    def goUntilDistanceFromWall(self, distance, speed=-40):
        while True:
            #self.moveTank.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), 0.25)
            self.steeringDrive.on(0, SpeedPercent(speed))
            print(self.mvInfrared.getDistance())
            if self.mvInfrared.getDistance() < distance:
                self.steeringDrive.off()
                return
