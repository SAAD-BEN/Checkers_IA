import pygame
from checkers.constants import SQUARE_SIZE, WHITE, RED
from checkers.game import Game
from agents.minimax import minimax
from agents.random import random

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
        elif game.turn == RED:
            new_board = random(game.get_board(), RED, game)
            if game.updateIA() == 'RESTART':
                pygame.time.delay(400)
                return 'RESTART'
            game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'

        game.updateIA()
        if game.updateIA() == 'RESTART':
            return 'RESTART'

