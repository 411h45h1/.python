#blink.py
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

blink = 0 
while (blink < 25):
    GPIO.output(4, True)
    time.sleep(0.1)
    GPIO.output(4, False)
    time.sleep(0.1)
    blink = blink + 1
    print('Led Blink:', blink)
print('End.')