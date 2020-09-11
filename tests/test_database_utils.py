"""
Testing DB utilities of app
"""

from modules.queens.models import Simulation
from modules.queens.simulation.board import Board
from modules.queens.utilities.json_array_operations import convert_array_in_json
from modules.queens.connections.database_utilities import create_or_update
from . import app
from app import db

"""Set the N size board"""
n = 10


def test_database_create_or_update(app):
    """Create test data in app"""
    with app.test_request_context("/"):
        test_board = Board(n)
        json_board = convert_array_in_json(test_board.get_board())
        test = Simulation(id=n, solutions=0, board=json_board)
        db.session.add(test)
        test_create = Simulation.query.filter_by(id=n).first()
        assert test_create.id == n
        test.solutions = 5
        create_or_update(test)
        test_update = Simulation.query.filter_by(id=n).first()
        assert test_update.solutions == 5
