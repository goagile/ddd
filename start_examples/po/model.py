

class Msg:

    def __init__(self, id):
        self.__is_plural = False
        self.str = ''
        self.__id = id
        self.__paths = []

    @property
    def is_plural(self):
        return self.__is_plural

    @property
    def id(self):
        return self.__id

    def add_path(self, path: str):
        self.__paths.append(path)

    @property
    def paths(self):
        return iter(self.__paths)


class MsgPlural(Msg):

    def __init__(self, id, id_plural=''):
        super().__init__(id)
        self.__is_plural = True
        self.__strs = []
        self.__id_plural = id_plural

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


class MsgCollection:

    def __init__(self):
        self.__msgs = []

    def add_msg(self, id, str):
        msg = Msg(id)
        msg.str = str
        self.__msgs.append(msg)

    @property
    def count(self):
        return len(self.__msgs)

    def get_msg(self, id):
        for msg in self.__msgs:
            if msg.id == id:
                return msg
        return None
