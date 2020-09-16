#blink.py
import time
import RPi.GPIO as GPIO

setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, True)
time.sleep(1)
GPIO.output(4, False)