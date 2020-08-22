import time
import pygame
from pygame.locals import *
import os, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#Càmera
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

pwm_h=GPIO.PWM(3,50) #PWM moviment horitzontal
pwm_v=GPIO.PWM(5,50) #PWM moviment vertical

[h,v]=[5.5,5.5]

pwm_h.start(h)
pwm_v.start(v)

#Motor
GPIO.setup(15,GPIO.OUT)#PWM Motor
GPIO.setup(12,GPIO.OUT)#AIN1 alt sentit positiu
GPIO.setup(13,GPIO.OUT)#AIN2 alt sentit negatiu
GPIO.setup(22,GPIO.OUT)#STBY alt per a sortir del mode stand by

pwm_M=GPIO.PWM(15,20000)
GPIO.output(12,0)#AIN1
GPIO.output(13,0)#AIN2
GPIO.output(22,1)

pwm_M.start(0)
[up,down]=[0,0]

#Servomotor
GPIO.setup(35,GPIO.OUT) #PWM servo
pwm_S=GPIO.PWM(35,100)
pwm_S.start(10)
direc=0

#Pygame
pygame.init() #Iniciar Pygame

screen=pygame.display.set_mode((240,240))
pygame.display.set_caption('Pi Crawler')

stop=False 

while True:
    time.sleep(0.1)
    if stop:
        break
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    key=pygame.key.get_pressed()
    
    #Control servos càmera
    if key[K_a] and h<8:#11
        h=h+0.56875
    elif key[K_d] and h>4:#1
        h=h-0.56875
    elif key[K_s] and v<8:
        v=v+0.56875
    elif key[K_w] and v>4:
        v=v-0.56875
    
    #Control servo de direcció
    if key[K_LEFT] and direc<21:#Canviar numero
        direc=direc+2
    if key[K_RIGHT] and direc>1:#canviar numero
        direc=direc-2
    if not key[K_LEFT] and not key[K_RIGHT]:
        if direc>13:
            direc=direc-2
        elif direc<13:
            direc=direc+2
        if direc==14 or direc==12:
            direc=13
    
    #Control motor escombretes
    if key[K_UP] and up<100:
        down=0
        if up==0:#si venim de estar en down
            GPIO.output(22,0)#Activem STBY
            time.sleep(0.1)#esperem
            pwm_M.ChangeDutyCycle(0)#Canviem de sentit de rotació a UP
            GPIO.output(13,0)#AIN2
            time.sleep(0.1)
            GPIO.output(12,1)#AIN1
            GPIO.output(22,1)
        up=up+5
        pwm_M.ChangeDutyCycle(up)
        
    if key[K_DOWN] and down<100:
        up=0
        if down==0: #Venim de sentit UP
            GPIO.output(22,0) #Activem STBY
            time.sleep(0.1) #Esperem per seguretat
            pwm_M.ChangeDutyCycle(0) #Canvi sentit gir motor
            GPIO.output(12,0)#AIN1
            time.sleep(0.1)
            GPIO.output(13,1)#AIN2
            GPIO.output(22,1)
        down=down+5
        pwm_M.ChangeDutyCycle(down)
        
    if not key[K_UP] and not key[K_DOWN]: #Si es deixa d'apretar els botons     
        if up>0: #Si estavam en UP
            up=up-5
            pwm_M.ChangeDutyCycle(up)
        if down>0: #Si estavam en DOWN
            down=down-5
            pwm_M.ChangeDutyCycle(down)
    
    #Sortir del programa
    elif key[K_ESCAPE]:
        
        pwm_h.ChangeDutyCycle(5.5)
        pwm_v.ChangeDutyCycle(5.5)
        stop=True

    pwm_h.ChangeDutyCycle(h)
    pwm_v.ChangeDutyCycle(v)
    pwm_S.ChangeDutyCycle(direc)
    print(up,down)
    
GPIO.output(22,0)
GPIO.output(12,0)
GPIO.output(13,0)
pwm_M.ChangeDutyCycle(0)
