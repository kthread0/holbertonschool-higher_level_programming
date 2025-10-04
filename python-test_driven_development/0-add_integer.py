#!/usr/bin/python3
"""Module that defines add_integer function following project spec.

Functions
---------
add_integer(a, b=98)
        Add two integers or floats (floats are cast to int).
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    a and b must be integers or floats (floats are cast to int).
    Raises TypeError with specific messages when types are invalid.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
