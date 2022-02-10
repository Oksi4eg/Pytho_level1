season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {
    1: season_list[0],
    2: season_list[0],
    3: season_list[1],
    4: season_list[1],
    5: season_list[1],
    6: season_list[2],
    7: season_list[2],
    8: season_list[2],
    9: season_list[3],
    10: season_list[3],
    11: season_list[3],
    12: season_list[3]
}

user = int(input("Введите номер месяца: "))

if user == 12:
    print(f'Результат list: {season_list[0]}')
else:
    print(f'Результат list: {season_list[user // 3]}')

print(f'Результат dict: {season_dict[user]}')
