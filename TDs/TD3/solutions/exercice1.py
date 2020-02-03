list_letters = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'a', 'b', 'a', 'z']
counter = {}

for letter in list_letters:
    counter[letter] = counter.get(letter, 0) + 1

print(counter)