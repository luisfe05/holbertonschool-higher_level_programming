#!/usr/bin/python3
"""
Module defining a VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """
    Subclass of list that prints notifications on modification methods.
    """

    def append(self, item):
        """
        Appends an item to the list and prints a notification.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extends the list with an iterable and prints a notification.
        """
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """
        Removes an item from the list and prints a notification.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item from the list and prints a notification.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
