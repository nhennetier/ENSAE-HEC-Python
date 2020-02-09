def mul_iteratif(a, b):
    '''Retourne la multiplication de a par b'''
    result = 0
    while b != 0:
        result = add_iteratif(result, a)
        b = minus_one(b)
    return result

def mul_recursif(a, b):
    '''Retourne la multiplication de a par b'''
    if b == 0:
        return 0
    elif b == 1:
        return a

    if b > a:
        return mul_recursif(b, a)
    return add_recursif(a, mul_recursif(a, minus_one(b)))