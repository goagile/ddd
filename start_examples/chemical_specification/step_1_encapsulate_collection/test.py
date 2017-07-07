import unittest


class TestContainer(unittest.TestCase):

    def test_add_spec(self):
        container = Container(specs=[], features=[])
        spec = ContainerSpecification('ARMORED')
        container.add_spec(spec)

        result = container.specs[0]

        self.assertEqual(spec, result)

    def test_add_feature(self):
        container = Container(specs=[], features=[])
        feature = 'ARMORED'
        container.add_feature(feature)

        result = container.features[0]

        self.assertEqual(feature, result)

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
        self.__features = features

    @property
    def specs(self):
        return self.__specs

    @property
    def features(self):
        return self.__features

    def add_spec(self, spec: ContainerSpecification):
        self.__specs.append(spec)

    def add_feature(self, feature: str):
        self.__features.append(feature)

    def is_safely_packed(self):
        for spec in self.__specs:
            if not spec.is_satisfied_by(self):
                return False
        return True
