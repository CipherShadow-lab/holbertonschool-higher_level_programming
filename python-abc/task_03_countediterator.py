#!/usr/bin/python3

class CountedIterator():
    """An interator that tracks number of items iterated over."""

    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return next item and increment counter"""
        try:
            item = next(self.iterable)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return count number of items iterated."""
        return self.count

    def __iter__(self):
        "Return iterator."
        return self
