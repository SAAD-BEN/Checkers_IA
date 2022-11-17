from copy import deepcopy
from random import randint
import pygame

from checkers.board import Board


def random(position, color,game):
    z = get_all_moves(position,color,game)
    if len(z) == 0:
        print("Random has no moves left so he lost")
        position.winner()
        return None
    return z[randint(0, (len(z)-1))]


def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board




def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            #draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)
    
    return moves
