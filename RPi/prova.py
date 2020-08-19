import pygame
from pygame.locals import *
import os, sys
import time


pygame.init() #Iniciar Pygame

screen=pygame.display.set_mode((240,240))
pygame.display.set_caption('Pi Crawler')
stop=False

while True:
    time.sleep(5)
    if stop:
        break
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_d:
                print('d')
    key=pygame.key.get_pressed()
    print(key[K_d])