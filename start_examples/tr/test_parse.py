import re
import unittest

from nilsson.start_examples.tr.model import TRWrapper


class TRWrapperConfig:

    special_symbols = r'- :_;.,?!'
    quotes = r'(?:\'|\")'
    tr = r'TR(\1)'
    ru = r'А-Яа-я'

    @property
    def pattern_to_search(self):
        return re.compile(self.wrap_in_quotes(r'[' + self.special_symbols + self.ru + ']+'))

    @property
    def pattern_to_replace(self):
        return self.tr

    @property
    def patterns_to_skip(self):
        return [
            re.compile(self.wrap_in_quotes('['+self.special_symbols+']+')),
            re.compile(self.wrap_in_quotes(', ')),
        ]

    def wrap_in_quotes(self, text):
        return '({}{}{})'.format(self.quotes, text, self.quotes)


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
