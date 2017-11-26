"""

Подключаем деньги

    >>> from value_objects.money.money import Money
    >>> from value_objects.money.currency import USD

Создаем объект деньги

    >>> five_dollars = Money(5, USD)
    >>> five_dollars.amount
    5
    >>> five_dollars.currency
    USD

Создаем копию объекта

    >>> d5 = Money(5, USD)
    >>> m = Money.from_money(d5)
    >>> d5 == m
    True
    >>> print(m, d5, sep='; ')
    $5; $5

Создаем ноль денег указанной валюты

    >>> zero_dollars = Money.from_currency(USD)
    >>> print(zero_dollars)
    $0

Добавляем деньги

    >>> hundred_dollars = zero_dollars.increase_amount(100)
    >>> hundred_dollars.amount
    100
    >>> print(hundred_dollars)
    $100
    >>> print(hundred_dollars.increase_amount(20))
    $120

"""
