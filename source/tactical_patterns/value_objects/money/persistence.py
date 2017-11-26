"""

Создаем деньги

    >>> d100 = Money(100, Currency.USD)
    >>> print(d100)
    $100

Сериализуем деньги в словарь

    >>> dumped = MoneyDictSerializer(d100).dumps()
    >>> isinstance(dumped, dict)
    True
    >>> print(dumped['amount'], dumped['iso_code'], sep='; ')
    100; USD

Десериализуем деньги из словаря

    >>> new_d100 = MoneyDictSerializer.loads(dumped)
    >>> isinstance(new_d100, Money)
    True
    >>> print(new_d100)
    $100

"""


from tactical_patterns.value_objects.money.money import Money
from tactical_patterns.value_objects.money.currency import Currency


INVALID_MONEY_DICT_FIELD = 'Invalid money dict field'


class MoneyDictSerializer:

    def __init__(self, money: Money):
        self.__money = money

    def dumps(self):
        result = {
            'amount': self.__money.amount,
            'iso_code': self.__money.currency.iso_code
        }
        return result

    @classmethod
    def loads(cls, dumped: dict):
        amount = cls.__validated(dumped, 'amount')
        iso_code = cls.__validated(dumped, 'iso_code')
        currency = Currency.from_iso_code(iso_code)
        result = Money(amount, currency)
        return result

    @classmethod
    def __validated(cls, dumped, key):
        value = dumped.get(key)
        if value is None:
            raise ValueError("{} {}".format(key, INVALID_MONEY_DICT_FIELD))
        return value
