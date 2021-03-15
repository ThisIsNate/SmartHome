import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)

def toggle_gpio():
    GPIO.output(18, True)
    print("18 on!")
    time.sleep(2)
    GPIO.output(18, False)
    print("18 off!")
    time.sleep(2)