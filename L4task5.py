from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
my_func = lambda a, b: a * b
result = reduce(my_func, my_list)
print(result)
