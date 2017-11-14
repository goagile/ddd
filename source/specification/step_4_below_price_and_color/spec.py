

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