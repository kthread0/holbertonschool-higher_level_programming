#!/usr/bin/python3
"""Matrix division utility.

Provides matrix_divided(matrix, div) which divides all elements by div.
"""


def matrix_divided(matrix, div):
	"""Divide all elements of a matrix by div and return new matrix.

	matrix must be a list of lists of ints/floats and all rows same size.
	div must be a non-zero int/float.
	Each result is rounded to 2 decimals.
	"""
	# Validate matrix structure
	if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	if len(matrix) == 0:
		return []
	row_len = len(matrix[0])
	for row in matrix:
		if len(row) != row_len:
			raise TypeError("Each row of the matrix must have the same size")
		for val in row:
			if not isinstance(val, (int, float)):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

	# Validate div
	if not isinstance(div, (int, float)):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")

	# Compute new matrix
	new_matrix = []
	for row in matrix:
		new_row = [round(val / div, 2) for val in row]
		new_matrix.append(new_row)
	return new_matrix
