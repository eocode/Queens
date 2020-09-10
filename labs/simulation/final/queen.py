"""
    Valid queen moves
"""


class Queen:

    @staticmethod
    def attack(x, y, available):
        if Queen.__safe_xy(x, y, available):
            if Queen.__safe_diagonal(x, y, available):
                return True, available
        return False, available

    @staticmethod
    def __safe_xy(x, y, available):
        # print("Adentro", x, y, available)
        if x in available.keys():
            available.pop(x)
        for row, col in available.items():
            if y in col:
                col.pop(y)
            if len(col) == 0:
                return False
        return True

    @staticmethod
    def __safe_diagonal(x, y, available):
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
