import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.screens import menu, ingame, endgame , ingame_vs_IA, ingame_IA_vs_IA


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
pygame.display.set_icon(pygame.image.load('assets/chinese-checkers-32.png'))


def main():
    screen = menu.run(WIN)
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if screen == 'Menu':
                screen = menu.run(WIN)
            elif screen == 'INGAME(1 vs 1)':
                screen = ingame.run(WIN)
            elif screen == 'INGAME(1 vs IA)':
                screen = ingame_vs_IA.run(WIN)
            elif screen == 'INGAME(IA vs IA)':
                screen = ingame_IA_vs_IA.run(WIN)
            elif screen == 'RESTART':
                screen = endgame.run(WIN)
            elif screen == 'QUIT':
                run = False
            

main()
