"""

    >>> o = Order('12062017_X_1', 100, 'Петров', 'Иван')
    >>> isinstance(o.order_id, OrderId)
    True
    >>> str(o.order_id)
    '12062017_X_1'

"""


class OrderId:

    def __init__(self, id_):
        self.id_ = id_

    def __eq__(self, other):
        return bool(self.id_ == other.id_)

    def __str__(self):
        return str(self.id_)


class Order:

    def __init__(self, id_, amount, first_name, last_name):
        self.id_ = id_
        self._order_id = None
        self.amount = amount
        self.first_name = first_name
        self.last_name = last_name

    @property
    def order_id(self):
        if not self._order_id:
            self._order_id = OrderId(self.id_)
        return self._order_id
