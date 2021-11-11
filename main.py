import pygame
import sys
import os
from pygame.locals import *
from player import Player
from menu import *

pygame.init()
pygame.font.init()
# pygame.mixer.init()

FPS = 60
playerSize = 128
displayX = 1080
displayY = 720
fpsClock = pygame.time.Clock()
 
# filepath = os.path.abspath(__file__)
# filedir = os.path.dirname(filepath)
# musicpath = os.path.join(filedir, "vgm-atmospheric-deepspace.mp3")

# pygame.mixer.music.load(musicpath)
# pygame.mixer.music.load("vgm-atmospheric-deepspace.mp3")
# pygame.mixer.music.play(-1)

DISPLAYSURF = pygame.display.set_mode((displayX, displayY), 0, 32) 
pygame.display.set_caption('Gravity Shift')


BLACK = (0, 0, 0)

player = Player(displayX, displayY)
menu = Menu(displayX, displayY, player)

playing = False

while True:
    if not playing:
        menu.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    action = menu.click()
                    if action == 1:
                        playing = True
                    # elif action == 2:
                    elif action == 3:
                        pygame.quit()
                        sys.exit()
                    action = 0
                elif event.key == K_UP:
                    menu.arrow('up')
                elif event.key == K_DOWN:
                    menu.arrow('down')
        pygame.display.update()
    while playing:
        player.draw()
        player.move()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    player.gravityShift()

        pygame.display.update()
        if player.colisão():
            pygame.quit()
            sys.exit()
        fpsClock.tick(FPS)
        
