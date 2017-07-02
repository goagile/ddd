

class Order:

    def __init__(self, product_type, need_quantity):
        self.product_type = product_type
        self.need_quantity = need_quantity
        self.quantity = 0

    def fill(self, stock):
        if not stock.has_inventory(self.product_type):
            return
        self.quantity = stock.unload(self.product_type, self.need_quantity)

    def is_filled(self):
        return bool(self.quantity != 0)


class Warehouse:

    def __init__(self):
        self.inventory = {}

    def get_inventory(self, product_type):
        return self.inventory.get(product_type)

    def add(self, product_type, product):
        self.inventory[product_type] = product

    def has_inventory(self, product_type):
        return bool(self.inventory.get(product_type, None))

    def unload(self, product_type, quantity):
        if self.inventory[product_type] < quantity:
            return 0
        self.inventory[product_type] -= quantity
        return quantity
