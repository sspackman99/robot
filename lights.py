import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)



GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

try:
    while 1 < 10:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(17, GPIO.LOW)

except KeyboardInterrupt:
        print("Lights stopped by User")
        GPIO.cleanup()
