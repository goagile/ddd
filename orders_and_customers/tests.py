import unittest

from nilsson.orders_and_customers.application_layer import Repository
from nilsson.orders_and_customers.domain_layer import (
    Town, create_a_customer_and_an_order, create_order, TotalCreditService
)

repository = Repository()


class TestFirst(unittest.TestCase):

    def test_can_get_customers_in_specific_town_with_orders_with_certain_size(self):
        num_of_instance_before = len(repository.get_customers(Town.Ronneby, 1000))
        expected = num_of_instance_before + 1
        create_ronneby_customer(20000)

        result = len(repository.get_customers(Town.Ronneby, 1000))

        self.assertEqual(expected, result)

    def test_can_get_orders_for_customer(self):
        new_customer = create_ronneby_customer(2000)

        orders_for_the_new_customer = repository.get_orders(new_customer)

        self.assertEqual(1, len(orders_for_the_new_customer))

    def test_can_get_total_amount_for_order(self):
        new_customer = create_ronneby_customer(420)

        order = repository.get_orders(new_customer)[0]

        self.assertEqual(420, order.total_amount)

    def test_can_iterate_over_order_lines(self):
        new_customer = create_ronneby_customer(420)

        orders = repository.get_orders(new_customer)

        self.fail('Not realized')
        # for o in orders:pass

    def test_can_get_total_credit_for_customer_excluding_current_order(self):
        new_customer = create_ronneby_customer(22)
        second_order = create_order(new_customer, 110)
        service = TotalCreditService()

        current_credit = service.get_current_credit(new_customer)
        second_current_credit = service.get_current_credit_by_order(new_customer, second_order)

        self.assertEqual(110 + 22, current_credit)
        self.assertEqual(22, second_current_credit)


def create_ronneby_customer(price):
    return create_a_customer_and_an_order(Town.Ronneby, 420)
