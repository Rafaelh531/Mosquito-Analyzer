import RPi.GPIO as gpio
from time import sleep
import sys

import subprocess

from camera import take_picture

def run_mosqmachine():
    motor_channel = (3,5,7,11)
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)

    gpio.setup(motor_channel, gpio.OUT)

    for j in range(0,15):
        print(j)
        take_picture(j)
        for i in range(1,170,5):
            gpio.output(motor_channel, (gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH))
            sleep(0.002)
            gpio.output(motor_channel, (gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH))
            sleep(0.002)
            gpio.output(motor_channel, (gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW))
            sleep(0.002)
            gpio.output(motor_channel, (gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW))
            sleep(0.002)
                    
        sleep(1)

    subprocess.call(['./classifier_trigger.sh'])
    # gpio.cleanup()
        