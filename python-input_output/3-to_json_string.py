#!/usr/bin/python3

"""
Module that defines a function to return the JSON representation of an object
"""

import json


def to_json_string(obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(obj)
