array = list(map(int, input().split()))


def is_array_increasing(array):
    for i in range(len(array) - 1):
        # если следующий элемент не больше предыдущего
        if array[i] >= array[i + 1]:
            return "NO"
    return "YES"


print(is_array_increasing(array))
