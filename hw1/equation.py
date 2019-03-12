"""
Разработала: Крылова Александра
Проект: решение квадратичного уравнения axx+bx+c
"""

import math

A = float(input("a = "))
B = float(input("b = "))
C = float(input("c = "))
DISCR = B ** 2 - 4 * A * C
if DISCR > 0.0:
    if A != 0.0:
        X1 = (-B + math.sqrt(DISCR)) / (2 * A)
        X2 = (-B - math.sqrt(DISCR)) / (2 * A)
        print('x1 = %.2f, x2 = %.2f' % (X1, X2))
    elif A == 0 and B != 0 and C != 0:
        X = -C / B
        print(X)
    elif B != 0 and A == 0 and C == 0:
        print("x = ", 0)
    else:
        print("Нет корней")
elif DISCR == 0.0:
    if A == 0.0 and B == 0.0:
        print("Нет корней")
    else:
        X = -B / (2 * A)
        print("x = %.2f" % X)
else:
    print("Корней нет")

