from nilsson.start_examples.specification.step_5.spec import ColorSpec, SizeSpec, BelowPriceSpec, AndSpec


class ProductFinder:

    def __init__(self, repository):
        self.__repository = repository

    def find_by_color(self, color):
        result = []
        spec = ColorSpec(color)
        for product in self.__repository:
            if spec.is_satisfied_by(product):
                result.append(product)
        return result

    def find_by_size(self, size):
        result = []
        spec = SizeSpec(size)
        for product in self.__repository:
            if spec.is_satisfied_by(product):
                result.append(product)
        return result

    def find_below_price_and_color(self, price, color):
        result = []
        spec = AndSpec(
            BelowPriceSpec(price),
            ColorSpec(color)
        )
        for product in self.__repository:
            if spec.is_satisfied_by(product):
                result.append(product)
        return result
