my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('L5task4_1.txt', 'r') as file:
    my_list = file.readlines()
for i in my_list:
    blank = i.find(" ", 1)
    i_name = i[:blank]
    new_name = my_dict[i_name]
    with open('L5task4_2.txt', 'a') as file:
        file.write(f'{new_name}{i[blank:]}')
