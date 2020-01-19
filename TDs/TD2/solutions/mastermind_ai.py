def ask_answer(guess):
    print(f'Je pense à {guess}.')
    n_good = int(input('Combien sont bien placés ? '))
    n_placed = int(input('Combien sont mal placés ? '))
    return n_good, n_placed


# Version non optimisée
def mastermind_ai():
    print('Pensez à un nombre')
    n_trash = 0
    while ask_answer(str(n_trash) * 5) != (0, 0):
        n_trash += 1
    good_answer = [n_trash] * 5
    for i in range(10):
        if i == n_trash:
            continue
        for j in range(5):
            guess = [str(n_trash)] * 5
            guess[j] = str(i)
            if ask_answer(''.join(guess))[0]:
                good_answer[j] = str(i)
    print(f"Vous pensez à {''.join(good_answer)}!")


# Mieux mais loin d'être parfait
def mastermind_ai():
    print('Pensez à un nombre')
    n_trash = 0
    while ask_answer(str(n_trash) * 5) != (0, 0):
        n_trash += 1
    good_answer = [n_trash] * 5
    for i in range(10):
        if i == n_trash:
            continue
        to_place = ask_answer(str(i) * 5)[0]
        if to_place == 0:
            continue
        for j in range(5):
            guess = [str(n_trash)] * 5
            guess[j] = str(i)
            if ask_answer(''.join(guess))[0]:
                good_answer[j] = str(i)
                to_place -= 1
                if to_place == 0:
                    break
        if n_trash not in good_answer:
            break
    print(f"Vous pensez à {''.join(good_answer)}!")
