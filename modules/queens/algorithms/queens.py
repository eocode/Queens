"""
    Algorithm to solve The eight queens puzzle
"""
import numpy as np


def create_array(n):
    return [['x' for i in range(n)]]


class Queens:

    def __init__(self, n):
        self.n = n
        self.board = create_array(n)

    def create_board(self):
        for i in range(self.n - 1):
            self.board = np.append(self.board, create_array(self.n), axis=0)

    def print_board(self):
        print(self.board)

    def get_board(self):
        return self.board
