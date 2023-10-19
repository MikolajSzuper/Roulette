#rouletteblocks.py
import pygame
from random import seed
from random import randint
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
    tick=0
    random_num=0
    seed(1)
    velocity=20
    max_tick=300
    max_velocity=20
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
    def moving(self):
        last=self.getLastInQueue()
        first=self.getFirstInQueue()
        num=self.getWhereIsNumber(str(self.random_num))
        if(self.tick > self.max_tick and self.blocks[num].getPos().x > 380 and self.blocks[num].getPos().x < 420):
            self.tick=0
            self.velocity=20
            return False
        elif(self.tick > self.max_tick/2 and self.velocity > self.max_velocity/2):
            self.velocity=self.velocity*0.9
        elif(self.tick > self.max_tick and self.blocks[num].getPos().x > 150 and self.blocks[num].getPos().x < 380 and self.velocity > 3):
            self.velocity=self.velocity*0.9

        if(self.blocks[last].getPos().x>800 and self.blocks[first].getPos().x >= self.pos.x):
            self.blocks[last].movePos(pygame.Vector2(self.pos.x - self.size.x - self.dis,self.blocks[last].getPos().y))
        for i in self.blocks:
            i.movePos(pygame.Vector2(i.getPos().x+self.velocity,i.getPos().y))
        self.tick+=1
        return True
    def getLastInQueue(self):
        last=0
        for i in range(len(self.blocks)):
            if(self.blocks[i].getPos().x>self.blocks[last].getPos().x):
                last=i
        return last
    def getFirstInQueue(self):
        first=0
        for i in range(len(self.blocks)):
            if(self.blocks[i].getPos().x<self.blocks[first].getPos().x):
                first=i
        return first
    def getWhereIsNumber(self,_text):
        for i in range(len(self.blocks)):
            if(self.blocks[i].getText()==_text):
                return i
    def getWinBlock(self,_text):
        for i in self.blocks:
            if(i.getText()==_text):
                return i
    def genRandomNum(self):
        self.random_num = randint(0,36)
    def click(self):
        self.genRandomNum()
    def getWinNum(self):
        win = self.getWinBlock(str(self.random_num))
        return win.getColor()