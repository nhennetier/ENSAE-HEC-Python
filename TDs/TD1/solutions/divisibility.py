x = 15

if int(x / 4) == x / 4:
    print("C'est un nombre pair multiple de 4")
elif int(x / 2) == x / 2:
    print("C'est un nombre pair non multiple de 4")
else:
    print("C'est un nombre impair")

# Or

if x % 4 == 0:
    print("C'est un nombre pair multiple de 4")
elif x % 2 == 0:
    print("C'est un nombre pair non multiple de 4")
else:
    print("C'est un nombre impair")