from domain_variables.base.current import CurrentValue
from domain_variables.current.units import Units


class Ikz(CurrentValue):

    def __init__(self, value, units=Units.A):
        super().__init__(
            value=value,
            name='Ikz',
            label='Iкз',
            units=units,
            path='x:I:z',
            description='Ток короткого замыкания',
            fpointdigits=2)
