#!/usr/bin/env python3
#############################################################################
# Filename    : DHT11.py
# Description : read the temperature and humidity data of DHT11
# Author      : freenove
# modification: 2020/10/16
########################################################################
import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT

DHTPin = 11     #define the pin of DHT11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16,False)


def toggle_gpio():
        while True:
            GPIO.output(18, True)
            print("18 on!")
            time.sleep(2)
            GPIO.output(18, False)
            print("18 off!")
            time.sleep(2)


def check_temp():
        while True:
            dht = DHT.DHT(DHTPin)   #create a DHT class object
            for i in range(0,15):
                chk = dht.readDHT11()   #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                    print("DHT11,OK!")
                    break
                else:
                    print("Bad reading, rechecking")
            if dht.temperature > 23:
                GPIO.output(16,True)
            else:
                GPIO.output(16,False)
            time.sleep(0.1)
            fahrenheit = (dht.temperature * 1.8) + 32
            print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
            print(f"Humidity : {dht.humidity} \t Temperature : {fahrenheit} \n")
