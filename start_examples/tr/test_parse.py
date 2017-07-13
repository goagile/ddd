import re
import unittest

from nilsson.start_examples.tr.config import wrapper


class TestTRWrapper(unittest.TestCase):

    def test_insert_tr(self):
        expected = 'var x = [TR("Имя"), TR("Фамилия")]; '
        text = 'var x = ["Имя", "Фамилия"]; '

        result = wrapper.wrap(text)

        self.assertEqual(expected, result)

    def test_insert_tr_2(self):
        expected = r'var x = [";?", TR("Имя, Отчество"), TR("Фамилия по"), ":", "-"]; '
        text = r'var x = [";?", "Имя, Отчество", "Фамилия по", ":", "-"]; '

        result = wrapper.wrap(text)

        self.assertEqual(expected, result)

    def test_comma(self):
        expected = r'[TR("Борщ"), ", ", TR("Щи")]'
        text = r'["Борщ", ", ", "Щи"]'

        result = wrapper.wrap(text)

        self.assertEqual(expected, result)

    def test_new_line(self):
        expected = r'[TR("Борщ"), '", "', TR("Щи")]'
        text = r'["Борщ", '", "', "Щи"]'

        result = wrapper.wrap(text)

        self.assertEqual(expected, result)
