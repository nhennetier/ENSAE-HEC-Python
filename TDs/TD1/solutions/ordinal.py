x = int(input('Please, enter a number: '))

if (x - x % 10) // 10 % 10 == 1:
    print(f'Its ordinal is {x}th.')
elif x % 10 == 1:
    print(f'Its ordinal is {x}st.')
elif x % 10 == 2:
    print(f'Its ordinal is {x}nd.')
elif x % 10 == 3:
    print(f'Its ordinal is {x}rd.')
else:
    print(f'Its ordinal is {x}th.')
