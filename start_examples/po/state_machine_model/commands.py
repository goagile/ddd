from start_examples.po.msg_model.msg_collection import MsgCollection


class ParsePathCommand:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection):
        path = line.strip().split('#:')[1].strip()
        if not msg_collection.current_msg:
            msg_collection.create_current_msg()
        msg_collection.add_path_to_current_msg(path)


class ParseIdCommand:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection: MsgCollection):
        new_id = line.split('msgid')[1].strip().strip('"')
        if msg_collection.current_msg:
            current = msg_collection.current_msg
            current.id = new_id
            return
        raise ValueError()


class ParseStrCommand:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection: MsgCollection):
        new_str = line.split('msgstr')[1].strip().strip('"')
        if msg_collection.current_msg:
            current = msg_collection.current_msg
            current.str = new_str
            return
        raise ValueError()
