

class Color:
    RED = 'Red'
    GREEN = 'Green'


class Size:
    S = 'S'
    M = 'M'
    L = 'L'


class Product:

    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __eq__(self, other):
        return all([
            self.color == other.color,
            self.size == other.size
        ])

    def __repr__(self):
        return 'Product: {}'.format(self.__dict__)
