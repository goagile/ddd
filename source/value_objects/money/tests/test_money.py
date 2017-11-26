"""

Подключаем деньги

    >>> from value_objects.money.money import Money

Создаем объект деньги

    >>> from value_objects.money.currency import Currency
    >>> five_dollars = Money(5, Currency('USD'))

    >>> five_dollars.amount
    5

    >>> five_dollars.currency
    USD

Создаем копию объекта

    >>> d5 = Money(5, Currency('USD'))
    >>> m = Money.from_money(d5)

    >>> d5 == m
    True

"""
