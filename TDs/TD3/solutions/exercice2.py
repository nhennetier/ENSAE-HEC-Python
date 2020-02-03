def letter_position(names, letter, pos):
    result = []
    for name in names:
        if len(name) > pos and name[pos] == letter:
            result.append(name)
    return result


dic = {}
for name in names:
    for i, letter in enumerate(name):
        dic[(letter, i)] = dic.get((letter, i), []) + [name]