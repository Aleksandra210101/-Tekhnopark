"""
Разработала: Крылова Александра
Проект: Нахождение НОД двух чисел
"""


def nod(a_num=0,b_num=1):
    """Нахождение НОД двух чисел"""
    while b_num:
        a_num, b_num = b_num, a_num % b_num
    return a_num


print(nod())