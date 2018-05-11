# game_functions.py
""" Check quit event """
import sys
import pygame
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.mv_right=True
    elif event.key == pygame.K_LEFT:
        ship.mv_left=True
    elif event.key == pygame.K_UP:
        ship.mv_up = True
    elif event.key == pygame.K_DOWN:
        ship.mv_down = True

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.mv_right=False
    elif event.key == pygame.K_LEFT:
        ship.mv_left = False 
    elif event.key == pygame.K_UP:
        ship.mv_up = False
    elif event.key == pygame.K_DOWN:
        ship.mv_down = False   

def update_screen(mysetting,screen,ship):
        screen.fill(mysetting.bg_color)
        ship.update()
        ship.blitme()
        pygame.display.flip()
