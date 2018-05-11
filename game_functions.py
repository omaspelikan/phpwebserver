# game_functions.py                   Check game event and update screen.
# pylint: disable=E1101               
# (prevent Visual Code for syntax error)
""" Check quit event """
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(mysetting,screen,ship,bullets):
    for event in pygame.event.get():
        """ check event type and assign to separate function """
        if event.type == pygame.QUIT:
        #if event.__dict__['key'] == pygame.k_q:
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
    elif event.key == pygame.K_SPACE:
        fire_bullets(mysetting,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.mv_right=False
    elif event.key == pygame.K_LEFT:
        ship.mv_left = False    

def update_screen(mysetting,screen,ship,aliens,bullets):
        screen.fill(mysetting.bg_color)
        ship.update()
        """ Redraw all bullets behide ship and alien """
        for bullet in bullets:
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)                             # sprite.Group.draw() to draw alien object to screen.
        pygame.display.flip()
        
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))

def fire_bullets(mysetting,screen,ship,bullets):
    if len(bullets) < mysetting.bullet_allow:
        new_bullet = Bullet(mysetting,screen,ship)
        bullets.add(new_bullet)
def get_number_aliens_x(mysetting,alien_width):
    """ determine number of aliens in a row."""
    avail_space_x = mysetting.width - (2*alien_width)               # 計算alien 物件可顯示的空間寬度 = 畫面 - 左右兩邊各一個alien的寬度當空白。
    num_aliens_x = int(avail_space_x/(2*alien_width))
    return num_aliens_x

def get_number_rows(mysetting,ship_height,alien_height):
    """ determine number of row aliens in screen """
    avail_space_y = (mysetting.height - (7*alien_height) - ship_height)
    num_rows = int(avail_space_y/(2*alien_height))
    return num_rows

def create_alien(mysetting,screen,aliens,alien_number,num_row): 
    alien = Alien(mysetting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_number * alien_width      # 第一個alien的x座標=空白（以alien的寬度），第二個alien的x座標 = 空白 + 第一個alien + 空白 = 3個alien寬
    alien.rect.x = alien.x        
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * num_row                              # 把第n個alien的x座標 置入到 alien.rect.x (alien 圖像的x座標)
    aliens.add(alien)
    
def create_fleet(mysetting,screen,ship,aliens):
    """ Create full fleet of aliens. """
    """ aliens is sprite.group() """
    alien = Alien(mysetting,screen)
    num_aliens_x = get_number_aliens_x(mysetting,alien.rect.width)      # 取得每列alien可以放的數量
    num_rows = get_number_rows(mysetting,ship.rect.height,alien.rect.height)
    """ Create the first row of aliens """
    for row_number in range(num_rows):
        for alien_number in range(num_aliens_x):
            create_alien(mysetting,screen,aliens,alien_number,row_number)
 


