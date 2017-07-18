from nilsson.start_examples.po.msg_model.msg_collection import MsgCollection


class CreateCurrentMsg:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection):
        msg_collection.create_current_msg()


class ParseMsgPath:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection):
        paths_str = line.split('#:')[1].strip()
        paths = paths_str.split()
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


class ParseMsgIdPlural:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection: MsgCollection):
        msgid_plural = line.split('msgid_plural')[1].strip().strip('"')
        if msg_collection.current_msg:
            current_id = msg_collection.current_msg.id
            current_paths = msg_collection.current_msg.paths
            msg_collection.remove_msg(current_id)
            msg_collection.add_msg_plural(id=current_id, id_plural=msgid_plural, strs=[], paths=current_paths)
            msg_collection.current_msg = msg_collection.get_msg(id=current_id)
            return
        raise ValueError()


class ParseMsgStr0:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection: MsgCollection):
        msgstr_0 = line.split('msgstr[0]')[1].strip().strip('"')
        if msg_collection.current_msg:
            current_id = msg_collection.current_msg.id
            msg = msg_collection.get_msg(current_id)
            msg.add_str(msgstr_0)
            return
        raise ValueError()


class ParseMsgStr1:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection: MsgCollection):
        msgstr_1 = line.split('msgstr[1]')[1].strip().strip('"')
        if msg_collection.current_msg:
            current_id = msg_collection.current_msg.id
            msg = msg_collection.get_msg(current_id)
            msg.add_str(msgstr_1)
            return
        raise ValueError()


class ParseMsgStr2:

    def __init__(self, name):
        self.name = name

    def execute(self, line, msg_collection: MsgCollection):
        msgstr_1 = line.split('msgstr[2]')[1].strip().strip('"')
        if msg_collection.current_msg:
            current_id = msg_collection.current_msg.id
            msg = msg_collection.get_msg(current_id)
            msg.add_str(msgstr_1)
            return
        raise ValueError()
