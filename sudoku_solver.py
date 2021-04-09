"""
sudoku solver using backtracking
author: Ofir Yaffe
"""
import time
import numpy as np
SIZE = 9
BLOCK_SIZE = 3

def print_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print()

def check_row(board, row, n):
    for col in board[row]:
        if n == col:
            return False
    return True


def check_col(board, col, n):
    for row in board:
        if n == row[col]:
            return False
    return True

def check_block(board, n_row, n_col, n):
    row_border_start = n_row - n_row % BLOCK_SIZE
    row_border_end = row_border_start + BLOCK_SIZE
    col_border_start = n_col - n_col % BLOCK_SIZE
    col_border_end = col_border_start + BLOCK_SIZE
    for row in range(row_border_start, row_border_end):
        for col in range(col_border_start, col_border_end):
            if n == board[row][col]:
                return False
    return True


def solve_sudoku(board):
    row, col = check_empty(board)
    if row is None and col is None:
        return True

    for n in range(1, SIZE + 1):
        if check_row(board, row, n) and check_col(board, col, n) and check_block(board, row, col, n):
            board[row][col] = n
            if solve_sudoku(board):
                return True
            board[row][col] = 0

def check_empty(board, depth=0):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                return row, col
    return None, None


def main():
    arr = np.array([[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]], dtype=int)
    print("unsolved:")
    print_board(arr)
    start_time = time.time()
    if solve_sudoku(arr):
        print(f"solved in time: {time.time() - start_time}")
        print_board(arr)
    else:
        print("there was no solution")

if __name__ == '__main__':
    main() 
