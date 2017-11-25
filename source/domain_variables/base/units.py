

class Unit:

    def __repr__(self):
        return '{}'.format(self.__class__.__name__)

    def __eq__(self, other):
        return bool(self.__class__.__name__ == other.__class__.__name__)
