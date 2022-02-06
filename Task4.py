# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_number = int(input('Введите целое пложительное число: '))
max_number = 0

while user_number > 0:
    number = user_number%10
    user_number//=10
    if number > max_number:
        max_number = number
print(f'Максимальная цифра в Вашем числе: {max_number}')
