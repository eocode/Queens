"""
    Create NxN board to solve
    Use numpy for manage board matrix
"""
import numpy as np


class Board:
    """Board Class"""

    def __init__(self, n):
        self.n = n
        self.__board = np.zeros((self.n, self.n))
        self.__positions = {v: {c: c for c in range(0, self.n)} for v in range(self.n)}

    def create_board(self):
        """Create numpy array as a bord chess n*n"""
        self.__board = np.zeros((self.n, self.n))

    def create_positions(self):
        """Generate dictionary with available positions of game"""
        self.__positions = {v: {c: c for c in range(0, self.n)} for v in range(self.n)}

    def get_board(self):
        """Return generated board"""
        return self.__board

    def get_positions(self):
        return self.__positions
