from otherstudentThreading import toggle_gpio, check_temp
import threading

print('Starting...')

check_temp_worker = threading.Thread(target=check_temp)
check_temp_worker.start()

other_worker = threading.Thread(target=toggle_gpio)
other_worker.start()



