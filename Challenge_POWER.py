#!/usr/bin/env pybricks-micropython

from ev3dev2.sensor.lego import InfraredSensor, ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_D,  SpeedPercent, MoveTank, MoveSteering, MediumMotor
import time
import sys
from time import sleep


infra = InfraredSensor()
tank = MoveSteering(OUTPUT_B, OUTPUT_C)
medium_motor = MediumMotor(OUTPUT_D)

FORWARD, BACKWARD, LEFT, RIGHT, WAIT = range(5)

cont = True
def deactivate():
    cont = False

def log_action(act_type, t_val):
    actions.append([act_type, t_val])

def top_left_channel_1_action(state):
    if state: # state is True (pressed) or False
        tank.on(steering=0, speed=SpeedPercent(100))
    else:
        tank.off()

def bottom_left_channel_1_action(state):
    if state:
        tank.on(steering=0, speed=SpeedPercent(-100))
    else:
        tank.off()

def top_right_channel_1_action(state):
    if state:
        tank.on(steering=100, speed=30)
    else:
        tank.off()

def bottom_right_channel_1_action(state):
    if state:
        tank.on(steering=-100, speed=30)
    else:
        tank.off()

def top_left_channel_2_action(state):
    if state: # state is True (pressed) or False
        medium_motor.on(speed=5)
    else:
        medium_motor.off()

def bottom_left_channel_2_action(state):
    if state:
        medium_motor.on(speed=-5)
    else:
        medium_motor.off()

def top_right_channel_2_action(state):
    if state:
        medium_motor.on(speed=5)
    else:
        medium_motor.off()

def bottom_right_channel_2_action(state):
    if state:
        medium_motor.on(speed=-5)
    else:
        medium_motor.off()

def beacon_channel_1_action(state):
    if state:
        sys.exit()
    else:
        cont = False

# Associate the event handlers with the functions defined above
infra.on_channel1_top_left = top_left_channel_1_action
infra.on_channel1_bottom_left = bottom_left_channel_1_action
infra.on_channel1_top_right = top_right_channel_1_action
infra.on_channel1_bottom_right = bottom_right_channel_1_action

infra.on_channel2_top_left = top_left_channel_1_action
infra.on_channel2_bottom_left = bottom_left_channel_1_action
infra.on_channel2_top_right = top_right_channel_2_action
infra.on_channel2_bottom_right = bottom_right_channel_2_action

infra.on_channel1_beacon = beacon_channel_1_action

while cont:
    infra.process()
    sleep(0.01)

