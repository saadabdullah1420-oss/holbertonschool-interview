#!/usr/bin/python3
"""Rotate a square matrix in place."""


def rotate_2d_matrix(matrix):
    """Rotate matrix 90 degrees clockwise in place."""
    size = len(matrix)
    for row in range(size):
        for col in range(row + 1, size):
            matrix[row][col], matrix[col][row] = (
                matrix[col][row], matrix[row][col]
            )

    for row_values in matrix:
        row_values.reverse()
