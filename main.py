import pygame
from menu import Menu
from gamemenu import GameMenu
from rouletteblocks import RouletteBlocks
pygame.init()

screen = pygame.display.set_mode((800, 720))
clock = pygame.time.Clock()
running = True
game_runing = False
game_start = False
bg = pygame.image.load("assets/bg.png")
menu = Menu()   
gamem = GameMenu()
blocks = RouletteBlocks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(not game_runing):
                game_runing = menu.click()
            elif(not game_start):
                game_start = gamem.click()
                if(game_start):
                    blocks.click()
    screen.fill((15,77,91))
    screen.blit(bg, (0, 0))
    if(game_start):
        game_start = blocks.moving()
        if(not game_start):
            gamem.result(blocks.getWinNum())
            gamem.setBetAvaible(True)
    if(not game_runing):
        menu.update(screen)
    else:
        gamem.update(screen)
        blocks.update(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()