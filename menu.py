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
        self.musica_on = "On"
        self.selecionado = "Jogar"
        
        
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
        self.draw_text('Música: ' + self.musica_on, 20, self.mid_x, self.mid_y + 60)
        self.draw_text('Sair', 20, self.mid_x, self.mid_y + 90)
        self.draw_cursor()

    def draw_cursor(self):
        if self.selecionado == "Jogar":
            self.draw_text('>', 20, self.mid_x - 37, self.mid_y + 27)
        elif self.selecionado == "Musica":
            self.draw_text('>', 20, self.mid_x - 63, self.mid_y + 57)
        elif self.selecionado == "Sair":
            self.draw_text('>', 20, self.mid_x - 30, self.mid_y + 87)
        
    def click(self):
        if self.selecionado == "Jogar":
            return 1
        elif self.selecionado == "Musica":
            if self.musica_on == "On":
                self.musica_on = "Off"
            elif self.musica_on == "Off":
                self.musica_on = "On"
            return 2
        elif self.selecionado == "Sair":
            return 3
            
    def arrow(self, up_down):
        if self.selecionado == "Jogar":
            if up_down == 'down':
                self.selecionado = "Musica"
        elif self.selecionado == "Musica":
            if up_down == 'up':
                self.selecionado = "Jogar"
            elif up_down == 'down':
                self.selecionado = "Sair"
        elif self.selecionado == "Sair":
            if up_down == 'up':
                self.selecionado = "Musica"
             
        