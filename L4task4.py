list_first = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = [el for el in list_first if list_first.count(el) == 1]
print(my_list)