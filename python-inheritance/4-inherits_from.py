#!/usr/bin/python3
"""Check if object is instance of a subclass of a given class."""


def inherits_from(obj, a_class):
    """Return True if obj's class is a subclass of a_class (not same)."""
    obj_type = type(obj)
    return issubclass(obj_type, a_class) and obj_type is not a_class
