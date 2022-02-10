n = int(input())
array = list(map(int, input().split()))
x = int(input())


def nearest_number(array, x):
    min_delta = abs(x - array[0])
    ans = array[0]

    for i in range(1, len(array)):
        delta = abs(x - array[i])
        if delta < min_delta:
            min_delta = delta
            ans = array[i]

    return ans


print(nearest_number(array, x))
