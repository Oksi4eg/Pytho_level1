a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Введите число 3: "))


def max_sum(num_1, num_2, num_3):
    tmp_list = [num_1, num_2, num_3]
    result = sum(tmp_list) - min(tmp_list)
    return result


print(max_sum(a, b, c))
