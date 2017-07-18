

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

    def __repr__(self):
        result = 'MsgCollection: ['
        for m in self.msgs:
            result += str(m)
        result += ']'
        return result

    def __eq__(self, other):
        other_msgs = [m for m in other.msgs]
        msgs = zip(self.__msgs, other_msgs)
        return all(s == o for s, o in msgs)

    @property
    def msgs(self):
        return iter(self.__msgs)

    def add_msg(self, id, str='', paths=None):
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

    def add_str_to(self, id, str):
        msg = self.get_msg(id)
        msg.str = str

    def add_path_to(self, id, path):
        msg = self.get_msg(id)
        msg.add_path(path)

    def has_msg(self, id):
        return bool(self.get_msg(id))

    def remove_msg(self, id):
        msg = self.get_msg(id)
        if msg:
            self.__msgs.remove(msg)
