import pygame

class Player():
    def __init__(self, displayX, displayY):
        self.displayX = displayX
        self.displayY = displayY
        self.playerSize = 128
        self.playerX = 10
        self.playerY = (self.displayY-self.playerSize)-10
        self.grounded = False
        self.gravity = "normal"
        self.playerImg = pygame.image.load('C:/Users/loren/source/repos/Python/GravityShift/player.png')
        self.playerSpeed = 2
        self.gravityVelocity = 5
        self.direction = 'right'
        self.DISPLAYSURF = pygame.display.set_mode((self.displayX, self.displayY), 0, 32)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
    
        
    def gravityShift(self):
        if self.grounded:
            if self.gravity == 'normal':
                self.gravity = 'inverse'
                self.grounded = False
            else:
                self.gravity = 'normal'
                self.grounded = False
                
    def draw(self):
        self.DISPLAYSURF.fill(self.WHITE)
        if self.gravity == 'normal':
            self.DISPLAYSURF.blit(self.playerImg, (self.playerX, self.playerY))
        else:
            self.DISPLAYSURF.blit(pygame.transform.flip(self.playerImg, False, True), (self.playerX, self.playerY))
    
    def move(self):
        if self.direction == 'right':
            self.playerX += self.playerSpeed
            if self.playerX >= (self.displayX-self.playerSize):
                self.direction = 'left'
            if self.gravity == 'normal':
                if not self.grounded:
                    self.playerY += self.gravityVelocity
                if self.playerY >= (self.displayY-self.playerSize):
                    self.grounded = True
            elif self.gravity == 'inverse':
                if not self.grounded:
                    self.playerY -= self.gravityVelocity
                if self.playerY <= 10:
                    self.grounded = True
            
        elif self.direction == 'left':
            self.playerX -= self.playerSpeed
            if self.playerX <= 0:
                self.direction = 'right'
            if self.gravity == 'normal':
                if not self.grounded:
                    self.playerY += self.gravityVelocity
                if self.playerY >= (self.displayY-self.playerSize):
                    self.grounded = True
            elif self.gravity == 'inverse':
                if not self.grounded:
                    self.playerY -= self.gravityVelocity
                if self.playerY <= 10:
                    self.grounded = True