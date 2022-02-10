array = list(map(int, input().split()))


def greater_than_neighbors(array):
    count = 0

    if len(array) < 2:
        return 0

    for i in range(len(array) - 2):
        if (array[i + 1] > array[i]) and (array[i + 1] > array[i + 2]):
            count += 1

    return count


print(greater_than_neighbors(array))
