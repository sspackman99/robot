
import RPi.GPIO as GPIO

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

pin = 4

GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin,True)

while True:
    try:
        pass
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()