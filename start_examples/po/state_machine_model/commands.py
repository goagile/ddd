from start_examples.po.msg_model.msg_collection import MsgCollection


class ParseMsgPath:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection):
        paths_str = line.strip().split('#:')[1].strip()
        paths = paths_str.split()
        if not msg_collection.current_msg:
            msg_collection.create_current_msg()
        for path in paths:
            msg_collection.add_path_to_current_msg(path)


class ParseMsgId:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection: MsgCollection):
        new_id = line.split('msgid')[1].strip().strip('"')
        if msg_collection.current_msg:
            current = msg_collection.current_msg
            current.id = new_id
            return
        raise ValueError()


class ParseMsgStr:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection: MsgCollection):
        new_str = line.split('msgstr')[1].strip().strip('"')
        if msg_collection.current_msg:
            current = msg_collection.current_msg
            current.str = new_str
            return
        raise ValueError()
