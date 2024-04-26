#!/usr/bin/python3
"""This module defines a function that rotates a matrix"""


def rotate_2d_matrix(matrix):
    """Rotates the matrix passed in as an argument"""
    size = len(matrix)

    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for arr in matrix:
        arr.reverse()
