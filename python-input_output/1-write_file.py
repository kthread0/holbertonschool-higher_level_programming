#!/usr/bin/python3

"""
Write a string to a text file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and
    returns the number of characters written
    """
    with open(filename, "w") as file:
        return file.write(text)
    return None
