"""Convert array - json structures"""
import json
import numpy as np


def convert_array_in_json(array):
    """
    Converter
    Return an array in a json
    """

    # Return array in json
    lists = array.tolist()
    return json.dumps(lists)


def convert_json_in_array(js):
    """
    Converter
    Return array
    """
    lst = json.loads(js)
    return np.array(lst)
