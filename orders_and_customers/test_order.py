import unittest
from datetime import datetime, timedelta

from nilsson.orders_and_customers.application_layer import OrderRepository
from nilsson.orders_and_customers.domain_layer import Order, Customer


order_repository = OrderRepository()


class TestOrder(unittest.TestCase):

    def fake_a_customer(self, customer_number):
        customer = Customer()

        customer.customer_number = customer_number

        return customer

    def fake_an_order(self, order_number, customer):
        order = Order(customer)

        order.order_number = order_number

        order_repository.add_order(order)

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
        customer = Customer()
        order_number = 42
        self.fake_an_order(order_number, customer)
        order = order_repository.get_order(order_number)

        result = order.order_number

        self.assertEqual(order_number, result)

    def test_can_add_order(self):
        order = Order(customer=Customer())

        order_repository.add_order(order)

    def test_can_find_orders_via_customer(self):
        customer = self.fake_a_customer(7)
        self.fake_an_order(42, customer)
        self.fake_an_order(12, customer=Customer())
        self.fake_an_order(3, customer)
        self.fake_an_order(21, customer)
        self.fake_an_order(1, customer=Customer())
        orders = order_repository.get_orders(customer)

        result = len(orders)

        self.assertEqual(3, result)

    def test_empty_order_has_zero_as_total_amount(self):
        order = Order(customer=Customer())

        result = order.total_amount

        self.assertEqual(0, result)
