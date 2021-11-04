import pygame
import sys
from pygame.locals import *
from player import Player
from menu import *

pygame.init()
pygame.font.init()

FPS = 60
playerSize = 128
displayX = 1080
displayY = 720
fpsClock = pygame.time.Clock()


DISPLAYSURF = pygame.display.set_mode((displayX, displayY), 0, 32)
pygame.display.set_caption('Gravity Shift')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player = Player(displayX, displayY)
menu = Menu(displayX, displayY, player)

playing = False

while True:
    if not playing:
        menu.draw()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    playing = True
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
        fpsClock.tick(FPS)
