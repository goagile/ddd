from domain_variables.base.value import DomainValue, EQUALITY_DELTA


class CurrentValue(DomainValue):

    def scale(self, func):
        # TODO: scale_function, scale_results
        translation = func(self.value)
        result = self.__class__(translation.new_value, translation.new_units)
        return result

    def __scale_to_si(self, other):
        """ Приводим к СИ """
        i1 = self.scale(self.units.A)
        i2 = other.scale(other.units.A)
        return i1, i2

    def equal(self, other, delta=EQUALITY_DELTA):
        i1, i2 = self.__scale_to_si(other)
        return bool(self._are_values_equal(i1.value, i2.value, delta))

    def __gt__(self, other):
        i1, i2 = self.__scale_to_si(other)
        return i1.value > i2.value

    def __lt__(self, other):
        i1, i2 = self.__scale_to_si(other)
        return i1.value < i2.value

    def __ge__(self, other):
        i1, i2 = self.__scale_to_si(other)
        return i1.value >= i2.value

    def __le__(self, other):
        i1, i2 = self.__scale_to_si(other)
        return i1.value <= i2.value

    def __add__(self, other):
        i1, i2 = self.__scale_to_si(other)
        new_value = i1.value + i2.value
        new_units = i1.units
        result = self.__class__(new_value, new_units)
        return result

    def __sub__(self, other):
        i1, i2 = self.__scale_to_si(other)
        new_value = i1.value - i2.value
        new_units = i1.units
        result = self.__class__(new_value, new_units)
        return result
