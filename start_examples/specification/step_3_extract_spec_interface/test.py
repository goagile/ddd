import unittest

from nilsson.start_examples.specification.step_3_extract_spec_interface.model import Color, Repository, Size


repository = Repository()
repository.add_product(Color.RED)
repository.add_product(Color.GREEN, Size.L)


class TestRepository(unittest.TestCase):

    def test_find_by_color(self):
        expected = 1
        products = repository.find_by_color(Color.RED)

        result = products[0].key

        self.assertEqual(1, len(products))
        self.assertEqual(expected, result)

    def test_find_by_size(self):
        expected = 2
        products = repository.find_by_size(Size.L)

        result = products[0].key

        self.assertEqual(1, len(products))
        self.assertEqual(expected, result)
