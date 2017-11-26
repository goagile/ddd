"""

Создаем валюту

    >>> from value_objects.money.currency import CurrencyModel

ISO код валюты должен быть валидным

    >>> usd = CurrencyModel('AAA22323', sign='$')
    Traceback (most recent call last):
      ...
    ValueError: Invalid Iso code

    >>> usd = CurrencyModel('USD', sign='$')
    >>> usd
    USD

"""
