from domain_variables.base.scalar_current_value import ScalarCurrentValue
from domain_variables.current.units import Units


class Ikz(ScalarCurrentValue):

    def __init__(self, value, units=Units.A):
        super().__init__(
            value=value,
            name='Ikz',
            label='Iкз',
            units=units,
            description='Ток короткого замыкания',
            fpointdigits=2)


class Ied(ScalarCurrentValue):

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
