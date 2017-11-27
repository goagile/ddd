EQUALITY_DELTA = 1e-6


class DomainValue:

    def __init__(self, value, name, label, units, description, fpointdigits=2):
        self.__value = value
        self.__name = name
        self.__label = label
        self.__units = units
        self.__description = description
        self.__fpointdigits = fpointdigits

    def __repr__(self):
        value_temp = '{{:.{}f}}'.format(self.__fpointdigits)
        value_str = value_temp.format(self.__value)
        return '{}={}, {}'.format(self.__label, value_str, self.__units)

    @property
    def name(self):
        return self.__name

    @property
    def label(self):
        return self.__label

    @property
    def value(self):
        return self.__value

    @property
    def units(self):
        return self.__units

    @property
    def description(self):
        return self.__description

    @property
    def fpointdigits(self):
        return self.__fpointdigits

    def __float__(self):
        return float(self.__value)

    def __round__(self, n=None):
        return round(self.__value, n)

    def __int__(self):
        return int(self.__value)

    def __eq__(self, other):
        return self.equal(other, delta=EQUALITY_DELTA)

    def equal(self, other, delta=EQUALITY_DELTA):
        return self._are_values_equal(self.value, other.value, delta)

    @classmethod
    def _are_values_equal(cls, v1, v2, delta):
        x = abs(v1 - v2)
        return bool(x <= delta)
