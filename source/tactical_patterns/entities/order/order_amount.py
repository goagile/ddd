"""

    >>> order = Order(
    ...    amount=Amount.dollar(100),
    ...    first_name='Петров',
    ...    last_name='Сидор'
    ... )

    >>> str(order)
    'Петров Сидор $100'

"""


class Dollar:

    def __init__(self, amount):
        self.__amount = amount

    def __str__(self):
        return '${}'.format(self.__amount)


class Amount:

    def __init__(self, value):
        self.value = value

    @classmethod
    def dollar(self, amount):
        return Dollar(amount)


class Order:

    def __init__(self, amount, first_name, last_name):
        self.amount = amount
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.amount)
