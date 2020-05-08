import pygame
from pygame.locals import *
import os, sys
import time
import socket

#Inicialitzar pygame
pygame.init()

#Per obrir la pestanya
screen = pygame.display.set_mode((240, 240))
pygame.display.set_caption('Pi Crawler')

stop=False
message=''

#Bucle principal del pygame
while True:
    time.sleep(0.1)
    #Crear el socket per fer la connexió amb la RPi
    ms=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='192.168.1.42'
    ms.connect((host,1220)) #És conecten utilitzant el port 1234

    #Comandes pygame
    keys=pygame.key.get_pressed() #Crea una llista amb l'estat de cada tecla (True si s'està apretant)
    if stop==True:
        break
    for event in pygame.event.get(): #Per sortir del programa si es tanca la finestra
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    if keys[K_UP]:
            message='u'
    elif keys[K_DOWN]:
            message='d'
    elif keys[K_RIGHT]:
            message='r'
    elif keys[K_LEFT]:
            message='l'
    elif keys[K_ESCAPE]:
            message='s'
            stop=True
    else:
        message=""

    #S'envia el missatge a la RPi
    ms.sendall(message.encode())
