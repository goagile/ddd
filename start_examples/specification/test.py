import unittest

from nilsson.start_examples.specification.model import Color, Product, Repository, Size


repository = Repository()
repository.add_product(Color.RED)
repository.add_product(Color.GREEN, Size.L)


class Test(unittest.TestCase):

    def test_find_by_color(self):
        expected = 1
        product = repository.find_by_color(Color.RED)

        result = product[0].key

        self.assertEqual(expected, result)

    def test_find_by_size(self):
        expected = 2
        product = repository.find_by_size(Size.L)

        result = product[0].key

        self.assertEqual(expected, result)
