

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
        return all([
            self.name == other.name,
            self.value == other.value,
            self.units == other.units
        ])

    def equal(self, other, delta=0.01):
        return all([
            self.name == other.name,
            self.__are_values_equal(other, delta),
            self.units == other.units
        ])

    def __are_values_equal(self, other, delta):
        x = abs(self.value - other.value)
        return bool(x <= delta)
