class MyZeroDiv(Exception):
    def __init__(self, text):
        self.text = text

    pass


str = input('Введите два числа через пробел: ')
my_list = str.split()
a = int(my_list[0])
b = int(my_list[1])

try:
    if b == 0:
        raise MyZeroDiv('Деление на ноль!')
except MyZeroDiv as err:
    print(err)
else:
    print(f'res={a / b}')
