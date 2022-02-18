#Мне кажется, что я сделала не то, но я не совсем поняла, как правильно
#Мучалась долго

class Data:

    @classmethod
    def get_count(cls, str_data):
        my_list = str_data.split('-')
        d = my_list[0]
        m = my_list[1]
        y = my_list[2]
        print(d, m, y)

    @staticmethod
    def validation(str_data):
        my_list = str_data.split('-')
        validation = 0 < int(my_list[0]) <= 31 and 0 < int(my_list[1]) <= 12 and my_list[2].isdigit()
        print(validation)


Data.get_count('01-12-2023')
Data.validation('01-12-2023')
