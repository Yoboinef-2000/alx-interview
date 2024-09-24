#!/usr/bin/python3

"""
This function returns the perimeter of the
island described in grid.
"""


def island_perimeter(grid):
    """Look at the first comment."""
    totalPerimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    totalPerimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    totalPerimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    totalPerimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    totalPerimeter += 1

    return totalPerimeter
