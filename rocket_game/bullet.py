# bullet.py
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ a class to manage bullets fired from the ship """
    def __init__(self,ai_setting,screen,ship):
        """ create a bullet at the ship's top position """
        super().__init__()
        self.screen = screen

        """ create a bullet rect at (0,0) then set position """
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        #self.rect.right = ship.rect.right
        self.rect.centerx = ship.rect.centerx
        self.rect.midright = ship.rect.midright

        """ store bullet's  position as a decimal value. """
        self.x = float(self.rect.x)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        self.x +=self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """ draw the bullet to screen. """
        pygame.draw.rect(self.screen,self.color,self.rect)