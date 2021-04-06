                                     #!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance via UltrasonicRanging sensor
# auther      : www.freenove.com
# modification: 2019/12/28 (Bryce Fletcher)
########################################################################
import RPi.GPIO as GPIO
import time

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

from time import sleep, strftime
from datetime import datetime

trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          # define the maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE*60   # calculate timeout according to the maximum measuring distance
GPIO.setmode(GPIO.BOARD)  # use PHYSICAL GPIO Numbering
GPIO.setup(trigPin, GPIO.OUT)  # set trigPin to OUTPUT mode
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(33, GPIO.OUT)


def pulseIn(pin,level,timeOut): # obtain pulse time of a pin under timeOut
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    pulseTime = (time.time() - t0)*1000000
    return pulseTime
    
def getSonar():     # get the measurement results of ultrasonic module,with unit: cm
    GPIO.output(trigPin,GPIO.HIGH)      # make trigPin output 10us HIGH level 
    time.sleep(0.00000001)
    GPIO.output(trigPin,GPIO.LOW) # make trigPin output LOW level 
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   # read plus time of echoPin
    distance = pingTime * 340.0 / 2.0 / 10000.0     # calculate distance with sound speed 340m/s
    return distance
    


def distance_light():
    PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
    PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.

    try:
        mcp = PCF8574_GPIO(PCF8574_address)
    except:
        try:
            mcp = PCF8574_GPIO(PCF8574A_address)
        except:
            print('I2C Address Error !')
            exit(1)
    # Create LCD, passing in MCP GPIO adapter.
    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)
    mcp.output(3, 1)  # turn on LCD backlight
    lcd.begin(16, 2)
    lcd.clear()

    while(True):
        distance = getSonar() # get distance
        print ("The distance is : %.2f Feet Away"%(distance))


        if distance<15 and distance > 0:
            print("light on")
            GPIO.output(33,GPIO.HIGH)

            lcd.setCursor(0, 0)  # set cursor position
            lcd.message('  Car Detected  ' + '\n')  # display CPU temperature
            lcd.message("      "+str(round(distance))+" cm")  # display the time

            time.sleep(5)
            lcd.clear()
        else :
            print ("light off")
            GPIO.output(33,GPIO.LOW)
            # lcd.clear()
            # lcd.setCursor(0, 0)  # set cursor position
            # lcd.message('   Distance:' + '\n')  # display CPU temperature
            # lcd.message("   " + str(round(distance, 2)))  # display the time
            # time.sleep(.5)

if __name__=="__main__":
    distance_light()