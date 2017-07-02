import unittest

from nilsson.orders_and_customers.application_layer import Repository
from nilsson.orders_and_customers.domain_layer import Town, create_a_customer_and_an_order

repository = Repository()


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
