def create_sudoku_from_list_of_index(xs, ys, values):
    sudoku = [[0 for _ in range(9)] for _ in range(9)]
    for x, y, value in zip(xs, ys, values):
        sudoku[x][y] = value
    return sudoku


def print_sodoku(sudoku):
    for row in sudoku:
        print(' '.join([str(i) for i in row]))


def check_row(sudoku, i):
    memory = set()
    for value in sudoku[i]:
        if value != 0 and value in memory:
            return False
        memory.add(value)
    return True


def check_column(sudoku, j):
    memory = set()
    for value in [row[j] for row in sudoku]:
        if value != 0 and value in memory:
            return False
        memory.add(value)
    return True


def check_square(sudoku, n):
    '''
    Consider the sudoku as 9 squares
     0 | 1 | 2
     3 | 4 | 5
     6 | 7 | 8

    '''
    memory = set()
    first_i = n // 3 * 3
    first_j = n % 3 * 3
    for row in sudoku[first_i: first_i + 3]:
        for value in row[first_j: first_j + 3]:
            if value != 0 and value in memory:
                return False
            memory.add(value)
    return True


def check_new_value(sudoku, i, j):
    return (check_row(sudoku, i)
            and check_column(sudoku, j)
            and check_square(sudoku, (i // 3) * 3 + (j // 3)))


def next_step(i, j):
    if j == 8:
        return i + 1, 0
    return i, j + 1


def solve_sudoku(sudoku, i=0, j=0):
    if i > 8:
        return True

    next_i, next_j = next_step(i, j)
    if sudoku[i][j] != 0:
        return solve_sudoku(sudoku, next_i, next_j)

    for value in range(1, 10):
        sudoku[i][j] = value
        if check_new_value(sudoku, i, j) and solve_sudoku(sudoku, next_i, next_j):
            return True
    sudoku[i][j] = 0
    return False


xs = [0, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8]
ys = [0, 5, 6, 7, 8, 2, 4, 5, 7, 2, 3, 2, 4, 0, 1, 6, 8, 0, 5, 7, 8, 2, 3]
values = [4, 9, 7, 8, 5, 7, 4, 8, 5, 1, 3, 6, 7, 8, 6, 9, 3, 7, 5, 6, 2, 3, 7]

sudoku = create_sudoku_from_list_of_index(xs, ys, values)
print_sodoku(sudoku)
print(solve_sudoku(sudoku))
print_sodoku(sudoku)
