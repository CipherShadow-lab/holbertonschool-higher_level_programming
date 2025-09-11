#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor - int or float.

    Returns:
        A new matrix with all elements divided and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Check that matrix is a list of lists
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Check that each element is an int or float
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)" \
                    "of integers/floats"
                    )

    # Check that all rows are the same length
    first_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check that div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for NaN or infinity
    if div != div or div in (float('inf'), float('-inf')):
        raise TypeError("div must be a number")

    # Check that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with each element divided and rounded
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
