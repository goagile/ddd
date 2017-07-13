import re
import unittest

from nilsson.start_examples.tr.model import TRWrapper


class TRWrapperConfig:

    def __init__(self):
        self.QUOTES = r'(?:\'|\")'
        self.SYMBOLS = r'- :_;.,?!'
        self.RU = r'А-Яа-я'

        self.CONST = re.compile(self.wrap_in_quotes(r'['+self.SYMBOLS+self.RU+']+'))
        self.TR = r'TR(\1)'

    def ignore_patterns(self):
        return [
            re.compile(self.wrap_in_quotes('['+self.SYMBOLS+']+')),
            re.compile(self.wrap_in_quotes(', ')),
        ]

    def wrap_in_quotes(self, text):
        return '({}{}{})'.format(self.QUOTES, text, self.QUOTES)


wrapper = TRWrapper(TRWrapperConfig())


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
