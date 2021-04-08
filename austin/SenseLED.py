#!/usr/bin/env python3
########################################################################
# Filename    : SenseLED.py
# Description : Control led with infrared Motion sensor. austin
# auther      : www.freenove.com
# modification: 2019/12/28hgh
########################################################################
import RPi.GPIO as GPIO
import time

ledPin = 15       # define ledPin
sensorPin = 13    # define sensorPin
buzzerPin = 32    # define buzzerPin
GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
GPIO.setup(ledPin, GPIO.OUT)    # set ledPin to OUTPUT mode
GPIO.setup(buzzerPin, GPIO.OUT) # set buzzerPin to OUTPUT mode
GPIO.setup(sensorPin, GPIO.IN)  # set sensorPin to INPUT mode

def loop():
    while True:
        if GPIO.input(sensorPin)==GPIO.HIGH:
            GPIO.output(ledPin,GPIO.HIGH) # turn on led
            print ('led turned on >>>')
        else :
            GPIO.output(ledPin,GPIO.LOW) # turn off led
            print ('led turned off <<<')
        if GPIO.input(sensorPin)==GPIO.LOW:
            GPIO.output(buzzerPin,GPIO.HIGH) #turn on buzzer
            print ('buzzer turned off >>>')
        else :
            GPIO.output(buzzerPin,GPIO.LOW) # turn off buzzer
            print ('buzzer turned on <<<')

        time.sleep(1)


if __name__ == "__main__":
    loop()

