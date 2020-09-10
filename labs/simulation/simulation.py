"""
    Algorithm to solve The eight queens puzzle
"""
from .board import Board
from algorithms.nqueens import NQueens
from simulation.solutions import Solutions
from simulation.final.board import Board as Board_2
from simulation.final.queen import Queen as Queen_2


class Simulation:
    """Start game simulation with the items"""

    def __init__(self, n):
        self.solutions = Solutions()
        self.n = n

    def start(self):
        """Start game simulation"""
        for i in range(self.n):
            board = Board(self.n)
            board.put_piece(i, 0, 1)
            board.set_solution_id()
            board.add_safe(i, 0)
            self.solutions.add_solution(board)

        for a in (range(self.n - 1)):
            self.solutions = NQueens.solve(self.n, self.solutions)
            print(len(self.solutions.get_solutions()))

        return self.solutions

    def start2(self):
        """Start second game simulation"""
        self.generate_initial_boards()

        for a in range(self.n - 1):
            self.solutions = NQueens.solve2(self.n, self.solutions)
            print(len(self.solutions.get_solutions()))

        return self.solutions

    def generate_initial_boards(self):
        for i in range(self.n):
            board = Board(self.n)
            board.put_piece(i, 0, 1)
            board.set_solution_id()
            board.add_safe(i, 0)
            board.x_values = {v: {c: c for c in range(1, self.n)} for v in range(self.n)}
            board.x_values.pop(i)
            for j, k in board.x_values.items():
                if j > i:
                    k.pop(0 + j - i)
                if j < i:
                    for t in range(i):
                        if i - t in board.x_values[t].keys():
                            board.x_values[t].pop(i - t - 0)
            self.solutions.add_solution(board)

    def generate_initial_boards_2(self):
        for i in range(self.n):
            board = Board_2(self.n)
            board.put_piece(i, 0, 1)
            board.add_safe(i, 0)
            board.x_values = {v: {c: c for c in range(1, self.n)} for v in range(self.n)}
            board.x_values.pop(i)
            for j, k in board.x_values.items():
                # Right up
                if j < i and 0 + i - j in k:
                    k.pop(0 + i - j)
                # Right down
                if j >= i and 0 + j - i in k:
                    k.pop(0 + j - i)
            self.solutions.add_solution(board)

    def show_solutions(self):
        for key, values in self.solutions.get_solutions().items():
            print(values, key)

    def start3(self):
        """Start Thirth game simulation"""
        # self.generate_initial_boards_2()
        # self.show_solutions()
        NQueens.solve3(self.n)
        # self.show_solutions()

    def start4(self):
        """Start Forth game simulation"""
        # self.generate_initial_boards_2()
        # self.show_solutions()
        q = NQueens()
        self.solutions = q.solve4(self.n)
        print(len(self.solutions.get_solutions()))
        # self.show_solutions()

    def get_solutions(self):
        """Solutions of the simulation"""
        return self.solutions
