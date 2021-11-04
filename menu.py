import pygame

class Menu():
    def __init__(self, displayX, displayY, player):
        self.displayX = displayX
        self.displayY = displayY
        self.player = player
        self.window = player.DISPLAYSURF
        self.mid_x, self.mid_y = self.displayX / 2, self.displayY / 2
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 200
        # self.font_name = '8-BIT WONDER.TTF'
        self.font_name = pygame.font.get_default_font()
        
        
    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.player.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.player.DISPLAYSURF.blit(text_surface,text_rect)
        

    def draw(self):
        self.player.DISPLAYSURF.fill(self.player.BLACK)
        self.draw_text('Gravity Shift', 30, self.mid_x, self.mid_y + self.offset)
        self.draw_text('Jogar', 20, self.mid_x, self.mid_y + 30)
        self.draw_text('Opçoes', 20, self.mid_x, self.mid_y + 60)
        self.draw_text('Sair', 20, self.mid_x, self.mid_y + 90)
