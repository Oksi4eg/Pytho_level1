# я офигела в час ночи, когда увидела википедию=))
# хорошо мозг быстро понял, как это в реальности программирования

class Complex_fig:
    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b

    def __str__(self):
        my_fig = f'{self.a} + {self.b}i'
        return my_fig

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex_fig(a, b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b  # i в квадрате =-1, час ночи - мозг работает =))
        b = self.a * other.b + self.b * other.a
        return Complex_fig(a, b)


fig1 = Complex_fig(2, 3)
fig2 = Complex_fig(4, 5)
print(fig1)
print(fig2)
print(fig1 + fig2)
print(fig1 * fig2)
