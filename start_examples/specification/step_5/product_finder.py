from nilsson.start_examples.specification.step_5.spec import ColorSpec, SizeSpec, BelowPriceSpec


class ProductFinder:

    def __init__(self, repository):
        self.__repository = repository

    def find_by_color(self, color):
        result = []
        for product in self.__repository:
            if ColorSpec(color).is_satisfied_by(product):
                result.append(product)
        return result

    def find_by_size(self, size):
        result = []
        for product in self.__repository:
            if SizeSpec(size).is_satisfied_by(product):
                result.append(product)
        return result

    def find_below_price_and_color(self, price, color):
        result = []
        price_spec = BelowPriceSpec(price)
        color_spec = ColorSpec(color)
        for product in self.__repository:
            if price_spec.is_satisfied_by(product) and color_spec.is_satisfied_by(product):
                result.append(product)
        return result
