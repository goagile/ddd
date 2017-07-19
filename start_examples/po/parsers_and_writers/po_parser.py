import codecs

from start_examples.po.config_po_statemachine import waiting_new_line, command_channel
from start_examples.po.msg_model.msg_collection import MsgCollection
from start_examples.po.state_machine_model.controller import Controller
from start_examples.po.state_machine_model.state_machine import StateMachine


class PoParser:

    @classmethod
    def new(cls):
        return PoParser(cls.__new_controller())

    def __init__(self, controller: Controller):
        self.__controller = controller

    def parse_file(self, path) -> MsgCollection:
        lines = self.__read_lines(path)
        result = self.parse_lines(lines)
        return result

    def parse_lines(self, lines):
        for line in lines:
            if line.startswith('\n') or line.startswith('\r'):
                self.__controller.handle('new_line_finded', line)

            elif line.startswith('#:'):
                self.__controller.handle('paths_finded', line)

            elif line.startswith('msgid_plural'):
                self.__controller.handle('msgid_plural_finded', line)

            elif line.startswith('msgid'):
                self.__controller.handle('msgid_finded', line)

            elif line.startswith('msgstr[0]'):
                self.__controller.handle('msgstr_0_finded', line)

            elif line.startswith('msgstr[1]'):
                self.__controller.handle('msgstr_1_finded', line)

            elif line.startswith('msgstr[2]'):
                self.__controller.handle('msgstr_2_finded', line)

            elif line.startswith('msgstr'):
                self.__controller.handle('msgstr_finded', line)

            else:
                continue

        result = self.__controller.msg_collection
        self.__ignore_empty_and_current(result)

        return result

    @classmethod
    def __ignore_empty_and_current(cls, result):
        if result.has_msg('Current'):
            result.remove_msg('Current')
        for msg in result:
            if msg.is_id_empty:
                result.remove_msg(msg.id)

    @classmethod
    def __new_controller(cls):
        return Controller(
            StateMachine(waiting_new_line),
            command_channel,
            MsgCollection()
        )

    def __read_lines(self, path) -> list:
        with codecs.open(path, "r", "utf-8") as file:
            return file.readlines()
