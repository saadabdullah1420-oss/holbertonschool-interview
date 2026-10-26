#!/usr/bin/python3
"""Print every solution to the N queens problem."""

import sys


def solve(n, row, board, columns, diagonals, anti_diagonals):
    """Place non-attacking queens row by row using backtracking."""
    if row == n:
        print([[r, board[r]] for r in range(n)])
        return

    for col in range(n):
        diagonal = row - col
        anti_diagonal = row + col

        if (col in columns or diagonal in diagonals or
                anti_diagonal in anti_diagonals):
            continue

        board.append(col)
        columns.add(col)
        diagonals.add(diagonal)
        anti_diagonals.add(anti_diagonal)

        solve(n, row + 1, board, columns, diagonals, anti_diagonals)

        board.pop()
        columns.remove(col)
        diagonals.remove(diagonal)
        anti_diagonals.remove(anti_diagonal)


def main():
    """Validate the command-line argument and print all solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(n, 0, [], set(), set(), set())


if __name__ == "__main__":
    main()
