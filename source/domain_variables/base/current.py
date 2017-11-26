from domain_variables.base.value import DomainValue


class CurrentValue(DomainValue):

    def scale(self, func):
        translation = func(self.value)
        result = self.__class__(translation.new_value, translation.new_units)
        return result

    def __add__(self, other):
        i1 = self.scale(self.units.A)
        i2 = other.scale(other.units.A)
        new_value = i1.value + i2.value
        new_units = i1.units
        result = self.__class__(new_value, new_units)
        return result
