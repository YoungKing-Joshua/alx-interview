#!/usr/bin/python3
"""
this defines a method that calculate the fewest number of operations
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    calculating the most little number of operations needed
    to result in exactly n H characters in the file
    """
    if n <= 0:
        return 0

    len_H = 1
    len_copied_H = 0
    total_operations = 0

    while len_H < n:
        if n % len_H == 0:
            total_operations += 2
            len_copied_H = len_H
            len_H += len_copied_H
        else:
            total_operations += 1
            len_H += len_copied_H

    return total_operations
