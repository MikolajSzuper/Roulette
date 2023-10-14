#rouletteblocks.py
import pygame
from block import Block
class RouletteBlocks:
    pos = pygame.Vector2(10,100)
    size = pygame.Vector2(64,64)
    dis=10
    margin = 30
    blocks = []
    numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
    num_color=(0,0,0)
    sid=0
    for i in range(37):
        if(i==0):
            num_color = (0,200,0)
        elif(i%2==0):
            num_color = (0,0,0)
        else:
            num_color = (200,0,0)
        blocks.append(Block(pygame.Vector2(pos.x+sid,pos.y),size,num_color,str(numbers[i])))
        sid+=64+dis
    def update(self,screen):
        pygame.draw.rect(screen,(20,20,20),[0,self.pos.y-30,800,self.size.y+60])
        for i in self.blocks:
            i.update(screen)
        pygame.draw.rect(screen,(200,255,0),[400,self.pos.y-30,5,self.size.y+60])