from start_examples.po.msg_model.msg import Msg
from start_examples.po.msg_model.msg_plural import MsgPlural


class MsgCollection:

    def __init__(self):
        self.__msgs = []
        self.current_msg = None

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

    def create_current_msg(self):
        self.add_msg(id='Current')
        self.current_msg = self.get_msg(id='Current')

    def add_path_to_current_msg(self, path):
        if self.current_msg:
            self.current_msg.add_path(path)
