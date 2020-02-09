# Pour résoudre le problème des tours, il faut déplacer tous les disques de gauche à droite.
# Pour cela, il faut déplacer tous les disques sauf 1 au centre, déplacer le dernier disque sur la droite,
# puis déplacer les disques du centre sur la droite.

# Pour modéliser ce jeu, vous pouvez utiliser une liste de liste d'entiers. Au départ, on a:
n_discs = 7
towers = [list(range(n_discs)), [], []]
# Le but est que towers deviennent
[[], [], list(range(n_discs))]

# L'indice 1 est vrai à chaque étape: pour déplacer n disques de pique 0 au pique 2, il faut déplacer
# n-1 disques du pique 0 au pique 1, 1 disque du pique 0 au pique 2, puis n-1 disques du pique 1 au pique 2.
# Pour déplacer n-1 disques du pique 0 au pique 1, il faut déplacer n-2 disques du pique 0 au pique 2,
# 1 disque du pique 0 au pique 1, puis n-2 disques du pique 2 au pique 1.

# Voici la structure du programme
n_discs = 5
towers = [list(range(n_discs)), [], []]

def move_one_disc(start, end, towers):
    '''Move one disc from start peg to end peg'''
    pass


def move_discs(start, end, tmp, n_to_move, towers):
    '''Move n_to_move discs from the start peg to the end peg. tmp is the indice of the third peg.'''
    pass


def solve(towers, n_discs):
    pass


solve(towers, n_discs)