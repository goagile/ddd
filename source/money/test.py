import unittest

from money.model import Currency, Currencies, Money, Price


RU20K = '20000 ₽'


class TestMoney(unittest.TestCase):
    """
        Заказ имеет свою полную стоимость, выраженную в деньгах 
    """

    def test_price_by_rubles_amount(self):
        price = Price.rubles(20000)

        self.assertEqual(RU20K, str(price))

    def test_price_str_representation(self):
        """
            Сумма, выраженная в деньгах, создание объектов напрямую 
        """
        price = Price(20000, Currencies.RUBLES)

        self.assertEqual(RU20K, str(price))

    def test_money_str_representation(self):
        """
            Прстое строковое представление
        """
        rubles = Money(20000, Currencies.RUBLES)

        self.assertEqual(RU20K, str(rubles))


class TestCurrency(unittest.TestCase):

    def test_str_representation(self):
        """
            Прстое строковое представление
        """
        expected = '₽'

        currency = Currencies.RUBLES

        self.assertEqual(expected, str(currency))
