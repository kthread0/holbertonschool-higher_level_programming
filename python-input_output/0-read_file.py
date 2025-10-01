#!/usr/bin/python3

"""
Module that defines a function to read a text file
"""

def read_file(filename=""):
    """Reads a text file"""
    with open(filename) as file:
        print(file.read(), end="")
    return None