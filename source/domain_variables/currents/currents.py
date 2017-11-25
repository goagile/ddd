from domain_variables.base.value import DomainValue
from domain_variables.currents.currents_units import Units


class Ikz(DomainValue):

    def __init__(self, value, units=Units.A):
        super().__init__(
            value=value,
            name='Ikz',
            label='Iкз',
            units=units,
            path='x:I:z',
            description='Ток короткого замыкания')

    def scale(self, func):
        translation = func(self.value)
        result = Ikz(translation.new_value, translation.new_units)
        return result

    def __add__(self, other):
        i1 = self.scale(self.units.A)
        i2 = other.scale(other.units.A)
        new_value = i1.value + i2.value
        new_units = i1.units
        result = Ikz(new_value, new_units)
        return result
