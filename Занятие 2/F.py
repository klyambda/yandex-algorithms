sequence_len = int(input())
sequence = list(map(int, input().split()))


def nums_to_add(seq):
    def is_symmetrical(subseq):
        """Проверка на симметричность подпоследовательности"""
        for i in range(len(subseq) // 2):
            if subseq[i] != subseq[len(subseq) - 1 - i]:
                return False
        return True

    stack_to_add = []
    for i in range(len(seq)):
        if is_symmetrical(seq[i:]):
            # если подпоследовательность симметрична, то
            # добавляем в конец последовательности числа, не вошедшие в симметричную подпоследовательность
            for j in range(i - 1, -1, -1):
                stack_to_add.append(seq[j])
            return stack_to_add

    return stack_to_add


stack_to_add = nums_to_add(sequence)
print(len(stack_to_add))
if len(stack_to_add):
    for el in stack_to_add:
        print(el, end=' ')
