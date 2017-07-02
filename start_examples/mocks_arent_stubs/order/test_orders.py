"""
    link: https://martinfowler.com/articles/mocksArentStubs.html
"""
import unittest
from unittest.mock import MagicMock

from nilsson.start_examples.mocks_arent_stubs.order import Order, Warehouse

TALISKER = 'Talisker'
HIGHLAND_PARK = 'Highland Park'
warehouse = Warehouse()


class Test(unittest.TestCase):

    def setUp(self):
        warehouse.add(TALISKER, 50)
        warehouse.add(HIGHLAND_PARK, 25)

    def test_order_is_filled_if_enough_in_warehouse(self):
        order = Order(TALISKER, 50)
        order.fill(warehouse)

        self.assertTrue(order.is_filled())
        self.assertEqual(0, warehouse.get_inventory(TALISKER))

    def test_order_does_not_remove_if_not_enough(self):
        order = Order(TALISKER, 51)
        order.fill(warehouse)

        self.assertFalse(order.is_filled())
        self.assertEqual(50, warehouse.get_inventory(TALISKER))


class TestWithMocks(unittest.TestCase):

    def test_filling_removes_inventory_if_in_stock(self):
        order = Order(TALISKER, 50)
        warehouse_mock = MagicMock(
            has_inventory=MagicMock(return_value=True),
            unload=MagicMock(return_value=50)
        )

        order.fill(warehouse_mock)

        self.assertTrue(order.is_filled())
        self.assertEqual(50, order.quantity)

    def test_filling_does_not_remove_if_not_enough_in_stock(self):
        order = Order(TALISKER, 51)
        warehouse_mock = MagicMock(
            has_inventory=MagicMock(return_value=False)
        )

        order.fill(warehouse_mock)

        self.assertFalse(order.is_filled())
