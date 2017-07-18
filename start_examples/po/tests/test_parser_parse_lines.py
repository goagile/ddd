import unittest

from start_examples.po.msg_model.msg_collection import MsgCollection
from start_examples.po.parser.po_parser import PoParser
from start_examples.po.config_po_states import waiting_new_line, command_channel
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
        expected.add_msg(id='Current', str='', paths=['../path/to/file.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300'
        ]
        self.parser.parse_lines(lines)

        result = self.parser.msg_collection

        self.assertEqual(expected, result)

    def test_parse_id_line(self):
        expected = MsgCollection()
        expected.add_msg(id='Box', str='', paths=['../path/to/file.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"'
        ]
        self.parser.parse_lines(lines)

        result = self.parser.msg_collection

        self.assertEqual(expected, result)

    def test_parse_str_line(self):
        expected = MsgCollection()
        expected.add_msg(id='Box', str='Ящик', paths=['../path/to/file.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgstr "Ящик"'
        ]
        self.parser.parse_lines(lines)

        result = self.parser.msg_collection

        self.assertEqual(expected, result)

    def test_parse_lines_with_2x_paths(self):
        expected = MsgCollection()
        expected.add_msg(id='Box', str='Ящик', paths=[
            '../path/to/file.js:300',
            '../path/to/file.js:500',
            '../path/to/file.js:510'
        ])
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            '#: ../path/to/file.js:500 ../path/to/file.js:510',
            'msgid "Box"',
            'msgstr "Ящик"'
        ]
        self.parser.parse_lines(lines)

        result = self.parser.msg_collection

        self.assertEqual(expected, result)

    def test_parse_plural_0(self):
        expected = MsgCollection()
        expected.add_msg_plural(id='Box', id_plural='Boxes', strs=['Ящик'], paths=['../path/to/file.js:300'])
        lines = [
            'AAAAAAA',
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgid_plural "Boxes"',
            'msgstr[0] "Ящик"'
        ]
        self.parser.parse_lines(lines)

        result = self.parser.msg_collection

        self.assertEqual(expected, result)

    def test_parse_plural_1(self):
        expected = MsgCollection()
        expected.add_msg_plural(id='Box', id_plural='Boxes', strs=[
            'Ящик',
            'Ящика'
        ], paths=['../path/to/file.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgid_plural "Boxes"',
            'msgstr[0] "Ящик"',
            'msgstr[1] "Ящика"'

        ]
        self.parser.parse_lines(lines)

        result = self.parser.msg_collection

        self.assertEqual(expected, result)

    def test_parse_plural_2(self):
        expected = MsgCollection()
        expected.add_msg_plural(id='Box', id_plural='Boxes', strs=[
            'Ящик',
            'Ящика',
            'Ящиков'
        ], paths=['../path/to/file.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgid_plural "Boxes"',
            'msgstr[0] "Ящик"',
            'msgstr[1] "Ящика"',
            'msgstr[2] "Ящиков"',

        ]
        self.parser.parse_lines(lines)

        result = self.parser.msg_collection

        self.assertEqual(expected, result)

    def test_parse_single_and_plurals(self):
        expected = MsgCollection()
        expected.add_msg(id='Fox', str='Лиса', paths=['../path/to/file.js:10'])
        expected.add_msg_plural(id='Box', id_plural='Boxes', strs=['Ящик', 'Ящика'], paths=['../path/to/file.js:300'])
        lines = [
            'TRASH',

            '\n',
            '#: ../path/to/file.js:10',
            'msgid "Fox"',
            'msgstr "Лиса"',

            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgid_plural "Boxes"',
            'msgstr[0] "Ящик"',
            'msgstr[1] "Ящика"',

            'TRASH',

        ]
        self.parser.parse_lines(lines)

        result = self.parser.msg_collection

        self.assertEqual(expected, result)
