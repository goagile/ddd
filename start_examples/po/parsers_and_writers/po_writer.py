import codecs

from start_examples.po.msg_model.msg_collection import MsgCollection


class PoWriter:

    def write_file(self, path, msg_collection: MsgCollection):
        lines = self.write_lines(msg_collection)
        with codecs.open(path, "w", "utf-8") as file:
            for line in lines:
                if line == '\n':
                    line = ''
                file.write(line + '\n')

    @staticmethod
    def new():
        return PoWriter()

    def write_lines(self, msg_collection):
        result = []
        for msg in msg_collection:
            if msg.is_plural:
                self.__write_msg_plural_to(result, msg)
            else:
                self.__write_msg_to(result, msg)
        return result

    def __write_msg_plural_to(self, result, msg):
        self.__write_new_line_to(result)
        self.__write_paths_to(result, msg.paths)
        self.__write_id_to(result, msg.id)
        self.__write_id_plural_to(result, msg.id_plural)
        self.__write_msg_strs_to(result, msg.strs)

    def __write_msg_to(self, result, msg):
        self.__write_new_line_to(result)
        self.__write_paths_to(result, msg.paths)
        self.__write_id_to(result, msg.id)
        self.__write_msg_str_to(result, msg.str)

    def __write_new_line_to(self, result):
        result.append('\n')

    def __write_paths_to(self, result, paths):
        for path in paths:
            result.append('#: {}'.format(path))

    def __write_id_to(self, result, id_):
        result.append('msgid "{}"'.format(id_))

    def __write_id_plural_to(self, result, id_):
        result.append('msgid_plural "{}"'.format(id_))

    def __write_msg_str_to(self, result, str):
        result.append('msgstr "{}"'.format(str))

    def __write_msg_strs_to(self, result, strs):
        for i, str in enumerate(strs):
            result.append('msgstr[{}] "{}"'.format(i, str))
