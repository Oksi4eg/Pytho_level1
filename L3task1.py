a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))


def div_nums(num_1, num_2):
    if num_2 == 0:
        print("Делить на ноль нельзя, попробуйте еще раз!")
    else:
        return num_1 / num_2


print(div_nums(a, b))
