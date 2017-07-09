from datetime import datetime


class Customer:
    def __init__(self):
        self.customer_number = 0
        self.credit_limit = 0


class Order:

    def __init__(self, customer):
        self.order_date = datetime.now()
        self.customer = customer
        self.order_number = 0
        self.__total_amount = 0
        self.order_lines = []

    def add_order_line(self, order_line):
        self.order_lines.append(order_line)

    @property
    def total_amount(self):
        self.__total_amount = sum(line.product.price * line.quantity for line in self.order_lines)
        return self.__total_amount


class OrderLine:

    def __init__(self, product):
        self.product = product
        self.quantity = 1

    @property
    def price(self):
        return self.product.price


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price





# class OrderFactory:
#
#     @classmethod
#     def create_order(cls, customer):
#         return Order(price=0)
#
#     @classmethod
#     def create_order_line(cls, order, product):
#         pass
#
#
# class Product:
#     def __init__(self, ):
#         pass
#
#
# class OrderStatus:
#     ACCEPTED = 'Accepted'
#
#
# class Town:
#     Ronneby = 'Ronneby'
#
#
# def create_a_customer_and_an_order(town, price):
#     return Customer()
#
#
# def create_customer(name):
#     return Customer()
#
#
# def create_order(customer, price):
#     return Order(price)
#
#
# class TotalCreditService:
#
#     def get_current_credit(self, customer):
#         return 0
#
#     def get_current_credit_by_order(self, customer, order):
#         return 0
