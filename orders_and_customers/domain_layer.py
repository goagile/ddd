

class Town:
    Ronneby = 'Ronneby'


def create_a_customer_and_an_order(town, price):
    return Customer()


def create_order(customer, price):
    return Order(price)


class Order:

    def __init__(self, price):
        self.pricr = price


class Customer:
    def __init__(self):
        pass


class TotalCreditService:

    def get_current_credit(self, customer):
        return 0

    def get_current_credit_by_order(self, customer, order):
        return 0
