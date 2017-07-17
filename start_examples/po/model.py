

class Msg:

    def __init__(self, id):
        self.str = ''
        self.__id = id
        self.__paths = []

    @property
    def id(self):
        return self.__id

    def add_path(self, path: str):
        self.__paths.append(path)

    @property
    def paths(self):
        return iter(self.__paths)
