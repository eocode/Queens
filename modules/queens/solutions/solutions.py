"""
Save solutions in PostgreSQL to
"""

import copy


class Solutions:
    """Save all solutions generated for the algorithm"""

    def __init__(self):
        self.__solutions = {}

    def add_solution(self, board, solution):
        """Add a solution"""
        self.__solutions[solution] = copy.copy(board)

    def get_solution(self, value):
        """Get a specific solution"""
        return self.__solutions[value]

    def get_solutions(self):
        """Return all solutions"""
        return self.__solutions
