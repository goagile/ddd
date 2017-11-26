

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

    @classmethod
    def from_money(cls, money):
        return cls(
            money.amount,
            money.currency)

    def __eq__(self, other):
        return all([
            self.amount == other.amount,
            self.currency == other.currency
        ])
