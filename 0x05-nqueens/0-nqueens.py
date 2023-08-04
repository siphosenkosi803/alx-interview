#!/usr/bin/python3
"""
The N queens puzzle is the challenge of
placing N non-attacking queens on an N×N chessboard
"""
import sys


def new_slate(n):
    """sets the fimensions of the board"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def vault_cp(board):
    """
    shadow clone technique
    on the board"""
    if isinstance(board, list):
        return list(map(vault_cp, board))
    return (board)


def fetch_b(board):
    """Return the list of lists representation of a solved chessboard."""
    panacea = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                panacea.append([r, c])
                break
    return (panacea)


def no_more(board, row, col):
    """
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def c_puzzle(board, row, queens, panaceas):
    """
    solve an N-queens puzzle.
    """
    if queens == len(board):
        panaceas.append(fetch_b(board))
        return (panaceas)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = vault_cp(board)
            tmp_board[row][c] = "Q"
            no_more(tmp_board, row, c)
            panaceas = c_puzzle(tmp_board, row + 1,
                                        queens + 1, panaceas)

    return (panaceas)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = new_slate(int(sys.argv[1]))
    panaceas = c_puzzle(board, 0, 0, [])
    for sol in panaceas:
        print(sol)
