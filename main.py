import pygame
from menu import Menu
from game import Game
from roulette import Roulette
pygame.init()

screen = pygame.display.set_mode((800, 720))
clock = pygame.time.Clock()
running = True
game_runing = False
bg = pygame.image.load("assets/bg.png")
menu = Menu()
game = Game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(not game_runing):
                game_runing = menu.click()
    screen.fill((15,77,91))
    screen.blit(bg, (0, 0))
    if(not game_runing):
        menu.update(screen)
    else:
        game.update(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()