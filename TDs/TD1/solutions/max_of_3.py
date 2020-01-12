n1 = float(input('Entrez trois nombres: '))
n2 = float(input())
n3 = float(input())

if n1 > n2 and n1 > n3:
    print(f'The maximum is {n1}')
elif n2 > n3:
    print(f'The maximum is {n2}')
else:
    print(f'The maximum is {n3}')

# Or shorter

n_max = max(n1, n2, n3)
print(f'The maximum is {n_max}')