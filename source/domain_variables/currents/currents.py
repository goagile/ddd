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
            description='Ток короткого замыкания'
        )

    def scale(self, scale_func):
        value, new_units = scale_func(self.value)
        result = Ikz(value, units=new_units)
        return result
