def print_triple_sequence(first_term):
    current_term = first_term
    for _ in range(12):
        print(current_term)
        current_term *= 3


def print_triple_sequence_user():
    first_term = int(input('Please, enter the first term: '))
    print_triple_sequence(first_term)
