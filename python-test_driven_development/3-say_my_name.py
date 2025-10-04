#!/usr/bin/python3
"""Function to print a full name with validation.

Contains say_my_name(first_name, last_name='') which prints
"My name is <first_name> <last_name>" after validating inputs.
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first> <last>' after validating types.

    Raise TypeError if first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
