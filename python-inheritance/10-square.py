#!/usr/bin/python3
"""Square class that inherits from Rectangle (9-rectangle)."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square shape where width and height are equal (size)."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """String representation uses Rectangle's format [Rectangle] w/h."""
        return f"[Rectangle] {self._Rectangle__width}/{self._Rectangle__height}"
