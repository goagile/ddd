import unittest


class TestContainerSpecification(unittest.TestCase):

    def test_is_satisfied_by(self):
        container = Container(specs=[], features=['ARMORED'])
        spec = ContainerSpecification('ARMORED')

        result = spec.is_satisfied_by(container)

        self.assertTrue(result)


class ContainerSpecification:

    def __init__(self, feature):
        self.__feature = feature

    def is_satisfied_by(self, container):
        return bool(self.__feature in container.features)


class Container:

    def __init__(self, specs, features):
        self.__specs = specs
        self.features = features

    def is_safely_packed(self):
        for spec in self.__specs:
            if not spec.is_satisfied_by(self):
                return False
        return True
