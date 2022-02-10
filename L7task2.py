from abc import ABC, abstractmethod


class Clothes:

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, name, V):
        self.name = name
        self.V = V

    @property
    def fabric(self):
        result = self.V / 6.5 + 0.5
        return result


class Suit(Clothes):
    def __init__(self, name, H):
        self.name = name
        self.H = H

    @property
    def fabric(self):
        result = 2 * self.H + 0.3
        return result


coat1 = Coat('внесезонное', 46)
print(coat1.fabric)
suit1 = Suit('приталенный', 171)
print(suit1.fabric)
