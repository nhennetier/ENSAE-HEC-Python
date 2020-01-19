def min_max_mean(l):
    current_min = l[0]
    current_max = l[0]
    current_mean = 0
    for value in l:
        current_min = min(current_min, value)
        current_max = max(current_max, value)
        current_mean += value
    return current_min, current_max, current_mean / len(l)
