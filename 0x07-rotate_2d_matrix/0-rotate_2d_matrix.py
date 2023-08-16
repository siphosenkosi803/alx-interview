#!/usr/bin/python3

""" Given an n x n 2D matrix, rotate it 90 degrees clockwise. """


def rotate_2d_matrix(matrix):
    """ Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place
    You can assume the matrix will have 2 dimensions and will not be empty.
    """
    n = len(matrix)
    begin = 0
    end = n - 1

    while begin < end:
        offset = 0
        for i in range(begin, end):
            exo = matrix[begin][i]
            matrix[begin][i] = matrix[end - offset][begin]
            matrix[end - offset][begin] = matrix[end][end - offset]
            matrix[end][end - offset] = matrix[i][end]
            matrix[i][end] = exo
            offset += 1
        begin += 1
        end -= 1

# Sample matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)

# Print the rotated matrix with proper formatting
for row in matrix:
    print(row)

