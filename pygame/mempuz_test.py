# memory puzzle test ground
# pylint: disable=E1101
# pylint: disable=W0614
# pylint: disable=E0602
# pylint: disable=E1121

import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
PIXELPERBOX = 50
PIXELPERGAP = 10
BOXPERROW = 10
BOXPERCOLUMN = 6
XMARGIN = int((WINDOWWIDTH - (PIXELPERBOX + PIXELPERGAP) * BOXPERROW) / 2)
YMARGIN = int((WINDOWHEIGHT - (PIXELPERBOX + PIXELPERGAP) * BOXPERCOLUMN) / 2)

#               R    G    B
GRAY        = (100, 100, 100)
NAVYBLUE    = (60, 60, 100)
WHITE       = (255, 255, 255)
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)
BLUE        = (0, 0, 255)
YELLOW      = (255, 255, 0)
ORANGE      = (255, 128, 0)
PURPLE      = (255, 0, 255)
CYAN        = (0, 255, 255)

BGCOLOR = NAVYBLUE
BOXCOLOR = WHITE

DONUT = 'dount'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES * 2) >= \
BOXPERCOLUMN * BOXPERROW , "Board is too big for number of shape/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
                                     # contain all the box.
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))   
    table = []
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('My Memory Puzzle.')
    # initial a table
    for y in range(BOXPERCOLUMN):
        for x in range(BOXPERROW):
            table.append([(x,y),False])
    #print(table)
    # How to show list to screen?
    #
    #myFont = pygame.font.Font('Arial.ttf',20)
    #showWord = myFont.render(str(table), True, YELLOW)
    #textRectObj = showWord.get_rect()
    #textRectObj.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)


    while True:
        DISPLAYSURF.fill(BGCOLOR)
        board = []
        mouseClicked = False
        for block in table:
            printBlock(block, board)

    #    DISPLAYSURF.blit(showWord, textRectObj)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                #if checkPixinBox(mousex, mousey, board):
                #    showHightlight(mousex, mousey, board)
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                

        if checkPixinBox(mousex, mousey, board) == True:
            showHightlight(mousex, mousey, board)
        if checkPixinBox(mousex, mousey, board) == True and mouseClicked:
            showIcon(mousex, mousey, board)


        pygame.display.update()
        FPSCLOCK.tick(FPS)


def printBlock(block, board):
    key , value = block
    boxx , boxy = key
    if value == False:
        board.append(pygame.Rect(boxx * PIXELPERBOX + boxx * PIXELPERGAP + XMARGIN , boxy * PIXELPERBOX + boxy * PIXELPERGAP + YMARGIN, PIXELPERBOX, PIXELPERBOX))
        pygame.draw.rect(DISPLAYSURF, WHITE, (boxx * PIXELPERBOX + boxx * PIXELPERGAP + XMARGIN , boxy * PIXELPERBOX + boxy * PIXELPERGAP + YMARGIN, PIXELPERBOX, PIXELPERBOX))

def showHightlight(mousex, mousey, board):
    for i in board:
        if i.collidepoint(mousex, mousey) == True:
            pygame.draw.rect(DISPLAYSURF, RED, i, 4)
    #pygame.display.update()
    #FPSCLOCK.tick(FPS)


def showIcon(mousex, mousey, board):
    for i in board:
        if i.collidepoint(mousex, mousey) == True:
            pygame.draw.rect(DISPLAYSURF, GREEN, i)
#       pygame.display.update()
        #FPSCLOCK.tick(FPS)
def checkPixinBox(mousex, mousey, board):
       for i in board:
        if i.collidepoint(mousex, mousey) == True:
          return True  


if __name__ == '__main__':
    main()