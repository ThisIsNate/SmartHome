
import threading

import RPi.GPIO as GPIO
GPIO.setwarnings(False)

# from .DoorOpener.KeypadPasswordCode import accept_code
from .otherstudentThreading import check_temp
from .DistanceLight.UltrasonicRanging import distance_light
from .austin.SenseLED import loop

print('Starting...')

GPIO.setmode(GPIO.BOARD)


# keypad_worker = threading.Thread(target=accept_code)
# keypad_worker.start()

check_temp_worker = threading.Thread(target=check_temp)
check_temp_worker.start()
#
distance_light_worker = threading.Thread(target=distance_light)
distance_light_worker.start()

austin_worker = threading.Thread(target=loop)
austin_worker.start()
#
