import pygame
from checkers.constants import WHITE, WIDTH, HEIGHT
from checkers.screens import menu, ingame, endgame


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
            winner = WHITE
            if event.type == pygame.QUIT:
                run = False

            if screen == 'Menu':
                screen = menu.run(WIN)
            elif screen == 'INGAME':
                screen, winner = ingame.run(WIN)
            elif screen == 'RESTART':
                screen = endgame.run(WIN, winner)
            elif screen == 'QUIT':
                run = False


main()
