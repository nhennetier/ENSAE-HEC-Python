#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 9 19:32:10 2019

@author: alex
"""

def solve_sudoku(sudoku):
    solve_sudoku_aux(sudoku, 0, 0)
    sudoku.show()


def next_item(i, j):
    if j < 8:
        return (i, j + 1)
    if i < 8:
        return (i + 1, 0)
    return (-1, -1)


def solve_sudoku_aux(sudoku, i, j):

    if sudoku.complete():
        return True

    if i == -1 and j == -1:
        return False

    next_i, next_j = next_item(i, j)

    if sudoku[i, j] == -1:
        for k in range(1, 10):
            if sudoku.mark(i, j, k) and solve_sudoku_aux(sudoku, next_i, next_j):
                return True
        sudoku.mark(i, j, -1)
        return False
    else:
        return solve_sudoku_aux(sudoku, next_i, next_j)


if __name__ == '__main__':
    from sudoku import Sudoku
    import numpy as np
    import time

    values = np.load('./exemple_sudoku.npy')
    game = Sudoku(values)
    game.show()
    t1 = time.time()
    solve_sudoku(game)
    t2 = time.time()
    print(f"Le solveur a pris {t2 - t1} secondes.")
