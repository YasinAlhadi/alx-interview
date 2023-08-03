#!/usr/bin/python3
"""N queens"""
import sys


def solve_n_queeen(n):
    """N queens"""
    n = int(n)
    if n <= 4:
        print("N must be at least 4")
        exit(1)
    if type(n) is not int:
        print("N must be a number")
        exit(1)
    if sys.argv[1].isdigit() is False:
        print("Usage: nqueens N")
        exit(1)

    def isSafe(board, row, col):
        """N queens"""
        for c in range(col):
            if board[c] is row or abs(board[c] - row) is abs(c - col):
                return False
        return True

    def solve(board, col):
        """N queens"""
        if col is n:
            print(str([[c, board[c]] for c in range(n)]))
            return True
        for row in range(n):
            if isSafe(board, row, col):
                board[col] = row
                solve(board, col + 1)
        return False

    solve([0 for i in range(n)], 0)


if __name__ == '__main__':
    n = sys.argv[1]
    solve_n_queeen(n)
