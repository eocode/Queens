"""
    Valid queen moves
"""


class Queen:

    def __init__(self, x, y, number):
        self.number = number
        self.x = x
        self.y = y
        self.__conflicts = True
        self.__piece_symbol = 1
        self.__selected = 0

    def add_selected(self):
        self.__selected += 1

    def get_selected(self):
        return self.__selected

    def remove_conflict(self):
        self.__conflicts = False

    def is_conflict(self):
        return self.__conflicts

    def get_piece_symbol(self):
        return self.__piece_symbol

    def set_current_position(self, x, y):
        self.x = x
        self.y = y

    def valid_move(self, board, n, x, y):
        # if self.__attack_y(board, n, x, y):
        #     return False
        if self.__attack_x(board, n, x, y):
            return False
        if self.__attack_diagonal(board, n, x, y):
            return False
        return True

    def simulate_if_can_move(self, board, n, x, y):
        board[self.x, self.y] = 0
        if self.__attack_y(board, n, x, y):
            board[self.x, self.y] = self.get_piece_symbol()
            return False
        if self.__attack_x(board, n, x, y):
            board[self.x, self.y] = self.get_piece_symbol()
            return False
        if self.__attack_diagonal(board, n, x, y):
            board[self.x, self.y] = self.get_piece_symbol()
            return False
        return True

    def __attack_y(self, board, n, x, y):
        points = 0
        for i in range(n):
            if x + i < n:
                points += board[x + i][y]
            if x - i >= 0 and x - i != x:
                points += board[x - i][y]
        return self.__determinate_if_attack(points)

    def __attack_x(self, board, n, x, y):
        points = 0
        for i in range(n):
            if y + i < n:
                points += board[x][y + i]
            if y - 1 >= 0 and y - i != y:
                points += board[x][y - i]
        return self.__determinate_if_attack(points)

    def __attack_diagonal(self, board, n, x, y):
        points = 0
        for i in range(n):
            # Right Diagonal Validation
            if y + i < n and x + i < n:
                points += board[x + i][y + i]
            if y - i >= 0 and x - i >= 0 and y - i != y and x - i != x:
                points += board[x - i][y - i]
            # Left Diagonal Validation
            if n > y - i >= 0 and x + i < n:
                points += board[x + i][y - i]
            if y + i < n and x - i >= 0 and y + i != y and x - i != x:
                points += board[x - i][y + i]
        return self.__determinate_if_attack(points)

    def attack(self, x, y, available, safe_queens, n):
        if self.__safe_xy(x, y, available, n - safe_queens - 1):
            if self.__safe_diagonal(x, y, available, n - safe_queens - 1):
                return True, available
        return False, available

    def __safe_xy(self, x, y, available, safe_queens):
        available.pop(x)
        for row, col in available.items():
            if y in col:
                col.pop(y)
            if len(col) == 0:
                return False
        return True

    def __safe_diagonal(self, x, y, available, safe_queens):
        # print('Diagonal: ', x, y, available, safe_queens)
        for j, k in available.items():
            # print('Iterando: ', j, k, y + j - x)
            # Right up
            if j < x and y + x - j in k:
                k.pop(y + x - j)
            # Left up
            if j < x and y - x + j in k:
                k.pop(y - x + j)
            # Right down
            if j >= x and y + j - x in k:
                k.pop(y + j - x)
            # Left down
            if j > x and y - j + x in k:
                k.pop(y - j + x)
            if len(k) == 0:
                return False
            # if safe_queens > len(available.keys()):
            #     return False
        # print('End Diagonal: ', x, y, available, safe_queens)
        return True

    def __determinate_if_attack(self, points):
        if points >= self.get_piece_symbol():
            return True
        else:
            return False
