"""
Testing save solutions
"""
from modules.queens.solutions.solutions import Solutions
from modules.queens.simulation.board import Board
from modules.queens.utilities.json_array_operations import convert_json_in_array
from modules.queens.models import Simulation
from . import app

"""Set the N size board"""
n = 10


def test_solution(app):
    board = Board(n)
    s = Solutions(n=n, persistence=False)
    assert s.add_solution(board.get_board())
    assert len(s.get_solution(1)) == n
    assert len(s.get_solutions(1)) > 0
    assert s.is_valid_in_range_of_minutes() is None
    assert s.validate_if_continue()
    assert s.update_simulation() is None


def test_solution_with_persistence(app):
    with app.test_request_context("/"):
        board = Board(n)
        s = Solutions(n=n, persistence=True)
        assert isinstance(s.update_simulation(), Simulation)
        assert s.add_solution(board.get_board())
        assert len(convert_json_in_array(s.get_solution(1).solution)) == n
        assert len(s.get_solutions(1).items) > 0
        assert s.is_valid_in_range_of_minutes() is None
        assert s.validate_if_continue()
