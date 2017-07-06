import unittest

from nilsson.start_examples.specification.step_3_extract_spec_interface.product import Color, Size, Product
from nilsson.start_examples.specification.step_3_extract_spec_interface.product_finder import ProductFinder
from nilsson.start_examples.specification.step_3_extract_spec_interface.product_repository import ProductRepository

repository = ProductRepository()
repository.add_product(Color.RED)
repository.add_product(Color.GREEN, Size.L)

finder = ProductFinder(repository)


def product(color, size=Size.M):
    return Product(color, size)


class TestRepository(unittest.TestCase):

    def test_find_by_color(self):
        expected = [product(Color.RED)]

        result = finder.find_by_color(Color.RED)

        self.assertEqual(expected, result)

    def test_find_by_size(self):
        expected = [product(Color.GREEN, Size.L)]

        result = finder.find_by_size(Size.L)

        self.assertEqual(expected, result)

    # def test_find_below_price_and_color(self):
    #     expected = [Pro]
    #     products = repository.find_below_price_and_color(100, Color.RED)
    #
    #     result = products[0]
    #
    #     self.assertEqual(2, len(products))
    #     self.assertEqual(expected, result)
