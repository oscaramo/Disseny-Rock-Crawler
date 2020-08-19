import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

pwm=GPIO.PWM(3,50)
pwm.start(0)

for i in range(1,12):
    time.sleep(0.5)
    pwm.ChangeDutyCycle(i)
    
pwm.ChangeDutyCycle(5)
pwm.ChangeDutyCycle(12)