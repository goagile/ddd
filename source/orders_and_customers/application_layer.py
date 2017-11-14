

class OrderRepository:

    def __init__(self):
        self.orders = []

    def get_order(self, order_number):
        for o in self.orders:
            if o.order_number == order_number:
                return o
        return None

    def add_order(self, order):
        number_of_orders_before = len(self.orders)

        self.orders.append(order)

        assert number_of_orders_before == len(self.orders) - 1

    def get_orders(self, customer):
        result = []
        for order in self.orders:
            if order.customer_snapshot == customer:
                result.append(order)
        return result


class UnitOfWork:
    def get_by_key(self, key):
        raise ValueError('Abstract method')


class FakeWorkspace(UnitOfWork):
    def get_by_key(self, key):
        return 0


class CustomerRepository:

    def __init__(self, workspace: UnitOfWork):
        self.workspace = workspace

    def get_by_key(self, key):
        return self.workspace.get_by_key(key)
