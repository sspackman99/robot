from re import M
import RPi.GPIO as GPIO
import pygame, sys
from pygame.locals import *
import time
from threading import Thread

pygame.init()

SCREEN_SIZE = (500,500)

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption('RoboCon 2022')

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
MOTOR1 = Motor(24,23)
MOTOR4 = Motor(17,18)
MOTOR2 = Motor(26,20)
MOTOR3 = Motor(19,13)

motors = [MOTOR1, MOTOR2, MOTOR3, MOTOR4]

left_motors = [MOTOR1, MOTOR3]

right_motors = [MOTOR2, MOTOR4]
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(8, GPIO.OUT)

###Directions

def all_forward():
    GPIO.output(8, GPIO.LOW)
    for motor in motors:
        motor.forward()

def all_backward():
    for motor in motors:
        motor.backward()
        GPIO.output(8, GPIO.HIGH)

def all_stop():
    GPIO.output(8, GPIO.LOW)
    for motor in motors:
        motor.stop()

def turn_left():
    GPIO.output(8, GPIO.LOW)
    for motor in left_motors:
        motor.forward()
    for motor in right_motors:
        motor.backward()

def turn_right():
    GPIO.output(8, GPIO.LOW)
    for motor in left_motors:
        motor.backward()
    for motor in right_motors:
        motor.forward()

# direction variables
forwards = False
reverse = False
go_left = False
go_right = False

# def lights():
#     while True:
#         if reverse == False:
#             GPIO.output(8, GPIO.HIGH)
#             GPIO.output(25, GPIO.LOW)
#             time.sleep(1)
#             GPIO.output(25, GPIO.HIGH)
#             GPIO.output(8, GPIO.LOW)
#             time.sleep(1)
#         else:
#             GPIO.output(8, GPIO.HIGH)
#             GPIO.output(25, GPIO.LOW)

# t = Thread(target=lights)
# t.start()

# try: 
## pygame main loop
while True:
    # event checker
    for event in pygame.event.get():

        # window close event
        if event.type == QUIT:
            #if event.key == K_q:
            print('quitting')
            pygame.quit()
            GPIO.cleanup()
            sys.exit()

        if event.type == KEYDOWN:
            # forward
            if event.key == K_w:
                print('you pressed w')
                forwards = True
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
            forwards = reverse = go_left = go_right = False
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

        pygame.display.update()
# except KeyboardInterrupt:
#         print("remote control stopped by User")
#         GPIO.cleanup()

            

