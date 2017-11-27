

class BaseUnit:

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def __eq__(self, other):
        return bool(self.__class__.__name__ == other.__class__.__name__)


class UnitsScaleResults:

    def __init__(self, new_value, new_units):
        self.new_value = new_value
        self.new_units = new_units
