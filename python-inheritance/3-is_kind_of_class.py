#!/usr/bin/python3
"""Type checking helpers."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance or subclass of a_class."""
    return isinstance(obj, a_class)
