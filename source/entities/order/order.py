"""

В этой реализации Заказа явно создается идентификатор заказа и передается заказу из вне

    >>> o1 = OrderId('12062017_X_1')
    >>> o2 = OrderId('12062017_X_2')
    >>> o3 = OrderId('12062017_X_1')
    >>> o1 == o2
    False
    >>> o1 == o3
    True

    >>> oid = OrderId('12062017_X_1')
    >>> o = Order(oid, 100, 'Петров', 'Иван')

"""


class OrderId:

    def __init__(self, id_):
        self.id_ = id_

    def __eq__(self, other):
        return bool(self.id_ == other.id_)


class Order:

    def __init__(self, order_id, amount, first_name, last_name):
        self.order_id = order_id
        self.amount = amount
        self.first_name = first_name
        self.last_name = last_name
