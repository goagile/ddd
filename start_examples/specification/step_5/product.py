

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
        self.price = price
        self.color = color
        self.size = size

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
