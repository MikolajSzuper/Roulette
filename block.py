#block.py
import pygame
GAME_FONT = pygame.font.SysFont('Arial Black',32)

class Block:
    pos = pygame.Vector2(0,0)
    size = pygame.Vector2(0,0)
    color = (0,0,0)
    text = ""
    def __init__(self,_pos,_size,_color,_text):
        self.pos = _pos
        self.size = _size
        self.color = _color
        self.text = _text
    def update(self,screen):
        pygame.draw.rect(screen,self.color,[self.pos.x,self.pos.y,self.size.x,self.size.y],border_radius=13)
        text_surface = GAME_FONT.render(self.text, False, (255, 255, 255))
        screen.blit(text_surface, (self.pos.x + self.size.x/2 - text_surface.get_width()/2, self.pos.y + self.pos.y/2 - (text_surface.get_height()*7/8)))
    def movePos(self,_pos):
        self.pos = _pos
    def getPos(self):
        return self.pos
    def getText(self):
        return self.text
