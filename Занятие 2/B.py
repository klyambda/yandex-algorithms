def sequence_type():
    first = int(input())

    is_constant = True
    is_ascending = True
    is_weakly_ascending = True
    is_descending = True
    is_weakly_descending = True
    is_random = True

    while True:
        second = int(input())
        if second == -2000000000:
            break

        if first != second:
            is_constant = False
        if first >= second:
            is_ascending = False
        if first > second:
            is_weakly_ascending = False
        if first <= second:
            is_descending = False
        if first < second:
            is_weakly_descending = False

        first = second

    if is_constant:
        return "CONSTANT"
    elif is_ascending:
        return "ASCENDING"
    elif is_weakly_ascending:
        return "WEAKLY ASCENDING"
    elif is_descending:
        return "DESCENDING"
    elif is_weakly_descending:
        return "WEAKLY DESCENDING"
    else:
        return "RANDOM"


print(sequence_type())
