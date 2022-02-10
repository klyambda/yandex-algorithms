n = int(input())
array = list(map(int, input().split()))


def vasily_place(distance_array, n):
    # определяем место одного из победителей
    winner_distance = -1
    winner_index = -1
    for i in range(n):
        if distance_array[i] > winner_distance:
            winner_distance = distance_array[i]
            winner_index = i

    # результат броска Василия
    vasily_result = -1
    for i in range(winner_index + 1, n - 1):
        if (distance_array[i] % 10 == 5) and (distance_array[i + 1] < distance_array[i]) and (
                distance_array[i] > vasily_result):
            vasily_result = distance_array[i]

    # определяем место, которое занял Василий
    if vasily_result == -1:  # не существует участника, который удовлетворяет условиям
        return 0
    else:
        # сортируем массив (nlgn)
        distance_array.sort()
        for i in range(n - 1, -1, -1):
            if distance_array[i] == vasily_result:
                return n - i


print(vasily_place(array, n))
