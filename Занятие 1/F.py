a1, b1, a2, b2 = map(int, input().split())


def get_min_size(a1, b1, a2, b2):
    # Создаем словарь, который в качестве ключа содержит площадь,
    # а в качестве значение стороны стола, при котором достигается эта площадь
    square_size_dict = {
        (a1 + a2) * max(b1, b2): (a1 + a2, max(b1, b2)),
        (a1 + b2) * max(b1, a2): (a1 + b2, max(b1, a2)),
        (b1 + a2) * max(a1, b2): (b1 + a2, max(a1, b2)),
        (b1 + b2) * max(a1, a2): (b1 + b2, max(a1, a2))
    }
    # выводим стороны с минимальной площадью
    return square_size_dict[min(square_size_dict)]


a, b = get_min_size(a1, b1, a2, b2)
print(a, b)
