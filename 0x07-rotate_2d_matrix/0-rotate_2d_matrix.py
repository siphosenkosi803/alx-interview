#!/usr/bin/python3
"""Rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
       Given an n x n 2D matrix,
       rotate it 90 degrees clockwise.
    """
    lhs, rhs = 0, len(matrix) - 1

    while lhs < rhs:
        for i in range(rhs - lhs):
            top, down = lhs, rhs
            topLeft = matrix[top][lhs + i]
            matrix[top][lhs + i] = matrix[down - i][lhs]
            matrix[down - i][lhs] = matrix[down][rhs - i]
            matrix[down][rhs - i] = matrix[top + i][rhs]
            matrix[top + i][rhs] = topLeft
        rhs -= 1
        lhs += 1
