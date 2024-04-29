import RPi.GPIO as GPIO
import time


'''
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, True)
finally:
    GPIO.cleanup()
    print('acabou')
'''

def turn_servo(pin_servo, turn_speed):
    try:
        pwm = GPIO.PWM(pin_servo, 50)
        pwm.start(0)
        while True:
            for duty_cycle in range(0, 101, turn_speed):
                pwm.ChangeDutyCycle(duty_cycle)
                time.sleep(5)
    except KeyboardInterrupt:
        pass
    
    pwm.stop()
    GPIO.cleanup()
    

if __name__ == '__main__':
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    
    servo = GPIO.PWM(7, 50)
    
    servo.start(0)
    time.sleep(2)
    
    print('Rotating 180 degrees!')
    
    duty = 2
    while duty <= 12:
        servo.ChangeDutyCycle(duty)
        time.sleep(1)
        print(duty)
        duty += 1
        
    servo.stop()
    GPIO.cleanup()
    
    
    #turn_servo(7, 10)
    