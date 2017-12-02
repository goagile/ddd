import unittest

from specification.refactoring_example.step_8_named_constants.product import Color, Size, product
from specification.refactoring_example.step_8_named_constants.product_finder import ProductFinder
from specification.refactoring_example.step_8_named_constants.product_repository import ProductRepository
from specification.refactoring_example.step_8_named_constants.spec import (
    ColorSpec, SizeSpec, AndSpec, BelowPriceSpec
)

red = Color.RED
green = Color.GREEN
blue = Color.BLUE

L = Size.L
M = Size.M
S = Size.S

repository = ProductRepository()
repository.add_product(color=red, size=S)
repository.add_product(color=green, size=L)
repository.add_product(price=120, color=blue, size=L)
repository.add_product(price=350, color=blue, size=M)

finder = ProductFinder(repository)


class TestRepository(unittest.TestCase):

    def test_find_by_color(self):
        expected = [product(color=red, size=S)]
        spec = ColorSpec(color=red)

        result = finder.select_by(spec)

        self.assertEqual(expected, result)

    def test_find_by_size(self):
        expected = [product(color=red, size=S)]
        spec = SizeSpec(size=S)

        result = finder.select_by(spec)

        self.assertEqual(expected, result)

    def test_find_below_price_and_color(self):
        expected = [
            product(price=120, color=blue, size=L),
            product(price=350, color=blue, size=M)
        ]
        spec = AndSpec(BelowPriceSpec(price=100), ColorSpec(color=blue))

        result = finder.select_by(spec)

        self.assertEqual(expected, result)
