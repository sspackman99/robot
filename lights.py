import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)



GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

try:
    while 1 < 10:
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)
        time.sleep(1)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
        print("Lights stopped by User")
        GPIO.cleanup()
