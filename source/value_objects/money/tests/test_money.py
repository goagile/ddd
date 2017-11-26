"""

Подключаем деньги

    >>> from value_objects.money.money import Money
    >>> from value_objects.money.currency import USD, RUR

Создаем объект деньги.
Проверяем его свойства, Печатем на консоли.

    >>> five_dollars = Money(5, USD)
    >>> five_dollars.amount
    5
    >>> five_dollars.currency
    USD
    >>> five_dollars
    $5

Создаем новые деньги на основе существующих.
Деньги должны быть равны.

    >>> d5 = Money(5, USD)
    >>> m = Money.from_money(d5)
    >>> d5 == m; print(m, d5, sep=' == ')
    True
    $5 == $5

Создаем ноль денег указанной валюты

    >>> zero = Money.from_currency(USD)
    >>> print(zero)
    $0

Увеличиваем сумму денег

    >>> zero = Money.from_currency(USD)
    >>> hundred = zero.increase_amount(100)
    >>> hundred.amount
    100
    >>> print(hundred)
    $100
    >>> print(hundred.increase_amount(20))
    $120

Складываем деньги

    >>> d100 = Money(100, USD)
    >>> d100
    $100
    >>> r2000 = Money(2000, RUR)
    >>> r2000
    ₽2000

Сложить деньги в разной валюте не удастся

    >>> x = d100 + r2000
    Traceback (most recent call last):
      ...
    ValueError: USD != RUR Currency are not equal

А вот в одинаковой можно

    >>> d20 = Money(20, USD)
    >>> d20
    $20
    >>> y = d100 + d20
    >>> y
    $120

При сложении денег были созданы новые деньги.
Существующие деньги не изменились.

    >>> print(d20, y, sep=' != ')
    $20 != $120

"""
