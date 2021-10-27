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

class Player():
    def __init__(self, playerX, playerY, grounded, gravity, direction):
        self.playerX = playerX
        self.playerY = playerY
        self.grounded = grounded
        self.gravity = gravity
        self.playerImg = pygame.image.load('C:/Users/loren/source/repos/Python/GravityShift/player.png')
        self.playerSpeed = 2
        self.gravityVelocity = 5
        self.direction = direction
        self.playerSize = 128
    
        
    def gravityShift(self):
        if self.grounded:
            if self.gravity == 'normal':
                self.gravity = 'inverse'
                self.grounded = False
            else:
                self.gravity = 'normal'
                self.grounded = False
                
    def draw(self):
        if self.gravity == 'normal':
            DISPLAYSURF.blit(self.playerImg, (self.playerX, self.playerY))
        else:
            DISPLAYSURF.blit(pygame.transform.flip(self.playerImg, False, True), (self.playerX, self.playerY))
    
    def move(self):
        if player.direction == 'right':
            player.playerX += player.playerSpeed
            if player.playerX >= (displayX-player.playerSize):
                player.direction = 'left'
            if player.gravity == 'normal':
                if not player.grounded:
                    player.playerY += player.gravityVelocity
                if player.playerY >= (displayY-player.playerSize):
                    player.grounded = True
            elif player.gravity == 'inverse':
                if not player.grounded:
                    player.playerY -= player.gravityVelocity
                if player.playerY <= 10:
                    player.grounded = True
            
        elif player.direction == 'left':
            player.playerX -= player.playerSpeed
            if player.playerX <= 0:
                player.direction = 'right'
            if player.gravity == 'normal':
                if not player.grounded:
                    player.playerY += player.gravityVelocity
                if player.playerY >= (displayY-player.playerSize):
                    player.grounded = True
            elif player.gravity == 'inverse':
                if not player.grounded:
                    player.playerY -= player.gravityVelocity
                if player.playerY <= 10:
                    player.grounded = True

player = Player(playerX, playerY, grounded, gravity, direction)

while True: 
    DISPLAYSURF.fill(WHITE)

    player.draw()
    player.move()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key==K_SPACE:
                player.gravityShift()
                

    pygame.display.update()
    fpsClock.tick(FPS)
