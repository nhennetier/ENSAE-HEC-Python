def is_concatenation(s):
    if len(s) % 2:
        return False
    middle = len(s) // 2
    for i in range(middle):
        if s[i] != s[middle + i]:
            return False
    return True
