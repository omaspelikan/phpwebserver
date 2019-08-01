# test.py
# pylint: disable=E1101
# pylint: disable=W0614
# pylint: disable=E0602
# pylint: disable=E1121
import pygame
import sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,400))
pygame.display.set_caption('Hello World!')

# set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

fontobj = pygame.font.Font('/Library/Fonts/Georgia.ttf', 40)
fontsurobj = fontobj.render('Hello world', True , GREEN, BLUE)
textRectObj = fontsurobj.get_rect()
textRectObj.center = (200,150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(fontsurobj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()