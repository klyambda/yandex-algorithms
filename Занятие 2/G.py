sequence = list(map(int, input().split()))


def twonums_with_maxmult(seq):
    # одновременно находим по паре самых больших и маленьких чисел,
    # так как произ-ние двух отрицательных чисел положительно и м.б. максимальным
    min_num1, min_num2 = min(seq[0], seq[1]), max(seq[0], seq[1])
    max_num1, max_num2 = min_num2, min_num1

    for i in range(2, len(seq)):
        if seq[i] < min_num2:
            if seq[i] < min_num1:
                min_num2 = min_num1
                min_num1 = seq[i]
            else:
                min_num2 = seq[i]

        if seq[i] > max_num2:
            if seq[i] > max_num1:
                max_num2 = max_num1
                max_num1 = seq[i]
            else:
                max_num2 = seq[i]

    if max_num1 * max_num2 > min_num1 * min_num2:
        return max_num2, max_num1
    else:
        return min_num1, min_num2


num1, num2 = twonums_with_maxmult(sequence)
print(num1, num2)
