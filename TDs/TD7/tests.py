import numpy as np


def test_exo_1(sudoku):
    xs = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]
    ys = [0, 1, 4, 3, 4, 5, 1, 2, 7, 0, 4, 8, 3, 5, 8, 0, 4, 8, 1, 6, 7, 4, 5, 8, 4, 7, 8]
    vs = [5, 3, 7, 1, 9, 5, 9, 8, 6, 8, 6, 3, 8, 3, 1, 7, 2, 6, 6, 2, 8, 1, 9, 5, 8, 7, 9]
    grid = np.zeros((9, 9)).astype(int)
    for x, y, v in zip(xs, ys, vs):
        grid[x, y] = v
    try:
        assert np.all(sudoku.grid == grid)
        print('Exercice 1 réussi.')
    except Exception:
        print('Pas encore !')


def test_exo_2(Sudoku):
    grid = np.ones((9, 9)).astype(int)
    sudoku = Sudoku(grid)
    for line in range(9):
        if sudoku.is_valid_row(line):
            print('Pas encore !')
            return
    sudoku.grid[0, :] = np.zeros(9)
    if not sudoku.is_valid_row(0):
        print('Pas encore !')
        return
    sudoku.grid[1, :] = list(range(1, 10))
    if not sudoku.is_valid_row(1):
        print('Pas encore !')
        return
    sudoku.grid[2, :] = [3, 0, 0, 0, 0, 0, 0, 0, 3]
    if sudoku.is_valid_row(2):
        print('Pas encore !')
        return
    print('Exercice 2 réussi')


def test_exo_3(Sudoku):
    grid = np.ones((9, 9)).astype(int)
    sudoku = Sudoku(grid)
    for line in range(9):
        if sudoku.is_valid_column(line):
            print('Pas encore !')
            return
    sudoku.grid[:, 0] = np.zeros(9)
    if not sudoku.is_valid_column(0):
        print('Pas encore !')
        return
    sudoku.grid[:, 1] = list(range(1, 10))
    if not sudoku.is_valid_column(1):
        print('Pas encore !')
        return
    sudoku.grid[:, 2] = [3, 0, 0, 0, 0, 0, 0, 0, 3]
    if sudoku.is_valid_column(2):
        print('Pas encore !')
        return
    print('Exercice 3 réussi')


def test_exo_4(Sudoku):
    grid = np.ones((9, 9)).astype(int)
    sudoku = Sudoku(grid)
    for row in range(9):
        for column in range(9):
            if sudoku.is_valid_square(row, column):
                print('Pas encore !')
                return
    sudoku.grid[0:3, 0:3] = np.zeros((3, 3))
    if not sudoku.is_valid_square(0, 1):
        print('Pas encore !')
        return
    sudoku.grid[3:6, 3:6] = np.arange(1, 10).reshape((3, 3))
    if not sudoku.is_valid_square(5, 4):
        print('Pas encore !')
        return
    sudoku.grid[6:9, 6:9] = np.array([3, 0, 0, 0, 0, 0, 0, 0, 3]).reshape((3, 3))
    if sudoku.is_valid_square(6, 7):
        print('Pas encore !')
        return
    print('Exercice 4 réussi')


def test_exo_5(Sudoku):
    grid = np.ones((9, 9)).astype(int)
    sudoku = Sudoku(grid)
    for line in range(9):
        if sudoku.is_valid(line, 0):
            print('Pas encore !')
            return
    sudoku.grid[0, :] = np.zeros(9)
    sudoku.grid[:, 0] = np.zeros(9)
    sudoku.grid[0:3, 0:3] = np.zeros((3, 3))
    if not sudoku.is_valid(0, 0):
        print('Pas encore !')
        return
    sudoku.grid[3:6, 3:6] = np.arange(1, 10).reshape((3, 3))
    sudoku.grid[5, :3] = np.zeros(3)
    sudoku.grid[5, 6:] = np.zeros(3)
    sudoku.grid[:3, 5] = np.zeros(3)
    sudoku.grid[6:, 5] = np.zeros(3)
    if not sudoku.is_valid(5, 5):
        print('Pas encore !')
        return
    sudoku.grid[2, :] = [3, 0, 0, 0, 0, 0, 0, 0, 3]
    if sudoku.is_valid(2, 7):
        print('Pas encore !')
        return
    sudoku.grid[6:9, 6:9] = np.array([3, 0, 0, 0, 0, 0, 0, 0, 3]).reshape((3, 3))
    if sudoku.is_valid(6, 7):
        print('Pas encore !')
        return
    print('Exercice 5 réussi')


def test_exo_6(Sudoku):
    xs = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]
    ys = [0, 1, 4, 3, 4, 5, 1, 2, 7, 0, 4, 8, 3, 5, 8, 0, 4, 8, 1, 6, 7, 4, 5, 8, 4, 7, 8]
    vs = [5, 3, 7, 1, 9, 5, 9, 8, 6, 8, 6, 3, 8, 3, 1, 7, 2, 6, 6, 2, 8, 1, 9, 5, 8, 7, 9]
    grid = np.zeros((9, 9)).astype(int)
    for x, y, v in zip(xs, ys, vs):
        grid[x, y] = v
    sudoku = Sudoku(grid)
    sudoku.solve()
    solutions = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [2, 7, 6, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 2, 5, 7, 6, 1, 4, 9, 3],
        [6, 4, 9, 8, 5, 3, 7, 2, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [4, 8, 7, 2, 1, 9, 6, 3, 5],
        [3, 5, 2, 4, 8, 6, 1, 7, 9],
    ]
    try:
        assert np.all(sudoku.grid == np.array(solutions))
        print('Exercice 6 réussi.')
    except Exception:
        print('Pas encore !')
