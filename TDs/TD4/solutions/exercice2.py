from random import randint

def random_multiple_iter():
    nb_print = 0
    while nb_print < 10:
        x = randint(0, 100)
        if x%5 == 0 or x%6 == 0:
            nb_print += 1
            print(x)


def random_multiple_rec(n=0):
    if n==10:
        return
    x = 3
    while x%5 and x%6:
        x = randint(0, 100)
    print(x)
    random_aux(n+1)