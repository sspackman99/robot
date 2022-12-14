#Libraries
from re import M
import RPi.GPIO as GPIO
import time

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

 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def all_forward():
    for motor in motors:
        motor.forward()

def all_backward():
    for motor in motors:
        motor.backward()
        GPIO.output(8, GPIO.HIGH)

def all_stop():
    for motor in motors:
        motor.stop()
    GPIO.output(8, GPIO.LOW)

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
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            if dist < 20:
                print("turning left")
                #turn_left()
                all_backward()
                #time.sleep(1.5)
            else:
                all_forward()
            time.sleep(.05)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

