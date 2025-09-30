#!/usr/bin/python3
"""Module returns a list of lists where each row
is a row of Pascal's triangle."""


def pascal_triangle(n):
    """returns a list of rows - Pascal's Triangle."""

    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
