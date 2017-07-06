

class Spec:

    def is_satisfied_by(self, color):
        raise ValueError('Base method')


class ColorSpec(Spec):

    def __init__(self, color):
        self.__color = color

    def is_satisfied_by(self, product):
        return product.color == self.__color


class SizeSpec(Spec):

    def __init__(self, size):
        self.__size = size

    def is_satisfied_by(self, product):
        return product.size == self.__size


class BelowPriceSpec(Spec):

    def __init__(self, price):
        self.__price = price

    def is_satisfied_by(self, product):
        return bool(product.price > self.__price)


class AndSpec(Spec):

    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def is_satisfied_by(self, product):
        return self.augend.is_satisfied_by(product) and self.addend.is_satisfied_by(product)
