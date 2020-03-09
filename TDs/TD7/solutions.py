class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def is_valid_row(self, i):
        seen = set()
        for value in self.grid[i, :]:
            if value != 0 and value in seen:
                return False
            seen.add(value)
        return True

    def is_valid_column(self, j):
        seen = set()
        for value in self.grid[:, j]:
            if value != 0 and value in seen:
                return False
            seen.add(value)
        return True

    def is_valid_square(self, i, j):
        i_min = i // 3 * 3
        i_max = i_min + 3
        j_min = j // 3 * 3
        j_max = j_min + 3
        seen = set()
        for value in self.grid[i_min:i_max, j_min:j_max].reshape(-1):
            if value != 0 and value in seen:
                return False
            seen.add(value)
        return True

    def is_valid(self, i, j):
        return self.is_valid_row(i) and self.is_valid_column(j) and self.is_valid_square(i, j)

    def solve(self, i=0, j=0):
        if i == 9 and j == 0:
            return True

        next_j = (j + 1) % 9
        next_i = i + int(next_j == 0)

        if self.grid[i, j] != 0:
            return self.solve(next_i, next_j)

        for value in range(1, 10):
            self.grid[i, j] = value
            if self.is_valid(i, j) and self.solve(next_i, next_j):
                return True
        self.grid[i, j] = 0
        return False

    def print(self):
        for j, line in enumerate(self.grid):
            print(
                "|".join(
                    [
                        " ".join([str(i) if i != 0 else " " for i in line[i * 3 : (i + 1) * 3]])
                        for i in range(3)
                    ]
                )
            )
            if j % 3 == 2 and j != 8:
                print("-" * 18)

        print()


if __name__ == "__main__":
    import numpy as np
    import time

    xs = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]
    ys = [0, 1, 4, 3, 4, 5, 1, 2, 7, 0, 4, 8, 3, 5, 8, 0, 4, 8, 1, 6, 7, 4, 5, 8, 4, 7, 8]
    vs = [5, 3, 7, 1, 9, 5, 9, 8, 6, 8, 6, 3, 8, 3, 1, 7, 2, 6, 6, 2, 8, 1, 9, 5, 8, 7, 9]
    grid = np.zeros((9, 9)).astype(int)
    for x, y, v in zip(xs, ys, vs):
        grid[x, y] = v
    sudoku = Sudoku(grid)
    sudoku.print()
    t0 = time.time()
    x = sudoku.solve()
    print(time.time() - t0)
    sudoku.print()
