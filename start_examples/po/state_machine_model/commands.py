from start_examples.po.msg_model.msg_collection import MsgCollection


class ParsePathCommand:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection):
        path = line.strip().split('#:')[1].strip()
        if not msg_collection.has_msg('Current'):
            msg_collection.add_msg('Current')
        msg_collection.add_path_to('Current', path)


class ParseIdCommand:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection: MsgCollection):
        new_id = line.split('msgid')[1].strip().strip('"')
        if msg_collection.has_msg('Current'):
            current = msg_collection.get_msg('Current')
            msg_collection.add_msg(id=new_id, paths=current.paths)
            return
        raise ValueError()


class ParseStrCommand:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection):
        new_id = line.split('msgstr')[1].strip().strip('"')
        if msg_collection.has_msg('Current'):
            msg = msg_collection.get_msg('Current')
            msg.id = new_id
            return
        raise ValueError()
