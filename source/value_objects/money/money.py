from value_objects.money.currency import CurrencyModel


class Money:

    def __init__(self, amount, currency: CurrencyModel):
        self.__amount = amount
        self.__currency = currency

    def __repr__(self):
        return '{}{}'.format(self.currency.sign, self.amount)

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency

    @classmethod
    def from_money(cls, money):
        return cls(money.amount, money.currency)

    @classmethod
    def from_currency(cls, currency: CurrencyModel):
        return cls(0, currency)

    def __eq__(self, other):
        return all([
            self.amount == other.amount,
            self.currency == other.currency
        ])

    def increase_amount(self, amount):
        return self.__class__(self.amount + amount, self.__currency)
