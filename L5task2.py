with open('l5task1.txt', 'r') as file:
    my_list=file.readlines()
print(f'Количество строк: {len(my_list)}')

for i,el in enumerate(my_list):
    print(f'{i+1} cтрока: {len(el)-2} символов')
