#!/usr/bin/python3


class MyList(list):
    """
    Custom list subclass with extra utility methods.
    """

    def print_sorted(self):
        """
        Prints the list elements sorted in ascending order.
        """
        print(sorted(self))
