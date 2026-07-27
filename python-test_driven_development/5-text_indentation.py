#!/usr/bin/python3
"""Module that provides a function for formatting text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':' characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start_of_line = True
    for char in text:
        if start_of_line and char == ' ':
            continue
        start_of_line = False
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n")
            start_of_line = True
