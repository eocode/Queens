"""Convert array - json structures"""
import json


def convert_array_in_json(array):
    """Return an array in a json"""
    lists = array.tolist()
    return json.dumps(lists)
