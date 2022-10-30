import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)



GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

try:
    while 1 < 10:
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)
        time.sleep(1)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
        print("Lights stopped by User")
        GPIO.cleanup()
