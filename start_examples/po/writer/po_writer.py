

class PoWriter:

    @staticmethod
    def new():
        return PoWriter()

    def write_lines(self, msg_collection):
        result = []
        for msg in msg_collection:
            if msg.is_plural:
                self.write_msg_plural_to(result, msg)
            else:
                self.write_msg_to(result, msg)
        return result

    def write_msg_plural_to(self, result, msg):
        self.write_new_line_to(result)
        self.write_paths_to(result, msg.paths)
        self.write_id_to(result, msg.id)
        self.write_id_plural_to(result, msg.id_plural)
        self.write_msg_strs_to(result, msg.strs)

    def write_msg_to(self, result, msg):
        self.write_new_line_to(result)
        self.write_paths_to(result, msg.paths)
        self.write_id_to(result, msg.id)
        self.write_msg_str_to(result, msg.str)

    def write_new_line_to(self, result):
        result.append('\n')

    def write_paths_to(self, result, paths):
        for path in paths:
            result.append('#: {}'.format(path))

    def write_id_to(self, result, id_):
        result.append('msgid "{}"'.format(id_))

    def write_id_plural_to(self, result, id_):
        result.append('msgid_plural "{}"'.format(id_))

    def write_msg_str_to(self, result, str):
        result.append('msgstr "{}"'.format(str))

    def write_msg_strs_to(self, result, strs):
        for i, str in enumerate(strs):
            result.append('msgstr[{}] "{}"'.format(i, str))
