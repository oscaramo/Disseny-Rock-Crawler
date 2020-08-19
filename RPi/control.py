import time
#import pipan
import pygame
from pygame.locals import *
import os, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

#PWM h i v (va de 1 a 11)
pwm_h=GPIO.PWM(3,50)
pwm_v=GPIO.PWM(5,50)

[h,v]=[5.5,5.5]

pwm_h.start(h)
pwm_v.start(v)

pygame.init() #Iniciar Pygame

screen=pygame.display.set_mode((240,240))
pygame.display.set_caption('Pi Crawler')

stop=False 

#[x,y]=[150,150] #Posicions inicials PiPan

#p=pipan.PiPan()

#p.do_tilt(x)
#p.do_pan(y)

while True:
    time.sleep(0.1)
    if stop:
        break
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    key=pygame.key.get_pressed()
    if key[K_a] and h<8:#11
        h=h+0.56875
    elif key[K_d] and h>4:#1
        h=h-0.56875
    elif key[K_s] and v<8:
        v=v+0.56875
    elif key[K_w] and v>4:
        v=v-0.56875
    elif key[K_ESCAPE]:
        pwm_h.ChangeDutyCycle(5.5)
        pwm_v.ChangeDutyCycle(5.5)
        stop=True

    pwm_h.ChangeDutyCycle(h)
    pwm_v.ChangeDutyCycle(v)

