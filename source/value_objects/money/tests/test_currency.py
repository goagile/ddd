"""

Создаем валюту

    >>> from value_objects.money.currency import Currency

ISO код валюты должен быть валидным

    >>> usd = Currency('AAA22323')
    Traceback (most recent call last):
      ...
    ValueError: Invalid Iso code

    >>> usd = Currency('USD')
    >>> usd
    USD

"""
