"""
    Create NxN board to solve
"""
import numpy as np


class Board:
    def __init__(self, n):
        self.n = n
        self.board = np.zeros((n, n))
        self.safe_queens = 0

    def all_queens_are_safe(self):
        return self.n == self.safe_queens

    def lock_box(self):
        return False

    def put_piece(self, position, piece):
        self.board[position][0] = piece

    def get_board(self):
        return self.board
