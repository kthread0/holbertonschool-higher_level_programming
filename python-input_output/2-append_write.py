#!/usr/bin/python3

"""
Module that defines a function to append text to a file
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file
    """

    with open(filename, "a") as file:
        return file.write(text)
    return None
