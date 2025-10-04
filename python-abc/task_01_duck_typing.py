#!/usr/bin/env python3
"""Shapes using abstract base class and duck typing."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract shape requiring area and perimeter methods."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""


class Circle(Shape):
    """Circle defined by a radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of any object following Shape protocol."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
