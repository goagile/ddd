from nilsson.start_examples.specification.step_3_extract_spec_interface.product import Size, Product


class ProductRepository:

    __products = []

    def add_product(self, color, size=Size.M):
        new_product = Product(color, size)
        self.__products.append(new_product)

    def __iter__(self):
        return iter(self.__products)
