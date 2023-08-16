#!/usr/bin/python3

""" Given an n x n 2D matrix, rotate it 90 degrees clockwise. """


def rotate_2d_matrix(matrix):
    """ Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place
    You can assume the matrix will have 2 dimensions and will not be empty.
    """
    n = len(matrix)
    first = 0
    last = n - 1

    while first < last:
        offset = 0
        for i in range(first, last):
            temp = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = temp
            offset += 1
        first += 1
        last -= 1

# Sample matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)

# Print the rotated matrix with proper formatting
for row in matrix:
    print(row)
