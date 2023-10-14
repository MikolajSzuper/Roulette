#gamemenu.py
import pygame
from button import Button
class GameMenu:
    pos = pygame.Vector2(50,600)
    size = pygame.Vector2(200,50)
    dis=50
    margin = 30
    btns = [
        Button(pygame.Vector2(pos.x,pos.y),pygame.Vector2(size.x,size.y),"red","+"),
        Button(pygame.Vector2(pos.x + size.x + dis,pos.y),pygame.Vector2(size.x,size.y),"red","-"),
        Button(pygame.Vector2(pos.x+ (2*size.x) + (2*dis),pos.y),pygame.Vector2(size.x,size.y),"red","Bet")
    ]
    def update(self,screen):
        pygame.draw.rect(screen,(20,20,20),[self.btns[0].getPos().x-self.margin,self.btns[0].getPos().y-self.margin,self.btns[0].btn_size.x*len(self.btns)+(self.margin*(len(self.btns)+2)),self.btns[0].getSize().y+(2*self.margin)],border_radius=13)
        for i in self.btns:
            i.update(screen)

    def click(self):
        if(self.btns[0].checkCursor()):
            return True
        elif(self.btns[1].checkCursor()):
            pygame.quit()
        return False