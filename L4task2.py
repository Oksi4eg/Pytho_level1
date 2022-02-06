first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [el for i, el in enumerate(first_list) if el > first_list[max(i - 1, 0)]]
print(my_list)
