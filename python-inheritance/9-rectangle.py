#!/usr/bin/python3
"""Rectangle with area and string representation."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with width and height stored privately."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area (width * height)."""
        return self.__width * self.__height

    def __str__(self):
        """Return string in format [Rectangle] width/height."""
        return f"[Rectangle] {self.__width}/{self.__height}"
