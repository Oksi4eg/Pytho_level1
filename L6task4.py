class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.color} {self.name} едет со скоростью {self.speed} км/час')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'{self.color} {self.name} едет со скоростью {self.speed} км/час')
        if self.speed > 60:
            print(f'❗ Ограничение скорости 60 км/час! Вы превышате!')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'{self.color} {self.name} едет со скоростью {self.speed} км/час')
        if self.speed > 40:
            print(f'❗ Ограничение скорости 40 км/час! Вы превышате!')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car1 = Car(80, 'красная', 'феррари', False)
car1.go()
car1.stop()
car1.turn('вправо')
car1.show_speed()

car2 = TownCar(60, 'синяя', 'киа')
car2.go()
car2.stop()
car2.turn('вправо')
car2.show_speed()

car3 = WorkCar(80, 'грязный', 'грузовик')
car3.go()
car3.stop()
car3.turn('вправо')
car3.show_speed()

car4 = SportCar(200, 'красная', 'феррари')
car4.go()
car4.stop()
car4.turn('вправо')
car4.show_speed()

car5 = PoliceCar(200, 'синяя', 'жигули')
car5.go()
car5.stop()
car5.turn('вправо')
car5.show_speed()
