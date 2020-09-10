"""
    Valid queen moves
"""
import numpy as np


class Queen:

    def __init__(self, x, y, conflicts):
        self.x = x
        self.y = y
        self.future_position = x
        self.__piece_symbol = 1
        self.queen_conflicts = conflicts

    def get_piece_symbol(self):
        return self.__piece_symbol

    def add_queen_conflict(self):
        self.queen_conflicts += 1

    def get_queen_conflicts(self):
        return self.queen_conflicts

    def valid_move(self, board):
        if self.__attack_col(board.get_board(), board.n):
            return False
        if self.__attack_row(board.get_board(), board.n):
            return False
        # if self.__attack_diagonal(board.get_board(), board.n):
        #     return False
        return True

    def __attack_col(self, board, n):
        points = 0
        for i in range(n - 1):
            points += board[self.x][self.y + i]
        if points > n:
            return True
        else:
            return False

    def __attack_row(self, board, n):
        points = 0
        for i in range(n):
            if self.x < n:
                points += board[self.x + i][self.y]
            if self.x < n:
                points += board[self.x + i][self.y]
        if points > n:
            return True
        else:
            return False

    def __attack_right_diagonal(self, board, n):
        points = 0
        for i in range(n):
            points += board[self.y][self.x]
        if points > 2 * n:
            return True
        else:
            return False

    def __attack_left_diagonal(self, board, n):
        points = 0
        for i in range(n):
            points += board[self.y][self.x]
        if points > 2 * n:
            return True
        else:
            return False
