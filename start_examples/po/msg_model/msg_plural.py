

class MsgPlural:

    def __init__(self, id, id_plural='', strs=None, paths=None):
        self.__is_plural = True
        self.__strs = [] if not strs else strs
        self.__id_plural = id_plural
        self.__id = id
        self.__paths = [] if not paths else paths

    def __repr__(self):
        return '{}(id={}, id_plural={}, strs={}, paths={})'.format(
            self.__class__.__name__, self.__id, self.__id_plural, self.strs, self.__paths
        )

    def __eq__(self, other):
        if not isinstance(other, MsgPlural):
            return False
        return all([
            self.id == other.id,
            self.__strs == [s for s in other.strs]
        ])

    @property
    def id(self):
        return self.__id

    @property
    def is_plural(self):
        return self.__is_plural

    @property
    def id_plural(self):
        return self.__id_plural

    @property
    def strs(self):
        return self.__strs

    def add_str(self, s):
        self.__strs.append(s)

    @property
    def paths(self):
        return iter(self.__paths)

    def add_path(self, path: str):
        self.__paths.append(path)
