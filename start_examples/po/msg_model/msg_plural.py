from start_examples.po.msg_model.msg import Msg


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
