

class State:

    def __init__(self):
        self.name = self.__class__.__name__

    def __eq__(self, other):
        return bool(self.name == other.name)


class Locked(State):
    pass


class Unlocked(State):
    pass
