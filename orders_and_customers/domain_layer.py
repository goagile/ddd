from datetime import datetime


class Customer:
    def __init__(self):
        self.customer_number = 0
        self.credit_limit = 0
        self.name = ''

    def take_snapshot(self):
        result = Customer()
        result.name = self.name
        return result


class Order:

    def __init__(self, customer):
        self.order_date = datetime.now()
        self.customer_snapshot = customer.take_snapshot()
        self.order_number = 0
        self.__order_lines = []

    def add_order_line(self, order_line):
        self.__order_lines.append(order_line)

    @property
    def total_amount(self) -> float:
        return sum(line.total_amount for line in self.__order_lines)

    @property
    def count(self):
        return len(self.__order_lines)


class OrderLine:

    def __init__(self, product):
        self.product = product
        self.quantity = 1

    @property
    def price(self):
        return self.product.price

    @property
    def total_amount(self):
        return self.product.price * self.quantity


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
