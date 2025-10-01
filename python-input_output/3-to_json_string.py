#!/usr/bin/python3

import json

""" 
Module that defines a function to return the JSON representation of an object
"""


def to_json_string(obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(obj)
