# game_functions.py
""" Check quit event """
import sys
import pygame
from bullet import Bullet

def check_events(mysetting,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,mysetting,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
def check_keydown_events(event,mysetting,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.mv_right=True
    elif event.key == pygame.K_LEFT:
        ship.mv_left=True
    elif event.key == pygame.K_UP:
        ship.mv_up = True
    elif event.key == pygame.K_DOWN:
        ship.mv_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(mysetting,screen,ship,bullets)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.mv_right=False
    elif event.key == pygame.K_LEFT:
        ship.mv_left = False 
    elif event.key == pygame.K_UP:
        ship.mv_up = False
    elif event.key == pygame.K_DOWN:
        ship.mv_down = False

def fire_bullets(mysetting,screen,ship,bullets):
    """ add bullet to sprite group and limit number of bullet show to screen """
    new_bullet = Bullet(mysetting,screen,ship)
    if len(bullets) < mysetting.bullet_allow:
        bullets.add(new_bullet)

def update_bullet(bullets,mysetting):
    """ check bullets group , if bullet pass screen then remove it. """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= mysetting.width:
            bullets.remove(bullet)
    print(len(bullets))
               

def update_screen(mysetting,screen,ship,bullets):
        screen.fill(mysetting.bg_color)
        ship.update()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        pygame.display.flip()
