#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represents a square geometric shape."""

    def __init__(self, size=0):
        """Initializes square with optional size."""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value checks."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
