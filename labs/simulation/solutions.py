import copy


class Solutions:
    def __init__(self):
        self.__solutions = {}

    def add_solution(self, board, solution):
        self.__solutions[solution] = copy.copy(board)

    def drop_solution(self, value):
        self.__solutions.pop(value)

    def get_solution(self, value):
        return self.__solutions[value]

    def get_solutions(self):
        return self.__solutions
