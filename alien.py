# Alien.py
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class that represent a single alien """
    def __init__(self,ai_setting,screen):
        super().__init__()
        self.screen = screen
        self.setting = ai_setting

        #  Load alien image and set its rect attritube
        self.image = pygame.image.load('alienship/alienship.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near top-left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien exact position
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
