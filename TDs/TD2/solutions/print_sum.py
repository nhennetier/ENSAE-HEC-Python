def print_result_sum(n):
    result = 0
    for i in range(n + 1):
        result += i
    print(f'La somme des entiers de 1 à {n} est {result}!')


def print_sum(n):
    result = 0
    sum_as_string = ""
    for i in range(1, n + 1):
        if i != 1:
            sum_as_string += ' + '
        sum_as_string += str(i)
        result += 1
    print(f'La somme des entiers de 1 à {n} est {sum_as_string} = {result}!')
print_sum(10)


# Ou en trichant
def print_sum(n):
    l_integers = list(range(1, n + 1))
    print(f"La somme {' + '.join([str(i) for i in l_integers])} vaut {sum(l_integers)}!")
print_sum(10)
