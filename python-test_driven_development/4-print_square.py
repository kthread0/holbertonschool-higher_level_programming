#!/usr/bin/python3
"""Print a square made of # characters.

Contains print_square(size) which validates size and prints a square.
"""


def print_square(size):
	"""Print a square of '#' characters of given size.

	size must be an integer >= 0. If size is not int (and not float with
	integral value) raise TypeError, value < 0 raises ValueError.
	"""
	if type(size) is float:
		raise TypeError("size must be an integer")
	if type(size) is not int:
		raise TypeError("size must be an integer")
	if size < 0:
		raise ValueError("size must be >= 0")
	for _ in range(size):
		print('#' * size)
