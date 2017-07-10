import unittest

from nilsson.orders_and_customers.domain_layer import Order, Customer, OrderLine, Product


TV_102 = Product('TV', price=102)
BOOK_50 = Product('BOOK', price=50)


class Test(unittest.TestCase):

    def test_can_exceed_max_amount_for_order(self):
        order = Order(Customer())
        order_line = OrderLine(TV_102)
        order_line.quantity = 1000
        order.add_order_line(order_line)

        result = order.is_valid()

        self.assertFalse(result)
