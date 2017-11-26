EQUALITY_DELTA = 0.000001


class DomainValue:

    def __init__(self, value, name, label, units, path, description):
        self.__value = value
        self.__name = name
        self.__label = label
        self.__units = units
        self.__path = path
        self.__description = description

    def __repr__(self):
        return '{}={}, {}'.format(self.__label, self.__value, self.__units)

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def units(self):
        return self.__units

    def __float__(self):
        return float(self.__value)

    def __round__(self, n=None):
        return round(self.__value, n)

    def __int__(self):
        return int(self.__value)

    def __eq__(self, other):
        return self.equal(other, delta=EQUALITY_DELTA)

    def equal(self, other, delta=EQUALITY_DELTA):
        return all([
            # self.name == other.name,
            self.are_values_equal(self.value, other.value, delta),
            # self.units == other.units
        ])

    def are_values_equal(self, v1, v2, delta):
        x = abs(v1 - v2)
        return bool(x <= delta)
