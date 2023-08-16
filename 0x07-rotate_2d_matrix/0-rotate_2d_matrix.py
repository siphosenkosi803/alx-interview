#!/usr/bin/python3
'''Given an n x n 2D matrix, rotate it 90 degrees clockwise.'''


def rotate_2d_matrix(matrix):
    '''rotates a 2d matrix 90°'''
    lhs, rhs = 0, len(matrix) - 1

    while lhs < rhs:
        for i in range(rhs - lhs):
            up, down = lhs, rhs
            # save uplhs  value
            upLeft = matrix[up][lhs + i]
            # move down lhs to up lhs
            matrix[up][lhs + i] = matrix[down - i][lhs]
            # move down rhs to down lhs
            matrix[down - i][lhs] = matrix[down][rhs - i]
            # move up rhs to down rhs
            matrix[down][rhs - i] = matrix[up + i][rhs]
            # move up lhs to up rhs
            matrix[up + i][rhs] = upLeft
        rhs -= 1
        lhs += 1

