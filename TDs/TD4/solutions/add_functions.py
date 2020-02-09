def add_itératif(a, b):
    '''Retourne la somme de a et b.'''
    if b > a:
        a, b = b, a
    while b > 0:
        a = plus_one(a)
        b = minus_one(b)
    return a
    
def add_recursif(a, b):
    '''Retourne la somme de a et b.'''
    if b == 0:
        return a
    elif b > a:
        add_recursif(b, a)
    return add_recursif(plus_one(a), minus_one(b))