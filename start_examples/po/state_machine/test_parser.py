import unittest

from nilsson.start_examples.po.state_machine import waiting_new_line
from nilsson.start_examples.po.state_machine.model import StateMachine, Controller, PrintCommand


class TestParser(unittest.TestCase):

    def setUp(self):
        command_channel = {
            'print': PrintCommand('print')
        }
        machine = StateMachine(waiting_new_line)
        controller = Controller(machine, command_channel)
        self.parser = PoParser(controller)

    def test_parse_lines(self):
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgstr "Ящик"'
        ]

        self.parser.parse(lines)


class PoParser:

    def __init__(self, controller):
        self.controller = controller

    def parse(self, lines):
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
