#!/usr/bin/env python3
"""CountedIterator keeps an internal iterator and counts fetched items."""


class CountedIterator:
    """Wrap an iterable's iterator and count how many items were returned."""

    def __init__(self, iterable):
        self._iter = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        val = next(self._iter)
        self._count += 1
        return val

    def get_count(self):
        """Return how many items have been yielded so far."""
        return self._count
