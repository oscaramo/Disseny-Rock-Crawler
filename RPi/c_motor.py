import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT) #STBY
GPIO.setup(7,GPIO.OUT) #AIN1
GPIO.setup(5,GPIO.OUT) #AIN2
GPIO.setup(3,GPIO.OUT) #PWMA

GPIO.output(11,False)
GPIO.output(7,False)
GPIO.output(5,True)

pwm=GPIO.PWM(3,350)

v=50
pwm.start(v)

