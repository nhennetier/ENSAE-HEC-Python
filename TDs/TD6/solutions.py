import numpy as np
import time
from tqdm import tqdm
from matplotlib import pyplot as plt


def fill_randomly(arr, n, elem):
    pos = np.where(arr == 0)
    pos = list(zip(pos[0], pos[1]))
    if len(pos) < n:
        raise ValueError('Not enough place')
    np.random.shuffle(pos)
    for x, y in pos[:n]:
        arr[x, y] = elem


class City:

    def __init__(self, grid_size):
        self.grid = np.zeros((grid_size, grid_size))
        self.height = grid_size
        self.n_cases = grid_size ** 2
        self.tolerance = 0.55

    def populate(self, percentages):
        if sum(percentages) > 1:
            raise ValueError('Too many people !')
        for i in range(len(percentages)):
            n_to_fill = int(self.n_cases * percentages[i])
            fill_randomly(self.grid, n_to_fill, i + 1)

    def __repr__(self):
        return str('\n'.join([str(l) for l in self.grid]))

    def want_to_move(self, x, y):
        if self.grid[x, y] == 0:
            return False
        n_neighbors = -1
        n_same_neighbors = -1
        for i in [-1, 0, 1]:
            if x + i >= 0 and x + i < len(self.grid):
                for j in [-1, 0, 1]:
                    if y + j >= 0 and y + j < len(self.grid):
                        n_neighbors += (self.grid[x + i, y + j] != 0)
                        n_same_neighbors += (self.grid[x + i, y + j] == self.grid[x, y])
        return (n_neighbors != 0) and (n_same_neighbors / n_neighbors < self.tolerance)

    def next_move(self):
        possible_pos = [(x, y) for x in range(self.height) for y in range(self.height)]
        move_from = None
        move_to = None
        np.random.shuffle(possible_pos)
        for x, y in possible_pos:
            if move_from is None and self.want_to_move(x, y):
                move_from = (x, y)
            elif move_to is None and self.grid[x, y] == 0:
                move_to = (x, y)
            if move_from is not None and move_to is not None:
                break
        return (move_from, move_to)

    def move(self, move_from, move_to):
        if self.grid[move_to] != 0:
            raise ValueError('Not a empty spot')
        self.grid[move_to] = self.grid[move_from]
        self.grid[move_from] = 0

    def is_complete(self):
        for x in range(self.height):
            for y in range(self.height):
                if self.want_to_move(x, y):
                    return False
        return True

    def percentage_complete(self):
        n = 0
        for x in range(self.height):
            for y in range(self.height):
                if self.want_to_move(x, y):
                    n += 1
        return n / self.n_cases

    def run_n_iterations(self, iter_max=100, verbose=1):
        history = [self.compute_segregation()]
        if self.is_complete():
            return True, history
        for n_iter in range(iter_max):
            if verbose:
                print(f'Iteration {n_iter + 1}')
            t0 = time.time()
            move_from, move_to = self.next_move()
            self.move(move_from, move_to)
            history.append(self.compute_segregation())
            if self.is_complete():
                return True, history
            t1 = time.time()
            if verbose:
                print(f'Done in {t1-t0} secondes.')
        return False, history

    def run_simulation(self):
        history = [self.compute_segregation()]
        is_complete = False
        self.show()
        while not is_complete:
            is_complete, current_history = self.run_n_iterations(iter_max=20, verbose=0)
            history += current_history[1:]
            print(f'{100 - self.percentage_complete() * 100} % Done')
            self.show()
        print('Done')
        self.show()
        plt.plot(history)
        plt.title('Evolution of number of segregated people')
        plt.show()

    def is_segregated(self, x, y):
        inhabitant = self.grid[x, y]
        for i in [-1, 0, 1]:
            if x + i >= 0 and x + i < self.height:
                for j in [-1, 0, 1]:
                    if y + j >= 0 and y + j < self.height and (i != 0 or j != 0):
                        if self.grid[x + i, y + j] != inhabitant and self.grid[x + i, y + j] != 0:
                            return False
        return True

    def compute_segregation(self):
        n_inhabitants = 0
        n_segregated = 0
        for i in range(self.height):
            for j in range(self.height):
                if self.grid[i, j] != 0:
                    n_inhabitants += 1
                    n_segregated += self.is_segregated(i, j)
        return n_segregated / n_inhabitants

    def show(self):
        fig, ax = plt.subplots()
        im = ax.imshow(self.grid)
        cbar = ax.figure.colorbar(im, ax=ax)
        cbar.ax.set_ylabel('inhabitant', rotation=-90, va="bottom")
        plt.show()


def create_city(height, percent_pop=[0.4, 0.4]):
    city = City(height)
    city.populate(percent_pop)
    return city


def performance_test():
    sizes = [5, 10, 50, 100, 200, 300, 400, 500]
    times = []
    for size in tqdm(sizes):
        city = create_city(size)
        t0 = time.time()
        city.run_n_iterations(iter_max=10, verbose=0)
        t1 = time.time()
        times.append(t1 - t0)
    plt.plot(sizes, times)
    plt.title('Performance of the algorithm')
    plt.show()


if __name__ == '__main__':
    city = create_city(30, [0.45, 0.45])
    city.run_simulation()
