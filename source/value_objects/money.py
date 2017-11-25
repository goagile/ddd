"""

    >>> from value_objects.currency import Currency
    >>> five_dollars = Money(5, Currency('USD'))

    >>> five_dollars.amount
    5

    >>> five_dollars.currency
    USD

"""


class Money:

    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency
