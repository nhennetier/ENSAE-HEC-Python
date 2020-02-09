def factoriel(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return factoriel(n-1) * factoriel(n-2)


def factoriel_opti(n):
    memory = {0: 1, 1: 1}
    return factoriel_aux(n, memory)

def factoriel_aux(n, memory):
    if n not in memory:
        memory[n] = factoriel_aux(n-1, memory) * factoriel_aux(n-2, memory)
    return memory[n]