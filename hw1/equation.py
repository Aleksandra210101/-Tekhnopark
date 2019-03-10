"""
Разработала: Крылова Александра
Проект: решение квадратичного уравнения
"""

import math

A = float(input("a = "))
B = float(input("b = "))
C = float(input("c = "))
DISCR = B ** 2 - 4 * A * C
if DISCR > 0:
    X1 = (-B + math.sqrt(DISCR)) / (2 * A)
    X2 = (-B - math.sqrt(DISCR)) / (2 * A)
    print('x1 = %.2f, x2 = %.2f' % (X1, X2))
elif DISCR == 0:
    X = -B / (2 * A)
    print("x = %.2f" % X)
else:
    print("Корней нет")
