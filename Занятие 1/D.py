a = int(input())
b = int(input())
c = int(input())


def solve(a, b, c):
    """sqrt(ax+b) = c"""
    # значение корня не может быть меньше нуля
    if c < 0:
        return "NO SOLUTION"
    # нельзя извлечь корень из отрицательного числа
    if a == 0 and b < 0:
        return "NO SOLUTION"
    # sqrt(b) != b
    if a == 0 and c ** 2 != b:
        return "NO SOLUTION"
    if a == 0:
        return "MANY SOLUTIONS"
    # решение ищем в целых числах
    if (c ** 2 - b) % a != 0:
        return "NO SOLUTION"
    return (c ** 2 - b) // a


print(solve(a, b, c))
