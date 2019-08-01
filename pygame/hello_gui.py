# test gui hello .py
# pylint: disable=E1101
# pylint: disable=W0614
# pylint: disable=E0602
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300),pygame.RESIZABLE, 32)
DISPLAYSURF.fill((255,255,255))
pygame.display.set_caption('Hello, World!')
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()