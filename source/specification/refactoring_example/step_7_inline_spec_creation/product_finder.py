from specification.refactoring_example.step_7_inline_spec_creation.spec import ColorSpec, SizeSpec, BelowPriceSpec, AndSpec


class ProductFinder:

    def __init__(self, repository):
        self.__repository = repository

    def find_by_color(self, color):
        spec = ColorSpec(color)
        return self.select_by(spec)

    def find_by_size(self, size):
        spec = SizeSpec(size)
        return self.select_by(spec)

    def find_below_price_and_color(self, price, color):
        spec = AndSpec(
            BelowPriceSpec(price),
            ColorSpec(color)
        )
        return self.select_by(spec)

    def select_by(self, spec):
        result = []
        for product in self.__repository:
            if spec.is_satisfied_by(product):
                result.append(product)
        return result
