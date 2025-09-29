#!/usr/bin/python3
"""Custom list subclass with a sorted print helper."""


class MyList(list):
	"""List subclass that can print itself sorted."""
	
	def print_sorted(self):
		"""Print the list items in ascending order."""
		print(sorted(self))
