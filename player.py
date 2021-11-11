import pygame
import os

class Player():
    def __init__(self, displayX, displayY):
        self.displayX = displayX
        self.displayY = displayY
        self.playerSize = 128
        self.playerX = 10
        self.playerY = (self.displayY-self.playerSize)-10
        self.grounded = False
        self.gravity = "normal"
        self.filepath = os.path.abspath(__file__)
        self.filedir = os.path.dirname(self.filepath)
        self.playerImgPath = os.path.join(self.filedir, "player.png")
        self.backImgPath = os.path.join(self.filedir, "city background.jpg")
        self.blocoPath = os.path.join(self.filedir, "selva.jpg")
        self.playerImg = pygame.image.load(self.playerImgPath)

        self.backImg=pygame.image.load(self.backImgPath).convert()
        self.backImg=pygame.transform.scale(self.backImg,(1080,720))

        self.bloco=pygame.image.load(self.blocoPath).convert()
        self.bloco=pygame.transform.scale(self.bloco,(72,72))
        self.map=[0]*30
        for i in range(0,30):
            self.map[i]=[0]*10
            if i==29:
                self.map[i][4]=1
                self.map[i-2][5]=1
        self.xabs=2160
        self.xblocos=[-72]*30
        self.yblocos=[-72]*10
        self.blocos=[]
        self.absblocos=[]
        for i in range(0,30):
            for j in range(0,10):
                if(self.map[i][j]==1):
                    self.blocos.append((i,j))
                    self.absblocos.append((i*72,j*72))
        
        self.vbloco=6
        self.xbloco=29*72
        self.ybloco=8*72
        self.xback=0
        self.yback=0
        self.vback=5
        self.xj=100
        self.xback2=1080
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
    def colisão(self):
       
        for i in range (0,len(self.absblocos)):
            if(self.absblocos[i][0]>=self.xj and self.absblocos[i][0]<=self.xj+128):
                if self.absblocos[i][1]>=self.playerY and self.absblocos[i][1]<=self.playerY+128:
                    print("okkkkk")
                    return True
        return False
    def draw(self):
        
        self.DISPLAYSURF.blit(self.backImg,(self.xback,self.yback))
        self.DISPLAYSURF.blit(self.backImg,(self.xback2,self.yback))
        c=0
        
        for i in range(0,len(self.blocos)):
            
            self.DISPLAYSURF.blit(self.bloco,(self.absblocos[i][0]  ,self.absblocos[i][1] ))
            
            
            if self.absblocos[i][0]>1080:
                self.absblocos[i]=(self.absblocos[i][0]-self.vback,self.absblocos[i][1])
            else:
                self.absblocos[i]=(self.absblocos[i][0]-self.vbloco,self.absblocos[i][1])
               
            if self.absblocos[i][0]<=-72:
                 self.absblocos[i]=(self.blocos[i][0]*72,self.absblocos[i][1])
        self.xback-=self.vback
        self.xback2-=self.vback
        
        self.xabs-=self.vback
         
        if self.xback<-1080:
            self.xback=1080
            
        if self.xback2<-1080:
            self.xback2=1080
        if self.xabs<=0:
            self.xabs=2160
            #for i in range(0,len(self.blocos)):
                #self.absblocos=(self.blocos[i][0]*72,self.blocos[i][1]*72)
            
        if self.gravity == 'normal':
            self.DISPLAYSURF.blit(self.playerImg, (100, self.playerY))
        else:
            self.DISPLAYSURF.blit(pygame.transform.flip(self.playerImg, False, True), (100, self.playerY))
    
    def move(self):
        if self.direction == 'right':
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