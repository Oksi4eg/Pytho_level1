# есть сомнения, что правильно поняла ТЗ

def user_info(name, surname, b_year, city, email, ph):
    result_1 = f'Пользователь {name} {surname}, {b_year} года рождения, город: {city}, Контактные данные: {email}, {ph}'
    return result_1


print(user_info('Oks', 'T', '1988', 'Moscow', 'xxx@mail.ru', '+71111'))
