#!/usr/bin/python3

"""The Queen Module."""
from sys import argv


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, n, solutions):
    """Utility function to solve the N Queens problem."""
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack


def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if len(argv) > 2 or len(argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n_queen = int(argv[1])
solve_nqueens(n_queen)
