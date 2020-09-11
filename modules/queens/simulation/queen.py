"""
    Class for simulate queen piece
"""


class Queen:
    """Queen class"""

    @staticmethod
    def attack(x, y, available):
        """Simulate attack
        * Validate if x and is safe
        * Validate if diagonal is safe
        * Delete posibilities in board
        """
        if Queen.safe_xy(x, y, available):
            if Queen.safe_diagonal(x, y, available):
                return True, available
        return False, available

    @staticmethod
    def safe_xy(x, y, available):
        """Validate x in y
        Delete positions in x
        Delete cols for y positions in n rows
        if one col will be empty, the solution ends
        """
        if x in available.keys():
            available.pop(x)
        for row, col in available.items():
            if y in col:
                col.pop(y)
            if len(col) == 0:
                return False
        return True

    @staticmethod
    def safe_diagonal(x, y, available):
        """Validate diagonal
        Delete all restant positions in board for x and y
        """
        for j, k in available.items():
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
        return True
