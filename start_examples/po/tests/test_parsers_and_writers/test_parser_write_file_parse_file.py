import os
import unittest

from start_examples.po.msg_model.msg_collection import MsgCollection
from start_examples.po.parsers_and_writers.po_parser import PoParser
from start_examples.po.parsers_and_writers.po_writer import PoWriter

path = os.path.join(
    'start_examples',
    'po',
    'tests',
    'generated',
    'parsed_po.po'
)


class TestParserWriteFileParseFile(unittest.TestCase):

    maxDiff = None

    def test_write_file_parse_file_(self):
        msg_collection = MsgCollection()
        msg_collection.add_msg(id='Fax', str='Факс', paths=[
            '../path.js:12'
        ])
        msg_collection.add_msg_plural(id='Box', id_plural='Boxes', strs=[
            'Ящик', 'Ящика'
        ], paths=[
            '../path.js:20'
        ])
        msg_collection.add_msg_plural(id='Fox', id_plural='Foxes', strs=[
            'Лиса', 'Лис'
        ], paths=[
            '../path.js:30'
        ])

        PoWriter.new().write_file(path, msg_collection)
        parsed_msg_collection = PoParser.new().parse_file(path)

        self.assertEqual(msg_collection, parsed_msg_collection)
