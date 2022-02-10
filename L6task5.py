class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}: Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}: Запуск отрисовки -> рисует вот так')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}: Запуск отрисовки -> рисует вот эдак')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}: Запуск отрисовки -> рисует и так, и сяк')


pen1 = Pen('синяя ручка')
pen1.draw()

pencil1 = Pencil('серый карандаш')
pencil1.draw()

handle1 = Handle('черный маркер')
handle1.draw()
