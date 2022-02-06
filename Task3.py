# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number1 = input('Введите число: ')
number2 = number1 * 2
number3 = number1 * 3
print(f'{number1} + {number2} + {number3} = {int(number1) + int(number2) + int(number3)}')
