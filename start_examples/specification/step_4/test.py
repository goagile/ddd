import unittest

from nilsson.start_examples.specification.step_4.product import Color, Size, product
from nilsson.start_examples.specification.step_4.product_finder import ProductFinder
from nilsson.start_examples.specification.step_4.product_repository import ProductRepository

repository = ProductRepository()
repository.add_product(color=Color.RED, size=Size.S)
repository.add_product(color=Color.GREEN, size=Size.L)
repository.add_product(price=120, color=Color.BLUE, size=Size.S)
repository.add_product(price=350, color=Color.BLUE, size=Size.M)

finder = ProductFinder(repository)


class TestRepository(unittest.TestCase):

    def test_find_by_color(self):
        expected = [product(color=Color.RED, size=Size.S)]

        result = finder.find_by_color(Color.RED)

        self.assertEqual(expected, result)

    def test_find_by_size(self):
        expected = [product(color=Color.GREEN, size=Size.L)]

        result = finder.find_by_size(Size.L)

        self.assertEqual(expected, result)

    # def test_find_below_price_and_color(self):
    #     expected = [
    #         product(price=120, color=Color.BLUE, size=Size.L),
    #         product(price=350, color=Color.BLUE, size=Size.M)
    #     ]
    #
    #     result = finder.find_below_price_and_color(100, Color.BLUE)
    #
    #     self.assertEqual(expected, result)
