"""Test cases for module queens"""
from modules.queens.utilities.json_array_operations import convert_array_in_json
from modules.queens.simulation.simulation import Simulation
import json
from . import app


def test_json(app):
    player = Simulation(8)
    player.start()
    a = player.get_game()

    j = convert_array_in_json(a)
    result = True
    try:
        json.loads(j)
    except ValueError as err:
        result = False

    assert result
