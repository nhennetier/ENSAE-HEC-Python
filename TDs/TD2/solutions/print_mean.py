def print_mean():
    grades = []
    grade = float(input('Please enter next grade: '))
    while grade >= 0:
        grades.append(grade)
        print(f'La moyenne est {sum(grades) / len(grades)}')
        grade = float(input('Please enter next grade: '))
