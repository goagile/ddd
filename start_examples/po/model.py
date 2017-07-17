

class Msg:

    def __init__(self, id):
        self.__is_plural = False
        self.str = ''
        self.__id = id
        self.__paths = []

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

    def __eq__(self, other):
        if not isinstance(other, MsgPlural):
            return False
        return all([
            self.id == other.id,
            self.__strs == [s for s in other.strs]
        ])

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

    def __eq__(self, other):
        msgs = zip(self.__msgs, [m for m in other.msgs])
        return all(s == o for s, o in msgs)

    @property
    def msgs(self):
        return iter(self.__msgs)

    def add_msg(self, id, str, paths=None):
        msg = Msg(id)
        msg.str = str
        if paths:
            for path in paths:
                msg.add_path(path)
        self.__msgs.append(msg)

    def add_msg_plural(self, id, id_plural, strs):
        msg = MsgPlural(id, id_plural)
        for s in strs:
            msg.add_str(s)
        self.__msgs.append(msg)

    @property
    def count(self):
        return len(self.__msgs)

    def get_msg(self, id):
        for msg in self.__msgs:
            if msg.id == id:
                return msg
        return None
