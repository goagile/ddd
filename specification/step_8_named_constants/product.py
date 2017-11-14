

class Color:
    EMPTY = 'Empty'
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'


class Size:
    S = 'S'
    M = 'M'
    L = 'L'


class Product:

    def __init__(self, price, color, size):
        self.__price = price
        self.__color = color
        self.__size = size

    @property
    def price(self):
        return self.__price

    @property
    def color(self):
        return self.__color

    @property
    def size(self):
        return self.__size

    def __eq__(self, other):
        return all([
            self.price == other.price,
            self.color == other.color,
            self.size == other.size
        ])

    def __repr__(self):
        return 'Product: {}'.format(self.__dict__)


def product(price=0, color=Color.EMPTY, size=Size.M):
    return Product(price, color, size)
