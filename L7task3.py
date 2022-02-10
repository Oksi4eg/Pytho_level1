from math import ceil


class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        result = str(self.cells)
        return result

    def __add__(self, other):
        result = self.cells + other.cells
        return Cell(result)

    def __sub__(self, other):
        result = self.cells - other.cells
        if result < 0:
            print('Какое-то из вычитаний меньше нуля')
        return Cell(result)

    def __mul__(self, other):
        result = self.cells * other.cells
        return Cell(result)

    def __truediv__(self, other):
        result = self.cells // other.cells
        return Cell(result)

    def make_order(self, row):
        lines = ceil(self.cells / row)
        count = self.cells
        pic = ''
        for l in range(lines):
            i = 1
            while i <= row and count > 0:
                pic += '◻'
                count -= 1
                i += 1
            pic += '\n'
        return pic


cell1 = Cell(30)
cell2 = Cell(200)
cell3 = Cell(2)
print(cell1)
print(cell1 + cell2 + cell3)
print(cell1 - cell2 - cell3)  # не могу принять в результат str, чтобы не было ошибки.
# и повторное сообщение и не выводить отр тоже не смогла обойти
print(cell1 * cell2 * cell3)
print(cell1 / cell2)
print(cell1.make_order(13))
