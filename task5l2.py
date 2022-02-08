list1 = [7, 5, 3, 3, 2]
count = len(list1)
print(f'Изначальный рейтинг: {list1}')

user = int(input('Введите свой рейтинг: '))

for i in list1[::-1]:
    if i >= user:
        list1.insert(count, user)
        break
    count -= 1
if user > max(list1):
    list1.insert(0, user)

print(f'Финальный рейтинг: {list1}')
