"""Test cases for module queens"""
from modules.queens.utilities.json_array_operations import convert_array_in_json
from modules.queens.algorithms.queens import Queens
import json
from . import app


def test_json(app):
    player = Queens(8)
    player.create_board()
    a = player.get_board()
    j = convert_array_in_json(a)
    result = True
    try:
        json.loads(j)
        print("Hola")
    except ValueError as err:
        result = False

    assert result
