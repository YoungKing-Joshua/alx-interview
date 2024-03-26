#!/usr/bin/python3
""" 
    Python module tO return list of lists of integers
    representing Pascal’s triangle
"""


def pascal_triangle(n):
    """
        function returns list of lists of integers
        representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    triangle = []

    for col in range(n):
        new_row = []
        for row in range(col + 1):
            if row == 0 or col == row:
                new_row.append(1)
            else:
                new_row.append(triangle[col - 1][row] +
                               triangle[col - 1][row - 1])
        triangle.append(new_row)
    return triangle
