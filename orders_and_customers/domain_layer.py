from datetime import datetime


class Order:

    def __init__(self, customer):
        self.order_date = datetime.now()
        self.customer = customer
        self.order_number = 0
        self.total_amount = 0

    def is_ok_accounting_to_size(self):
        return False


class Customer:
    def __init__(self):
        self.customer_number = 0
        self.credit_limit = 0







class OrderFactory:

    @classmethod
    def create_order(cls, customer):
        return Order(price=0)

    @classmethod
    def create_order_line(cls, order, product):
        pass


class Product:
    def __init__(self):
        pass


class OrderStatus:
    ACCEPTED = 'Accepted'


class Town:
    Ronneby = 'Ronneby'


def create_a_customer_and_an_order(town, price):
    return Customer()


def create_customer(name):
    return Customer()


def create_order(customer, price):
    return Order(price)


class TotalCreditService:

    def get_current_credit(self, customer):
        return 0

    def get_current_credit_by_order(self, customer, order):
        return 0
