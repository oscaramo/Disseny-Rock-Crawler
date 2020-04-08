import RPi.GPIO as GPIO
from tkinter import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
pwm=GPIO.PWM(12,50)

pwm.start(0)

#Controlling via a pwm the 
def servo(duty):
    pwm.ChangeDutyCycle(int(duty))

#creating a scale in RPi srceeen
root=Tk()
w=Scale(root,from_=2,to=12,length=300,orient=HORIZONTAL,command=servo)
w.pack()


