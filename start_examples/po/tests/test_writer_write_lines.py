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

    def test_write_plural_0(self):
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

    def test_write_plurals(self):
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

    def test_write_many_msgs(self):
        expected = [
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
        ]
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Fox', str='Лиса', paths=['../path/to/file.js:10'])
        msg_collection.add_msg_plural(id='Box', id_plural='Boxes', strs=[
            'Ящик',
            'Ящика'
        ], paths=['../path/to/file.js:300'])

        result = self.writer.write_lines(msg_collection)

        self.assertEqual(expected, result)
