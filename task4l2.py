user_list = input('Заполните элементы списка через пробел: ')
list = user_list.split()
count = len(list)

for i in range(count):
    str = list[i]
    print(f'{i + 1}. {str[:10]}')
