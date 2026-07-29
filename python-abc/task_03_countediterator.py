#!/usr/bin/python3
"""
Module providing a CountedIterator class that tracks iteration counts.
"""


class CountedIterator:
    """
    Iterator wrapper that keeps track of the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator object and the iteration counter.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current count of iterated items.
        """
        return self.count

    def __next__(self):
        """
        Fetches the next item, increments the count, and returns the item.
        """
        item = next(self.iterator)
        self.count += 1
        return item
