n_discs = 5
towers = [list(range(n_discs)), [], []]

def move_one_disc(start, end, towers):
    '''Move one disc from start peg to end peg'''
    print(f'Called with towers {towers}')
    print(f'Will move 1 discs from {start} to {end}')
    towers[end].append(towers[start][-1])
    towers[start] = towers[start][:-1]
    return towers

def move_discs(start, end, tmp, n_to_move, towers):
    '''Move n_to_move discs from the start peg to the end peg. tmp is the indice of the third peg.'''
    if n_to_move == 1:
        towers = move_one_disc(start, end, towers)
    else:
        towers = move_discs(start, tmp, end, n_to_move - 1, towers)
        towers = move_one_disc(start, end, towers)
        towers = move_discs(tmp, end, start, n_to_move - 1, towers)
    return towers

def solve(towers, n_discs):
    move_discs(0, 2, 1, n_discs, towers)
    print('Solved')
    print(towers)
    
solve(towers, n_discs)