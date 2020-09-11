"""
Testing DB utilities of app
"""

from modules.queens.models import Simulation
from modules.queens.connections.database_utilities import add
from . import app
from datetime import datetime

"""Set the N size board"""
n = 10
solutions = 724


def test_create_simulation(app):
    with app.test_request_context("/"):
        simulation = Simulation(
            id=n,
            solutions=solutions,
            time_start=datetime.now(),
            time_end=datetime.now(),
            minutes=0,
        )
        a = add(simulation)
        assert isinstance(a, Simulation)


def test_database_create_or_update(app):
    """Create test data in app"""
    with app.test_request_context("/"):
        simulation = Simulation(
            id=n,
            solutions=solutions,
            time_start=datetime.now(),
            time_end=datetime.now(),
            minutes=0,
        )
        test = add(simulation)
        test.solutions = 5
        add(test)
        test_update = Simulation.query.filter_by(id=n).first()
        assert test_update.solutions == 5
