from nilsson.start_examples.po.config_po_states import waiting_new_line, command_channel
from nilsson.start_examples.po.msg_model.msg_collection import MsgCollection
from nilsson.start_examples.po.state_machine_model.controller import Controller
from nilsson.start_examples.po.state_machine_model.state_machine import StateMachine


class PoParser:

    def __init__(self, controller):
        self.controller = controller

    @staticmethod
    def new():
        return PoParser(Controller(
            StateMachine(waiting_new_line),
            command_channel,
            MsgCollection()
        ))

    @property
    def msg_collection(self):
        return self.controller.msg_collection

    def parse_lines(self, lines):
        for line in lines:
            if line.startswith('\n') or line.startswith('\r'):
                self.controller.handle('new_line_finded', line)

            elif line.startswith('#:'):
                self.controller.handle('paths_finded', line)

            elif line.startswith('msgid_plural'):
                self.controller.handle('msgid_plural_finded', line)

            elif line.startswith('msgid'):
                self.controller.handle('msgid_finded', line)

            elif line.startswith('msgstr[0]'):
                self.controller.handle('msgstr_0_finded', line)

            elif line.startswith('msgstr[1]'):
                self.controller.handle('msgstr_1_finded', line)

            elif line.startswith('msgstr[2]'):
                self.controller.handle('msgstr_2_finded', line)

            elif line.startswith('msgstr'):
                self.controller.handle('msgstr_finded', line)

            else:
                continue
