# pygame.py
# pylint: disable=E1101
""" test pygame module """
import sys
import pygame
import game_functions as gf
from setting import Setting
from ship import Ship
from pygame.sprite import Group
   
def run_game():
# initial game and display a screen object.
    pygame.init()
    mysetting = Setting()
    #bg_color = (130,230,230)
    screen = pygame.display.set_mode((mysetting.width,mysetting.height))
    pygame.display.set_caption("Alien Invasion")                           # 顯示視窗標題
    """ make a bullet group , a ship and a team of alien ship."""
    bullets = Group()
    ship = Ship(mysetting,screen)
    """ create a aliens group """
    aliens = Group()
    """ create the fleet of alien ship """
    gf.create_fleet(mysetting,screen,ship,aliens)
    while True:
        gf.check_events(mysetting,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(mysetting,screen,ship,aliens,bullets)
 

run_game()