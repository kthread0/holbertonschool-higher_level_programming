#!/usr/bin/python3
"""Base geometry with abstract area method."""


class BaseGeometry:
    """Base class that declares area() to be implemented."""

    def area(self):
        raise Exception("area() is not implemented")
