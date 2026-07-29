#!/usr/bin/python3
"""
This module defines a MyList class that inherits from list.
"""


class MyList(list):
    """
    Subclass of list with additional utility methods.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        """
        print(sorted(self))
