## было оч трудно, плаваю в представлении данных, что есть что. не поняла, зачем ID, если у нас объекты типа уникальные
class Warehouse:
    def __init__(self):
        self.current_types = {}
        self.current_eqpts = {}

    def add_eqpt(self, eqpts):
        print('**ДОСТАВКА**')
        for eqpt, n in eqpts.items():
            eqpt_id = eqpt.get_id()
            eqpt_class = eqpt.class_type
            if self.current_eqpts.get(eqpt_id):
                self.current_eqpts[eqpt_id] += n
            else:
                self.current_eqpts[eqpt_id] = n

            if self.current_types.get(eqpt_class):  # для красивого вида
                self.current_types[eqpt_class] += n
            else:
                self.current_types[eqpt_class] = n

    def remove_eqpt(self, eqpt):
        eqpt_id = eqpt.get_id()
        eqpt_class = eqpt.class_type
        if eqpt_id in self.current_eqpts:
            print('**ВЫДАЧА ОБОРУДОВАНИЯ**')
            self.current_eqpts[eqpt_id] -= 1
            if self.current_eqpts[eqpt_id] == 0:
                self.current_eqpts.pop(eqpt_id)
            self.current_types[eqpt_class] -= 1
            if self.current_types[eqpt_class] == 0:
                self.current_types.pop(eqpt_class)
            return True
        return False

    def __str__(self):
        my_str = ("Количество оборудования на складе\n")
        my_str += ('-----------------------------------\n')
        for i, j in self.current_types.items():
            my_str2 = str(i)
            my_str += (f'{my_str2.upper()}, общее количество {j} штук(и)\n')
            for m, n in self.current_eqpts.items():
                eqpt = Equipment.all_eqpts[m]
                if eqpt.class_type == i:
                    my_str += f'{eqpt}, {n} штук\n'
            my_str += '\n'
        return my_str


class Equipment():
    __id = 0
    all_eqpts = []

    def get_type(cls):
        return cls.__class__.__name__

    def __init__(self, name):
        self.name = name
        self.class_type = self.get_type()
        self.__id = Equipment.__id
        Equipment.all_eqpts.append(self)
        Equipment.__id += 1

    def __str__(self):
        str = f'{self.__id}.{self.name} ({self.class_type.lower()}) '
        return str

    def get_id(self):
        return self.__id


class Printer(Equipment):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size


class Scanner(Equipment):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand


class Xerox(Equipment):

    def __init__(self, name, property):
        super().__init__(name)
        self.property = property


class Division():
    __id = 0
    norm_qty = 2

    def __init__(self, name):
        self.name = name
        self.equipments = {}
        self.__id = Division.__id
        Division.__id += 1
        self.sum_qty = 0

    def get_id(self):
        return self.__id

    def add_eqpt(self, whs, eqpt, confirmation=False):
        if self.sum_qty == 2 and not confirmation:
            print("Превышение нормы по оборудованию, нужно разрешение")
            return False
        else:
            eqpt_id = eqpt.get_id()
            if whs.remove_eqpt(eqpt):
                self.sum_qty += 1
                if self.equipments.get(eqpt_id):
                    self.equipments[eqpt_id] += 1
                else:
                    self.equipments[eqpt_id] = 1
            else:
                print('Такого оборудования на складе нет')


printer1 = Printer('Printer2020 w/b', 50)
printer2 = Printer('Printer2021 color', 50)
scanner1 = Scanner('Scan2021', 'Xerox')
xerox1 = Xerox('Xerox2021', 'Anything')
xerox2 = Xerox('Xerox2022', 'Anything')
print(Equipment.all_eqpts)
delivery1 = {printer1: 2, printer2: 3, scanner1: 1, xerox1: 5}
delivery2 = {printer1: 2}
my_warehouse = Warehouse()
my_warehouse.add_eqpt(delivery1)
my_warehouse.add_eqpt(delivery2)
print(my_warehouse)
division1 = Division('IT')
division1.add_eqpt(my_warehouse, printer1)
division1.add_eqpt(my_warehouse, xerox2)  # нет такого оборудования
division1.add_eqpt(my_warehouse, printer2)
division1.add_eqpt(my_warehouse, scanner1)  # без разрешения
division1.add_eqpt(my_warehouse, scanner1, True)
print(division1.equipments)  # сорян, не стала дописывать init, устала. но было бы такое же как у склада))
print(my_warehouse)
