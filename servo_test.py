import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

servo = GPIO.PWM(7, 50)
servo.start(0)

try:
    while True:
        angle = float(input('Angle between 0 and 180 degrees: '))
        servo.ChangeDutyCycle(2 + (angle/36))
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)
        
finally:
    servo.stop()
    GPIO.cleanup()
    
servo.stop()
GPIO.cleanup()