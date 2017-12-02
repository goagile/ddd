from specification.refactoring_example.step_9_spec_factory.spec import ColorSpec, SizeSpec, AndSpec, BelowPriceSpec


class SpecFactory:

    @staticmethod
    def color_spec(color):
        return ColorSpec(color)

    @staticmethod
    def size_spec(size):
        return SizeSpec(size)

    @staticmethod
    def and_spec(augend, addend):
        return AndSpec(augend, addend)

    @staticmethod
    def below_price_spec(price):
        return BelowPriceSpec(price)
