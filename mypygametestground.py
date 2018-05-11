# my pygame test ground
import pygame
import sys
from setting import Setting
import game_functions_rocket as gfr
from ship import Ship
def run_game():
    pygame.init()
    """ initial object """
    mysetting = Setting()
    screen = pygame.display.set_mode((mysetting.width,mysetting.height))                  # set display screen size.
    rocket = Ship(mysetting,screen)
                        
    while True:
        gfr.check_events(rocket)
        gfr.update_screen(mysetting,screen,rocket)


run_game()