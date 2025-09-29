#!/usr/bin/env python3
"""VerboseList extends list and logs changes."""


class VerboseList(list):
    """List subclass that prints notifications on mutations."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = 0
        for _ in iterable:
            count += 1
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        return super().remove(item)

    def pop(self, index=-1):
        val = self[index]
        print(f"Popped [{val}] from the list.")
        return super().pop(index)
