#!/usr/bin/python3
"""
   Describes a function that returns the perimeter
   of the island described in grid
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""

    perimeter = 0

    for index, y in enumerate(grid):

        for x in range(len(y)):
            if y[x] == 1:
                # check for water on the west
                if y[x - 1] == 0 or not y[x - 1]:
                    perimeter += 1

                # check for water on the east
                if y[x + 1] == 0 or not y[x + 1]:
                    perimeter += 1

                # check for water on the north
                if y[index - 1] == 0 or not y[index - 1]:
                    perimeter += 1

                # check for water on the south
                if y[index + 1] == 0 or not y[index + 1]:
                    perimeter += 1

    return perimeter
