from matplotlib import pyplot as plt

def plot_points(points):
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    plt.scatter(xs, ys)
    plt.show()


from random import randint


def get_n_points_in_square(n):
    points = [
        (randint(-100, 100) / 100, randint(-100, 100) / 100)
        for _ in range(n)
    ]
    plot_points(points)
    

def get_n_points_in_circle(n):
    points = []
    while len(points) < n:
        x = randint(-100, 100) / 100
        y = randint(-100, 100) / 100
        if x ** 2 + y ** 2 <= 1:
            points.append((x, y))
    plot_points(points)