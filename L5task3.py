with open('L5task3.txt', 'r') as file:
    my_list = file.readlines()
wage_list = []
print("Зп свыше 20 000 имеют сотрудники: ")
for i in my_list:
    blank = i.find(" ", 1)
    i_name = i[0:blank]
    i_wage = float(i[blank + 1:-1])
    wage_list.append(i_wage)
    if i_wage > 20000:
        print(i_name)
print(f'Средняя зп всех сотрудников составляет: {sum(wage_list) / len(my_list)}')
