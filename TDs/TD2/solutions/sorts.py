def sort1(l):
    elem_max = max(l)
    answer = []
    for _ in range(len(l)):
        current_min = elem_max
        for i, elem in enumerate(l):
            if elem < current_min:
                current_min = elem
                position_of_min = i
        l[position_of_min] = elem_max
        answer.append(current_min)
    return answer


def sort2(l):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                is_sorted = False
                tmp = l[i]
                l[i] = l[i + 1]
                l[i + 1] = tmp
    return l
