user_stop = False

with open('l5task1.txt', 'a') as file:
    while not user_stop:
        my_str = input('Your text: ')
        if my_str == '':
            user_stop = True
            break
        file.write(f'{my_str}\n')
