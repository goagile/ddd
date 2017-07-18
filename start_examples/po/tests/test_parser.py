import unittest

from start_examples.po.msg_model.msg_collection import MsgCollection
from start_examples.po.parser.po_parser import PoParser
from start_examples.po.state_machine_model import waiting_new_line, command_channel
from start_examples.po.state_machine_model.controller import Controller
from start_examples.po.state_machine_model.state_machine import StateMachine


class TestParser(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.controller = Controller(
            StateMachine(waiting_new_line),
            command_channel,
            MsgCollection())
        self.parser = PoParser(self.controller)

    def test_parse_path_line(self):
        expected = MsgCollection()
        expected.add_msg(id='Current', str='', paths=['../modules/user/x.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300'
        ]
        self.parser.parse_lines(lines)

        result = self.parser.controller.msg_collection

        self.assertEqual(expected, result)

    def test_parse_id_line(self):
        expected = MsgCollection()
        expected.add_msg(id='Current', str='', paths=['../modules/user/x.js:300'])
        expected.add_msg(id='Box', str='', paths=['../modules/user/x.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"'
        ]
        self.parser.parse_lines(lines)

        result = self.parser.controller.msg_collection

        self.assertEqual(expected, result)

    # def test_parse_str_line(self):
    #     expected = MsgCollection()
    #     expected.add_msg(id='Current', str='Ящик', paths=['../modules/user/x.js:300'])
    #     lines = [
    #         '\n',
    #         '#: ../path/to/file.js:300',
    #         'msgid "Box"',
    #         'msgstr "Ящик"'
    #     ]
    #     self.parser.parse_lines(lines)
    #
    #     result = self.parser.controller.msg_collection
    #
    #     self.assertEqual(expected, result)
