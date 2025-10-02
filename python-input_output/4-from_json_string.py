#!/usr/bin/python3

"""
Convert a JSON string to a Python object.
Returns:
    dict: The Python object representation of the JSON string.
"""

import json


def from_json_string(my_dict):
    """
    :param my_dict: Description
    """
    return json.loads(my_dict)
