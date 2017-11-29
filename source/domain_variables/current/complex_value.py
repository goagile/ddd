from domain_variables.base.scalar_current_value import ScalarCurrentValue
from domain_variables.current.units import Units


class Ic(ScalarCurrentValue):

    def __init__(self, re, im, units=Units.A):
        super().__init__(
            value=re,
            name='Ic',
            label='Ic',
            units=units,
            description='Ток комплексный',
            fpointdigits=2)
        self.im = im

    @classmethod
    def from_rect(cls, re, im):
        return cls(re, im)
