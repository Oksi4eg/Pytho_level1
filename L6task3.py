#Я запуталась, класс позиция не может быть меньше класса работника (по задаче я понимаю наоборот)
#Логически позиция должна содержать зп, а работник наследовать позицию с ЗП
#Мы должны сначала заводить позицию, а потом работника. у позиции должна быть функция инкам,
# у работника ФИ + наследуемый инкам
# прошу прощения, уточнять ТЗ поздно, сделала 1) как я придумала 2) как поняла условие закомментировано

class Position:
    def __init__(self, position, wage, bonus):
        self.position=position
        self._income = {'wage': wage, 'bonus': bonus}
    def get_total_income(self):
        income=self._income['wage']+self._income['bonus']
        print(f'Доход с учетом премии: {income} тысяч долларов')

class Worker(Position):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(position,wage,bonus)
        self.name=name
        self.surname=surname
    def get_full_name(self):
        print(f'ФИ: {self.name} {self.surname}')

worker1 = Worker('John', 'Smith', 'agent', 20000, 5000)
worker1.get_full_name()
worker1.get_total_income()

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {'wage': wage, 'bonus': bonus}
#
#     def get_full_name(self):
#         print(f'ФИ: {self.name} {self.surname}')
#
#     def get_total_income(self):
#         income = self._income['wage'] + self._income['bonus']
#         print(f'Доход с учетом премии: {income} тысяч долларов')
#
#
# class Position(Worker):
#     def __init__(self, name, surname, _income):
#         super(Position, self).__init__(name, surname, _income)
#
# worker1 = Worker('John', 'Smith', 'agent', 20000, 5000)
# worker1.get_full_name()
# worker1.get_total_income()
