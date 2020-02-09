def dichotomie_iter(l, n):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (end + start) // 2
        if l[mid] == n:
            return True
        elif l[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return False

def dichotomie_rec(l, n):
    if l == []:
        return False
    mid = len(l) // 2
    if l[mid] == n:
        return True
    elif l[mid] > n:
        return dichotomie_rec(l[:mid], n)
    else:
        return dichotomie_rec(l[mid + 1:], n)
    return False

# Version mieux car elle évite de copier la liste plusieurs fois
def dichotomie_rec_v2(l, n):
    return dichotomie_rec_v2_aux(l, n, 0, len(l) - 1)

def dichotomie_rec_v2_aux(l, n, start, end):
    if start > end:
        return False
    
    mid = (end + start) // 2
    if l[mid] == n:
        return True
    elif l[mid] > n:
        return dichotomie_rec_v2_aux(l, n, start, mid - 1)
    else:
        return dichotomie_rec_v2_aux(l, n, mid + 1, end)