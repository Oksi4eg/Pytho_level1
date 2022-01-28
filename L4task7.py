# from functools import reduce

user_num = int(input('Введите число: '))


# def fact(num):
#     my_list = [el for el in range(1, num + 1)]
#     my_func = lambda a, b: a * b
#     result = reduce(my_func, my_list)
#     return result
#
#
# print(fact(user_num))

def fact(end):  # перечитала задание =))
    current = 1
    for i in range(1, end + 1):
        yield current
        current += 1


result = 1
for el in fact(user_num):
    result *= el

print(result)
