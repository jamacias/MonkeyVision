#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, SpeedPercent, MoveSteering
from ev3dev2.sensor import INPUT_1
from MVColorSensor import *
from time import sleep, time

class MVFollowLine:
    def __init__(self):
        self.colorSensor = MVColorSensor()
        self.steeringDrive = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.oldError = 0.01
        self.timer = 0

    def followLine(self):
        isRed = False
        self.timer = time()
        while not isRed:
            self._followLine(self.oldError)
            if (time() - self.timer) > 100:
                isRed = self._isRed(self.colorSensor.getRGB())

        self.steeringDrive.off()

    def lookForLine(self, speed=-40):
        intensity = self.colorSensor.getRefectionLight()
        while intensity < 17: # prev 20
            print(intensity)
            self.steeringDrive.on(0, SpeedPercent(speed))
            intensity = self.colorSensor.getRefectionLight()

    def turnOnLine(self):
        epsilon = 10
        while True:
            intensity = self.colorSensor.getRefectionLight()
            if 18 < intensity and intensity < 22:
                self.steeringDrive.on_for_seconds(0, SpeedPercent(-30), 2)
                break
            else: 
                self._followLine(self.oldError)

    def _followLine(self, oldError, kp=100, ki=0):
        intensity = self._mapping(self.colorSensor.getRefectionLight())
        speed = -20
        self.steeringDrive.on(0.7*intensity, SpeedPercent(speed))
        
        #self.oldError = intensity

    def _mapping(self, x):
        if x <= 20:
            return max(100/12*x - 1000/6, -100)

        return min(5*x-100, 100)

    # red : 150, 175, 286
    # white:  137, 151, 181
    # black: 38, 32, 40
    # yellow: 190, 143, 40
    def _isRed(self, rgb):
        return rgb[0] > 145 and rgb[1] > 165 and rgb[2] > 250
    