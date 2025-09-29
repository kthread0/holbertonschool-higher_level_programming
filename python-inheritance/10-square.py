#!/usr/bin/python3
"""Square class built on Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
	"""Square with size validated like Rectangle."""
	
	def __init__(self, size):
		self.integer_validator("size", size)
		super().__init__(size, size)
	
	def __str__(self):
		return f"[Rectangle] {self._Rectangle__width}/{self._Rectangle__height}"
