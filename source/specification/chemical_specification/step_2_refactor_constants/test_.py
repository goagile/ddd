import unittest

from specification.chemical_specification.step_2_refactor_constants.model import (
    Container,
    ContainerSpecification,
    ContainerFeature
)


ARM = ContainerFeature.ARMORED
ARM_SPEC = ContainerSpecification(ARM)


class TestContainer(unittest.TestCase):

    def test_add_spec(self):
        container = Container()
        container.add_spec(ARM_SPEC)

        result = container.specs

        self.assertEqual([ARM_SPEC], result)

    def test_add_feature(self):
        container = Container()
        container.add_feature(ARM)

        result = container.features

        self.assertEqual([ARM], result)


class TestContainerSpecification(unittest.TestCase):

    def test_is_satisfied_by(self):
        container = Container()
        container.add_feature(ARM)

        result = ARM_SPEC.is_satisfied_by(container)

        self.assertTrue(result)
