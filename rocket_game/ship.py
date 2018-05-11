# ship.py
import pygame

class Ship():
    
    def __init__(self,setting,screen):
        self.screen = screen
        self.image = pygame.image.load('alien_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.mv_right = False
        self.mv_left = False
        self.mv_up = False
        self.mv_down = False
        """ start ship at the bottom center position """
        #self.rect.centerx = self.screen_rect.centerx
        self.rect.left = self.screen_rect.left
        #self.rect.bottom = self.screen_rect.bottom
        self.rect.bottom = self.screen_rect.bottom/2
        self.ai_setting = setting
        self.center = float(self.rect.centerx)
        self.r_height = float(self.rect.bottom)

    def update(self):
        if self.mv_right and self.rect.right < self.screen_rect.right:
            self.center +=self.ai_setting.speed_factor
        if self.mv_left and self.rect.left > 0:
            self.center -=self.ai_setting.speed_factor
        if self.mv_up and self.rect.top > self.screen_rect.top:
            self.r_height -= self.ai_setting.speed_factor
        if self.mv_down and self.rect.bottom < self.screen_rect.bottom:
            self.r_height += self.ai_setting.speed_factor
        self.rect.centerx = self.center
        self.rect.bottom= self.r_height

    def blitme(self):
        """ draw the ship at its current location """
        self.screen.blit(self.image,self.rect)


        