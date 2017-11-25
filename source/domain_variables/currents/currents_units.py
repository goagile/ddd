from domain_variables.base.units import Unit, UnitTranslation


class CurrentUnit(Unit):

    @staticmethod
    def A(value) -> UnitTranslation:
        return UnitTranslation(value, A())


class A(CurrentUnit):

    @staticmethod
    def kA(value) -> UnitTranslation:
        return UnitTranslation(
            new_value=value / 1e3,
            new_units=kA())


class kA(CurrentUnit):

    @staticmethod
    def A(value) -> UnitTranslation:
        return UnitTranslation(
            new_value=value * 1e3,
            new_units=A())


class Units:
    A = A()
    kA = kA()
