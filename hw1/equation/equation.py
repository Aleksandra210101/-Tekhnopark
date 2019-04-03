"""
Разработала: Крылова Александра
Проект: решение квадратичного уравнения axx+bx+c
"""
import math

def num_get_roots(A, B, C):
    root = get_roots(A, B, C)
    if type(root) == tuple:
        return 2
    elif root == None:
        return 0
    else:
        return 1

def get_roots(A, B, C):
    if A != 0 :
        return  solve_quadratic(A, B, C)
    else:
        return solve_linear(B, C)


def solve_quadratic(A, B, C):
    """Quadratic equation solution"""
    DISCR = B ** 2 - 4 * A * C
    if DISCR > 0:
        X1 = (-B + math.sqrt(DISCR)) / (2 * A)
        X2 = (-B - math.sqrt(DISCR)) / (2 * A)
        return X1, X2
    elif DISCR == 0:
        X = -B / (2 * A)
        return X


def solve_linear(B, C):
    """Linear equation solution"""
    if (B != 0) and (C != 0):
        X = -C / B
        return X
    elif (B != 0) and (C == 0):
        return 0
    else:
        return None
