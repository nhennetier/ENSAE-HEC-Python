print('Quelle heure est-il ?')
heures = int(input("heures: "))
minutes = int(input("minutes: "))
secondes = int(input("secondes: "))

if secondes != 59:
    secondes += 1
else:
    secondes = 0
    if minutes != 59:
        minutes += 1
    else:
        minutes = 0
        if heures != 23:
            heures += 1
        else:
            heures = 0

print(f'Dans une seconde, il sera {heures} heures {minutes} minutes et {secondes} secondes.')

print('Quelle heure est-il ?')
heures = int(input("heures: "))
minutes = int(input("minutes: "))
secondes = int(input("secondes: "))

ajout = int(input('Combien de secondes voulez vous ajouter ? '))

secondes += ajout

if secondes > 59:
    secondes -= 60
    minutes += 1
    if minutes == 60:
        minutes = 0
        heures += 1
        if heures == 24:
            heures = 0

print(f'Dans une seconde, il sera {heures} heures {minutes} minutes et {secondes} secondes.')