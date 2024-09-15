#!/usr/bin/python3

"""Rotating a 2D matrix."""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise."""
    theN = len(matrix)

    i = 0

    while i < theN:
        j = i
        while j < theN:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            j += 1
        i += 1

    for z in range(theN):
        matrix[z].reverse()
