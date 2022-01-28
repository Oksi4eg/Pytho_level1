user_text = input('Напишите слово или предложение: ')
list = user_text.split()


def int_func(word):
    word = word[0].upper() + word[1:]
    return word


system_text = ''

for i, el in enumerate(list):
    system_text += int_func(el)
    system_text += ' ' if i < len(list) - 1 else ''

print(system_text)
