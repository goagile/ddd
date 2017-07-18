import unittest

from nilsson.start_examples.po.msg_model.msg_collection import MsgCollection
from nilsson.start_examples.po.writer.po_writer import PoWriter


class TestParser(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.writer = PoWriter.new()

    def test_write_path_line(self):
        expected = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgstr "Ящик"',
        ]
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик', paths=['../path/to/file.js:300'])

        result = self.writer.write_lines(msg_collection)

        self.assertEqual(expected, result)

    def test_write_many_paths_line(self):
        expected = [
            '\n',
            '#: ../path/to/file.js:300',
            '#: ../path/to/file.js:500',
            'msgid "Box"',
            'msgstr "Ящик"',
        ]
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Box', str='Ящик', paths=['../path/to/file.js:300', '../path/to/file.js:500'])

        result = self.writer.write_lines(msg_collection)

        self.assertEqual(expected, result)

    def test_parse_plural_0(self):
        expected = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgid_plural "Boxes"',
            'msgstr[0] "Ящик"'
        ]
        msg_collection = MsgCollection()
        msg_collection.add_msg_plural(id='Box', id_plural='Boxes', strs=['Ящик'], paths=['../path/to/file.js:300'])

        result = self.writer.write_lines(msg_collection)

        self.assertEqual(expected, result)

    def test_parse_plurals(self):
        expected = [
            '\n',
            '#: ../path/to/file.js:300',
            'msgid "Box"',
            'msgid_plural "Boxes"',
            'msgstr[0] "Ящик"',
            'msgstr[1] "Ящика"',
            'msgstr[2] "Ящиков"',
        ]
        msg_collection = MsgCollection()
        msg_collection.add_msg_plural(id='Box', id_plural='Boxes', strs=[
            'Ящик',
            'Ящика',
            'Ящиков'
        ], paths=['../path/to/file.js:300'])

        result = self.writer.write_lines(msg_collection)

        self.assertEqual(expected, result)

    #
    # def test_parse_single_and_plurals(self):
    #     expected = MsgCollection()
    #     expected.add_msg(id='Fox', str='Лиса', paths=['../path/to/file.js:10'])
    #     expected.add_msg_plural(id='Box', id_plural='Boxes', strs=['Ящик', 'Ящика'], paths=['../path/to/file.js:300'])
    #     lines = [
    #         'TRASH',
    #
    #         '\n',
    #         '#: ../path/to/file.js:10',
    #         'msgid "Fox"',
    #         'msgstr "Лиса"',
    #
    #         '\n',
    #         '#: ../path/to/file.js:300',
    #         'msgid "Box"',
    #         'msgid_plural "Boxes"',
    #         'msgstr[0] "Ящик"',
    #         'msgstr[1] "Ящика"',
    #
    #         'TRASH',
    #
    #     ]
    #     self.parser.parse_lines(lines)
    #
    #     result = self.parser.msg_collection
    #
    #     self.assertEqual(expected, result)
