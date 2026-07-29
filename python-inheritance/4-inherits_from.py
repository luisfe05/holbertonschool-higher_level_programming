#!/usr/bin/python3
"""
This module provides a function to check if an object inherits from
a specified class directly or indirectly, excluding exact class matches.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from
    a_class (subclass check); otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
