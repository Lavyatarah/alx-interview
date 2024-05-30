import sys

def is_safe(row, col, board):
    """Checks if placing a queen at (row, col) is safe (no attacks)."""
    n = len(board)
    # Check for queens in the same row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check for queens in diagonals (upward and downward)
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col, n):
    """Solves the N-queens problem recursively."""
    if col == n:
        # Reached the last column, print the solution
        for row in board:
            print(''.join(row))
        return

    for i in range(n):
        # Check if placing a queen at (i, col) is safe
        if is_safe(i, col, board):
            board[i][col] = 'Q'
            solve_nqueens(board, col + 1, n)  # Recursively solve for next column
            board[i][col] = '.'  # Backtrack for other solutions

def main():
    """Handles program arguments and calls the N-queens solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    # Create an empty NxN board
    board = [['.'] * n for _ in range(n)]

    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()

