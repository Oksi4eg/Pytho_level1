sum_list = 0
stop = False
while not stop:
    str = input('Введите числа через пробел (при окончании в конце поставьте " *"): ')
    list = str.split()
    for i, el in enumerate(list):
        if el == '*':
            list.pop()
            stop = True
            break
        else:
            list[i] = int(el)
    sum_list += sum(list)
    print(sum_list)
