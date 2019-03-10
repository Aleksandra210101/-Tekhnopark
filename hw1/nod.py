def nod():
    """Нахождение НОД двух чисел"""
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    NOD = a + b
    print(NOD)


nod()
