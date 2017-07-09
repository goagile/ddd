import unittest
from datetime import datetime, timedelta

from nilsson.orders_and_customers.application_layer import OrderRepository
from nilsson.orders_and_customers.domain_layer import Order, Customer


order_repository = OrderRepository()


class TestOrder(unittest.TestCase):

    def test_can_create_an_order(self):
        result = Order(customer=Customer())

        self.assertIsNotNone(result)

    def test_can_create_order_with_customer(self):
        order = Order(customer=Customer())

        result = order.customer

        self.assertIsNotNone(result)

    def test_order_date_is_current_after_creation(self):
        the_time_before = datetime.now() - timedelta(milliseconds=1)

        order = Order(customer=Customer())

        self.assertTrue(order.order_date > the_time_before)
        self.assertTrue(order.order_date < datetime.now() + timedelta(milliseconds=1))

    def test_order_number_is_zero_after_creation(self):
        order = Order(customer=Customer())

        result = order.order_number

        self.assertEqual(0, result)

    def test_order_number_cant_be_zero_after_reconstruction(self):
        order_number = 42
        self.fake_an_order(order_number)
        order = order_repository.get_order(order_number)

        result = order.order_number

        self.assertEqual(order_number, result)

    def fake_an_order(self, order_number):
        order = Order(customer=Customer())

        order.order_number = order_number

        order_repository.add_order(order)

    def test_can_add_order(self):
        order = Order(customer=Customer())

        order_repository.add_order(order)
