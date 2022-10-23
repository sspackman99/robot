
import RPi.GPIO as GPIO

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

pin = 23

GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin,GPIO.HIGH)

while True:
    try:
        pass
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        break
