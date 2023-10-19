#gamemenu.py
import pygame
from button import Button
from gui import Gui
class GameMenu:
    pos = pygame.Vector2(50,600)
    size = pygame.Vector2(200,50)
    dis=50
    margin = 30
    gui = Gui()
    b_a=True
    btns = [
        Button(pygame.Vector2(pos.x,pos.y),pygame.Vector2(size.x,size.y),"red","+"),
        Button(pygame.Vector2(pos.x + size.x + dis,pos.y),pygame.Vector2(size.x,size.y),"red","-"),
        Button(pygame.Vector2(pos.x+ (2*size.x) + (2*dis),pos.y),pygame.Vector2(size.x,size.y),"red","Bet"),
        Button(pygame.Vector2(30 + 350/2 - 32 - 70,205 + 250),pygame.Vector2(64,64),"red","R",(200,0,0)),
        Button(pygame.Vector2(30 + 350/2 - 32,205 + 250),pygame.Vector2(64,64),"red","0",(0,200,0)),
        Button(pygame.Vector2(30 + 350/2 - 32 + 70,205 + 250),pygame.Vector2(64,64),"red","B",(0,0,0))
    ]
    def update(self,screen):
        pygame.draw.rect(screen,(20,20,20),[self.btns[0].getPos().x-self.margin,self.btns[0].getPos().y-self.margin,self.btns[0].btn_size.x*len(self.btns)+(self.margin*(len(self.btns)+2)),self.btns[0].getSize().y+(2*self.margin)],border_radius=13)
        self.gui.update(screen)
        for i in self.btns:
            i.update(screen)

    def click(self):
        if(self.btns[0].checkCursor()):
            self.gui.add_m(100)
        elif(self.btns[1].checkCursor()):
            self.gui.sub_m(100)
        elif(self.btns[2].checkCursor() and self.getBetAvaible()):
            self.setBetAvaible(False)
            self.gui.bet()
            return True
        elif(self.btns[3].checkCursor()):
            self.gui.whatBet("R")
        elif(self.btns[4].checkCursor()):
            self.gui.whatBet("0")
        elif(self.btns[5].checkCursor()):
            self.gui.whatBet("B")
        return 
    def result(self,_winum):
        self.gui.result(_winum)
    def setBetAvaible(self, _handler):
        self.b_a = _handler
    def getBetAvaible(self):
        return self.b_a