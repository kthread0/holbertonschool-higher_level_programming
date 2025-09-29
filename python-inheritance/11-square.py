#!/usr/bin/python3
"""Square class that prints as [Square]."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that uses Rectangle for implementation."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
