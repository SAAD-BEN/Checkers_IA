import pygame
from checkers.agents.minimax import minimax
from checkers.agents.random import random
from checkers.constants import RED, SQUARE_SIZE, WHITE
from checkers.game import Game


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def run(win):
    run = True
    clock = pygame.time.Clock()
    game = Game(win)

    while run:
        clock.tick(60)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 2, True, game)
            game.ai_move(new_board)
        #if game.turn == RED:
        #    new_board = random(game.get_board(), RED, game)
        #    game.ai_move(new_board)
        if game.winner() != None:
            print(game.winner())
            return 'RESTART', game.winner()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT', game.winner()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
