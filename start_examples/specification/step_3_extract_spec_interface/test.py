import unittest

from nilsson.start_examples.specification.step_3_extract_spec_interface.model import Color, Repository, Size, Product

repository = Repository()
repository.add_product(Color.RED)
repository.add_product(Color.GREEN, Size.L)


def product(color, size=Size.M):
    return Product(color, size)


class TestRepository(unittest.TestCase):

    def test_find_by_color(self):
        expected = [product(Color.RED)]

        result = repository.find_by_color(Color.RED)

        self.assertEqual(expected, result)

    def test_find_by_size(self):
        expected = [product(Color.RED, Size.L)]

        result = repository.find_by_size(Size.L)

        self.assertEqual(expected, result)

    # def test_find_below_price_and_color(self):
    #     expected = [Pro]
    #     products = repository.find_below_price_and_color(100, Color.RED)
    #
    #     result = products[0]
    #
    #     self.assertEqual(2, len(products))
    #     self.assertEqual(expected, result)
