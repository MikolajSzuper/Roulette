#gui.py
#menu.py
import pygame
from button import Button
GAME_FONT = pygame.font.SysFont('Arial Black',24)
GAME_FONT2 = pygame.font.SysFont('Arial Black',42)

class Gui:
    pos = pygame.Vector2(30,205)
    size = pygame.Vector2(350,350)
    dis=70
    margin = 30
    money = 1000
    ybet = 0
    hw=0
    onwh="Nothing"
    onwhc=(255,255,255)
    def update(self,screen):
        pygame.draw.rect(screen,(20,20,20),[self.pos.x,self.pos.y,self.size.x,self.size.y],border_radius=13)
        self.draws(screen)
    def draws(self,screen):
        text_surface1 = GAME_FONT2.render("Stake", False, (255, 255, 255))
        text_surface2 = GAME_FONT.render(f"Your money: {self.money}", False, (255, 255, 255))
        text_surface3 = GAME_FONT.render(f"Your bet: {self.ybet}", False, (255, 255, 255))
        text_surface4 = GAME_FONT.render(f"On what:", False, (255,255,255))
        text_surface5 = GAME_FONT.render(f" {self.onwh}", False, self.onwhc)
        text_surface6 = GAME_FONT.render(f"How many: {self.hw}", False, (255, 255, 255))
        screen.blit(text_surface1, (self.pos.x + self.size.x/2 - text_surface1.get_width()/2, self.pos.y))
        screen.blit(text_surface2, (self.pos.x + 20, self.pos.y + 50))
        screen.blit(text_surface3, (self.pos.x + 20, self.pos.y + 80))
        screen.blit(text_surface4, (self.pos.x + 20, self.pos.y + 110))
        screen.blit(text_surface5, (self.pos.x + 20 + text_surface4.get_width(), self.pos.y + 110))
        screen.blit(text_surface6, (self.pos.x + 20, self.pos.y + 140))
    def add_m(self,_hw):
        if(self.hw+_hw<=self.money):
            self.hw+=_hw
    def sub_m(self,_hw):
        if(self.hw-_hw >= 0):
            self.hw-=_hw
    def bet(self):
        self.money-=self.hw
        self.ybet = self.hw
    def result(self,_winnum):
        self.hw = 0
        if(_winnum==self.onwh):
            price=0
            if(_winnum=="0"):
                price=self.ybet*5
            else:
                price=self.ybet*2
            self.money += price
    def whatBet(self,what):
        if(what=="R"):
            self.onwh="R"
            self.onwhc=(200,0,0)
        elif(what=="0"):
            self.onwh="0"
            self.onwhc=(0,200,0)
        elif(what=="B"):
            self.onwh="B"
            self.onwhc=(255,255,255)
