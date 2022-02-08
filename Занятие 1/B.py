a = int(input())
b = int(input())
c = int(input())


def solve(a, b, c):
    """Можно построить треугольник с заданными сторонами,
        если сумма любых двух сторон превосходит третью"""
    if (a + b > c) and (a + c > b) and (b + c > a):
        return "YES"
    else:
        return "NP"


solve(a, b, c)
