#menu.py
import pygame
from button import Button
pygame.init()
pygame.font.init()
GAME_FONT = pygame.font.SysFont('Arial Black',32)

class Menu:
    pos = pygame.Vector2(100,200)
    size = pygame.Vector2(200,50)
    dis=70
    margin = 30
    btns = [
        Button(pygame.Vector2(pos.x,pos.y),pygame.Vector2(size.x,size.y),"red","Play"),
        Button(pygame.Vector2(pos.x,pos.y+(1*dis)),pygame.Vector2(size.x,size.y),"red","Exit")
    ]
    def __init__(self) -> None:
        pass
    def update(self,screen):
        pygame.draw.rect(screen,(20,20,20),[self.btns[0].getPos().x-self.margin,self.btns[0].getPos().y-self.margin,self.btns[0].btn_size.x+(2*self.margin),self.btns[0].getSize().y*len(self.btns)+(self.dis*(len(self.btns)-1))],border_radius=13)
        for i in self.btns:
            i.update(screen)

    def click(self):
        if(self.btns[0].checkCursor()):
            return True
        elif(self.btns[1].checkCursor()):
            pygame.quit()
        return False