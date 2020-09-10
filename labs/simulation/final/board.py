"""
    Create NxN board to solve
"""
import numpy as np


class Board:
    def __init__(self, n):
        self.n = n
        self.end = self.validate_end(n, n)
        self.__board = np.zeros((n, n))
        self.__safe_queens = 0
        self.__solution_id = 0
        self.__without_solution = False
        self.x_values = {}

    @staticmethod
    def validate_end(x, y):
        tmp = str(x)
        tmp2 = str(y)
        return int(tmp + tmp2)

    def set_safe_board(self, values):
        self.x_values = values

    def set_board(self, board):
        self.__board = board

    def set_without_solution(self):
        self.__without_solution = True

    def get_without_solution(self):
        return self.__without_solution

    def get_solution_id(self):
        return self.__solution_id

    def all_queens_are_safe(self):
        return self.n == self.__safe_queens

    def get_safe_queens(self):
        return self.__safe_queens

    def add_safe(self):
        self.__safe_queens += 1

    def put_piece(self, x, y, piece):
        self.__board[x][y] = piece
        self.__solution_id = str(self.__board.ravel())

    def get_board(self):
        return self.__board
