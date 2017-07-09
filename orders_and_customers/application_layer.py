

class Repository():

    def get_customers(self, town, price):
        return []

    def get_orders(self, customer):
        return []


class OrderRepository:

    def __init__(self):
        self.orders = []

    def get_order(self, order_number):
        for o in self.orders:
            if o.order_number == order_number:
                return o
        return None

    def add_order(self, order):
        """ Утверждение по выходным условиям контракта """
        number_of_orders_before = len(self.orders)

        self.orders.append(order)

        assert number_of_orders_before == len(self.orders) - 1
