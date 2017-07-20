import unittest

from start_examples.po.msg_model.msg_collection import MsgCollection
from start_examples.po.parsers_and_writers.po_parser import PoParser


class TestParser(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.parser = PoParser.new()

    def test_parse_path_line(self):
        expected = MsgCollection()
        expected.add_msg(id='Current', str='', paths=['../path/to/file.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300'
        ]

        result = self.parser.parse_lines(lines)

        self.assertEqual(expected, result)

    def test_parse_id_line(self):
        expected = MsgCollection()
        expected.add_msg(id='Box', str='', paths=['../path/to/file.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"'
        ]

        result = self.parser.parse_lines(lines)

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

        result = self.parser.parse_lines(lines)

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

        result = self.parser.parse_lines(lines)

        self.assertEqual(expected, result)

    def test_parse_plural_0(self):
        expected = MsgCollection()
        expected.add_msg_plural(id='Box', id_plural='Boxes', strs=['Ящик'], paths=['../path/to/file.js:300'])
        lines = [
            'TRASH',

            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgid_plural "Boxes"',
            'msgstr[0] "Ящик"'
        ]

        result = self.parser.parse_lines(lines)

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

        result = self.parser.parse_lines(lines)

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

        result = self.parser.parse_lines(lines)

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

        result = self.parser.parse_lines(lines)

        self.assertEqual(expected, result)

    @unittest.skip('not needed')
    def test_duplicates(self):
        expected = MsgCollection()
        expected.add_msg(id='Box', str='Ящик', paths=['../path/to/file.js:300'])
        lines = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgstr "Ящик"'

            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgid_plural "Boxes"',
            'msgstr[0] "Ящик"',
        ]

        result = self.parser.parse_lines(lines)

        self.assertEqual(expected, result)
