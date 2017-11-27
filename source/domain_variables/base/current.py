from domain_variables.base.value import DomainValue, EQUALITY_DELTA
from domain_variables.current.units import Units

WRONG_MUL_OPERAND = 'Wrong mul operand'


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
        result = self._new_result(new_value, new_units)
        return result

    def __sub__(self, other):
        i1, i2 = self.__scale_to_si(other)
        new_value = i1.value - i2.value
        new_units = i1.units
        result = self._new_result(new_value, new_units)
        return result

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            result = self._mul_scalar(other)
        elif isinstance(other, CurrentValue):
            result = self._mul_current(other)
        else:
            raise TypeError("'{}' {}".format(other, WRONG_MUL_OPERAND))
        return result

    # def __matmul__(self, other):
    #     if isinstance(other, float) or isinstance(other, int):
    #         result = self._mul_scalar(other)
    #     elif isinstance(other, CurrentValue):
    #         result = self._mul_current(other)
    #     else:
    #         raise TypeError("'{}' {}".format(other, WRONG_MUL_OPERAND))
    #     return result

    def _mul_scalar(self, other):
        i1 = self.scale(self.units.A)
        new_value = i1.value * other
        new_units = i1.units
        result = self.__class__(new_value, new_units)
        return result

    def _mul_current(self, other):
        i1, i2 = self.__scale_to_si(other)
        new_value = i1.value * i2.value
        new_units = i1.units
        result = self._new_result(new_value, new_units)
        return result

    def _new_result(self, value, units):
        result = I(value, units)
        return result


class I(CurrentValue):
    """ Ток, который получается в результате расчетов """

    def __init__(self, value, units=Units.A):
        super().__init__(
            value=value,
            name='I',
            label='I',
            units=units,
            path='',
            description='Результирующий ток',
            fpointdigits=2)
