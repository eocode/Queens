"""Convert array - json structures"""
import json


def convert_array_in_json(array):
    """
    Converter
    Return an array in a json
    """

    # Return array in json
    lists = array.tolist()
    return json.dumps(lists)
