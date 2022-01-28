# наверное, можно было проще

user_list = input('Заполните элементы списка через пробел: ')
list = user_list.split()
print(f'First list: {list}')
count = len(list)
list_2 = []
p = 0
for i in range(count // 2):
    list_i = list[p:p + 2] #я думала, он сразу может перевернуть, но нет
    list_i = list_i[::-1]
    list_2.append(list_i[0])
    list_2.append(list_i[1])
    p += 2

if count % 2 != 0:
    list_2.append(list[count - 1])

print(f'Second list: {list_2}')
