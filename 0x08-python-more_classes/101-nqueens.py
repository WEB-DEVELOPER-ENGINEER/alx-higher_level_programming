#!/usr/bin/python3
"""nqueens
"""


import sys


def nqueens(N):
    '''
        Check that N is a valid integer
    '''
    if not isinstance(N, int) or N < 4:
        print("N must be an integer greater or equal to 4")
        sys.exit(1)

    # Initialize the board as an empty list of N lists
    board = [0] * N

    def place_queens(row):
        '''
            Recursive function to place queens on the board.
            If we've placed all N queens, print the board and return
        '''
        if row == N:
            print_board(board)
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_valid_position(board, row, col):
                board[row] = col
                place_queens(row + 1)

    def print_board(board):
        '''
            Helper function to print the board in the required format
        '''
        print([[row, col] for row, col in enumerate(board)])

    def is_valid_position(board, row, col):
        '''
            function to check if a queen can be placed in a given position
        '''
        # Check the rows above
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == row - r:
                return False

        return True

    # Start the recursive function with the first row
    place_queens(0)

# Check that the program was called with the correct number of arguments


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Convert the argument to an integer before passing it to the nqueens function
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Call the nqueens function with the user-provided argument
nqueens(N)
