with open('L5task5.txt', 'w') as file:
    file.write('5 2 10 20 15 6 20 50')

with open('L5task5.txt', 'r') as file:
    my_list = file.read().split()

my_list = [int(el) for el in my_list if el.isdigit()]
print(sum(my_list))
