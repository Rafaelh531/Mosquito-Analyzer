import RPi.GPIO as gpio
from time import sleep
import sys

motor_channel = (3,5,7,11)
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

gpio.setup(motor_channel, gpio.OUT)

motor_direction = input('select motor direction a=anticlockwise, c=clockwise:')
for j in range(0,15):
    print(j)
    for i in range(1,170,5):
        if(motor_direction == 'a'):
            gpio.output(motor_channel, (gpio.HIGH,gpio.LOW,gpio.LOW,gpio.HIGH))
            sleep(0.002)
            gpio.output(motor_channel, (gpio.LOW,gpio.LOW,gpio.HIGH,gpio.HIGH))
            sleep(0.002)
            gpio.output(motor_channel, (gpio.LOW,gpio.HIGH,gpio.HIGH,gpio.LOW))
            sleep(0.002)
            gpio.output(motor_channel, (gpio.HIGH,gpio.HIGH,gpio.LOW,gpio.LOW))
            sleep(0.002)
                
    sleep(1)
    motor_direction = 'a' #input('select motor direction a=anticlock, c=clockwise')
    if(motor_direction == 'q'):
        gpio.cleanup()
        sys.exit(0)
        

