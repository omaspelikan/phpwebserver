# test.py
# pylint: disable=E1101
import pygame

def p_list(event):
    print(event)

def run_game():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            p_list(event)

while True:
    run_game()