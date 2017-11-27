from domain_variables.base.units import BaseUnit, UnitsScaleResults


class StandardCurrentUnit(BaseUnit):

    @staticmethod
    def A(value) -> UnitsScaleResults:
        return UnitsScaleResults(value, A())


class A(StandardCurrentUnit):

    @staticmethod
    def kA(value) -> UnitsScaleResults:
        return UnitsScaleResults(
            new_value=value / 1e3,
            new_units=kA())


class kA(StandardCurrentUnit):

    @staticmethod
    def A(value) -> UnitsScaleResults:
        return UnitsScaleResults(
            new_value=value * 1e3,
            new_units=A())


class Units:
    A = A()
    kA = kA()


registry_of_units = {
    'A': Units.A,
    'kA': Units.kA
}
