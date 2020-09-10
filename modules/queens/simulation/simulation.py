"""
    Algorithm to solve The eight queens puzzle
"""
from .board import Board
from ..algorithms.min_conflicts import min_conflicts
from ..simulation.queen import Queen


class Simulation:
    """Start game simulation with the items"""

    def __init__(self, n):
        self.n = n
        self.solutions = []
        # Create board
        self.board = Board(n=self.n)
        # Create game pieces
        self.queens = []
        for i in range(n):
            # Position locked with a queen
            q = Queen(0, i, n)
            self.board.put_piece(i, q.get_piece_symbol())
            self.queens.append(q)
        self.a = None

    def start(self):
        """Start game simulation"""
        self.solutions, self.a = min_conflicts(self.board, self.queens)

    def get_solutions(self):
        """Solutions of the simulation"""
        return self.solutions

    def get_board(self):
        """Board to start the game"""
        return self.board.get_board()

    def get_queens(self):
        """Get queens of the game"""
        return self.get_queens()
