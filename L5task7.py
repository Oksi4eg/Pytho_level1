import json

with open('l5task7.txt', 'r') as file:
    my_list = file.readlines()
    profit_list = []
    my_dict = {}
print('Фирмы, показывающие прибыль: ')
for i in my_list:
    firm_list = i.split()
    profit = int(firm_list[3]) - int(firm_list[2])
    name = firm_list[0]
    my_dict[name] = profit
    if profit > 0:
        print(f'{name}: {profit}')
        profit_list.append(profit)
avg_profit = sum(profit_list) / len(profit_list)

my_dict2 = {'average_profit': avg_profit}
final_list = [my_dict, my_dict2]

with open('L5task7.json', 'w') as file:
    json.dump(final_list, fp=file)

print(f'Средняя прибыль: {avg_profit}')
