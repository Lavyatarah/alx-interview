#!/usr/bin/python3

"""import sys module"""

import sys


"""create a function"""


def print_solution(solutions):
    """function takes a list of solutions where each solution
    is represented as a list of [row, column] pairs
    indicating the positions of the queens on the chessboard.
    """
    for solution in solutions:
        print(solution)


def is_safe(board, row, col, n):
    """This function determines if it's safe to place
    a queen at the board position [row, col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    """Check upper diagonal on left side"""
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    """Check lower diagonal on left side"""
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n, solutions):
    """recursive function attempts to solve the N-Queens problem"""
    if col >= n:
        solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens(board, col + 1, n, solutions)
            board[i][col] = 0  # backtrack


def nqueens(n):
    """main function that sets up the board
    and calls the backtracking solver function
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    print_solution(solutions)


if __name__ == "__main__":
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
    nqueens(n)
