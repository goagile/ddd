import unittest

from nilsson.orders_and_customers.application_layer import Repository
from nilsson.orders_and_customers.domain_layer import (
    Town, create_a_customer_and_an_order, create_order, TotalCreditService,
    create_customer, OrderFactory, Product, OrderStatus)

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

    def test_can_check_that_an_order_total_size_is_ok(self):
        new_customer = create_ronneby_customer(2000000)

        order = repository.get_orders(new_customer)[0]

        self.assertFalse(order.is_ok_accounting_to_size())

    def test_cant_set_to_high_credit_limit_for_customer(self):
        new_customer = create_ronneby_customer(10)

        # Нужен упрощенный вариант CreditService <= 300
        new_customer.credit_service = StubCreditService(300)
        new_customer.credit_limit = 1000

        self.assertFalse(new_customer.is_ok_credit_limit)

    def test_can_create_order_with_order_line(self):
        new_customer = create_customer('Jim')
        new_order = OrderFactory.create_order(new_customer)

        OrderFactory.create_order_line(new_order, Product())

        self.assertEqual(1, new_order.order_lines)

    def test_can_accept_order(self):
        new_customer = create_customer('Jim')
        order = OrderFactory.create_order(new_customer)
        self.assertFalse(order.status == OrderStatus.ACCEPTED)

        order.accept()

        self.assertTrue(order.status == OrderStatus.ACCEPTED)


def create_ronneby_customer(price):
    return create_a_customer_and_an_order(Town.Ronneby, 420)


class StubCreditService:

    def __init__(self, limit):
        self.limit = limit
