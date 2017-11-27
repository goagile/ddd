from domain_variables.base.current import CurrentValue
from domain_variables.current.units import Units


class Ikz(CurrentValue):

    def __init__(self, value, units=Units.A):
        super().__init__(
            value=value,
            name='Ikz',
            label='Iкз',
            units=units,
            description='Ток короткого замыкания',
            fpointdigits=2)


class Ied(CurrentValue):

    def __init__(self, value, units=Units.A):
        super().__init__(
            value=value,
            name='Ied',
            label='Iэд',
            units=units,
            description='Ток двигателей',
            fpointdigits=2)


registry_of_currents = {
    'Ikz': Ikz,
    'Ied': Ied
}
