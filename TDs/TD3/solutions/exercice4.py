def dichotomie(l, n):
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