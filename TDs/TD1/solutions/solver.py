print("Solveur d'équation ax + b = 0")
a = int(input('a = '))
b = int(input('b = '))

if a == 0:
    if b == 0:
        print('Tout x est solution.')
    else:
        print("Cette équation n'a pas de solution")
else:
    sol = -b / a
    print(f'La solution de cette équation est {sol}')