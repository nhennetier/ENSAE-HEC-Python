def lowest_cost(l):
    if len(l) == 2:
        return sum(l)
    if len(l) <= 1:
        return 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            current_cost = l[i] + l[j] + lowest_cost([l[i] + l[j]] + l[:i] + l[i+1:j] + l[j+1:])
            if i == 0 and j == 1:
                min_cost = current_cost
            else:
                min_cost = min(min_cost, current_cost)
    return min_cost