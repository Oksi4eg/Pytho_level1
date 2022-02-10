# у меня видимо времени много, в общем, можно складывать любые размерности хоть в строках, хоть в столбцах=)
# я не стала делать поиск макс числа, чтобы пробелы еще выравнить, если появится трехзначное число

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        result = ''
        for i in self.list:
            for el in i:
                if el > 9:
                    result += f'{el} '
                else:
                    result += f' {el} '
            result += '\n'
        return result

    def __add__(self, other):
        res_list = []
        l_self = len(self.list)
        r = len(other.list) - l_self
        for i, el in enumerate(self.list):
            if i < len(other.list) - 1:
                tmp_list = other.list[i]
                for i2, el2 in enumerate(el):
                    if i2 <= len(tmp_list) - 1:
                        tmp_list[i2] += el2
                    else:
                        tmp_list.append(el2)

            else:
                tmp_list = el
            res_list.append(tmp_list)
        if r > 0:
            for i in range(r):
                res_list.append(other.list[i + l_self])

        return Matrix(res_list)


matrix1 = Matrix([[10, 2, 3], [3, 4], [5]])
matrix2 = Matrix([[2, 4, 3, 4], [5, 8], [1], [1, 2, 2]])
print(matrix1, '******')
print(matrix2, '******')
print(matrix1 + matrix2)
