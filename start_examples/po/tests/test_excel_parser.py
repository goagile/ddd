import unittest

from start_examples.po.parser.excel_parser import RuEnExcelParser


class TestExcelParser(unittest.TestCase):

    def test_split_ids_by_new_line__1_slash_n(self):
        expected = [
            'Fax',
            ''
        ]
        ids = (
            'Fax'
        )

        result = RuEnExcelParser._split_plural_ids_by_new_line(ids)

        self.assertEqual(expected, result)

    def test_split_ids_by_new_line(self):
        expected = [
            'Fax',
            'Faxes'
        ]
        ids = (
            'Fax\n\n\n\n'
            '\n\n\n\rFaxes\n'
        )

        result = RuEnExcelParser._split_by_new_line(ids)

        self.assertEqual(expected, result)
