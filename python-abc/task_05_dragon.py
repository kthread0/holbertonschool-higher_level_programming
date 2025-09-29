#!/usr/bin/env python3
"""Mixins for flying and swimming and a Dragon combining them."""


class SwimMixin:
	"""Provide swim behavior."""
	
	def swim(self):
		print("The creature swims!")


class FlyMixin:
	"""Provide fly behavior."""
	
	def fly(self):
		print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
	"""Dragon composed from SwimMixin and FlyMixin."""
	
	def roar(self):
		print("The dragon roars!")
