import random


def min_conflicts(board, queens):
    queen = queens[1]

    a = queen.valid_move(board)

    # Initalize queens
    return board.get_board(), a
