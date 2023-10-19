#button.py
import pygame
pygame.init()
pygame.font.init()
GAME_FONT = pygame.font.SysFont('Arial Black',32)

class Button:
    btn_pos = pygame.Vector2(0,0)
    btn_color = ""
    btn_text = ""
    btn_text_color = (255,255,255)
    btn_size = pygame.Vector2(0,0)

    def __init__(self, _pos, _size, _color, _text, _btn_color=(255,255,255)):
        self.btn_pos = _pos
        self.btn_color = _color
        self.btn_size = _size
        self.btn_text = _text
        self.btn_color = _btn_color

    def checkCursor(self):
        x, y = pygame.mouse.get_pos()
        if(x > self.btn_pos.x and x < self.btn_pos.x+self.btn_size.x and y > self.btn_pos.y and y < self.btn_pos.y + self.btn_size.y):
            return True
        return False

    def update(self, screen):
        self.btn_color = (60,60,60)
        x, y = pygame.mouse.get_pos()
        if(self.checkCursor()):
            self.btn_color = (0,200,60)
        pygame.draw.rect(screen,self.btn_color,[self.btn_pos.x,self.btn_pos.y,self.btn_size.x,self.btn_size.y],border_radius=13)
        text_surface = GAME_FONT.render(self.btn_text, False, self.btn_text_color)
        screen.blit(text_surface, (self.btn_pos.x + self.btn_size.x/2 - text_surface.get_width()/2, self.btn_pos.y + self.btn_size.y/2 - text_surface.get_height()/2))
    def getPos(self):
        return self.btn_pos
    def getSize(self):
        return self.btn_size
