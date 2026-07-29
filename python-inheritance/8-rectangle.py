#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class representing a rectangle geometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with validated private width and height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
