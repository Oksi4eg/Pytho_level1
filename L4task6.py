# нужно отправлять фантазию спать раньше себя =))

from itertools import count, cycle

user_num = int(input("красивенько будет <4: "))  # не смогла вывести также, как выводили время в формате в 2 знака
step = user_num  # сначала писала конкретные числа, но подумала, что так будет вывод красивее ))
ncycle = user_num  # сначала писала конкретные числа, но подумала, что так будет вывод красивее ))
map_list = ncycle * step
my_list_first = []
my_list_full = []
my_dict = {}
for el in count(user_num, step):
    my_list_first.append(el)
    if el == user_num * ncycle:
        break
i = 1
countcycle = 0
for el in cycle(my_list_first):
    if i == countcycle:
        i += 1
        continue
    my_list_full.append(el)
    map_list -= 1
    if i < ncycle:
        i += 1
    else:
        i = 1
        countcycle += 1
    if map_list == 0:
        break

for i in range(ncycle):
    scope = (i) * ncycle
    print(my_list_full[scope:scope + ncycle])
