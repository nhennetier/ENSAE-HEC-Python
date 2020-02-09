def fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci(n-1) + fibonnaci(n-2)


def fibonnaci_opti(n):
    memory = {0: 0, 1: 1}
    return fibonnaci_aux(n, memory)

def fibonnaci_aux(n, memory):
    if n not in memory:
        memory[n] = fibonnaci_aux(n-1, memory) + fibonnaci_aux(n-2, memory)
    return memory[n]