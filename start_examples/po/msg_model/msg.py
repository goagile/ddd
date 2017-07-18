

class Msg:

    def __init__(self, id, str='', paths=None):
        self.__is_plural = False
        self.str = str
        self.__id = id
        self.__paths = [] if not paths else paths

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.__dict__)

    def __eq__(self, other):
        if not isinstance(other, Msg):
            return False
        return all([
            self.id == other.id,
            self.str == other.str
        ])

    @property
    def is_plural(self):
        return self.__is_plural

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def add_path(self, path: str):
        self.__paths.append(path)

    @property
    def paths(self):
        return iter(self.__paths)
