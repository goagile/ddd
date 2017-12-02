import unittest

from specification.refactoring_example.step_7_inline_spec_creation.product import Color, Size, product
from specification.refactoring_example.step_7_inline_spec_creation.product_finder import ProductFinder
from specification.refactoring_example.step_7_inline_spec_creation.product_repository import ProductRepository
from specification.refactoring_example.step_7_inline_spec_creation.spec import ColorSpec, SizeSpec, AndSpec, \
    BelowPriceSpec

repository = ProductRepository()
repository.add_product(color=Color.RED, size=Size.S)
repository.add_product(color=Color.GREEN, size=Size.L)
repository.add_product(price=120, color=Color.BLUE, size=Size.L)
repository.add_product(price=350, color=Color.BLUE, size=Size.M)

finder = ProductFinder(repository)


class TestRepository(unittest.TestCase):

    def test_find_by_color(self):
        expected = [product(color=Color.RED, size=Size.S)]
        spec = ColorSpec(color=Color.RED)

        result = finder.select_by(spec)

        self.assertEqual(expected, result)

    def test_find_by_size(self):
        expected = [product(color=Color.RED, size=Size.S)]
        spec = SizeSpec(size=Size.S)

        result = finder.select_by(spec)

        self.assertEqual(expected, result)

    def test_find_below_price_and_color(self):
        expected = [
            product(price=120, color=Color.BLUE, size=Size.L),
            product(price=350, color=Color.BLUE, size=Size.M)
        ]
        spec = AndSpec(
            BelowPriceSpec(price=100),
            ColorSpec(color=Color.BLUE)
        )

        result = finder.select_by(spec)

        self.assertEqual(expected, result)
