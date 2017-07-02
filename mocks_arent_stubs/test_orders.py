"""
    link: https://martinfowler.com/articles/mocksArentStubs.html
"""
import unittest

TALISKER = 'Talisker'
HIGHLAND_PARK = 'Highland Park'
warehouse = WarehouseImp()


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
