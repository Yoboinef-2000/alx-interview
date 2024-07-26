#!/usr/bin/python3

"""Implementation of Pascal's Triangle."""

def pascal_triangle(n):
    """Pascal's Triangle."""
    if n <= 0:
        return []

    theNth_pascal = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(theNth_pascal[i - 1][j - 1] + theNth_pascal[i - 1][j])
        row.append(1)
        theNth_pascal.append(row)

    return theNth_pascal
