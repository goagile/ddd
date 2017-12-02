from specification.refactoring_example.step_3_extract_spec_interface.spec import ColorSpec, SizeSpec


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
