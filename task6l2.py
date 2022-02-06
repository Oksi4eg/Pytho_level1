question_list = ['Номер товара', 'Название', 'Цена', 'Количество', 'Единица измерения']
main_list = []
product_list = []
product_dict = {}
count = int(input("Какое количество товаров Вы хотите завести: "))
for i in range(count):
    print(f'Укажите характеристики товара {i + 1}:')
    idd = input(f'{question_list[0]}: ')
    product_dict[question_list[1]] = input(f'{question_list[1]}: ')
    product_dict[question_list[2]] = input(f'{question_list[2]}: ')
    product_dict[question_list[3]] = input(f'{question_list[3]}: ')
    product_dict[question_list[4]] = input(f'{question_list[4]}: ')
    copy_dict = product_dict.copy()  # я потратила на это час своей жизни
    product_list = [idd, copy_dict]
    main_list.append(tuple(product_list))

print(f'Основной лист: {main_list}')

name_list = []  # не смогла тут записать сразу множество, определял как dict
price_list = []
quantity_list = []
unit_list = []

for i in main_list:
    element = i[1]
    name_list.append(element[question_list[1]])
    price_list.append(element[question_list[2]])
    quantity_list.append(element[question_list[3]])
    unit_list.append(element[question_list[4]])

print('Множества:')
print(f'{question_list[1]}: {set(name_list)}')
print(f'{question_list[2]}: {set(price_list)}')
print(f'{question_list[3]}: {set(quantity_list)}')
print(f'{question_list[4]}: {set(unit_list)}')
