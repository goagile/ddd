from domain_variables.base.units import Unit, ScaleResults


class StandardCurrentUnit(Unit):

    @staticmethod
    def A(value) -> ScaleResults:
        return ScaleResults(value, A())


class A(StandardCurrentUnit):

    @staticmethod
    def kA(value) -> ScaleResults:
        return ScaleResults(
            new_value=value / 1e3,
            new_units=kA())


class kA(StandardCurrentUnit):

    @staticmethod
    def A(value) -> ScaleResults:
        return ScaleResults(
            new_value=value * 1e3,
            new_units=A())


class Units:
    A = A()
    kA = kA()


registry_of_units = {
    'A': Units.A,
    'kA': Units.kA
}
