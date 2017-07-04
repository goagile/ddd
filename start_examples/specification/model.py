class Color:
    RED = 'Red'
    GREEN = 'Green'


class Product:

    def __init__(self, key, color):
        self.key = key
        self.color = color


class Repository:

    key = 0
    products = []

    def add_product(self, color):
        new_key = self.key + 1
        self.key = new_key
        new_product = Product(new_key, color)
        self.products.append(new_product)

    def find_by_color(self, color):
        result = []
        for product in self.products:
            if product.color == color:
                result.append(product)
        return result

    def find_by_size(self, size):
        result = []
        for product in self.products:
            if product.size == size:
                result.append(product)
        return result