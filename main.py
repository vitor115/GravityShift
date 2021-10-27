import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
playerSize = 128
displayX = 1080
displayY = 720
fpsClock = pygame.time.Clock()


DISPLAYSURF = pygame.display.set_mode((displayX, displayY), 0, 32)
pygame.display.set_caption('Gravity Shift')

WHITE = (255, 255, 255)
playerImg = pygame.image.load('C:/Users/loren/source/repos/Python/GravityShift/player.png')
playerX = 10
playerY = (displayY-playerSize)-10
playerSpeed = 2
gravityVelocity = 5
direction = 'right'
gravity = 'normal'
grounded = False

while True: 
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        playerX += playerSpeed
        if playerX >= (displayX-playerSize):
            direction = 'left'
        if gravity == 'normal':
            if not grounded:
                playerY += gravityVelocity
            if playerY >= (displayY-playerSize):
                grounded = True
        elif gravity == 'inverse':
            if not grounded:
                playerY -= gravityVelocity
            if playerY <= 10:
                grounded = True
            
    elif direction == 'left':
        playerX -= playerSpeed
        if playerX <= 0:
            direction = 'right'
        if gravity == 'normal':
            if not grounded:
                playerY += gravityVelocity
            if playerY >= (displayY-playerSize):
                grounded = True
        elif gravity == 'inverse':
            if not grounded:
                playerY -= gravityVelocity
            if playerY <= 10:
                grounded = True
                
    if gravity == 'normal':
        DISPLAYSURF.blit(playerImg, (playerX, playerY))
    else:
        DISPLAYSURF.blit(pygame.transform.flip(playerImg, False, True), (playerX, playerY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key==K_SPACE:
                if gravity == 'normal':
                    gravity = 'inverse'
                    grounded = False
                else:
                    gravity = 'normal'
                    grounded = False
                

    pygame.display.update()
    fpsClock.tick(FPS)
