import unittest

from nilsson.start_examples.specification.model import Color, Product, Repository

repository = Repository()
repository.add_product(color=Color.RED)


class Test(unittest.TestCase):

    def test(self):
        expected = 1
        product = repository.find_by_color(Color.RED)

        result = product[0].key

        self.assertEqual(expected, result)
