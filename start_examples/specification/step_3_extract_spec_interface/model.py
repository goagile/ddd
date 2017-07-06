

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


class Repository:

    __products = []

    def add_product(self, color, size=Size.M):
        new_product = Product(color, size)
        self.__products.append(new_product)

    def __iter__(self):
        return iter(self.__products)


class ProductFinder:

    def __init__(self, repository):
        self.__repository = repository

    def find_by_color(self, color):
        result = []
        for product in self.__repository:
            if ColorSpec(color).is_satisfied_by(product):
                result.append(product)
        return result

    def find_by_size(self, size):
        result = []
        for product in self.__repository:
            if SizeSpec(size).is_satisfied_by(product):
                result.append(product)
        return result


class Spec:

    def is_satisfied_by(self, color):
        raise ValueError('Base method')


class ColorSpec(Spec):

    def __init__(self, color):
        self.color = color

    def is_satisfied_by(self, product):
        return product.color == self.color


class SizeSpec(Spec):

    def __init__(self, size):
        self.size = size

    def is_satisfied_by(self, product):
        return product.size == self.size
