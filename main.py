import RPi.GPIO as GPIO
import time
from stepper_motor import run_mosqmachine

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_callback(channel):
    print('Running mosqMachine')
    run_mosqmachine()

GPIO.add_event_detect(38, GPIO.RISING, callback=button_callback, bouncetime=200)

while True:
    time.sleep(0.1)
