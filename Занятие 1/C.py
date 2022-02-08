number_to_add = input()
numbers = [input() for _ in range(3)]


def get_code_num(number):
    # определим отдельно код и номер телефонного номера
    num = ""
    # начинаем проверять номер с конца
    i = len(number) - 1
    num_count = 0
    # номер содержит 7 цифр, поэтому когда мы подсчитаем 7 символов, то номер найден
    while num_count != 7:
        # пропускаем символ '-'
        if number[i] != '-':
            num += number[i]
            num_count += 1
        i -= 1
    num = num[::-1]

    code = ""
    # i указывает на элемент, стоящий перед номером
    # код пропущен
    if i == -1 or i == 0 or i == 1:
        code = "495"
    else:
        # код содержит 3 цифры
        code_count = 0
        while code_count != 3:
            if number[i] != ')' and number[i] != '-':
                code += number[i]
                code_count += 1
            i -= 1
        code = code[::-1]
    return code, num


def is_equal(number_to_add, number):
    code_to_add, num_to_add = get_code_num(number_to_add)
    code, num = get_code_num(number)
    if (code_to_add == code) and (num_to_add == num):
        return "YES"
    return "NO"


for i in range(3):
    print(is_equal(number_to_add, numbers[i]))
