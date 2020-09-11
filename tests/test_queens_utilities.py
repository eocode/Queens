"""
Test cases for module queens
Testing utilities
"""
from modules.queens.utilities.json_array_operations import (
    convert_array_in_json,
    convert_json_in_array,
)
from modules.queens.utilities.time import count_elapsed_time
import json
import numpy as np
from . import app


def test_converter_in_json(app):
    """Test if Json converter works"""
    test_array = np.zeros((2, 2))
    testing_json = convert_array_in_json(test_array)
    result = True
    try:
        json.loads(testing_json)
    except ValueError as err:
        result = False

    assert result


def test_converter_in_array(app):
    test_array = np.zeros((2, 2))
    testing_json = convert_array_in_json(test_array)
    result = convert_json_in_array(testing_json)
    assert result[0][0] == 0


@count_elapsed_time
def timer():
    """Test function"""
    print("hello")


def test_elapsed_time_decorator(app):
    """Test if decorator time works"""
    res = timer()

    assert res is None
