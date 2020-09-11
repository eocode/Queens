"""
    Queens algorithms to solve
"""
from simulation.queen import Queen
from simulation.board import Board
from simulation.final.board import Board as Board_2
from simulation.final.queen import Queen as Queen_2
from simulation.solutions import Solutions
import random
import copy


class NQueens:
    def __init__(self):
        self.solutions = Solutions()

    @staticmethod
    def solve(n, solutions):
        for key, board in list(solutions.get_solutions().items()):
            for row in range(n):
                queen = Queen(row, 0, row)
                if row not in board.get_safe_x():
                    for col in range(n):
                        if col not in board.get_safe_y():
                            if queen.valid_move(board.get_board(), n, row, col):
                                b = Board(n)
                                b.set_board(copy.copy(board.get_board()))
                                b.set_track_solution(
                                    copy.copy(board.get_track_solution()),
                                    copy.copy(board.get_value_track()),
                                )
                                b.set_safe(
                                    copy.copy(board.get_safe_x()),
                                    copy.copy(board.get_safe_y()),
                                )
                                b.add_safe(row, col)
                                b.put_piece(row, col, queen.get_piece_symbol())
                                solutions.add_solution(b)
            # print("Board eliminado")
            solutions.drop_solution(key)

        return solutions

    @staticmethod
    def solve2(n, solutions):
        for key, board in list(solutions.get_solutions().items()):
            print(
                board.get_board(),
                board.x_values,
                board.get_value_track(),
                board.get_track_solution(),
            )
            for row in board.x_values.keys():
                for col in list(board.x_values[row].values()):
                    queen = Queen(row, col, row)
                    apply, new_values = queen.attack(
                        row,
                        col,
                        copy.deepcopy(board.x_values),
                        board.get_safe_queens(),
                        board.n,
                    )
                    if apply:
                        b = Board(n)
                        b.set_board(copy.copy(board.get_board()))
                        b.set_track_solution(
                            copy.copy(board.get_track_solution()),
                            copy.copy(board.get_value_track()),
                        )
                        b.set_safe_board(new_values)
                        b.add_safe(row, col)
                        b.put_piece(row, col, queen.get_piece_symbol())
                        solutions.add_solution(copy.copy(b))
            solutions.drop_solution(key)

    @staticmethod
    def solve3(n):
        # print(board.get_board(), board.x_values)
        board = NQueens.create_board(n)
        NQueens.n_queens(board)

    @staticmethod
    def create_board(n):
        board = Board_2(n)
        board.x_values = {v: {c: c for c in range(0, n)} for v in range(n)}
        return board

    @staticmethod
    def n_queens(board):

        row = 0
        col = 0
        cursor_x = 0
        cursor_y = 0

        solutions = Solutions()

        while row <= board.n:

            # print("Entry", row, col, board.x_values, board.get_safe_queens())

            if row in board.x_values.keys():
                x = board.x_values[row]

                if col in x:
                    y = x[col]
                    # print(board.get_board(), 'Coordenada before', row, col, board.x_values)
                    apply, values = Queen_2.attack(row, col, board.x_values)
                    if apply:
                        board.put_piece(row, col, 1)
                        board.add_safe()
                        # print(board.get_board(), 'Coordenada after', row, col, board.x_values)
                    else:
                        board = NQueens.create_board(board.n)
                        cursor_y += 1
                        if cursor_y == board.n:
                            cursor_x += 1
                            cursor_y = 0
                        row = cursor_x
                        col = cursor_y
                        # print("Sin solución")
                        continue

            if len(board.x_values) > 0:
                row = random.choice(list(board.x_values.keys()))
                # print('Get row col:', row, col, board.x_values.keys(), board.x_values[row].values())
                col = random.choice(list(board.x_values[row].values()))
                # print('Validate row col:', row, col)

            if board.all_queens_are_safe():
                solutions.add_solution(board)
                board = NQueens.create_board(board.n)
                cursor_y += 1
                if cursor_y == board.n:
                    cursor_x += 1
                    cursor_y = 0
                row = cursor_x
                col = cursor_y

            if Board_2.validate_end(row, col) == board.end:
                break

            # if board.get_safe_queens() == board.n - 1:
            #     print(board.get_board(), "Solved")
            #     return True

        print("Solutions: ", len(solutions.get_solutions()))
        for key, values in solutions.get_solutions().items():
            print(values.get_board(), key)
        print("Solutions: ", len(solutions.get_solutions()))

    def solve4(self, n):
        # print(board.get_board(), board.x_values)
        board = NQueens.create_board(n)
        self.n_queens_2(board.get_board(), 0, board.x_values)
        return self.solutions

    def n_queens_2(self, board, col, positions):
        if col == len(board):
            self.solutions.add_solution(board, len(self.solutions.get_solutions()) + 1)
            return True

        for row in range(len(board)):
            if row in positions.keys() and col in positions[row]:
                # print("Tree", row, col)
                apply, values = Queen_2.attack(row, col, copy.deepcopy(positions))
                if apply:
                    # print(board)
                    board[row][col] = 1
                    self.n_queens_2(board, col + 1, values)
                    board[row][col] = 0
