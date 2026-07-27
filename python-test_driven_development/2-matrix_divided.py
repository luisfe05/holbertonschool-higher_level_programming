#!/usr/bin/python3
"""Module that provides a function for dividing all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimal places."""
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            res = elem / div
            if res == float('inf') or res == float('-inf') or res != res:
                new_row.append(res)
            else:
                new_row.append(round(res, 2))
        new_matrix.append(new_row)
    return new_matrix
