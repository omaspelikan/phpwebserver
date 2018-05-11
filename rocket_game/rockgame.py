# my pygame test ground
# pylint: disable=E1101
import pygame
import sys
from setting import Setting
import game_functions_rocket as gfr
from ship import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()
    """ initial object """
    mysetting = Setting()
    bullets = Group()                                                                     
    # create bullet group to record bullets posistion.
    screen = pygame.display.set_mode((mysetting.width,mysetting.height))                  
    # set display screen size.
    ship = Ship(mysetting,screen)                                                         
    # show ship.
                        
    while True:
        gfr.check_events(mysetting,screen,ship,bullets)
        ship.update()
        gfr.update_bullet(bullets,mysetting)
        gfr.update_screen(mysetting,screen,ship,bullets)


run_game()