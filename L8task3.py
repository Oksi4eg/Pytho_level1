class NotValue(Exception):
    def __init__(self, text):
        self.text = text

    pass


stop = False
my_list = []
while not stop:
    my_str = input('введите число (при завершении наберите stop): ')
    if my_str == 'stop':
        stop = True
    else:
        try:
            if not my_str.isdigit():
                raise NotValue('Вы ввели не число')
        # except ValueError:
        #     print('Вы ввели не число')
        except NotValue as err:
            print(err)
        else:
            my_str = int(my_str)
            my_list.append(my_str)
    print(my_list)
