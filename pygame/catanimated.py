# test.py
# pylint: disable=E1101
# pylint: disable=W0614
# pylint: disable=E0602
# pylint: disable=E1121
import pygame
import sys
from pygame.locals import *


pygame.init()

FPS = 40
fpsclock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Animation')

# set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'


# draw on the surface object


while True:
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        catx+=5
        if catx==280:
            direction = 'down'
    elif direction == 'down':
        caty+=5
        if caty==220:
            direction='left'
    elif direction == 'left':
        catx-=5
        if catx==10:
            direction = 'up'
    elif direction == 'up':
        caty-=5
        if caty==10:
            direction = 'right'

    DISPLAYSURF.blit(catImg,(catx,caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsclock.tick(FPS)