import unittest


class Repository():

    def get_customers(self, town, price):
        return []

    def get_orders(self, customer):
        return []


repository = Repository()


class Town:
    Ronneby = 'Ronneby'


class TestFirst(unittest.TestCase):

    def test_can_get_customers_in_specific_town_with_orders_with_certain_size(self):
        num_of_instance_before = len(repository.get_customers(Town.Ronneby, 1000))
        expected = num_of_instance_before + 1
        create_a_customer_and_an_order(Town.Ronneby, 20000)

        result = len(repository.get_customers(Town.Ronneby, 1000))

        self.assertEqual(expected, result)

    def test_can_get_orders_for_customer(self):
        new_customer = create_a_customer_and_an_order(Town.Ronneby, 2000)

        orders_for_the_new_customer = repository.get_orders(new_customer)

        self.assertEqual(1, len(orders_for_the_new_customer))

    def test_(self):
        pass


def create_a_customer_and_an_order(town, proce):
    return Customer()


class Customer:
    def __init__(self):
        pass
