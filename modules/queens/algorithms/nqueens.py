"""
    Queens algorithms to solve n*n board
    Version 4 in production
    See test and other solutions in labs folder
    This code solve until
"""
from modules.queens.simulation.board import Board
from modules.queens.simulation.queen import Queen
from modules.queens.solutions.solutions import Solutions
import copy


class NQueens:
    """Main class"""

    def __init__(self, n):
        self.__n = n
        self.__solutions = Solutions()

    def solve(self):
        """Main method to start algorithm
        Prepare to start algorithm
        """
        board = Board(self.__n)
        board.create_board()
        board.create_positions()
        self.__n_queens(board.get_board(), 0, board.get_positions())

    def __n_queens(self, board, col, positions):
        """Last N Queens Algorithm
        Development by @eocode
        Version 4
        """
        if col == len(board):
            self.__solutions.add_solution(
                board, len(self.__solutions.get_solutions()) + 1
            )
            return True

        for row in range(len(board)):
            if row in positions.keys() and col in positions[row]:
                apply, values = Queen.attack(row, col, copy.deepcopy(positions))
                if apply:
                    board[row][col] = 1
                    self.__n_queens(board, col + 1, values)
                    board[row][col] = 0

    def get_solutions(self):
        return self.__solutions.get_solutions()
