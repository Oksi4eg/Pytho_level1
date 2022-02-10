with open('l5task6.txt', 'r') as file:
    my_list = file.readlines()
for i in my_list:
    name_count=i.find(' ',1)
    i_name=i[0:name_count]
    i_el=''
    i_sum=0
    for el in i[name_count:-2]: #подсократить работу
        if el.isdigit():
            i_el+=el
        else:
            if i_el.isdigit():
                i_sum+=int(i_el)
                i_el=''
    print(f'{i_name} {i_sum}')