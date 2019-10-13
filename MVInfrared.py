#!/usr/bin/env python3
from ev3dev2.sensor.lego import InfraredSensor

class MVInfraredSensor:
    def __init__(self, port=None):
        self.infrared = InfraredSensor(port)
        self.infrared.mode = "IR-PROX"
    
    def getDistance(self):
        value = self.infrared.value()
        realDistance = (value/100)*70
        return realDistance