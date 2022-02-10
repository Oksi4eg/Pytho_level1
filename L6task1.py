# наверное, я перемудрила

from itertools import cycle


class TrafficLight:
    list_color = []
    color_dict = {'красный': 7, 'желтый': 2, 'зеленый': 3}
    list_check = [key for key, value in color_dict.items()]
    work_time = 100

    def __init__(self, color):
        self.__color = color
        self.list_color.append(self.__color)

    def running(self):
        color = self.__color
        sec = self.color_dict[self.__color]
        print(f'{color}: {sec} секунд')
        TrafficLight.work_time -= sec


color1 = TrafficLight('красный')
color2 = TrafficLight('желтый')
color3 = TrafficLight('зеленый')

if TrafficLight.list_color != TrafficLight.list_check:
    print('Нарушен порядок')
else:
    while TrafficLight.work_time >= 0:
        color1.running()
        color2.running()
        color3.running()
