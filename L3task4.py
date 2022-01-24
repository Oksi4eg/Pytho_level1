a = int(input("Введите число 1: "))
b = int(input("Введите отр: число 2: "))

my_func = lambda num_1, num_2: num_1 ** num_2
print(my_func(a, b))


def pow_nums(num_1, num_2):
    if num_2 > 0:
        result = 1
        for i in range(num_2):
            result *= num_1
    elif num_2 < 0:
        result = 1 / num_1
        for i in range(-num_2 - 1):
            result /= num_1
    else:
        result = 1
    return result


print(pow_nums(a, b))
