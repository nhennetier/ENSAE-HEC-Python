import random


def check_input(user_in):
    # Check if the input is 5 integers
    if len(user_in) != 5:
        return False
    for char in user_in:
        try:
            int(char)
        except Exception:
            return False
    return True


def n_placed_and_n_wrongly_placed(answer, guess):
    # Compute the number of good placed guesses and the number of wrongly placed good guesses
    used = [False] * 5
    n_placed = 0
    n_good = 0
    for i, elem in enumerate(guess):
        if answer[i] == elem:
            if used[i]:
                n_good -= 1
                n_placed += 1
            else:
                used[i] = True
                n_placed += 1
        else:
            for j in range(5):
                if not used[j] and answer[j] == elem:
                    used[j] = True
                    n_good += 1
                    break
    return n_placed, n_good


def mastermind():
    # Game function
    answer = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    n_try = 0
    guess = ''
    while guess != answer:
        n_try += 1
        guess = input('Quelle est votre proposition ?\n')
        while not check_input(guess):
            guess = input('Entrez un nombre à 5 chiffres: ')
        n_placed, n_good = n_placed_and_n_wrongly_placed(answer, guess)
        print(f'Vous avez {n_placed} chiffres bien placés '
              f'et {n_good} chiffres bons mais mal placés.')
    print(f'Gagné en {n_try} essais.')
