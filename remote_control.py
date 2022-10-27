from re import M
import RPi.GPIO as GPIO
import pygame
from pygame.locals import *
import sys
import time

pygame.init()

# SCREEN_SIZE = (500,500)

# screen = pygame.display.set_mode(SCREEN_SIZE)

# pygame.display.set_caption('RoboCon 2022')

#Create motor class

class Motor:
    def __init__(self,pin1,pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.LOW)
    def forward(self):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
    def backward(self):
        GPIO.output(self.pin2, GPIO.HIGH)
        GPIO.output(self.pin1, GPIO.LOW)
    def stop(self):
        GPIO.output(self.pin2, GPIO.LOW)
        GPIO.output(self.pin1, GPIO.LOW)
        
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 16
GPIO_ECHO = 12
MOTOR1 = Motor(23,24)
MOTOR2 = Motor(18,17)
MOTOR3 = Motor(20,26)
MOTOR4 = Motor(13,19)

motors = [MOTOR1, MOTOR2, MOTOR3, MOTOR4]

left_motors = [MOTOR1, MOTOR3]

right_motors = [MOTOR2, MOTOR4]
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

###Directions

def all_forward():
    for motor in motors:
        motor.forward()

def all_backward():
    for motor in motors:
        motor.backward()

def all_stop():
    for motor in motors:
        motor.stop()

def turn_left():
    for motor in left_motors:
        motor.backward()
    for motor in right_motors:
        motor.forward()

def turn_right():
    for motor in left_motors:
        motor.forward()
    for motor in right_motors:
        motor.backward()

# direction variables
forwards = False
reverse = False
go_left = False
go_right = False

## pygame main loop
while 1 < 10:

    # event checker
    for event in pygame.event.get():

        # window close event
        if event.type == QUIT:
            if event.key == K_q:
                print('quitting')
                pygame.quit()
                sys.exit()

        if event.type == KEYDOWN:
            # forward
            if event.key == K_w:
                print('you pressed w')
                forward = True
            # backward
            if event.key == K_s:
                print('you pressed s')
                reverse = True
            # turn left
            if event.key == K_a:
                print('you pressed a')
                go_left = True
            # turn right
            if event.key == K_d:
                print('you pressed d')
                go_right = True

        if event.type == KEYUP:
            forward = reverse = go_left = go_right = False
            all_stop()
        # This will actually make the robot work
        if forwards:
            print('going forward')
            all_forward()
        if reverse:
            print('going back')
            all_backward()
        if go_left:
            print('going left')
            turn_left()
        if go_right:
            print('going right')
            turn_right()

        #pygame.display.update()

            

