sequence = list(map(int, input().split()))


def nums3_with_maxmult(seq):
    """Найдем три максимальных и два минимальных числа. Наибольшее произведение определим из произведения
    трех максимальных чисел и произведения двух минимальных и одного максимального числа.
    max1 > max2 > max3. min1 < min2
    """
    max1 = max(seq[0], seq[1], seq[2])
    max3 = min(seq[0], seq[1], seq[2])
    max2 = seq[0] + seq[1] + seq[2] - max1 - max3
    min1 = max3
    min2 = max2

    for curr in seq[3:]:
        if curr > max3:
            if curr > max2:
                if curr > max1:
                    max3 = max2
                    max2 = max1
                    max1 = curr
                else:
                    max3 = max2
                    max2 = curr
            else:
                max3 = curr
        elif curr < min2:
            if curr < min1:
                min2 = min1
                min1 = curr
            else:
                min2 = curr

    mult1 = max3 * max2 * max1
    mult2 = min1 * min2 * max1
    if mult1 > mult2:
        return max3, max2, max1
    else:
        return min1, min2, max1


print(nums3_with_maxmult(sequence))
