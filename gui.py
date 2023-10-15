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
    bet = 0
    # btns = [
    #     Button(pygame.Vector2(pos.x,pos.y),pygame.Vector2(size.x,size.y),"red","Play"),
    #     Button(pygame.Vector2(pos.x,pos.y+(1*dis)),pygame.Vector2(size.x,size.y),"red","Exit")
    # ]
    def update(self,screen):
        pygame.draw.rect(screen,(20,20,20),[self.pos.x,self.pos.y,self.size.x,self.size.y],border_radius=13)
        self.draws(screen)
        # for i in self.btns:
        #     i.update(screen)
    def draws(self,screen):
        text_surface1 = GAME_FONT2.render("Stake", False, (255, 255, 255))
        text_surface2 = GAME_FONT.render(f"Your money: {self.money}", False, (255, 255, 255))
        text_surface3 = GAME_FONT.render(f"Your bet: {self.bet}", False, (255, 255, 255))
        screen.blit(text_surface1, (self.pos.x + self.size.x/2 - text_surface1.get_width()/2, self.pos.y))
        screen.blit(text_surface2, (self.pos.x + 20, self.pos.y + 50))
        screen.blit(text_surface3, (self.pos.x + 20, self.pos.y + 80))

    # def click(self):
    #     if(self.btns[0].checkCursor()):
    #         return True
    #     elif(self.btns[1].checkCursor()):
    #         pygame.quit()
    #     return False