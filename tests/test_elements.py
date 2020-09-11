"""
Test cases for elements of the n queens
This file test Board and Queen funcs
"""
from modules.queens.simulation.queen import Queen
from modules.queens.simulation.board import Board
from . import app

"""Set the N size board"""
n = 10


def test_board(app):
    """Test board functionalities"""
    board = Board(n)
    board.create_board()
    board.create_positions()
    test_b = board.get_board()
    test_positions = board.get_positions()
    assert len(test_b) == n
    assert len(test_positions.keys()) == n
    assert len(test_positions[n - 1]) == n


def test_attack_xy(app):
    """Test if Json converter works"""
    board = Board(n)
    queen = Queen()
    valid, positions = queen.attack(n / 2, n / 2, board.get_positions())

    assert valid
    assert len(positions.keys()) > 0


def test_if_xy_are_safe(app):
    """Test if Json converter works"""
    board = Board(n)
    queen = Queen()
    result = queen.safe_xy(n / 2, n / 2, board.get_positions())

    assert result


def test_if_diagonal_are_safe(app):
    """Test if Json converter works"""
    board = Board(n)
    queen = Queen()
    result = queen.safe_diagonal(n / 2, n / 2, board.get_positions())

    assert result
