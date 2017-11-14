

class Currency:

    def __init__(self, name, sign):
        self.__name = name
        self.__sign = sign

    @property
    def sign(self):
        return self.__sign

    def __str__(self):
        return self.__sign


class Currencies:
    RUBLES = Currency('Rubles', '₽')


class Money:

    def __init__(self, amount, currency=Currencies.RUBLES):
        self.__amount = amount
        self.__currency = currency
        self.__template = '{} {}'

    def __str__(self):
        return self.__template.format(self.__amount, self.__currency.sign)


class Price:

    def __init__(self, amount, currency: Currency):
        self.__money = Money(amount, currency)

    def __str__(self):
        return str(self.__money)

    @classmethod
    def rubles(cls, amount):
        return Money(amount, Currencies.RUBLES)
