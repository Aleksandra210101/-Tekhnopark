"""
Разработала: Крылова Александра
Проект: Нахождение НОД двух чисел
"""


def nod():
    """Нахождение НОД двух чисел"""
    a_num = int(input('Введите первое число: '))
    b_num = int(input('Введите второе число: '))
    while b_num:
        a_num, b_num = b_num, a_num % b_num
    return a_num


print(nod())