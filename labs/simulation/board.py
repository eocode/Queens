"""
    Create NxN board to solve
"""
import numpy as np


class Board:
    def __init__(self, n):
        self.n = n
        self.board = np.zeros((n, n))
        self.__safe_queens = 0
        self.__final_queen = False
        self.__without_solution = False
        self.__solved = False
        self.__track_solution = ""
        self.__solution_id = ""
        self.__value_track = 0
        self.__safe_x = {}
        self.__safe_y = {}
        self.__locked_positions = {}
        self.x_values = {}
        self.y_values = {}

    def set_board(self, board):
        self.board = board

    def add_track_solution(self, x, y):
        self.__track_solution += str(x)
        self.__track_solution += str(y)
        self.__value_track += x + y

    def set_track_solution(self, track, value):
        self.__track_solution = track
        self.__value_track += value

    def get_track_solution(self):
        return self.__track_solution

    def set_solution_id(self):
        self.__solution_id = str(self.board.ravel())

    def get_solution_id(self):
        return self.__solution_id

    def get_value_track(self):
        return self.__value_track

    def set_without_solution(self):
        self.__without_solution = True

    def is_without_solution(self):
        return self.__without_solution

    def __set_end_of_the_road(self):
        self.__final_queen = True

    def is_end_of_the_road(self):
        return self.__final_queen

    def all_queens_are_safe(self):
        return self.n == self.__safe_queens

    def get_safe_queens(self):
        return self.__safe_queens

    def set_safe(self, row, col):
        self.__safe_x = row
        self.__safe_y = col

    def set_safe_board(self, values):
        self.x_values = values

    def add_safe(self, row, col):
        self.__safe_x[row] = row
        self.__safe_y[col] = col
        self.__safe_queens += 1

    def valid_if_safe(self, key):
        try:
            return self.__safe_x[key] >= 0
        except:
            return False

    def get_safe_x(self):
        return self.__safe_x

    def get_safe_y(self):
        return self.__safe_y

    def add_queen_safe(self):
        self.__safe_queens += 1
        if self.__safe_queens + 1 == self.n:
            self.__set_end_of_the_road()
        if self.__safe_queens == self.n:
            self.__solved = True

    def is_solved(self):
        return self.__solved

    def put_piece(self, x, y, piece):
        self.board[x][y] = piece
        self.__solution_id = str(self.board.ravel())
        self.__track_solution += str(x)
        self.__track_solution += str(y)
        self.__value_track += x + y

    def get_board(self):
        return self.board
