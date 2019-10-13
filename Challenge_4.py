#!/usr/bin/env pybricks-micropython

import pickle
from ev3dev2.sensor.lego import InfraredSensor, ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MoveSteering
import time
import sys
from time import sleep

tank = MoveSteering(OUTPUT_B, OUTPUT_C)

FORWARD, BACKWARD, LEFT, RIGHT, WAIT = range(5)

with open ('maze', 'rb') as fp:
    actions = pickle.load(fp)


for action in actions:
    if action[0] == FORWARD:
        tank.on_for_seconds(steering = 0, speed = 40, seconds=action[1])
    elif action[0] == BACKWARD:
        tank.on_for_seconds(steering = 0, speed = -40, seconds=action[1])
    elif action[0] == LEFT:
        tank.on_for_seconds(steering = 100, speed = 30, seconds=action[1])
    elif action[0] == RIGHT:
        tank.on_for_seconds(steering = -100, speed = 30, seconds=action[1])
    elif action[0] == WAIT:
        sleep(action[1])
    sleep(0.02)
