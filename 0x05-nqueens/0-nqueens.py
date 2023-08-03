#!/usr/bin/env python3
"""
The N queens puzzle
is the challenge of placing N non-attacking queens on an N×N chessboard.
"""
import sys

def vibes_c(board, row, col):
    # Check if the current position (row, col) is safe for placing a queen
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            # If there's already a queen in the same column or on the same diagonal, return False (not safe)
            return False
    return True

def fixer(N, board, row):
    # Recursive function to solve the N-Queens problem
    if row == N:
        # If all rows are filled (all queens are placed), print the solution
        print([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if vibes_c(board, row, col):
            # If the current position is safe, place a queen and move to the next row
            board[row] = col
            fixer(N, board, row + 1)

def nqueens(N):
    # Main function to solve the N-Queens problem for the given N
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    fixer(N, board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

