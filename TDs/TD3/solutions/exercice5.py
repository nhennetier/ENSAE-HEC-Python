def quicksort(l):
    if len(l) < 2:
        return l
    smaller, bigger = [], []
    pivot = l[0]
    for elem in l[1:]:
        if elem < pivot:
            smaller.append(elem)
        else:
            bigger.append(elem)
    return quicksort(smaller) + [pivot] + quicksort(bigger)


def merge(l1, l2):
    result = []
    i1, i2 = 0, 0
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            result.append(l1[i1])
            i1 += 1
        else:
            result.append(l2[i2])
            i2 += 1
    result += l1[i1:] + l2[i2:]
    return result

def merge_sort(l):
    if len(l) < 2:
        return l
    mid = len(l) // 2
    return merge(merge_sort(l[:mid]), merge_sort(l[mid:]))