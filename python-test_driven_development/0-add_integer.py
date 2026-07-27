#!/usr/bin/python3
"""Module that provides a function for adding two integers."""


def add_integer(a, b=98):
    """Adds two numbers after casting floats to integers."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    try:
        a = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")
    return a + b
