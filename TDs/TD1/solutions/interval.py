user_number = float(input('Please, enter a number: '))
in_interval = user_number >= 0 and user_number < 8
if in_interval:
    print('Gagné !')
else:
    print('Perdu !')

user_number = float(input('Please, enter a number: '))
in_interval = (user_number >= 0 and user_number < 8) or (user_number > 10 and user_number <= 13.5)
if in_interval:
    print('Gagné !')
else:
    print('Perdu !')

user_number = float(input('Please, enter a number: '))
if (user_number >= 0 and user_number < 8) or (user_number > 10 and user_number <= 13.5):
    print('Gagné !')
else:
    print('Perdu !')
