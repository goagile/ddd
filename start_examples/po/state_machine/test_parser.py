import unittest

from start_examples.po.msg.model import MsgCollection
from start_examples.po.state_machine import waiting_new_line, command_channel
from start_examples.po.state_machine.model import StateMachine, Controller


class TestParser(unittest.TestCase):

    def setUp(self):
        self.controller = Controller(
            StateMachine(waiting_new_line),
            command_channel,
            MsgCollection())
        self.parser = PoParser(self.controller)

    def test_parse_lines(self):
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgstr "Ящик"'
        ]

        self.parser.parse_lines(lines)

        for m in self.controller.msg_collection.msgs:
            print(m)


class PoParser:

    def __init__(self, controller):
        self.controller = controller

    def parse_lines(self, lines):
        for line in lines:
            if line == '\n':
                self.controller.handle('new_line_finded', line)
            elif line.startswith('#:'):
                self.controller.handle('paths_finded', line)
            elif line.startswith('msgid'):
                self.controller.handle('msgid_finded', line)
            elif line.startswith('msgstr'):
                self.controller.handle('msgstr_finded', line)
            else:
                raise ValueError('Ошибка чтения po', line)
